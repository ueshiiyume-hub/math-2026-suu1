"""２学期期末考査まで：①-6〜③-4 の デッキ（プリントの 画像を 背景に して、空らんに 答えを 出す）
build_kimatsu.py から 読みこまれる。@@IMG:ページ:x1,y1,x2,y2@@ は プリントの その部分の 画像に なる。
座標は すべて プリント（PDF）の pt。"""

COMMON = r'''
const IMG = s => s;
const A = (s,r,h,fs,al) => ({s,r,h,fs,al});
const MK = (m,r,e) => ({m,r,e});
const JA = t => `<span class="ja">${t}</span>`;
const FX = (n,d) => KF(n,d);
'''

XCOMMON = r'''
/* x軸との 共有点（②-1・②-2）の 部品（プリントの 配置どおり。座標は PDF の pt。生徒が 書きこむので 枠の 位置は 変えない）
   2行目と 3行目の ＝ は 同じ x に そろえる */
const T  = (r,h,fs=10.5,cls='') => ({r,h,fs,cls});
const BG = (r,cls) => `<rect class="${cls}" x="${r[0]}" y="${r[1]}" width="${(r[2]-r[0]).toFixed(1)}" height="${(r[3]-r[1]).toFixed(1)}"/>`;
const XA = (s,r,h,fs=12,cls='xan') => ({s,r,h,fs,cls,al:'c'});
const LBL = (y) => [
  T([314.6,y,430,y+11],`<span class="ja"><i class="math">x</i>軸との共有点の<i class="math">x</i>座標</span>`),
  T([314.6,y+31.5,430,y+42.5],`<span class="ja"><i class="math">x</i>軸との共有点の個数</span>`),
  T([314.6,y+61.5,430,y+72.5],`<span class="ja">グラフの概形</span>`)];
/* { と 緑の 矢印（プリントの 色） */
const BRC = (y0,y1,s) => { const m=(y0+y1)/2;
  return `<path d="M311 ${y0} Q303 ${y0} 303 ${y0+10} L303 ${m-6.5} Q303 ${m} 299.8 ${m} Q303 ${m} 303 ${m+6.5} L303 ${y1-10} Q303 ${y1} 311 ${y1}" fill="none" stroke="#d7e4bd" stroke-width="2.25" stroke-linecap="round"/>`
       + `<g class="gs" data-s="${s}"><path d="M234 ${y1-18} L253 ${y0+33} L280 ${y0+33}" fill="none" stroke="#d7e4bd" stroke-width="6" stroke-linejoin="round"/><polygon points="278,${y0+25} 289,${y0+33} 278,${y0+41}" fill="#d7e4bd"/></g>`; };
/* グラフの 枠の x軸 */
const AX = (ay) => `<line x1="410" y1="${ay}" x2="499" y2="${ay}" stroke="#555" stroke-width=".8"/><polygon points="501,${ay} 497,${ay-1.6} 497,${ay+1.6}" fill="#555"/><text class="pgt" x="497" y="${ay-3}" font-style="italic">x</text>`;

'''

def add(decks):
    # ------------------------------------------------------------ ①-6 実数解の個数（1枚に 1つの ことを 大きく）
    decks['1-6_実数解の個数'] = ('①-6 実数解の個数', COMMON + r"""
const KK = KIMATSU + '　①-6';
const POL = `<div class="fpol"><div class="fa math">D ＝ b${P2} − 4ac</div><div class="fv">プラス・0・マイナス</div><div class="fb math">2個・1個・0個</div></div>`;
const L  = (s,h,cls='') => `<div class="dl lh ${cls}" data-s="${s}">${h}</div>`;
const OR = t => `<span class="hlo">${t}</span>`;
const DIM = (o,t) => `<span class="dimx" data-o="${o}">${t}</span>`;
const RES = (s,h) => `<div class="dres lh" data-s="${s}">${h}</div>`;

/* ± から 枝が 分かれる 図。kind：'two' 2つ / 'one' 重なる / 'none' 実数に ない */
function BR(kind, s, start, top, bot){
  const P = (d,cls='') => `<path class="${cls}" pathLength="1" d="${d}"/>`;
  let svg = '', lab = '';
  if(kind==='two'){
    svg = P('M150 150 C210 150 230 70 300 70') + P('M150 150 C210 150 230 230 300 230')
        + `<text class="brs" x="190" y="92">＋</text><text class="brs" x="190" y="230">−</text>`;
    lab = `<div class="brl" style="left:310px;top:44px">${top}</div><div class="brl" style="left:310px;top:204px">${bot}</div>`;
  } else if(kind==='one'){
    svg = P('M150 150 C210 150 220 80 270 100 C300 112 300 140 320 150') + P('M150 150 C210 150 220 220 270 200 C300 188 300 160 320 150')
        + `<text class="brs" x="186" y="84">＋0</text><text class="brs" x="186" y="240">−0</text>`;
    lab = `<div class="brl one" style="left:330px;top:124px">${top}</div>`;
  } else {
    svg = P('M150 150 C210 150 230 70 290 70','brx') + P('M150 150 C210 150 230 230 290 230','brx')
        + `<g class="brc"><path d="M290 54 L322 86 M322 54 L290 86"/><path d="M290 214 L322 246 M322 214 L290 246"/></g>`;
    lab = `<div class="brl no" style="left:340px;top:126px">${top}</div>`;
  }
  return `<div class="br lh" data-s="${s}"><div class="brst">${start}</div><svg width="520" height="300" viewBox="0 0 520 300">${svg}</svg>${lab}</div>`;
}

/* 2枚目：問いかけ */
const q0 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="dq0 math">
      <div>①　x${P2} ＋ 2x ${K('o','− 5')} ＝ 0</div>
      <div>②　x${P2} ＋ 2x ${K('o','＋ 1')} ＝ 0</div>
      <div>③　x${P2} ＋ 2x ${K('o','＋ 7')} ＝ 0</div>
    </div>
    <div class="dbub lh" data-s="1">解は それぞれ<br><b>何個</b> ある？</div>
  </div>
  ${cbar([
    `3つの 2次方程式。　ちがうのは <b>数だけの項</b>（−5、＋1、＋7）だけ。`,
    `それぞれ 解は <b>何個</b> あるかな？　まずは 解の公式で 解いてみよう。`
  ])}`;

/* 3〜5枚目：実際に 解いてみる */
const solve = (n, eq, lines, br, res, cms) => `
  <div class="card abs dcard">${EQTAPE}
    <div class="dt math">${n}　${eq}</div>
    <div class="dls math">${lines.map((h,i)=>L(i+1,h)).join('')}</div>
    ${br}
    ${RES(lines.length+2, res)}
  </div>
  ${cbar(cms)}`;
const s1 = solve('①', `x${P2} ＋ 2x − 5 ＝ 0`,
  [`x ＝ ${KF(`−2 ± ${SQ(OR('4 ＋ 20'))}`,'2')}`, `＝ ${KF(`−2 ± ${SQ(OR('24'))}`,'2')} ＝ ${KF(`−2 ± 2${SQ('6')}`,'2')}`, `＝ −1 ± ${SQ('6')}`],
  BR('two', 4, `−1 ± ${SQ('6')}`, `−1 ＋ ${SQ('6')}`, `−1 − ${SQ('6')}`),
  `実数解 <b>2</b> 個`, [
  `① ${M('x² ＋ 2x − 5 ＝ 0')} を 解の公式で 解いてみよう。`,
  `ルートの中は ${M('4 ＋ 20')}。`,
  `${M('√24 ＝ 2√6')}。`,
  `約分して ${M('x ＝ −1 ± √6')}。`,
  `<b>±</b> が あるので、<b>＋ の方</b> と <b>− の方</b> に 分かれる。`,
  `ちがう 2つの 解 → 実数解は <b>2個</b>。`]);
const s2 = solve('②', `x${P2} ＋ 2x ＋ 1 ＝ 0`,
  [`x ＝ ${KF(`−2 ± ${SQ(OR('4 − 4'))}`,'2')}`, `＝ ${KF(`−2 ± ${SQ(OR('0'))}`,'2')}`, `＝ −1 ± 0`],
  BR('one', 4, '−1 ± 0', '−1'),
  `実数解 <b>1</b> 個（重解）`, [
  `② ${M('x² ＋ 2x ＋ 1 ＝ 0')} を 解いてみよう。`,
  `ルートの中は ${M('4 − 4')}。`,
  `${M('4 − 4 ＝ 0')}。　ルートの中が <b>0</b>！`,
  `${M('√0 ＝ 0')} なので ${M('−1 ± 0')}。`,
  `＋0 も −0 も 同じ。　2つの 枝が <b>重なって 1つ</b> に なる。`,
  `解は −1 だけ → 実数解は <b>1個</b>（<b>重解</b>）。`]);
const s3 = solve('③', `x${P2} ＋ 2x ＋ 7 ＝ 0`,
  [`x ＝ ${KF(`−2 ± ${SQ(OR('4 − 28'))}`,'2')}`, `＝ ${KF(`−2 ± ${SQ(OR('−24'))}`,'2')}`, `<span class="ja dno">2乗して マイナスに なる数は ない</span>`],
  BR('none', 4, `${SQ('−24')}`, '実数に ない'),
  `実数解 <b>0</b> 個`, [
  `③ ${M('x² ＋ 2x ＋ 7 ＝ 0')} を 解いてみよう。`,
  `ルートの中は ${M('4 − 28')}。`,
  `${M('4 − 28 ＝ −24')}。　ルートの中が <b>マイナス</b>！`,
  `${M('√−24')} は、2乗して −24 に なる数。　でも 2乗して マイナスに なる 数は <b>ない</b>。`,
  `＋ の方も − の方も 進めない。`,
  `実数解は <b>0個</b>。`]);

/* 6枚目：比べて 気づく */
const cmp = (n, root, res) => `<div class="drow">
    <span class="dn">${n}</span>
    <span class="math">x ＝ ${KF(`${DIM(1,'−2 ±')} ${SQ(tm('o',root,1))}`, DIM(1,'2'))}</span>
    <span class="dar lh" data-s="2">→ ${res}</span></div>`;
const s4 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="drows">${cmp('①','24','<b>2</b> 個')}${cmp('②','0','<b>1</b> 個')}${cmp('③','−24','<b>0</b> 個')}</div>
    <div class="dmsg lh" data-s="3">解の 個数を 決めているのは <b>ルートの中</b> だけ！</div>
  </div>
  ${cbar([
    `3つを 並べて 比べてみよう。`,
    `−2 ± や 分母の 2 は 3つとも 同じ。　ちがうのは <b>ルートの中</b> だけ。`,
    `ルートの中が <b>プラス</b> → 2個、<b>0</b> → 1個、<b>マイナス</b> → 0個。`,
    `つまり、解の 個数を 決めているのは <b>ルートの中</b> だけ！`])}`;

/* 7枚目：解を 求めなくていい → 判別式 */
const s5 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="dfx math">x ＝ ${KF(`${DIM(1,'−b ±')} ${SQ(tm('r',`b${P2} − 4ac`,1))}`, DIM(1,'2a'))}</div>
    <div class="dpt lh" data-s="2">ここだけ 計算すれば<br>個数が わかる！</div>
    <div class="dD lh" data-s="3"><span class="ja">判別式</span>　<span class="math">D ＝ b${P2} − 4ac</span></div>
  </div>
  ${cbar([
    `個数を 知りたい だけ なのに、毎回 解を 最後まで 求めるのは 大変…`,
    `個数を 決めるのは <b>ルートの中</b> だけ。　−b や 2a は 個数に 関係ない。`,
    `だから <b>解を 求めなくても</b>、ルートの中 ${M('b² − 4ac')} だけ 計算すれば 個数が わかる！`,
    `この ${M('b² − 4ac')} を <b>判別式</b> と いい、<b>D</b> で 表す。`])}`;

/* 8枚目：まとめ（アニメーションなし） */
const card = (cls, d, n, sub) => `<div class="card dsc ${cls}"><div class="dsc-d math">${d}</div><div class="dsc-n">実数解 <b>${n}</b> 個</div><div class="dsc-s">${sub}</div></div>`;
const s6 = `
  <div class="end-h"><h2>判別式 D ＝ b${P2} − 4ac</h2></div>
  <div class="dsum">${card('c1','D ＞ 0','2','プラス')}${card('c2','D ＝ 0','1','0（重解）')}${card('c3','D ＜ 0','0','マイナス')}</div>
  ${cbar([`<b>D の 符号</b> だけで 実数解の 個数が わかる。　プラス → 2個、0 → 1個（重解）、マイナス → 0個。`])}`;

/* 9〜11枚目：例 */
const ex = (n, eq, abc, b2, ac, d, sign, row, ans, cms) => `
  <div class="card abs dcard">${EQTAPE}
    <div class="dt math">${n}　${eq}</div>
    <div class="dabc lh" data-s="1">${abc}</div>
    <div class="dxr math"><span>D ＝</span>
      <span class="dbx g"><span class="dnt lh" data-s="2">${b2[0]}</span><span class="lh" data-s="2">${b2[1]}</span></span>
      <span class="dbx o"><span class="dnt lh" data-s="3">${ac[0]}</span><span class="lh" data-s="3">${ac[1]}</span></span>
      <span>＝</span><span class="dbx b"><span class="lh" data-s="4">${d}</span></span>
      <span class="dsg lh" data-s="5">${sign}</span></div>
    <div class="dans"><span class="ja">実数解の個数は</span><span class="dabx"><span class="lh" data-s="6">${ans}</span></span><span class="ja">個</span></div>
    <div class="dtb">
      <div class="dtr" data-o="${row===0?5:99}"><span class="math">D ＞ 0</span> → 2個</div>
      <div class="dtr" data-o="${row===1?5:99}"><span class="math">D ＝ 0</span> → 1個</div>
      <div class="dtr" data-o="${row===2?5:99}"><span class="math">D ＜ 0</span> → 0個</div>
    </div>
  </div>
  <div class="abs r done pgdone" data-s="6"><div class="seal">完成！</div></div>
  ${cbar(cms)}`;
const ABC = (a,b,c) => `${KA(`a ＝ ${a}`)}　${KB(`b ＝ ${b}`)}　${KC(`c ＝ ${c}`)}`;
const e1 = ex('⑴', `2x${P2} ＋ 3x − 1 ＝ 0`, ABC(2,3,'−1'), [`3${P2}`,'9'], ['−4 × 2 × (−1)','＋ 8'], '17', 'プラス', 0, '2', [
  `例 ⑴ ${M('2x² ＋ 3x − 1 ＝ 0')} の 実数解の 個数を 求めよう。　解は 求めなくて いい！`,
  `a・b・c を 読みとる。　a ＝ 2、b ＝ 3、c ＝ −1。`,
  `${M('b² ＝ 3² ＝ 9')}`,
  `${M('−4ac ＝ −4 × 2 × (−1) ＝ ＋8')}`,
  `${M('D ＝ 9 ＋ 8 ＝ 17')}`,
  `D は <b>プラス</b>。`,
  `だから 実数解は <b>2個</b>。　<b>完成！</b>`]);
const e2 = ex('⑵', `x${P2} ＋ 10x ＋ 25 ＝ 0`, ABC(1,10,25), [`10${P2}`,'100'], ['−4 × 1 × 25','− 100'], '0', '0', 1, '1', [
  `例 ⑵ ${M('x² ＋ 10x ＋ 25 ＝ 0')} の 実数解の 個数を 求めよう。`,
  `a ＝ 1、b ＝ 10、c ＝ 25。`,
  `${M('b² ＝ 10² ＝ 100')}`,
  `${M('−4ac ＝ −4 × 1 × 25 ＝ −100')}`,
  `${M('D ＝ 100 − 100 ＝ 0')}`,
  `D は <b>0</b>。`,
  `だから 実数解は <b>1個</b>（重解）。　<b>完成！</b>`]);
const e3 = ex('⑶', `3x${P2} − 4x ＋ 2 ＝ 0`, ABC(3,'−4',2), [`(−4)${P2}`,'16'], ['−4 × 3 × 2','− 24'], '−8', 'マイナス', 2, '0', [
  `例 ⑶ ${M('3x² − 4x ＋ 2 ＝ 0')} の 実数解の 個数を 求めよう。`,
  `a ＝ 3、b ＝ −4、c ＝ 2。`,
  `${M('b² ＝ (−4)² ＝ 16')}。　b が マイナスでも 2乗すると プラス！`,
  `${M('−4ac ＝ −4 × 3 × 2 ＝ −24')}`,
  `${M('D ＝ 16 − 24 ＝ −8')}`,
  `D は <b>マイナス</b>。`,
  `だから 実数解は <b>0個</b>。　<b>完成！</b>`]);

const DECK = {title:'①-6 実数解の個数', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">実数解</span>の<br>個数', '判別式 D で 調べる', '解を 求めなくても わかる！', POL, 'D の 符号')},
  {name:'問い', html:q0}, {name:'①', html:s1}, {name:'②', html:s2}, {name:'③', html:s3},
  {name:'比べる', html:s4}, {name:'判別式', html:s5}, {name:'まとめ', html:s6},
  {name:'⑴', html:e1}, {name:'⑵', html:e2}, {name:'⑶', html:e3},
  {name:'終', html:endF(KK + '　実数解の個数', POL)}
]};
""")

    # ------------------------------------------------------------ ②-1 x軸との共有点（1枚に 1つの ことを 大きく）
    decks['2-1_x軸との共有点'] = ('②-1 x軸との共有点', COMMON + XCOMMON + r"""
const KK = KIMATSU + '　②-1';
const POL = `<div class="fpol"><div class="fa math">y ＝ x${P2} − 2x − 3</div><div class="fv">y ＝ 0 と する</div><div class="fb math">x ＝ −1, 3</div></div>`;
const L  = (s,h,cls='') => `<div class="dl lh ${cls}" data-s="${s}"><span>${h}</span></div>`;

/* グラフ（px）：x軸と 下に凸の 放物線 y ＝ k(x − r1)(x − r2)。 o = {w,h,ay:x軸の 高さ, cx:中心の x, sc:1目もりの px, k, r:[r1,r2], top:かき始める 高さ,
   sd:点の 番, sc2:放物線の 番, lab:[html,html]（点の 下の 文字）, ls:文字の 番} */
function GR(o){
  const X = x => o.w/2 + (x-o.cx)*o.sc, Yp = x => o.ay - o.k*(x-o.r[0])*(x-o.r[1]);
  const m = (o.r[0]+o.r[1])/2, dep = o.k*(m-o.r[0])*(m-o.r[1]);              // 頂点の 深さ（マイナス）
  const hw = Math.sqrt(((o.ay-o.top) - dep)/o.k);                            // かき始める x の はば
  let d = ''; for(let i=0;i<=80;i++){ const x = m-hw+2*hw*i/80; d += (i?'L':'M')+X(x).toFixed(1)+' '+Yp(x).toFixed(1)+' '; }
  const dots = o.r.map(x=>`<circle class="gdot" cx="${X(x).toFixed(1)}" cy="${o.ay}" r="9"/>`).join('');
  const labs = (o.lab||[]).map((h,i)=>`<div class="glab lh" data-s="${o.ls??o.sd}" style="left:${(X(o.r[i])+(i?1:-1)*(o.lo||0)).toFixed(1)}px;top:${o.ay+16}px"><span>${h}</span></div>`).join('');
  return `<div class="gbox" style="width:${o.w}px;height:${o.h}px">
    <svg width="${o.w}" height="${o.h}" viewBox="0 0 ${o.w} ${o.h}">
      <line class="gax" x1="16" y1="${o.ay}" x2="${o.w-18}" y2="${o.ay}"/><polygon class="gah" points="${o.w-6},${o.ay} ${o.w-22},${o.ay-7} ${o.w-22},${o.ay+7}"/>
      <text class="gxl" x="${o.w-24}" y="${o.ay+30}">x</text>
      ${o.sc2!==undefined?`<path class="curve gcv" data-s="${o.sc2}" pathLength="1" d="${d}"/>`:''}
      <g class="gs" data-s="${o.sd}">${dots}</g>
      ${o.yax!==undefined?`<g class="gya" data-o="${o.yax}"><line x1="${X(0).toFixed(1)}" y1="${o.h-8}" x2="${X(0).toFixed(1)}" y2="14"/><polygon points="${X(0).toFixed(1)},2 ${(X(0)-7).toFixed(1)},18 ${(X(0)+7).toFixed(1)},18"/><text x="${(X(0)+12).toFixed(1)}" y="22">y</text><text class="go" x="${(X(0)-24).toFixed(1)}" y="${o.ay+26}">O</text></g>`:''}
    </svg>${labs}</div>`;
}
/* プリントの 緑の 矢印（式 → 答え） */
const GA = (s) => `<svg class="xga gs" data-s="${s}" width="150" height="90" viewBox="0 0 150 90"><path d="M8 82 L56 26 L128 26" fill="none" stroke="#c9dca6" stroke-width="12" stroke-linejoin="round"/><polygon points="122,8 146,26 122,44" fill="#c9dca6"/></svg>`;
/* 右の 答えの 欄（プリントの { と 水色の 枠） */
const XR = (xs, xh, ns, nh, tall) => `<div class="xrp">
    <div class="xbr"></div>
    <div class="xrow"><span class="xlb">x軸との<br>共有点の <i class="math">x</i>座標</span><span class="xbx${tall?' tall':''}"><span class="lh math" data-s="${xs}">${xh}</span></span></div>
    <div class="xrow"><span class="xlb">x軸との<br>共有点の 個数</span><span class="xbx"><span class="lh" data-s="${ns}">${nh}</span></span></div>
  </div>`;
const YT = s => `<span class="ytag lh" data-s="${s}">y ＝ 0 と する</span>`;

/* 2枚目：考え方（プリントの 上の 帯）。y軸を かいてから「今回は いらない」と 言って 消す */
const s0 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="xband"><span class="xkw">x軸の 共有点</span> に ついて 問われたら、<span class="xblank"><span class="lh math" data-s="4">y ＝ 0</span></span> と して 考える。</div>
    <div class="xg0">${GR({w:560,h:300,ay:150,cx:1,sc:62,k:22,r:[-1,3],top:30,sd:2,sc2:0,lo:30,yax:1,lab:[`(−1, ${tm('r','0',3)})`,`(3, ${tm('r','0',3)})`]})}</div>
    <div class="xyn lh" data-s="1" data-o="2">今回は <b><i class="math">y</i>軸</b> を 使わない<br>→ かかない</div>
    <div class="xbub lh" data-s="3">x軸の 上の 点は<br><i class="math">y</i>座標が いつも <b>0</b></div>
  </div>
  ${cbar([
    `<b>x軸との 共有点</b> とは、グラフが x軸と 交わったり 接したり する 点。`,
    `今回 見るのは <b>x軸との 共有点</b> だけ。　<i class="math">y</i>軸は 使わないので <b>かかない</b>。`,
    `この 放物線と x軸との 共有点は (−1, 0) と (3, 0)。`,
    `x軸の 上の 点は、<i class="math">y</i>座標が いつも <b>0</b>。`,
    `だから x軸との 共有点を 求める ときは「<b>y ＝ 0</b> と して 考える」！`])}`;

/* 3・4枚目：例⑴⑵（部品は XCOMMON） */
const s1 = ptSlide({clip:[56,165,510,335],
  svg:[BG([154.8,179.1,197.1,204.6],'xpb'), BG([73.2,207.1,197.1,232.6],'xpb'), BG([128.3,235.3,227.2,260.9],'xpb'),
    BG([435.7,169,505.7,197.8],'xpr'), BG([435.7,202.8,505.7,231.6],'xpr'), BG([404.9,237.3,505.6,328.6],'xpr'),
       BRC(181.9,259.4,5), AX(294.8),
       PB({xv:455, yv:316.8, q:0.0416, ay:294.8, top:243, s:8, dot:'f', ds:7, ls:9, lab:[[432,'−1'],[478,'3']]})],
  items:[
    T([61.6,182,154,199],`⑴<span class="xsp"></span>y ＝ x${P2} − 2x − 3`,10.5),
    T([157.2,207.1,165.1,232.6],'=',12,'ac xeqp'), T([157.2,235.3,165.1,260.9],'=',12,'ac xeqp'),
    ...LBL(179.1),
    {s:1, r:[201,180.5,294,203.5], h:`<span class="ytag">y ＝ 0 と する</span>`, fs:10.5, cls:'xyt'},
    XA(2,[154.8,179.1,197.1,204.6],'＝ 0',12,'xan xeq0'),
    XA(3,[73.2,207.1,157.2,232.6],'(x ＋ 1)(x − 3)',10.5,'xan xr'), XA(3,[165.1,207.1,197.1,232.6],'0',12,'xan xl'),
    XA(4,[128.3,235.3,157.2,260.9],'x',12,'xan xr'), XA(4,[165.1,235.3,227.2,260.9],'−1, 3',12,'xan xl'),
    XA(5,[435.7,169,505.7,197.8],'−1, 3',13), XA(6,[435.7,202.8,505.7,231.6],'2 個',13)],
  done:9,
  cm:[
    `⑴ ${M('y ＝ x² − 2x − 3')} と x軸との 共有点を 求めよう。`,
    `x軸との 共有点 なので <b>y ＝ 0</b> と する。`,
    `y が 0 → 式の 右に <b>＝ 0</b>。　2次方程式 ${M('x² − 2x − 3 ＝ 0')} に なる。`,
    `たして −2、かけて −3 → <b>因数分解</b>。`,
    `${M('x ＝ −1, 3')}。`,
    `この 解が、そのまま 共有点の <b>x座標</b>。`,
    `解が 2つ → 共有点も <b>2個</b>。`,
    `グラフの 概形。　x軸に 共有点を 2つ 打つ。`,
    `${M('x²')} の 係数が プラス → <b>下に凸</b>。　2つの 点を 通るように かく。`,
    `点の 下に x座標 <b>−1</b>、<b>3</b> を 書く。　<b>完成！</b>`]});

const r21 = Math.sqrt(21), rr2 = Math.sqrt((513-491.1)/0.0352);
const s3 = ptSlide({clip:[56,343,510,530],
  svg:[BG([154.8,375.4,197.1,400.9],'xpb'), BG([73.2,403.4,211.7,454.2],'xpb'), BG([107.8,456.6,211.7,507.4],'xpb'),
    BG([435.7,350.8,505.6,394.1],'xpr'), BG([435.7,399.1,505.7,427.9],'xpr'), BG([404.9,433.5,505.6,524.9],'xpr'),
       BRC(378.2,455.7,5), AX(491.1),
       PB({xv:455, yv:513, q:0.0352, ay:491.1, top:440, s:8, dot:'f', ds:7})],
  items:[
    T([61.6,379,154,396],`⑵<span class="xsp"></span>y ＝ x${P2} − x − 5`,10.5),
    T([109.8,403.4,118.5,454.2],'=',12,'ac xeqp'), T([109.8,456.6,118.5,507.4],'=',12,'ac xeqp'),
    ...LBL(375.3),
    {s:1, r:[201,376.8,294,399.5], h:`<span class="ytag">y ＝ 0 と する</span>`, fs:10.5, cls:'xyt'},
    XA(2,[154.8,375.4,197.1,400.9],'＝ 0',12,'xan xeq0'),
    XA(3,[73.2,403.4,109.8,454.2],'x',12,'xan xr'), XA(3,[118.5,403.4,211.7,454.2],KF(`1 ± ${SQ('1 ＋ 20')}`,'2'),11,'xan xl'),
    XA(4,[118.5,456.6,211.7,507.4],KF(`1 ± ${SQ('21')}`,'2'),11,'xan xl'),
    XA(5,[435.7,350.8,505.6,394.1],KF(`1 ± ${SQ('21')}`,'2'),11), XA(6,[435.7,399.1,505.7,427.9],'2 個',13),
    {s:9, r:[(455-rr2)-22,493,(455-rr2)+6,512], h:KF(`1 − ${SQ('21')}`,'2'), fs:6.5, cls:'xgl', al:'c'},
    {s:9, r:[(455+rr2)-6,493,(455+rr2)+22,512], h:KF(`1 ＋ ${SQ('21')}`,'2'), fs:6.5, cls:'xgl', al:'c'}],
  done:9,
  cm:[
    `⑵ ${M('y ＝ x² − x − 5')} と x軸との 共有点を 求めよう。`,
    `x軸との 共有点 なので <b>y ＝ 0</b> と する。`,
    `式の 右に <b>＝ 0</b>。　${M('x² − x − 5 ＝ 0')}。　たして −1、かけて −5 の 組は ない → 因数分解 できない…`,
    `<b>解の公式</b>！　a ＝ 1、b ＝ −1、c ＝ −5 を 入れる。`,
    `ルートの中を 計算して ${M('x ＝ (1 ± √21)/2')}。`,
    `これが 共有点の <b>x座標</b>。`,
    `± で 2つ → 共有点は <b>2個</b>。`,
    `グラフの 概形。　x軸に 共有点を 2つ 打つ（位置は <b>だいたい</b> で よい）。`,
    `${M('x²')} の 係数が プラス → <b>下に凸</b>。　2つの 点を 通るように かく。`,
    `点の 下に x座標を 書く。　<b>完成！</b>`]});

/* 7枚目：まとめ（アニメーションなし） */
const s5 = `
  <div class="end-h"><h2>x軸との 共有点 → y ＝ 0</h2></div>
  <div class="dsum">
    <div class="card dsc xsc c2"><div class="dsc-s">共有点の <i class="math">x</i>座標</div><div class="xeq">＝</div><div class="dsc-n">2次方程式の <b>解</b></div></div>
    <div class="card dsc xsc c1"><div class="dsc-s">共有点の 個数</div><div class="xeq">＝</div><div class="dsc-n">2次方程式の <b>解の 個数</b></div></div>
  </div>
  ${cbar([`<b>y ＝ 0</b> と して 2次方程式を 解けば、共有点の x座標も 個数も わかる。`])}`;

const DECK = {title:'②-1 x軸との共有点', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">x軸</span>との<br>共有点', 'y ＝ 0 と して 考える', '2次方程式を 解けば わかる！', POL, 'y ＝ 0')},
  {name:'考え方', html:s0}, {name:'⑴', html:s1}, {name:'⑵', html:s3}, {name:'まとめ', html:s5},
  {name:'終', html:endF(KK + '　x軸との共有点', POL)}
]};
""")

    # ------------------------------------------------------------ ②-2 x軸との共有点（重解・なし）
    decks['2-2_x軸との共有点'] = ('②-2 x軸との共有点', COMMON + XCOMMON + r"""
const KK = KIMATSU + '　②-2';
const POL = `<div class="fpol"><div class="fa" style="font-size:24px;font-weight:900">重解 → 接する</div><div class="fv">x軸との 共有点</div><div class="fb" style="font-size:22px;font-weight:900">解なし → 共有点なし</div></div>`;

/* 例⑴ 重解 → 接する */
const s1 = ptSlide({clip:[56,95,510,262],
  svg:[BG([154.8,107.1,197.1,132.6],'xpb'), BG([73.2,135.1,197.1,160.6],'xpb'), BG([128.3,163.3,227.2,188.9],'xpb'), BG([181.2,192.5,246.4,218],'xpk'),
       BG([435.7,97,505.7,125.8],'xpr'), BG([435.7,130.8,505.7,159.6],'xpr'), BG([404.9,165.3,505.6,256.6],'xpr'),
       BRC(109.9,187.4,6), AX(222.8),
       PB({xv:455, yv:222.8, q:0.045, ay:222.8, top:171, s:9, dot:'f', ds:8, ls:10, lab:[[455,'−1']]})],
  items:[
    T([61.6,110,154,127],`⑴<span class="xsp"></span>y ＝ x${P2} ＋ 2x ＋ 1`,10.2),
    T([157.2,135.1,165.1,160.6],'=',12,'ac xeqp'), T([157.2,163.3,165.1,188.9],'=',12,'ac xeqp'),
    ...LBL(107.0),
    {s:1, r:[201,108.5,294,131.5], h:`<span class="ytag">y ＝ 0 と する</span>`, fs:10.5, cls:'xyt'},
    XA(2,[154.8,107.1,197.1,132.6],'＝ 0',12,'xan xeq0'),
    XA(3,[73.2,135.1,157.2,160.6],`(x ＋ 1)${P2}`,12,'xan xr'), XA(3,[165.1,135.1,197.1,160.6],'0',12,'xan xl'),
    XA(4,[128.3,163.3,157.2,188.9],'x',12,'xan xr'), XA(4,[165.1,163.3,227.2,188.9],'−1',12,'xan xl'),
    XA(5,[181.2,192.5,246.4,218],'重解',12,'xja xred'),
    XA(6,[435.7,97,505.7,125.8],'−1',13), XA(7,[435.7,130.8,505.7,159.6],'1 個',13)],
  done:10,
  cm:[
    `⑴ ${M('y ＝ x² ＋ 2x ＋ 1')} と x軸との 共有点を 求めよう。`,
    `x軸との 共有点 なので <b>y ＝ 0</b> と する。`,
    `式の 右に <b>＝ 0</b>。　${M('x² ＋ 2x ＋ 1 ＝ 0')}。`,
    `たして ＋2、かけて ＋1 → 同じ ( ) が 2つ → <b>2乗に まとめる</b>。`,
    `${M('x ＝ −1')}。`,
    `解が 1つ だけ → <b>重解</b>。`,
    `共有点の <b>x座標</b> は −1。`,
    `解が 1つ → 共有点も <b>1個</b>。`,
    `グラフの 概形。　x軸に 共有点を 1つ 打つ。`,
    `下に凸。　x軸に <b>接する</b> ように かく（交わらずに、1点で ふれる）。`,
    `点の 下に x座標 <b>−1</b> を 書く。　<b>完成！</b>`]});

/* 例⑵ 解なし → 共有点なし */
const s2 = ptSlide({clip:[56,278,510,472],
  svg:[BG([154.8,305.7,197.1,331.2],'xpb'), BG([73.2,333.7,211.7,384.5],'xpb'), BG([107.8,386.9,211.7,437.7],'xpb'), BG([181.2,442.5,246.4,468],'xpb'),
       BG([435.7,281.1,505.6,324.5],'xpr'), BG([435.7,329.4,505.7,358.2],'xpr'), BG([404.9,363.9,505.6,455.2],'xpr'),
       BRC(308.6,386,6), AX(421.4),
       PB({xv:455, yv:407, q:0.045, ay:421.4, top:369, s:8})],
  items:[
    T([61.6,308.5,154,325.5],`⑵<span class="xsp"></span>y ＝ x${P2} ＋ 2x ＋ 3`,10.2),
    T([109.8,333.7,118.5,384.5],'=',12,'ac xeqp'), T([109.8,386.9,118.5,437.7],'=',12,'ac xeqp'),
    ...LBL(305.7),
    {s:1, r:[201,307,294,330], h:`<span class="ytag">y ＝ 0 と する</span>`, fs:10.5, cls:'xyt'},
    XA(2,[154.8,305.7,197.1,331.2],'＝ 0',12,'xan xeq0'),
    XA(3,[73.2,333.7,109.8,384.5],'x',12,'xan xr'), XA(3,[118.5,333.7,211.7,384.5],KF(`−2 ± ${SQ('4 − 12')}`,'2'),11,'xan xl'),
    XA(4,[118.5,386.9,211.7,437.7],KF(`−2 ± ${SQ('−8')}`,'2'),11,'xan xl'),
    XA(5,[181.2,442.5,246.4,468],'解なし',12,'xja xred'),
    XA(6,[435.7,281.1,505.6,324.5],'なし',13,'xja xan'), XA(7,[435.7,329.4,505.7,358.2],'0 個',13)],
  done:8,
  cm:[
    `⑵ ${M('y ＝ x² ＋ 2x ＋ 3')} と x軸との 共有点を 求めよう。`,
    `x軸との 共有点 なので <b>y ＝ 0</b> と する。`,
    `式の 右に <b>＝ 0</b>。　${M('x² ＋ 2x ＋ 3 ＝ 0')}。　因数分解 できない → <b>解の公式</b>。`,
    `a ＝ 1、b ＝ 2、c ＝ 3 を 入れる。`,
    `${M('4 − 12 ＝ −8')}。　ルートの中が <b>マイナス</b>！`,
    `2乗して マイナスに なる 数は ない → <b>解なし</b>。`,
    `解が ない → x軸との 共有点の <b>x座標</b> も <b>なし</b>。`,
    `共有点は <b>0個</b>。`,
    `グラフは x軸と ふれない。　下に凸で、x軸より <b>上に 浮いている</b>（位置は だいたい）。　<b>完成！</b>`]});

/* まとめ（アニメーションなし）：解の 個数 ↔ 共有点 ↔ グラフ */
const MGR = (dep) => { // dep：頂点が x軸から 下へ 何px（マイナスなら 上）
  const ay=80, q=0.022, vy=ay+dep, top=8, hw=Math.sqrt((vy-top)/q);
  let d=''; for(let i=0;i<=60;i++){ const x=150-hw+2*hw*i/60; d+=(i?'L':'M')+x.toFixed(1)+' '+(vy-q*(x-150)**2).toFixed(1)+' '; }
  const r = dep>0 ? Math.sqrt(dep/q) : (dep===0?0:null);
  const dots = r===null ? '' : (r===0 ? [150] : [150-r,150+r]).map(x=>`<circle cx="${x.toFixed(1)}" cy="${ay}" r="7"/>`).join('');
  return `<svg class="xmg" width="300" height="130" viewBox="0 0 300 130"><line x1="10" y1="${ay}" x2="282" y2="${ay}"/><polygon points="292,${ay} 280,${ay-6} 280,${ay+6}"/><path d="${d}"/>${dots}</svg>`; };
const card = (cls, g, sol, n, rel) => `<div class="card dsc xmc ${cls}">${g}<div class="xms">解 <b>${sol}</b></div><div class="dsc-n">共有点 <b>${n}</b> 個</div><div class="xmr">${rel}</div></div>`;
const s3 = `
  <div class="end-h"><h2>解の 個数 ＝ x軸との 共有点の 個数</h2></div>
  <div class="dsum">${card('c1',MGR(40),'2つ','2','交わる')}${card('c2',MGR(0),'1つ（重解）','1','接する')}${card('c3',MGR(-30),'なし','0','共有点なし')}</div>
  ${cbar([`<b>y ＝ 0</b> と して 解いた 解の 個数が、そのまま x軸との 共有点の 個数。　重解 → <b>接する</b>、解なし → <b>共有点なし</b>。`])}`;

const DECK = {title:'②-2 x軸との共有点', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">x軸</span>との<br>共有点 ②', '重解 や 解なし の とき', 'グラフは どう なる？', POL, '接する・交わらない')},
  {name:'⑴', html:s1}, {name:'⑵', html:s2}, {name:'まとめ', html:s3},
  {name:'終', html:endF(KK + '　x軸との共有点', POL)}
]};
""")

    # ------------------------------------------------------------ ②-3 x軸との位置関係
    decks['2-3_x軸との位置関係'] = ('②-3 x軸との位置関係', COMMON + XCOMMON + r"""
const KK = KIMATSU + '　②-3';
const POL = `<div class="fpol"><div class="fa" style="font-size:24px;font-weight:900">解 2個 → 交わる</div><div class="fv">解 1個 → 接する</div><div class="fb" style="font-size:22px;font-weight:900">解 0個 → 共有点なし</div></div>`;

/* 印刷されている 小さな グラフ（pt）：x軸 と 放物線、青い 点 */
const SG = (ay, xv, yv, q, top, dots) => {
  const hw = Math.sqrt((yv-top)/q); let d='';
  for(let i=0;i<=40;i++){ const x=xv-hw+2*hw*i/40; d+=(i?'L':'M')+x.toFixed(2)+' '+(yv-q*(x-xv)**2).toFixed(2)+' '; }
  return `<line x1="84" y1="${ay}" x2="158" y2="${ay}" stroke="#555" stroke-width=".6"/><polygon points="160,${ay} 157,${ay-1.2} 157,${ay+1.2}" fill="#555"/><text class="pgt" x="157" y="${ay+6}" font-style="italic" style="font-size:5px">x</text>`
       + `<path d="${d}" fill="none" stroke="#222" stroke-width=".9"/>` + dots.map(x=>`<circle cx="${x}" cy="${ay}" r="2.3" fill="#4f81bd"/>`).join(''); };
const WB = r => `<rect x="${r[0]}" y="${r[1]}" width="${(r[2]-r[0]).toFixed(1)}" height="${(r[3]-r[1]).toFixed(1)}" fill="#fff"/>`;
const ROW = [[123.2,151.5,114.5,159.9],[200.7,229,192,237.3],[281.8,310.1,273.1,318.4]];

const s1 = ptSlide({clip:[60,82,533,327],
  svg:[`<rect class="xpb" x="61.3" y="82.7" width="470.3" height="243.7"/>`,
       ...ROW.flatMap(([a,b,c,e])=>[WB([210.8,a,256.8,b]), WB([319.7,a,395.4,b]), WB([412.2,c,487.8,e])]),
       SG(142.7, 118.9, 157, 0.071, 118, [104.7,133]),
       SG(230.6, 118.8, 230.6, 0.084, 190, [118.8]),
       SG(319, 118.8, 309, 0.085, 268, [])],
  items:[
    T([66.6,91,200,106],`<span class="ja">◎<i class="math">x</i>軸と交わるとき</span>`,12),
    ...ROW.flatMap(([a,b])=>[T([186.4,a,210.6,b],'<span class="ja">解は</span>'), T([244.7,a,258.4,b],'<span class="ja">個</span>'), T([294.5,a,317.6,b],'(例)')]),
    {m:1, e:4, r:[84,116,160,160]}, {m:4, e:7, r:[84,188,160,236]}, {m:7, e:99, r:[84,265,160,322]},
    XA(1,[210.8,123.2,244.7,151.5],'2',14), XA(2,[319.7,123.2,395.4,151.5],'x ＝ −1, 2',11), XA(3,[412.2,114.5,487.8,159.9],`x ＝ ${KF(`1 ± ${SQ('5')}`,'2')}`,11),
    XA(4,[210.8,200.7,244.7,229],'1',14), XA(5,[319.7,200.7,395.4,229],'x ＝ −1',11), XA(6,[412.2,192,487.8,237.3],`x ＝ ${KF(`−2 ± ${SQ('0')}`,'2')}`,11),
    XA(7,[210.8,281.8,244.7,310],'0',14), XA(8,[319.7,281.8,395.4,310.1],'解なし',11,'xja xan'), XA(9,[412.2,273.1,487.8,318.4],`x ＝ ${KF(`−2 ± ${SQ('−8')}`,'2')}`,11)],
  done:9,
  cm:[
    `グラフと x軸の <b>位置関係</b> は 3つ。　y ＝ 0 に した 2次方程式の <b>解の 個数</b> と つながって いる。`,
    `x軸と <b>2点で 交わる</b> → 共有点 2個 → 解は <b>2個</b>。`,
    `因数分解 できる 例：${M('(x ＋ 1)(x − 2) ＝ 0')} → ${M('x ＝ −1, 2')}。　ちがう 解が 2つ。`,
    `解の公式の 例：ルートの中が <b>プラス</b> → ± で ちがう 解が 2つ。`,
    `x軸と <b>接する</b> → 共有点 1個 → 解は <b>1個</b>。`,
    `因数分解 できる 例：${M('(x ＋ 1)² ＝ 0')} → ${M('x ＝ −1')}（<b>重解</b>）。`,
    `解の公式の 例：ルートの中が <b>0</b> → ＋0 も −0 も 同じ → 解は 1つ。`,
    `x軸と <b>共有点なし</b> → 共有点 0個 → 解は <b>0個</b>。`,
    `2乗して マイナスに なる 数は ない → <b>解なし</b>。`,
    `解の公式の 例：ルートの中が <b>マイナス</b> → 解なし。　<b>完成！</b>`]});

const DECK = {title:'②-3 x軸との位置関係', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">x軸</span>との<br>位置関係', '交わる・接する・共有点なし', '解の 個数で わかる！', POL, '解の 個数 と グラフ')},
  {name:'位置関係', html:s1},
  {name:'終', html:endF(KK + '　x軸との位置関係', POL)}
]};
""")

    # ------------------------------------------------------------ ③-1 2次不等式の解法
    decks['3-1_2次不等式の解法'] = ('③-1 2次不等式の解法', COMMON + XCOMMON + r'''
const WB = r => `<rect x="${r[0]}" y="${r[1]}" width="${(r[2]-r[0]).toFixed(1)}" height="${(r[3]-r[1]).toFixed(1)}" fill="#fff"/>`;
const KK = KIMATSU + '　③-1';
const POL = `<div class="fpol"><div class="fa math">x${P2} − 2x − 3 ＞ 0</div><div class="fv">グラフを 塗る</div><div class="fb math">x ＜ −1, 3 ＜ x</div></div>`;

/* ===== 大きい グラフ（px）。y ＝ k(x − r1)(x − r2) を 下に凸で かく。x軸 ＝ 水面 ===== */
function IG(o){
  const W = 660, H = 410, ay = o.ay;
  const X = x => W/2 + (x-o.cx)*o.sc, Y = x => ay - o.k*(x-o.r[0])*(x-o.r[1]);
  const m = (o.r[0]+o.r[1])/2, c0 = (m-o.r[0])*(m-o.r[1]);
  const hw = Math.sqrt((ay-o.top)/o.k - c0), xa = m-hw, xb = m+hw;
  const path = (a,b) => { let d=''; for(let i=0;i<=60;i++){ const x=a+(b-a)*i/60; d+=(i?'L':'M')+X(x).toFixed(1)+' '+Y(x).toFixed(1)+' '; } return d; };
  const f = n => n.toFixed(1);
  const g = {X, Y, ay, W, H, xa, xb, r:o.r, path};
  let wave=''; for(let x=14;x<=W-28;x+=4) wave+=(x===14?'M':'L')+x+' '+(ay+3*Math.sin(x/9)).toFixed(1)+' ';
  g.base = (o.water ? `<g class="${o.ws!==undefined?'gs':''}"${o.ws!==undefined?` data-s="${o.ws}"`:''}><rect class="iwater" x="14" y="${ay}" width="${W-28}" height="${H-ay-6}"/><path class="iwave" d="${wave}"/>
      <text class="iwl" x="22" y="34">水の 上（<tspan font-style="italic">y</tspan> ＞ 0）</text><text class="iwl in" x="22" y="${H-16}">水の 中（<tspan font-style="italic">y</tspan> ＜ 0）</text></g>` : '')
    + `<rect class="itint" data-s="${o.tint??99}" x="14" y="10" width="${W-28}" height="${ay-10}"/>
    <line class="iax" x1="10" y1="${ay}" x2="${W-16}" y2="${ay}"/><polygon class="iah" points="${W-2},${ay} ${W-20},${ay-9} ${W-20},${ay+9}"/>
    <text class="ixl" x="${W-24}" y="${ay+38}">x</text>
    ${o.r.map(x=>`<text class="inum" x="${f(X(x))}" y="${ay+44}" text-anchor="middle">${x<0?'−'+(-x):x}</text>`).join('')}
    <path class="icv${o.cs!==undefined?' gs':''}"${o.cs!==undefined?` data-s="${o.cs}"`:''} d="${path(xa,xb)}"/>`;
  /* 塗る：a から b まで（コースターと 同じ 速さで のびる） */
  g.seg = (a,b,s) => `<g class="ipaint" data-s="${s}"><path pathLength="1" d="${path(a,b)}"/></g>`;
  /* 水面の 点：open＝白丸、さもなくば 黒丸 */
  g.dot = (x,s,open) => `<g class="gs" data-s="${s}"><circle class="iend ${open?'op':''}" cx="${f(X(x))}" cy="${ay}" r="12"/></g>`;
  /* OK・ダメ の 札（グラフの 上に） */
  g.tag = (x,s,ok,txt,dx=0) => `<g class="gs" data-s="${s}"><text class="itag ${ok?'ok':'ng'}" x="${f(X(x)+dx)}" y="${f(Y(x)+(Y(x)<ay?-26:44))}" text-anchor="middle">${txt}</text></g>`;
  /* 塗れた 部分に 置く x の 札 */
  g.xmark = (x,s) => `<g class="gs" data-s="${s}"><circle class="ixb" cx="${f(X(x)+(x<m?-34:34))}" cy="${f(Y(x))}" r="24"/><text class="ixt" x="${f(X(x)+(x<m?-34:34))}" y="${f(Y(x)+10)}" text-anchor="middle">x</text></g>`;
  /* 高さ y の 矢印（x軸 から グラフの 点まで） */
  g.hgt = (x,s,lab,e=99,left=false) => { const up = Y(x)<ay; return `<g class="gs ihg" data-s="${s}" data-o="${e}"><line class="ihl ${up?'up':'dn'}" x1="${f(X(x))}" y1="${ay}" x2="${f(X(x))}" y2="${f(Y(x)+(up?10:-10))}"/><polygon class="ihh ${up?'up':'dn'}" points="${f(X(x)-8)},${f(Y(x)+(up?14:-14))} ${f(X(x)+8)},${f(Y(x)+(up?14:-14))} ${f(X(x))},${f(Y(x))}"/><circle class="ipc" cx="${f(X(x))}" cy="${f(Y(x))}" r="8"/><text class="ihtx ${up?'up':'dn'}" text-anchor="${left?'end':'start'}" x="${f(X(x)+(left?-14:14))}" y="${f(up?(ay+Y(x))/2+8:Y(x)+34)}">${lab}</text></g>`; };
  /* スタート地点で 待つ 乗り物（s 番で 出て、e 番で 消える） */
  g.wait = (kind,s,e) => `<div class="iwait lh" data-s="${s}" data-o="${e}" style="left:${f(X(xa)-32)}px;top:${f(Y(xa)-30)}px">${RIDER(kind,false)}</div>`;
  g.svg = (...parts) => `<svg class="isv" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${parts.join('')}</svg>`;
  /* コースター（レール＝放物線 に そって 走る）。wa 番で 走り、wb 番で 消える */
  /* 乗り物（鳥号・魚号）が レール（放物線）に そって 進む。wa 番で 走り、wb 番で 消える。ng＝息が できない（くるしい 顔） */
  g.ride = (a,b,wa,wb,kind,ng) => `<div class="iride${ng?' ng':''}" data-wa="${wa}" data-wb="${wb}" style="offset-path:path('${path(a,b)}')">${RIDER(kind,ng)}${ng?'<span class="ibub">くるしい…</span>':''}</div>`;
  return g;
}

/* 鳥号・魚号の 絵（ng＝くるしい 顔） */
const RIDER = (kind, ng) => {
  const eye = ng ? `<path d="M33 13 l5 4 M38 13 l-5 4" stroke="#333" stroke-width="2" stroke-linecap="round"/>` : `<circle cx="36" cy="15" r="3" fill="#333"/><circle cx="37" cy="14" r="1" fill="#fff"/>`;
  const mouth = ng ? `<path d="M40 24 q3 -3 6 0" fill="none" stroke="#333" stroke-width="1.8" stroke-linecap="round"/>` : '';
  if(kind==='fish') return `<svg width="64" height="40" viewBox="0 0 64 40"><path d="M6 20 L0 8 L0 32 Z" fill="#f08a2a"/><ellipse cx="30" cy="20" rx="24" ry="14" fill="#5aa9e6"/><path d="M22 8 q6 -8 14 0" fill="#3f86c4"/><path d="M20 20 q6 4 12 0" fill="none" stroke="#3f86c4" stroke-width="2"/>${eye}${mouth||'<path d="M48 22 q2 2 4 0" fill="none" stroke="#333" stroke-width="1.8"/>'}</svg>`;
  return `<svg width="64" height="40" viewBox="0 0 64 40"><ellipse cx="30" cy="22" rx="20" ry="15" fill="#ffd34d"/><path d="M12 22 q8 -14 20 -2 q-8 10 -20 2 Z" fill="#f5b400"/><path d="M48 18 l12 4 l-12 4 Z" fill="#f08a2a"/>${eye}${mouth}</svg>`; };
/* 説明の 中の 小さな アイコン */
const ICON = kind => `<span class="iicon">${RIDER(kind,false)}</span>`;
const IP = (s,h,cls='') => `<div class="ipr lh ${cls}" data-s="${s}">${h}</div>`;
const EQ1 = `x${P2} − 2x − 3 ＞ 0`, EQ2 = `x${P2} ＋ 3x ＋ 2 ≦ 0`;
/* ②-1 と 同じ くらい しゅっと した 放物線 */
const G1 = {ay:220, cx:1, sc:80, k:42, r:[-1,3], top:22};
const G2 = {ay:220, cx:-1.5, sc:160, k:330, r:[-2,-1], top:22};

/* ===== 2枚目：考え方 ===== */
const gk = IG({...G1, tint:3, cs:1});
const s0 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ig">${gk.svg(gk.base)}</div>
    <div class="ipn">
      <div class="ipr ibig math">${EQ1}</div>
      <div class="ipr ja0">って どういう こと？</div>
      ${IP(1,`x${P2} − 2x − 3 を <b class="math">y</b> と おく<br><span class="math">y ＝ x${P2} − 2x − 3</span>`)}
      ${IP(2,`「＞ 0」は <b class="math">y ＞ 0</b>`)}
      ${IP(3,`y ＞ 0 ＝ グラフが <b>x軸より 上</b>`)}
      ${IP(4,`グラフが x軸より 上に なる <b>x</b> を 探す 問題！`,'ikey')}
    </div>
  </div>
  ${cbar([
    `初めての <b>2次不等式</b>。　${M('x² − 2x − 3 ＞ 0')} って、どういう 意味だろう？`,
    `左の 式 ${M('x² − 2x − 3')} を <b>y</b> と おく。　すると、おなじみの 2次関数の グラフが かける。`,
    `「${M('x² − 2x − 3')} が 0 より 大きい」は「<b>y が 0 より 大きい</b>」と 同じ。`,
    `y ＞ 0 は、グラフの 点が <b>x軸より 上</b> に ある ところ。`,
    `つまり 2次不等式は、グラフが x軸より 上（または 下）に なる <b>x の 範囲</b> を 探す 問題！`])}`;

/* ===== 3枚目：2次不等式の 解き方（プリントの 枠どおり） ===== */
const s1 = ptSlide({clip:[60,84,535,252],
  svg:[`<rect class="xpb" x="62.1" y="85" width="470.9" height="165.9"/>`,
       WB([182.9,109.7,302.7,138]), WB([163.5,146.1,266.2,174.5]), WB([244.9,182.1,282.6,210.4]), WB([370.7,182.1,408.4,210.4]), WB([192,218.1,229.8,246.4])],
  items:[
    T([71.9,94.5,250,109],'<span class="ja" style="font-weight:900">2次不等式の解き方</span>',12),
    T([80.6,116.5,128,130],'<span class="ja"><i class="nv">Step</i>❶</span>'), T([80.6,188.8,128,202.3],'<span class="ja"><i class="nv">Step</i>❷</span>'), T([80.6,224.8,128,238.3],'<span class="ja"><i class="nv">Step</i>❸</span>'),
    T([129.3,116.5,182.9,130],'<span class="ja">2次関数の</span>',9.2), T([304.5,116.5,420,130],'<span class="ja">の問題として解く。</span>',9.2),
    T([129.3,152.5,163.5,166],'<span class="ja">つまり、</span>',8.7), T([268,152.5,380,166],'<span class="ja">を解き、グラフを書く。</span>',9.2),
    T([129.3,188.8,244.9,202.3],`<span class="ja">グラフを塗る。<i class="math">y</i> ＞ 0の時、</span>`,8.7), T([284.4,188.8,370.7,202.3],`<span class="ja">を塗る。<i class="math">y</i> ＜ 0の時、</span>`,8.7), T([410.2,188.8,460,202.3],'<span class="ja">を塗る。</span>',9.2),
    T([129.3,224.8,192,238.3],'<span class="ja">塗れた場所を</span>',9.2), T([231.6,224.8,320,238.3],'<span class="ja">方向で答える。</span>',9.2),
    XA(1,[182.9,109.7,302.7,138],'x軸との共有点',11,'xja xan'), XA(2,[163.5,146.1,266.2,174.5],'y ＝ 0（2次方程式）',9.5,'xja xan'),
    XA(3,[244.9,182.1,282.6,210.4],'上',13,'xja xan'), XA(4,[370.7,182.1,408.4,210.4],'下',13,'xja xan'), XA(5,[192,218.1,229.8,246.4],'x軸',12,'xja xan')],
  cm:[
    `2次不等式の 解き方は 3つの <i class="nv">Step</i>。　空らんを うめよう。`,
    `<i class="nv">Step</i>❶：グラフと x軸の 関係を 見る → 2次関数の <b>x軸との 共有点</b> の 問題。`,
    `x軸との 共有点 → <b>y ＝ 0</b>（2次方程式）を 解いて、グラフを かく。　②-1 と 同じ！`,
    `<i class="nv">Step</i>❷：y ＞ 0 は x軸より <b>上</b> → 上を 塗る。`,
    `y ＜ 0 は x軸より <b>下</b> → 下を 塗る。`,
    `<i class="nv">Step</i>❸：塗れた 場所を <b>x軸</b> 方向で 答える（x の 範囲で 答える）。`]});

/* ===== 例の プリントの 配置（⑴ dy＝0、⑵ dy＝252）。phase 1：<i class="nv">Step</i>❶ ／ 2：<i class="nv">Step</i>❷・❸ ===== */
function PR(o){
  const dy = o.dy, Yd = y => y+dy, R = r => [r[0],r[1]+dy,r[2],r[3]+dy];
  const ph1 = o.phase===1, sx = n => ph1 ? n : undefined;
  const pv = o.pv;      // 印刷された グラフ：xv, yv, q
  const top = Yd(440), ay = Yd(492);
  const hw = Math.sqrt((pv.yv+dy-top)/pv.q); let d='';
  for(let i=0;i<=50;i++){ const x=pv.xv-hw+2*hw*i/50; d+=(i?'L':'M')+x.toFixed(2)+' '+((pv.yv+dy)-pv.q*(x-pv.xv)**2).toFixed(2)+' '; }
  const L = (s,r,h,fs=11) => s===undefined ? T(R(r),h,fs,'xan') : XA(s,R(r),h,fs,'xan xl');
  const items = [
    T(R([62.3,281.5,200,297.5]),`${o.no}<span class="xsp"></span>${o.eq}`,11),
    T(R([73.5,304.5,119,323]),'<span class="ja"><i class="nv">Step</i>❶</span>',10.5,'ac'), T(R([73.5,428.9,119,447.4]),'<span class="ja"><i class="nv">Step</i>❷</span>',10.5,'ac'), T(R([286.7,428.9,332.3,447.4]),'<span class="ja"><i class="nv">Step</i>❸</span>',10.5,'ac'),
    T(R([160,485.5,180,497.5]),`<span style="font-size:.8em">${o.lab[0]}</span>`,8.5), T(R([221,485.5,240,497.5]),`<span style="font-size:.8em">${o.lab[1]}</span>`,8.5),
    L(sx(1),[148,309,326,331],o.c[0]), {s:sx(2), r:R([262,310,326,330]), h:`<span class="ytag">y ＝ 0 と する</span>`, fs:7.8, cls:'xyt'},
    L(sx(2),[148,335,326,357],o.c[1]), L(sx(3),[148,361,326,383],o.c[2]), L(sx(4),[148,387,326,409],o.c[3]),
    ...(ph1 ? [] : [XA(3,R([323.2,467.2,507.3,498.3]),o.ans,13)])];
  const svg = [
    `<rect class="xpb" x="73.5" y="${Yd(304.5)}" width="45.5" height="18.5"/><rect class="xpb" x="73.5" y="${Yd(428.9)}" width="45.5" height="18.5"/><rect class="xpb" x="286.7" y="${Yd(428.9)}" width="45.6" height="18.5"/>`,
    `<rect class="xpb" x="142.8" y="${Yd(305.4)}" width="184" height="109.8"/><rect class="xpb" x="354.2" y="${Yd(305.4)}" width="137.2" height="109.8"/><rect class="xpr" x="323.2" y="${Yd(467.2)}" width="184.1" height="31.1"/>`,
    `<line x1="373.5" y1="${Yd(384.5)}" x2="467" y2="${Yd(384.5)}" stroke="#555" stroke-width=".7"/><polygon points="469,${Yd(384.5)} 465.5,${Yd(383)} 465.5,${Yd(386)}" fill="#555"/><text class="pgt" x="465" y="${Yd(392)}" font-style="italic">x</text>`,
    `<line x1="140" y1="${ay}" x2="268" y2="${ay}" stroke="#333" stroke-width=".8"/><polygon points="271,${ay} 266.5,${ay-1.8} 266.5,${ay+1.8}" fill="#333"/><text class="pgt" x="265" y="${ay+11}" font-style="italic" style="font-size:9px">x</text>`,
    `<path d="${d}" fill="none" stroke="#111" stroke-width="1.6"/>`,
    ph1 ? PB({xv:o.gx, yv:Yd(404.5), q:0.05, ay:Yd(384.5), top:Yd(312), s:6, dot:'f', ds:5, ls:7, lab:[[o.gx-20,o.lab[0]],[o.gx+20,o.lab[1]]]})
        : PB({xv:pv.xv, yv:pv.yv+dy, q:pv.q, ay, top, draw:false, paint:o.paint, ps:1, dot:o.dot, ds:2})];
  if(!ph1) svg.push(PB({xv:o.gx, yv:Yd(404.5), q:0.05, ay:Yd(384.5), top:Yd(312), dot:'f', lab:[[o.gx-20,o.lab[0]],[o.gx+20,o.lab[1]]]}).replace(/class="curve pgc" data-s="undefined"/,'class="curve pgc show"').replace(/class="gs" data-s="undefined"/g,'class="gs show"'));
  return ptSlide({clip:[60,278+dy,535,526+dy], svg, items, done: ph1 ? 7 : 3, cm:o.cm});
}
const P1 = {dy:0, no:'⑴', eq:EQ1, gx:420, lab:['−1','3'], pv:{xv:201.9, yv:520, q:0.0581},
  c:[`y ＝ x${P2} − 2x − 3`, `x${P2} − 2x − 3 ＝ 0`, '(x ＋ 1)(x − 3) ＝ 0', 'x ＝ −1, 3'], ans:'x ＜ −1, 3 ＜ x', paint:'up', dot:'o'};
const P2_ = {dy:252, no:'⑵', eq:EQ2, gx:420, lab:['−2','−1'], pv:{xv:201.9, yv:520, q:0.0581},
  c:[`y ＝ x${P2} ＋ 3x ＋ 2`, `x${P2} ＋ 3x ＋ 2 ＝ 0`, '(x ＋ 2)(x ＋ 1) ＝ 0', 'x ＝ −2, −1'], ans:'−2 ≦ x ≦ −1', paint:'down', dot:'f'};
const STEP1CM = (P,fac,why) => [
  `${P.no} ${M(P.eq.replace(/<sup>2<\/sup>/,'²'))}。　<b><i class="nv">Step</i>❶</b>：2次関数の x軸との 共有点の 問題として 解く。`,
  `左の 式を y と おく。　${M(P.c[0].replace(/<sup>2<\/sup>/,'²'))}。`,
  `x軸との 共有点 → <b>y ＝ 0</b> と する。　${M(P.c[1].replace(/<sup>2<\/sup>/,'²'))}。`,
  `${why} → <b>因数分解</b>。　${M(fac)}。`,
  `${M(P.c[3])}。　これが グラフと x軸の 共有点。`,
  `右の グラフ。　x軸に 共有点を 2つ 打つ。`,
  `下に凸の 放物線を、2つの 点を 通るように かく。`,
  `点の 下に x座標を 書く。　<i class="nv">Step</i>❶ <b>完成！</b>`];

/* ===== 例⑴ ===== */
const s2 = PR({...P1, phase:1, cm:STEP1CM(P1,'(x ＋ 1)(x − 3) ＝ 0','たして −2、かけて −3')});
/* ⑴ Step❷：まず「y ＞ 0 は どこ？」を ていねいに → 上が すき → 鳥号 → 左から 塗る */
const a1 = IG({...G1, water:true, ws:2});
const s3 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ititle math">⑴　${EQ1}　<span class="istep"><i class="nv">Step</i>❷ 塗る</span></div>
    <div class="ig">${a1.svg(a1.base, a1.hgt(-1.7,2,'y ＞ 0',4), a1.hgt(2,2,'y ＜ 0',4),
        a1.seg(a1.xa,-1,4), a1.tag(-1.3,4,true,'息できる！',-95), a1.tag(1,6,false,'くるしい…'), a1.seg(3,3+(a1.xb-3),8), a1.dot(-1,5,true), a1.dot(3,7,true), a1.tag(3.3,8,true,'息できる！',95))}
      ${a1.wait('bird',3,4)}${a1.ride(a1.xa,-1,4,5,'bird')}${a1.ride(-1,3,6,7,'bird',true)}${a1.ride(3,3+(a1.xb-3)*0.8,8,99,'bird')}</div>
    <div class="ipn2">
      <div class="iq2 lh" data-s="1"><span class="inum2">1</span><div><span class="math">x${P2} − 2x − 3</span> は <b class="math">y</b> の こと<br>だから <span class="ibx math">y ＞ 0</span></div></div>
      <div class="iq2 lh" data-s="2"><span class="inum2">2</span><div><b class="math">y</b> は グラフの 点の <b>高さ</b><br>y ＞ 0 → x軸（水面）より <b>上</b></div></div>
      <div class="iq2 lh" data-s="3"><span class="inum2">3</span><div>上が すき → <b>鳥号</b> ${ICON('bird')}<br><span class="isub2">空なら 息が できる → 塗る</span></div></div>
    </div>
  </div>
  ${cbar([
    `<b><i class="nv">Step</i>❷ 塗る</b>。　まず「${M('x² − 2x − 3 ＞ 0')}」が グラフの <b>どこ</b> の ことか 考えよう。`,
    `Step❶ で ${M('y ＝ x² − 2x − 3')} と おいた。　だから 左の ${M('x² − 2x − 3')} は <b>y</b> の こと。　この 不等式は <b>y ＞ 0</b>。`,
    `y は グラフの 点の <b>高さ</b>。　x軸より 上の 点は y ＞ 0、下の 点は y ＜ 0。　x軸を <b>水面</b> と 思うと、y ＞ 0 は <b>水の 上</b>。`,
    `水の 上（空）が すきなのは <b>鳥号</b>。　鳥が 息を できる ところを、左から 順に 塗って いこう。`,
    `空を 進む → 息が できる → <b>塗る</b>。`,
    `−1 で ちょうど 水面（y ＝ 0）。　「0 ＞ 0」は まちがい → 塗れない → 中が 空っぽの <b>白丸</b>。`,
    `−1 から 3 の 間は <b>水の 中</b>。　鳥は 息が できない → 塗らない。`,
    `3 で また 水面 → <b>白丸</b>。`,
    `3 より 少しでも 右なら また 空 → 白丸の 先を <b>塗る</b>。`])}`;

/* ⑴ Step❸：塗れた 部分に x を 置いて、−1・3 と 比べる */
const b1 = IG({...G1});
const s4 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ititle math">⑴　${EQ1}　<span class="istep"><i class="nv">Step</i>❸ 答える</span></div>
    <div class="ig">${b1.svg(b1.base, b1.seg(b1.xa,-1,0), b1.seg(3,b1.xb,0), b1.dot(-1,0,true), b1.dot(3,0,true), b1.xmark(-1.7,1), b1.xmark(3.7,1),
      `<g class="gs" data-s="2"><text class="iblab" x="${b1.X(-1.7)-34}" y="${b1.Y(-1.7)+66}" text-anchor="middle">x ＜ −1</text></g>`,
      `<g class="gs" data-s="3"><text class="iblab" x="${b1.X(3.7)+34}" y="${b1.Y(3.7)+66}" text-anchor="middle">3 ＜ x</text></g>`)}</div>
    <div class="ipn">
      <div class="ipr">塗れた ところ の x は？</div>
      ${IP(1,`塗れた 2か所に <b class="math">x</b> を 置く`,'isub')}
      ${IP(2,`左の x は −1 より <b>小さい</b><br>→ <span class="math">x ＜ −1</span>`,'isub')}
      ${IP(3,`右の x は 3 より <b>大きい</b>（右）<br>→ <span class="math">3 ＜ x</span>`,'isub')}
      <div class="ians lh" data-s="4"><span class="math">x ＜ −1, 3 ＜ x</span></div>
      ${IP(5,`白丸 → <b class="math">＜</b>（＝ なし）　黒丸 → <b class="math">≦</b>`,'itip')}
    </div>
  </div>
  ${cbar([
    `<b><i class="nv">Step</i>❸ 答える</b>。　塗れた ところは どこ？　グラフの 塗れた 部分 だけ を 見る。`,
    `塗れた 部分の 点の 横の 位置が <b>x</b>。　左と 右の 2か所に x を 置く。`,
    `左の x は −1 より 左 ＝ −1 より <b>小さい</b>。　−1 は 白丸 なので ${M('x ＜ −1')}。`,
    `右の x は 3 より 右 ＝ 3 より <b>大きい</b>。　3 も 白丸 なので ${M('3 ＜ x')}。`,
    `2つを 「,」で 並べて ${M('x ＜ −1, 3 ＜ x')}。`,
    `白丸（塗れない 点）なら <b>＜</b>、黒丸（塗れる 点）なら <b>≦</b>。　<b>完成！</b>`])}`;

const s5 = PR({...P1, phase:2, cm:[
  `プリントに 書きこもう。　<i class="nv">Step</i>❷ の グラフ。`,
  `x軸より 上の 部分（外側の 2本）を 塗る。`,
  `端の −1、3 は 白丸（含まない）。`,
  `<i class="nv">Step</i>❸ に ${M('x ＜ −1, 3 ＜ x')}。　<b>完成！</b>`]});

/* ===== 例⑵ ===== */
const s6 = PR({...P2_, phase:1, cm:STEP1CM(P2_,'(x ＋ 2)(x ＋ 1) ＝ 0','たして ＋3、かけて ＋2')});
/* ⑵ Step❷：y ≦ 0 は どこ？ → 下が すき → 魚号 */
const a2 = IG({...G2, water:true, ws:2});
const s7 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ititle math">⑵　${EQ2}　<span class="istep"><i class="nv">Step</i>❷ 塗る</span></div>
    <div class="ig">${a2.svg(a2.base, a2.hgt(-2.35,2,'y ＞ 0',4,true), a2.hgt(-1.5,2,'y ＜ 0',4),
        a2.tag(-2.15,4,false,'くるしい…',-95), a2.seg(-2,-1,6), a2.dot(-2,5,false), a2.tag(-1.5,6,true,'息できる！'), a2.dot(-1,7,false), a2.tag(-0.85,8,false,'くるしい…',95))}
      ${a2.wait('fish',3,4)}${a2.ride(a2.xa,-2,4,5,'fish',true)}${a2.ride(-2,-1,6,7,'fish')}${a2.ride(-1,-1+(a2.xb+1)*0.7,8,99,'fish',true)}</div>
    <div class="ipn2">
      <div class="iq2 lh" data-s="1"><span class="inum2">1</span><div><span class="math">x${P2} ＋ 3x ＋ 2</span> は <b class="math">y</b> の こと<br>だから <span class="ibx math">y ≦ 0</span></div></div>
      <div class="iq2 lh" data-s="2"><span class="inum2">2</span><div><b class="math">y</b> は グラフの 点の <b>高さ</b><br>y ≦ 0 → x軸（水面）より <b>下</b>（と 水面）</div></div>
      <div class="iq2 lh" data-s="3"><span class="inum2">3</span><div>下が すき → <b>魚号</b> ${ICON('fish')}<br><span class="isub2">水の 中なら 息が できる → 塗る</span></div></div>
    </div>
  </div>
  ${cbar([
    `⑵ の <b><i class="nv">Step</i>❷ 塗る</b>。　「${M('x² ＋ 3x ＋ 2 ≦ 0')}」は グラフの どこ？`,
    `${M('y ＝ x² ＋ 3x ＋ 2')} と おいたので、左の 式は <b>y</b>。　この 不等式は <b>y ≦ 0</b>。`,
    `y は 点の <b>高さ</b>。　y ≦ 0 は 高さが 0 以下 → x軸（水面）より <b>下</b>（水の 中）と、ちょうど 水面。`,
    `水の 中が すきなのは <b>魚号</b>。　魚が 息を できる ところを、左から 順に 塗ろう。`,
    `はじめは 空 → 魚は 息が できない → 塗らない。`,
    `−2 で ちょうど 水面（y ＝ 0）。　「0 ≦ 0」は 正しい → 塗れる → 中まで 塗った <b>黒丸</b>。`,
    `−2 から −1 の 間は <b>水の 中</b> → 息が できる → <b>塗る</b>。`,
    `−1 で また 水面 → 塗れる → <b>黒丸</b>。`,
    `−1 より 右は 空 → くるしい。　塗れたのは 真ん中の 1か所 だけ。`])}`;

/* ⑵ Step❸ */
const b2 = IG({...G2});
const s8 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ititle math">⑵　${EQ2}　<span class="istep"><i class="nv">Step</i>❸ 答える</span></div>
    <div class="ig">${b2.svg(b2.base, b2.seg(-2,-1,0), b2.dot(-2,0,false), b2.dot(-1,0,false),
      `<g class="gs" data-s="1"><circle class="ixb" cx="${b2.X(-1.5)}" cy="${b2.Y(-1.5)+46}" r="24"/><text class="ixt" x="${b2.X(-1.5)}" y="${b2.Y(-1.5)+56}" text-anchor="middle">x</text></g>`,
      `<g class="gs" data-s="2"><text class="iblab" x="${b2.X(-2)-40}" y="${b2.Y(-1.5)+56}" text-anchor="middle">−2 ≦</text></g>`,
      `<g class="gs" data-s="3"><text class="iblab" x="${b2.X(-1)+40}" y="${b2.Y(-1.5)+56}" text-anchor="middle">≦ −1</text></g>`)}</div>
    <div class="ipn">
      <div class="ipr">塗れた ところ の x は？</div>
      ${IP(1,`塗れた 1か所に <b class="math">x</b> を 置く`,'isub')}
      ${IP(2,`x は −2 より <b>大きい</b>（右）<br>−2 は 黒丸 → <span class="math">−2 ≦ x</span>`,'isub')}
      ${IP(3,`x は −1 より <b>小さい</b>（左）<br>−1 も 黒丸 → <span class="math">x ≦ −1</span>`,'isub')}
      <div class="ians lh" data-s="4"><span class="math">−2 ≦ x ≦ −1</span></div>
      ${IP(5,`x が 2つに <b>はさまれる</b> 形`,'itip')}
    </div>
  </div>
  ${cbar([
    `⑵ の <b><i class="nv">Step</i>❸ 答える</b>。　塗れた ところは 真ん中の 1か所。`,
    `塗れた 部分に <b>x</b> を 置く。`,
    `x は −2 より 右 ＝ <b>大きい</b>。　−2 は 黒丸（塗れる）なので ${M('−2 ≦ x')}。`,
    `x は −1 より 左 ＝ <b>小さい</b>。　−1 も 黒丸 なので ${M('x ≦ −1')}。`,
    `まとめて ${M('−2 ≦ x ≦ −1')}。`,
    `x が −2 と −1 に <b>はさまれる</b> 形。　黒丸 なので ≦。　<b>完成！</b>`])}`;

const s9 = PR({...P2_, phase:2, cm:[
  `プリントに 書きこもう。　<i class="nv">Step</i>❷ の グラフ。`,
  `x軸より 下の 部分（真ん中の 1本）を 塗る。`,
  `端の −2、−1 は 黒丸（含む）。`,
  `<i class="nv">Step</i>❸ に ${M('−2 ≦ x ≦ −1')}。　<b>完成！</b>`]});

/* ===== まとめ（アニメーションなし） ===== */
const MG2 = (out) => {
  const W=320, H=150, ay=out?95:60, r1=out?120:130, r2=out?200:190, m=(r1+r2)/2, k=out?0.022:0.05;
  const Y = x => ay - k*(x-r1)*(x-r2), top=8, c0=(m-r1)*(m-r2), hw=Math.sqrt((ay-top)/k - c0);
  const P = (a,b) => { let d=''; for(let i=0;i<=40;i++){ const x=a+(b-a)*i/40; d+=(i?'L':'M')+x.toFixed(1)+' '+Y(x).toFixed(1)+' '; } return d; };
  const seg = out ? P(m-hw,r1)+P(r2,m+hw) : P(r1,r2);
  return `<svg class="imsv" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><line x1="16" y1="${ay}" x2="${W-18}" y2="${ay}"/><polygon points="${W-6},${ay} ${W-20},${ay-7} ${W-20},${ay+7}"/>
    <path class="mc" d="${P(m-hw,m+hw)}"/><path class="mp" d="${seg}"/>${[r1,r2].map(x=>`<circle class="${out?'op':''}" cx="${x}" cy="${ay}" r="8"/>`).join('')}
    <text x="${r1}" y="${ay+30}" text-anchor="middle">${out?'−1':'−2'}</text><text x="${r2}" y="${ay+30}" text-anchor="middle">${out?'3':'−1'}</text></svg>`; };
const s10 = `
  <div class="end-h"><h2>2次不等式の 答え方</h2></div>
  <div class="dsum">
    <div class="card dsc isc c1">${MG2(true)}<div class="dsc-s math">${EQ1}</div><div class="isr">＞ → <b>鳥号</b> ${ICON('bird')} 上を 塗る → <b>外側</b> 2本</div><div class="dsc-n math">x ＜ −1, 3 ＜ x</div></div>
    <div class="card dsc isc c2">${MG2(false)}<div class="dsc-s math">${EQ2}</div><div class="isr">≦ → <b>魚号</b> ${ICON('fish')} 下を 塗る → <b>内側</b> 1本</div><div class="dsc-n math">−2 ≦ x ≦ −1</div></div>
  </div>
  ${cbar([`＝ が ない（＞、＜）→ <b>白丸</b>・答えも <b>＜</b>。　＝ が ある（≧、≦）→ <b>黒丸</b>・答えも <b>≦</b>。　並びは 数直線と 同じ 左 → 右。`])}`;

const DECK = {title:'③-1 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">2次不等式</span><br>の 解き方', 'グラフを かいて 塗る', '塗れた 場所を x の 範囲で 答える', POL, '3つの Step')},
  {name:'考え方', html:s0}, {name:'解き方', html:s1},
  {name:'⑴ Step❶', html:s2}, {name:'⑴ 塗る', html:s3}, {name:'⑴ 答える', html:s4}, {name:'⑴ 書きこみ', html:s5},
  {name:'⑵ Step❶', html:s6}, {name:'⑵ 塗る', html:s7}, {name:'⑵ 答える', html:s8}, {name:'⑵ 書きこみ', html:s9},
  {name:'まとめ', html:s10},
  {name:'終', html:endF(KK + '　2次不等式の解法', POL)}
]};
''')

    # ------------------------------------------------------------ ③-2 練習編
    decks['3-2_2次不等式_練習編'] = ('③-2 2次不等式 練習編', COMMON + r'''
const KK = KIMATSU + '　③-2';
const POL = `<div class="fpol"><div class="fa math">＞ ＜ → 白丸</div><div class="fv">塗った 場所を 読む</div><div class="fb math">≧ ≦ → 黒丸</div></div>`;
const R = (i,y1,y2) => { const [x1,x2] = [[62.8,170.2],[182.9,290.4],[303,410.4],[423.1,530.5]][i]; return [x1,y1,x2,y2]; };
const row = (y1,y2,clip,ans,cms) => pgSlide({img:clip[0], clip:clip[1],
  items: ans.map((t,i)=>A(i+1,R(i,y1,y2),t,10)), done:4, cm:cms});
const s1 = row(167.8,202,['@@IMG:11:56,76,540,205@@',[56,76,540,205]],
  ['x ＜ −1, 3 ＜ x','−1 ＜ x ＜ 3','x ≦ −1, 3 ≦ x','−1 ≦ x ≦ 3'], [
  `${M('y ＝ x² − 2x − 3')} は x軸と −1、3 で 交わる。　塗った 場所を x軸 方向で 読もう。`,
  `⑴ 上を 塗る。　白丸 なので ＝ は つかない。　<b>${M('x ＜ −1, 3 ＜ x')}</b>`,
  `⑵ 下を 塗る。　<b>${M('−1 ＜ x ＜ 3')}</b>`,
  `⑶ 上を 塗る。　黒丸 なので ＝ が つく。　<b>${M('x ≦ −1, 3 ≦ x')}</b>`,
  `⑷ 下を 塗る。　<b>${M('−1 ≦ x ≦ 3')}</b>`]);
const s2 = row(311.8,346,['@@IMG:11:56,202,540,349@@',[56,202,540,349]],
  [JA('1以外のすべての実数'),JA('解なし'),JA('すべての実数'),'x ＝ 1'], [
  `${M('y ＝ x² − 2x ＋ 1 ＝ (x − 1)²')} は x軸と 1 で <b>接する</b>。`,
  `⑸ 上を 塗る。　1 だけ 白丸で ぬけている。　<b>1以外の すべての 実数</b>`,
  `⑹ x軸より 下の 部分が ない。　<b>解なし</b>`,
  `⑺ 上を 塗る。　1 も 黒丸で ふくむ。　<b>すべての 実数</b>`,
  `⑻ x軸より 下は ないが、＝ の 1 だけ ふくむ。　<b>${M('x ＝ 1')}</b>`]);
const s3 = row(455.8,490,['@@IMG:11:56,346,540,493@@',[56,346,540,493]],
  [JA('すべての実数'),JA('解なし'),JA('すべての実数'),JA('解なし')], [
  `${M('y ＝ x² − 2x ＋ 5')} は x軸と <b>交わらない</b>（いつも x軸より 上）。`,
  `⑼ グラフ 全部が 上 → <b>すべての 実数</b>`,
  `⑽ 下の 部分は ない → <b>解なし</b>`,
  `⑾ グラフ 全部が 上 → <b>すべての 実数</b>`,
  `⑿ 下の 部分も、x軸上の 点も ない → <b>解なし</b>`]);
const DECK = {title:'③-2 2次不等式 練習編', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">2次不等式</span><br>練習編', '塗った 場所を 読む', '12問 いっきに！', POL, '白丸・黒丸')},
  {name:'⑴〜⑷', html:s1}, {name:'⑸〜⑻', html:s2}, {name:'⑼〜⑿', html:s3},
  {name:'終', html:endF(KK + '　2次不等式 練習編', POL)}
]};
''')

    # ------------------------------------------------------------ ③-3 2次不等式の解法
    decks['3-3_2次不等式の解法'] = ('③-3 2次不等式の解法', COMMON + r'''
const KK = KIMATSU + '　③-3';
const POL = `<div class="fpol"><div class="fa math">接する・交わらない</div><div class="fv">とき は？</div><div class="fb math">すべての実数 / 解なし</div></div>`;
/* 1問：dy は ⑴ からの ずれ（162pt ずつ） */
const q = (img, dy, lines, g, ans, cms) => {
  const top = 125.4+dy, ay = top+76.9;
  const gr = PB(Object.assign({xv:300.4, q:0.03, ay, top:top+6, s:4, ls:4}, g(ay)));
  return pgSlide({img, clip:[56,98+dy,540,240+dy], svg:[gr],
    items:[...lines.map((t,i)=>A(i+1,[68,top+6+i*34,240,top+38+i*34],t,10.5,'l')), A(6,[359.6,204+dy,527.3,235.2+dy],ans,11)],
    done:6, cm:cms});
};
const s1 = q('@@IMG:13:56,98,540,240@@', 0, [`x${P2} ＋ 4x ＋ 2 ＝ 0`, `x ＝ ${FX(`−4 ± ${SQ('16 − 8')}`,'2')}`, `＝ −2 ± ${SQ('2')}`],
  ay=>({yv:ay+21, q:0.04, paint:'up', ps:5, dot:'f', ds:5, lab:[[276,'−2−√2'],[325,'−2+√2']]}),
  `x ≦ −2 − ${SQ('2')}, −2 ＋ ${SQ('2')} ≦ x`, [
  `⑴ ${M('x² ＋ 4x ＋ 2 ≧ 0')} を 解こう！`,
  `Step❶ ${M('x² ＋ 4x ＋ 2 ＝ 0')}。　因数分解 できないので 解の公式。`,
  `${M(`x ＝ ${FR('−4 ± √(16 − 8)',2)}`)}`,
  `${M(`＝ ${FR('−4 ± 2√2',2)} ＝ −2 ± √2`)}`,
  `グラフを かく。　x軸と 2点で 交わる。`,
  `Step❷ <b>≧ 0</b> → 上を 塗る。　＝ が あるので 黒丸。`,
  `Step❸ <b>${M('x ≦ −2 − √2, −2 ＋ √2 ≦ x')}</b>　<b>完成！</b>`]);
const s2 = q('@@IMG:13:56,260,540,402@@', 162, [`x${P2} ＋ 6x ＋ 9 ＝ 0`, `(x ＋ 3)${P2} ＝ 0`, 'x ＝ −3（重解）'],
  ay=>({yv:ay, q:0.032, dot:'o', ds:5, lab:[[300.4,'−3']]}), JA('解なし'), [
  `⑵ ${M('x² ＋ 6x ＋ 9 ＜ 0')} を 解こう！`,
  `Step❶ ${M('x² ＋ 6x ＋ 9 ＝ 0')}。`,
  `${M('(x ＋ 3)² ＝ 0')}`,
  `${M('x ＝ −3')}（重解）。`,
  `グラフは x軸と −3 で <b>接する</b>。`,
  `Step❷ <b>＜ 0</b> → 下を 塗りたい けど、x軸より 下の 部分が <b>ない</b>。`,
  `だから <b>解なし</b>。　<b>完成！</b>`]);
const s3 = q('@@IMG:13:56,422,540,564@@', 324, [`x${P2} − 2x ＋ 1 ＝ 0`, `(x − 1)${P2} ＝ 0`, 'x ＝ 1（重解）'],
  ay=>({yv:ay, q:0.032, paint:'all', ps:5, dot:'o', ds:5, lab:[[300.4,'1']]}), JA('1以外のすべての実数'), [
  `⑶ ${M('x² − 2x ＋ 1 ＞ 0')} を 解こう！`,
  `Step❶ ${M('x² − 2x ＋ 1 ＝ 0')}。`,
  `${M('(x − 1)² ＝ 0')}`,
  `${M('x ＝ 1')}（重解）。`,
  `グラフは x軸と 1 で <b>接する</b>。`,
  `Step❷ <b>＞ 0</b> → 上を 塗る。　x ＝ 1 の 点だけ y ＝ 0 なので <b>白丸</b>（ふくまない）。`,
  `Step❸ <b>1 以外の すべての 実数</b>。　<b>完成！</b>`]);
const s4 = q('@@IMG:13:56,584,540,726@@', 486, [`x${P2} ＋ 2x ＋ 5 ＝ 0`, 'D ＝ 4 − 20 ＝ −16 ＜ 0', JA('x軸との共有点 なし')],
  ay=>({yv:ay-14, q:0.026, paint:'all', ps:5}), JA('すべての実数'), [
  `⑷ ${M('x² ＋ 2x ＋ 5 ＞ 0')} を 解こう！`,
  `Step❶ ${M('x² ＋ 2x ＋ 5 ＝ 0')}。`,
  `判別式 ${M('D ＝ 2² − 4×1×5 ＝ −16')}。　<b>マイナス</b>！`,
  `x軸との 共有点は <b>なし</b>。`,
  `グラフは x軸と <b>交わらない</b>（いつも 上）。`,
  `Step❷ <b>＞ 0</b> → 上を 塗る。　グラフ <b>全部</b> が 塗れる。`,
  `Step❸ <b>すべての 実数</b>。　<b>完成！</b>`]);
const DECK = {title:'③-3 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">2次不等式</span><br>いろいろ', '接する・交わらない とき', 'グラフを かけば こわくない！', POL, 'すべての実数？')},
  {name:'⑴', html:s1}, {name:'⑵', html:s2}, {name:'⑶', html:s3}, {name:'⑷', html:s4},
  {name:'終', html:endF(KK + '　2次不等式', POL)}
]};
''')

    # ------------------------------------------------------------ ③-4 x² の係数が マイナス
    decks['3-4_2次不等式の解法'] = ('③-4 2次不等式の解法', COMMON + r'''
const KK = KIMATSU + '　③-4';
const POL = `<div class="fpol"><div class="fa math">−x${P2} − 6x − 7 ＞ 0</div><div class="fv">× (−1)　向きが 逆に！</div><div class="fb math">x${P2} ＋ 6x ＋ 7 ＜ 0</div></div>`;
const s0 = pgSlide({img:'@@IMG:16:56,80,540,186@@', clip:[56,80,540,186],
  items:[A(1,[218.2,131.4,255.9,159.7],'−1',13), A(2,[73.3,144.6,183.9,172.9],`x${P2} ＋ 6x ＋ 7 ＜ 0`,11)],
  cm:[
    `x² の 前が <b>マイナス</b> の 2次不等式。　このままだと グラフが 上に凸 で 考えにくい…`,
    `両辺に <b>−1</b> を かけて、x² の 前を プラスに する。`,
    `マイナスを かけると <b>不等号の 向きが 逆</b> に なる！　${M('x² ＋ 6x ＋ 7 ＜ 0')}`
  ]});
const ay = 266.6+76.9;
const g = PB({xv:299.6, yv:ay+22, q:0.04, ay, top:273, s:5, ls:5, dot:'o', ds:6, paint:'down', ps:6, lab:[[275,'−3−√2'],[324,'−3+√2']]});
const s1 = pgSlide({img:'@@IMG:16:56,206,540,380@@', clip:[56,206,540,380], svg:[g],
  items:[A(1,[62.7,231.5,199.9,263.4],`x${P2} ＋ 6x ＋ 7 ＜ 0`,11),
         A(2,[68,272,240,304],`x${P2} ＋ 6x ＋ 7 ＝ 0`,10.5,'l'), A(3,[68,306,240,338],`x ＝ ${FX(`−6 ± ${SQ('36 − 28')}`,'2')}`,10.5,'l'),
         A(4,[68,340,240,372],`＝ −3 ± ${SQ('2')}`,10.5,'l'), A(7,[358.9,345.3,526.6,376.4],`−3 − ${SQ('2')} ＜ x ＜ −3 ＋ ${SQ('2')}`,11)],
  done:7,
  cm:[
    `⑴ ${M('−x² − 6x − 7 ＞ 0')} を 解こう！`,
    `両辺に −1 を かけて、向きを 逆に。　${M('x² ＋ 6x ＋ 7 ＜ 0')}`,
    `Step❶ ${M('x² ＋ 6x ＋ 7 ＝ 0')}。　解の公式。`,
    `${M(`x ＝ ${FR('−6 ± √(36 − 28)',2)}`)}`,
    `${M(`＝ ${FR('−6 ± 2√2',2)} ＝ −3 ± √2`)}`,
    `グラフを かく。`,
    `Step❷ <b>＜ 0</b> → 下を 塗る。　＝ が ないので 白丸。`,
    `Step❸ <b>${M('−3 − √2 ＜ x ＜ −3 ＋ √2')}</b>　<b>完成！</b>`
  ]});
const DECK = {title:'③-4 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK, 'x² の 前が<br><span class="mk">マイナス</span>', '2次不等式の 解き方', '−1 を かけて 向きを 逆に！', POL, '向きが 逆')},
  {name:'考え方', html:s0}, {name:'⑴', html:s1},
  {name:'終', html:endF(KK + '　2次不等式', POL)}
]};
''')
