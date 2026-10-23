"""数学Ⅲ の 解説スライドを 作る（数学Ⅰ・数学C の _作成用/ とは 別もの）
使い方: python math3/_作成用/build.py math3/integral
デッキ（スライドの 中身）は decks_integral.py の DECKS に 書く。一覧は menus.py で 作る
"""
import os, sys, json
B = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
sys.path.insert(0, B)
rd = lambda f: open(os.path.join(B, f), encoding='utf-8').read()
from decks_integral import DECKS

head = rd('head.html').replace('{{CSS}}', rd('slide.css'))
VERS = json.load(open(os.path.join(B, 'versions.json'), encoding='utf-8'))
BODY = '<body>\n<div id="stage"></div>\n<div id="bar"></div>\n<div id="ui"></div>\n<div id="jump"></div>\n<script>\n'

def page(name, title, js):
    v = VERS.get(name, {'v': '1.0', 'date': ''})
    ver = f"const VER = 'ver {v['v']}　{v['date']}';\n"
    # 最後の ページの 先（終わりの パネル）で 使う：この 単元の デッキの 並びと 今の デッキ
    ser = [dict(f=n, no=t.split(' ', 1)[0], t=t.split(' ', 1)[-1],
                v=VERS.get(n, {}).get('v', '') + '_' + VERS.get(n, {}).get('date', '')) for n, (t, _) in DECKS.items()]
    ver += f"const SERIES = {json.dumps(ser, ensure_ascii=False)}, ME = {json.dumps(name, ensure_ascii=False)};\n"
    return (head.replace('{{TITLE}}', title) + BODY + ver + rd('parts.js')
            + '\n/* ====== このプリントの スライド ====== */\n' + js + '\n'
            + rd('engine.js') + '\n' + rd('ink.js') + '\n</script>\n</body>\n</html>\n')

only = sys.argv[2:]   # 名前を 書けば その デッキ だけ
os.makedirs(OUT, exist_ok=True)
for name, (title, js) in DECKS.items():
    if only and name not in only: continue
    open(os.path.join(OUT, name + '.html'), 'w', encoding='utf-8').write(page(name, title, js))
    print('ok', name)
