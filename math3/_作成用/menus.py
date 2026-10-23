"""数学Ⅲ の 目次ページを作る（数学Ⅰ・数学C の menus.py とは 別もの）
使い方: python math3/_作成用/menus.py math3
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
    # back_href が None のときは「戻る」リンクを 出さない（数学Ⅲ の トップは ほかの 科目に つなげない）
    back = f'<a class="toplink" href="{back_href}">← {back_label}</a><br>' if back_href else ''
    h = (tpl.replace('{{TITLE}}', title).replace('{{BACK}}', back).replace('{{KICKER}}', kicker)
            .replace('{{H1}}', h1).replace('{{LEAD}}', lead)
            .replace('{{ITEMS}}', json.dumps(items, ensure_ascii=False, indent=1)))
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(h)
    print('ok', path)

# 数学Ⅲ の トップ（単元ごとの カード）
make('index.html', '数学Ⅲ 解説スライド', None, None,
     '数学Ⅲ', '解説スライド', '単元を選んでください', [
  {'href':'integral/index.html', 'no':'積分法', 'title':'積分法', 'desc':'①-1〜④-4　不定積分の 公式・置換積分・部分積分・分数関数・三角関数'},
])

# 積分法（スライドが できたら ここに 足す。no は プリントと 同じ「①-1」）
make('integral/index.html', '積分法 解説スライド', '../index.html', '数学Ⅲ の トップへ',
     '数学Ⅲ　積分法', '解説スライド', 'プリントの 番号を 選んでください', [
  {'href':'1-1_xnの不定積分.html', 'no':'①-1', 'title':'xⁿ の不定積分', 'desc':'公式・例⑴〜⑸・問1'},
  {'href':'1-2_分子が多項式の場合.html', 'no':'①-2', 'title':'分子が多項式の場合', 'desc':'各項を 分母で 割る　例・問2'},
  {'href':'1-3_三角関数の不定積分.html', 'no':'①-3', 'title':'三角関数の不定積分', 'desc':'公式・tan²x の 直し方　例・問3'},
  {'href':'1-4_指数関数の不定積分.html', 'no':'①-4', 'title':'指数関数の不定積分', 'desc':'eˣ・aˣ の 公式　例・問4'},
  {'href':'1-5_合成関数の不定積分.html', 'no':'①-5', 'title':'合成関数の不定積分', 'desc':'当たりを つけて 帳尻を 合わせる　例・問5'},
  {'href':'2-1_置換積分_1次式.html', 'no':'②-1', 'title':'置換積分（1次式を t に）', 'desc':'置換積分法の 手順　例・問6'},
  {'href':'2-2_置換積分_根号.html', 'no':'②-2', 'title':'置換積分（√ を t に）', 'desc':'根号を まるごと t と おく　例・問7'},
  {'href':'2-3_置換積分_xで微分.html', 'no':'②-3', 'title':'置換積分（x で 微分する 型）', 'desc':'g(x) と g′(x) が そろう 形　例・問8'},
  {'href':'2-4_置換積分_分子が分母の微分.html', 'no':'②-4', 'title':'置換積分（分子が 分母の 微分）', 'desc':'log|分母|　例・問9'},
  {'href':'3-1_部分積分.html', 'no':'③-1', 'title':'部分積分法', 'desc':'公式・選び方　例・問10'},
  {'href':'3-2_部分積分_指数と対数.html', 'no':'③-2', 'title':'部分積分（eˣ・log x）', 'desc':'log x は 1×log x と 考える　例・問11・問12'},
  {'href':'4-1_分数関数の不定積分.html', 'no':'④-1', 'title':'分数関数の不定積分', 'desc':'割り算・部分分数分解　例・問14・問16'},
  {'href':'4-2_半角と積和の公式.html', 'no':'④-2', 'title':'半角の公式・積和の公式', 'desc':'加法定理から 導く ❶〜❻'},
  {'href':'4-3_三角関数_次数を下げる.html', 'no':'④-3', 'title':'三角関数の不定積分（次数を下げる）', 'desc':'公式❶〜❸　例・問17'},
  {'href':'4-4_三角関数_積を和に.html', 'no':'④-4', 'title':'三角関数の不定積分（積を和に）', 'desc':'積和の 公式❹〜❻　例・問18'},
])
