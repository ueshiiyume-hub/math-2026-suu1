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
    decks['2-1_x軸との共有点'] = ('②-1 x軸との共有点', COMMON + r"""
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

/* 3・4枚目：例⑴⑵（プリントの 配置どおり。座標は PDF の pt。生徒が 書きこむので 枠の 位置は 変えない）
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
    decks['2-2_x軸との共有点'] = ('②-2 x軸との共有点', COMMON + r'''
const KK = KIMATSU + '　②-2';
const POL = `<div class="fpol"><div class="fa math">重解 → 接する</div><div class="fv">x軸との 共有点</div><div class="fb math">解なし → 共有点なし</div></div>`;

const g1 = PB({xv:455, yv:222.8, q:0.045, ay:222.8, top:171, s:7, dot:'f', ds:7, lab:[[455,'−1']]});
const s1 = pgSlide({img:'@@IMG:8:56,78,540,262@@', clip:[56,78,540,262], svg:[g1],
  items:[A(1,[154.8,107.1,197.1,132.6],'y ＝ 0',10),
         A(2,[73.2,135.1,157,160.6],`(x ＋ 1)${P2}`,10.5), A(2,[168.2,135.1,197.1,160.6],'0',10.5),
         A(3,[128.3,163.3,157,188.9],'x',10.5), A(3,[168.2,163.3,227.2,188.9],'−1',10.5),
         A(4,[181.2,192.5,246.4,218],JA('重解'),10.5),
         A(5,[435.7,97,505.7,125.8],'−1',11), A(6,[435.7,130.8,505.7,159.6],'1個',11)],
  done:7,
  cm:[
    `⑴ ${M('y ＝ x² ＋ 2x ＋ 1')} と x軸との 共有点を 求めよう。`,
    `<b>y ＝ 0</b> と する。`,
    `因数分解。　${M('(x ＋ 1)² ＝ 0')}`,
    `${M('x ＝ −1')}`,
    `解が 1つ → <b>重解</b>。`,
    `共有点の x座標は <b>−1</b>。`,
    `共有点は <b>1個</b>。`,
    `グラフは x軸と −1 で <b>接する</b>。　<b>完成！</b>`
  ]});

const g2 = PB({xv:455, yv:409, q:0.045, ay:421.4, top:369, s:7});
const s2 = pgSlide({img:'@@IMG:8:56,300,540,472@@', clip:[56,300,540,472], svg:[g2],
  items:[A(1,[154.8,305.7,197.1,331.2],'y ＝ 0',10),
         A(2,[73.2,333.7,109.8,384.5],'x',10.5), A(2,[120.8,333.7,211.7,384.5],FX(`−2 ± ${SQ('4 − 12')}`,'2'),10),
         A(3,[122.5,386.9,211.7,437.7],FX(`−2 ± ${SQ('−8')}`,'2'),10.5),
         A(4,[181.2,442.5,246.4,468],JA('解なし'),10.5),
         A(5,[435.7,281.1,505.6,324.5],JA('なし'),11), A(6,[435.7,329.4,505.7,358.2],'0個',11)],
  done:7,
  cm:[
    `⑵ ${M('y ＝ x² ＋ 2x ＋ 3')} と x軸との 共有点を 求めよう。`,
    `<b>y ＝ 0</b> と する。　因数分解 できないので <b>解の公式</b>。`,
    `${M(`x ＝ ${FR('−2 ± √(4 − 12)',2)}`)}`,
    `${M(`＝ ${FR('−2 ± √−8',2)}`)}。　<b>ルートの中が マイナス</b>！`,
    `だから <b>解なし</b>。`,
    `共有点の x座標は <b>なし</b>。`,
    `共有点は <b>0個</b>。`,
    `グラフは x軸と <b>交わらない</b>（x軸より 上に ある）。　<b>完成！</b>`
  ]});

const DECK = {title:'②-2 x軸との共有点', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">x軸</span>との<br>共有点 ②', '重解 や 解なし の とき', 'グラフは どう なる？', POL, '接する・交わらない')},
  {name:'⑴', html:s1}, {name:'⑵', html:s2},
  {name:'終', html:endF(KK + '　x軸との共有点', POL)}
]};
''')

    # ------------------------------------------------------------ ②-3 x軸との位置関係
    decks['2-3_x軸との位置関係'] = ('②-3 x軸との位置関係', COMMON + r'''
const KK = KIMATSU + '　②-3';
const POL = `<div class="fpol"><div class="fa math">D ＞ 0 → 交わる</div><div class="fv">D ＝ 0 → 接する</div><div class="fb math">D ＜ 0 → 交わらない</div></div>`;
const s1 = pgSlide({img:'@@IMG:9:56,80,540,330@@', clip:[56,80,540,330],
  items:[A(1,[210.8,123.2,256.8,151.5],'2',13), A(2,[319.7,123.2,395.4,151.5],`y ＝ x${P2} ＋ 2x − 1`,9), A(3,[412.2,114.5,487.8,159.9],'D ＞ 0',12),
         A(4,[210.8,200.7,256.8,229],'1',13), A(5,[319.7,200.7,395.4,229],`y ＝ x${P2} ＋ 2x ＋ 1`,9), A(6,[412.2,192,487.8,237.3],'D ＝ 0',12),
         A(7,[210.8,281.8,256.8,310],'0',13), A(8,[319.7,281.8,395.4,310.1],`y ＝ x${P2} ＋ 2x ＋ 2`,9), A(9,[412.2,273.1,487.8,318.4],'D ＜ 0',12)],
  done:9,
  cm:[
    `グラフと x軸の <b>位置関係</b> を 整理しよう。　y ＝ 0 と した 2次方程式の <b>解の 個数</b> と 対応 しているよ。`,
    `x軸と <b>2点で 交わる</b> とき、解は <b>2個</b>。`,
    `例えば ${M('y ＝ x² ＋ 2x − 1')}。`,
    `判別式は ${M('D ＝ 4 ＋ 4 ＝ 8')}、<b>D ＞ 0</b>。`,
    `x軸と <b>接する</b> とき、解は <b>1個</b>（重解）。`,
    `例えば ${M('y ＝ x² ＋ 2x ＋ 1')}。`,
    `${M('D ＝ 4 − 4 ＝ 0')}、<b>D ＝ 0</b>。`,
    `x軸と <b>交わらない</b> とき、解は <b>0個</b>。`,
    `例えば ${M('y ＝ x² ＋ 2x ＋ 2')}。`,
    `${M('D ＝ 4 − 8 ＝ −4')}、<b>D ＜ 0</b>。　<b>完成！</b>`
  ]});
const DECK = {title:'②-3 x軸との位置関係', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">x軸</span>との<br>位置関係', '交わる・接する・交わらない', '判別式 D で わかる！', POL, 'D と グラフ')},
  {name:'まとめ', html:s1},
  {name:'終', html:endF(KK + '　x軸との位置関係', POL)}
]};
''')

    # ------------------------------------------------------------ ③-1 2次不等式の解法
    decks['3-1_2次不等式の解法'] = ('③-1 2次不等式の解法', COMMON + r'''
const KK = KIMATSU + '　③-1';
const POL = `<div class="fpol"><div class="fa math">x${P2} − 2x − 3 ＞ 0</div><div class="fv">グラフを 塗る</div><div class="fb math">x ＜ −1, 3 ＜ x</div></div>`;

const s0 = pgSlide({img:'@@IMG:10:56,80,540,255@@', clip:[56,80,540,255],
  items:[A(1,[182.9,109.7,302.7,138],JA('x軸との共有点'),11), A(2,[163.5,146.1,266.2,174.5],'y ＝ 0',12),
         A(3,[244.9,182.1,282.6,210.4],JA('上'),12), A(4,[370.7,182.1,408.4,210.4],JA('下'),12), A(5,[192,218.1,229.8,246.4],JA('x軸'),11)],
  cm:[
    `<b>2次不等式</b> の 解き方。　3つの Step で 解くよ。`,
    `Step❶ 2次関数の <b>x軸との 共有点</b> の 問題として 解く。`,
    `つまり <b>y ＝ 0</b> を 解き、グラフを かく。`,
    `Step❷ グラフを 塗る。　y ＞ 0 の とき（x軸より）<b>上</b> を 塗る。`,
    `y ＜ 0 の とき（x軸より）<b>下</b> を 塗る。`,
    `Step❸ 塗れた 場所を <b>x軸</b> 方向で 答える。`
  ]});

/* Step❶ の グラフ（自分で かく）と、Step❷ の 印刷された グラフに 塗る */
const mk = (dy, img, lines, gl, pr, ans, cms) => {
  const g = PB({xv:422.5, yv:407.3+dy, q:0.033, ay:382.3+dy, top:311+dy, s:4, dot:'f', lab:gl});
  const p = PB({xv:200.4, yv:521.6+dy, q:0.0668, ay:486.6+dy, top:441+dy, draw:false, paint:pr.paint, ps:5, dot:pr.dot, ds:5});
  /* ページ右下の QR コードが 少し 写るので 白で かくす */
  const qr = `<rect x="510" y="${508+dy}" width="36" height="22" fill="#fff"/>`;
  return pgSlide({img, clip:[56,278+dy,540,525+dy], svg:[g,p,qr],
    items:[...lines.map((t,i)=>A(i+1,[150,312+dy+i*33,322,342+dy+i*33],t,11,'l')), A(6,[323.2,467.2+dy,507.3,498.3+dy],ans,12)],
    done:6, cm:cms});
};
const s1 = mk(0, '@@IMG:10:56,278,540,525@@', [`x${P2} − 2x − 3 ＝ 0`, '(x ＋ 1)(x − 3) ＝ 0', 'x ＝ −1, 3'], [[395,'−1'],[450,'3']], {paint:'up', dot:'o'},
  'x ＜ −1, 3 ＜ x', [
    `⑴ ${M('x² − 2x − 3 ＞ 0')} を 解こう！`,
    `Step❶ ${M('y ＝ 0')} と して ${M('x² − 2x − 3 ＝ 0')}。`,
    `因数分解。　${M('(x ＋ 1)(x − 3) ＝ 0')}`,
    `${M('x ＝ −1, 3')}`,
    `グラフを かく。　x軸と −1、3 で 交わる。`,
    `Step❷ <b>＞ 0</b> なので x軸より <b>上</b> を 塗る。　＝ が ないので 点は <b>白丸</b>。`,
    `Step❸ 塗れた 場所を x軸 方向で 読む。　<b>${M('x ＜ −1, 3 ＜ x')}</b>　<b>完成！</b>`
  ]);
/* ⑵ は 252pt 下 */
const s2 = mk(252, '@@IMG:10:56,530,540,777@@', [`x${P2} ＋ 3x ＋ 2 ＝ 0`, '(x ＋ 2)(x ＋ 1) ＝ 0', 'x ＝ −2, −1'], [[395,'−2'],[450,'−1']], {paint:'down', dot:'f'},
  '−2 ≦ x ≦ −1', [
    `⑵ ${M('x² ＋ 3x ＋ 2 ≦ 0')} を 解こう！`,
    `Step❶ ${M('x² ＋ 3x ＋ 2 ＝ 0')}。`,
    `因数分解。　${M('(x ＋ 2)(x ＋ 1) ＝ 0')}`,
    `${M('x ＝ −2, −1')}`,
    `グラフを かく。　x軸と −2、−1 で 交わる。`,
    `Step❷ <b>≦ 0</b> なので x軸より <b>下</b> を 塗る。　＝ が あるので 点は <b>黒丸</b>（ふくむ）。`,
    `Step❸ <b>${M('−2 ≦ x ≦ −1')}</b>　<b>完成！</b>`
  ]);

const DECK = {title:'③-1 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK, '<span class="mk">2次不等式</span>の<br>解き方', 'グラフを かいて 塗る', '3つの Step で 解こう！', POL, 'グラフを 塗る')},
  {name:'解き方', html:s0}, {name:'⑴', html:s1}, {name:'⑵', html:s2},
  {name:'終', html:endF(KK + '　2次不等式', POL)}
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
