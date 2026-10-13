/* ====== 大問５：ことばの穴うめ ====== */
function wordsSlide(){
  const W = ['２次関数','１次関数','双曲線','放物線','原点','軸','頂点','＜','＞','上','下'];
  const A = ['２次関数','放物線','軸','頂点','＞','下'];          // ①〜⑥ の答え
  const NO = ['①','②','③','④','⑤','⑥'];
  const wid = w => 'w'+W.indexOf(w);
  const slot = (i,sm='') => `<span class="wslot${sm}"><span class="num">${NO[i]}</span><span class="tm tm-r on fly" data-f="${i+1}" data-src="${wid(A[i])}">${A[i]}</span></span>`;
  const used = w => { const i=A.indexOf(w); return i<0 ? 99 : i+1; };
  const go = W.map(w=>`<span class="tm tm-w" data-o="${used(w)}" data-k="${wid(w)}">${w}</span>`).join('');
  const sents = `
    <p class="sent">${M('y ＝ x²')} のように、y が x の ２次式で 表されるとき、<br>y は x の ${slot(0)} という。</p>
    <p class="sent">${M('y ＝ ax²')} の グラフの形のような 曲線を ${slot(1)} という。</p>
    <p class="sent">右の図において、Ａを ${slot(2)}、Ｂを ${slot(3)} という。</p>
    <p class="sent">${M('y ＝ ax²')} の グラフは、a ${slot(4,' sm')} 0 なので、<br>${slot(5,' sm')} に凸な グラフである。</p>`;
  const fig = `<svg width="300" height="220" viewBox="0 0 300 220">
    <path d="M 60 18 Q 150 330 240 18" fill="none" stroke="var(--curve)" stroke-width="4" stroke-linecap="round"/>
    <g class="hl" data-o="3"><line x1="150" y1="6" x2="150" y2="214" stroke="var(--o-ink)" stroke-width="2.5" stroke-dasharray="8 6"/>
      <text class="gt" x="162" y="30" style="font-size:24px;font-family:'Zen Maru Gothic';font-weight:900">Ａ</text></g>
    <g class="hl" data-o="4"><circle cx="150" cy="174" r="7" fill="var(--ink)"/>
      <text class="gt" x="164" y="200" style="font-size:24px;font-family:'Zen Maru Gothic';font-weight:900">Ｂ</text></g>
  </svg>`;
  const cm = [
    `５ 次の ①〜⑥ に 当てはまる 言葉を、右下の <b>語群</b> から 選ぼう！`,
    `① ${M('y ＝ x²')} のように y が x の <b>２次式</b> で 表されるとき、y は x の <b>２次関数</b> という。`,
    `② ${M('y ＝ ax²')} の グラフのような 曲線を <b>放物線</b> という。　ボールを 投げたときの 道すじの 形だね。`,
    `③ Ａ は 放物線の まん中を たてに 通る 直線。　放物線は この直線を さかいに 左右が 同じ形。　これを <b>軸</b> という。`,
    `④ Ｂ は 放物線と 軸が 交わる点。　グラフの いちばん下（または上）の点で、<b>頂点</b> という。`,
    `⑤ 図の グラフは 下に凸（∪ の形）。　下に凸になるのは a が プラスのとき。　だから a <b>＞</b> 0。`,
    `⑥ a ＞ 0 なので、<b>下</b> に凸な グラフ。`,
    `<b>完成！</b>　①２次関数　②放物線　③軸　④頂点　⑤＞　⑥下`
  ];
  return `
  <div class="pno">５</div>
  <div class="card abs wcard">${EQTAPE}${sents}</div>
  <div class="card abs zcard">${TP('yellow','right:22px;top:-14px;transform:rotate(4deg)')}<div class="lab">図</div>${fig}</div>
  <div class="card abs gocard">${TP('lav','right:24px;top:-14px;transform:rotate(-5deg)')}<div class="lab">語群</div>${go}</div>
  ${SEAL(7)}
  ${cbar(cm)}`;
}
