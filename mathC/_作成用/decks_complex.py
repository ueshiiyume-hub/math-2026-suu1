"""複素数平面（プリント ①-1〜③-3）の デッキ
DECKS['ファイル名'] = (題, JS)。JS では const DECK = {title, pages:[{name, html}]} を 作る
部品（M・S・FILL・CAP・HD・BOX・PL・coverSlide）は parts.js
"""
DECKS = {}

# ---------------------------------------------------------------- ①-1 複素数平面
DECKS['1-1_複素数平面'] = ('①-1 複素数平面', r'''
const NO = '①-1', SEC = '数学C　複素数平面';
const R4 = {x0:-4, x1:4, y0:-4, y1:4};

/* 表紙 */
const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'複素数平面', sub:'複素数を 点で 表す'});

/* 2つの 数の 組 → 点 */
const g1 = PL({x0:-1, x1:5, y0:-1, y1:4, ticks:false});
const p1 = HD(NO, '複素数は 2つの 数の 組', SEC) + `<div class="bd">
  <div class="l" style="align-items:center;gap:26px">
    <div class="big">${M`\on{1}{re}{a}+\on{1}{im}{b}\,i`}</div>
    <div class="q" data-s="1"><span class="re">実部 ${M`a`}</span>　と　<span class="im">虚部 ${M`b`}</span></div>
    <div class="big" data-s="2">${M`(\RE{a},\ \IM{b})`}</div>
    <div class="q" data-s="3">座標平面の 点と 同じ</div>
  </div>
  <div class="r">${g1.svg(
      g1.walk(3, 2, 3, {la:'<tspan class="it">a</tspan>', lb:'<tspan class="it">b</tspan>'}) + g1.dot(3, 2, '(<tspan class="it">a</tspan>, <tspan class="it">b</tspan>)', 3, {d:1.2})
    )}</div>
</div>` + CAP([
  `複素数 ${M`a+bi`} を よく 見てみましょう。`,
  `この 数を 決めているのは、実部 ${M`a`} と 虚部 ${M`b`} の <b>2つの 数</b> です。`,
  `2つの 数の 組 ${M`(a,\ b)`} は、どこかで 見た 形ですね。`,
  `座標平面の 点と 同じです。だから、複素数は <b>平面の 点</b> で 表せます。`
]);

/* 名前を つける */
const g2 = PL(R4);
const p2 = HD(NO, '複素数平面', SEC) + `<div class="bd">
  <div class="l">${BOX('定義', `
    各点が 複素数を 表すと 定められた 座標平面を ${FILL(1,'複素数平面',6)} という。<br>
    ${M`x`} 軸を ${FILL(2,'実軸')}、<br>${M`y`} 軸を ${FILL(3,'虚軸')} という。<br>
    <span data-s="4">原点 O は 実数 ${M`0`} を 表す。</span>`)}
  </div>
  <div class="r">${g2.svg(
      g2.axl('re', 2) + g2.axl('im', 3)
    + g2.text(3.3, 0.4, '実軸', 'jp re', 2) + g2.text(0.3, 3.55, '虚軸', 'jp im', 3, 'start')
    + g2.dot(0, 0, '', 4) + g2.text(-1.3, -0.85, '0 + 0<tspan class="it">i</tspan>', 'dp', 4)
    )}</div>
</div>` + CAP([
  `点で 表すための 平面に、名前を つけます。`,
  `複素数を 点で 表す 平面を <b>複素数平面</b> と いいます。`,
  `横の 軸には 実部が 並ぶので <b class="re">実軸</b>。`,
  `縦の 軸には 虚部が 並ぶので <b class="im">虚軸</b>。`,
  `原点 O は ${M`0+0i`}、つまり 実数 ${M`0`} を 表します。`
]);

/* 点の 書き方 */
const p3 = HD(NO, '点の 書き方', SEC) + `<div class="bd col">
  ${BOX('記法', `複素数 ${M`z=a+bi`} を 表す 点 P を<br>
    　${M`\mathrm{P}(z)`}　または　${M`\mathrm{P}(a+bi)`}　と 書き、単に <b>点 ${M`z`}</b> ともいう。`)}
  <div class="q" data-s="1"><span class="tag">例</span>${M`\mathrm{P}(2+2i)`}　＝　点 ${M`2+2i`}　（${M`2+2i`} を 表す 点）</div>
</div>` + CAP([
  `点には 名前を つけて、表す 複素数を ( ) の 中に 書きます。`,
  `名前を 省いて「点 ${M`2+2i`}」と いうことも あります。`
]);

/* 例：4点を 図示 */
const g4 = PL(R4);
const ROW = (n, h, note) => `<div class="row" data-o="${n}">${h}${note||''}</div>`;
const p4 = HD(NO, '例　4点を 図示する', SEC) + `<div class="bd">
  <div class="l">
    <div class="q">複素数平面上に、次の 4点を 図示せよ。</div>
    <div class="rows">
      ${ROW(1, M`\mathrm{P}(\on{1}{re}{2}+\on{2}{im}{2i})`)}
      ${ROW(4, M`\mathrm{Q}(\RE{-2}+\IM{3i})`)}
      ${ROW(5, M`\mathrm{R}(-2i)`, `<span class="nt" data-s="5">＝ ${M`\RE{0}\IM{-2i}`}</span>`)}
      ${ROW(6, M`\mathrm{S}(3)`, `<span class="nt" data-s="6">＝ ${M`\RE{3}+\IM{0i}`}</span>`)}
    </div>
  </div>
  <div class="r">${g4.svg(
      g4.axl('im', 7) + g4.axl('re', 7)
    + g4.walk(2, 2, 1, {split:true, e:4}) + g4.dot(2, 2, 'P', 3)
    + g4.walk(-2, 3, 4, {e:5}) + g4.dot(-2, 3, 'Q', 4, {d:1.2, pos:'nw'})
    + g4.walk(0, -2, 5, {e:6}) + g4.dot(0, -2, 'R', 5, {d:.7, pos:'se'})
    + g4.walk(3, 0, 6, {e:7}) + g4.dot(3, 0, 'S', 6, {d:.7})
    )}</div>
</div>` + CAP([
  `原点から、<b class="re">実部の 分だけ 横</b>、<b class="im">虚部の 分だけ 縦</b> に 進みます。`,
  `${M`\mathrm{P}(2+2i)`}：実部は ${M`2`}。横に ${M`2`} 進みます。`,
  `虚部は ${M`2`}。縦に ${M`2`} 進みます。`,
  `着いた ところが 点 P です。`,
  `${M`\mathrm{Q}(-2+3i)`}：横に ${M`-2`}（左へ 2）、縦に ${M`3`}。`,
  `${M`\mathrm{R}(-2i)`}：実部は ${M`0`}。横には 動かず、縦に ${M`-2`}。`,
  `${M`\mathrm{S}(3)`}：虚部は ${M`0`}。縦には 動きません。`,
  `実数（S）は <b class="re">実軸の 上</b>、${M`-2i`} のような 数（R）は <b class="im">虚軸の 上</b> に きます。`
]);

/* 問4 */
const g5 = PL(R4);
const p5 = HD(NO, '問4', SEC) + `<div class="bd">
  <div class="l">
    <div class="q">次の 複素数を 表す 点を、<br>複素数平面に かき入れよ。</div>
    <div class="rows">
      ${ROW(1, M`\mathrm{A}(1+2i)`)}
      ${ROW(2, M`\mathrm{B}(-2-3i)`)}
      ${ROW(3, M`\mathrm{C}(3i)`)}
      ${ROW(4, M`\mathrm{D}(-3)`)}
    </div>
  </div>
  <div class="r">${g5.svg(
      g5.walk(1, 2, 1, {e:2}) + g5.dot(1, 2, 'A', 1, {d:1.2})
    + g5.walk(-2, -3, 2, {e:3}) + g5.dot(-2, -3, 'B', 2, {d:1.2, pos:'sw'})
    + g5.walk(0, 3, 3, {e:4}) + g5.dot(0, 3, 'C', 3, {d:.7})
    + g5.walk(-3, 0, 4) + g5.dot(-3, 0, 'D', 4, {d:.7, pos:'nw'})
    )}</div>
</div>` + CAP([
  `同じように、<b class="re">横</b> → <b class="im">縦</b> の 順に 進みましょう。`,
  `${M`\mathrm{A}(1+2i)`}：右に ${M`1`}、上に ${M`2`}。`,
  `${M`\mathrm{B}(-2-3i)`}：左に ${M`2`}、下に ${M`3`}。`,
  `${M`\mathrm{C}(3i)`}：実部は ${M`0`}。上に ${M`3`} だけ（虚軸の 上）。`,
  `${M`\mathrm{D}(-3)`}：虚部は ${M`0`}。左に ${M`3`} だけ（実軸の 上）。`
]);

/* 問5：点から 読み取る */
const g6 = PL(R4);
const PTS = [[3,3,'A','ne'],[-2,1,'B','nw'],[-3,-3,'C','sw'],[1,-2,'D','se'],[2,0,'E','ne'],[0,2,'F','ne']];
const ANS5 = [M`3+3i`, M`-2+i`, M`-3-3i`, M`1-2i`, M`2`, M`2i`];
const p6 = HD(NO, '問5', SEC) + `<div class="bd">
  <div class="l">
    <div class="q">右の 複素数平面上の 点は、<br>それぞれ どのような 複素数を 表しているか。</div>
    <div class="rows" style="display:grid;grid-template-columns:1fr 1fr;gap:8px 12px">
      ${PTS.map(([a,b,n],i)=>`<div class="row" data-o="${i+1}">${M`\mathrm{${n}}`}${FILL(i+1, ANS5[i], 4.4)}</div>`).join('')}
    </div>
  </div>
  <div class="r">${g6.svg(
      PTS.map(([a,b,n,p],i)=>g6.walk(a, b, i+1, {e:i+2})).join('')
    + PTS.map(([a,b,n,p])=>g6.dot(a, b, n, null, {pos:p, given:true})).join('')
    )}</div>
</div>` + CAP([
  `今度は 逆です。点から、原点から 横に いくつ・縦に いくつ を 読み取ります。`,
  `A：右に ${M`3`}、上に ${M`3`} → ${M`3+3i`}`,
  `B：左に ${M`2`}、上に ${M`1`} → ${M`-2+i`}（${M`1i`} は ${M`i`} と 書きます）`,
  `C：左に ${M`3`}、下に ${M`3`} → ${M`-3-3i`}`,
  `D：右に ${M`1`}、下に ${M`2`} → ${M`1-2i`}`,
  `E：実軸の 上。縦は ${M`0`} → ${M`2`}（${M`+0i`} は 書きません）`,
  `F：虚軸の 上。横は ${M`0`} → ${M`2i`}（${M`0+`} は 書きません）`
]);

/* まとめ（アニメーション なし） */
const g7 = PL(R4);
const p7 = HD(NO, 'まとめ', SEC) + `<div class="bd">
  <div class="l"><div class="sum">
    <span>点 ${M`(a,\ b)`}</span><span class="ar">⟷</span><span>複素数 ${M`\RE{a}+\IM{b}i`}</span>
    <span class="re">実軸の 上</span><span class="ar">⟷</span><span>実数（虚部が ${M`0`}）</span>
    <span class="im">虚軸の 上</span><span class="ar">⟷</span><span>${M`bi`} の 形（実部が ${M`0`}）</span>
  </div></div>
  <div class="r">${g7.svg(
      g7.walk(2, 2, null, {lab:false}) + g7.dot(2, 2, '2 + 2<tspan class="it">i</tspan>', null)
    + g7.dot(3, 0, '3', null, {pos:'se'}) + g7.dot(0, -2, '−2<tspan class="it">i</tspan>', null, {pos:'se'})
    )}</div>
</div>` + CAP([
  `複素数 ${M`a+bi`} は、点 ${M`(a,\ b)`} として 平面に 表せます。①-2 では、この 点で 計算を 見ていきます。`
]);

const DECK = {title:'①-1 複素数平面', pages:[
  {name:'表紙', html:p0},
  {name:'複素数は 2つの 数の 組', html:p1},
  {name:'複素数平面（定義）', html:p2},
  {name:'点の 書き方', html:p3},
  {name:'例　4点を 図示する', html:p4},
  {name:'問4', html:p5},
  {name:'問5', html:p6},
  {name:'まとめ', html:p7},
]};
''')
