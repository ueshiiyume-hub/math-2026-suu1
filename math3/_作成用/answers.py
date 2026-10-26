"""プリントの 解答（docx の 後ろの 解答セクション）を 画像に して、目次つきの HTML を 作る
使い方: python math3/_作成用/answers.py <プリントの PDF> math3/integral
  PDF は Word で「名前を付けて保存 → PDF」した もの（LibreOffice だと 数式の 赤字・枠の 中の 式が 出ない）
  1ページ目から 順に 見て、タイトルに「【解答】」が ある ページから 新しい 節、「【作業記録】」で 終わり
出力: <出力先>/解答.html と <出力先>/kaitou/NN.png
"""
import os, sys, re, subprocess, json, shutil, html
from PIL import Image

PDF, OUT = sys.argv[1], sys.argv[2]
B = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(OUT, 'kaitou')

def page_text(i):
    return subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-layout', PDF, '-'], capture_output=True, text=True).stdout

n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', PDF], capture_output=True, text=True).stdout).group(1))
secs, cur = [], None   # [{no, title, pages:[ページ番号]}]
for i in range(1, n + 1):
    t = page_text(i)
    if '【作業記録】' in t: break
    head = '\n'.join(t.splitlines()[:5])
    m = re.search(r'([①②③④⑤⑥⑦⑧⑨])\s*-\s*(\d+)\s*(.*?)\s*【解答】', head)
    if m:
        title = re.sub(r'\s+', ' ', m.group(3)).strip()
        title = title.replace('x n', 'xⁿ')
        cur = {'no': f'{m.group(1)}-{m.group(2)}', 'title': title, 'pages': []}
        secs.append(cur)
    if cur: cur['pages'].append(i)
assert secs, '【解答】 の ページが 見つからない'

# 画像（色を 減らした PNG：文字が くっきり、軽い）
if os.path.isdir(IMG): shutil.rmtree(IMG)
os.makedirs(IMG)
k = 0
for s in secs:
    s['imgs'] = []
    for p in s['pages']:
        k += 1
        base = os.path.join(IMG, f'{k:02d}')
        subprocess.run(['pdftoppm', '-r', '130', '-png', '-singlefile', '-f', str(p), '-l', str(p), PDF, base], check=True)
        im = Image.open(base + '.png').convert('RGB').quantize(colors=48, method=Image.Quantize.MEDIANCUT)
        im.save(base + '.png', optimize=True)
        s['imgs'].append(f'kaitou/{k:02d}.png')

# HTML（目次 → 節ごとに 画像を 縦に）
VERS = json.load(open(os.path.join(B, 'versions.json'), encoding='utf-8')).get('解答', {'v': '1.0', 'date': ''})
toc = ''.join(f'<a href="#s{i+1}"><b>{s["no"]}</b>{html.escape(s["title"])}</a>' for i, s in enumerate(secs))
body = ''.join(
    f'<section id="s{i+1}"><h2><span class="no">{s["no"]}</span>{html.escape(s["title"])}<a class="up" href="#top">↑ 目次</a></h2>'
    + ''.join(f'<img src="{src}?v={VERS["v"]}" alt="{s["no"]} 解答 {j+1}ページ目" loading="lazy" width="1075" height="1520">' for j, src in enumerate(s['imgs']))
    + '</section>' for i, s in enumerate(secs))
tpl = open(os.path.join(B, 'answers.html'), encoding='utf-8').read()
out = tpl.replace('{{TOC}}', toc).replace('{{BODY}}', body).replace('{{VER}}', f'ver {VERS["v"]}　{VERS["date"]}')
open(os.path.join(OUT, '解答.html'), 'w', encoding='utf-8').write(out)
print('ok', len(secs), '節', k, 'ページ')
for s in secs: print(' ', s['no'], s['title'], s['pages'])
