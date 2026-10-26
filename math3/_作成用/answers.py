"""プリント（２学期期末考査まで）の 解答を HTML に 書き出す（数式は KaTeX）
使い方: python math3/_作成用/answers.py math3/integral   → math3/integral/解答.html
中身は answers_data.py（プリントの 解答・赤枠コメント を 書き写した もの）。板書から 足した コメントは 追加の 日付つき
"""
import os, sys, re, json, html
B = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B)
from answers_data import SHEETS
OUT = sys.argv[1]

def tex(t, disp=True):
    return f'<span class="m{" d" if disp else ""}">{html.escape(t)}</span>'

def mixed(s):
    """'文字 $TeX$ 文字' → html。[[…]] は 空らんの 答え"""
    s = re.sub(r'\[\[(.*?)\]\]', lambda m: '\x00' + m.group(1) + '\x01', s)
    out = []
    for k, seg in enumerate(re.split(r'\$', s)):
        if k % 2: out.append(tex(seg, False))
        else: out.append(html.escape(seg))
    h = ''.join(out)
    return h.replace('\x00', '<span class="fill">').replace('\x01', '</span>')

def line(s):
    return f'<div class="ln">{mixed(s) if "$" in s else tex(s)}</div>'

def note(n):
    title, lines, add = n
    badge = f'<span class="nadd">追加 {add}</span>' if add else ''
    return f'<div class="note{" add" if add else ""}"><div class="nt">{mixed(title)}{badge}</div>' + ''.join(f'<div>{mixed(l)}</div>' for l in lines) + '</div>'

def item(it):
    return (f'<div class="it"><div class="q"><span class="tag">{it["t"]}</span>{tex(it["q"])}</div>'
            f'<div class="ans">{"".join(line(l) for l in it["a"])}</div>{"".join(note(n) for n in it["notes"])}</div>')

secs, toc = [], []
for i, s in enumerate(SHEETS):
    sid = f's{i+1}'
    toc.append(f'<a href="#{sid}"><b>{s["no"]}</b>{mixed(s["title"])}</a>')
    h = f'<section id="{sid}"><h2><span class="no">{s["no"]}</span><span class="tt">{mixed(s["title"])}</span><a class="up" href="#top">↑ 目次</a></h2>'
    for name, lines in s.get('boxes', []):
        h += f'<div class="box"><div class="bl">{mixed(name)}</div><div class="bc">{"".join(f"<div>{mixed(l)}</div>" for l in lines)}</div></div>'
    for name, lines in s.get('derive', []):
        h += f'<h3>{html.escape(name)}</h3><div class="der">{"".join(f"<div>{mixed(l)}</div>" for l in lines)}</div>'
    for name, items in s.get('groups', []):
        h += f'<h3>{html.escape(name)}　<small>次の不定積分を求めよ。</small></h3><div class="grid">{"".join(item(x) for x in items)}</div>'
    secs.append(h + '</section>')

V = json.load(open(os.path.join(B, 'versions.json'), encoding='utf-8')).get('解答', {'v': '1.0', 'date': ''})
tpl = open(os.path.join(B, 'answers.html'), encoding='utf-8').read()
out = tpl.replace('{{TOC}}', ''.join(toc)).replace('{{BODY}}', ''.join(secs)).replace('{{VER}}', f'ver {V["v"]}　{V["date"]}')
open(os.path.join(OUT, '解答.html'), 'w', encoding='utf-8').write(out)
print('ok', len(SHEETS), 'プリント')
