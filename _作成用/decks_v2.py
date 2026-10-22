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
  <div class="card abs dcard v2 v2cont">${EQTAPE}
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

const DECK = {title:'③-1 2次不等式の解法 ver 2', pages:[
  {name:'表紙', html:coverF(KK2, '<span class="mk">2次不等式</span><br>の 解き方', '塗って 答える', '', POL, '3つの Step')},
  {name:'やること', html:v1}, {name:'⑴ ❶ ＝0 に', html:va}, {name:'⑴ ❶ 解く', html:vb}, {name:'⑴ ❶ プリント', html:s2v}, {name:'⑴ ❷ 上を塗る', html:v3}, {name:'⑴ ❷ x軸上', html:v4},
  {name:'⑴ ❸ 答える', html:v5}, {name:'⑴ 書きこみ', html:s5},
  {name:'終', html:endF(KK2 + '　2次不等式の解法', POL)}
]};
'''

def add(decks):
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    decks['3-1_2次不等式の解法_v2'] = ('③-1 2次不等式の解法 ver 2', base + V2)
