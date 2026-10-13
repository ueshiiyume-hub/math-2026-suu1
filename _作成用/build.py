import os, sys, json
B = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
rd = lambda f: open(os.path.join(B, f), encoding='utf-8').read()
head = rd('head.html').replace('</style>', rd('extra.css') + '\n' + rd('ink.css') + '\n</style>')
core = rd('core.js') + '\n' + rd('words.js')
engine = rd('engine.js') + '\n' + rd('ink.js')   # 手書き

TAIL_BODY = '''<body>
<div id="bg"></div>
<div id="stage"></div>
<div id="bar"></div>
<div class="ui" id="ui"></div>
<div id="jump"></div>
<script>
'''
# head.html は </head><body>… の手前まで入っているので body 以降を作り直す
head = head[:head.index('</head>')] + '</head>\n'

def page(title, deck_js):
    h = head.replace('<title>2次関数のグラフ</title>', f'<title>{title}</title>')
    return h + TAIL_BODY + core + '\n/* ====== この大問のスライド ====== */\n' + deck_js + '\n' + engine + '\n</script>\n</body>\n</html>\n'

decks = {}

decks['大問1_グラフ・頂点・軸'] = ('大問１ グラフ・頂点・軸', r'''
const problems = [
  {num:'⑴', a: 2, p:-1, q:-1}, {num:'⑵', a: 1, p: 2, q: 1}, {num:'⑶', a:-1, p: 1, q: 3},
  {num:'⑷', a: 1, p:-2, q:-3}, {num:'⑸', a:-2, p:-1, q: 5}, {num:'⑹', a: 3, p: 1, q:-2},
  {num:'⑺', a: 1, p: 1, q: 0}, {num:'⑻', a:-2, p:-1, q: 0}, {num:'⑼', a: 1, p: 0, q:-3},
  {num:'⑽', a:-2, p: 0, q: 1}, {num:'⑾', a: 3, p: 0, q: 0}, {num:'⑿', a:-1, p: 0, q: 0}
];
const DECK = {title:'大問１ グラフ・頂点・軸', pages:[
  {name:'表紙', html:cover('数学Ⅰ　２学期中間考査対策　大問１', '<span class="mk">2次関数</span>の<br>グラフ・頂点・軸', FORM_SUB, '式から 向き・頂点・軸 を 読みとろう！', '頂点 と 軸')},
  {name:'基本', html:graphBasic},
  ...problems.map(p=>({name:p.num, html:genGraph(p)})),
  {name:'終', html:endHtml}
]};
''')

decks['大問2_平方完成'] = ('大問２ 平方完成', r'''
const problems = [
  {num:'⑴',a:1,b:-6,c:0}, {num:'⑵',a:1,b:4,c:0}, {num:'⑶',a:1,b:-2,c:0}, {num:'⑷',a:1,b:8,c:0},
  {num:'⑸',a:1,b:-4,c:7}, {num:'⑹',a:1,b:6,c:5}, {num:'⑺',a:1,b:-8,c:10}, {num:'⑻',a:1,b:2,c:-3},
  {num:'⑼',a:2,b:-8,c:5}, {num:'⑽',a:3,b:6,c:1}, {num:'⑾',a:-1,b:4,c:-1}, {num:'⑿',a:-2,b:-12,c:-7}
];
const DECK = {title:'大問２ 平方完成', pages:[
  {name:'表紙', html:cover('数学Ⅰ　２学期中間考査対策　大問２', '<span class="mk">平方完成</span>で<br>形を かえよう', `y ＝ ax${P2} ＋ bx ＋ c　→　${FORM_SUB}`, '公式メモを 使って ⑴〜⑿ を やってみよう！', '平方完成')},
  {name:'公式', html:heihoBasic},
  ...problems.map(p=>({name:p.num, html:heihoSlide(p)})),
  {name:'終', html:endHtml}
]};
''')

decks['大問3_平方完成してグラフ'] = ('大問３ 平方完成してグラフ', r'''
const raw = [
  {num:'⑴',a:1,b:2,c:0}, {num:'⑵',a:1,b:-4,c:0}, {num:'⑶',a:1,b:-2,c:0},
  {num:'⑷',a:1,b:-2,c:3}, {num:'⑸',a:1,b:4,c:1}, {num:'⑹',a:1,b:2,c:-2},
  {num:'⑺',a:2,b:-4,c:0}, {num:'⑻',a:-1,b:2,c:2}, {num:'⑼',a:-2,b:-4,c:1}
];
const pg3 = [];
raw.forEach(r=>{
  const p = -r.b/(2*r.a), q = r.c - r.b*r.b/(4*r.a);
  pg3.push({name:r.num+'式', html:heihoSlide({...r, next:true})});
  pg3.push({name:r.num+'図', html:genGraph({num:r.num, a:r.a, p, q, yint:r.c, orig:{a:r.a,b:r.b}})});
});
const DECK = {title:'大問３ 平方完成してグラフ', pages:[
  {name:'表紙', html:cover('数学Ⅰ　２学期中間考査対策　大問３', '平方完成して<br><span class="mk">グラフ</span>をかこう', `y ＝ ax${P2} ＋ bx ＋ c　→　${FORM_SUB}`, 'まず 平方完成 → つぎに 向き・頂点・軸 と グラフ', 'グラフ')},
  {name:'公式', html:heihoBasic},
  {name:'読み方', html:graphBasic},
  ...pg3,
  {name:'終', html:endHtml}
]};
''')

decks['大問4_最大値・最小値'] = ('大問４ 最大値・最小値', r'''
const DECK = {title:'大問４ 最大値・最小値', pages:[
  {name:'表紙', html:cover('数学Ⅰ　２学期中間考査対策　大問４', '<span class="mk">最大値</span>・<span class="mk">最小値</span>', FORM_SUB, 'グラフを かいて、いちばん上・いちばん下 を さがそう！', '頂点 に 注目')},
  {name:'考え方', html:mmBasic},
  {name:'読み方', html:graphBasic},
  {name:'⑴', html:mmSlide({num:'⑴', a:2, p:-1, q:-1})},
  {name:'⑵', html:mmSlide({num:'⑵', a:-3, p:2, q:4})},
  {name:'⑶式', html:heihoSlide({num:'⑶', a:1, b:-4, c:5, next:true})},
  {name:'⑶図', html:mmSlide({num:'⑶', a:1, p:2, q:1, orig:{a:1,b:-4,c:5}, intro:`⑶ 平方完成した 式 ${M('y ＝ (x − 2)² ＋ 1')} を 使って、<b>最大値・最小値</b> を 求めよう！`})},
  {name:'⑷式', html:heihoSlide({num:'⑷', a:-2, b:4, c:1, next:true})},
  {name:'⑷図', html:mmSlide({num:'⑷', a:-2, p:1, q:3, orig:{a:-2,b:4,c:1}, intro:`⑷ 平方完成した 式 ${M('y ＝ −2(x − 1)² ＋ 3')} を 使って、<b>最大値・最小値</b> を 求めよう！`})},
  {name:'終', html:endHtml}
]};
''')

decks['大問5_ことば'] = ('大問５ 2次関数のことば', r'''
const DECK = {title:'大問５ 2次関数のことば', pages:[
  {name:'表紙', html:cover('数学Ⅰ　２学期中間考査対策　大問５', '2次関数の<br><span class="mk">ことば</span>', '２次関数・放物線・軸・頂点', '語群から 選んで ①〜⑥ を うめよう！', '軸 と 頂点')},
  {name:'問題', html:wordsSlide()},
  {name:'終', html:endHtml}
]};
''')

decks['大問6_平方完成'] = ('大問６ 平方完成', r'''
const problems = [
  {num:'⑴',a:1,b:4,c:0}, {num:'⑵',a:1,b:-12,c:0}, {num:'⑶',a:1,b:-6,c:-2}, {num:'⑷',a:2,b:8,c:1}
];
const DECK = {title:'大問６ 平方完成', pages:[
  {name:'表紙', html:cover('数学Ⅰ　２学期中間考査対策　大問６', '<span class="mk">平方完成</span><br>しなさい', `y ＝ ax${P2} ＋ bx ＋ c　→　${FORM_SUB}`, '⑴〜⑷ で 仕上げ！', '平方完成')},
  {name:'公式', html:heihoBasic},
  ...problems.map(p=>({name:p.num, html:heihoSlide(p)})),
  {name:'終', html:endHtml}
]};
''')

decks['大問7_グラフをかく'] = ('大問７ グラフをかく', r'''
const DECK = {title:'大問７ グラフをかく', pages:[
  {name:'表紙', html:cover('数学Ⅰ　２学期中間考査対策　大問７', 'グラフを<br><span class="mk">かいてみよう</span>', FORM_SUB, '頂点 と もう1点 を とって、なめらかに！', '頂点 と もう1点')},
  {name:'読み方', html:graphBasic},
  {name:'⑴', html:genGraph({num:'⑴', a:1, p:1, q:3, intro:`⑴ ${M('y ＝ (x − 1)² ＋ 3')} の <b>グラフ</b> を かき、<b>軸と頂点</b> を 求めよう。　頂点と それ以外の <b>1点</b> を 図示するよ。`})},
  {name:'終', html:endHtml}
]};
''')

os.makedirs(OUT, exist_ok=True)
for fn, (title, js) in decks.items():
    open(os.path.join(OUT, fn + '.html'), 'w', encoding='utf-8').write(page(title, js))

# 目次
cards = [
  ('大問1_グラフ・頂点・軸', '大問１', 'グラフ・<br>頂点・軸', '式から読みとる ⑴〜⑿', 'pink', -2),
  ('大問2_平方完成', '大問２', '平方完成', 'a(x−p)²＋q の形へ ⑴〜⑿', 'mint', 1.5),
  ('大問3_平方完成してグラフ', '大問３', '平方完成して<br>グラフ', '⑴〜⑼', 'yellow', -1),
  ('大問4_最大値・最小値', '大問４', '最大値・最小値', '⑴〜⑷', 'lav', 2),
  ('大問5_ことば', '大問５', '2次関数の<br>ことば', '語群から選ぶ ①〜⑥', 'blue', -1.5),
  ('大問6_平方完成', '大問６', '平方完成', '⑴〜⑷', 'pink', 1),
  ('大問7_グラフをかく', '大問７', 'グラフをかく', '頂点ともう1点', 'mint', -2),
]
# トップページと同じ「ふつうのWebページ」の作り（スクロール・更新ができる）
items = [{'href':fn+'.html','no':no,'title':tt.replace('<br>',''),'desc':ds} for fn,no,tt,ds,tp,rot in cards]
menu = rd('menu.html').replace('{{ITEMS}}', json.dumps(items, ensure_ascii=False, indent=1))
open(os.path.join(OUT, '目次.html'), 'w', encoding='utf-8').write(menu)
print('ok', len(decks)+1, 'files')
