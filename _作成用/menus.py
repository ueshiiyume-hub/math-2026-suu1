"""目次ページ（期末考査の入口・授業プリント・対策プリント）を作る
使い方: python menus.py <リポジトリのルート>
カードを足すときは、下の PAGES の items に足して もう一度 実行する
"""
import os, sys, json
B = os.path.dirname(os.path.abspath(__file__))
ROOT = sys.argv[1]
tpl = open(os.path.join(B, 'menu.html'), encoding='utf-8').read()

EMPTY_CSS = '.empty{grid-column:1/-1;background:var(--paper);border:2px dashed var(--r-bd);border-radius:6px;padding:28px 20px;text-align:center;color:var(--muted);font-size:17px}\n</style>'
EMPTY_JS = "document.getElementById('list').innerHTML = ITEMS.length ? ITEMS.map("

def make(path, title, back_href, back_label, kicker, h1, lead, items):
    h = tpl
    h = h.replace('<title>２学期中間考査対策 目次</title>', f'<title>{title}</title>')
    h = h.replace('<a class="toplink" href="../index.html">← トップへ</a>', f'<a class="toplink" href="{back_href}">← {back_label}</a>')
    h = h.replace('<span class="kicker">数学Ⅰ　２学期中間考査対策プリント</span>', f'<span class="kicker">{kicker}</span>')
    h = h.replace('<h1><span class="mk">解説</span>スライド</h1>', f'<h1>{h1}</h1>')
    h = h.replace('<p class="lead">見たい 大問の カードを クリックしてね</p>', f'<p class="lead">{lead}</p>')
    h = h.replace('/* 大問の一覧（build.py が書きこむ） */', '/* カードの一覧（menus.py が書きこむ） */')
    h = h.replace('{{ITEMS}}', json.dumps(items, ensure_ascii=False, indent=1))
    # カードが まだ無いときは「準備中」を出す
    h = h.replace('</style>', EMPTY_CSS)
    h = h.replace("document.getElementById('list').innerHTML = ITEMS.map(", EMPTY_JS)
    h = h.replace("</a>`).join('');", "</a>`).join('') : '<div class=\"empty\">これから 追加していくよ。お楽しみに！</div>';")
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(h)
    print('ok', path)

# ２学期期末考査の入口
make('期末考査/目次.html', '２学期期末考査 目次', '../index.html', 'トップへ',
     '数学Ⅰ　２学期期末考査', '<span class="mk">期末考査</span>まで',
     '見たい 教材の カードを クリックしてね', [
  {'href':'jugyo/目次.html', 'no':'授業プリント', 'title':'授業プリントの 解説スライド',
   'desc':'2次方程式、x軸との共有点、2次不等式'},
  {'href':'taisaku/目次.html', 'no':'考査対策', 'title':'期末考査対策プリントの 解説',
   'desc':'期末考査 対策プリントの 解説'},
])

# 授業プリント（スライドができたら ここに足す）
make('期末考査/jugyo/目次.html', '授業プリント 解説 目次', '../目次.html', '期末考査へ',
     '数学Ⅰ　２学期期末考査まで　授業プリント', '<span class="mk">解説</span>スライド',
     '見たい 単元の カードを クリックしてね', [
  {'href':'1-1_因数分解の復習.html', 'no':'①-1', 'title':'因数分解の 復習', 'desc':'4つの パターン ⑴〜⑷'},
  {'href':'1-2_2次方程式の解.html', 'no':'①-2', 'title':'2次方程式の 解', 'desc':'因数分解して 解く ⑴〜⑷'},
  {'href':'1-3_2次方程式の解.html', 'no':'①-3', 'title':'2次方程式の 解 ②', 'desc':'x² に 数が つく ⑴⑵'},
  {'href':'1-4_解の公式.html', 'no':'①-4', 'title':'解の公式', 'desc':'公式に a・b・c を 入れる ⑴〜⑶'},
  {'href':'1-5_解の公式_重解と解なし.html', 'no':'①-5', 'title':'2次方程式の 解 ③', 'desc':'ルートの中が 0、マイナス ⑴⑵'},
  {'href':'1-6_実数解の個数.html', 'no':'①-6', 'title':'実数解の 個数', 'desc':'判別式 D'},
  {'href':'2-1_x軸との共有点.html', 'no':'②-1', 'title':'x軸との 共有点', 'desc':'y ＝ 0 と して 考える ⑴⑵'},
  {'href':'2-2_x軸との共有点.html', 'no':'②-2', 'title':'x軸との 共有点 ②', 'desc':'接する・共有点なし ⑴⑵'},
  {'href':'2-3_x軸との位置関係.html', 'no':'②-3', 'title':'x軸との 位置関係', 'desc':'交わる・接する・交わらない'},
  {'href':'3-1_2次不等式の解法.html', 'no':'③-1', 'title':'2次不等式の 解き方', 'desc':'Step❶〜❸ ⑴⑵'},
  {'href':'3-2_2次不等式_練習編.html', 'no':'③-2', 'title':'2次不等式 練習編', 'desc':'⑴〜⑿'},
  {'href':'3-3_2次不等式の解法.html', 'no':'③-3', 'title':'2次不等式 いろいろ', 'desc':'接する・交わらない ⑴〜⑷'},
  {'href':'3-4_2次不等式の解法.html', 'no':'③-4', 'title':'x² の前が マイナス', 'desc':'−1 を かけて 解く'},
])

# 期末考査対策プリント（スライドができたら ここに足す）
make('期末考査/taisaku/目次.html', '期末考査対策 目次', '../目次.html', '期末考査へ',
     '数学Ⅰ　２学期期末考査対策プリント', '<span class="mk">解説</span>スライド',
     '見たい 大問の カードを クリックしてね', [
])
