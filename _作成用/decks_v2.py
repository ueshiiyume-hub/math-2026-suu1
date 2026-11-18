"""③-2 2次不等式の解法 ver 2.0（2026-10-30 の プリントの 並べかえで ③-1 → ③-2。ファイル名・URL は そのまま）（作り直し）。ver 1.4（3-1_2次不等式の解法.html）は そのまま 残す。
土台の 部品は v2_base_3-1.js（ver 1.4 の 写し）。この ファイルの 画面は 1画面に 主役 1つ、言葉は 短く。"""
import os
B = os.path.dirname(os.path.abspath(__file__))

V2 = r'''
const KK2 = KIMATSU + '　③-2';
/* 左の 現在地（❶ 式 ／ ❷ 塗る ／ ❸ 答える） */
const NAV = (on) => `<div class="v2nav">${['❶ 式','❷ 塗る','❸ 答える'].map((t,i)=>`<div class="v2n${i+1===on?' on':''}${i+1<on?' done':''}">${t}</div>`).join('')}</div>`;
/* 小さい 一言 ＋ 大きい 主役（mk：マーカー、sub：かっこ書き） */
const BIG = (sm, big, sub, s, o) => `<div class="v2kw lh" data-s="${s??0}"${o!==undefined?` data-o="${o}"`:''}>
    ${sm?`<div class="v2sm">${sm}</div>`:''}<div class="v2big"><span class="v2mk">${big}</span>${sub?`<span class="v2sub">${sub}</span>`:''}</div></div>`;
/* グラフ（主役の 下） */
const GV = {ay:236, cx:1, sc:40, k:20, r:[-1,3], top:8, W:880, H:320};   // 頂点は x軸の 少し 下、上に 高く   // Step❶ の グラフと 同じ 形（しゅっと）

/* 塗った あとの 形（アニメーション なし）、白丸（s 番で かく、draw＝線を なぞって かく） */
const E = -0.15;   // 塗りは 少し 先まで かいて、x軸の ところで まっすぐ 切る（x軸の ギリギリ まで、x軸は 塗らない）
let CLN = 0;
/* 塗りを x軸の すぐ 上で 切る（ClipPath） */
const UPCUT = (g, inner) => { const id = 'v2cut' + (++CLN);
  return `<clipPath id="${id}"><rect x="0" y="0" width="${g.W}" height="${(g.ay-2).toFixed(1)}"/></clipPath><g clip-path="url(#${id})">${inner}</g>`; };
const PAINTED = (g,a,b) => UPCUT(g, `<g class="ipaint show v2still"><path d="${g.path(g.xa,a)}"/><path d="${g.path(b,g.xb)}"/></g>`);
const WD = (g,x,s,draw) => `<circle class="v2wd${draw?' v2draw':''}${s!==undefined?' gs':''}"${s!==undefined?` data-s="${s}"`:''} cx="${g.X(x).toFixed(1)}" cy="${g.ay}" r="9" pathLength="1"/>`;

/* 1：これから やること */
const v1 = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(0)}
    <div class="v2c">
      ${BIG('これから やること','2次不等式を 解く')}
      <div class="v2eq lh math" data-s="1">${EQ1}</div>
    </div>
  </div>
  ${cbar([`今日 やるのは <b>2次不等式</b> を 解くこと。`, `たとえば ${M('x² − 2x − 3 ＞ 0')}。　3つの ステップで 解いて いこう。`])}`;


/* 2：不等式の「＞ 0」が「＝ 0」に 変わる → 2次方程式を 解く */
const va = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(1)}
    <div class="v2c">
      <div class="v2eqm math">x${P2} − 2x − 3 <span class="v2sw"><span class="v2gt" data-o="1">＞ 0</span><span class="v2eq0" data-o="1">＝ 0</span></span></div>
      ${BIG('まずは','2次方程式を 解く',null,2)}
    </div>
  </div>
  ${cbar([`${M('x² − 2x − 3 ＞ 0')}。　まずは ＞ を ＝ に して…`, `${M('x² − 2x − 3 ＝ 0')}。　これは 2次方程式。`, `まずは <b>2次方程式を 解く</b>。　x軸との 共有点を 求める ため。`])}`;

/* 3：Step❶ の 枠を 大きく（左：計算、右：グラフ）。書く 順：①y＝0とする ②＝0 ③因数分解 ④x＝ ⑤−1, 3 → 点 → 放物線 → 座標 */
const CU = (() => {
  const W=330, H=300, ay=210, X=x=>165+(x-1)*36, Y=x=>ay-14*(x+1)*(x-3);
  let d=''; for(let i=0;i<=60;i++){ const x=1-3.8+7.6*i/60; d+=(i?'L':'M')+X(x).toFixed(1)+' '+Y(x).toFixed(1)+' '; }
  return `<svg class="v2gsv" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
    <line class="iax" x1="10" y1="${ay}" x2="${W-14}" y2="${ay}"/><polygon class="iah" points="${W-2},${ay} ${W-16},${ay-7} ${W-16},${ay+7}"/><text class="ixl" x="${W-22}" y="${ay+32}">x</text>
    <path class="curve v2cv" data-s="7" pathLength="1" d="${d}"/>
    <g class="gs" data-s="6"><circle class="v2pt" cx="${X(-1)}" cy="${ay}" r="9"/><circle class="v2pt" cx="${X(3)}" cy="${ay}" r="9"/></g>
    <g class="gs" data-s="8"><text class="inum" x="${X(-1)-14}" y="${ay+40}" text-anchor="middle">−1</text><text class="inum" x="${X(3)+14}" y="${ay+40}" text-anchor="middle">3</text></g></svg>`; })();
const vb = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(1)}
    <div class="v2c">
      <div class="v2st"><i class="nv">Step</i>❶</div>
      <div class="v2calc math">
        <div class="v2r1"><span>y ＝ x${P2} − 2x − 3</span><span class="v2q lh" data-s="2">＝</span><span class="v2a lh" data-s="2">0</span></div>
        <div class="v2r2"><span class="lh" data-s="3">(x ＋ 1)(x − 3)</span><span class="v2q lh" data-s="3">＝</span><span class="v2a lh" data-s="3">0</span></div>
        <div class="v2r3"><span class="lh" data-s="4">x</span><span class="v2q lh" data-s="4">＝</span><span class="v2a lh" data-s="5"><span class="v2hit">−1, 3</span></span></div>
        <span class="ytag v2yt lh" data-s="1">y ＝ 0 と する</span>
      </div>
      <div class="v2gbox">${CU}</div>
    </div>
  </div>
  ${cbar([
    `<i class="nv">Step</i>❶。　${M('y ＝ x² − 2x − 3')} と おく。`,
    `x軸との 共有点 → <b>y ＝ 0</b> と する。`,
    `式の 右に <b>＝ 0</b>。　2次方程式 ${M('x² − 2x − 3 ＝ 0')} に なる。`,
    `たして −2、かけて −3 → 因数分解。`,
    `x ＝ …`,
    `${M('x ＝ −1, 3')}。　これが グラフと x軸の 共有点。`,
    `グラフ：x軸に 共有点を 2つ 打つ。`,
    `下に凸の 放物線を、2つの 点を 通るように かく。`,
    `点の 下に x座標を 書く。　<i class="nv">Step</i>❶ <b>完成！</b>`])}`;

/* 3：0より 大きい（上を 塗る） */
const g3 = IG({...GV});
const v3 = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(2)}
    <div class="v2c">
      ${BIG(`<span class="math">x${P2} − 2x − 3</span> を <span class="math">y</span> と みる`, '0より 大きい', '（上を 塗る）')}
      <div class="v2g">${g3.svg(`<rect class="v2up gs" data-s="1" x="10" y="2" width="${g3.W-20}" height="${g3.ay-2}"/>`, g3.base, UPCUT(g3, g3.seg(g3.xa,-1-E,2) + g3.seg(3+E,g3.xb,2)))}</div>
    </div>
  </div>
  ${cbar([
    `${M('x² − 2x − 3')} を <b>y</b> と みると、${M('y ＞ 0')}。　0より 大きい → x軸より <b>上</b>。`,
    `x軸より 上を <b>全部</b> 塗る。`,
    `グラフの うち、塗った 中に 入って いる ところが 答えの 部分。`])}`;

/* 4：x軸上は 塗らない。−1 に ググっと 寄って「ギリギリ ここまで」→ 白丸を かく → 引いて 全体 */
const g4 = IG({...GV});
const Z = 3.4;   // 寄る 倍率
const v4 = `
  <div class="card abs dcard v2 v2cont">${EQTAPE}
    ${NAV(2)}
    <div class="v2c">
      ${BIG('＞ に ＝ が ない','x軸上は 塗らない')}
      <div class="v2g v2zw" style="width:${g4.W}px;height:${g4.H}px"><div class="v2zoom" data-wa="1" data-wb="4" style="transform-origin:${g4.X(-1)}px ${g4.ay}px">
        ${g4.svg(`<rect class="v2up show" x="10" y="2" width="${g4.W-20}" height="${g4.ay-2}"/>`, g4.base, PAINTED(g4,-1-E,3+E),
          `<g class="gs v2zl" data-s="2" data-o="4"><path class="v2zarw" d="M${g4.X(-1.03)+30} ${(g4.ay-4)-10} L${g4.X(-1.03)+6} ${(g4.ay-4)-2}"/><polygon class="v2zah" points="${g4.X(-1.03)+5},${(g4.ay-4)-1.6} ${g4.X(-1.03)+10},${(g4.ay-4)-5.5} ${g4.X(-1.03)+11},${(g4.ay-4)-1}"/><text class="v2ztx" x="${g4.X(-1.03)+32}" y="${(g4.ay-4)-8}">ギリギリ ここまで 塗る</text></g>`,
          WD(g4,-1,3,true), `<g class="gs v2zl" data-s="3" data-o="4"><text class="v2ztx" x="${g4.X(-1)+14}" y="${g4.ay+16}">白丸（x軸上は 塗らない）</text></g>`,
          WD(g4,3,4))}
      </div></div>
    </div>
  </div>
  ${cbar([
    `−1 と 3 は ちょうど x軸の 上（y ＝ 0）。　ここは 塗る？`,
    `−1 の ところに ぐっと 寄って みよう。`,
    `0より 大きい ところ だけ 塗る。　y ＝ 0 の x軸上は 塗らない → x軸の <b>ギリギリ 手前</b> まで 塗る。`,
    `x軸上は 塗って いない、と 分かるように 中が 空っぽの <b>白丸</b> を かく。`,
    `引いて 全体を 見る。　3 も 同じ → <b>白丸</b>。`])}`;

/* 5：x を 置く → 斜めに 比べる → 答え */
const g5 = IG({...GV});
const C5L = CMP(g5,'L',-1,-1.3,1,2,'x ＜ −1'), C5R = CMP(g5,'R',3,3.3,1,4,'3 ＜ x');
const v5 = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(3)}
    <div class="v2c">
      ${BIG('塗れた ところの x は？','x を 置く',null,0,6)}
      <div class="v2kw v2ans lh" data-s="6"><div class="v2sm">答え</div><div class="v2big math"><span class="v2mk">x ＜ −1, 3 ＜ x</span></div></div>
      <div class="v2g">${g5.svg(C5L.band, C5R.band, g5.base, PAINTED(g5,-1-E,3+E), WD(g5,-1), WD(g5,3), C5L.rest, C5R.rest)}</div>
    </div>
  </div>
  ${cbar([
    `塗れた ところの x は どんな 数？`,
    `塗れた 2か所に <b>x</b> を 置く。`,
    `左：x は −1 より 小さい。　白丸 なので ＜。`,
    `書き直して ${M('x ＜ −1')}。`,
    `右：x は 3 より 大きい。　白丸 なので ＜。`,
    `書き直して ${M('3 ＜ x')}。`,
    `答え ${M('x ＜ −1, 3 ＜ x')}。　<b>完成！</b>`])}`;

/* プリントの 配置の ページ（Step❶）：アニメーション なしで、書いた あとの 形を 出す */
const STILL = h => h.replace(/data-s="\d+"/g,'data-s="0"').replace(/<div class="abs r done pgdone"[^]*?<\/div><\/div>/,'');
const s2v = STILL(PR({...P1, phase:1, cm:[`プリントでは こう なる。　<i class="nv">Step</i>❶ の 全体。`]}));

/* ❷ が 終わったら、プリントの 配置で 全体を 見せて グラフを 塗る（❸ は まだ） */
const s5a = PR({...P1, phase:2, upto:true, cm:[
  `全体を 見て みよう。　プリントの <i class="nv">Step</i>❷ の グラフ。`,
  `x軸より 上の 部分を、x軸の ギリギリ まで 塗る。`,
  `x軸上は 塗らない → −1、3 は <b>白丸</b>。　<i class="nv">Step</i>❷ <b>完成！</b>`]});

/* 書きこみ：<i class="nv">Step</i>❷ は もう 塗って ある 形で 始め、❸（x を 置く → 比べる → 答え）だけ 動かす */
const AFTER2 = h => h.replace(/class="gs" data-s="[12]"/g,'class="gs show"').replace(/data-s="(\d+)"/g,(m,n)=>`data-s="${Math.max(0,n-2)}"`);
const s5b = AFTER2(PR({...P1, phase:2, cm:[
  `プリントに 書きこもう。　<i class="nv">Step</i>❷ は もう 塗れて いる。`,
  `<i class="nv">Step</i>❸。　塗れた 2か所に <b>x</b> を 置く。`,
  `左：x は −1 より 左 → 小さい。　白丸 なので <b>＜</b>。`,
  `書き直して ${M('x ＜ −1')}。`,
  `右：x は 3 より 右 → 大きい。　白丸 なので <b>＜</b>。`,
  `書き直して ${M('3 ＜ x')}。`,
  `<i class="nv">Step</i>❸ の 枠に ${M('x ＜ −1, 3 ＜ x')}。　<b>完成！</b>`]}));

/* ===================== ⑵ x² ＋ 3x ＋ 2 ≦ 0（⑴ と 同じ 形） ===================== */
const GV2 = {ay:150, cx:-1.5, sc:190, k:240, r:[-2,-1], top:8, W:880, H:316};   // ⑴ と 同じ 見た目の 放物線
/* 塗りを x軸の すぐ 下で 切る */
/* ⑵ は ≦（＝ が ある）ので、塗りは はじめから x軸の 上 ぴったり まで（はみ出さない、足りなく ない） */
const DNCUT = (g, inner) => { const id = 'v2cut' + (++CLN);
  return `<clipPath id="${id}"><rect x="0" y="${g.ay}" width="${g.W}" height="${g.H}"/></clipPath><g clip-path="url(#${id})">${inner}</g>`; };
const PAINTED2 = g => DNCUT(g, `<g class="ipaint show v2still"><path d="${g.path(-2.15,-0.85)}"/></g>`);
const BD = (g,x,s,draw) => `<circle class="v2bd${draw?' v2draw':''}${s!==undefined?' gs':''}"${s!==undefined?` data-s="${s}"`:''} cx="${g.X(x).toFixed(1)}" cy="${g.ay}" r="9" pathLength="1"/>`;

/* ❶ ＝0 に */
const wa = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(1)}
    <div class="v2c">
      <div class="v2eqm math">x${P2} ＋ 3x ＋ 2 <span class="v2sw"><span class="v2gt" data-o="1">≦ 0</span><span class="v2eq0" data-o="1">＝ 0</span></span></div>
      ${BIG('まずは','2次方程式を 解く',null,2)}
    </div>
  </div>
  ${cbar([`⑵ ${M('x² ＋ 3x ＋ 2 ≦ 0')}。　まずは ≦ を ＝ に して…`, `${M('x² ＋ 3x ＋ 2 ＝ 0')}。　これは 2次方程式。`, `まずは <b>2次方程式を 解く</b>。`])}`;

/* ❶ 解く（計算 ＋ グラフ） */
const CU2 = (() => {
  const W=330, H=300, ay=210, X=x=>165+(x+1.5)*144, Y=x=>ay-224*(x+2)*(x+1);
  let d=''; for(let i=0;i<=60;i++){ const x=-1.5-0.95+1.9*i/60; d+=(i?'L':'M')+X(x).toFixed(1)+' '+Y(x).toFixed(1)+' '; }
  return `<svg class="v2gsv" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
    <line class="iax" x1="10" y1="${ay}" x2="${W-14}" y2="${ay}"/><polygon class="iah" points="${W-2},${ay} ${W-16},${ay-7} ${W-16},${ay+7}"/><text class="ixl" x="${W-22}" y="${ay+32}">x</text>
    <path class="curve v2cv" data-s="7" pathLength="1" d="${d}"/>
    <g class="gs" data-s="6"><circle class="v2pt" cx="${X(-2)}" cy="${ay}" r="9"/><circle class="v2pt" cx="${X(-1)}" cy="${ay}" r="9"/></g>
    <g class="gs" data-s="8"><text class="inum" x="${X(-2)-16}" y="${ay+40}" text-anchor="middle">−2</text><text class="inum" x="${X(-1)+16}" y="${ay+40}" text-anchor="middle">−1</text></g></svg>`; })();
const wb = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(1)}
    <div class="v2c">
      <div class="v2st"><i class="nv">Step</i>❶</div>
      <div class="v2calc math">
        <div class="v2r1"><span>y ＝ x${P2} ＋ 3x ＋ 2</span><span class="v2q lh" data-s="2">＝</span><span class="v2a lh" data-s="2">0</span></div>
        <div class="v2r2"><span class="lh" data-s="3">(x ＋ 2)(x ＋ 1)</span><span class="v2q lh" data-s="3">＝</span><span class="v2a lh" data-s="3">0</span></div>
        <div class="v2r3"><span class="lh" data-s="4">x</span><span class="v2q lh" data-s="4">＝</span><span class="v2a lh" data-s="5"><span class="v2hit">−2, −1</span></span></div>
        <span class="ytag v2yt lh" data-s="1">y ＝ 0 と する</span>
      </div>
      <div class="v2gbox">${CU2}</div>
    </div>
  </div>
  ${cbar([
    `<i class="nv">Step</i>❶。　${M('y ＝ x² ＋ 3x ＋ 2')} と おく。`,
    `x軸との 共有点 → <b>y ＝ 0</b> と する。`,
    `式の 右に <b>＝ 0</b>。　2次方程式 ${M('x² ＋ 3x ＋ 2 ＝ 0')} に なる。`,
    `たして ＋3、かけて ＋2 → 因数分解。`,
    `x ＝ …`,
    `${M('x ＝ −2, −1')}。　これが グラフと x軸の 共有点。`,
    `グラフ：x軸に 共有点を 2つ 打つ。`,
    `下に凸の 放物線を、2つの 点を 通るように かく。`,
    `点の 下に x座標を 書く。　<i class="nv">Step</i>❶ <b>完成！</b>`])}`;
const w2v = STILL(PR({...P2_, phase:1, cm:[`プリントでは こう なる。　<i class="nv">Step</i>❶ の 全体。`]}));

/* ❷ 下を 塗る */
const h3 = IG({...GV2});
const w3 = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(2)}
    <div class="v2c">
      ${BIG(`<span class="math">x${P2} ＋ 3x ＋ 2</span> を <span class="math">y</span> と みる`, '0より 小さい', '（下を 塗る）')}
      <div class="v2g">${h3.svg(`<rect class="v2up gs" data-s="1" x="10" y="${h3.ay}" width="${h3.W-20}" height="${h3.H-h3.ay}"/>`, h3.base, DNCUT(h3, h3.seg(-2.15,-0.85,2)))}</div>
    </div>
  </div>
  ${cbar([
    `${M('x² ＋ 3x ＋ 2')} を <b>y</b> と みると、${M('y ≦ 0')}。　まずは 0より 小さい → x軸より <b>下</b>。`,
    `x軸より 下を <b>全部</b> 塗る。`,
    `グラフの うち、塗った 中に 入って いる ところ（−2 と −1 の 間）が 塗れる。　≦ なので x軸の 上まで。`])}`;

/* ❷ x軸上も 塗る（＝ が ある → 黒丸）。−2 に 寄る → ここまで 塗った → 黒丸を かく → 引く */
const h4 = IG({...GV2});
const w4 = `
  <div class="card abs dcard v2 v2cont">${EQTAPE}
    ${NAV(2)}
    <div class="v2c">
      ${BIG('≦ に ＝ が ある','x軸上も 塗る')}
      <div class="v2g v2zw" style="width:${h4.W}px;height:${h4.H}px"><div class="v2zoom" data-wa="1" data-wb="4" style="transform-origin:${h4.X(-2)}px ${h4.ay}px">
        ${h4.svg(`<rect class="v2up show" x="10" y="${h4.ay}" width="${h4.W-20}" height="${h4.H-h4.ay}"/>`, h4.base, PAINTED2(h4),
          `<g class="gs v2zl" data-s="2" data-o="3"><path class="v2zarw" d="M${h4.X(-2)-30} ${h4.ay-14} L${h4.X(-2)-3} ${h4.ay-1}"/><text class="v2ztx" x="${h4.X(-2)-32}" y="${h4.ay-14}" text-anchor="end">ここまで 塗る</text></g>`,
          BD(h4,-2,3,true), `<g class="gs v2zl" data-s="3" data-o="4"><text class="v2ztx" x="${h4.X(-2)-14}" y="${h4.ay-14}" text-anchor="end">黒丸（塗りつぶす）</text></g>`,
          BD(h4,-1,4))}
      </div></div>
    </div>
  </div>
  ${cbar([
    `今度は ≦。　＝ が ある ので、y ＝ 0 の x軸上も 塗る。`,
    `−2 の ところに ぐっと 寄って みよう。`,
    `＝ が ある ので <b>x軸上も 塗る</b>。　塗りは x軸の 上 ぴったり まで 来て いる。`,
    `x軸上も 塗った ことが 分かるように、塗って いる 色で 丸を <b>塗りつぶす</b>。　これが <b>黒丸</b>。`,
    `引いて 全体を 見る。　−1 も 同じ → <b>黒丸</b>。`])}`;
const w5a = PR({...P2_, phase:2, upto:true, cm:[
  `全体を 見て みよう。　プリントの <i class="nv">Step</i>❷ の グラフ。`,
  `x軸より 下の 部分を 塗る。`,
  `x軸上も 塗る → −2、−1 は <b>黒丸</b>。　<i class="nv">Step</i>❷ <b>完成！</b>`]});

/* ❸ 答える：x を 1つ 置き、−2・−1 と 斜めに 比べる → −2 ≦ x ≦ −1 */
/* A（小さい 方）と B（大きい 方）を 斜めに 比べる。side：書き直しを 置く 側 */
const CMPAB = (g, A, B, s, out, side, le) => {
  const f = n => n.toFixed(1), mx=(A[0]+B[0])/2, my=(A[1]+B[1])/2;
  const ang = Math.atan2(B[1]-A[1], B[0]-A[0])*180/Math.PI, len = Math.hypot(B[0]-A[0], B[1]-A[1]) + 76;
  const tr = `translate(${f(mx)} ${f(my)}) rotate(${f(ang)})`;
  const sign = `M16 -16 L-16 0 L16 16${le?' M-16 11 L16 27':''}`;
  const tx = side==='L' ? mx-170 : mx+170, ty = my+12, ex = side==='L' ? tx+92 : tx-92, ey = ty-12;
  return {band:`<g class="gs" data-s="${s}"><rect class="iband2" x="${f(-len/2)}" y="-30" width="${f(len)}" height="60" rx="30" transform="${tr}"/></g>`,
    rest:`<g class="gs" data-s="${s}"><path class="ilt-h" d="${sign}" transform="${tr}"/><path class="ilt" d="${sign}" transform="${tr}"/></g>
    <g class="gs" data-s="${s+1}"><line class="idot2" x1="${f(mx+(side==='L'?-34:34))}" y1="${f(my)}" x2="${f(ex)}" y2="${f(ey)}"/>
      <text class="iwr" x="${f(tx)}" y="${f(ty)}" text-anchor="middle">${out.replace(/x/g,'<tspan font-style="italic">x</tspan>')}</text></g>`}; };
const h5 = IG({...GV2});   // ほかの ページと 同じ 形
const XP = [h5.X(-1.5), h5.Y(-1.5)+72];      // x の 札（塗れた ところの 下）
const XC = [h5.X(-1.5), h5.Y(-1.5)+8];
const NL = [h5.X(-2), h5.ay+34], NR = [h5.X(-1), h5.ay+34];   // −2・−1 の 数
const D5L = CMPAB(h5, NL, XP, 2, '−2 ≦ x', 'L', true), D5R = CMPAB(h5, XP, NR, 4, 'x ≦ −1', 'R', true);
const w5 = `
  <div class="card abs dcard v2">${EQTAPE}
    ${NAV(3)}
    <div class="v2c">
      ${BIG('塗れた ところの x は？','x を 置く',null,0,6)}
      <div class="v2kw v2ans lh" data-s="6"><div class="v2sm">答え</div><div class="v2big math"><span class="v2mk">−2 ≦ x ≦ −1</span></div></div>
      <div class="v2g">${h5.svg(D5L.band, D5R.band, `<rect class="v2up show" x="10" y="${h5.ay}" width="0" height="0"/>`, h5.base, PAINTED2(h5), BD(h5,-2), BD(h5,-1),
        `<g class="gs" data-s="1"><line class="ixln" x1="${XP[0]}" y1="${XP[1]-24}" x2="${XC[0]}" y2="${XC[1]+4}"/><circle class="ixdot" cx="${XC[0]}" cy="${XC[1]}" r="6"/><circle class="ixb" cx="${XP[0]}" cy="${XP[1]}" r="24"/><text class="ixt" x="${XP[0]}" y="${XP[1]+10}" text-anchor="middle">x</text></g>`,
        D5L.rest, D5R.rest)}</div>
    </div>
  </div>
  ${cbar([
    `塗れた ところの x は どんな 数？`,
    `塗れた ところに <b>x</b> を 置く。`,
    `x は −2 より 右 → 大きい。　黒丸 なので ＝ も つけて <b>≦</b>。`,
    `書き直して ${M('−2 ≦ x')}。`,
    `x は −1 より 左 → 小さい。　黒丸 なので <b>≦</b>。`,
    `書き直して ${M('x ≦ −1')}。`,
    `2つを まとめて 答え ${M('−2 ≦ x ≦ −1')}。　<b>完成！</b>`])}`;
const w5b = AFTER2(PR({...P2_, phase:2, cm:[
  `プリントに 書きこもう。　<i class="nv">Step</i>❷ は もう 塗れて いる。`,
  `<i class="nv">Step</i>❸。　塗れた ところに <b>x</b> を 置く。`,
  `x は −2 より 右 → 大きい。　黒丸 なので <b>≦</b>。`,
  `書き直して ${M('−2 ≦ x')}。`,
  `x は −1 より 左 → 小さい。　黒丸 なので <b>≦</b>。`,
  `書き直して ${M('x ≦ −1')}。`,
  `2つを まとめて、<i class="nv">Step</i>❸ の 枠に ${M('−2 ≦ x ≦ −1')}。　<b>完成！</b>`]}));

/* ===== 基本の 解説：⑴ ⑵ を それぞれ 1枚（プリントの 配置に 書きこむ。先生の 指示 11/18） =====
   下の 説明（いま やっていること）は なし → カードを 大きく。計算・グラフは 1行ずつ。
   いま 書いて いる Step を ズーム → 終わったら 全体 → 次の Step を ズーム（入れ子の .zw が data-wa〜data-wb の 間だけ 拡大）
   番：1 y＝… 2 y＝0 と する・＝0 3 因数分解 4 x＝ 5 点 6 放物線 7 x座標 ／ 8 全体 ／ 9 塗る 10 白丸・黒丸 ／ 11 全体 ／
       12 x を 置く 13 左を 比べる 14 書き直す 15 右を 比べる 16 書き直す 17 答え ／ 18 全体（完成） */
function PRF(o){
  const dy = o.dy, Yd = y => y+dy, R = r => [r[0],r[1]+dy,r[2],r[3]+dy];
  const pv = o.pv, top = Yd(440), ay = Yd(492);
  const hw = Math.sqrt((pv.yv+dy-top)/pv.q); let d='';
  const rr = Math.sqrt((pv.yv+dy-ay)/pv.q), r1 = pv.xv-rr, r2 = pv.xv+rr, Yc = x => (pv.yv+dy)-pv.q*(x-pv.xv)**2;
  for(let i=0;i<=50;i++){ const x=pv.xv-hw+2*hw*i/50; d+=(i?'L':'M')+x.toFixed(2)+' '+((pv.yv+dy)-pv.q*(x-pv.xv)**2).toFixed(2)+' '; }
  const L = (s,r,h,fs=11) => XA(s,R(r),h,fs,'xan xl');
  const B = n => n + 9;                       // Step❸ の 番（PR の phase 2 の 3〜8 → 12〜17）
  const items = [
    T(R([62.3,281.5,200,297.5]),`${o.no}<span class="xsp"></span>${o.eq}`,11),
    T(R([73.5,304.5,119,323]),'<span class="ja"><i class="nv">Step</i>❶</span>',10.5,'ac'), T(R([73.5,428.9,119,447.4]),'<span class="ja"><i class="nv">Step</i>❷</span>',10.5,'ac'), T(R([286.7,428.9,332.3,447.4]),'<span class="ja"><i class="nv">Step</i>❸</span>',10.5,'ac'),
    T([r1-14,ay+1.5,r1+6,ay+12.5],`<span style="font-size:.8em">${o.lab[0]}</span>`,8.5,'ac'), T([r2-6,ay+1.5,r2+14,ay+12.5],`<span style="font-size:.8em">${o.lab[1]}</span>`,8.5,'ac'),
    L(1,[148,309,326,331],o.c[0]), {s:2, r:R([262,310,326,330]), h:`<span class="ytag">y ＝ 0 と する</span>`, fs:7.8, cls:'xyt'},
    L(2,[148,335,326,357],o.c[1]), L(3,[148,361,326,383],o.c[2]), L(4,[148,387,326,409],o.c[3]),
    XA(B(8),R([323.2,467.2,507.3,498.3]),o.ans,13),
    ...o.rw.map((h,i)=>({s:B(5+2*i), r:[333+i*86,Yd(449),411+i*86,Yd(463)], h:h, fs:11, cls:'xan xwr', al:'c'}))];
  const svg = [
    `<rect class="xpb" x="73.5" y="${Yd(304.5)}" width="45.5" height="18.5"/><rect class="xpb" x="73.5" y="${Yd(428.9)}" width="45.5" height="18.5"/><rect class="xpb" x="286.7" y="${Yd(428.9)}" width="45.6" height="18.5"/>`,
    `<rect class="xpb" x="142.8" y="${Yd(305.4)}" width="184" height="109.8"/><rect class="xpb" x="354.2" y="${Yd(305.4)}" width="137.2" height="109.8"/><rect class="xpr" x="323.2" y="${Yd(467.2)}" width="184.1" height="31.1"/>`,
    `<line x1="373.5" y1="${Yd(384.5)}" x2="467" y2="${Yd(384.5)}" stroke="#555" stroke-width=".7"/><polygon points="469,${Yd(384.5)} 465.5,${Yd(383)} 465.5,${Yd(386)}" fill="#555"/><text class="pgt" x="465" y="${Yd(392)}" font-style="italic">x</text>`,
    `<line x1="140" y1="${ay}" x2="268" y2="${ay}" stroke="#333" stroke-width=".8"/><polygon points="271,${ay} 266.5,${ay-1.8} 266.5,${ay+1.8}" fill="#333"/><text class="pgt" x="265" y="${ay+11}" font-style="italic" style="font-size:9px">x</text>`,
    `<path d="${d}" fill="none" stroke="#111" stroke-width="1.6"/>`,
    PB({xv:o.gx, yv:Yd(404.5), q:0.05, ay:Yd(384.5), top:Yd(312), s:6, dot:'f', ds:5, ls:7, lab:[[o.gx-20,o.lab[0]],[o.gx+20,o.lab[1]]]}),
    PB({xv:pv.xv, yv:pv.yv+dy, q:pv.q, ay, top, draw:false, paint:o.paint, ps:9, dot:o.dot, ds:10})];
  /* Step❸：x を 置く → 数と 斜めに 比べる（うすい 帯 ＋ 不等号）→ 書き直す（PR と 同じ） */
  const f = n => n.toFixed(1);
  const P = o.out ? {L:[r1,ay+2], R:[r2,ay+2]} : {L:[r1-4,ay+9], R:[r2+4,ay+9]};
  const X = o.out ? [{at:[r1-22,ay-11], to:[r1-7,Yc(r1-7)]}, {at:[r2+22,ay-11], to:[r2+7,Yc(r2+7)]}]
                  : [{at:[pv.xv,ay+36], to:[pv.xv,Yc(pv.xv)+1.5]}];
  const pairs = o.out ? [[X[0].at,P.L,B(4)],[P.R,X[1].at,B(6)]] : [[P.L,X[0].at,B(4)],[X[0].at,P.R,B(6)]];
  const le = o.dot==='f';
  pairs.forEach(([A,Bp,st])=>{
    const mx=(A[0]+Bp[0])/2, my=(A[1]+Bp[1])/2, ang=Math.atan2(Bp[1]-A[1],Bp[0]-A[0])*180/Math.PI, len=Math.hypot(Bp[0]-A[0],Bp[1]-A[1])+16;
    const tr = `translate(${f(mx)} ${f(my)}) rotate(${f(ang)})`;
    svg.splice(4,0,`<g class="gs" data-s="${st}"><rect class="iband2" x="${f(-len/2)}" y="-7" width="${f(len)}" height="14" rx="7" transform="${tr}"/></g>`);
    svg.push(`<g class="gs" data-s="${st}"><path class="ilt pt" d="M3.5 -3.5 L-3.5 0 L3.5 3.5${le?' M-3.5 2.6 L3.5 6.1':''}" transform="${tr}"/></g>`);
  });
  svg.push(`<g class="gs" data-s="${B(3)}">${X.map(x=>`<line class="ixln pt" x1="${f(x.at[0])}" y1="${f(x.at[1])}" x2="${f(x.to[0])}" y2="${f(x.to[1])}"/><circle class="ixdot" cx="${f(x.to[0])}" cy="${f(x.to[1])}" r="1.4"/><circle class="ixb" cx="${f(x.at[0])}" cy="${f(x.at[1])}" r="5.2"/><text class="ixt pt" x="${f(x.at[0])}" y="${f(x.at[1]+2.4)}" text-anchor="middle">x</text>`).join('')}</g>`);
  /* ズームする ところ（PDF の pt）：[番の はじめ, 終わりの 次, x1, y1, x2, y2] */
  const yb = (o.out?528:546)+dy;
  const Z = [[1,5, 66,300+dy,332,418+dy], [5,8, 342,300+dy,498,418+dy], [9,11, 66,424+dy,286,yb], [12,18, 112,424+dy,512,yb]];   // ❶ 計算 → ❶ グラフ → ❷ → ❸
  return ptBig({clip:[60,278+dy,535,yb], svg, items, done:18, Z});
}
/* ptSlide と 同じ 配置で、下の 説明 なし・カードを 大きく、ズーム つき */
function ptBig(P){
  const AW = 1184, AH = 640;
  const [cx1,cy1,cx2,cy2] = P.clip, w = cx2-cx1, h = cy2-cy1;
  const s = Math.min(1150/w, (AH-20)/h, 2.8);
  const W = w*s, H = h*s, L = (AW-W)/2, T = (AH-H)/2;
  const X = x => (L+(x-cx1)*s), Y = y => (T+(y-cy1)*s);
  const R = r => `left:${X(r[0]).toFixed(1)}px;top:${Y(r[1]).toFixed(1)}px;width:${((r[2]-r[0])*s).toFixed(1)}px;height:${((r[3]-r[1])*s).toFixed(1)}px`;
  const it = P.items.map(o => `<div class="pte ${o.cls||''} ${o.al==='c'?'ac':''}${o.s!==undefined?' lh':''}"${o.s!==undefined?` data-s="${o.s}"`:''} style="${R(o.r)};font-size:${((o.fs||10.5)*s).toFixed(1)}px"><span class="kwr">${o.h}</span></div>`).join('');
  /* ズームは 入れ子の .zw（ズームする ところの 数だけ）（それぞれ data-wa〜data-wb の 間だけ wv-on → transform:var(--zt)）。:has() は 使わない（古い 端末・一部の ブラウザで 効かない） */
  const zt = ([a,b,x1,y1,x2,y2]) => { const a1=X(x1), b1=Y(y1), a2=X(x2), b2=Y(y2);
    const k = Math.min(AW/(a2-a1), AH/(b2-b1)) * .95, tx = AW/2 - k*(a1+a2)/2, ty = AH/2 - k*(b1+b2)/2;
    return `translate(${tx.toFixed(1)}px,${ty.toFixed(1)}px) scale(${k.toFixed(3)})`; };
  const open = P.Z.map(z=>`<div class="zw" data-wa="${z[0]}" data-wb="${z[1]}" style="--zt:${zt(z)}">`).join('');
  return `
  <div class="card abs ptcard ptbig">
    ${open}
      <svg class="pgsv" style="left:${L.toFixed(1)}px;top:${T.toFixed(1)}px" width="${W.toFixed(1)}" height="${H.toFixed(1)}" viewBox="${cx1} ${cy1} ${w} ${h}">${P.svg.join('')}</svg>
      ${it}
    ${P.Z.map(()=>'</div>').join('')}
  </div>
  <div class="abs r done pgdone" data-s="${P.done}"><div class="seal">完成！</div></div>`;
}
const F1 = PRF(P1), F2 = PRF(P2_);
/* くわしい 解説の 見出し */
const DH = `
  <div class="card abs ncard phcard">${EQTAPE}
    <div class="ph-k">もっと くわしく</div>
    <div class="ph-h">くわしい 解説</div>
    <div class="ph-t">⑴ ⑵ を、1つずつ ゆっくり 見て いこう。</div>
    <div class="ph-l math"><span>⑴ ${EQ1}</span><span>⑵ ${EQ2}</span></div>
  </div>
  ${cbar(['ここからは <b>くわしい 解説</b>。　グラフを 塗る ところ・答え方を、1つずつ 見て いこう。'])}`;

const DECK = {title:'③-2 2次不等式の解法', groups:{'⑴':`⑴ ${EQ1}`, '⑵':`⑵ ${EQ2}`}, pages:[
  {name:'表紙', html:coverF(KK2, '<span class="mk">2次不等式</span><br>の 解き方', '塗って 答える', '', POL, '3つの Step')},
  {name:'解き方', html:s1},   // 解き方（3つの Step）を 最初に（先生の 指示 11/18。前は 最後の「手順の まとめ」）
  {name:'⑴', html:F1}, {name:'⑵', html:F2},   // 基本の 解説：1枚ずつ（11/18）
  {name:'くわしい 解説', html:DH},           // ここから 前の アニメーションの 解説（くわしい 版。書きこみの ページは ⑴ ⑵ と 同じ なので 外した）
  {name:'やること', html:v1}, {name:'⑴ ❶ ＝0 に', html:va}, {name:'⑴ ❶ 解く', html:vb}, {name:'⑴ ❶ プリント', html:s2v}, {name:'⑴ ❷ 上を塗る', html:v3}, {name:'⑴ ❷ x軸上', html:v4}, {name:'⑴ ❷ プリント', html:s5a},
  {name:'⑴ ❸ 答える', html:v5},
  {name:'⑵ ❶ ＝0 に', html:wa}, {name:'⑵ ❶ 解く', html:wb}, {name:'⑵ ❶ プリント', html:w2v}, {name:'⑵ ❷ 下を塗る', html:w3}, {name:'⑵ ❷ x軸上', html:w4}, {name:'⑵ ❷ プリント', html:w5a},
  {name:'⑵ ❸ 答える', html:w5},
  {name:'終', html:endF(KK2 + '　2次不等式の解法', POL)}
]};
'''

def add(decks):
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    decks['3-1_2次不等式の解法_v2'] = ('③-2 2次不等式の解法 ver 2', base + V2)
