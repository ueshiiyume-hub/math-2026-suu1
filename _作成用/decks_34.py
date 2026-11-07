"""③-4 2次不等式の解法（x² の 前が マイナス）ver 2（2026-11-07、作り直し）。前の 版（3-4_2次不等式の解法.html、プリント画像の 下書き）は 残す。
③-3 ver 2 と 同じ 作り：③-1 の 部品（decks_32.py の 前半）＋ ③-3 の 部品（decks_33.SHARED33）を つなげる。
流れ：表紙 → 解き方（−1 を かけて 向きを 逆に）→ なぜ 向きが 逆に なるか（2 ＞ 1 → −2 ＜ −1）→ 例⑴（Step❶ 解く → 塗る・答える → 書きこみ）
→ まとめ → プリント問題 ⑴⑵（−1 を かける → 計算の 枠 → グラフ → 塗る → 答え）。判別式は 使わない。"""
import os
B = os.path.dirname(os.path.abspath(__file__))

JS34 = r'''
const KK34 = KIMATSU + '　③-4';
const POL34 = `<div class="fpol"><div class="fa math">−x${P2} − 6x − 7 ＞ 0</div><div class="fv">× (−1)　向きが 逆に！</div><div class="fb math">x${P2} ＋ 6x ＋ 7 ＜ 0</div></div>`;

/* ===== 解き方（プリントの 上の 枠）：−1 を かけると 符号が 1つずつ 変わり、最後に 不等号の 向きが 逆に ===== */
const H4A = [`−x${P2}`, '− 6x', '− 7', '＞', '0'];
const H4B = [[`x${P2}`,2,1], ['＋ 6x',3,1], ['＋ 7',4,1], ['＜',5,2], ['0',5,0]];   // [文字, 番, 0 そのまま・1 符号が 変わる・2 向きが 逆]
const HOW4 = `
  <div class="card abs dcard v2">${EQTAPE}
    <svg class="h4arw lh" data-s="1" width="70" height="200" viewBox="0 0 70 200"><path d="M40 10 C 70 60, 70 140, 30 180" fill="none" stroke="#2c4d75" stroke-width="10" stroke-linecap="round"/><polygon points="12,170 44,166 30,196" fill="#2c4d75"/></svg>
    <div class="h4grid math">
      ${H4A.map(t=>`<span>${t}</span>`).join('')}
      ${H4B.map(([t,s,c])=>`<span class="lh ${c===1?'h4c':c===2?'h4sg':''}" data-s="${s}">${t}</span>`).join('')}
    </div>
    <div class="h4chip lh" data-s="1"><span class="math">× (−1)</span>両辺に −1 を かける</div>
    <div class="h4rev lh" data-s="5">← 向きが 逆！</div>
    <div class="h4end lh" data-s="6"><span class="v2mk">x${P2} の 前が プラス → いつもの 解き方で 解ける</span></div>
  </div>
  ${cbar([`${M('−x² − 6x − 7 ＞ 0')}。　x² の 前が <b>マイナス</b>。　このままだと グラフが 上に 開いた 形に なって 考えにくい。`,
    `x² の 前を プラスに したい。　両辺に <b>−1</b> を かける。`,
    `${M('−x²')} に −1 を かけて ${M('x²')}。`, `${M('−6x')} → ${M('＋6x')}。`, `${M('−7')} → ${M('＋7')}。　符号が 全部 変わる。`,
    `0 は −1 を かけても 0。　そして <b>不等号の 向きが 逆</b>：＞ が ＜ に なる！`,
    `${M('x² ＋ 6x ＋ 7 ＜ 0')}。　x² の 前が プラス に なったので、あとは いつもの 解き方。`])}`;

/* ===== なぜ 向きが 逆に なるか：2 ＞ 1 の 両方に −1 を かける → −2 と −1 → 数直線で −2 が 左 → −2 ＜ −1 ===== */
const NX = x => 380 + x*105;
const WHY4 = `
  <div class="card abs dcard v2">${EQTAPE}
    <div class="w4eq math" style="top:40px">2 ＞ 1</div>
    <div class="w4chip lh" data-s="1"><span class="math">× (−1)</span>両方に −1 を かける</div>
    <div class="w4eq math lh" data-s="1" style="top:210px">−2 <span class="lh" data-s="2" style="color:#e0465e">＜</span> −1</div>
    <svg class="w4nl" width="780" height="320" viewBox="0 0 780 320">
      <line class="iax" x1="40" y1="200" x2="740" y2="200"/><polygon class="iah" points="756,200 738,192 738,208"/>
      ${[-3,-2,-1,0,1,2,3].map(x=>`<line x1="${NX(x)}" y1="190" x2="${NX(x)}" y2="210" stroke="var(--ink)" stroke-width="3"/><text class="w4t" x="${NX(x)}" y="246" text-anchor="middle">${x<0?'−'+(-x):x}</text>`).join('')}
      <circle class="v2pt" cx="${NX(1)}" cy="200" r="11" style="fill:#2f86c8"/><circle class="v2pt" cx="${NX(2)}" cy="200" r="11" style="fill:#2f86c8"/>
      <g class="gs" data-s="1">
        <path d="M${NX(2)} 186 Q ${NX(0)} 40 ${NX(-2)+10} 184" fill="none" stroke="#d9731a" stroke-width="4" stroke-dasharray="8 8"/>
        <path d="M${NX(1)} 186 Q ${NX(0)} 110 ${NX(-1)+8} 184" fill="none" stroke="#d9731a" stroke-width="4" stroke-dasharray="8 8"/>
        <circle cx="${NX(-1)}" cy="200" r="11" fill="#d9731a"/><circle cx="${NX(-2)}" cy="200" r="11" fill="#d9731a"/></g>
      <g class="gs" data-s="2"><path d="M${NX(-1)-14} 280 L${NX(-2)+14} 280" stroke="#e0465e" stroke-width="5"/><polygon points="${NX(-2)},280 ${NX(-2)+18},270 ${NX(-2)+18},290" fill="#e0465e"/>
        <text class="w4lab" x="${NX(-1.5)}" y="312" text-anchor="middle">左 ＝ 小さい</text></g>
    </svg>
    <div class="w4msg lh" data-s="3"><span class="v2mk">マイナスを かけると 大きい・小さいが 入れかわる → 向きが 逆</span></div>
  </div>
  ${cbar([`なぜ 向きが 逆に なるの？　数で 見て みよう。　${M('2 ＞ 1')}。`,
    `両方に −1 を かけると ${M('−2')} と ${M('−1')}。`,
    `数直線では −2 の 方が 左。　左の 方が 小さい → ${M('−2 ＜ −1')}。`,
    `マイナスを かけると、大きい・小さいが 入れかわる。　だから 不等号の 向きが 逆に なる。`])}`;

/* ===== 例⑴ ===== */
const BX4 = (r,c) => `<rect fill="${c}" x="${r[0]}" y="${r[1]}" width="${(r[2]-r[0]).toFixed(1)}" height="${(r[3]-r[1]).toFixed(1)}"/>`;
const L4 = `<div class="p3list"><div class="p3i sm on"><span>⑴</span><span class="math">−x${P2} − 6x − 7 ＞ 0</span></div></div>`;
const E4S = ES1G(['⑴','＜',`x${P2} ＋ 6x ＋ 7`], L4, [['x', FX(`−6 ± ${SQ('36 − 28')}`,'2'), 3],
    ['', FX(`−${RDX('6','3',5)} ± ${RDX('2','1',5)}${SQ('2')}`, RDX('2','1',5,true)), 4],
    ['', HIT(`−3 ± ${SQ('2')}`), 6]], 0, ['−3−√2','−3+√2'], [7,8,9], [
  `⑴ −1 を かけた 式 ${M('x² ＋ 6x ＋ 7 ＜ 0')}。　<b>Step❶</b> まず ＝ 0 の 式を 解く。`,
  `x軸との 共有点 → <b>y ＝ 0</b> と する。`,
  `${M('x² ＋ 6x ＋ 7 ＝ 0')}。　たして 6、かけて 7 に なる 整数は ない → <b>解の公式</b>。`,
  `${M(`x ＝ ${FR('−6 ± √(36 − 28)',2)}`)}`,
  `8 を すだれ算：${M('8 ＝ 2 × 2 × 2')} → ${M('√8 ＝ 2√2')}。`,
  `2 で 約分。`,
  `${M('x ＝ −3 ± √2')}。　これが x軸との 共有点。`,
  `グラフ：x軸に 点を 2つ 打つ。`,
  `下に凸の 放物線を、2つの 点を 通るように かく。`,
  `点の 下に ${M('−3 − √2')}、${M('−3 ＋ √2')} を 書く。　<b>Step❶ 完成！</b>`],
  `<div class="e33sd lh" data-s="4">${SUDARE(8)}</div>`);
const E4P = GQ({no:'⑴', f:`x${P2} ＋ 6x ＋ 7`, s:1, roots:[-3-Math.SQRT2, -3+Math.SQRT2], lab:['−3−√2','−3+√2'], am:true, tag:null, cur:0, listH:L4,
  ans:`−3 − ${SQ('2')} ＜ x ＜ −3 ＋ ${SQ('2')}`, dt:[
  `左：${M('−3 − √2')} と <b>x</b> を 比べる。　x の 方が 大きい。　白丸 なので <b>＜</b>。`, `書き直して ${M('−3 − √2 ＜ x')}。`,
  `右：<b>x</b> と ${M('−3 ＋ √2')} を 比べる。　x の 方が 小さい。　白丸 なので <b>＜</b>。`, `書き直して ${M('x ＜ −3 ＋ √2')}。`,
  `2つを まとめて 答え ${M('−3 − √2 ＜ x ＜ −3 ＋ √2')}。`]});
/* 書きこみ：プリント（No.16）の 配置。−1 の 枠と Step❶ は 書いた 形、塗る(1) → 答え(2) だけ 動かす */
const W4 = (() => { const ay = 343.6, xv = 299.6;
  const gr = PB({xv, ay, top:272, s:0, yv:ay+22, q:22/18**2, lab:[[xv-20,'−3−√2','end'],[xv+20,'−3+√2','start']], paint:'down', ps:1, dot:'o', ds:1});
  return ptSlide({clip:[58,207,534,380],
    svg:[BX4([62.7,231.5,199.9,263.4],'#dce6f2'), BX4([62.7,266.6,240.9,376.4],'#dce6f2'), BX4([245.9,266.6,353.4,376.4],'#dce6f2'), BX4([358.9,345.3,526.6,376.4],'#dbeef4'),
      `<line x1="255" y1="${ay}" x2="342" y2="${ay}" stroke="#555" stroke-width=".8"/><polygon points="344,${ay} 340,${ay-1.6} 340,${ay+1.6}" fill="#555"/><text class="pgt" x="342" y="${ay+8}" font-style="italic">x</text>`,
      `<g class="w33">${gr}</g>`],
    items:[T([61.6,210,330,227],`⑴<span class="xsp"></span>−x${P2} − 6x − 7 ＞ 0`,10.5),
      {s:0, r:[62.7,231.5,199.9,263.4], h:`x${P2} ＋ 6x ＋ 7 ＜ 0`, fs:11, cls:'xan', al:'c'},
      ...[`x${P2} ＋ 6x ＋ 7 ＝ 0`, `x ＝ ${FX(`−6 ± ${SQ('36 − 28')}`,'2')}`, `＝ ${FX(`−6 ± 2${SQ('2')}`,'2')}`, `＝ −3 ± ${SQ('2')}`]
        .map((h,i)=>({s:0, r:[68,271+i*26,240,295+i*26], h, fs:10, al:'l', cls:'xan'})),
      {s:0, r:[196,270,240,338], h:SUDARE(8), fs:6},
      XA(2,[358.9,345.3,526.6,376.4], `−3 − ${SQ('2')} ＜ x ＜ −3 ＋ ${SQ('2')}`, 9.5)],
    done:2, cm:[`プリントに 書こう。　−1 を かけた 式と Step❶ は 書けて いる。`, `下を 塗る。　＝ が ない ので x軸は 塗らない → 白丸。`,
      `答えの 枠に ${M('−3 − √2 ＜ x ＜ −3 ＋ √2')}。　<b>完成！</b>`]}); })();

/* ===== まとめ（動きなし） ===== */
const SUM4 = `
  <div class="end-h"><h2>x${P2} の 前が マイナス の とき</h2></div>
  <div class="dsum p3sum">${SUMC('① −1 を かける','向きを 逆に<br>＞ → ＜<br>≧ → ≦')}${SUMC('② いつもの 解き方','Step❶ 解く<br>Step❷ 塗る<br>Step❸ 答える')}</div>
  ${cbar([`x² の 前が マイナス → まず 両辺に −1 を かけて、不等号の 向きを 逆に する。　あとは いつもの Step❶〜❸。`])}`;

/* ===== プリント問題③-4 ⑴⑵：−1 を かける → 計算の 枠 → グラフ → 塗る → 答え ===== */
const CV = t => `<span class="q34m">× (−1)</span>${t}`;
const PL4 = [['⑴','＞',`−x${P2} ＋ x ＋ 2`], ['⑵','≦',`−x${P2} ＋ 2x ＋ 2`]];
const H34 = '−1 を かけて、＝ 0 を 解く', C34 = '<b>x² の 前が マイナス</b> → まず 両辺に −1 を かける。';
const PROB34 = [
  {name:'問 ⑴', html:GQ({no:'⑴', q0:`−x${P2} ＋ x ＋ 2 ＞ 0`, f:`x${P2} − x − 2`, s:1, roots:[-1,2], ans:'−1 ＜ x ＜ 2', cur:0, tag:'プリント問題③-4',
    list:PL4, pre:PRE33('⑴', `−x${P2} ＋ x ＋ 2`, '＞', [
      [CV(`x${P2} − x − 2 ＜ 0`), `両辺に −1 を かけて、向きを 逆に。　＞ は ＜ に なる。　${M('x² − x − 2 ＜ 0')}`],
      [`x${P2} − x − 2 ＝ 0`, `${M('x² − x − 2 ＝ 0')}。　たして −1、かけて −2 → 因数分解。`],
      ['(x ＋ 1)(x − 2) ＝ 0', M('(x ＋ 1)(x − 2) ＝ 0')], ['x ＝ −1, 2', M('x ＝ −1, 2')]], 'x ＝ −1, 2', GL[0], null, H34, C34)})},
  {name:'問 ⑵', html:GQ({no:'⑵', q0:`−x${P2} ＋ 2x ＋ 2 ≦ 0`, f:`x${P2} − 2x − 2`, s:2, roots:[1-Math.sqrt(3), 1+Math.sqrt(3)], lab:['1−√3','1+√3'], am:true,
    ans:`x ≦ 1 − ${SQ('3')}, 1 ＋ ${SQ('3')} ≦ x`, cur:1, tag:'プリント問題③-4',
    list:PL4, pre:PRE33('⑵', `−x${P2} ＋ 2x ＋ 2`, '≦', [
      [CV(`x${P2} − 2x − 2 ≧ 0`), `両辺に −1 を かけて、向きを 逆に。　≦ は ≧ に なる。　${M('x² − 2x − 2 ≧ 0')}`],
      [`x ＝ ${FX(`2 ± ${SQ('4 ＋ 8')}`,'2')}`, `${M('x² − 2x − 2 ＝ 0')} を 解の公式で。　12 を すだれ算 → ${M('√12 ＝ 2√3')}。`],
      [`x ＝ ${FX(`${RDX('2','1',3)} ± ${RDX('2','1',3)}${SQ('3')}`, RDX('2','1',3,true))} <span class="vm">＝ 1 ± ${SQ('3')}</span>`, `2 で 約分 して ${M('x ＝ 1 ± √3')}。`]],
      `x ＝ 1 ± ${SQ('3')}`, GL[0], [12,2], H34, C34)})}];
const PH34 = probHead('プリント問題③-4', '次の 2次不等式を 解きなさい。', ['⑴ −x² ＋ x ＋ 2 ＞ 0', '⑵ −x² ＋ 2x ＋ 2 ≦ 0'],
  `ここから <b>プリント問題③-4</b>。　まず −1 を かけて、向きを 逆に！`);

const DECK = {title:'③-4 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK34, 'x² の 前が<br><span class="mk">マイナス</span>', '2次不等式の 解き方', '−1 を かけて 向きを 逆に！', POL34, '向きが 逆')},
  {name:'解き方', html:HOW4}, {name:'なぜ 向きが 逆？', html:WHY4},
  {name:'⑴ Step❶', html:E4S}, {name:'⑴ 塗る・答える', html:E4P}, {name:'⑴ 書きこみ', html:W4},
  {name:'まとめ', html:SUM4}, {name:'プリント問題', html:PH34}, ...PROB34,
  {name:'終', html:endF(KK34 + '　2次不等式', POL34)}]};
'''

def add(decks):
    import decks_32, decks_33
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    parts = decks_32.JS.split('const PG = [')
    assert len(parts) == 2
    decks['3-4_2次不等式の解法_v2'] = ('③-4 2次不等式の解法 ver 2', base + parts[0] + decks_33.SHARED33 + JS34)
