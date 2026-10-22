"""③-1 2次不等式の解法 ver 2.0（作り直し）。ver 1.4（3-1_2次不等式の解法.html）は そのまま 残す。
土台の 部品は v2_base_3-1.js（ver 1.4 の 写し）。この ファイルの 画面は 1画面に 主役 1つ、言葉は 短く。"""
import os
B = os.path.dirname(os.path.abspath(__file__))

V2 = r'''
const KK2 = KIMATSU + '　③-1';
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
const DNCUT = (g, inner) => { const id = 'v2cut' + (++CLN);
  return `<clipPath id="${id}"><rect x="0" y="${(g.ay+2).toFixed(1)}" width="${g.W}" height="${g.H}"/></clipPath><g clip-path="url(#${id})">${inner}</g>`; };
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
    `グラフの うち、塗った 中に 入って いる ところ（−2 と −1 の 間）が 塗れる。`])}`;

/* ❷ x軸上も 塗る（＝ が ある → 黒丸）。−2 に 寄る → ここまで 塗った → 黒丸を かく → 引く */
const h4 = IG({...GV2});
const w4 = `
  <div class="card abs dcard v2 v2cont">${EQTAPE}
    ${NAV(2)}
    <div class="v2c">
      ${BIG('≦ に ＝ が ある','x軸上も 塗る')}
      <div class="v2g v2zw" style="width:${h4.W}px;height:${h4.H}px"><div class="v2zoom" data-wa="1" data-wb="4" style="transform-origin:${h4.X(-2)}px ${h4.ay}px">
        ${h4.svg(`<rect class="v2up show" x="10" y="${h4.ay}" width="${h4.W-20}" height="${h4.H-h4.ay}"/>`, h4.base, PAINTED2(h4),
          `<g class="gs v2zl" data-s="2" data-o="4"><path class="v2zarw" d="M${h4.X(-2)+34} ${h4.ay-12} L${h4.X(-1.97)+6} ${h4.ay+3}"/><text class="v2ztx" x="${h4.X(-2)+36}" y="${h4.ay-10}">x軸の すぐ 下まで 塗れた</text></g>`,
          BD(h4,-2,3,true), `<g class="gs v2zl" data-s="3" data-o="4"><text class="v2ztx" x="${h4.X(-2)-14}" y="${h4.ay-14}" text-anchor="end">黒丸（x軸上も 塗る）</text></g>`,
          BD(h4,-1,4))}
      </div></div>
    </div>
  </div>
  ${cbar([
    `今度は ≦。　＝ が ある ので、y ＝ 0 の x軸上も 答えに 入る。`,
    `−2 の ところに ぐっと 寄って みよう。`,
    `0より 小さい ところは、x軸の すぐ 下まで 塗れて いる。`,
    `＝ が ある ので <b>x軸上も 塗る</b>。　中まで 塗った <b>黒丸</b> を かく。`,
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
  const tx = side==='L' ? mx-230 : mx+230, ty = my+12, ex = side==='L' ? tx+96 : tx-96, ey = ty-12;
  return {band:`<g class="gs" data-s="${s}"><rect class="iband2" x="${f(-len/2)}" y="-30" width="${f(len)}" height="60" rx="30" transform="${tr}"/></g>`,
    rest:`<g class="gs" data-s="${s}"><path class="ilt-h" d="${sign}" transform="${tr}"/><path class="ilt" d="${sign}" transform="${tr}"/></g>
    <g class="gs" data-s="${s+1}"><line class="idot2" x1="${f(mx+(side==='L'?-50:50))}" y1="${f(my)}" x2="${f(ex)}" y2="${f(ey)}"/>
      <text class="iwr" x="${f(tx)}" y="${f(ty)}" text-anchor="middle">${out.replace(/x/g,'<tspan font-style="italic">x</tspan>')}</text></g>`}; };
const h5 = IG({...GV2, sc:270, k:150});
const XP = [h5.X(-1.5), h5.Y(-1.5)+76];      // x の 札（塗れた ところの 下）
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

const DECK = {title:'③-1 2次不等式の解法 ver 2', pages:[
  {name:'表紙', html:coverF(KK2, '<span class="mk">2次不等式</span><br>の 解き方', '塗って 答える', '', POL, '3つの Step')},
  {name:'やること', html:v1}, {name:'⑴ ❶ ＝0 に', html:va}, {name:'⑴ ❶ 解く', html:vb}, {name:'⑴ ❶ プリント', html:s2v}, {name:'⑴ ❷ 上を塗る', html:v3}, {name:'⑴ ❷ x軸上', html:v4}, {name:'⑴ ❷ プリント', html:s5a},
  {name:'⑴ ❸ 答える', html:v5}, {name:'⑴ 書きこみ', html:s5b},
  {name:'⑵ ❶ ＝0 に', html:wa}, {name:'⑵ ❶ 解く', html:wb}, {name:'⑵ ❶ プリント', html:w2v}, {name:'⑵ ❷ 下を塗る', html:w3}, {name:'⑵ ❷ x軸上', html:w4}, {name:'⑵ ❷ プリント', html:w5a},
  {name:'⑵ ❸ 答える', html:w5}, {name:'⑵ 書きこみ', html:w5b},
  {name:'終', html:endF(KK2 + '　2次不等式の解法', POL)}
]};
'''

def add(decks):
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    decks['3-1_2次不等式の解法_v2'] = ('③-1 2次不等式の解法 ver 2', base + V2)
