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
  {'href':'1-3_絶対値.html', 'no':'①-3', 'title':'複素数の絶対値', 'desc':'原点からの 距離　例・練習⑴〜⑶'},
  {'href':'1-4_極形式.html', 'no':'①-4', 'title':'複素数の極形式', 'desc':'長さと 向きで 表す　読み取り・例・くくる だけ'},
  {'href':'1-4_極形式_練習編.html', 'no':'①-4 練習編', 'title':'極形式 練習編（問10）', 'desc':'⑴〜⒃　長さ → くくる → 向き'},
  {'href':'2-1_掛け算と長さ向き.html', 'no':'②-1', 'title':'掛け算と長さ・向き', 'desc':'i を 掛けると 回る　長さは 掛け算・向きは 足し算'},
  {'href':'2-2_複素数の積.html', 'no':'②-2', 'title':'複素数の積', 'desc':'公式・意味・導出（加法定理）　例・問11'},
  {'href':'2-3_掛け算と回転.html', 'no':'②-3', 'title':'掛け算と回転', 'desc':'掛ける ＝ 伸ばして 回す　例・問13'},
  {'href':'3-1_ド・モアブルの定理.html', 'no':'③-1', 'title':'ド・モアブルの定理', 'desc':'同じ 回転の くり返し　例・問16'},
  {'href':'3-2_1のn乗根.html', 'no':'③-2', 'title':'1のn乗根', 'desc':'n 回 掛けると 1 に 戻る 数　例・問17・問18'},
  {'href':'3-3_回転の応用.html', 'no':'③-3', 'title':'【発展】回転の応用', 'desc':'回転で 正三角形・正方形の 頂点を 求める'},
])
