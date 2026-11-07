"""③-3 2次不等式の解法 ver 2（2026-11-07、作り直し）。前の 版（3-3_2次不等式の解法.html、プリント画像の 下書き）は ファイル・URL とも 残す。
作りは ③-2 ver 2・③-1 練習編 ver 3 と 同じ（1画面に 主役 1つ、色も 同じ）。③-1 の 部品（GQ・SUM3 など）を そのまま 使う
（decks_32.py の JS の 前半を つなげる。③-1 を 直すと ここも 変わる）。
流れ：表紙 → グラフの 形は 3つ → 例 ⑴〜⑷（Step❶ 解く → 塗る・答える → 書きこみ）→ まとめ → プリント問題 ⑴〜⑿（Step❶ の 枠 → グラフ → 塗る → 答え）。
判別式は 使わない（先生の 指示、11/7）：交わらない ときは 解の公式で √ の 中が マイナス → 解なし。"""
import os
B = os.path.dirname(os.path.abspath(__file__))

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

/* ===== 例：左の 一覧 ===== */
const EXQ = [['⑴','≧',`x${P2} ＋ 4x ＋ 2`], ['⑵','＜',`x${P2} ＋ 6x ＋ 9`], ['⑶','＞',`x${P2} − 2x ＋ 1`], ['⑷','＞',`x${P2} ＋ 2x ＋ 5`]];
const EXL = cur => `<div class="p3list">${EXQ.map(([n,sg,f],k)=>`<div class="p3i sm${k===cur?' on':''}${k<cur?' done':''}"><span>${n}</span><span class="math">${f} ${sg} 0</span></div>`).join('')}</div>`;

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
const ES1 = (cur, rows, kind, lab, gs, cm, extra='') => `
  <div class="card abs dcard v2 p3">${EQTAPE}
    ${EXL(cur)}
    <div class="v2c">
      <div class="e33h"><span class="v2st e33st">Step❶</span><span class="math e33q">${EXQ[cur][0]}　${EXQ[cur][2]} ${EXQ[cur][1]} 0</span></div>
      <div class="v2calc e33calc math">
        <div class="e33r1"><span>y ＝ ${EXQ[cur][2]}</span><span class="v2q lh e33red" data-s="2">＝</span><span class="lh e33red" data-s="2">0</span></div>
        ${rows.map(([l,rt,s])=>`<div class="v2row" data-s="${s}"><span>${l??''}</span><span class="v2q">${l===null?'':'＝'}</span><span>${rt}</span></div>`).join('')}
        <span class="ytag v2yt lh" data-s="1">y ＝ 0 と する</span>${extra}
      </div>
      <div class="v2gbox e33g">${EGR(kind, lab, gs)}</div>
    </div>
  </div>
  ${cbar(cm)}`;
const HIT = h => `<span class="v2hit">${h}</span>`;

const E1a = ES1(0, [['x', FX(`−4 ± ${SQ('16 − 8')}`,'2'), 3],
    ['', FX(`−${RDX('4','2',5)} ± ${RDX('2','1',5)}${SQ('2')}`, RDX('2','1',5,true)), 4],
    ['', HIT(`−2 ± ${SQ('2')}`), 6]], 0, ['−2−√2','−2+√2'], [7,8,9], [
  `⑴ ${M('x² ＋ 4x ＋ 2 ≧ 0')}。　<b>Step❶</b> まず ＝ 0 の 式を 解く。`,
  `x軸との 共有点 → <b>y ＝ 0</b> と する。`,
  `${M('x² ＋ 4x ＋ 2 ＝ 0')}。　たして 4、かけて 2 に なる 整数は ない → <b>解の公式</b>。`,
  `${M(`x ＝ ${FR('−4 ± √(16 − 8)',2)}`)}`,
  `8 を すだれ算：${M('8 ＝ 2 × 2 × 2')} → ${M('√8 ＝ 2√2')}。`,
  `2 で 約分。`,
  `${M('x ＝ −2 ± √2')}。　これが x軸との 共有点。`,
  `グラフ：x軸に 点を 2つ 打つ。`,
  `下に凸の 放物線を、2つの 点を 通るように かく。`,
  `点の 下に ${M('−2 − √2')}、${M('−2 ＋ √2')} を 書く。　<b>Step❶ 完成！</b>`],
  `<div class="e33sd lh" data-s="4">${SUDARE(8)}</div>`);
const E2a = ES1(1, [['', `(x ＋ 3)${P2}`, 3], ['x', `${HIT('−3')}（重解）`, 4]], 1, ['−3'], [5,6,7], [
  `⑵ ${M('x² ＋ 6x ＋ 9 ＜ 0')}。　<b>Step❶</b> まず ＝ 0 の 式を 解く。`,
  `x軸との 共有点 → <b>y ＝ 0</b> と する。`,
  `${M('x² ＋ 6x ＋ 9 ＝ 0')}。　たして 6、かけて 9 → 同じ ( ) が 2つ。`, `2乗に まとめて ${M('(x ＋ 3)² ＝ 0')}。`,
  `${M('x ＝ −3')}。　答えが 1つ → <b>重解</b>。`,
  `グラフ：x軸に 点を 1つ 打つ。`,
  `放物線は −3 の 点で x軸に <b>接する</b>。`,
  `点の 下に −3 を 書く。　<b>Step❶ 完成！</b>`]);
const E3a = ES1(2, [['', `(x − 1)${P2}`, 3], ['x', `${HIT('1')}（重解）`, 4]], 1, ['1'], [5,6,7], [
  `⑶ ${M('x² − 2x ＋ 1 ＞ 0')}。　<b>Step❶</b> まず ＝ 0 の 式を 解く。`,
  `x軸との 共有点 → <b>y ＝ 0</b> と する。`,
  `${M('x² − 2x ＋ 1 ＝ 0')}。　たして −2、かけて 1 → 同じ ( ) が 2つ。`, `2乗に まとめて ${M('(x − 1)² ＝ 0')}。`,
  `${M('x ＝ 1')}。　答えが 1つ → <b>重解</b>。`,
  `グラフ：x軸に 点を 1つ 打つ。`,
  `放物線は 1 の 点で x軸に <b>接する</b>。`,
  `点の 下に 1 を 書く。　<b>Step❶ 完成！</b>`]);
const E4a = ES1(3, [['x', FX(`−2 ± ${SQ('4 − 20')}`,'2'), 3], ['', FX(`−2 ± ${SQ('−16')}`,'2'), 4],
    [null, `${HIT('解なし')}<span class="e33nw">√ の 中が マイナス</span>`, 5]], 2, [], [0,6,6], [
  `⑷ ${M('x² ＋ 2x ＋ 5 ＞ 0')}。　<b>Step❶</b> まず ＝ 0 の 式を 解く。`,
  `x軸との 共有点 → <b>y ＝ 0</b> と する。`,
  `${M('x² ＋ 2x ＋ 5 ＝ 0')}。　因数分解 できない → <b>解の公式</b>。`,
  `${M(`x ＝ ${FR('−2 ± √(4 − 20)',2)}`)}`,
  `√ の 中が マイナス。`,
  `2乗して マイナスに なる 数は ない → <b>解なし</b>。　x軸との 共有点が ない。`,
  `放物線は x軸と <b>交わらない</b>（x軸より 上に 浮いて いる）。　<b>Step❶ 完成！</b>`],
);

/* ===== 例の 塗る・答える：③-1 の GQ（左の 一覧は 例 ⑴〜⑷） ===== */
const R2 = SQ('2');
const EQP = (cur, o) => GQ({no:EXQ[cur][0], f:EXQ[cur][2], tag:null, cur, list:EXQ.map(([n,sg,f])=>[n,sg,f]), ...o});
const E1b = EQP(0, {s:2, roots:[-2-Math.SQRT2, -2+Math.SQRT2], lab:['−2−√2','−2+√2'], am:true,
  ans:`x ≦ −2 − ${R2}, −2 ＋ ${R2} ≦ x`, dt:[
  `左：<b>x</b> と ${M('−2 − √2')} を 比べる。　x の 方が 小さい。　黒丸 なので ＝ も つけて <b>≦</b>。`, `書き直して ${M('x ≦ −2 − √2')}。`,
  `右：<b>x</b> と ${M('−2 ＋ √2')} を 比べる。　x の 方が 大きい。　黒丸 なので <b>≦</b>。`, `書き直して ${M('−2 ＋ √2 ≦ x')}。`,
  `2か所 なので 答えは 2つ。　答え ${M('x ≦ −2 − √2, −2 ＋ √2 ≦ x')}。`]});
const E2b = EQP(1, {s:1, roots:[-3], ans:'解なし'});
const E3b = EQP(2, {s:0, roots:[1], ans:'1以外の すべての実数'});
const E4b = EQP(3, {s:0, roots:[], ans:'すべての実数'});

/* ===== 例の 書きこみ：プリント（No.13）の 配置。Step❶ は 書いた 形、塗る(1) → 答え(2) だけ 動かす ===== */
const BX33 = (r,c) => `<rect fill="${c}" x="${r[0]}" y="${r[1]}" width="${(r[2]-r[0]).toFixed(1)}" height="${(r[3]-r[1]).toFixed(1)}"/>`;
const W33 = (cur, lines, kind, lab, paint, dot, ans, afs, cm, sud) => {
  const ay = 205, xv = 300.4;
  const g = kind===0 ? {yv:ay+22, q:22/18**2, lab:[[xv-20,lab[0],'end'],[xv+20,lab[1],'start']]} : kind===1 ? {yv:ay, q:0.035, lab:[[xv,lab[0]]]} : {yv:ay-16, q:0.03, lab:[]};
  const gr = PB({xv, ay, top:134, s:0, ls:0, ...g, ...(paint?{paint, ps:1}:{}), ...(dot?{dot, ds:1}:{})});
  return ptSlide({clip:[58,100,534,242],
    svg:[BX33([63.5,128.4,241.6,238.2],'#dce6f2'), BX33([246.6,128.4,354.2,238.2],'#dce6f2'), BX33([359.6,207,527.3,238.2],'#dbeef4'),
      `<line x1="256" y1="${ay}" x2="343" y2="${ay}" stroke="#555" stroke-width=".8"/><polygon points="345,${ay} 341,${ay-1.6} 341,${ay+1.6}" fill="#555"/><text class="pgt" x="343" y="${ay+8}" font-style="italic">x</text>`,
      `<g class="w33">${gr}</g>`],
    items:[T([61.6,103,330,121],`${EXQ[cur][0]}<span class="xsp"></span>${EXQ[cur][2]} ${EXQ[cur][1]} 0`,10.5),
      ...lines.map((h,i)=>({s:0, r:[68,134+i*26,240,158+i*26], h, fs:10, al:'l', cls:'xan'})),
      ...(sud ? [{s:0, r:[196,132,240,200], h:SUDARE(sud), fs:6}] : []),
      XA(2,[359.6,207,527.3,238.2], ans, afs||11)],
    done:2, cm});
};
const E1c = W33(0, [`x${P2} ＋ 4x ＋ 2 ＝ 0`, `x ＝ ${FX(`−4 ± ${SQ('16 − 8')}`,'2')}`, `＝ ${FX(`−4 ± 2${SQ('2')}`,'2')}`, `＝ −2 ± ${SQ('2')}`],
  0, ['−2−√2','−2+√2'], 'up', 'f', `x ≦ −2 − ${R2}, −2 ＋ ${R2} ≦ x`, 9.5,
  [`プリントに 書こう。　Step❶ は 書けて いる。`, `上を 塗る。　＝ が ある ので x軸も 塗る → 黒丸。`, `答えの 枠に ${M('x ≦ −2 − √2, −2 ＋ √2 ≦ x')}。　<b>完成！</b>`], 8);
const E2c = W33(1, [`x${P2} ＋ 6x ＋ 9 ＝ 0`, `(x ＋ 3)${P2} ＝ 0`, 'x ＝ −3（重解）'], 1, ['−3'], null, 'o', JA('解なし'), 11,
  [`プリントに 書こう。　Step❶ は 書けて いる。`, `下を 塗りたい けど、x軸より 下に グラフが ない。　−3 は 白丸。`, `答えの 枠に <b>解なし</b>。　<b>完成！</b>`]);
const E3c = W33(2, [`x${P2} − 2x ＋ 1 ＝ 0`, `(x − 1)${P2} ＝ 0`, 'x ＝ 1（重解）'], 1, ['1'], 'all', 'o', JA('1以外のすべての実数'), 10,
  [`プリントに 書こう。　Step❶ は 書けて いる。`, `上を 塗る → 全部 塗れる。　1 は x軸の 上 なので 白丸。`, `答えの 枠に <b>1以外の すべての実数</b>。　<b>完成！</b>`]);
const E4c = W33(3, [`x${P2} ＋ 2x ＋ 5 ＝ 0`, `x ＝ ${FX(`−2 ± ${SQ('4 − 20')}`,'2')}`, `＝ ${FX(`−2 ± ${SQ('−16')}`,'2')}`, JA('√ の中がマイナス → 解なし')], 2, [], 'all', null, JA('すべての実数'), 11,
  [`プリントに 書こう。　Step❶ は 書けて いる。`, `上を 塗る → グラフ 全部 塗れる。`, `答えの 枠に <b>すべての実数</b>。　<b>完成！</b>`]);

/* ===== プリント問題③-3（No.14・15、⑴〜⑿）：Step❶ の 枠（大きく）→ グラフ → ③-1 と 同じ 塗る・答える =====
   P3Q = [番号, 式, 不等号の 番号, 根, 答え, 文字, 計算の 行 [[html, 説明], …], 答えの 小さな まとめ, オプション] */
const PRE33 = (no, f, sg, rows, res, gline, sud) => {
  const k = rows.length + 1;
  return {cm:[`${no} ${M(`${f.replace(/<sup>2<\/sup>/,'²')} ${sg} 0`)}。　<b>Step❶</b> まず ＝ 0 の 式を 解く。`, ...rows.map(r=>r[1]), gline],
    html:`<div class="p3w" data-o="${k}"><span class="v2mk">まず ＝ 0 を 解く</span></div>
      <div class="q33c math" data-o="${k}">${rows.map(([h],i)=>`<div class="lh" data-s="${i+1}"><span>${h}</span></div>`).join('')}${sud ? `<div class="q33sd lh" data-s="${sud[1]}">${SUDARE(sud[0])}</div>` : ''}</div>
      <div class="q33r math lh" data-s="${k}">${res}</div>`}; };
const GL = ['グラフを かく。　x軸と <b>2点で 交わる</b>。', 'グラフは x軸に <b>接する</b>。', 'グラフは x軸と <b>交わらない</b>（上に 浮いて いる）。'];
const FAC = (eq, fac, root, how) => [[`${eq} ＝ 0`, `${M(eq.replace(/<sup>2<\/sup>/,'²') + ' ＝ 0')}。　${how}`], [`${fac} ＝ 0`, M(fac.replace(/<sup>2<\/sup>/,'²') + ' ＝ 0')], [`x ＝ ${root}`, M('x ＝ ' + root.replace(/<[^>]+>/g,''))]];
const P3Q = [
  ['⑴',`x${P2} ＋ 5x ＋ 6`,2,[-3,-2],'x ≦ −3, −2 ≦ x',null, FAC(`x${P2} ＋ 5x ＋ 6`,'(x ＋ 3)(x ＋ 2)','−3, −2','たして 5、かけて 6 → 因数分解。'), 'x ＝ −3, −2'],
  ['⑵',`2x${P2} ＋ 3x − 2`,1,[-2,0.5],`−2 ＜ x ＜ ${FR(1,2)}`,['−2','1/2'], FAC(`2x${P2} ＋ 3x − 2`,'(x ＋ 2)(2x − 1)',`−2, ${FR(1,2)}`,'たすき掛けで 因数分解。'), `x ＝ −2, ${FR(1,2)}`, {am:true}],
  ['⑶',`x${P2} ＋ 3x − 5`,1,[-4.19,1.19],`${FX(`−3 − ${SQ('29')}`,'2')} ＜ x ＜ ${FX(`−3 ＋ ${SQ('29')}`,'2')}`,['(−3−√29)/2','(−3+√29)/2'],
    [[`x${P2} ＋ 3x − 5 ＝ 0`, `${M('x² ＋ 3x − 5 ＝ 0')}。　因数分解 できない → <b>解の公式</b>。`], [`x ＝ ${FX(`−3 ± ${SQ('9 ＋ 20')}`,'2')}`, M(`x ＝ ${FR('−3 ± √(9 ＋ 20)',2)}`)],
     [`x ＝ ${FX(`−3 ± ${SQ('29')}`,'2')}`, `${M(`x ＝ ${FR('−3 ± √29',2)}`)}。　29 は これ以上 簡単に ならない。`]], `x ＝ ${FX(`−3 ± ${SQ('29')}`,'2')}`, {am:true}],
  ['⑷',`x${P2} ＋ 2x − 2`,2,[-1-Math.sqrt(3),-1+Math.sqrt(3)],`x ≦ −1 − ${SQ('3')}, −1 ＋ ${SQ('3')} ≦ x`,['−1−√3','−1+√3'],
    [[`x${P2} ＋ 2x − 2 ＝ 0`, `${M('x² ＋ 2x − 2 ＝ 0')}。　因数分解 できない → <b>解の公式</b>。`], [`x ＝ ${FX(`−2 ± ${SQ('4 ＋ 8')}`,'2')}`, `${M(`x ＝ ${FR('−2 ± √(4 ＋ 8)',2)}`)}。　12 を すだれ算 → ${M('√12 ＝ 2√3')}。`],
     [`x ＝ ${FX(`−${RDX('2','1',3)} ± ${RDX('2','1',3)}${SQ('3')}`, RDX('2','1',3,true))} <span class="vm">＝ −1 ± ${SQ('3')}</span>`, `2 で 約分 して ${M('x ＝ −1 ± √3')}。`]], `x ＝ −1 ± ${SQ('3')}`, {am:true, sud:[12,2]}],
  ['⑸',`x${P2} ＋ 5x`,3,[-5,0],'−5 ≦ x ≦ 0',null, FAC(`x${P2} ＋ 5x`,'x(x ＋ 5)','−5, 0','共通な x で くくる。'), 'x ＝ −5, 0'],
  ['⑹',`x${P2} − 4`,0,[-2,2],'x ＜ −2, 2 ＜ x',null, FAC(`x${P2} − 4`,'(x ＋ 2)(x − 2)','−2, 2','2乗 − 2乗 → 因数分解。'), 'x ＝ −2, 2'],
  ['⑺',`x${P2} ＋ 4x ＋ 4`,0,[-2],'−2以外の すべての実数',null, FAC(`x${P2} ＋ 4x ＋ 4`,`(x ＋ 2)${P2}`,'−2（重解）','たして 4、かけて 4 → 同じ ( ) が 2つ。'), 'x ＝ −2（重解）'],
  ['⑻',`x${P2} ＋ 4x ＋ 4`,2,[-2],'すべての実数',null, FAC(`x${P2} ＋ 4x ＋ 4`,`(x ＋ 2)${P2}`,'−2（重解）','⑺ と 同じ 式。'), 'x ＝ −2（重解）'],
  ['⑼',`x${P2} − 6x ＋ 9`,1,[3],'解なし',null, FAC(`x${P2} − 6x ＋ 9`,`(x − 3)${P2}`,'3（重解）','たして −6、かけて 9 → 同じ ( ) が 2つ。'), 'x ＝ 3（重解）'],
  ['⑽',`x${P2} − 6x ＋ 9`,3,[3],'x ＝ 3',null, FAC(`x${P2} − 6x ＋ 9`,`(x − 3)${P2}`,'3（重解）','⑼ と 同じ 式。'), 'x ＝ 3（重解）'],
  ['⑾',`x${P2} ＋ 4x ＋ 6`,0,[],'すべての実数',null,
    [[`x${P2} ＋ 4x ＋ 6 ＝ 0`, `${M('x² ＋ 4x ＋ 6 ＝ 0')}。　因数分解 できない → <b>解の公式</b>。`], [`x ＝ ${FX(`−4 ± ${SQ('16 − 24')}`,'2')} ＝ ${FX(`−4 ± ${SQ('−8')}`,'2')}`, M(`x ＝ ${FR('−4 ± √(16 − 24)',2)} ＝ ${FR('−4 ± √(−8)',2)}`)],
     [JA('√ の中がマイナス → 解なし'), '√ の 中が マイナス → <b>解なし</b>。　x軸との 共有点が ない。']], JA('共有点なし')],
  ['⑿',`x${P2} ＋ 4x ＋ 6`,3,[],'解なし',null,
    [[`x${P2} ＋ 4x ＋ 6 ＝ 0`, `${M('x² ＋ 4x ＋ 6 ＝ 0')}。　⑾ と 同じ 式。`], [`x ＝ ${FX(`−4 ± ${SQ('16 − 24')}`,'2')} ＝ ${FX(`−4 ± ${SQ('−8')}`,'2')}`, M(`x ＝ ${FR('−4 ± √(16 − 24)',2)} ＝ ${FR('−4 ± √(−8)',2)}`)],
     [JA('√ の中がマイナス → 解なし'), '√ の 中が マイナス → <b>解なし</b>。　x軸との 共有点が ない。']], JA('共有点なし')]];
const PROB33 = P3Q.map(([no,f,s,roots,ans,lab,rows,res,opt],i)=>{ const g0 = Math.floor(i/4)*4, o = opt || {};
  return {name:`問 ${no}`, html:GQ({no, f, s, roots, ans, lab: lab || undefined, span:o.span, wo:o.wo, cur:i-g0, tag:'プリント問題③-3', am:o.am,
    list:P3Q.slice(g0,g0+4).map(q=>[q[0], SIGN3[q[2]], q[1]]),
    pre:PRE33(no, f, SIGN3[s], rows, res, GL[roots.length===2 ? 0 : roots.length===1 ? 1 : 2], o.sud)})}; });
const PH33 = probHead('プリント問題③-3', '次の 2次不等式を 解け。', ['⑴〜⑹　2点で 交わる', '⑺〜⑽　接する', '⑾⑿　交わらない'],
  `ここから <b>プリント問題③-3</b>。　Step❶ で 解いて、グラフを かいて、塗って 答える！`);

const DECK = {title:'③-3 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK33, '<span class="mk">2次不等式</span><br>いろいろ', '接する・交わらない とき', 'グラフを かけば こわくない！', POL33, 'グラフの 形')},
  {name:'グラフの 形は 3つ', html:IN33},
  {name:'⑴ Step❶', html:E1a}, {name:'⑴ 塗る・答える', html:E1b}, {name:'⑴ 書きこみ', html:E1c},
  {name:'⑵ Step❶', html:E2a}, {name:'⑵ 塗る・答える', html:E2b}, {name:'⑵ 書きこみ', html:E2c},
  {name:'⑶ Step❶', html:E3a}, {name:'⑶ 塗る・答える', html:E3b}, {name:'⑶ 書きこみ', html:E3c},
  {name:'⑷ Step❶', html:E4a}, {name:'⑷ 塗る・答える', html:E4b}, {name:'⑷ 書きこみ', html:E4c},
  {name:'まとめ', html:SUM3}, {name:'プリント問題', html:PH33}, ...PROB33,
  {name:'終', html:endF(KK33 + '　2次不等式', POL33)}]};
'''

def add(decks):
    import decks_32
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    parts = decks_32.JS.split('const PG = [')
    assert len(parts) == 2
    decks['3-3_2次不等式の解法_v2'] = ('③-3 2次不等式の解法 ver 2', base + parts[0] + JS33)
