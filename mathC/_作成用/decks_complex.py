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

# ---------------------------------------------------------------- ①-2 和・差・実数倍・共役
DECKS['1-2_和差実数倍共役'] = ('①-2 和・差・実数倍・共役', r'''
const NO = '①-2', SEC = '数学C　複素数平面';
/* SVG の 文字：z₁ や w、共役（上に 線） */
const Zs = (v, i) => `<tspan class="it">${v}</tspan>${i?`<tspan baseline-shift="sub" font-size="15">${i}</tspan>`:''}`;
const BAR = h => `<tspan text-decoration="overline">${h}</tspan>`;

/* 1つの 計算を 図で 見せる ページ
   kind: add（和）・sub（差）・mul（実数倍）・conj（共役）
   p：1つ目の 点 [a,b,名前]、q：2つ目の 点（add・sub）、k：実数倍の k、r：結果 [a,b,名前]
   top：左上（規則の 枠 や 問題）、calc：計算（TeX の 行）、fill：空らんが 埋まる 番、extra：最後に 1段 足す（例 だけ）、cm：説明 */
function opPage(o){
  const g = PL(o.R), [pa,pb,pn] = o.p, [ra,rb,rn] = o.r, q = o.q;
  let fig = g.arr(0,0,pa,pb,null) + g.dot(pa,pb,pn,null,{given:true, pos:o.pp||'ne'});
  if(q) fig += g.arr(0,0,q[0],q[1],null) + g.dot(q[0],q[1],q[2],null,{given:true, pos:o.qp||'ne'});
  const res = n => g.dot(ra,rb,rn,n,{pos:o.rp||'ne', d:o.kind==='mul'?.6:1.3});
  if(o.kind==='add'){
    fig += g.move(g.arr(0,0,q[0],q[1],null,{c:'m', dash:true}), pa, pb, 2)
         + g.arr(0,0,ra,rb,3,{c:'g'}) + res(3);
    if(o.extra) fig += g.move(g.arr(0,0,pa,pb,null,{c:'m', dash:true}), q[0], q[1], 4);
  }
  if(o.kind==='sub'){
    fig += g.move(g.arr(q[0],q[1],pa,pb,null,{c:'g', dash:true}), -q[0], -q[1], 3)
         + g.arr(q[0],q[1],pa,pb,2,{c:'g', e:3}) + g.arr(0,0,ra,rb,3,{c:'g', d:1.3}) + res(3);
  }
  if(o.kind==='mul'){
    fig += g.line(pa,pb,2) + g.arr(0,0,ra,rb,3,{c:'g'}) + res(3);
    if(o.extra) fig += g.arr(0,0,-pa,-pb,4,{c:'m'}) + g.dot(-pa,-pb,o.extra,4,{pos:'sw', d:.6});
  }
  if(o.kind==='conj'){
    fig += g.axl('re', 2) + g.flip(g.arr(0,0,pa,pb,null,{c:'g'}), 2) + res(2)
         + `<line class="dash" x1="${g.X(pa)}" y1="${g.Y(pb)}" x2="${g.X(ra)}" y2="${g.Y(rb)}" data-s="3"/>`;
  }
  return HD(NO, o.title, SEC) + `<div class="bd">
    <div class="l op">${o.top}
      <div class="calc">${o.calc.map((c,i)=>`<div data-s="1"${i?` style="--d:${i*.5}s"`:''}>${M(c)}</div>`).join('')}</div>
      ${o.note||''}
    </div>
    <div class="r">${g.svg(fig)}</div>
  </div>` + CAP(o.cm);
}

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'和・差・実数倍・共役', sub:'ベクトルと 同じように 図で 考える'});

/* 点 ＝ 原点からの 矢印 */
const gv = PL({x0:-1, x1:4, y0:-1, y1:3});
const p1 = HD(NO, 'ベクトルと 同じように 考える', SEC) + `<div class="bd">
  <div class="l" style="align-items:center;gap:30px">
    <div class="big">${M`z=\RE{a}+\IM{b}i`}</div>
    <div class="big" data-s="1">${M`\updownarrow`}</div>
    <div class="big" data-s="1">ベクトル ${M`(\RE{a},\ \IM{b})`}</div>
  </div>
  <div class="r">${gv.svg(gv.dot(1,2,Zs('z')+' = 1 + 2'+Zs('i'),null) + gv.arr(0,0,1,2,1,{c:'g'}))}</div>
</div>` + CAP([
  `①-1 では、複素数 ${M`z=a+bi`} を 点で 表しました。`,
  `その 点を、原点から のびる <b>矢印</b> と 見ると、ベクトル ${M`(a,\ b)`} と 同じです。`,
  `だから 和・差・実数倍 は、ベクトルと 同じように 図で 見られます。`
]);

/* 例：z₁ ＝ 1＋2i、z₂ ＝ 4＋i */
const RX = {x0:-4, x1:6, y0:-3, y1:5, u:44};
const EX = `<div class="q"><span class="tag">例</span>${M`z_1=1+2i,\ z_2=4+i`}</div>`;
const Z1 = [1,2,Zs('z',1)], Z2 = [4,1,Zs('z',2)];

const p2 = opPage({title:'和　z₁＋z₂', kind:'add', R:RX, p:Z1, q:Z2, r:[5,3,Zs('z',1)+' + '+Zs('z',2)], qp:'se', extra:true,
  top: BOX('和', `点 ${M`z_1`} を、${M`z_2`} の 分だけ<br>${FILL(3,'平行移動')} した 点`) + EX,
  calc:[String.raw`z_1+z_2=(\RE{1+4})+(\IM{2+1})i`, String.raw`=\DP{5+3i}`],
  note:`<div class="vnote" data-s="4">ベクトルでは ${M`\overrightarrow{a}+\overrightarrow{b}`}（平行四辺形の 対角線）</div>`,
  cm:[`${M`z_1`} と ${M`z_2`} を、原点からの 矢印で かいて おきます。`,
      `計算は、<b class="re">実部どうし</b>・<b class="im">虚部どうし</b> を たします。${M`z_1+z_2=5+3i`}`,
      `図では、${M`z_2`} の 矢印を ${M`z_1`} の 先へ <b>平行移動</b> します。`,
      `着いた 点が ${M`z_1+z_2`}。計算した ${M`5+3i`} と 一致します。`,
      `逆に ${M`z_1`} を ${M`z_2`} の 先へ 動かしても 同じ 点。ベクトルの 和と 同じ 平行四辺形 です。`]});

const p3 = opPage({title:'差　z₁−z₂', kind:'sub', R:RX, p:Z1, q:Z2, r:[-3,1,Zs('z',1)+' − '+Zs('z',2)], qp:'se', rp:'nw',
  top: BOX('差', `点 ${M`z_2`} から 点 ${M`z_1`} へ 向かう 矢印を、<br>原点から 引いた 先`) + EX,
  calc:[String.raw`z_1-z_2=(\RE{1-4})+(\IM{2-1})i`, String.raw`=\DP{-3+i}`],
  note:`<div class="vnote" data-s="3">ベクトルでは ${M`\overrightarrow{a}-\overrightarrow{b}`}</div>`,
  cm:[`今度は 差 ${M`z_1-z_2`} です。`,
      `計算は、実部どうし・虚部どうし を ひきます。${M`z_1-z_2=-3+i`}`,
      `${M`z_2+(z_1-z_2)=z_1`} なので、差は「${M`z_2`} から ${M`z_1`} へ 向かう 矢印」です。`,
      `その 矢印を 原点から 引くと、先が ${M`z_1-z_2=-3+i`}。計算と 一致します。`]});

const p4 = opPage({title:'実数倍　kz', kind:'mul', R:RX, p:Z1, r:[2,4,'2'+Zs('z',1)], extra:'−'+Zs('z',1),
  top: BOX('実数倍', `原点と 点 ${M`z`} を 通る ${FILL(2,'直線')} 上。<br>原点からの 距離は ${M`|k|`} 倍`) + EX,
  calc:[String.raw`2z_1=2(1+2i)`, String.raw`=\DP{2+4i}`],
  note:`<div class="vnote" data-s="3">ベクトルでは ${M`k\overrightarrow{a}`}</div>`,
  cm:[`実数倍 ${M`2z_1`} を 図で 見ます。`,
      `計算は、実部も 虚部も 2倍。${M`2z_1=2+4i`}`,
      `実部と 虚部が 同じ 割合で 伸びるので、点は 原点と ${M`z_1`} を 通る <b>直線</b> の 上に のります。`,
      `向きは そのまま、原点からの 距離が 2倍の 点が ${M`2z_1`} です。`,
      `${M`k`} が 負なら 反対向き。たとえば ${M`-z_1`} は 原点の 反対側に きます。`]});

const p5 = opPage({title:'共役　z̄', kind:'conj', R:RX, p:Z1, r:[1,-2,BAR(Zs('z',1))], rp:'se',
  top: BOX('共役', `${M`\overline{z}=a-bi`}<br>点 ${M`z`} と ${FILL(2,'実軸')} に<br>関して 対称な 点`) + EX,
  calc:[String.raw`\overline{z_1}=\RE{1}\on{1}{im}{-2i}`],
  note:`<div class="vnote" data-s="3">ベクトルでは ${M`y`} 座標の 符号を 変える</div>`,
  cm:[`最後は 共役 ${M`\overline{z_1}`} です。`,
      `共役は、<b class="im">虚部の 符号</b> だけを 変えます。${M`\overline{z_1}=1-2i`}`,
      `縦の 位置だけが 反対に なるので、<b class="re">実軸</b> を 折り目に して 折り返した 点です。`,
      `${M`z_1`} と ${M`\overline{z_1}`} は、実軸から 同じ 距離の ところに あります。`]});

/* 練習：z ＝ −3＋2i、w ＝ 1＋i */
const RP = {x0:-5, x1:3, y0:-3, y1:4, u:52};
const PQ = (n, t) => `<div class="q"><span class="tag">練習</span>${M`z=-3+2i,\ w=1+i`} のとき、次の 点を 図示せよ。</div><div class="q big" style="font-size:36px">${n}　${M(t)}</div>`;
const ZZ = [-3,2,Zs('z')], WW = [1,1,Zs('w')];
const p6 = opPage({title:'練習 ⑴', kind:'add', R:RP, p:ZZ, q:WW, r:[-2,3,Zs('z')+' + '+Zs('w')], pp:'nw', qp:'se',
  top: PQ('⑴', 'z+w'), calc:[String.raw`z+w=(\RE{-3+1})+(\IM{2+1})i`, String.raw`=\DP{-2+3i}`],
  cm:[`和は「平行移動」でした。`, `実部どうし・虚部どうし を たして ${M`-2+3i`}。`,
      `${M`w`} の 矢印を ${M`z`} の 先へ 平行移動 します。`, `着いた 点が ${M`z+w=-2+3i`} です。`]});
const p7 = opPage({title:'練習 ⑵', kind:'sub', R:RP, p:ZZ, q:WW, r:[-4,1,Zs('z')+' − '+Zs('w')], pp:'nw', qp:'se', rp:'nw',
  top: PQ('⑵', 'z-w'), calc:[String.raw`z-w=(\RE{-3-1})+(\IM{2-1})i`, String.raw`=\DP{-4+i}`],
  cm:[`差は「${M`w`} から ${M`z`} へ 向かう 矢印」でした。`, `実部どうし・虚部どうし を ひいて ${M`-4+i`}。`,
      `${M`w`} から ${M`z`} へ 向かう 矢印を かきます。`, `原点から 引くと、先が ${M`z-w=-4+i`} です。`]});
const p8 = opPage({title:'練習 ⑶', kind:'mul', R:RP, p:WW, r:[2,2,'2'+Zs('w')], pp:'se',
  top: PQ('⑶', '2w'), calc:[String.raw`2w=2(1+i)`, String.raw`=\DP{2+2i}`],
  cm:[`実数倍は「原点と 点を 通る 直線の 上」でした。`, `実部も 虚部も 2倍して ${M`2+2i`}。`,
      `原点と ${M`w`} を 通る 直線を 引きます。`, `その 上で、距離が 2倍の 点が ${M`2w=2+2i`} です。`]});
const p9 = opPage({title:'練習 ⑷', kind:'conj', R:RP, p:ZZ, r:[-3,-2,BAR(Zs('z'))], pp:'nw', rp:'sw',
  top: PQ('⑷', String.raw`\overline{z}`), calc:[String.raw`\overline{z}=\RE{-3}\on{1}{im}{-2i}`],
  cm:[`共役は「実軸に 関して 対称な 点」でした。`, `虚部の 符号だけ 変えて ${M`-3-2i`}。`,
      `実軸を 折り目に して 折り返します。`, `${M`\overline{z}=-3-2i`} です。`]});

/* まとめ（プリントの 表。アニメーション なし） */
const p10 = HD(NO, 'まとめ', SEC) + `<div class="bd col">
  <div class="tbl">
    <div class="th">計算</div><div class="th">複素数平面での 意味</div><div class="th">ベクトルでは</div>
    <div>和　${M`z_1+z_2`}</div><div>点 ${M`z_1`} を、${M`z_2`} の 分だけ <b class="dp">平行移動</b> した 点</div><div>${M`\overrightarrow{a}+\overrightarrow{b}`}</div>
    <div>差　${M`z_1-z_2`}</div><div>点 ${M`z_2`} から 点 ${M`z_1`} へ 向かう 矢印を、原点から 引いた 先</div><div>${M`\overrightarrow{a}-\overrightarrow{b}`}</div>
    <div>実数倍　${M`kz`}</div><div>原点と 点 ${M`z`} を 通る <b class="dp">直線</b> 上。原点からの 距離は ${M`|k|`} 倍</div><div>${M`k\overrightarrow{a}`}</div>
    <div>共役　${M`\overline{z}`}</div><div>点 ${M`z`} と <b class="dp">実軸</b> に 関して 対称な 点</div><div>${M`y`} 座標の 符号を 変える</div>
  </div>
</div>` + CAP([`複素数の 計算は、点（矢印）の 動きとして 図で 見られます。`]);

const DECK = {title:'①-2 和・差・実数倍・共役', pages:[
  {name:'表紙', html:p0},
  {name:'ベクトルと 同じように 考える', html:p1},
  {name:'例　和', html:p2}, {name:'例　差', html:p3}, {name:'例　実数倍', html:p4}, {name:'例　共役', html:p5},
  {name:'練習 ⑴　z＋w', html:p6}, {name:'練習 ⑵　z−w', html:p7}, {name:'練習 ⑶　2w', html:p8}, {name:'練習 ⑷　共役', html:p9},
  {name:'まとめ', html:p10},
]};
''')

# ---------------------------------------------------------------- ①-3 複素数の絶対値
DECKS['1-3_絶対値'] = ('①-3 複素数の絶対値', r'''
const NO = '①-3', SEC = '数学C　複素数平面';
const IT = v => `<tspan class="it">${v}</tspan>`;
const ABSZ = `|${IT('z')}|`;

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'複素数の絶対値', sub:'原点からの 距離'});

/* 定義 */
const gd = PL({x0:-1, x1:5, y0:-1, y1:4, ticks:false});
const PZ = gd.dot(3, 2, `${IT('z')} = ${IT('a')} + ${IT('b')}${IT('i')}`, null);
const p1 = HD(NO, '絶対値', SEC) + `<div class="bd">
  <div class="l">${BOX('定義', `原点 O と 点 ${M`z=a+bi`} の 距離を<br>${M`z`} の ${FILL(1,'絶対値')} といい、${M`|z|`} で 表す。`)}</div>
  <div class="r">${gd.svg(gd.seg(0,0,3,2,1,{lab:ABSZ, side:-1}) + PZ)}</div>
</div>` + CAP([
  `複素数 ${M`z`} は 平面の 点でした。その 点が、原点から どれだけ 離れて いるかを 考えます。`,
  `原点 O からの 距離を ${M`z`} の <b>絶対値</b> と いい、${M`|z|`} と 書きます。`
]);

/* 三平方の 定理で 求める */
const p2 = HD(NO, '絶対値の 求め方', SEC) + `<div class="bd">
  <div class="l">${BOX('三平方の 定理', `三平方の 定理より　${M`|z|^2=`}${FILL(2, M`\RE{a}^2+\IM{b}^2`, 5)}<br>
    よって　${M`|z|=|a+bi|=`}${FILL(3, M`\sqrt{\RE{a}^2+\IM{b}^2}`, 6)}`)}</div>
  <div class="r">${gd.svg(gd.walk(3, 2, 1, {plain:true, la:IT('a'), lb:IT('b')}) + gd.ra(3, 2, 1) + gd.seg(0,0,3,2,null,{lab:ABSZ, side:-1}) + PZ)}</div>
</div>` + CAP([
  `距離 ${M`|z|`} を、${M`a`} と ${M`b`} で 表して みましょう。`,
  `<b class="re">横に ${M`a`}</b>、<b class="im">縦に ${M`b`}</b>。${M`|z|`} は 直角三角形の <b>斜辺</b> です。`,
  `三平方の 定理で、${M`|z|^2=a^2+b^2`}。`,
  `${M`|z|`} は 距離で 0 以上 なので、正の 平方根を とって ${M`\sqrt{a^2+b^2}`}。`,
  `${M`a`} や ${M`b`} が 負でも、2乗 すれば 同じ。いつでも この 式で 求められます。`
]);

/* 例・練習：点 → 三角形 → 計算
   pt：[a, b, 点の 名前]、leg：[横の 長さ, 縦の 長さ]、calc：[[TeX, 番, 遅れ], …]、hyp：斜辺の 文字、extra：最後の 1段（SVG） */
function absPage(o){
  const g = PL(o.R), [a,b,name] = o.pt;
  const fig = g.walk(a, b, 1, {plain:true, la:o.leg[0], lb:o.leg[1]}) + (o.noRa ? '' : g.ra(a, b, 1))
    + g.seg(0, 0, a, b, 2, {lab:o.hyp, ls:3, side:o.side||-1})
    + g.dot(a, b, name, null, {pos:o.pp||'ne'}) + (o.extra ? o.extra(g) : '');
  return HD(NO, o.title, SEC) + `<div class="bd">
    <div class="l">${o.top}
      <div class="calc">${o.calc.map(([t,n,d])=>`<div data-s="${n}"${d?` style="--d:${d}s"`:''}>${M(t)}</div>`).join('')}</div>
    </div>
    <div class="r">${g.svg(fig)}</div>
  </div>` + CAP(o.cm);
}
const Q = (tag, t) => `<div class="q"><span class="tag">${tag}</span>${t}</div>`;

const p3 = absPage({title:'例　|3＋4i|', R:{x0:-1, x1:5, y0:-1, y1:5, u:52}, pt:[3, 4, `3 + 4${IT('i')}`], leg:['3','4'], hyp:'5',
  top: Q('例', `${M`|3+4i|`} を 求めよ。`),
  calc:[[String.raw`|3+4i|=\sqrt{\RE{3}^2+\IM{4}^2}`, 2], [String.raw`=\sqrt{25}=\DP{5}`, 3]],
  cm:[`点 ${M`3+4i`} と 原点の 距離を 求めます。`,
      `横に ${M`3`}、縦に ${M`4`} の 直角三角形が できます。`,
      `斜辺の 長さは、三平方の 定理で ${M`\sqrt{3^2+4^2}`}。`,
      `${M`\sqrt{25}=5`}。原点から 距離 ${M`5`} の ところに あります。`]});

const p4 = absPage({title:'練習 ⑴　|3−4i|', R:{x0:-1, x1:5, y0:-5, y1:5, u:44}, pt:[3, -4, `3 − 4${IT('i')}`], leg:['3','4'], hyp:'5', pp:'se', side:1,
  top: Q('練習', '次の 複素数の 絶対値を 求めよ。') + `<div class="q big" style="font-size:36px">⑴　${M`3-4i`}</div>`,
  calc:[[String.raw`|3-4i|=\sqrt{\RE{3}^2+(\IM{-4})^2}`, 2], [String.raw`=\sqrt{25}=\DP{5}`, 3]],
  extra: g => g.seg(0, 0, 3, 4, 4, {c:'m'}) + g.dot(3, 4, `3 + 4${IT('i')}`, 4, {given:true}) + `<line class="dash" x1="${g.X(3)}" y1="${g.Y(4)}" x2="${g.X(3)}" y2="${g.Y(-4)}" data-s="4"/>`,
  cm:[`点 ${M`3-4i`} は、実軸より 下に あります。`,
      `横に ${M`3`}、下へ ${M`4`}。直角を はさむ 辺の 長さは ${M`3`} と ${M`4`} です。`,
      `${M`-4`} も 2乗 すれば ${M`16`}。${M`\sqrt{3^2+(-4)^2}`} です。`,
      `${M`\sqrt{25}=5`}。`,
      `${M`3+4i`}（共役）と 実軸で 対称なので、距離も 同じ ${M`5`} です。`]});

const p5 = absPage({title:'練習 ⑵　|−2i|', R:{x0:-3, x1:3, y0:-3, y1:2, u:60}, pt:[0, -2, `−2${IT('i')}`], leg:['',''], hyp:'2', pp:'se', side:1, noRa:true,
  top: `<div class="q big" style="font-size:36px">⑵　${M`-2i`}</div>`,
  calc:[[String.raw`\lvert -2i\rvert=\sqrt{\RE{0}^2+(\IM{-2})^2}`, 2], [String.raw`=\DP{2}`, 3]],
  cm:[`点 ${M`-2i`} は 虚軸の 上に あります。`,
      `実部が ${M`0`} なので 横には 進みません。三角形が つぶれて、縦の 線だけに なります。`,
      `式に あてはめると ${M`\sqrt{0^2+(-2)^2}`}。`,
      `${M`=2`}。図で 見た とおり、原点から そのまま ${M`2`} です。`]});

const S3 = Math.sqrt(3);
const p6 = absPage({title:'練習 ⑶　|1＋√3 i|', R:{x0:-1, x1:3, y0:-1, y1:3, u:84}, pt:[1, S3, `1 + √3${IT('i')}`], leg:['1','√3'], hyp:'2',
  top: `<div class="q big" style="font-size:36px">⑶　${M`1+\sqrt{3}i`}</div>`,
  calc:[[String.raw`|1+\sqrt{3}i|=\sqrt{\RE{1}^2+(\IM{\sqrt{3}})^2}`, 2], [String.raw`=\sqrt{4}=\DP{2}`, 3]],
  extra: g => { const r = 32, cx = g.X(0), cy = g.Y(0), ex = cx + r*Math.cos(Math.PI/3), ey = cy - r*Math.sin(Math.PI/3);
    return `<path class="arc" d="M${cx+r} ${cy} A${r} ${r} 0 0 0 ${ex.toFixed(1)} ${ey.toFixed(1)}" data-s="4"/>`
      + `<text class="dp" x="${cx+36}" y="${cy-8}" style="font-size:17px" data-s="4">60°</text>`; },
  cm:[`点 ${M`1+\sqrt{3}i`} は、横に ${M`1`}、縦に ${M`\sqrt{3}`} の ところです。`,
      `横 ${M`1`}、縦 ${M`\sqrt{3}`} の 直角三角形が できます。`,
      `${M`(\sqrt{3})^2=3`} なので、${M`\sqrt{1+3}`}。`,
      `${M`\sqrt{4}=2`}。`,
      `辺の 比 ${M`1:\sqrt{3}:2`} は 三角定規の 形。この 角 ${M`60^\circ`} は ①-4 で 使います。`]});

/* まとめ（アニメーション なし） */
const p7 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:34px">
  ${BOX('絶対値', `<span class="big">${M`|z|=|a+bi|=\sqrt{\RE{a}^2+\IM{b}^2}`}</span><br>（原点からの 距離）`)}
  <div class="res4">
    <span>${M`|3+4i|=5`}</span><span>${M`|3-4i|=5`}</span><span>${M`\lvert -2i\rvert=2`}</span><span>${M`|1+\sqrt{3}i|=2`}</span>
  </div>
</div>` + CAP([`絶対値は「原点からの 距離」。直角三角形の 斜辺として、三平方の 定理で 求めます。`]);

const DECK = {title:'①-3 複素数の絶対値', pages:[
  {name:'表紙', html:p0}, {name:'絶対値（定義）', html:p1}, {name:'絶対値の 求め方', html:p2},
  {name:'例　|3＋4i|', html:p3}, {name:'練習 ⑴　|3−4i|', html:p4}, {name:'練習 ⑵　|−2i|', html:p5}, {name:'練習 ⑶　|1＋√3 i|', html:p6},
  {name:'まとめ', html:p7},
]};
''')

# ---------------------------------------------------------------- ①-4 複素数の極形式
DECKS['1-4_極形式'] = ('①-4 複素数の極形式', r'''
const NO = '①-4', SEC = '数学C　複素数平面';
const IT = v => `<tspan class="it">${v}</tspan>`;
const S3 = Math.sqrt(3), S2 = Math.sqrt(2);

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'複素数の極形式', sub:'長さと 向きで 表す'});

/* 2通りの 表し方（②を 強調：①を うすく → 向きに ぐるっと 回す → 長さ r を のばす → 点が 波打つ） */
const g1 = PL({x0:-1, x1:5, y0:-1, y1:4, ticks:false});
const T1 = 32.9, R1 = Math.hypot(3.4, 2.2) * g1.u;
const P1 = g1.dot(3.4, 2.2, 'P', null);
const SWEEP = `<g data-s="2"><g transform="translate(${g1.X(0)} ${g1.Y(0)})"><g class="sweep" data-o="2" style="--rot:${-T1}deg">
  <line class="swl" x1="0" y1="0" x2="${(R1+40).toFixed(1)}" y2="0"/></g></g></g>`;
const RING = `<circle class="pulse" cx="${g1.X(3.4)}" cy="${g1.Y(2.2)}" r="22" data-s="3" style="--d:.6s"/>`;
const p1 = HD(NO, '点の 位置の 2通りの 表し方', SEC) + `<div class="bd">
  <div class="l" style="gap:30px">
    <div class="q dimo" data-s="1" data-o="2"><b>①</b>　<span class="re">実軸方向に ${M`a`}</span>、<span class="im">虚軸方向に ${M`b`}</span><br>　→　${M`z=a+bi`}</div>
    <div class="q hl2" data-s="2" data-o="3"><b>②</b>　<span class="dp">向き ${M`\theta`} に、長さ ${M`r`}</span><br>　→　<b class="dp">長さ ${M`r`} と 向き ${M`\theta`}</b></div>
  </div>
  <div class="r">${g1.svg(`<g class="dimo" data-o="2">${g1.walk(3.4, 2.2, 1, {plain:true, below:true, la:IT('a'), lb:IT('b')})}</g>`
    + SWEEP + g1.ang(T1, 2, {lab:IT('θ'), r:50, d:1.1, fs:24})
    + g1.seg(0, 0, 3.4, 2.2, 3, {lab:IT('r'), side:-1, w:6}) + P1 + RING)}</div>
</div>` + CAP([
  `点 P の 位置の 表し方は、1つでは ありません。`,
  `① これまでの 表し方。<b class="re">横に ${M`a`}</b>、<b class="im">縦に ${M`b`}</b> 進んだ 点 → ${M`a+bi`}。`,
  `② もう1つの 表し方。まず <b class="dp">向き</b>：実軸の 正の 向きから、ぐるっと ${M`\theta`} だけ 回します。`,
  `次に <b class="dp">長さ</b>：その 向きに ${M`r`} だけ 進みます。「北東へ 3km」のような 言い方です。これが 極形式の もとに なります。`
]);

/* 長さ と 向き の 名前 */
const p2 = HD(NO, '長さ と 向き', SEC) + `<div class="bd col" style="gap:30px">
  <div class="tbl" style="grid-template-columns:auto 1fr auto auto">
    <div class="th"></div><div class="th">意味</div><div class="th">記号</div><div class="th">読み方</div>
    <div><b class="dp">長さ ${M`r`}</b></div><div>原点 O からの 距離</div><div>${FILL(1, M`|z|`, 3)}</div><div>${M`z`} の 絶対値</div>
    <div><b class="dp">向き ${M`\theta`}</b></div><div>実軸の 正の 向きから、左回りに 測った 角</div><div>${FILL(2, M`\arg z`, 3.6)}</div><div>${M`z`} の 偏角<br><span class="mu" style="font-size:18px">（arg：argument）</span></div>
  </div>
  <div class="q" data-s="3">「${M`\arg z=60^\circ`}」＝「${M`z`} は ${M`60^\circ`} の 向きに ある」</div>
</div>` + CAP([
  `②の 長さ と 向き には、名前と 記号が あります。`,
  `長さ ${M`r`} は、①-3 で 学んだ <b>絶対値</b> ${M`|z|`} です。`,
  `向き ${M`\theta`} は <b>偏角</b> と いい、${M`\arg z`} と 書きます。実軸の 正の 向きから <b>左回り</b> に 測ります。`,
  `${M`\arg z`} は「${M`z`} の 向き」と 読みかえると わかりやすいです。`
]);

/* 極形式 */
const g3 = PL({x0:-1, x1:5, y0:-1, y1:4, ticks:false});
const p3 = HD(NO, '極形式', SEC) + `<div class="bd">
  <div class="l">${BOX('極形式', `長さ ${M`r`}、向き ${M`\theta`} の 点 P の 座標は<br>
    　${M`a=`}${FILL(1, M`\RE{r\cos\theta}`, 4)}、${M`b=`}${FILL(2, M`\IM{r\sin\theta}`, 4)}<br>
    よって　${M`z=`}${FILL(3, M`r(\cos\theta+i\sin\theta)`, 8)}<br>
    これを ${M`z`} の ${FILL(4,'極形式')} という。<br>
    ${M`\theta`} を ${M`z`} の ${FILL(4,'偏角')} といい、${M`\arg z`} で 表す。`)}
    <div class="vnote" data-s="5">（${M`\cos\theta+i\sin\theta`}：長さ ${M`1`}、向き ${M`\theta`} の 数）</div>
  </div>
  <div class="r">${g3.svg(g3.seg(0, 0, 3.4, 2.2, null, {lab:IT('r'), side:-1}) + g3.ang(32.9, null, {lab:IT('θ'), r:50})
    + g3.walk(3.4, 2.2, 1, {plain:true, split:true, below:true, la:IT('r')+' cos '+IT('θ'), lb:IT('r')+' sin '+IT('θ')}) + g3.ra(3.4, 2.2, 1)
    + g3.dot(3.4, 2.2, 'P', null))}</div>
</div>` + CAP([
  `長さ ${M`r`} と 向き ${M`\theta`} から、${M`a`} と ${M`b`} を 求めて みます。`,
  `三角比の 定義 ${M`\cos\theta=\dfrac{a}{r}`} より、横の 長さは ${M`a=r\cos\theta`}。`,
  `${M`\sin\theta=\dfrac{b}{r}`} より、縦の 長さは ${M`b=r\sin\theta`}。`,
  `${M`z=a+bi`} に 入れて、${M`r`} で くくると ${M`r(\cos\theta+i\sin\theta)`}。`,
  `この 形を <b>極形式</b>、${M`\theta`} を <b>偏角</b> と いいます。`,
  `かっこの 中の ${M`\cos\theta+i\sin\theta`} が「向き」、前の ${M`r`} が「長さ」を 表して います。`
]);

/* 長さと 向きを 読み取る */
const PG = {x0:-3, x1:3, y0:-3, y1:3, u:62, grid:false, ticks:false, xl:null, yl:null,
  polar:{n:3, rays:[0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330], labels:[30,60,120,150,210,240,300,330]}};
const g4 = PL(PG);
const RD = [['A',2,30,[S3,1],'2', String.raw`2(\cos30^\circ+i\sin30^\circ)`, String.raw`\sqrt{3}+i`],
            ['B',3,90,[0,3],'3', String.raw`3(\cos90^\circ+i\sin90^\circ)`, String.raw`3i`],
            ['C',1,180,[-1,0],'1', String.raw`\cos180^\circ+i\sin180^\circ`, String.raw`-1`],
            ['D',2,225,[-S2,-S2],'2', String.raw`2(\cos225^\circ+i\sin225^\circ)`, String.raw`-\sqrt{2}-\sqrt{2}i`]];
const p4 = HD(NO, '長さと 向きを 読み取る', SEC) + `<div class="bd">
  <div class="l" style="flex:1.25">
    <div class="q" style="font-size:22px">点 A〜D の 長さと 向きを 読み取り、<br>極形式と ${M`a+bi`} の 形で 表せ。</div>
    <div class="tbl rd" style="grid-template-columns:auto auto auto 1fr auto">
      <div class="th">点</div><div class="th">長さ</div><div class="th">向き</div><div class="th">極形式</div><div class="th">${M`a+bi`}</div>
      ${RD.map(([n,r,t,p,rs,pf,ab],i)=>`<div>${n}</div><div>${FILL(2*i+1, M(rs), 1.6)}</div><div>${FILL(2*i+1, M(t+'^\\circ'), 2.4)}</div><div>${FILL(2*i+2, M(pf), 4)}</div><div>${FILL(2*i+2, M(ab), 3)}</div>`).join('')}
    </div>
  </div>
  <div class="r">${g4.svg(
      RD.map(([n,r,t,[a,b]],i)=>g4.seg(0,0,a,b,2*i+1,{e:2*i+3}) + g4.ang(t, 2*i+1, {lab:false, r:26, e:2*i+3})).join('')
    + RD.map(([n,r,t,[a,b]])=>g4.dot(a, b, n, null, {pos:b<0?'sw':a<0?'nw':'ne'})).join('')
  , 'pg')}</div>
</div>` + CAP([
  `円は 原点からの 距離（長さ）、線は 向きを 表します。`,
  `A：2つめの 円の 上、${M`30^\circ`} の 線の 上。長さ ${M`2`}、向き ${M`30^\circ`}。`,
  `極形式は ${M`2(\cos30^\circ+i\sin30^\circ)`}。${M`\cos30^\circ=\frac{\sqrt{3}}{2}`}、${M`\sin30^\circ=\frac{1}{2}`} を 入れて ${M`\sqrt{3}+i`}。`,
  `B：長さ ${M`3`}、真上なので 向き ${M`90^\circ`}。`,
  `${M`\cos90^\circ=0`}、${M`\sin90^\circ=1`} なので ${M`3i`}。`,
  `C：長さ ${M`1`}、真左なので 向き ${M`180^\circ`}。`,
  `長さが ${M`1`} の ときは、前の ${M`1`} を 書きません。${M`\cos180^\circ=-1`} なので ${M`-1`}。`,
  `D：長さ ${M`2`}、${M`180^\circ`} より さらに ${M`45^\circ`} 回って ${M`225^\circ`}。`,
  `${M`\cos225^\circ=\sin225^\circ=-\frac{1}{\sqrt{2}}`} なので ${M`-\sqrt{2}-\sqrt{2}i`}。`
]);

/* 例：1＋i を 極形式で */
const g5 = PL({x0:-1, x1:2, y0:-1, y1:2, u:84});
const POINT = `<div class="pbox"><div class="pl2">Point</div>${M`r=\sqrt{a^2+b^2}`}<br>${M`\cos\theta=\dfrac{a}{r},\ \sin\theta=\dfrac{b}{r}`}</div>`;
const p5 = HD(NO, '例　1＋i を 極形式で', SEC) + `<div class="bd">
  <div class="l">
    <div class="q" style="font-size:23px"><span class="tag">例</span>${M`1+i`} を 極形式で 表せ。<br>ただし、偏角 ${M`\theta`} は ${M`0^\circ\leqq\theta<360^\circ`} とする。</div>
    <div class="calc" style="font-size:28px;gap:10px">
      <div>${M`r=|1+i|=`}${FILL(1, M`\sqrt{1^2+1^2}`, 3)}${M`=`}${FILL(1, M`\sqrt{2}`, 2)}</div>
      <div>${M`\cos\theta=`}${FILL(2, M`\frac{1}{\sqrt{2}}`, 2)}、${M`\sin\theta=`}${FILL(2, M`\frac{1}{\sqrt{2}}`, 2)}</div>
      <div>${M`0^\circ\leqq\theta<360^\circ`} より　${M`\theta=`}${FILL(3, M`45^\circ`, 2)}</div>
      <div>よって　${M`1+i=`}${FILL(4, M`\sqrt{2}`, 1.6)}${M`(\cos`}${FILL(4, M`45^\circ`, 1.8)}${M`+i\sin`}${FILL(4, M`45^\circ`, 1.8)}${M`)`}</div>
    </div>
  </div>
  <div class="r" style="flex-direction:column;gap:14px">${g5.svg(g5.walk(1, 1, 1, {plain:true}) + g5.seg(0,0,1,1,1,{lab:'√2', side:-1}) + g5.ang(45, 3, {r:44})
    + g5.dot(1, 1, `1 + ${IT('i')}`, null), 'sm2')}${POINT}</div>
</div>` + CAP([
  `極形式に するには、長さ ${M`r`} と 向き ${M`\theta`} が わかれば よい。`,
  `長さは 絶対値。${M`r=\sqrt{1^2+1^2}=\sqrt{2}`}。`,
  `${M`\cos\theta=\dfrac{a}{r}`}、${M`\sin\theta=\dfrac{b}{r}`} に 入れると、どちらも ${M`\dfrac{1}{\sqrt{2}}`}。`,
  `${M`\cos`} も ${M`\sin`} も ${M`\dfrac{1}{\sqrt{2}}`} に なる 角は ${M`45^\circ`}。図でも 45° です。`,
  `長さ ${M`\sqrt{2}`}、向き ${M`45^\circ`} なので、${M`1+i=\sqrt{2}(\cos45^\circ+i\sin45^\circ)`}。`
]);

/* 特別な 角は「くくる」だけ */
/* プリントの Point：三角比の 表（2026-10-23 の プリント更新で 変わった） */
const TRIG = `<div class="trig">${[
  ['\\theta', '0^\\circ','30^\\circ','45^\\circ','60^\\circ','90^\\circ'],
  ['\\sin\\theta', '0','\\frac{1}{2}','\\frac{1}{\\sqrt{2}}','\\frac{\\sqrt{3}}{2}','1'],
  ['\\cos\\theta', '1','\\frac{\\sqrt{3}}{2}','\\frac{1}{\\sqrt{2}}','\\frac{1}{2}','0'],
  ['\\tan\\theta', '0','\\frac{1}{\\sqrt{3}}','1','\\sqrt{3}','なし']].map((r,i)=>r.map((c,j)=>`<div class="${i===0||j===0?'th':''}">${c==='なし'?c:M(c)}</div>`).join('')).join('')}</div>`;
const p6 = HD(NO, '特別な 角は「くくる」だけ', SEC) + `<div class="bd">
  <div class="l">
    <div class="q">絶対値 ${M`r`} で くくると、かっこの 中が ${M`\cos\theta`}、${M`\sin\theta`} の 値に なる。</div>
    <div class="calc" style="font-size:30px;gap:8px">
      <div data-s="1">${M`1+i=\DP{\sqrt{2}}\left(\on{2}{re}{\tfrac{1}{\sqrt{2}}}+\on{2}{im}{\tfrac{1}{\sqrt{2}}}i\right)`}</div>
      <div data-s="2">${M`\quad=\sqrt{2}(\cos45^\circ+i\sin45^\circ)`}</div>
      <div data-s="3">${M`1+\sqrt{3}i=\DP{2}\left(\on{4}{re}{\tfrac{1}{2}}+\on{4}{im}{\tfrac{\sqrt{3}}{2}}i\right)`}</div>
      <div data-s="4">${M`\quad=2(\cos60^\circ+i\sin60^\circ)`}</div>
    </div>
  </div>
  <div class="r" style="flex-direction:column;gap:6px">
    <div class="pbox"><div class="pl2">Point</div>${TRIG}</div>
  </div>
</div>` + CAP([
  `毎回 ${M`\cos\theta`}、${M`\sin\theta`} を 計算しなくても、もっと 速い 方法が あります。`,
  `長さ ${M`r=\sqrt{2}`} で くくると、かっこの 中に ${M`\tfrac{1}{\sqrt{2}}`} と ${M`\tfrac{1}{\sqrt{2}}`} が 出て きます。`,
  `これは ${M`(\cos45^\circ,\ \sin45^\circ)`}。そのまま ${M`45^\circ`} と 読めます。`,
  `${M`1+\sqrt{3}i`} は、長さ ${M`r=2`} で くくります。`,
  `${M`\left(\tfrac{1}{2},\tfrac{\sqrt{3}}{2}\right)`} は ${M`60^\circ`}。Point の 表の 値と 見比べれば、くくる だけで 角が わかります。`
]);

/* まとめ（アニメーション なし） */
const p7 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('極形式', `<span class="big">${M`z=a+bi=r(\cos\theta+i\sin\theta)`}</span><br>${M`r=|z|`}（長さ）、${M`\theta=\arg z`}（向き）`)}
  <div class="q" style="font-size:27px;line-height:1.8">
    <b class="dp">① 長さ</b>　${M`r=\sqrt{a^2+b^2}`} を 求める<br>
    <b class="dp">② くくる</b>　${M`r`} で くくって、かっこの 中を ${M`(\cos\theta,\ \sin\theta)`} に する<br>
    <b class="dp">③ 向き</b>　30°・45°・60° の 形と、符号（象限）から ${M`\theta`} を 決める
  </div>
</div>` + CAP([`この 手順で、練習編（問10）の 16問を 解いて いきます。`]);

const DECK = {title:'①-4 複素数の極形式', pages:[
  {name:'表紙', html:p0}, {name:'2通りの 表し方', html:p1}, {name:'長さ と 向き', html:p2}, {name:'極形式', html:p3},
  {name:'長さと 向きを 読み取る', html:p4}, {name:'例　1＋i を 極形式で', html:p5}, {name:'特別な 角は「くくる」だけ', html:p6},
  {name:'まとめ', html:p7},
]};
''')

# ---------------------------------------------------------------- ①-4 練習編（問10）
DECKS['1-4_極形式_練習編'] = ('①-4 極形式 練習編（問10）', r'''
const NO = '①-4', SEC = '数学C　複素数平面　練習編';
const IT = v => `<tspan class="it">${v}</tspan>`;
const S3 = Math.sqrt(3), S2 = Math.sqrt(2), S6 = Math.sqrt(6);
/* 基準の 角 → かっこの 中の (cos, sin) の 大きさ */
const FR = {30:[String.raw`\dfrac{\sqrt{3}}{2}`, String.raw`\dfrac{1}{2}`], 45:[String.raw`\dfrac{1}{\sqrt{2}}`, String.raw`\dfrac{1}{\sqrt{2}}`], 60:[String.raw`\dfrac{1}{2}`, String.raw`\dfrac{\sqrt{3}}{2}`]};
const KK = (r, a, b, base) => `${r}\\left(\\RE{${a<0?'-':''}${FR[base][0]}}${b<0?'-':'+'}\\IM{${FR[base][1]}}i\\right)`;
const POLAR = (r, t) => r==='1' ? `\\cos${t}^\\circ+i\\sin${t}^\\circ` : `${r}(\\cos${t}^\\circ+i\\sin${t}^\\circ)`;
const QN = (a, b) => a>0 ? (b>0 ? 1 : 4) : (b>0 ? 2 : 3);
const SG = v => v>0 ? '＋' : '−';
/* [番号, z, a, b, r の 計算, r（図の 文字）, r（TeX）, 基準の 角（軸の 上は null）, θ, 軸の 上の ときの 言葉] */
const PR = [
  ['⑴', String.raw`\sqrt{3}+i`, S3, 1, String.raw`\sqrt{(\sqrt{3})^2+1^2}=\sqrt{4}=2`, '2', '2', 30, 30],
  ['⑵', String.raw`-1+i`, -1, 1, String.raw`\sqrt{(-1)^2+1^2}=\sqrt{2}`, '√2', String.raw`\sqrt{2}`, 45, 135],
  ['⑶', String.raw`1-i`, 1, -1, String.raw`\sqrt{1^2+(-1)^2}=\sqrt{2}`, '√2', String.raw`\sqrt{2}`, 45, 315],
  ['⑷', String.raw`-1+\sqrt{3}i`, -1, S3, String.raw`\sqrt{(-1)^2+(\sqrt{3})^2}=\sqrt{4}=2`, '2', '2', 60, 120],
  ['⑸', String.raw`-\sqrt{3}+i`, -S3, 1, String.raw`\sqrt{(-\sqrt{3})^2+1^2}=\sqrt{4}=2`, '2', '2', 30, 150],
  ['⑹', String.raw`2+2i`, 2, 2, String.raw`\sqrt{2^2+2^2}=\sqrt{8}=2\sqrt{2}`, '2√2', String.raw`2\sqrt{2}`, 45, 45],
  ['⑺', String.raw`i`, 0, 1, String.raw`\sqrt{0^2+1^2}=1`, '1', '1', null, 90, '虚軸の 正の 向き（真上）'],
  ['⑻', String.raw`-3`, -3, 0, String.raw`\sqrt{(-3)^2+0^2}=3`, '3', '3', null, 180, '実軸の 負の 向き（真左）'],
  ['⑼', String.raw`-1-\sqrt{3}i`, -1, -S3, String.raw`\sqrt{(-1)^2+(-\sqrt{3})^2}=\sqrt{4}=2`, '2', '2', 60, 240],
  ['⑽', String.raw`\sqrt{3}-i`, S3, -1, String.raw`\sqrt{(\sqrt{3})^2+(-1)^2}=\sqrt{4}=2`, '2', '2', 30, 330],
  ['⑾', String.raw`-2i`, 0, -2, String.raw`\sqrt{0^2+(-2)^2}=2`, '2', '2', null, 270, '虚軸の 負の 向き（真下）'],
  ['⑿', String.raw`4`, 4, 0, String.raw`\sqrt{4^2+0^2}=4`, '4', '4', null, 0, '実軸の 正の 向き（真右）'],
  ['⒀', String.raw`-2-2i`, -2, -2, String.raw`\sqrt{(-2)^2+(-2)^2}=\sqrt{8}=2\sqrt{2}`, '2√2', String.raw`2\sqrt{2}`, 45, 225],
  ['⒁', String.raw`1-\sqrt{3}i`, 1, -S3, String.raw`\sqrt{1^2+(-\sqrt{3})^2}=\sqrt{4}=2`, '2', '2', 60, 300],
  ['⒂', String.raw`3+\sqrt{3}i`, 3, S3, String.raw`\sqrt{3^2+(\sqrt{3})^2}=\sqrt{12}=2\sqrt{3}`, '2√3', String.raw`2\sqrt{3}`, 30, 30],
  ['⒃', String.raw`-\sqrt{6}+\sqrt{2}i`, -S6, S2, String.raw`\sqrt{(-\sqrt{6})^2+(\sqrt{2})^2}=\sqrt{8}=2\sqrt{2}`, '2√2', String.raw`2\sqrt{2}`, 30, 150],
];
const QTX = {1:(b,t)=>`第1象限 なので そのまま ${M(`\\theta=${t}^\\circ`)}`, 2:(b,t)=>`第2象限 なので ${M(`\\theta=180^\\circ-${b}^\\circ=${t}^\\circ`)}`,
             3:(b,t)=>`第3象限 なので ${M(`\\theta=180^\\circ+${b}^\\circ=${t}^\\circ`)}`, 4:(b,t)=>`第4象限 なので ${M(`\\theta=360^\\circ-${b}^\\circ=${t}^\\circ`)}`};

function prPage([no, z, a, b, rc, rl, rt, base, t, axis]){
  const R = Math.ceil(Math.max(Math.abs(a), Math.abs(b))) + 1, g = PL({x0:-R, x1:R, y0:-R, y1:R, u:Math.floor(400/(2*R)), ticks:false});
  const q = base ? QN(a, b) : 0, ans = POLAR(rt, t), sa = 2;   // 番：1 長さ、2 くくる（軸は 向き）、3 象限・角、4 答え
  const qx = q===1||q===4 ? 0 : -R, qy = q===1||q===2 ? R : 0;
  const quad = q ? `<rect class="qd" x="${g.X(qx)}" y="${g.Y(qy)}" width="${R*g.u}" height="${R*g.u}" data-s="3"/>` : '';
  const fig = quad + g.seg(0, 0, a, b, 1, {lab:rl, side:(a>=0)===(b>=0) ? -1 : 1}) + (t ? g.ang(t, base ? 3 : 2, {r:34, lr:26}) : g.text(R*.3, -R*.2, '0°', 'dp', 2))
    + g.dot(a, b, `${no}`, null, {pos:(b<0?'s':'n')+(a<0?'w':'e')});
  const lines = base
    ? [[`r=${rc}`, 1], [`${z}=${KK(rt, a, b, base)}`, 2], [`\\theta=${t}^\\circ`, 3], [`${z}=\\DP{${ans}}`, 4]]
    : [[`r=${rc}`, 1], [`\\theta=${t}^\\circ`, 2], [`${z}=\\DP{${ans}}`, 3]];
  const cm = base
    ? [`${M(z)} を 極形式に します。`,
       `① 長さ：${M(`r=${rc}`)}`,
       `② ${M(rt)} で くくると、かっこの 中は（${M('\\cos')}，${M('\\sin')}）＝（${SG(a)}，${SG(b)}）で、大きさは ${M(`${base}^\\circ`)} の 形。`,
       `③ 符号が（${SG(a)}，${SG(b)}）→ ${QTX[q](base, t)}。`,
       `${M(`${z}=${ans}`)}`]
    : [`${M(z)} を 極形式に します。`,
       `① 長さ：${M(`r=${rc}`)}`,
       `② 点は ${axis}。だから 向きは ${M(`${t}^\\circ`)}。`,
       `${M(`${z}=${ans}`)}${rt==='1' ? '（長さ 1 は 書かない）' : ''}`];
  return HD(NO, `問10 ${no}　${'<span class="m">'+z+'</span>'}`, SEC) + `<div class="bd">
    <div class="l">
      <div class="q big" style="font-size:40px">${no}　${M(z)}</div>
      <div class="calc" style="font-size:30px;gap:10px">${lines.map(([x,n])=>`<div data-s="${n}">${M(x)}</div>`).join('')}</div>
    </div>
    <div class="r">${g.svg(fig, 'pr')}</div>
  </div>` + CAP(cm);
}

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO+'　練習編', title:'極形式（問10）', sub:'⑴〜⒃　手順どおりに テンポよく'});

/* 手順と 象限 */
const gq = PL({x0:-3, x1:3, y0:-3, y1:3, u:62, grid:false, ticks:false, xl:null, yl:null});
const QL = [[1.5,1.6,'第1象限','（＋，＋）','θ ＝ 基準'],[-1.5,1.6,'第2象限','（−，＋）','180° − 基準'],[-1.5,-1.4,'第3象限','（−，−）','180° ＋ 基準'],[1.5,-1.4,'第4象限','（＋，−）','360° − 基準']];
const p1 = HD(NO, '手順', SEC) + `<div class="bd">
  <div class="l"><div class="q" style="font-size:27px;line-height:1.9">
    <b class="dp">① 長さ</b>　${M`r=\sqrt{a^2+b^2}`}<br>
    <b class="dp">② くくる</b>　${M`r`} で くくって（${M`\cos`}，${M`\sin`}）の 形に<br>
    <b class="dp">③ 向き</b>　基準の 角（30°・45°・60°）と 符号（象限）で ${M`\theta`}<br>
    <span class="mu" style="font-size:22px">軸の 上の 点は、図から そのまま 向きを 読む</span></div></div>
  <div class="r">${gq.svg(QL.map(([x,y,n,s,f])=>gq.text(x,y,n,'jp dp') + gq.text(x,y-.45,s,'') + gq.text(x,y-.9,f,'sm')).join(''), 'pr')}</div>
</div>` + CAP([`かっこの 中の 符号（${M`\cos`}，${M`\sin`}）で 象限が 決まり、基準の 角から ${M`\theta`} が 決まります。`]);

const pages = PR.map(prPage);

/* 答えの 一覧（アニメーション なし） */
const pe = HD(NO, '答え（問10）', SEC) + `<div class="bd col"><div class="ans16">
  ${PR.map(([no,z,a,b,rc,rl,rt,base,t])=>`<div><span class="mu">${no}</span> ${M(`${z}=${POLAR(rt,t)}`)}</div>`).join('')}
</div></div>` + CAP([`まちがえた 問題は、目次から その ページに 戻って 確かめましょう。`]);

const DECK = {title:'①-4 極形式 練習編（問10）', pages:[
  {name:'表紙', html:p0}, {name:'手順', html:p1},
  ...PR.map((p,i)=>({name:`${p[0]}　${p[1].replace(/\\sqrt\{(\d)\}/g,'√$1').replace(/-/g,'−')}`, html:pages[i]})),
  {name:'答え（一覧）', html:pe},
]};
''')

# ---------------------------------------------------------------- ②-1 掛け算と長さ・向き
DECKS['2-1_掛け算と長さ向き'] = ('②-1 掛け算と長さ・向き', r'''
const NO = '②-1', SEC = '数学C　複素数平面';
const IT = v => `<tspan class="it">${v}</tspan>`;
const S3 = Math.sqrt(3);

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'掛け算と長さ・向き', sub:'掛けると 回る'});

/* i を 掛けると */
const gu = PL({x0:-1.6, x1:1.6, y0:-1.6, y1:1.6, u:140, grid:false, ticks:false});
const RR = gu.u, CX = gu.X(0), CY = gu.Y(0);
/* 円の 外側を 回る 矢印（a0° → a1°、左回り） */
const arcA = (a0, a1, R, n, lab) => {
  const r = Math.PI/180, x0 = CX+R*Math.cos(a0*r), y0 = CY-R*Math.sin(a0*r), t = a1*r, x1 = CX+R*Math.cos(t), y1 = CY-R*Math.sin(t);
  const dx = -Math.sin(t), dy = -Math.cos(t), s = 13, w = 7;   // 左回りの 進む 向き
  const hp = `${x1.toFixed(1)},${y1.toFixed(1)} ${(x1-dx*s-dy*w).toFixed(1)},${(y1-dy*s+dx*w).toFixed(1)} ${(x1-dx*s+dy*w).toFixed(1)},${(y1-dy*s-dx*w).toFixed(1)}`;
  const m = (a0+a1)/2*r, lx = CX+(R+30)*Math.cos(m), ly = CY-(R+30)*Math.sin(m)+7;
  return `<path class="arc rot dr" pathLength="1" d="M${x0.toFixed(1)} ${y0.toFixed(1)} A${R} ${R} 0 0 0 ${x1.toFixed(1)} ${y1.toFixed(1)}" data-s="${n}"/>`
    + `<polygon class="roth" points="${hp}" data-s="${n}" style="--d:.5s"/>`
    + `<text class="dp" x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" text-anchor="middle" data-s="${n}" style="--d:.3s">×${IT('i')}</text>`;
};
const UPTS = [[1,0,'1','nw'],[0,1,IT('i'),'se'],[-1,0,'−1','ne'],[0,-1,'−'+IT('i'),'nw']];
const p1 = HD(NO, 'i を 掛けると', SEC) + `<div class="bd">
  <div class="l">
    <div class="q">${M`1`} に ${M`i`} を 次々に 掛ける。</div>
    <div class="calc" style="font-size:32px;gap:10px">
      <div>${M`1\times i=`}${FILL(1, M`i`, 2.4)}</div>
      <div>${M`i\times i=`}${FILL(2, M`-1`, 2.4)}</div>
      <div>${M`(-1)\times i=`}${FILL(3, M`-i`, 2.4)}</div>
      <div>${M`(-i)\times i=`}${FILL(4, M`1`, 2.4)}</div>
    </div>
    <div class="q" data-s="5">→ ${M`i`} を 掛けると、原点の まわりに ${FILL(5, M`90^\circ`, 2.6)} 回転</div>
    <div class="q" data-s="6">→ ${M`i^2=-1`}：${M`90^\circ`} 回転を 2回で 反対向き</div>
  </div>
  <div class="r">${gu.svg(`<circle class="ucirc" cx="${CX}" cy="${CY}" r="${RR}"/>`
    + arcA(4, 86, RR+16, 1) + arcA(94, 176, RR+16, 2) + arcA(184, 266, RR+16, 3) + arcA(274, 356, RR+16, 4)
    + gu.ang(180, 6, {r:62, lab:IT('i')+'²', fs:22, la:120})
    + UPTS.map(([a,b,l,p],i)=>gu.dot(a, b, l, i ? i : null, {pos:p, d:i ? .6 : 0})).join(''))}</div>
</div>` + CAP([
  `${M`1`} から スタートして、${M`i`} を 1回ずつ 掛けて いきます。`,
  `${M`1\times i=i`}。点 ${M`1`} が 点 ${M`i`} へ。真上に 回りました。`,
  `${M`i\times i=i^2=-1`}。さらに 回って 真左へ。`,
  `${M`(-1)\times i=-i`}。真下へ。`,
  `${M`(-i)\times i=-i^2=1`}。1周して 元の ${M`1`} に 戻りました。`,
  `${M`i`} を 掛ける たびに、原点の まわりを <b>${M`90^\circ`} ずつ 回って</b> います。`,
  `${M`i^2=-1`} は「${M`90^\circ`} 回転を 2回 → ${M`180^\circ`} で 反対向き」と 見られます。`
]);

/* 積を 計算する */
const CALC = [String.raw`2\times(1+i)=\DP{2+2i}`, String.raw`i\times(1+i)=i+i^2=\DP{-1+i}`, String.raw`(-1)\times(1+i)=\DP{-1-i}`,
  String.raw`(1+i)\times(1+i)=1+2i+i^2=\DP{2i}`, String.raw`i\times(\sqrt{3}+i)=\sqrt{3}i+i^2=\DP{-1+\sqrt{3}i}`,
  String.raw`(1+\sqrt{3}i)(\sqrt{3}+i)=\sqrt{3}+i+3i+\sqrt{3}i^2=\DP{4i}`];
const p2 = HD(NO, '積を 計算する', SEC) + `<div class="bd col" style="align-items:flex-start">
  <div class="q">次の 積を 計算し、結果の 長さ（絶対値）と 向き（偏角）を 求めよ。</div>
  <div class="calc" style="font-size:29px;gap:6px">${CALC.map((c,i)=>`<div data-s="${i+1}">${M(c)}</div>`).join('')}</div>
</div>` + CAP([
  `まず、6つの 積を ふつうに 計算します。`,
  `実数倍は、実部も 虚部も 2倍。`,
  `${M`i^2=-1`} に 注意。`,
  `${M`-1`} 倍は 符号が 反対に なります。`,
  `${M`(1+i)^2=1+2i+i^2`}。${M`i^2=-1`} で 実部が 消えて ${M`2i`}。`,
  `${M`\sqrt{3}i+i^2=-1+\sqrt{3}i`}。`,
  `${M`\sqrt{3}i^2=-\sqrt{3}`} なので、実部が 消えて ${M`4i`}。`
]);

/* 長さと 向きを 表に する */
const L = (t, n) => `\\on{${n}}{re}{${t}}`, A = (t, n) => `\\on{${n}}{im}{${t}^\\circ}`;
const ROWS = [
  [String.raw`2\times(1+i)`, '2','0', String.raw`\sqrt{2}`,'45', '2+2i', String.raw`2\sqrt{2}`,'45'],
  [String.raw`i\times(1+i)`, '1','90', String.raw`\sqrt{2}`,'45', '-1+i', String.raw`\sqrt{2}`,'135'],
  [String.raw`(-1)\times(1+i)`, '1','180', String.raw`\sqrt{2}`,'45', '-1-i', String.raw`\sqrt{2}`,'225'],
  [String.raw`(1+i)\times(1+i)`, String.raw`\sqrt{2}`,'45', String.raw`\sqrt{2}`,'45', '2i', '2','90'],
  [String.raw`i\times(\sqrt{3}+i)`, '1','90', '2','30', String.raw`-1+\sqrt{3}i`, '2','120'],
  [String.raw`(1+\sqrt{3}i)(\sqrt{3}+i)`, '2','60', '2','30', '4i', '4','90']];
const p3 = HD(NO, '長さと 向きを 比べる', SEC) + `<div class="bd col" style="gap:16px">
  <div class="tbl mt" style="grid-template-columns:auto auto auto auto auto">
    <div class="th">積</div><div class="th">${M`z_1`} の 長さ，向き</div><div class="th">${M`z_2`} の 長さ，向き</div><div class="th">計算した 結果</div><div class="th">結果の 長さ，向き</div>
    ${ROWS.map(([p,l1,a1,l2,a2,res,lr,ar],i)=>`<div>${M(p)}</div><div>${M(`${L(l1,7)},\\ ${A(a1,8)}`)}</div><div>${M(`${L(l2,7)},\\ ${A(a2,8)}`)}</div>`
      + `<div>${FILL(i+1, M(res), 4)}</div><div>${FILL(i+1, M(`${L(lr,7)},\\ ${A(ar,8)}`), 5)}</div>`).join('')}
  </div>
  <div class="q" data-s="9">→ 長さは ${FILL(9,'掛け算')}、向きは ${FILL(9,'足し算')}</div>
</div>` + CAP([
  `計算した 結果の 長さと 向きを、表に 入れて いきます。`,
  `${M`2+2i`}：長さ ${M`2\sqrt{2}`}、向き ${M`45^\circ`}。`,
  `${M`-1+i`}：長さ ${M`\sqrt{2}`}、向き ${M`135^\circ`}。`,
  `${M`-1-i`}：長さ ${M`\sqrt{2}`}、向き ${M`225^\circ`}。`,
  `${M`2i`}：長さ ${M`2`}、向き ${M`90^\circ`}。`,
  `${M`-1+\sqrt{3}i`}：長さ ${M`2`}、向き ${M`120^\circ`}。`,
  `${M`4i`}：長さ ${M`4`}、向き ${M`90^\circ`}。`,
  `<b class="re">長さ</b> を 見比べると…　${M`2\times\sqrt{2}=2\sqrt{2}`}、${M`\sqrt{2}\times\sqrt{2}=2`}、${M`2\times2=4`}。<b>掛け算</b> に なって います。`,
  `<b class="im">向き</b> は…　${M`90^\circ+45^\circ=135^\circ`}、${M`60^\circ+30^\circ=90^\circ`}。<b>足し算</b> に なって います。`,
  `掛け算は「<b>長さは 掛け算、向きは 足し算</b>」。極形式（長さと 向き）で 見ると、しくみが よく 見えます。`
]);

/* 図で 確かめる */
const gm = PL({x0:-1, x1:3, y0:-1, y1:5, u:66});
const p4 = HD(NO, '図で 確かめる', SEC) + `<div class="bd">
  <div class="l">
    <div class="big" style="font-size:38px">${M`(1+\sqrt{3}i)(\sqrt{3}+i)=4i`}</div>
    <div class="calc" style="font-size:28px;gap:10px">
      <div data-s="1">${M`z_1=1+\sqrt{3}i`}：長さ ${M`\RE{2}`}、向き ${M`\IM{60^\circ}`}</div>
      <div data-s="2">${M`z_2=\sqrt{3}+i`}：長さ ${M`\RE{2}`}、向き ${M`\IM{30^\circ}`}</div>
      <div data-s="3">${M`4i`}：長さ ${M`\RE{2\times2}=4`}、向き ${M`\IM{60^\circ+30^\circ}=90^\circ`}</div>
    </div>
  </div>
  <div class="r">${gm.svg(gm.arr(0,0,1,S3,1) + gm.dot(1,S3,IT('z')+'₁',1,{d:.6}) + gm.ang(60, 1, {r:42, lr:22, d:.6, la:48})
    + gm.arr(0,0,S3,1,2) + gm.dot(S3,1,IT('z')+'₂',2,{d:.6, pos:'se'}) + gm.ang(30, 2, {r:74, lr:24, d:.6, la:11})
    + gm.arr(0,0,0,4,3,{c:'g', w:5}) + gm.dot(0,4,'4'+IT('i'),3,{d:.6}) + gm.ang(90, 3, {r:110, lr:26, d:.6, la:76}))}</div>
</div>` + CAP([
  `最後の 積を、図で 確かめます。`,
  `${M`z_1`} は 長さ ${M`2`}、向き ${M`60^\circ`}。`,
  `${M`z_2`} は 長さ ${M`2`}、向き ${M`30^\circ`}。`,
  `積 ${M`4i`} は、向きが ${M`60^\circ+30^\circ=90^\circ`}（真上）、長さが ${M`2\times2=4`}。表の とおりです。`
]);

/* まとめ（アニメーション なし） */
const p5 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:30px">
  <div class="sum" style="font-size:32px">
    <span>${M`\times i`}</span><span class="ar">→</span><span>原点の まわりに ${M`90^\circ`} 回転</span>
    <span>${M`z_1z_2`}</span><span class="ar">→</span><span><b class="re">長さは 掛け算</b>、<b class="im">向きは 足し算</b></span>
  </div>
</div>` + CAP([`②-2 では、この しくみを 極形式の 式で 確かめます。`]);

const DECK = {title:'②-1 掛け算と長さ・向き', pages:[
  {name:'表紙', html:p0}, {name:'i を 掛けると', html:p1}, {name:'積を 計算する', html:p2},
  {name:'長さと 向きを 比べる', html:p3}, {name:'図で 確かめる', html:p4}, {name:'まとめ', html:p5},
]};
''')

# ---------------------------------------------------------------- ②-2 複素数の積
DECKS['2-2_複素数の積'] = ('②-2 複素数の積', r'''
const NO = '②-2', SEC = '数学C　複素数平面';
const IT = v => `<tspan class="it">${v}</tspan>`;
const SB = (v, i) => `${IT(v)}<tspan baseline-shift="sub" font-size="15">${i}</tspan>`;
const S3 = Math.sqrt(3), S2 = Math.sqrt(2), D = Math.PI/180;

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'複素数の積', sub:'長さは 掛けて、向きは 足す'});

/* 公式と 意味（図：z₁ を θ₂ 回して r₂ 倍） */
const gf = PL({x0:-1, x1:4, y0:-1, y1:4, u:84, ticks:false});
const R1 = 2, T1 = 20, R12 = 3.3, T12 = 62;
const P1 = [R1*Math.cos(T1*D), R1*Math.sin(T1*D)], P12 = [R12*Math.cos(T12*D), R12*Math.sin(T12*D)];
const FIG = (n1, n2) => gf.svg(gf.arr(0,0,...P1,n1) + gf.dot(...P1, SB('z',1), n1, {pos:'se', d:.6}) + gf.ang(T1, n1, {r:50, lab:SB('θ',1), lr:20, d:.6, la:8})
  + gf.text(P1[0]*.55-.1, P1[1]*.55+.3, SB('r',1), 'dp', n1)
  + gf.arr(0,0,...P12,n2,{c:'g', w:5}) + gf.dot(...P12, SB('z',1)+SB('z',2), n2, {d:.6}) + gf.ang(T12, n2, {r:96, from:T1, lab:SB('θ',2), lr:22, d:.6})
  + gf.text(P12[0]*.5-.42, P12[1]*.5+.1, SB('r',1)+SB('r',2), 'dp', n2));
const ZDEF = `<div class="q" style="font-size:24px">${M`z_1=r_1(\cos\theta_1+i\sin\theta_1)`}、<br>${M`z_2=r_2(\cos\theta_2+i\sin\theta_2)`} の とき</div>`;
const p1 = HD(NO, '複素数の積', SEC) + `<div class="bd">
  <div class="l">${ZDEF}
    ${BOX('積', `${M`z_1z_2=`}${FILL(3, M`\RE{r_1r_2}\{\cos(\IM{\theta_1+\theta_2})+i\sin(\IM{\theta_1+\theta_2})\}`, 12)}`)}</div>
  <div class="r">${FIG(1, 2)}</div>
</div>` + CAP([
  `②-1 で 見つけた「長さは 掛け算、向きは 足し算」を、極形式の 式に します。`,
  `${M`z_1`} は 長さ ${M`r_1`}、向き ${M`\theta_1`}。`,
  `${M`z_2`} を 掛けると、長さが ${M`r_2`} 倍、向きが さらに ${M`\theta_2`} 回ります。`,
  `だから ${M`z_1z_2`} は 長さ ${M`r_1r_2`}、向き ${M`\theta_1+\theta_2`}。極形式で 書くと この 式に なります。`
]);
const p2 = HD(NO, '式の 持つ 意味', SEC) + `<div class="bd">
  <div class="l"><div class="q" style="font-size:28px;line-height:2.2">
    大きさ ${M`r`} は ${FILL(1,'積',2.4)}<br>　…　${M`|z_1z_2|=`}${FILL(1, M`\RE{r_1r_2}`, 3)}<br>
    偏角 ${M`\theta`} は ${FILL(2,'和',2.4)}<br>　…　${M`\arg(z_1z_2)=`}${FILL(2, M`\IM{\theta_1+\theta_2}`, 4)}</div></div>
  <div class="r">${FIG(null, null)}</div>
</div>` + CAP([
  `公式の 意味を 言葉で まとめます。`,
  `<b class="re">大きさ（絶対値）は 積</b>：${M`|z_1z_2|=r_1r_2=|z_1||z_2|`}`,
  `<b class="im">偏角は 和</b>：${M`\arg(z_1z_2)=\theta_1+\theta_2=\arg z_1+\arg z_2`}`
]);

/* 導出（加法定理と 色で 対応） */
const C1 = String.raw`\RE{\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2}`, C2 = String.raw`\IM{\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2}`;
const p3 = HD(NO, '導出', SEC) + `<div class="bd col" style="align-items:flex-start;gap:16px">
  <div class="calc" style="font-size:25px;gap:8px">
    <div data-s="1">${M`z_1z_2=r_1r_2(\cos\theta_1+i\sin\theta_1)(\cos\theta_2+i\sin\theta_2)`}</div>
    <div data-s="2">${M`=r_1r_2(\cos\theta_1\cos\theta_2+i\cos\theta_1\sin\theta_2+i\sin\theta_1\cos\theta_2+\DP{i^2}\sin\theta_1\sin\theta_2)`}</div>
    <div data-s="3">${M(`=r_1r_2\\{(${C1})+i(${C2})\\}`)}</div>
    <div data-s="5">${M`=r_1r_2\{\RE{\cos(\theta_1+\theta_2)}+i\IM{\sin(\theta_1+\theta_2)}\}`}</div>
  </div>
  <div class="pbox" data-s="4" style="font-size:23px"><div class="pl2">Point</div>
    ${M`i^2=-1`}、　${M`\RE{\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta}`}、　${M`\IM{\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta}`}</div>
</div>` + CAP([
  `なぜ この 式に なるのか、確かめます。`,
  `${M`r_1r_2`} を 前に 出して、かっこを 展開します。`,
  `4つの 項が でき、最後の 項に ${M`i^2`} が 出て きます。`,
  `${M`i^2=-1`} として、<b class="re">${M`i`} の つかない 項</b> と <b class="im">${M`i`} の つく 項</b> に 分けます。`,
  `この 形は… 数学Ⅱ の <b>加法定理</b> そのものです。`,
  `<b class="re">${M`\cos(\theta_1+\theta_2)`}</b>、<b class="im">${M`\sin(\theta_1+\theta_2)`}</b> に まとまり、公式が 出ました。`
]);

/* 例・問11：極形式に して → 長さを 掛ける・角を 足す → 図 */
function mulPage(o){
  const g = PL(o.R), [a1,b1] = o.z1, [a2,b2] = o.z2, [pa,pb] = o.p;
  const fig = g.arr(0,0,a1,b1,null) + g.dot(a1,b1,SB('z',1),null,{given:true, pos:o.p1||'se'}) + g.ang(o.t1, 1, {r:34, lr:20, fs:17, la:o.l1})
    + g.arr(0,0,a2,b2,null) + g.dot(a2,b2,SB('z',2),null,{given:true, pos:o.p2||'se'}) + g.ang(o.t2, 2, {r:52, lr:20, fs:17, la:o.l2})
    + g.arr(0,0,pa,pb,3,{c:'g', w:5}) + g.ang(o.t1+o.t2, 4, {r:76, lr:24, la:o.l3}) + g.dot(pa,pb,SB('z',1)+SB('z',2),4,{pos:o.pp||'nw', d:.5});
  return HD(NO, o.title, SEC) + `<div class="bd">
    <div class="l">${o.top}
      <div class="calc" style="font-size:26px;gap:6px">${o.lines.map(([t,n])=>`<div data-s="${n}">${typeof t==='string'&&t.startsWith('<')?t:M(t)}</div>`).join('')}</div>
    </div>
    <div class="r">${g.svg(fig)}</div>
  </div>` + CAP(o.cm);
}
const p4 = mulPage({title:'例', R:{x0:-1, x1:3, y0:-1, y1:3, u:96}, z1:[1,1], z2:[S3,1], p:[S3-1, S3+1], t1:45, t2:30, l1:52, l2:12, l3:82, p1:'nw',
  top:`<div class="q" style="font-size:24px"><span class="tag">例</span>${M`z_1=1+i`}、${M`z_2=\sqrt{3}+i`} の とき、<br>積 ${M`z_1z_2`} の 絶対値と 偏角を 求めよ。また、点 ${M`z_1z_2`} を 図示せよ。</div>`,
  lines:[[String.raw`z_1=\sqrt{2}(\cos45^\circ+i\sin45^\circ)`,1], [String.raw`z_2=2(\cos30^\circ+i\sin30^\circ)`,2],
         [String.raw`|z_1z_2|=\RE{\sqrt{2}\times2}=\DP{2\sqrt{2}}`,3], [String.raw`\arg(z_1z_2)=\IM{45^\circ+30^\circ}=\DP{75^\circ}`,4],
         [`<span class="vnote">（確かめ：${M`(1+i)(\sqrt{3}+i)=(\sqrt{3}-1)+(\sqrt{3}+1)i`}）</span>`,5]],
  cm:[`まず、それぞれを 極形式に します（①-4 の 手順）。`, `${M`z_1=1+i`}：長さ ${M`\sqrt{2}`}、向き ${M`45^\circ`}。`, `${M`z_2=\sqrt{3}+i`}：長さ ${M`2`}、向き ${M`30^\circ`}。`,
      `<b class="re">長さは 掛ける</b>：${M`\sqrt{2}\times2=2\sqrt{2}`}。`, `<b class="im">向きは 足す</b>：${M`45^\circ+30^\circ=75^\circ`}。長さ ${M`2\sqrt{2}`}、向き ${M`75^\circ`} の 点が ${M`z_1z_2`} です。`,
      `ふつうに 展開した 結果とも 一致します。`]});
const p5 = mulPage({title:'問11 ⑴', R:{x0:-7, x1:4, y0:-1, y1:7, u:42}, z1:[0,2], z2:[3,3], p:[-6,6], t1:90, t2:45, l1:62, l2:20, l3:150, p1:'nw', p2:'se', pp:'ne',
  top:`<div class="q" style="font-size:24px"><span class="tag">問11</span>積 ${M`z_1z_2`} の 絶対値と<br>偏角を 求めよ。</div><div class="q big" style="font-size:32px">⑴　${M`z_1=2i,\ z_2=3+3i`}</div>`,
  lines:[[String.raw`z_1=2(\cos90^\circ+i\sin90^\circ)`,1], [String.raw`z_2=3\sqrt{2}(\cos45^\circ+i\sin45^\circ)`,2],
         [String.raw`\text{絶対値}\ \ \RE{2\times3\sqrt{2}}=\DP{6\sqrt{2}}`,3], [String.raw`\text{偏角}\ \ \IM{90^\circ+45^\circ}=\DP{135^\circ}`,4],
         [`<span class="vnote">（確かめ：${M`z_1z_2=-6+6i`}）</span>`,5]],
  cm:[`同じ 手順で 解きます。`, `${M`z_1=2i`}：真上なので 長さ ${M`2`}、向き ${M`90^\circ`}。`, `${M`z_2=3+3i`}：長さ ${M`3\sqrt{2}`}、向き ${M`45^\circ`}。`,
      `絶対値は 掛けて ${M`6\sqrt{2}`}。`, `偏角は 足して ${M`135^\circ`}。`, `${M`2i(3+3i)=6i+6i^2=-6+6i`}。図の とおり、長さ ${M`6\sqrt{2}`}、向き ${M`135^\circ`} です。`]});
const p6 = mulPage({title:'問11 ⑵', R:{x0:-4, x1:3, y0:-1, y1:3, u:52}, z1:[S3,1], z2:[-1,S3], p:[-2*S3,2], t1:30, t2:120, l1:12, l2:62, l3:165, p1:'se', p2:'ne', pp:'nw',
  top:`<div class="q big" style="font-size:32px">⑵　${M`z_1=\sqrt{3}+i`}<br>　　${M`z_2=-1+\sqrt{3}i`}</div>`,
  lines:[[String.raw`z_1=2(\cos30^\circ+i\sin30^\circ)`,1], [String.raw`z_2=2(\cos120^\circ+i\sin120^\circ)`,2],
         [String.raw`\text{絶対値}\ \ \RE{2\times2}=\DP{4}`,3], [String.raw`\text{偏角}\ \ \IM{30^\circ+120^\circ}=\DP{150^\circ}`,4],
         [`<span class="vnote">（確かめ：${M`z_1z_2=-2\sqrt{3}+2i`}）</span>`,5]],
  cm:[`⑵ も 同じ 手順です。`, `${M`z_1=\sqrt{3}+i`}：長さ ${M`2`}、向き ${M`30^\circ`}。`, `${M`z_2=-1+\sqrt{3}i`}：長さ ${M`2`}、向き ${M`120^\circ`}（第2象限）。`,
      `絶対値は 掛けて ${M`4`}。`, `偏角は 足して ${M`150^\circ`}。`, `展開すると ${M`-2\sqrt{3}+2i`}。長さ ${M`4`}、向き ${M`150^\circ`} と 一致します。`]});

/* まとめ（アニメーション なし） */
const p7 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:28px">
  ${BOX('複素数の 積', `<span style="font-size:32px">${M`z_1z_2=\RE{r_1r_2}\{\cos(\IM{\theta_1+\theta_2})+i\sin(\IM{\theta_1+\theta_2})\}`}</span>`)}
  <div class="q" style="font-size:29px">${M`|z_1z_2|=\RE{|z_1||z_2|}`}（<b class="re">長さは 積</b>）　${M`\arg(z_1z_2)=\IM{\arg z_1+\arg z_2}`}（<b class="im">向きは 和</b>）</div>
</div>` + CAP([`②-3 では、「掛ける ＝ 伸ばして 回す」を 使って、点を 回転させます。`]);

const DECK = {title:'②-2 複素数の積', pages:[
  {name:'表紙', html:p0}, {name:'複素数の積（公式）', html:p1}, {name:'式の 持つ 意味', html:p2}, {name:'導出', html:p3},
  {name:'例', html:p4}, {name:'問11 ⑴', html:p5}, {name:'問11 ⑵', html:p6}, {name:'まとめ', html:p7},
]};
''')

# ---------------------------------------------------------------- ②-3 掛け算と回転
DECKS['2-3_掛け算と回転'] = ('②-3 掛け算と回転', r'''
const NO = '②-3', SEC = '数学C　複素数平面';
const IT = v => `<tspan class="it">${v}</tspan>`;
const SB = (v, i) => `${IT(v)}<tspan baseline-shift="sub" font-size="15">${i}</tspan>`;
const S3 = Math.sqrt(3), S2 = Math.sqrt(2), D = Math.PI/180;

/* 回る 矢印：原点からの 矢印 (a,b) が n 番で 出て、deg だけ 左回りに 回る（ゴースト） */
function ROT(g, a, b, deg, n, op={}){
  const L = Math.hypot(a, b)*g.u, t0 = Math.atan2(b, a)/D, hl = 14, hw = 7;
  return `<g data-s="${n}"${op.e?` data-e="${op.e}"`:''}><g transform="translate(${g.X(0)} ${g.Y(0)}) rotate(${(-t0).toFixed(2)})">`
    + `<g class="sweep" data-o="${n}" style="--rot:${-deg}deg">`
    + `<line class="swl" x1="0" y1="0" x2="${(L-hl*.8).toFixed(1)}" y2="0"/><polygon class="roth" points="${L.toFixed(1)},0 ${(L-hl).toFixed(1)},${-hw} ${(L-hl).toFixed(1)},${hw}"/>`
    + `</g></g></g>`;
}

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'掛け算と回転', sub:'掛ける ＝ 伸ばして 回す'});

/* 積の 図形的な 意味 */
const g1 = PL({x0:-1, x1:4, y0:-1, y1:4, u:84, ticks:false});
const A1 = [2.4, 1], T = 40, RK = 1.5, t1 = Math.atan2(1, 2.4)/D, L1 = Math.hypot(...A1);
const RT = [L1*Math.cos((t1+T)*D), L1*Math.sin((t1+T)*D)], PR = RT.map(v=>v*RK);
const p1 = HD(NO, '積の 図形的な 意味', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="q hl2" data-s="0" style="font-size:22px">${M`\RE{2}(\cos\IM{60^\circ}+i\sin\IM{60^\circ})`} を 掛ける ＝<br>「<b class="re">2倍に 伸ばして</b>、<b class="im">60° 回す</b>」</div>
    ${BOX('積の 図形的な 意味', `${M`z_2=r(\cos\theta+i\sin\theta)`} の とき、点 ${M`z_1z_2`} は<br>
      点 ${M`z_1`} を 原点の まわりに ${FILL(1, M`\IM{\theta}`, 2.4)} だけ 回転し、<br>原点からの 距離を ${FILL(2, M`\RE{r}`, 2.4)} 倍 した 点<br>
      <span data-s="3">とくに ${M`r=1`} の とき、点 ${M`z_1(\cos\theta+i\sin\theta)`} は<br>点 ${M`z_1`} を 原点の まわりに ${FILL(3, M`\IM{\theta}`, 2.4)} だけ 回転した 点</span>`)}
  </div>
  <div class="r">${g1.svg(g1.arr(0,0,...A1,null) + g1.dot(...A1, SB('z',1), null, {given:true, pos:'se'})
    + ROT(g1, ...A1, T, 1) + g1.ang(t1+T, 1, {from:t1, r:70, lab:IT('θ'), d:1.1, lr:20})
    + g1.arr(0,0,...PR,2,{c:'g', w:5}) + g1.dot(...PR, SB('z',1)+SB('z',2), 2, {d:.6, pos:'ne'})
    + g1.text(PR[0]*.5-.45, PR[1]*.5+.2, `${IT('r')} 倍`, 'dp', 2))}</div>
</div>` + CAP([
  `②-2 で「長さは 掛け算、向きは 足し算」でした。図で 言うと どう なるでしょうか。`,
  `${M`z_2`} の 向きは ${M`\theta`}。掛けると、${M`z_1`} の 向きに ${M`\theta`} が 足されるので、<b class="im">${M`\theta`} だけ 回転</b> します。`,
  `${M`z_2`} の 長さは ${M`r`}。掛けると、長さが <b class="re">${M`r`} 倍</b> に 伸びます。`,
  `長さが ${M`1`} の 数 ${M`\cos\theta+i\sin\theta`} を 掛けると、伸びずに <b>回転だけ</b> します。`
]);

/* 原点の まわりの 回転（i・−1・−i） */
const g2 = PL({x0:-4, x1:4, y0:-4, y1:4, u:54, ticks:false});
const Z = [3, 1];
const p2 = HD(NO, '原点の まわりの 回転', SEC) + `<div class="bd">
  <div class="l" style="gap:12px">
    <div class="q" style="font-size:23px">${M`i=\cos90^\circ+i\sin90^\circ`} など</div>
    <div class="q" style="font-size:25px;line-height:2.1">
      点 ${M`z_1i`} は、点 ${M`z_1`} を ${FILL(1, M`90^\circ`, 2.8)} だけ 回転した 点<br>
      点 ${M`-z_1`} は、点 ${M`z_1`} を ${FILL(2, M`180^\circ`, 2.8)} だけ 回転した 点<br>
      点 ${M`-z_1i`} は、点 ${M`z_1`} を ${FILL(3, M`-90^\circ`, 2.8)} だけ 回転した 点</div>
    <div class="q" data-s="4" style="font-size:22px;line-height:1.9"><span class="mu">（参考）割り算は 逆向きの 回転</span><br>
      点 ${M`\dfrac{z_1}{z_2}`} は、点 ${M`z_1`} を 原点の まわりに ${FILL(4, M`-\theta`, 2.4)} だけ 回転し、原点からの 距離を ${M`\dfrac{1}{r}`} 倍 した 点</div>
  </div>
  <div class="r">${g2.svg(g2.arr(0,0,...Z,null) + g2.dot(...Z, SB('z',1), null, {given:true, pos:'ne'})
    + ROT(g2, ...Z, 90, 1) + g2.dot(-1, 3, SB('z',1)+IT('i'), 1, {d:1.2, pos:'nw'})
    + ROT(g2, ...Z, 180, 2) + g2.dot(-3, -1, '−'+SB('z',1), 2, {d:1.2, pos:'sw'})
    + ROT(g2, ...Z, -90, 3) + g2.dot(1, -3, '−'+SB('z',1)+IT('i'), 3, {d:1.2, pos:'se'}))}</div>
</div>` + CAP([
  `${M`i`}、${M`-1`}、${M`-i`} は、どれも 長さ ${M`1`} の 数。掛けると 回転だけ します。`,
  `${M`i`} は 向き ${M`90^\circ`}。${M`i`} を 掛けると ${M`90^\circ`} 回転（②-1 で 見ました）。`,
  `${M`-1=\cos180^\circ+i\sin180^\circ`}。${M`-1`} 倍は ${M`180^\circ`} 回転で、原点の 反対側へ。`,
  `${M`-i`} は 向き ${M`-90^\circ`}（${M`270^\circ`}）。右回りに ${M`90^\circ`} 回転 です。`,
  `割り算は 掛け算の 逆。向きは 引き算に なるので、逆向き（${M`-\theta`}）に 回転します。`
]);

/* 例・問13：回る 先を 見て → 計算 → 答え */
function rotPage(o){
  const g = PL(o.R), [a,b] = o.z, [ra,rb] = o.r;
  const fig = g.arr(0,0,a,b,null) + g.dot(a, b, o.zl, null, {given:true, pos:o.zp||'se'})
    + ROT(g, a, b, o.deg, 1) + g.ang(Math.atan2(b,a)/D + o.deg, 1, {from:Math.atan2(b,a)/D, r:o.ar||50, lab:o.deg+'°', d:1.1, lr:22, la:o.la})
    + g.arr(0,0,ra,rb,3,{c:'g', w:5}) + g.dot(ra, rb, o.rl, 3, {d:.5, pos:o.rp||'nw'});
  return HD(NO, o.title, SEC) + `<div class="bd">
    <div class="l">${o.top}
      <div class="calc" style="font-size:25px;gap:6px">${o.lines.map(([t,n,d])=>`<div data-s="${n}"${d?` style="--d:${d}s"`:''}>${M(t)}</div>`).join('')}</div>
      ${o.point ? `<div class="pbox" style="font-size:21px;line-height:1.7"><div class="pl2">Point</div>${M`\theta`} 回転 するには ${M`\DP{\cos\theta+i\sin\theta}`} を 掛ける</div>` : ''}
    </div>
    <div class="r">${g.svg(fig)}</div>
  </div>` + CAP(o.cm);
}
const RE = {x0:-3, x1:3, y0:-1, y1:3, u:76, ticks:false};
const EXQ = n => `<div class="q" style="font-size:22px"><span class="tag">例</span>点 ${M`2+2i`} を、原点の まわりに 次の 角だけ 回転した 点を 表す 複素数を 求めよ。</div><div class="q big" style="font-size:32px">${n}</div>`;
const p3 = rotPage({title:'例 ⑴　90° 回転', R:RE, z:[2,2], zl:`2 + 2${IT('i')}`, deg:90, r:[-2,2], rl:`−2 + 2${IT('i')}`, la:112, point:true,
  top: EXQ(`⑴　${M`90^\circ`}`),
  lines:[[String.raw`90^\circ\text{ 回転は }\DP{i}\text{ を 掛ける}`, 2], [String.raw`(2+2i)i=2i+2i^2=\DP{-2+2i}`, 3]],
  cm:[`点 ${M`2+2i`} を ${M`90^\circ`} 回します。`, `まず 図で、どこに 行くかを 見ます。左上の ${M`(-2,\ 2)`} あたり です。`,
      `${M`90^\circ`} 回転は ${M`\cos90^\circ+i\sin90^\circ=i`} を 掛けること。`, `${M`(2+2i)i=-2+2i`}。図の とおりの 点です。`]});
const p4 = rotPage({title:'例 ⑵　45° 回転', R:{...RE, y1:4, u:70}, z:[2,2], zl:`2 + 2${IT('i')}`, deg:45, r:[0,2*S2], rl:`2√2${IT('i')}`, rp:'ne', la:68, point:true,
  top: EXQ(`⑵　${M`45^\circ`}`),
  lines:[[String.raw`(2+2i)(\cos45^\circ+i\sin45^\circ)`, 2], [String.raw`=(2+2i)\left(\tfrac{1}{\sqrt{2}}+\tfrac{1}{\sqrt{2}}i\right)`, 2, .5],
         [String.raw`=\tfrac{1}{\sqrt{2}}(2+2i+2i+2i^2)=\tfrac{4i}{\sqrt{2}}=\DP{2\sqrt{2}i}`, 3]],
  cm:[`今度は ${M`45^\circ`} 回します。`, `${M`2+2i`} は 向き ${M`45^\circ`}。さらに ${M`45^\circ`} 回すと 向き ${M`90^\circ`}、真上に 来ます。`,
      `${M`45^\circ`} 回転 ＝ ${M`\cos45^\circ+i\sin45^\circ`} を 掛ける。値は Point の 表から。`, `${M`2\sqrt{2}i`}。長さ ${M`2\sqrt{2}`} の まま、真上に 来ました。`]});
const p5 = rotPage({title:'例 ⑶　60° 回転', R:RE, z:[2,2], zl:`2 + 2${IT('i')}`, deg:60, r:[1-S3, 1+S3], rl:`(1−√3) + (1+√3)${IT('i')}`, rp:'nw', la:76, point:true,
  top: EXQ(`⑶　${M`60^\circ`}`),
  lines:[[String.raw`(2+2i)(\cos60^\circ+i\sin60^\circ)`, 2], [String.raw`=(2+2i)\left(\tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i\right)`, 2, .5],
         [String.raw`=(1+i)(1+\sqrt{3}i)=\DP{(1-\sqrt{3})+(1+\sqrt{3})i}`, 3]],
  cm:[`${M`60^\circ`} 回します。`, `向きは ${M`45^\circ+60^\circ=105^\circ`}。真上より 少し 左です。`,
      `${M`\cos60^\circ+i\sin60^\circ=\tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i`} を 掛けます。${M`2`} と ${M`\tfrac{1}{2}`} を 先に 掛けると 楽です。`,
      `${M`(1-\sqrt{3})+(1+\sqrt{3})i`}。実部が 少し マイナス なので、真上より 少し 左。図と 合います。`]});
const RQ = {x0:-2, x1:2, y0:-1, y1:3, u:96, ticks:false};
const Q13 = n => `<div class="q" style="font-size:22px"><span class="tag">問13</span>${M`z_1=1+\sqrt{3}i`} とする。点 ${M`z_1`} を 原点の まわりに 次の 角度だけ 回転した 点を 表す 複素数を 求めよ。</div><div class="q big" style="font-size:32px">${n}</div>`;
const Z1L = `1 + √3${IT('i')}`;
const p6 = rotPage({title:'問13 ⑴　30° 回転', R:RQ, z:[1,S3], zl:Z1L, deg:30, r:[0,2], rl:`2${IT('i')}`, rp:'ne', ar:46, la:76,
  top: Q13(`⑴　${M`30^\circ`}`),
  lines:[[String.raw`(1+\sqrt{3}i)(\cos30^\circ+i\sin30^\circ)`, 2], [String.raw`=(1+\sqrt{3}i)\left(\tfrac{\sqrt{3}}{2}+\tfrac{1}{2}i\right)`, 2, .5],
         [String.raw`=\tfrac{\sqrt{3}}{2}+\tfrac{1}{2}i+\tfrac{3}{2}i-\tfrac{\sqrt{3}}{2}=\DP{2i}`, 3]],
  cm:[`${M`z_1=1+\sqrt{3}i`} は 長さ ${M`2`}、向き ${M`60^\circ`}。`, `${M`30^\circ`} 回すと 向き ${M`90^\circ`}。真上の ${M`2i`} に なるはず です。`,
      `${M`\cos30^\circ+i\sin30^\circ=\tfrac{\sqrt{3}}{2}+\tfrac{1}{2}i`} を 掛けます。`, `実部が 消えて ${M`2i`}。図の とおりです。`]});
const p7 = rotPage({title:'問13 ⑵　60° 回転', R:RQ, z:[1,S3], zl:Z1L, deg:60, r:[-1,S3], rl:`−1 + √3${IT('i')}`, ar:46, la:90,
  top: Q13(`⑵　${M`60^\circ`}`),
  lines:[[String.raw`(1+\sqrt{3}i)(\cos60^\circ+i\sin60^\circ)`, 2], [String.raw`=(1+\sqrt{3}i)\left(\tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i\right)`, 2, .5],
         [String.raw`=\tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i+\tfrac{\sqrt{3}}{2}i-\tfrac{3}{2}=\DP{-1+\sqrt{3}i}`, 3]],
  cm:[`今度は ${M`60^\circ`} 回します。`, `向きは ${M`60^\circ+60^\circ=120^\circ`}。`,
      `${M`\cos60^\circ+i\sin60^\circ=\tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i`} を 掛けます。`, `${M`-1+\sqrt{3}i`}。向き ${M`120^\circ`}、長さ ${M`2`} の 点です。`]});
const p8 = rotPage({title:'問13 ⑶　90° 回転', R:RQ, z:[1,S3], zl:Z1L, deg:90, r:[-S3,1], rl:`−√3 + ${IT('i')}`, ar:46, la:105,
  top: Q13(`⑶　${M`90^\circ`}`),
  lines:[[String.raw`90^\circ\text{ 回転は }\DP{i}\text{ を 掛ける}`, 2], [String.raw`(1+\sqrt{3}i)i=i+\sqrt{3}i^2=\DP{-\sqrt{3}+i}`, 3]],
  cm:[`最後は ${M`90^\circ`}。`, `向きは ${M`60^\circ+90^\circ=150^\circ`}。`, `${M`90^\circ`} 回転は ${M`i`} を 掛ける だけ。`, `${M`-\sqrt{3}+i`}。向き ${M`150^\circ`} の 点です。`]});

/* まとめ（アニメーション なし） */
const p9 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('掛け算と 回転', `<span style="font-size:30px">${M`r(\cos\theta+i\sin\theta)`} を 掛ける ＝「<b class="re">${M`r`} 倍に 伸ばして</b>、<b class="im">${M`\theta`} 回す</b>」</span>`)}
  <div class="sum" style="font-size:28px">
    <span>${M`\theta`} 回転</span><span class="ar">→</span><span>${M`\cos\theta+i\sin\theta`} を 掛ける</span>
    <span>${M`\times i`}・${M`\times(-1)`}・${M`\times(-i)`}</span><span class="ar">→</span><span>${M`90^\circ`}・${M`180^\circ`}・${M`-90^\circ`} 回転</span>
  </div>
</div>` + CAP([`③-1 では、同じ 回転を くり返す（${M`n`} 乗）と どう なるかを 見ます。`]);

const DECK = {title:'②-3 掛け算と回転', pages:[
  {name:'表紙', html:p0}, {name:'積の 図形的な 意味', html:p1}, {name:'原点の まわりの 回転', html:p2},
  {name:'例 ⑴　90° 回転', html:p3}, {name:'例 ⑵　45° 回転', html:p4}, {name:'例 ⑶　60° 回転', html:p5},
  {name:'問13 ⑴　30° 回転', html:p6}, {name:'問13 ⑵　60° 回転', html:p7}, {name:'問13 ⑶　90° 回転', html:p8},
  {name:'まとめ', html:p9},
]};
''')

# ---------------------------------------------------------------- ③-1 ド・モアブルの定理
DECKS['3-1_ド・モアブルの定理'] = ('③-1 ド・モアブルの定理', r'''
const NO = '③-1', SEC = '数学C　複素数平面';
const IT = v => `<tspan class="it">${v}</tspan>`;
const SP = (v, k) => `${v}<tspan baseline-shift="super" font-size="15">${k}</tspan>`;
const S3 = Math.sqrt(3), S2 = Math.sqrt(2), D = Math.PI/180;

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'ド・モアブルの定理', sub:'同じ 回転の くり返し'});

/* 同じ 回転の くり返し：w ＝ cos45°＋i sin45° を 次々に 掛ける */
const gw = PL({x0:-1.6, x1:1.6, y0:-1.6, y1:1.6, u:130, grid:false, ticks:false});
const WR = gw.u;
const WP = k => [Math.cos(45*k*D), Math.sin(45*k*D)];
const WL = k => k===1 ? IT('w') : SP(IT('w'), k);
/* k 番目の 点が 出る 番（5〜7乗は まとめて 1回） */
const WS = {1:1, 2:2, 3:3, 4:4, 5:5, 6:5, 7:5, 8:6};
const WPOS = {1:'sw', 2:'se', 3:'se', 4:'ne', 5:'ne', 6:'ne', 7:'nw', 8:'nw'};   // 円の 内側に 名前
const figW = `<circle class="ucirc" cx="${gw.X(0)}" cy="${gw.Y(0)}" r="${WR}"/>` + gw.dot(1, 0, '1', null, {pos:'se'})
  + [1,2,3,4,5,6,7,8].map(k => gw.carc(45*(k-1)+4, 45*k-4, WR+18, WS[k], {d:k>=5&&k<=7 ? (k-5)*.9 : 0, lab:k===1?'45°':''})
      + gw.dot(...WP(k), WL(k), WS[k], {pos:WPOS[k], d:(k>=5&&k<=7 ? (k-5)*.9 : 0)+.6})).join('');
const p1 = HD(NO, '同じ 回転の くり返し', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="q" style="font-size:24px">${M`w=\cos45^\circ+i\sin45^\circ`}（長さ ${M`1`}、向き ${M`45^\circ`}）を 次々に 掛ける。<br><span class="mu" style="font-size:20px">（掛け算：長さは 掛け算、向きは 足し算）</span></div>
    <div class="tbl wt" style="grid-template-columns:repeat(6,auto)">
      <div class="th"></div><div class="th">${M`w`}</div><div class="th">${M`w^2`}</div><div class="th">${M`w^3`}</div><div class="th">${M`w^4`}</div><div class="th">${M`w^8`}</div>
      <div class="th">向き</div><div>${M`45^\circ`}</div><div>${FILL(2, M`90^\circ`, 2.4)}</div><div>${FILL(3, M`135^\circ`, 2.6)}</div><div>${FILL(4, M`180^\circ`, 2.6)}</div><div>${FILL(6, M`360^\circ`, 2.6)}</div>
      <div class="th">値</div><div>${M`w`}</div><div>${FILL(2, M`i`, 2)}</div><div>${FILL(3, M`-\tfrac{1}{\sqrt{2}}+\tfrac{1}{\sqrt{2}}i`, 5.6)}</div><div>${FILL(4, M`-1`, 2)}</div><div>${FILL(6, M`1`, 2)}</div>
    </div>
    <div class="q" data-s="7" style="font-size:25px">→ ${M`w^n`} の 向きは ${FILL(7, M`45^\circ\times n`, 4)}、${M`w^8=`}${FILL(7, M`1`, 1.6)}（1周して 元に 戻る）</div>
  </div>
  <div class="r">${gw.svg(figW)}</div>
</div>` + CAP([
  `長さ ${M`1`}、向き ${M`45^\circ`} の 数 ${M`w`} を、${M`1`} に 次々に 掛けて いきます。`,
  `${M`w`}：向き ${M`45^\circ`}。`,
  `${M`w^2`}：向きは 足し算 なので ${M`45^\circ+45^\circ=90^\circ`}。長さは ${M`1\times1=1`} の まま。真上の ${M`i`} です。`,
  `${M`w^3`}：向き ${M`135^\circ`}。値は ${M`\cos135^\circ+i\sin135^\circ`}。`,
  `${M`w^4`}：向き ${M`180^\circ`}。真左の ${M`-1`} です。`,
  `${M`w^5,\ w^6,\ w^7`} と、${M`45^\circ`} ずつ 円の 上を 進みます。`,
  `${M`w^8`}：向き ${M`45^\circ\times8=360^\circ`}。1周して ${M`1`} に 戻りました。`,
  `${M`n`} 回 掛けると、向きは ${M`45^\circ`} を ${M`n`} 回 足して ${M`45^\circ\times n`}。長さは ${M`1`} の まま です。`
]);

/* ド・モアブルの 定理 */
const gd = PL({x0:-1.6, x1:1.6, y0:-1.6, y1:1.6, u:130, grid:false, ticks:false});
const TH = 40;
const p2 = HD(NO, 'ド・モアブルの定理', SEC) + `<div class="bd">
  <div class="l" style="gap:20px">
    ${BOX('ド・モアブルの定理', `${M`n`} が 整数の とき<br><span style="font-size:32px">${M`(\cos\theta+i\sin\theta)^n=`}${FILL(4, M`\cos\DP{n\theta}+i\sin\DP{n\theta}`, 7)}</span>`)}
    <div class="q" data-s="4" style="font-size:24px">（${M`\theta`} 回転を ${M`n`} 回 くり返す ＝ ${M`n\theta`} 回転）</div>
  </div>
  <div class="r">${gd.svg(`<circle class="ucirc" cx="${gd.X(0)}" cy="${gd.Y(0)}" r="${gd.u}"/>` + gd.dot(1, 0, '1', null, {pos:'se'})
    + [1,2,3].map(k => gd.carc(TH*(k-1)+3, TH*k-3, gd.u+18, k, {lab:IT('θ')}) + gd.dot(Math.cos(TH*k*D), Math.sin(TH*k*D), '', k, {d:.6})).join('')
    + gd.seg(0, 0, Math.cos(3*TH*D), Math.sin(3*TH*D), 4, {c:'g'}) + gd.ang(3*TH, 4, {r:46, lab:'3'+IT('θ'), lr:24, d:.4}))}</div>
</div>` + CAP([
  `①-4 で、${M`\cos\theta+i\sin\theta`} は「長さ ${M`1`}、向き ${M`\theta`} の 数」でした。`,
  `1回 掛けると、${M`\theta`} だけ 回ります。`,
  `2回 掛けると ${M`2\theta`}。長さは ${M`1\times1=1`} の まま。`,
  `3回で ${M`3\theta`}。${M`n`} 回 掛けると、${M`\theta`} を ${M`n`} 回 足して ${M`n\theta`} です。`,
  `だから ${M`(\cos\theta+i\sin\theta)^n`} は、長さ ${M`1`}、向き ${M`n\theta`} の 数。これが ド・モアブルの定理 です。`
]);

/* 例・問16：極形式 → 長さは n 乗、角は n 倍 → 値 */
function dmPage(o){
  const g = PL(o.R), [a,b] = o.z, [ra,rb] = o.res;
  const fig = g.arr(0,0,a,b,null) + g.dot(a,b,o.zl,null,{given:true, pos:o.zp||'se'}) + g.ang(o.t, 1, {r:o.r1||32, lr:20, fs:17, la:o.l1})
    + g.ang(o.t*o.n, 2, {r:o.r2||54, lr:24, la:o.l2}) + g.arr(0,0,ra,rb,3,{c:'g', w:5}) + g.dot(ra, rb, o.rl, 3, {d:.5, pos:o.rp||'nw'});
  return HD(NO, o.title, SEC) + `<div class="bd">
    <div class="l">${o.top}
      <div class="calc" style="font-size:26px;gap:8px">${o.lines.map(([t,n])=>`<div data-s="${n}">${M(t)}</div>`).join('')}</div>
    </div>
    <div class="r">${g.svg(fig)}</div>
  </div>` + CAP(o.cm);
}
const p3 = dmPage({title:'例　(1＋i)⁴ の 値', R:{x0:-5, x1:2, y0:-1, y1:2, u:66, ticks:false}, z:[1,1], zl:`1 + ${IT('i')}`, t:45, n:4, l2:150, res:[-4,0], rl:'−4', rp:'nw',
  top:`<div class="q" style="font-size:26px"><span class="tag">例</span>${M`(1+i)^4`} の 値を 求めよ。</div>`,
  lines:[[String.raw`1+i=\RE{\sqrt{2}}(\cos\IM{45^\circ}+i\sin\IM{45^\circ})\ \text{より}`,1],
         [String.raw`(1+i)^4=\RE{(\sqrt{2})^4}(\cos\IM{180^\circ}+i\sin\IM{180^\circ})`,2], [String.raw`=4\times(-1)=\DP{-4}`,3]],
  cm:[`4回 掛ける 計算を、極形式で 楽に します。`, `まず 極形式に。長さ ${M`\sqrt{2}`}、向き ${M`45^\circ`}。`,
      `4乗 すると、<b class="re">長さは 4回 掛けて ${M`(\sqrt{2})^4=4`}</b>、<b class="im">向きは 4倍 で ${M`45^\circ\times4=180^\circ`}</b>。`,
      `${M`\cos180^\circ=-1`}、${M`\sin180^\circ=0`} なので ${M`-4`}。真左、長さ ${M`4`} の 点です。`]});

/* 例：図示（うずまき） */
const gs = PL({x0:-5, x1:2, y0:-1, y1:3, u:66, ticks:false});
const SPI = [[1,1,`1 + ${IT('i')}`,'se'], [0,2,`(1 + ${IT('i')})²`,'ne'], [-2,2,`(1 + ${IT('i')})³`,'nw'], [-4,0,`(1 + ${IT('i')})⁴`,'nw']];
const p4 = HD(NO, '例　図示する', SEC) + `<div class="bd">
  <div class="l">
    <div class="q" style="font-size:24px">また、${M`1+i`}、${M`(1+i)^2`}、${M`(1+i)^3`}、${M`(1+i)^4`} を 図示せよ。</div>
    <div class="calc" style="font-size:27px;gap:8px">
      <div data-s="2">${M`(1+i)^2=2i`}</div><div data-s="3">${M`(1+i)^3=-2+2i`}</div><div data-s="4">${M`(1+i)^4=-4`}</div>
      <div data-s="5" style="font-size:24px">→ ${M`\IM{45^\circ}`} ずつ 回転し、原点からの 距離は ${M`\RE{\sqrt{2}}`} 倍ずつ</div>
    </div>
  </div>
  <div class="r">${gs.svg(SPI.map(([a,b,l,p],i)=>gs.arr(0,0,a,b,i+1,{c:i===3?'g':'m'}) + gs.dot(a,b,l,i+1,{pos:p, d:.6})).join('')
    + SPI.slice(0,3).map(([a,b],i)=>{ const [c,d] = SPI[i+1]; return `<line class="dash" x1="${gs.X(a)}" y1="${gs.Y(b)}" x2="${gs.X(c)}" y2="${gs.Y(d)}" data-s="5"/>`; }).join(''))}</div>
</div>` + CAP([
  `${M`(1+i)`} を 1回ずつ 掛けた 点を、順に 打って いきます。`,
  `${M`1+i`}：長さ ${M`\sqrt{2}`}、向き ${M`45^\circ`}。`,
  `${M`(1+i)^2=2i`}：向き ${M`90^\circ`}、長さ ${M`2`}。`,
  `${M`(1+i)^3=-2+2i`}：向き ${M`135^\circ`}、長さ ${M`2\sqrt{2}`}。`,
  `${M`(1+i)^4=-4`}：向き ${M`180^\circ`}、長さ ${M`4`}。`,
  `1回 掛ける ごとに ${M`45^\circ`} 回り、${M`\sqrt{2}`} 倍に 伸びて、うずまきの ように 外へ 広がります。`
]);

const p5 = dmPage({title:'問16 ⑴　(1＋√3 i)³', R:{x0:-9, x1:3, y0:-1, y1:3, u:42, ticks:false}, z:[1,S3], zl:`1 + √3${IT('i')}`, t:60, n:3, r1:30, r2:50, l1:30, l2:120, res:[-8,0], rl:'−8', rp:'nw',
  top:`<div class="q" style="font-size:24px"><span class="tag">問16</span>次の 複素数の 値を 求めよ。</div><div class="q big" style="font-size:34px">⑴　${M`(1+\sqrt{3}i)^3`}</div>`,
  lines:[[String.raw`1+\sqrt{3}i=\RE{2}(\cos\IM{60^\circ}+i\sin\IM{60^\circ})\ \text{より}`,1],
         [String.raw`(1+\sqrt{3}i)^3=\RE{2^3}(\cos\IM{180^\circ}+i\sin\IM{180^\circ})`,2], [String.raw`=8\times(-1)=\DP{-8}`,3]],
  cm:[`同じ 手順です。`, `極形式に。長さ ${M`2`}、向き ${M`60^\circ`}。`, `3乗：長さは ${M`2^3=8`}、向きは ${M`60^\circ\times3=180^\circ`}。`, `${M`-8`}。真左、長さ ${M`8`} の 点です。`]});
const p6 = dmPage({title:'問16 ⑵　(1＋i)⁷', R:{x0:-1, x1:9, y0:-9, y1:2, u:40, ticks:false}, z:[1,1], zl:`1 + ${IT('i')}`, t:45, n:7, r1:30, r2:46, l1:22, l2:200, res:[8,-8], rl:`8 − 8${IT('i')}`, rp:'se',
  top:`<div class="q big" style="font-size:34px">⑵　${M`(1+i)^7`}</div>`,
  lines:[[String.raw`1+i=\RE{\sqrt{2}}(\cos\IM{45^\circ}+i\sin\IM{45^\circ})\ \text{より}`,1],
         [String.raw`(1+i)^7=\RE{(\sqrt{2})^7}(\cos\IM{315^\circ}+i\sin\IM{315^\circ})`,2],
         [String.raw`=8\sqrt{2}\left(\tfrac{1}{\sqrt{2}}-\tfrac{1}{\sqrt{2}}i\right)=\DP{8-8i}`,3]],
  cm:[`7回 掛けるのは 大変ですが、極形式なら すぐです。`, `長さ ${M`\sqrt{2}`}、向き ${M`45^\circ`}。`,
      `7乗：長さは ${M`(\sqrt{2})^7=8\sqrt{2}`}、向きは ${M`45^\circ\times7=315^\circ`}（第4象限）。`,
      `${M`\cos315^\circ=\tfrac{1}{\sqrt{2}}`}、${M`\sin315^\circ=-\tfrac{1}{\sqrt{2}}`} なので ${M`8-8i`}。`]});

/* まとめ（アニメーション なし） */
const p7 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('ド・モアブルの定理', `<span style="font-size:32px">${M`(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta`}</span>`)}
  <div class="q" style="font-size:28px">${M`z=r(\cos\theta+i\sin\theta)`} の とき<br>${M`z^n=\RE{r^n}(\cos\IM{n\theta}+i\sin\IM{n\theta})`}（<b class="re">長さは ${M`n`} 乗</b>、<b class="im">向きは ${M`n`} 倍</b>）</div>
</div>` + CAP([`③-2 では、逆に「${M`n`} 乗して ${M`1`} に なる 数」を 探します。`]);

const DECK = {title:'③-1 ド・モアブルの定理', pages:[
  {name:'表紙', html:p0}, {name:'同じ 回転の くり返し', html:p1}, {name:'ド・モアブルの定理', html:p2},
  {name:'例　(1＋i)⁴ の 値', html:p3}, {name:'例　図示する', html:p4},
  {name:'問16 ⑴', html:p5}, {name:'問16 ⑵', html:p6}, {name:'まとめ', html:p7},
]};
''')

# ---------------------------------------------------------------- ③-2 1のn乗根
DECKS['3-2_1のn乗根'] = ('③-2 1のn乗根', r'''
const NO = '③-2', SEC = '数学C　複素数平面';
const IT = v => `<tspan class="it">${v}</tspan>`;
const D = Math.PI/180;
const UCIRC = g => `<circle class="ucirc" cx="${g.X(0)}" cy="${g.Y(0)}" r="${g.u}"/>`;
const PT = t => [Math.cos(t*D), Math.sin(t*D)];

const p0 = coverSlide({kicker:'数学C　複素数平面', no:NO, title:'1のn乗根', sub:'n 回 掛けると 1 に 戻る 数'});

/* n 乗根：z³＝1 の 解 ＝ 3回 掛けると 1 に 戻る 数 */
const g1 = PL({x0:-1.6, x1:1.6, y0:-1.6, y1:1.6, u:130, grid:false, ticks:false});
const p1 = HD(NO, 'n 乗根', SEC) + `<div class="bd">
  <div class="l" style="gap:18px">
    ${BOX('n 乗根', `${M`n`} を 正の 整数、${M`\alpha`} を 複素数と する とき、<br>方程式 ${M`z^n=\alpha`} の 解を ${M`\alpha`} の ${FILL(1, M`n` + ' 乗根', 3.6)} という。`)}
    <div class="q" data-s="2" style="font-size:26px;line-height:1.9">${M`z^3=1`} の 解 ＝ <b class="dp">3回 掛けると ${M`1`} に 戻る 数</b><br>
      <span data-s="3">→ 1回で ${FILL(3, M`120^\circ`, 2.8)} 回転する 数（円周の ${M`3`} 等分点）</span></div>
  </div>
  <div class="r">${g1.svg(UCIRC(g1) + g1.dot(1, 0, '1', null, {pos:'se'})
    + [0,1,2].map(k => g1.carc(120*k+4, 120*(k+1)-4, g1.u+18, 3, {d:k*.9, lab:k===0?'120°':''})).join('')
    + [1,2].map(k => g1.dot(...PT(120*k), '', 3, {d:k*.9+.6})).join('')
    + `<polygon class="tri" points="${[0,120,240].map(t=>`${g1.X(Math.cos(t*D)).toFixed(1)},${g1.Y(Math.sin(t*D)).toFixed(1)}`).join(' ')}" data-s="4"/>`)}</div>
</div>` + CAP([
  `③-1 とは 逆に、「${M`n`} 乗して ${M`\alpha`} に なる 数」を 考えます。`,
  `方程式 ${M`z^n=\alpha`} の 解を、${M`\alpha`} の ${M`n`} <b>乗根</b> と いいます。`,
  `たとえば ${M`z^3=1`} の 解は、「3回 掛けると ${M`1`} に 戻る 数」です。`,
  `3回で ちょうど 1周（${M`360^\circ`}）する には、1回で ${M`360^\circ\div3=120^\circ`} 回れば よい。長さは ${M`1`} の まま です。`,
  `だから 解は、円周を ${M`3`} 等分する 点に なります。`
]);

/* 解く ページ：z＝r(cosθ＋i sinθ) とおく → 長さと 偏角を 比べる → k を 動かす → 図形 */
function rootPage(o){
  const g = PL({x0:-1.6, x1:1.6, y0:-1.6, y1:1.6, u:122, grid:false, ticks:false});
  const n = o.n, ks = [...Array(n).keys()], step = 360/n, KS = 5;   // 番 5 で k を 順に、最後の 番で 図形
  const fig = UCIRC(g) + ks.map(k => g.seg(0, 0, ...PT(step*k), KS, {c:'m', d:k*.7}) + g.dot(...PT(step*k), `${IT('k')}=${k}`, KS, {d:k*.7+.4, pos:o.pos[k]})).join('')
    + (o.shape ? `<polygon class="tri" points="${ks.map(k=>`${g.X(Math.cos(step*k*D)).toFixed(1)},${g.Y(Math.sin(step*k*D)).toFixed(1)}`).join(' ')}" data-s="${o.shape}"/>` : '');
  return HD(NO, o.title, SEC) + `<div class="bd">
    <div class="l" style="gap:10px">${o.top}
      <div class="calc" style="font-size:23px;gap:3px">${o.lines.map(([t,s])=>`<div data-s="${s}">${t.startsWith('<')?t:M(t)}</div>`).join('')}</div>
    </div>
    <div class="r" style="flex-direction:column;gap:8px">
      <div class="pbox" style="font-size:20px;line-height:1.7"><div class="pl2">Point</div>${M`(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta`}<br>偏角：${M`\DP{+360^\circ\times k}`}</div>
      ${g.svg(fig, 'rt')}
    </div>
  </div>` + CAP(o.cm);
}
const p2 = rootPage({title:'例　z³＝1 を 解く', n:3, shape:7, pos:['se','nw','sw'],
  top:`<div class="q" style="font-size:26px"><span class="tag">例</span>方程式 ${M`z^3=1`} を 解け。</div>`,
  lines:[[String.raw`z=r(\cos\theta+i\sin\theta)\ \text{とおくと}\ \ z^3=\RE{r^3}(\cos\IM{3\theta}+i\sin\IM{3\theta})`,1],
         [String.raw`1=\cos0^\circ+i\sin0^\circ\ \text{より}`,2],
         [String.raw`\RE{r^3=1},\ \ \IM{3\theta=0^\circ+360^\circ\times k}\ (k\text{ は 整数})`,3],
         [String.raw`r=1,\ \ \theta=120^\circ\times k`,4],
         [String.raw`0^\circ\leqq\theta<360^\circ\ \text{より}\ \ k=0,\ 1,\ 2`,5],
         [String.raw`z=\DP{1,\ -\tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i,\ -\tfrac{1}{2}-\tfrac{\sqrt{3}}{2}i}`,6],
         [`<span style="font-size:24px">解を 表す 点は、点 ${M`1`} を 頂点と する ${FILL(7,'正三角形',5)} の 頂点。</span>`,7]],
  cm:[`${M`z^3=1`} を、極形式で 解きます。`,
      `${M`z`} を 極形式で おくと、ド・モアブルの定理で ${M`z^3`} は 長さ ${M`r^3`}、向き ${M`3\theta`}。`,
      `右辺の ${M`1`} も 極形式に します。長さ ${M`1`}、向き ${M`0^\circ`}。`,
      `<b class="re">長さ</b> と <b class="im">向き</b> を 比べます。向きは 1周（${M`360^\circ`}）回ると 同じ なので、${M`0^\circ`} だけで なく ${M`360^\circ,\ 720^\circ,\ \cdots`} でも よい（<b>${M`+360^\circ\times k`}</b>）。`,
      `${M`r`} は 正の 数 なので ${M`r=1`}。${M`\theta=120^\circ\times k`}。`,
      `${M`k=0,1,2`} で ${M`0^\circ,\ 120^\circ,\ 240^\circ`}。${M`k=3`} は ${M`360^\circ`} で ${M`k=0`} と 同じ 点に 戻るので、ここまで です。`,
      `${M`\cos120^\circ+i\sin120^\circ`}、${M`\cos240^\circ+i\sin240^\circ`} を 計算して、3つの 解。`,
      `3つの 点は 円周を 3等分 する ので、<b>正三角形</b> の 頂点に なります。`]});

const p3 = rootPage({title:'問17　1の4乗根', n:4, shape:null, pos:['se','ne','nw','se'],
  top:`<div class="q" style="font-size:26px"><span class="tag">問17</span>${M`1`} の ${M`4`} 乗根を 求めよ。</div>`,
  lines:[[String.raw`z=r(\cos\theta+i\sin\theta)\ \text{とおくと}\ \ z^4=\RE{r^4}(\cos\IM{4\theta}+i\sin\IM{4\theta})`,1],
         [String.raw`1\ \text{を 極形式で 表すと}\ \ 1=\cos0^\circ+i\sin0^\circ`,2],
         [String.raw`\text{絶対値と 偏角を 比較して}\ \ \RE{r^4=1},\ \IM{4\theta=0^\circ+360^\circ\times k}`,3],
         [String.raw`\text{よって}\ \ r=1,\ \ \theta=90^\circ\times k`,4],
         [String.raw`0^\circ\leqq\theta<360^\circ\ \text{より}\ \ k=0,\ 1,\ 2,\ 3\ \ (\theta=0^\circ,\ 90^\circ,\ 180^\circ,\ 270^\circ)`,5],
         [String.raw`\text{したがって、}1\text{ の }4\text{ 乗根は}\ \ \DP{1,\ i,\ -1,\ -i}`,6]],
  cm:[`${M`1`} の ${M`4`} 乗根 ＝ ${M`z^4=1`} の 解。例と 同じ 手順です。`, `ド・モアブルの定理で ${M`z^4`} は 長さ ${M`r^4`}、向き ${M`4\theta`}。`,
      `${M`1`} は 長さ ${M`1`}、向き ${M`0^\circ`}。`, `長さと 偏角を 比べます。偏角は ${M`+360^\circ\times k`}。`, `${M`r=1`}、${M`\theta=360^\circ\div4\times k=90^\circ\times k`}。`,
      `${M`k=0,1,2,3`}。1回で ${M`90^\circ`} 回る 数 ── ②-1 で 見た ${M`i`} の 仲間です。`, `${M`1,\ i,\ -1,\ -i`}。どれも 4回 掛けると ${M`1`} に 戻ります。`]});

/* 問18：図示して 図形を 答える */
const g4 = PL({x0:-1.6, x1:1.6, y0:-1.6, y1:1.6, u:130, grid:false, ticks:false});
const P4 = [[1,0,'1','se'],[0,1,IT('i'),'ne'],[-1,0,'−1','nw'],[0,-1,'−'+IT('i'),'se']];
const p4 = HD(NO, '問18', SEC) + `<div class="bd">
  <div class="l" style="gap:18px">
    <div class="q" style="font-size:25px"><span class="tag">問18</span>問17で 求めた ${M`1`} の ${M`4`} 乗根を 表す 点を、複素数平面上に 図示せよ。<br>また、それらの 点を 結んで できる 図形は 何か。</div>
    <div class="q" data-s="2" style="font-size:27px">点 ${M`1`} を 1つの 頂点と する ${FILL(2,'正方形',4)}</div>
  </div>
  <div class="r">${g4.svg(UCIRC(g4) + P4.map(([a,b,l,p],i)=>g4.dot(a,b,l,1,{d:i*.4, pos:p})).join('')
    + `<polygon class="tri" points="${P4.map(([a,b])=>`${g4.X(a)},${g4.Y(b)}`).join(' ')}" data-s="2"/>`)}</div>
</div>` + CAP([
  `問17の 4つの 点を、図に 打ちます。`,
  `${M`1,\ i,\ -1,\ -i`}。円周を ${M`4`} 等分する 点です。`,
  `結ぶと <b>正方形</b>。${M`z^n=1`} の 解は、点 ${M`1`} を 頂点と する <b>正 ${M`n`} 角形</b> の 頂点に なります。`
]);

/* まとめ（アニメーション なし） */
const g5 = PL({x0:-1.4, x1:1.4, y0:-1.4, y1:1.4, u:90, grid:false, ticks:false});
const SH = n => g5.svg(UCIRC(g5) + `<polygon class="tri" points="${[...Array(n).keys()].map(k=>`${g5.X(Math.cos(360/n*k*D)).toFixed(1)},${g5.Y(Math.sin(360/n*k*D)).toFixed(1)}`).join(' ')}"/>`
  + [...Array(n).keys()].map(k=>g5.dot(...PT(360/n*k), '', null)).join(''), 'sm3');
const p5 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:20px">
  ${BOX('1 の n 乗根', `${M`z^n=1`} の 解 ＝ ${M`n`} 回 掛けると ${M`1`} に 戻る 数<br>${M`z=\cos\dfrac{360^\circ\times k}{n}+i\sin\dfrac{360^\circ\times k}{n}`}<br>（${M`k=0,1,\cdots,n-1`}）`)}
  <div style="display:flex;gap:30px;align-items:center;justify-content:center">
    <div style="text-align:center">${SH(3)}<div class="q" style="font-size:22px">${M`n=3`}：正三角形</div></div>
    <div style="text-align:center">${SH(4)}<div class="q" style="font-size:22px">${M`n=4`}：正方形</div></div>
  </div>
</div>` + CAP([`解は 円周の ${M`n`} 等分点。点 ${M`1`} を 頂点と する 正 ${M`n`} 角形の 頂点に なります。`]);

const DECK = {title:'③-2 1のn乗根', pages:[
  {name:'表紙', html:p0}, {name:'n 乗根', html:p1}, {name:'例　z³＝1 を 解く', html:p2},
  {name:'問17　1の4乗根', html:p3}, {name:'問18　図示と 図形', html:p4}, {name:'まとめ', html:p5},
]};
''')
