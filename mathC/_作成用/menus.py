"""数学C の 目次ページを作る（数学Ⅰ の _作成用/menus.py とは 別もの）
使い方: python mathC/_作成用/menus.py mathC
カードを足すときは、下の items に足して もう一度 実行する
"""
import os, sys, json
B = os.path.dirname(os.path.abspath(__file__))
ROOT = sys.argv[1]
tpl = open(os.path.join(B, 'menu.html'), encoding='utf-8').read()

def make(path, title, back_href, back_label, kicker, h1, lead, items):
    # スマホが 古い スライドを 覚えて いても、新しい 版が 出るように リンクに ?v=バージョン を つける
    try: VERS = json.load(open(os.path.join(B, 'versions.json'), encoding='utf-8'))
    except Exception: VERS = {}
    items = [dict(it, href=it['href'] + ('?v=' + VERS[it['href'][:-5]]['v'] + '_' + VERS[it['href'][:-5]]['date'] if it['href'].endswith('.html') and it['href'][:-5] in VERS else '')) for it in items]
    # back_href が None のときは「戻る」リンクを 出さない（数学C の トップは 数学Ⅰ の トップに つなげない）
    back = f'<a class="toplink" href="{back_href}">← {back_label}</a><br>' if back_href else ''
    h = (tpl.replace('{{TITLE}}', title).replace('{{BACK}}', back).replace('{{KICKER}}', kicker)
            .replace('{{H1}}', h1).replace('{{LEAD}}', lead)
            .replace('{{ITEMS}}', json.dumps(items, ensure_ascii=False, indent=1)))
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(h)
    print('ok', path)

# 数学C の トップ（単元ごとの カード）
make('index.html', '数学C 解説スライド', None, None,
     '数学C', '解説スライド', '単元を選んでください', [
  {'href':'complex/index.html', 'no':'複素数平面', 'title':'複素数平面', 'desc':'①-1〜③-3　点・極形式・積と回転・ド・モアブル'},
])

# 複素数平面（スライドが できたら ここに 足す。no は プリントと 同じ「①-1」）
make('complex/index.html', '複素数平面 解説スライド', '../index.html', '数学C の トップへ',
     '数学C　複素数平面', '解説スライド', '単元を選んでください', [
  {'href':'1-1_複素数平面.html', 'no':'①-1', 'title':'複素数平面', 'desc':'複素数を 点で 表す　例・問4・問5'},
  {'href':'1-2_和差実数倍共役.html', 'no':'①-2', 'title':'和・差・実数倍・共役', 'desc':'ベクトルと 同じように 図で 考える　例・練習⑴〜⑷'},
])
