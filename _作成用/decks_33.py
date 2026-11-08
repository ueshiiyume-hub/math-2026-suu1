"""③-3 2次不等式の解法 ver 2（2026-11-07、作り直し）。前の 版（3-3_2次不等式の解法.html、プリント画像の 下書き）は ファイル・URL とも 残す。
作りは ③-2 ver 2・③-1 練習編 ver 3 と 同じ（1画面に 主役 1つ、色も 同じ）。③-1 の 部品（GQ・SUM3 など）を そのまま 使う
（decks_32.py の JS の 前半を つなげる。③-1 を 直すと ここも 変わる）。
流れ：表紙 → グラフの 形は 3つ → 例 ⑴〜⑷ → まとめ → プリント問題 ⑴〜⑿。例も 問題も 1ページ（1画面）に Step❶〜❸（11/8、SIDEG ＋ GQ の side）。
判別式は 使わない（先生の 指示、11/7）：交わらない ときは 解の公式で √ の 中が マイナス → 解なし。"""
import os
B = os.path.dirname(os.path.abspath(__file__))

SHARED33 = r'''
/* ③-3・③-4 で 使う 部品（decks_34.py も つなげる） */
/* ===== 例の Step❶：左に 計算（大きな 枠）、右に グラフ（点 → 放物線 → 座標）。③-2 の Step❶ と 同じ 形 =====
   rows：[[左, 右, 番], …]（左が '' なら ＝ だけ）。kind：0 交わる・1 接する・2 交わらない。lab：点の 下の 文字。g：グラフの 番 [点, 線, 文字] */
const EGR = (kind, lab, gs) => {
  const W = 290, H = 380, ay = kind===2 ? 300 : 250, cx = 145, r = 55;
  const vy = kind===0 ? ay+55 : kind===1 ? ay : ay-60, q = kind===0 ? 55/r**2 : 0.02;
  const hw = Math.sqrt((vy-20)/q); let d=''; for(let i=0;i<=60;i++){ const dx=-hw+2*hw*i/60; d+=(i?'L':'M')+f1(cx+dx)+' '+f1(vy-q*dx*dx)+' '; }
  const pts = kind===0 ? [cx-r, cx+r] : kind===1 ? [cx] : [];
  const LB = (x, t, an) => HASM(t) ? FO3(x, ay+28, TXH(t), 'fo3n e33f', an) : `<text class="inum e33n" x="${x}" y="${ay+38}" text-anchor="${an}">${t}</text>`;
  const txt = kind===0 ? LB(cx-r-6, lab[0], 'end') + LB(cx+r+6, lab[1], 'start')
            : kind===1 ? LB(cx, lab[0], 'middle')
            : `<text class="e33nt" x="${cx}" y="${ay+44}" text-anchor="middle">x軸と 交わらない</text>`;
  return `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
    <line class="iax" x1="8" y1="${ay}" x2="${W-14}" y2="${ay}"/><polygon class="iah" points="${W-2},${ay} ${W-16},${ay-7} ${W-16},${ay+7}"/><text class="ixl" x="${W-20}" y="${ay+30}">x</text>
    <path class="curve v2cv" data-s="${gs[1]}" pathLength="1" d="${d}"/>
    ${pts.length ? `<g class="gs" data-s="${gs[0]}">${pts.map(x=>`<circle class="v2pt" cx="${x}" cy="${ay}" r="8"/>`).join('')}</g>` : ''}
    <g class="gs" data-s="${gs[2]}">${txt}</g></svg>`; };
const ES1G = (q, list, rows, kind, lab, gs, cm, extra='') => `
  <div class="card abs dcard v2 p3">${EQTAPE}
    ${list}
    <div class="v2c">
      <div class="e33h"><span class="v2st e33st">Step❶</span><span class="math e33q">${q[0]}　${q[2]} ${q[1]} 0</span></div>
      <div class="v2calc e33calc math">
        <div class="e33r1"><span>y ＝ ${q[2]}</span><span class="v2q lh e33red" data-s="2">＝</span><span class="lh e33red" data-s="2">0</span></div>
        ${rows.map(([l,rt,s])=>`<div class="v2row" data-s="${s}"><span>${l??''}</span><span class="v2q">${l===null?'':'＝'}</span><span>${rt}</span></div>`).join('')}
        <span class="ytag v2yt lh" data-s="1">y ＝ 0 と する</span>${extra}
      </div>
      <div class="v2gbox e33g">${EGR(kind, lab, gs)}</div>
    </div>
  </div>
  ${cbar(cm)}`;
const HIT = h => `<span class="v2hit">${h}</span>`;
const PRE33 = (no, f, sg, rows, res, gline, sud, head='まず ＝ 0 を 解く', c0='<b>Step❶</b> まず ＝ 0 の 式を 解く。') => {
  const k = rows.length + 1;
  return {cm:[`${no} ${M(`${f.replace(/<sup>2<\/sup>/,'²')} ${sg} 0`)}。　${c0}`, ...rows.map(r=>r[1]), gline],
    html:`<div class="p3w" data-o="${k}"><span class="v2mk">${head}</span></div>
      <div class="q33c math" data-o="${k}">${rows.map(([h],i)=>`<div class="lh" data-s="${i+1}"><span>${h}</span></div>`).join('')}${sud ? `<div class="q33sd lh" data-s="${sud[1]}">${SUDARE(sud[0])}</div>` : ''}</div>
      <div class="q33r math lh" data-s="${k}">${res}</div>`}; };
const GL = ['グラフを かく。　x軸と <b>2点で 交わる</b>。', 'グラフは x軸に <b>接する</b>。', 'グラフは x軸と <b>交わらない</b>（上に 浮いて いる）。'];
const FAC = (eq, fac, root, how) => [[`${eq} ＝ 0`, `${M(eq.replace(/<sup>2<\/sup>/,'²') + ' ＝ 0')}。　${how}`], [`${fac} ＝ 0`, M(fac.replace(/<sup>2<\/sup>/,'²') + ' ＝ 0')], [`x ＝ ${root}`, M('x ＝ ' + root.replace(/<[^>]+>/g,''))]];

/* 問題を 解く ページ（1画面、③-3・③-4、先生の 指示 11/8）：左の 列に 式と Step❶ の 計算（大きく）、右に グラフ → 塗る → 答え（GQ の side）。
   o = {no, nf, sg, org（③-4：−1 を かける 前の 式。あれば 0 元の 式・1 新しい 式・2 二重線）, rows:[[html, 番], …], cm:[0〜k−1 番の 説明], gl, sud:[n, 番]}
   計算は 1行ずつ 出さず、まとめて 出す（解の公式に 当てはめる ところまで 1番。すだれ算は 小さく 残す） */
const SIDEG = o => { const k = o.cm.length;
  const top = o.org
    ? `<div class="s4q math"><span class="s4no">${o.no}</span><span class="s4org">${o.org}<span class="s4strike" data-s="2"></span></span></div>
      <div class="s4new math lh" data-s="1"><span class="q34m">× (−1)</span>${o.nf} <span class="p3sg" data-o="${k+1}">${o.sg} 0</span></div>
      <div class="s4tip lh" data-s="2"><span class="s4bdg">おすすめ</span>元の 式は 二重線で 消す</div>`
    : `<div class="s4q s4q3 math"><span class="s4no">${o.no}</span>${o.nf} <span class="p3sg" data-o="${k+1}">${o.sg} 0</span></div>`;
  return {cm:[...o.cm, o.gl], html:`<div class="s4col">${top}
      <div class="s4calc math">${o.rows.map(([h,st])=>`<div class="lh" data-s="${st}"><span>${h}</span></div>`).join('')}</div>
      ${o.sud ? `<div class="s4sd lh" data-s="${o.sud[1]}" data-o="${k}">${SUDARE(o.sud[0])}</div>` : ''}
    </div>`}; };
/* x の 根 2つ → 交わる・1つ → 接する・なし → 交わらない */
const GLK = roots => GL[roots.length===2 ? 0 : roots.length===1 ? 1 : 2];
'''

JS33 = r'''
const KK33 = KIMATSU + '　③-3';
const POL33 = `<div class="fpol"><div class="fa math">接する・交わらない</div><div class="fv">とき も</div><div class="fb" style="font-size:24px;font-weight:900">塗って 答える</div></div>`;

/* ===== 導入：グラフの 形は 3つ ===== */
const SHP = (k, t, sub) => { const W = 300, H = 230, ay = k===2 ? 190 : 150, vy = k===0 ? ay+45 : k===1 ? ay : ay-40, q = k===0 ? 45/55**2 : 0.016;
  const hw = Math.sqrt((vy-14)/q); let d=''; for(let i=0;i<=60;i++){ const dx=-hw+2*hw*i/60; d+=(i?'L':'M')+f1(150+dx)+' '+f1(vy-q*dx*dx)+' '; }
  const pts = k===0 ? [95,205] : k===1 ? [150] : [];
  return `<div class="card sh33 lh" data-s="${k}"><svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
    <line class="iax" x1="10" y1="${ay}" x2="${W-16}" y2="${ay}"/><polygon class="iah" points="${W-2},${ay} ${W-18},${ay-8} ${W-18},${ay+8}"/>
    <path class="icv p3cv" d="${d}"/>${pts.map(x=>`<circle class="v2pt" cx="${x}" cy="${ay}" r="8"/>`).join('')}</svg>
    <div class="sh33t">${t}</div><div class="sh33s">${sub}</div></div>`; };
const IN33 = `
  <div class="card abs dcard v2 p3">${EQTAPE}
    <div class="sh33row">${SHP(0,'2点で 交わる','③-2 で やった')}${SHP(1,'1点で 接する','今回')}${SHP(2,'交わらない','今回')}</div>
  </div>
  ${cbar([`③-2 では、グラフが x軸と <b>2点で 交わる</b> 形 だった。`, `グラフが x軸に <b>1点で 接する</b> ことも ある。`,
    `x軸と <b>交わらない</b> ことも ある。　どの 形でも「塗って 答える」は 同じ！`])}`;

/* ===== 例 ⑴〜⑷・プリント問題 ⑴〜⑿：どれも 1ページ（1画面）に Step❶〜❸（SIDEG ＋ GQ の side。先生の 指示 11/8）
   Q33(no, f, 不等号の 番号, 根, 答え, {lab, am, dt, tag, rows, cm, sud}) ===== */
const EQ0 = f => `${f} ＝ 0`, MS = f => M(f.replace(/<sup>2<\/sup>/g,'²'));
const Q33 = (no, f, s, roots, ans, o) => GQ({no, f, s, roots, ans, lab:o.lab, am:o.am, dt:o.dt, tag:o.tag===undefined ? 'プリント問題③-3' : o.tag, side:true, W:600,
  pre:SIDEG({no, nf:f, sg:SIGN3[s], rows:o.rows, sud:o.sud, gl:GLK(roots),
    cm:[`${no} ${MS(f + ' ' + SIGN3[s] + ' 0')}。　<b>Step❶</b> まず ＝ 0 の 式を 解く。`, ...o.cm]})});
/* 因数分解 で 解ける：1番 ＝0 と 因数分解、2番 x ＝ */
const FAC2 = (f, fac, root, how) => ({rows:[[EQ0(f),1],[EQ0(fac),1],[`x ＝ ${root}`,2]], cm:[`${MS(EQ0(f))}。　${how}　${MS(EQ0(fac))}`, `${M('x ＝ ' + root)}。`]});
const R2 = SQ('2'), R3 = SQ('3');
const E1 = Q33('⑴', `x${P2} ＋ 4x ＋ 2`, 2, [-2-Math.SQRT2, -2+Math.SQRT2], `x ≦ −2 − ${R2}, −2 ＋ ${R2} ≦ x`, {tag:null, lab:['−2−√2','−2+√2'], am:true,
  rows:[[EQ0(`x${P2} ＋ 4x ＋ 2`),1], [`x ＝ ${FX(`−4 ± ${SQ('16 − 8')}`,'2')}`,1], [`x ＝ ${FX(`−${RDX('4','2',3)} ± ${RDX('2','1',3)}${R2}`, RDX('2','1',3,true))} <span class="vm">＝ −2 ± ${R2}</span>`,3]],
  sud:[8,2], cm:[`${MS(EQ0(`x${P2} ＋ 4x ＋ 2`))}。　因数分解 できない → <b>解の公式</b>。　${M(`x ＝ ${FR('−4 ± √(16 − 8)',2)}`)}`,
    `8 を すだれ算：${M('8 ＝ 2 × 2 × 2')} → ${M('√8 ＝ 2√2')}。`, `2 で 約分 して ${M('x ＝ −2 ± √2')}。`],
  dt:[`左：<b>x</b> と ${M('−2 − √2')} を 比べる。　x の 方が 小さい。　黒丸 なので ＝ も つけて <b>≦</b>。`, `書き直して ${M('x ≦ −2 − √2')}。`,
    `右：<b>x</b> と ${M('−2 ＋ √2')} を 比べる。　x の 方が 大きい。　黒丸 なので <b>≦</b>。`, `書き直して ${M('−2 ＋ √2 ≦ x')}。`,
    `2か所 なので 答えは 2つ。　答え ${M('x ≦ −2 − √2, −2 ＋ √2 ≦ x')}。`]});
const E2 = Q33('⑵', `x${P2} ＋ 6x ＋ 9`, 1, [-3], '解なし', {tag:null, ...FAC2(`x${P2} ＋ 6x ＋ 9`, `(x ＋ 3)${P2}`, '−3（重解）', 'たして 6、かけて 9 → 同じ ( ) が 2つ。')});
const E3 = Q33('⑶', `x${P2} − 2x ＋ 1`, 0, [1], '1以外の すべての実数', {tag:null, ...FAC2(`x${P2} − 2x ＋ 1`, `(x − 1)${P2}`, '1（重解）', 'たして −2、かけて 1 → 同じ ( ) が 2つ。')});
const E4 = Q33('⑷', `x${P2} ＋ 2x ＋ 5`, 0, [], 'すべての実数', {tag:null,
  rows:[[EQ0(`x${P2} ＋ 2x ＋ 5`),1], [`x ＝ ${FX(`−2 ± ${SQ('4 − 20')}`,'2')} ＝ ${FX(`−2 ± ${SQ('−16')}`,'2')}`,1], [JA('√ の中がマイナス → 解なし'),2]],
  cm:[`${MS(EQ0(`x${P2} ＋ 2x ＋ 5`))}。　因数分解 できない → <b>解の公式</b>。　${M(`x ＝ ${FR('−2 ± √(4 − 20)',2)} ＝ ${FR('−2 ± √(−16)',2)}`)}`,
    `√ の 中が マイナス。　2乗して マイナスに なる 数は ない → <b>解なし</b>（x軸との 共有点が ない）。`]});

/* プリント問題③-3 */
const NOROOT = (f, a, b) => ({rows:[[EQ0(f),1], [`x ＝ ${FX(`−4 ± ${SQ(a)}`,'2')} ＝ ${FX(`−4 ± ${SQ(b)}`,'2')}`,1], [JA('√ の中がマイナス → 解なし'),2]],
  cm:[`${MS(EQ0(f))}。　因数分解 できない → <b>解の公式</b>。　${M(`x ＝ ${FR(`−4 ± √(${a})`,2)} ＝ ${FR(`−4 ± √(${b})`,2)}`)}`, '√ の 中が マイナス → <b>解なし</b>（x軸との 共有点が ない）。']});
const PROB33 = [
  Q33('⑴', `x${P2} ＋ 5x ＋ 6`, 2, [-3,-2], 'x ≦ −3, −2 ≦ x', FAC2(`x${P2} ＋ 5x ＋ 6`, '(x ＋ 3)(x ＋ 2)', '−3, −2', 'たして 5、かけて 6 → 因数分解。')),
  Q33('⑵', `2x${P2} ＋ 3x − 2`, 1, [-2,0.5], `−2 ＜ x ＜ ${FR(1,2)}`, {lab:['−2','1/2'], am:true, ...FAC2(`2x${P2} ＋ 3x − 2`, '(x ＋ 2)(2x − 1)', `−2, ${FR(1,2)}`, 'たすき掛けで 因数分解。')}),
  Q33('⑶', `x${P2} ＋ 3x − 5`, 1, [-4.19,1.19], `${FX(`−3 − ${SQ('29')}`,'2')} ＜ x ＜ ${FX(`−3 ＋ ${SQ('29')}`,'2')}`, {lab:['(−3−√29)/2','(−3+√29)/2'], am:true,
    rows:[[EQ0(`x${P2} ＋ 3x − 5`),1], [`x ＝ ${FX(`−3 ± ${SQ('9 ＋ 20')}`,'2')}`,1], [`x ＝ ${FX(`−3 ± ${SQ('29')}`,'2')}`,2]],
    cm:[`${MS(EQ0(`x${P2} ＋ 3x − 5`))}。　因数分解 できない → <b>解の公式</b>。　${M(`x ＝ ${FR('−3 ± √(9 ＋ 20)',2)}`)}`, `${M(`x ＝ ${FR('−3 ± √29',2)}`)}。　29 は これ以上 簡単に ならない。`]}),
  Q33('⑷', `x${P2} ＋ 2x − 2`, 2, [-1-Math.sqrt(3),-1+Math.sqrt(3)], `x ≦ −1 − ${R3}, −1 ＋ ${R3} ≦ x`, {lab:['−1−√3','−1+√3'], am:true,
    rows:[[EQ0(`x${P2} ＋ 2x − 2`),1], [`x ＝ ${FX(`−2 ± ${SQ('4 ＋ 8')}`,'2')}`,1], [`x ＝ ${FX(`−${RDX('2','1',3)} ± ${RDX('2','1',3)}${R3}`, RDX('2','1',3,true))} <span class="vm">＝ −1 ± ${R3}</span>`,3]],
    sud:[12,2], cm:[`${MS(EQ0(`x${P2} ＋ 2x − 2`))}。　因数分解 できない → <b>解の公式</b>。　${M(`x ＝ ${FR('−2 ± √(4 ＋ 8)',2)}`)}`,
      `12 を すだれ算：${M('12 ＝ 2 × 2 × 3')} → ${M('√12 ＝ 2√3')}。`, `2 で 約分 して ${M('x ＝ −1 ± √3')}。`]}),
  Q33('⑸', `x${P2} ＋ 5x`, 3, [-5,0], '−5 ≦ x ≦ 0', FAC2(`x${P2} ＋ 5x`, 'x(x ＋ 5)', '−5, 0', '共通な x で くくる。')),
  Q33('⑹', `x${P2} − 4`, 0, [-2,2], 'x ＜ −2, 2 ＜ x', FAC2(`x${P2} − 4`, '(x ＋ 2)(x − 2)', '−2, 2', '2乗 − 2乗 → 因数分解。')),
  Q33('⑺', `x${P2} ＋ 4x ＋ 4`, 0, [-2], '−2以外の すべての実数', FAC2(`x${P2} ＋ 4x ＋ 4`, `(x ＋ 2)${P2}`, '−2（重解）', 'たして 4、かけて 4 → 同じ ( ) が 2つ。')),
  Q33('⑻', `x${P2} ＋ 4x ＋ 4`, 2, [-2], 'すべての実数', FAC2(`x${P2} ＋ 4x ＋ 4`, `(x ＋ 2)${P2}`, '−2（重解）', '⑺ と 同じ 式。')),
  Q33('⑼', `x${P2} − 6x ＋ 9`, 1, [3], '解なし', FAC2(`x${P2} − 6x ＋ 9`, `(x − 3)${P2}`, '3（重解）', 'たして −6、かけて 9 → 同じ ( ) が 2つ。')),
  Q33('⑽', `x${P2} − 6x ＋ 9`, 3, [3], 'x ＝ 3', FAC2(`x${P2} − 6x ＋ 9`, `(x − 3)${P2}`, '3（重解）', '⑼ と 同じ 式。')),
  Q33('⑾', `x${P2} ＋ 4x ＋ 6`, 0, [], 'すべての実数', NOROOT(`x${P2} ＋ 4x ＋ 6`, '16 − 24', '−8')),
  Q33('⑿', `x${P2} ＋ 4x ＋ 6`, 3, [], '解なし', NOROOT(`x${P2} ＋ 4x ＋ 6`, '16 − 24', '−8'))
].map((h,i)=>({name:`問 ${'⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿'[i]}`, html:h}));
const PH33 = probHead('プリント問題③-3', '次の 2次不等式を 解け。', ['⑴〜⑹　2点で 交わる', '⑺〜⑽　接する', '⑾⑿　交わらない'],
  `ここから <b>プリント問題③-3</b>。　Step❶ で 解いて、グラフを かいて、塗って 答える！`);

const DECK = {title:'③-3 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK33, '<span class="mk">2次不等式</span><br>いろいろ', '接する・交わらない とき', 'グラフを かけば こわくない！', POL33, 'グラフの 形')},
  {name:'グラフの 形は 3つ', html:IN33},
  {name:'⑴', html:E1}, {name:'⑵', html:E2}, {name:'⑶', html:E3}, {name:'⑷', html:E4},
  {name:'まとめ', html:SUM3}, {name:'プリント問題', html:PH33}, ...PROB33,
  {name:'終', html:endF(KK33 + '　2次不等式', POL33)}]};
'''

def add(decks):
    import decks_32
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    parts = decks_32.JS.split('const PG = [')
    assert len(parts) == 2
    decks['3-3_2次不等式の解法_v2'] = ('③-3 2次不等式の解法 ver 2', base + parts[0] + SHARED33 + JS33)
