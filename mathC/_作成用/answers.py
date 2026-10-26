"""プリント（複素数平面）の 解答を HTML に 書き出す（数式は KaTeX、図は SVG）
使い方: python mathC/_作成用/answers.py mathC/complex   → mathC/complex/解答.html
中身は answers_data.py（プリントの 解答・赤枠コメント を 書き写した もの）。板書から 足した コメントは 追加の 日付つき
数学Ⅲ の math3/_作成用/answers.py を もとに、表（tbl）と 図（fig）を 足した もの
"""
import os, sys, re, json, html
B = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B)
from answers_data import SHEETS
OUT = sys.argv[1]

def tex(t, disp=True):
    return f'<span class="m{" d" if disp else ""}">{html.escape(t)}</span>'

def mixed(s):
    """'文字 $TeX$ 文字' → html。[[…]] は 空らんの 答え（中に $TeX$ を 書いて よい）"""
    s = re.sub(r'\[\[(.*?)\]\]', lambda m: '\x00' + m.group(1) + '\x01', s)
    out = []
    for k, seg in enumerate(re.split(r'\$', s)):
        if k % 2: out.append(tex(seg, False))
        else: out.append(html.escape(seg))
    h = ''.join(out)
    h = h.replace('&lt;small&gt;', '<small>').replace('&lt;/small&gt;', '</small>')   # 見出しの 補足は 小さい 字
    return h.replace('\x00', '<span class="fill">').replace('\x01', '</span>')

def line(s):
    return f'<div class="ln">{mixed(s) if ("$" in s or "[[" in s) else tex(s)}</div>'

def note(n):
    title, lines, add = n
    badge = f'<span class="nadd">追加 {add}</span>' if add else ''
    return f'<div class="note{" add" if add else ""}"><div class="nt">{mixed(title)}{badge}</div>' + ''.join(f'<div>{mixed(l)}</div>' for l in lines) + '</div>'

def item(it):
    q = mixed(it['q'])   # 問の 文は いつも「文字 $TeX$」の まぜ書き
    figs = f'<div class="figs">{"".join(it["figs"])}</div>' if it['figs'] else ''
    return (f'<div class="it"><div class="q"><span class="tag">{it["t"]}</span><span>{q}</span></div>'
            f'<div class="ans">{"".join(line(l) for l in it["a"])}</div>{figs}{"".join(note(n) for n in it["notes"])}</div>')

def block(b):
    kind = b[0]
    if kind == 'box':      # ('box', 名前, [行])
        _, name, lines = b
        return f'<div class="box"><div class="bl">{mixed(name)}</div><div class="bc">{"".join(f"<div>{mixed(l)}</div>" for l in lines)}</div></div>'
    if kind == 'text':     # ('text', 見出し or None, [行])
        _, name, lines = b
        return (f'<h3>{mixed(name)}</h3>' if name else '') + f'<div class="tx">{"".join(f"<div>{mixed(l)}</div>" for l in lines)}</div>'
    if kind == 'tbl':      # ('tbl', 見出し or None, [見出しの 行], [[マス, …], …])
        _, name, head, rows = b
        cells = ''.join(f'<div class="th">{mixed(c)}</div>' for c in head) + ''.join(f'<div>{mixed(c)}</div>' for r in rows for c in r)
        return (f'<h3>{mixed(name)}</h3>' if name else '') + f'<div class="tb" style="grid-template-columns:repeat({len(head)},auto)">{cells}</div>'
    if kind == 'group':    # ('group', 見出し, 小さい 文, [問])
        _, name, sub, items = b
        return f'<h3>{mixed(name)}　<small>{mixed(sub)}</small></h3><div class="grid">{"".join(item(x) for x in items)}</div>'
    if kind == 'note':     # ('note', 題, [行], 追加の日)
        return note(b[1:])
    raise ValueError(kind)

secs, toc = [], []
for i, s in enumerate(SHEETS):
    sid = f's{i+1}'
    toc.append(f'<a href="#{sid}"><b>{s["no"]}</b>{mixed(s["title"])}</a>')
    h = f'<section id="{sid}"><h2><span class="no">{s["no"]}</span><span class="tt">{mixed(s["title"])}</span><a class="up" href="#top">↑ 目次</a></h2>'
    secs.append(h + ''.join(block(b) for b in s['blocks']) + '</section>')

V = json.load(open(os.path.join(B, 'versions.json'), encoding='utf-8')).get('解答', {'v': '1.0', 'date': ''})
tpl = open(os.path.join(B, 'answers.html'), encoding='utf-8').read()
out = tpl.replace('{{TOC}}', ''.join(toc)).replace('{{BODY}}', ''.join(secs)).replace('{{VER}}', f'ver {V["v"]}　{V["date"]}')
open(os.path.join(OUT, '解答.html'), 'w', encoding='utf-8').write(out)
print('ok', len(SHEETS), 'プリント')
