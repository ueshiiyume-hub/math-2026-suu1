"""③-4 2次不等式の解法（x² の 前が マイナス）ver 2（2026-11-07、作り直し）。前の 版（3-4_2次不等式の解法.html、プリント画像の 下書き）は 残す。
③-3 ver 2 と 同じ 作り：③-1 の 部品（decks_32.py の 前半）＋ ③-3 の 部品（decks_33.SHARED33）を つなげる。
流れ：表紙 → 解き方（−1 を かけて 向きを 逆に）→ 例⑴（1ページ：−1 → 解く → グラフ → 塗る → 答え）→ まとめ → プリント問題 ⑴⑵（−1 を かける → 計算の 枠 → グラフ → 塗る → 答え）。判別式は 使わない。"""
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
    <svg class="h4arw lh" data-s="1" width="90" height="210" viewBox="0 0 90 210"><defs><marker id="h4mk" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#2c4d75"/></marker></defs><path d="M66 18 C 14 40, 10 150, 58 186" fill="none" stroke="#2c4d75" stroke-width="9" stroke-linecap="round" marker-end="url(#h4mk)"/></svg>
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

/* ===== 例⑴ ===== */
const BX4 = (r,c) => `<rect fill="${c}" x="${r[0]}" y="${r[1]}" width="${(r[2]-r[0]).toFixed(1)}" height="${(r[3]-r[1]).toFixed(1)}"/>`;
const L4 = `<div class="p3list"><div class="p3i sm on"><span>⑴</span><span class="math">−x${P2} − 6x − 7 ＞ 0</span></div></div>`;
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

/* 例⑴：−1 を かけた あとは いつもと 同じ なので 1ページに まとめる（−1 → 解く → グラフ → 塗る → 答え。先生の 指示 11/7） */
const E41 = GQ({no:'⑴', q0:`−x${P2} − 6x − 7 ＞ 0`, f:`x${P2} ＋ 6x ＋ 7`, s:1, roots:[-3-Math.SQRT2, -3+Math.SQRT2], lab:['−3−√2','−3+√2'], am:true,
  ans:`−3 − ${SQ('2')} ＜ x ＜ −3 ＋ ${SQ('2')}`, tag:null, cur:0, listH:L4,
  pre:PRE33('⑴', `−x${P2} − 6x − 7`, '＞', [
    [CV(`x${P2} ＋ 6x ＋ 7 ＜ 0`), `両辺に −1 を かけて、向きを 逆に。　${M('x² ＋ 6x ＋ 7 ＜ 0')}`],
    [`x ＝ ${FX(`−6 ± ${SQ('36 − 28')}`,'2')}`, `${M('x² ＋ 6x ＋ 7 ＝ 0')} を 解の公式で。　8 を すだれ算 → ${M('√8 ＝ 2√2')}。`],
    [`x ＝ ${FX(`−${RDX('6','3',3)} ± ${RDX('2','1',3)}${SQ('2')}`, RDX('2','1',3,true))} <span class="vm">＝ −3 ± ${SQ('2')}</span>`, `2 で 約分 して ${M('x ＝ −3 ± √2')}。`]],
    `x ＝ −3 ± ${SQ('2')}`, GL[0], [8,2], H34, C34)});
const DECK = {title:'③-4 2次不等式の解法', pages:[
  {name:'表紙', html:coverF(KK34, 'x² の 前が<br><span class="mk">マイナス</span>', '2次不等式の 解き方', '−1 を かけて 向きを 逆に！', POL34, '向きが 逆')},
  {name:'解き方', html:HOW4},
  {name:'⑴', html:E41},
  {name:'まとめ', html:SUM4}, {name:'プリント問題', html:PH34}, ...PROB34,
  {name:'終', html:endF(KK34 + '　2次不等式', POL34)}]};
'''

def add(decks):
    import decks_32, decks_33
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    parts = decks_32.JS.split('const PG = [')
    assert len(parts) == 2
    decks['3-4_2次不等式の解法_v2'] = ('③-4 2次不等式の解法 ver 2', base + parts[0] + decks_33.SHARED33 + JS34)
