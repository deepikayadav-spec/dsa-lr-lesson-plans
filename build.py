#!/usr/bin/env python3
"""Build the static lesson-plan site.

Reads every course under content/, converts its markdown to HTML, and writes a
static site to dist/ :

    dist/index.html              course picker
    dist/<course-slug>/index.html   reader for that course

Run:  python build.py
Then: vercel deploy --prod     (or push to a Vercel-connected git repo)

Adding a course: make content/<slug>/ , drop a course.json in it, and add
markdown files named session-01-*.md, session-02-*.md, … . Anything else ending
in .md becomes a "Guide". Files starting with _ are ignored.
"""
import glob, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
DIST = os.path.join(ROOT, "dist")

# ============================================================ markdown

def inline(t):
    """Inline spans.

    Code spans are stashed as placeholders BEFORE emphasis runs, so markers that
    span a code span (e.g. **pick `x`:**) still pair up. Restored last, so their
    contents are never treated as markdown.
    """
    spans = []

    def stash(m):
        spans.append(m.group(1))
        return "\x00%d\x00" % (len(spans) - 1)

    t = re.sub(r"`([^`]+)`", stash, t)
    t = html.escape(t)
    # images before links - "![alt](src)" is a superset of the link pattern,
    # and must consume the leading "!" or the link regex leaves it dangling
    t = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)",
               r'<img src="\2" alt="\1" loading="lazy">', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    # twice: an outer *…* wrapping an inner *…* only becomes matchable once the
    # inner pair has already been replaced by <em> tags
    for _ in range(2):
        t = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", t)
    return re.sub(r"\x00(\d+)\x00",
                  lambda m: "<code>%s</code>" % html.escape(spans[int(m.group(1))]), t)


def slugify(txt):
    """Single source of truth for anchor ids — used by the heading renderer and
    by the timeline metadata, so the two can never drift apart."""
    return re.sub(r"[^a-z0-9]+", "-", txt.strip().lower()).strip("-")[:60]


def _cells(row):
    return [c.strip() for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]


def render(md):
    # Source notes about unverified slide placement must stay VISIBLE — they warn
    # the instructor that a block's contents were inferred, not read off the deck.
    # Promote them to a rendered note before comments are stripped.
    md = re.sub(r"<!--\s*(placement:.*?)-->",
                lambda m: "\n\n@@NOTE@@%s\n\n" % m.group(1).strip().rstrip("-").strip(),
                md, flags=re.S | re.I)
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    lines, out, i = md.split("\n"), [], 0

    while i < len(lines):
        ln = lines[i]

        if ln.startswith("```"):                                   # fenced code
            lang, i, buf = ln[3:].strip(), i + 1, []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<pre class="code" data-lang="%s"><code>%s</code></pre>'
                       % (html.escape(lang), html.escape("\n".join(buf))))
            continue

        if ln.strip().startswith("|") and i + 1 < len(lines) and \
                re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):   # table
            head, i, body = _cells(ln), i + 2, []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(_cells(lines[i])); i += 1
            t = ["<div class='tw'><table><thead><tr>"]
            t += ["<th>%s</th>" % inline(c.replace("\\|", "|")) for c in head]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>%s</tr>" % "".join(
                    "<td>%s</td>" % inline(c.replace("\\|", "|")) for c in r))
            out.append("".join(t) + "</tbody></table></div>")
            continue

        if ln.startswith(">"):                                      # blockquote
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].lstrip()); i += 1
            out.append("<blockquote>%s</blockquote>"
                       % "<br>".join(inline(b) for b in buf if b.strip()))
            continue

        m_ul, m_ol = re.match(r"^\s*[-*]\s+(.*)", ln), re.match(r"^\s*\d+\.\s+(.*)", ln)
        if m_ul or m_ol:                                            # lists
            tag = "ul" if m_ul else "ol"
            pat = r"^\s*[-*]\s+(.*)" if m_ul else r"^\s*\d+\.\s+(.*)"
            items = []
            while i < len(lines):
                m = re.match(pat, lines[i])
                if m:
                    items.append(m.group(1)); i += 1
                elif lines[i].startswith("  ") and lines[i].strip() and items:
                    items[-1] += " " + lines[i].strip(); i += 1
                else:
                    break
            out.append("<%s>%s</%s>" % (tag, "".join(
                "<li>%s</li>" % inline(x) for x in items), tag))
            continue

        if re.match(r"^\s*---+\s*$", ln):                           # hr
            out.append("<hr>"); i += 1; continue

        m = re.match(r"^(#{1,4})\s+(.*)", ln)                       # heading
        if m:
            lvl, txt = len(m.group(1)), m.group(2).strip()
            cls = ' class="h-act"' if txt.startswith("⚡") else (
                  ' class="h-warn"' if txt.startswith("⚠️") else "")
            out.append('<h%d id="%s"%s>%s</h%d>'
                       % (lvl, slugify(txt), cls, inline(txt), lvl))
            i += 1; continue

        if ln.startswith("@@NOTE@@"):                               # source caveat
            out.append('<p class="caveat">%s</p>' % inline(ln[8:].strip()))
            i += 1; continue

        if ln.strip():                                              # paragraph
            buf = [ln]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(
                    r"^(#{1,4}\s|```|>|\s*[-*]\s|\s*\d+\.\s|\s*---+\s*$)", lines[i]) \
                    and not lines[i].strip().startswith("|"):
                buf.append(lines[i]); i += 1
            # these documents use single newlines as real line breaks
            # (poll questions, metadata headers), so preserve them
            out.append("<p>%s</p>" % "<br>".join(inline(b.strip()) for b in buf))
            continue

        i += 1

    return "\n".join(out)

# ============================================================ metadata

def doc_meta(path, md):
    base = os.path.basename(path)
    m = re.match(r"session-(\d+)", base)
    num = int(m.group(1)) if m else 0

    h1 = re.search(r"^#\s+(.*)", md, re.M)
    title = h1.group(1).strip() if h1 else base
    title = re.sub(r"^Session\s+\d+\s*[—-]\s*", "", title).strip()

    kind = "Concept"
    tm = re.search(r"\*\*Session type\*\*\s*(.+)", md)
    if tm and "support" in tm.group(1).lower():
        kind = "Support"
    if not num:
        kind = "Guide"

    low = md.lower()
    no_deck = ("no video and no slide deck exist" in low
               or "no deck exists for this session" in low)

    blocks = []
    for h in re.findall(r"^##\s+(.*)$", md, re.M):
        tk = re.search(r"\((\d+)\s*[–-]\s*(\d+)\s*min\)", h)
        if not tk:
            continue
        label = re.sub(r"\s*\(\d+\s*[–-]\s*\d+\s*min\)", "", h).strip()
        label = re.sub(r"\s*—\s*(DELIVER SLIDES AS-IS|BOARD \+ LIVE TYPING)", "", label)
        short = re.sub(r"^⚡\s*", "", label)
        short = re.sub(r"^Activity \d+\s*[—-]\s*", "", short)
        short = re.sub(r":.*$", "", short).strip()
        blocks.append({"start": int(tk.group(1)), "end": int(tk.group(2)),
                       "label": short, "id": slugify(h),
                       "act": label.startswith("⚡")})

    return {"num": num, "title": title, "kind": kind,
            "noDeck": no_deck, "blocks": blocks}


def relink(h):
    """Point cross-document .md links at the reader's own routes."""
    h = re.sub(r'href="\.?/?session-0*(\d+)[^"]*\.md"', r'href="#session-\1"', h)
    h = re.sub(r'href="\.?/?practice-session-playbook\.md"', 'href="#g0"', h)
    h = re.sub(r'href="\.?/?README\.md"', 'href="#g1"', h)
    # internal ops docs are not published — keep the text, drop the link
    return re.sub(r'<a href="\.?/?_[^"]*">(.*?)</a>', r"\1", h)


def section_for(num, sections):
    """Which named sub-section (course.json 'sections': [{label,from,to}]) a
    session number falls into, or None if the course doesn't define any."""
    for s in sections:
        if s["from"] <= num <= s["to"]:
            return s["label"]
    return None


def load_course(folder):
    slug = os.path.basename(folder)
    cfg = json.load(open(os.path.join(folder, "course.json"), encoding="utf-8"))
    sections = cfg.get("sections", [])
    sessions, guides = [], []
    for p in sorted(glob.glob(os.path.join(folder, "*.md"))):
        if os.path.basename(p).startswith("_"):
            continue
        md = open(p, encoding="utf-8").read()
        d = doc_meta(p, md)
        d["html"] = relink(render(md))
        d["hideNum"] = bool(cfg.get("hideSessionNumbers"))
        d["section"] = section_for(d["num"], sections) if d["num"] else None
        (sessions if d["num"] else guides).append(d)
    sessions.sort(key=lambda d: d["num"])
    return {"slug": slug, "name": cfg.get("name", slug),
            "subtitle": cfg.get("subtitle", ""), "order": cfg.get("order", 99),
            "docs": sessions + guides, "count": len(sessions)}

# ============================================================ styles

CSS = """
:root{
  --page:#EFF1F4; --surface:#FFFFFF; --sidebar:#F7F8FA;
  --ink:#171A1F; --muted:#626C7A; --rule:#D9DDE3; --rule2:#E9ECEF;
  --accent:#0F5C8C; --accent-soft:#E4EEF5;
  --act:#B4531A; --act-soft:#FBEDE3;
  --warn:#A8321F; --codebg:#F4F6F8;
}
@media (prefers-color-scheme:dark){:root{
  --page:#0F1216; --surface:#171B21; --sidebar:#13171C;
  --ink:#E3E8EE; --muted:#8D98A6; --rule:#2C333B; --rule2:#222831;
  --accent:#6BAEDC; --accent-soft:#16303F;
  --act:#E39055; --act-soft:#33231A;
  --warn:#F0836F; --codebg:#10141A;
}}
:root[data-theme="dark"]{
  --page:#0F1216; --surface:#171B21; --sidebar:#13171C;
  --ink:#E3E8EE; --muted:#8D98A6; --rule:#2C333B; --rule2:#222831;
  --accent:#6BAEDC; --accent-soft:#16303F;
  --act:#E39055; --act-soft:#33231A;
  --warn:#F0836F; --codebg:#10141A;
}
:root[data-theme="light"]{
  --page:#EFF1F4; --surface:#FFFFFF; --sidebar:#F7F8FA;
  --ink:#171A1F; --muted:#626C7A; --rule:#D9DDE3; --rule2:#E9ECEF;
  --accent:#0F5C8C; --accent-soft:#E4EEF5;
  --act:#B4531A; --act-soft:#FBEDE3;
  --warn:#A8321F; --codebg:#F4F6F8;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--page);color:var(--ink);
 font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
 font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.tools{position:fixed;right:18px;bottom:18px;display:flex;gap:8px;z-index:30}
.tools button,.tools a{background:var(--surface);color:var(--muted);
 border:1px solid var(--rule);border-radius:20px;padding:7px 13px;font:inherit;
 font-size:12.5px;cursor:pointer;text-decoration:none}
.tools button:hover,.tools a:hover{color:var(--ink);border-color:var(--muted)}
"""

READER_CSS = """
.shell{display:flex;min-height:100vh}
.side{width:272px;flex:none;background:var(--sidebar);border-right:1px solid var(--rule);
 position:sticky;top:0;height:100vh;overflow-y:auto;padding:18px 0 40px}
.brand{padding:2px 20px 14px;border-bottom:1px solid var(--rule2);margin-bottom:8px}
.brand a.back{font-size:11.5px;color:var(--muted);text-decoration:none;display:block;
 margin-bottom:7px}
.brand a.back:hover{color:var(--accent)}
.brand h1{font-size:15px;margin:0 0 3px;letter-spacing:-.01em;font-weight:660}
.brand p{margin:0;font-size:12px;color:var(--muted)}
.navsec{font-size:10.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
 color:var(--muted);padding:14px 20px 6px}
a.item{display:flex;gap:10px;align-items:baseline;padding:7px 20px;text-decoration:none;
 color:var(--ink);border-left:3px solid transparent;font-size:14px;line-height:1.35}
a.item:hover{background:var(--rule2)}
a.item.on{background:var(--accent-soft);border-left-color:var(--accent);font-weight:620}
a.item .n{color:var(--muted);font-variant-numeric:tabular-nums;font-size:12px;
 min-width:16px;flex:none;font-weight:600}
a.item.on .n{color:var(--accent)}
a.item .t{flex:1}
.badge{font-size:9.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;
 padding:1px 5px;border-radius:3px;background:var(--rule2);color:var(--muted);
 align-self:center;flex:none}
.badge.sup{background:var(--act-soft);color:var(--act)}
.badge.nd{background:var(--rule2);color:var(--muted)}
.main{flex:1;min-width:0}
.topbar{position:sticky;top:0;z-index:20;background:var(--surface);
 border-bottom:1px solid var(--rule);padding:14px 32px 0}
.topbar h2{margin:0 0 2px;font-size:20px;letter-spacing:-.02em;font-weight:680}
.topbar .sub{font-size:12.5px;color:var(--muted);margin-bottom:12px}
.burger{display:none}
.tl{display:flex;gap:2px;padding-bottom:12px}
.tl a{flex-grow:var(--w);flex-basis:0;text-decoration:none;min-width:0;
 border-top:3px solid var(--rule);padding-top:6px;color:var(--muted);font-size:10.5px;
 line-height:1.2;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
 transition:color .12s,border-color .12s}
.tl a:hover{color:var(--ink);border-top-color:var(--muted)}
.tl a.act{border-top-color:var(--act);color:var(--act)}
.tl a.cur{border-top-color:var(--accent);color:var(--accent);font-weight:700}
.tl a.act.cur{border-top-color:var(--act)}
.tl .mins{display:block;font-variant-numeric:tabular-nums;font-weight:700;font-size:10px}
.doc{padding:34px 32px 120px;max-width:820px}
.doc h1{display:none}
.doc h2{font-size:21px;letter-spacing:-.018em;font-weight:680;margin:44px 0 12px;
 padding-top:14px;border-top:1px solid var(--rule);scroll-margin-top:120px}
.doc h2:first-of-type{border-top:0;margin-top:0;padding-top:0}
.doc h2.h-act{color:var(--act);border-top-color:var(--act)}
.doc h2.h-warn{color:var(--warn)}
.doc h3{font-size:15px;font-weight:680;margin:26px 0 8px;letter-spacing:-.008em;
 scroll-margin-top:120px}
.doc h4{font-size:13.5px;font-weight:680;margin:20px 0 6px;color:var(--muted)}
.doc p{margin:0 0 12px}
.doc img{max-width:100%;height:auto;display:block;border-radius:8px;
 border:1px solid var(--rule2);margin:4px 0 14px}
.doc ul,.doc ol{margin:0 0 14px;padding-left:22px}
.doc li{margin:0 0 5px}
.doc hr{border:0;border-top:1px solid var(--rule2);margin:26px 0}
.doc strong{font-weight:660}
.doc code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
 font-size:.875em;background:var(--codebg);padding:1.5px 5px;border-radius:3px;
 border:1px solid var(--rule2)}
.doc pre.code{background:var(--codebg);border:1px solid var(--rule2);border-radius:7px;
 padding:13px 15px;overflow-x:auto;margin:0 0 14px;line-height:1.5}
.doc pre.code code{background:none;border:0;padding:0;font-size:13.5px}
.doc blockquote{margin:0 0 14px;padding:11px 16px;background:var(--surface);
 border-left:3px solid var(--accent);border-radius:0 6px 6px 0}
.doc .tw{overflow-x:auto;margin:0 0 16px;border:1px solid var(--rule);border-radius:7px}
.doc table{border-collapse:collapse;width:100%;font-size:14px;background:var(--surface)}
.doc th{text-align:left;font-weight:660;font-size:11px;letter-spacing:.06em;
 text-transform:uppercase;color:var(--muted);padding:9px 13px;
 border-bottom:1px solid var(--rule);white-space:nowrap}
.doc td{padding:9px 13px;border-bottom:1px solid var(--rule2);vertical-align:top}
.doc tr:last-child td{border-bottom:0}
.doc td code{white-space:pre-wrap}
.doc p.caveat{font-size:12.5px;color:var(--warn);background:var(--act-soft);
 border:1px dashed var(--warn);border-radius:6px;padding:7px 11px;margin:0 0 14px}
.doc p.caveat::before{content:"⚠ ";font-weight:700}
@media (max-width:880px){
  .side{position:fixed;left:0;top:0;z-index:40;transform:translateX(-100%);
   transition:transform .18s;box-shadow:0 0 40px rgba(0,0,0,.2)}
  .side.open{transform:none}
  .burger{display:inline-block;background:none;border:1px solid var(--rule);
   border-radius:6px;color:var(--ink);font:inherit;font-size:13px;padding:5px 11px;
   cursor:pointer;margin-bottom:10px}
  .topbar,.doc{padding-left:18px;padding-right:18px}
  .tl a{font-size:0}.tl .mins{font-size:9.5px}
}
@media print{.side,.topbar,.tools{display:none}.doc{max-width:none;padding:0}
 body{background:#fff}}
"""

INDEX_CSS = """
.wrap{max-width:760px;margin:0 auto;padding:72px 24px 100px}
header{margin-bottom:38px}
.eyebrow{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
 color:var(--muted);margin:0 0 10px}
h1{font-size:clamp(28px,4.4vw,38px);line-height:1.12;letter-spacing:-.022em;
 font-weight:680;margin:0 0 12px}
.lede{font-size:17px;color:var(--muted);margin:0;max-width:60ch}
.courses{display:flex;flex-direction:column;gap:2px;background:var(--rule2);
 border:1px solid var(--rule2);border-radius:10px;overflow:hidden}
a.course,div.course{display:flex;align-items:baseline;gap:16px;padding:20px 22px;
 background:var(--surface);text-decoration:none;color:var(--ink)}
a.course:hover{background:var(--accent-soft)}
div.course{opacity:.55}
.course .body{flex:1;min-width:0}
.course h2{margin:0 0 3px;font-size:17px;font-weight:660;letter-spacing:-.01em}
.course p{margin:0;font-size:13.5px;color:var(--muted)}
.course .meta{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums;
 white-space:nowrap;flex:none}
.soon{font-size:9.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
 color:var(--muted);border:1px solid var(--rule);border-radius:3px;padding:2px 6px}
footer{margin-top:36px;padding-top:18px;border-top:1px solid var(--rule);
 font-size:13px;color:var(--muted)}
"""

# ============================================================ pages

def page(title, css, body, favicon="📘"):
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>%s</text></svg>">
<style>%s</style>
</head>
<body>
%s
</body>
</html>
""" % (html.escape(title), favicon, css, body)


THEME_JS = """
const root=document.documentElement;
const saved=localStorage.getItem('lp-theme');
if(saved)root.setAttribute('data-theme',saved);
document.getElementById('theme').onclick=()=>{
  const now=root.getAttribute('data-theme')||
    (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
  const next=now==='dark'?'light':'dark';
  root.setAttribute('data-theme',next);
  localStorage.setItem('lp-theme',next);
};
"""

READER_JS = """
const nav=document.getElementById('nav'),doc=document.getElementById('doc'),
      side=document.getElementById('side');
const sessions=DOCS.filter(d=>d.num>0),guides=DOCS.filter(d=>d.num===0);

function link(d){
  const a=document.createElement('a');
  a.className='item';
  a.href='#'+(d.num?'session-'+d.num:'g'+guides.indexOf(d));
  a.dataset.idx=DOCS.indexOf(d);
  a.innerHTML='<span class="n">'+(d.hideNum?'·':(d.num||'·'))+'</span><span class="t">'+d.title+'</span>'
    +(d.kind==='Support'?'<span class="badge sup">Support</span>':'')
    +(d.noDeck?'<span class="badge nd" title="No slide deck — teaching blocks provided instead">No deck</span>':'');
  return a;
}
function section(t){const h=document.createElement('div');h.className='navsec';
  h.textContent=t;nav.appendChild(h);}
if(sessions.length){
  let lastSec=null;
  sessions.forEach(d=>{
    const sec=d.section||'Sessions';
    if(sec!==lastSec){section(sec);lastSec=sec;}
    nav.appendChild(link(d));
  });
}
if(guides.length){section('Guides');guides.forEach(d=>nav.appendChild(link(d)));}

function show(idx){
  const d=DOCS[idx];if(!d)return;
  document.getElementById('ttl').textContent=(d.num&&!d.hideNum?'Session '+d.num+' — ':'')+d.title;
  const bits=[];
  if(d.num)bits.push('60 min');
  if(d.kind!=='Guide')bits.push(d.kind+' session');
  if(d.noDeck)bits.push('no slide deck — teaching blocks provided');
  document.getElementById('sub').textContent=bits.join(' · ');
  const tl=document.getElementById('tl');tl.innerHTML='';
  d.blocks.forEach(b=>{
    const a=document.createElement('a');
    a.href='#'+b.id;a.style.setProperty('--w',b.end-b.start);
    a.className=b.act?'act':'';
    a.title=b.label+'  ('+b.start+'–'+b.end+' min)';
    a.innerHTML='<span class="mins">'+b.start+'</span>'+b.label;
    tl.appendChild(a);
  });
  doc.innerHTML=d.html;
  document.querySelectorAll('a.item').forEach(a=>
    a.classList.toggle('on',+a.dataset.idx===idx));
  window.scrollTo(0,0);side.classList.remove('open');mark();
}
function route(){
  const h=location.hash.slice(1);let idx=0;
  if(h.startsWith('session-')){
    const f=DOCS.findIndex(d=>d.num===+h.split('-')[1]);if(f>-1)idx=f;
  }else if(/^g\\d+$/.test(h)){
    const f=DOCS.indexOf(guides[+h.slice(1)]);if(f>-1)idx=f;
  }else if(h){
    const el=document.getElementById(h);if(el){el.scrollIntoView();return;}
  }
  show(idx);
}
function mark(){
  const links=[...document.querySelectorAll('.tl a')];if(!links.length)return;
  let cur=0;
  links.forEach((a,i)=>{const el=document.getElementById(a.getAttribute('href').slice(1));
    if(el&&el.getBoundingClientRect().top<160)cur=i;});
  links.forEach((a,i)=>a.classList.toggle('cur',i===cur));
}
let tick=false;
addEventListener('scroll',()=>{if(tick)return;tick=true;
  requestAnimationFrame(()=>{mark();tick=false;});},{passive:true});
addEventListener('hashchange',route);
document.getElementById('burger').onclick=()=>side.classList.toggle('open');
route();
"""


def build_reader(course):
    body = """<div class="shell">
  <nav class="side" id="side">
    <div class="brand">
      <a class="back" href="/">← All courses</a>
      <h1>%s</h1><p>%s</p>
    </div>
    <div id="nav"></div>
  </nav>
  <div class="main">
    <div class="topbar">
      <button class="burger" id="burger">☰ Sessions</button>
      <h2 id="ttl"></h2><div class="sub" id="sub"></div>
      <div class="tl" id="tl"></div>
    </div>
    <div class="doc" id="doc"></div>
  </div>
</div>
<div class="tools">
  <button id="theme">◐ Theme</button>
  <button onclick="window.print()">Print</button>
</div>
<script>const DOCS=%s;</script>
<script>%s</script>
<script>%s</script>
""" % (html.escape(course["name"]),
       html.escape(course["subtitle"] or ("%d sessions" % course["count"])),
       json.dumps(course["docs"], ensure_ascii=False), THEME_JS, READER_JS)
    return page("%s — Lesson Plans" % course["name"], CSS + READER_CSS, body)


def build_index(courses):
    rows = []
    for c in courses:
        if c["count"]:
            rows.append(
                '<a class="course" href="/%s/"><div class="body"><h2>%s</h2>'
                '<p>%s</p></div><span class="meta">%d sessions</span></a>'
                % (c["slug"], html.escape(c["name"]), html.escape(c["subtitle"]),
                   c["count"]))
        else:
            rows.append(
                '<div class="course"><div class="body"><h2>%s</h2><p>%s</p></div>'
                '<span class="soon">Not yet added</span></div>'
                % (html.escape(c["name"]), html.escape(c["subtitle"])))

    ready = sum(1 for c in courses if c["count"])
    total = sum(c["count"] for c in courses)
    body = """<div class="wrap">
  <header>
    <p class="eyebrow">Instructor Resources</p>
    <h1>Lesson Plans</h1>
    <p class="lede">Session-by-session plans for live 60-minute classes — warm-up polls,
      slide-block timings, in-class activities, and the real classroom-quiz questions.</p>
  </header>
  <div class="courses">%s</div>
  <footer>%d course%s live · %d sessions planned</footer>
</div>
<div class="tools"><button id="theme">◐ Theme</button></div>
<script>%s</script>
""" % ("".join(rows), ready, "" if ready == 1 else "s", total, THEME_JS)
    return page("Lesson Plans", CSS + INDEX_CSS, body)

# ============================================================ main

def main():
    if not os.path.isdir(CONTENT):
        sys.exit("no content/ directory at %s" % CONTENT)

    courses = []
    for folder in sorted(glob.glob(os.path.join(CONTENT, "*"))):
        if os.path.exists(os.path.join(folder, "course.json")):
            courses.append(load_course(folder))
    courses.sort(key=lambda c: (c["order"], c["name"]))

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(
        build_index(courses))

    for c in courses:
        if not c["count"]:
            print("  %-24s — skipped (no sessions yet)" % c["slug"])
            continue
        d = os.path.join(DIST, c["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
            build_reader(c))
        anchors = sum(len(x["blocks"]) for x in c["docs"])
        print("  %-24s %2d sessions, %d guides, %d timeline blocks"
              % (c["slug"], c["count"], len(c["docs"]) - c["count"], anchors))

    total_kb = sum(os.path.getsize(os.path.join(r, f))
                   for r, _, fs in os.walk(DIST) for f in fs) // 1024
    print("\nbuilt %d course page(s) + index -> dist/  (%d KB)"
          % (sum(1 for c in courses if c["count"]), total_kb))


if __name__ == "__main__":
    main()
