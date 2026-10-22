"""数学C の 目次ページを作る（数学Ⅰ の _作成用/menus.py とは 別もの）
使い方: python mathC/_作成用/menus.py mathC
カードを足すときは、下の items に足して もう一度 実行する
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
    # back_href が None のときは「戻る」リンクを 出さない（数学C の トップは 数学Ⅰ の トップに つなげない）
    back = f'<a class="toplink" href="{back_href}">← {back_label}</a><br>' if back_href else ''
    h = h.replace('<a class="toplink" href="../index.html">← トップへ</a><br>', back)
    h = h.replace('<span class="kicker">数学Ⅰ　２学期中間考査対策プリント</span>', f'<span class="kicker">{kicker}</span>')
    h = h.replace('<h1><span class="mk">解説</span>スライド</h1>', f'<h1>{h1}</h1>')
    h = h.replace('<p class="lead">見たい 大問の カードを クリックしてね</p>', f'<p class="lead">{lead}</p>')
    h = h.replace('/* 大問の一覧（build.py が書きこむ） */', '/* カードの一覧（menus.py が書きこむ） */')
    # スマホが 古い スライドを 覚えて いても、新しい 版が 出るように リンクに ?v=バージョン を つける
    try: VERS = json.load(open(os.path.join(B, 'versions.json'), encoding='utf-8'))
    except Exception: VERS = {}
    items = [dict(it, href=it['href'] + ('?v=' + VERS[it['href'][:-5]]['v'] + '_' + VERS[it['href'][:-5]]['date'] if it['href'].endswith('.html') and it['href'][:-5] in VERS else '')) for it in items]
    h = h.replace('{{ITEMS}}', json.dumps(items, ensure_ascii=False, indent=1))
    # カードが まだ無いときは「準備中」を出す
    h = h.replace('</style>', EMPTY_CSS, 1)
    h = h.replace("document.getElementById('list').innerHTML = ITEMS.map(", EMPTY_JS)
    h = h.replace("</a>`).join('');", "</a>`).join('') : '<div class=\"empty\">これから 追加していくよ。お楽しみに！</div>';")
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(h)
    print('ok', path)

# 数学C の トップ（スライドができたら ここに カードを足す）
make('index.html', '数学C 解説スライド', None, None,
     '数学C', '<span class="mk">数学C</span> 解説スライド',
     '見たい 単元の カードを クリックしてね', [
])
