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
