"""③-2 2次不等式の解法〜練習編 ver 2（テンポよく「塗る → 答える」を くり返す）。
前の 版（3-2_2次不等式_練習編.html、プリント画像の 下書き）は ファイルだけ 残す。
1問 1ページ：式 → ❶ 塗る（上／下）→ ❷ x軸上（白丸／黒丸）→ ❸ 答え。段の 終わりに プリントの 配置で 答えを 書きこむ。"""
import os
B = os.path.dirname(os.path.abspath(__file__))

JS = r'''
const KK3 = KIMATSU + '　③-2';
const POL3 = `<div class="fpol"><div class="fa math">x${P2} − 2x ＋ 5 ＞ 0</div><div class="fv">塗って 答える</div><div class="fb" style="font-size:24px;font-weight:900">すべての実数</div></div>`;
const f1 = n => n.toFixed(1);

/* グラフ（px）：y ＝ k(x − xv)² ＋ c を 下に凸で。sc：1目もりの px、ay：x軸 */
function SG(o){
  const W = o.W||800, H = o.H||300, ay = o.ay;
  const vs = o.vs||o.sc, X = x => W/2 + (x-o.xv)*o.sc, Y = x => ay - (o.k*(x-o.xv)**2 + o.c)*vs;
  const hw = Math.sqrt(((ay-o.top)/vs - o.c)/o.k);
  let d=''; for(let i=0;i<=80;i++){ const x=o.xv-hw+2*hw*i/80; d+=(i?'L':'M')+f1(X(x))+' '+f1(Y(x))+' '; }
  return {X,Y,ay,W,H,d};
}
let CL3 = 0;
/* 塗る：up（上）／ dn（下）、eq（x軸上も）。塗りは グラフを 塗る 範囲で 切る */
const PAINT3 = (g, up, eq, s, cls='') => { const id='c3_'+(++CL3);
  const r = up ? `<rect x="0" y="0" width="${g.W}" height="${f1(eq? g.ay : g.ay-2)}"/>` : `<rect x="0" y="${f1(eq? g.ay : g.ay+2)}" width="${g.W}" height="${g.H}"/>`;
  return `<clipPath id="${id}">${r}</clipPath><g clip-path="url(#${id})"><g class="ipaint ${s===undefined?'show v2still':''} ${cls}"${s!==undefined?` data-s="${s}"`:''}><path pathLength="1" d="${g.d}"/></g></g>`; };
const TINT3 = (g, up, s) => `<rect class="v2up gs" data-s="${s}" x="10" y="${up?2:g.ay}" width="${g.W-20}" height="${up?g.ay-2:g.H-g.ay}"/>`;
const AX3 = g => `<line class="iax" x1="10" y1="${g.ay}" x2="${g.W-16}" y2="${g.ay}"/><polygon class="iah" points="${g.W-2},${g.ay} ${g.W-20},${g.ay-9} ${g.W-20},${g.ay+9}"/><text class="ixl" x="${g.W-24}" y="${g.ay+38}">x</text>`;
const NUM3 = (g, xs) => xs.map(x=>`<text class="inum" x="${f1(g.X(x)+(xs.length>1?(x<1?-20:20):0))}" y="${g.ay+42}" text-anchor="middle">${x<0?'−'+(-x):x}</text>`).join('');
const DOT3 = (g, x, filled, s) => `<circle class="${filled?'v2bd':'v2wd'} gs" data-s="${s}" cx="${f1(g.X(x))}" cy="${g.ay}" r="10"/>`;

/* 段ごとの グラフ */
const ROW3 = [
  {f:`x${P2} − 2x − 3`, o:{xv:1, k:1, c:-4, sc:40, vs:20, ay:170, top:10, H:316}, roots:[-1,3]},
  {f:`x${P2} − 2x ＋ 1`, o:{xv:1, k:1, c:0, sc:40, vs:20, ay:250, top:10}, roots:[1]},
  {f:`x${P2} − 2x ＋ 5`, o:{xv:1, k:1, c:2, sc:40, vs:20, ay:272, top:10}, roots:[]}];
/* 12問：段、不等号、答え、言葉 */
const SIGN3 = ['＞','＜','≧','≦'];
const ANS3 = [
  ['x ＜ −1, 3 ＜ x', '−1 ＜ x ＜ 3', 'x ≦ −1, 3 ≦ x', '−1 ≦ x ≦ 3'],
  ['1以外の すべての実数', '解なし', 'すべての実数', 'x ＝ 1'],
  ['すべての実数', '解なし', 'すべての実数', '解なし']];
const WHY = [
  ['外側 2か所が 塗れた', '内側が 塗れた', '外側 ＋ x軸上', '内側 ＋ x軸上'],
  ['1 だけ 塗れない', '塗れる ところが ない', '全部 塗れた', '1 の 点 だけ 塗れた'],
  ['全部 塗れた', '塗れる ところが ない', '全部 塗れた', '塗れる ところが ない']];
const NO3 = '⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿';
const MATHY = a => /^[x−\d ＜＝≦,]+$/.test(a.replace(/\s/g,''));

/* 左：この 段の 4問（今の 問題を 目立たせる） */
const LIST3 = (r, j, j2=j) => `<div class="p3list">${SIGN3.map((sg,k)=>`<div class="p3i${k>=j&&k<=j2?' on':''}${k<j?' done':''}"><span>${NO3[r*4+k]}</span><span class="math">${sg} 0</span></div>`).join('')}</div>`;


/* x の 札（塗れた ところと 点線で つなぐ） */
const XB3 = (at, to) => `<line class="ixln" x1="${f1(at[0])}" y1="${f1(at[1])}" x2="${f1(to[0])}" y2="${f1(to[1])}"/><circle class="ixdot" cx="${f1(to[0])}" cy="${f1(to[1])}" r="6"/><circle class="ixb" cx="${f1(at[0])}" cy="${f1(at[1])}" r="22"/><text class="ixt" x="${f1(at[0])}" y="${f1(at[1]+10)}" text-anchor="middle">x</text>`;
/* A（小さい 方）と B（大きい 方）を 斜めに 比べる：帯（後ろ）と 不等号（前）。le＝≦ */
const CMP3 = (A, B, le) => { const mx=(A[0]+B[0])/2, my=(A[1]+B[1])/2, ang=Math.atan2(B[1]-A[1],B[0]-A[0])*180/Math.PI, len=Math.hypot(B[0]-A[0],B[1]-A[1])+64;
  const tr=`translate(${f1(mx)} ${f1(my)}) rotate(${f1(ang)})`, d=`M13 -13 L-13 0 L13 13${le?' M-13 9 L13 22':''}`;
  return {band:`<rect class="iband2" x="${f1(-len/2)}" y="-26" width="${f1(len)}" height="52" rx="26" transform="${tr}"/>`,
          sign:`<path class="ilt-h" d="${d}" transform="${tr}"/><path class="ilt" d="${d}" transform="${tr}"/>`}; };
const WR3 = (x, y, t) => `<text class="iwr p3wr" x="${f1(x)}" y="${f1(y)}" text-anchor="middle">${t.replace(/x/g,'<tspan font-style="italic">x</tspan>')}</text>`;
/* 1問の「x を 置く（3番）→ 式を 書く（4番）」 */
function XSTEP(r, j, g){
  const up = j%2===0, le = j>=2, sg = le?'≦':'＜';
  const NL = x => [g.X(x)+(x<1?-20:20), g.ay+32];      // 数（−1・3）の 文字の 位置
  let back='', x3='', w4='';
  if(r===0 && up){            // 外側 2か所
    const L=[g.X(-1)-110, g.ay-48], R=[g.X(3)+110, g.ay-48];
    const c1=CMP3(L, NL(-1), le), c2=CMP3(NL(3), R, le);
    back = `<g class="gs" data-s="6">${c1.band}${c2.band}</g>`;
    x3 = XB3(L,[g.X(-1.4),g.Y(-1.4)]) + XB3(R,[g.X(3.4),g.Y(3.4)]);
    w4 = c1.sign + c2.sign + WR3(g.X(-1)-200, g.ay+80, `x ${sg} −1`) + WR3(g.X(3)+200, g.ay+80, `3 ${sg} x`);
  } else if(r===0){           // 内側
    const X=[g.X(1), g.Y(1)+42], c1=CMP3(NL(-1), X, le), c2=CMP3(X, NL(3), le);
    back = `<g class="gs" data-s="6">${c1.band}${c2.band}</g>`;
    x3 = XB3(X,[g.X(1),g.Y(1)]);
    w4 = c1.sign + c2.sign + WR3(g.X(-1)-170, g.ay+90, `−1 ${sg} x`) + WR3(g.X(3)+170, g.ay+90, `x ${sg} 3`);
  } else if(r===1 && j===0){  // 1 以外
    const L=[g.X(1)-150, g.ay-80], R=[g.X(1)+150, g.ay-80], N=[g.X(1), g.ay+34];
    const c1=CMP3(L, N, false), c2=CMP3(N, R, false);
    back = `<g class="gs" data-s="6">${c1.band}${c2.band}</g>`;
    x3 = XB3(L,[g.X(-0.5),g.Y(-0.5)]) + XB3(R,[g.X(2.5),g.Y(2.5)]);
    w4 = c1.sign + c2.sign + WR3(g.X(1)-250, g.ay+20, 'x ＜ 1') + WR3(g.X(1)+250, g.ay+20, '1 ＜ x');
  } else if(r===1 && j===3){  // 1点 だけ
    const A=[g.X(1)+110, g.ay-60];
    x3 = XB3(A,[g.X(1),g.ay]);
    w4 = WR3(g.X(1)+220, g.ay-50, 'x ＝ 1');
  } else if(up){              // 全部 塗れた
    const A=[g.X(2.4)+100, g.Y(2.4)];
    x3 = XB3(A,[g.X(2.4),g.Y(2.4)]);
    w4 = `<text class="iwr p3wr" x="${f1(g.X(2.4)+140)}" y="${f1(g.Y(2.4)+10)}">どこでも OK</text>`;
  } else {                    // 塗れた ところが ない
    x3 = `<text class="iwr p3wr" x="${f1(g.X(3.2))}" y="${f1(g.ay-120)}" style="fill:var(--muted)">x を 置く ところが ない</text>`;
  }
  return {back, front:`<g class="gs" data-s="5">${x3}</g><g class="gs" data-s="6">${w4}</g>`};
}
function Q3(r, j){
  const R = ROW3[r], up = j%2===0, eq = j>=2, sg = SIGN3[j], g = SG({...R.o}), ans = ANS3[r][j];
  const any = !(r===1 && !up) && !(r===2 && !up);
  const dots = R.roots.map(x=>DOT3(g, x, eq, 4)).join('');
  const w2 = R.roots.length ? (eq ? 'x軸上も 塗る' : 'x軸上は 塗らない') : 'x軸上に グラフは ない';
  const am = MATHY(ans), xs = XSTEP(r, j, g);
  /* 番：1 ${sg} 0 を 強調、2 0より 大きい／小さい、3 上／下を 塗る、4 x軸上、5 x を 置く、6 式・答え */
  return `
  <div class="card abs dcard v2 p3">${EQTAPE}
    ${LIST3(r,j)}
    <div class="v2c">
      <div class="p3q math">${NO3[r*4+j]}　${R.f} <span class="p3sg" data-o="1">${sg} 0</span></div>
      <div class="p3w lh" data-s="2" data-o="4"><span class="v2mk">${up?'0より 大きい':'0より 小さい'}</span><span class="v2sub lh" data-s="3">（${up?'上':'下'}を 塗る）</span></div>
      <div class="p3w lh" data-s="4" data-o="5"><span class="v2mk">${w2}</span></div>
      <div class="p3w lh" data-s="5" data-o="6"><span class="v2mk">${any?'塗れた ところに x を 置く':'塗れた ところは？'}</span></div>
      <div class="p3w p3a lh" data-s="6"><span class="p3why">${WHY[r][j]} →</span><span class="v2mk ${am?'math':''}">${ans}</span></div>
      <div class="p3g"><svg class="isv" width="${g.W}" height="${g.H}" viewBox="0 0 ${g.W} ${g.H}">
        ${TINT3(g, up, 3)}${xs.back}${AX3(g)}${NUM3(g, R.roots)}<path class="icv" d="${g.d}"/>
        ${any ? PAINT3(g, up, false, 3) : ''}${eq && R.roots.length ? `<g class="gs" data-s="4">${PAINT3(g, up, true)}</g>` : ''}${dots}${xs.front}</svg></div>
    </div>
  </div>
  ${cbar([
    `${NO3[r*4+j]} ${M(`${R.f.replace(/<sup>2<\/sup>/,'²')} ${sg} 0`)}`,
    `右側の「${sg} 0」に 注目。`,
    `${up?'0より 大きい':'0より 小さい'}。`,
    `${up?'0より 大きい → x軸より <b>上</b> を 塗る。':'0より 小さい → x軸より <b>下</b> を 塗る。'}${any?'':'　…でも グラフは x軸より 下に ない！'}`,
    R.roots.length ? (eq ? `＝ が ある → x軸上も 塗る → <b>黒丸</b>。` : `＝ が ない → x軸上は 塗らない → <b>白丸</b>。`) : `x軸と 交わらない ので、x軸上の 点は ない。`,
    any ? `塗れた ところに <b>x</b> を 置く。` : `塗れた ところが ない ので、x を 置けない。`,
    `${WHY[r][j]} → 答え <b>${ans}</b>。`])}`;
}


/* 2問 1ページ（左右に 並べて、塗る → x軸上 → 答え を 同時に） */
function HALF3(r, j){
  const R = ROW3[r], up = j%2===0, eq = j>=2, sg = SIGN3[j], ans = ANS3[r][j];
  const o = {...R.o, sc:R.o.sc*0.7, vs:R.o.vs*0.7, W:440, H:250, ay:Math.round(R.o.ay*0.86), top:8};
  const g = SG(o), dots = R.roots.map(x=>DOT3(g, x, eq, 2)).join(''), am = MATHY(ans);
  const w1 = `${up?'0より 大きい':'0より 小さい'}<span class="p3s2">（${up?'上':'下'}を 塗る）</span>`;
  const w2 = R.roots.length ? (eq ? 'x軸上も 塗る' : 'x軸上は 塗らない') : 'x軸上に グラフは ない';
  return `<div class="p3h">
      <div class="p3hq math">${NO3[r*4+j]}　${R.f} ${sg} 0</div>
      <div class="p3hw">
        <div class="p3w2 lh" data-s="1" data-o="2"><span class="v2mk">${w1}</span></div>
        <div class="p3w2 lh" data-s="2" data-o="3"><span class="v2mk">${w2}</span></div>
        <div class="p3w2 p3a2 lh" data-s="3"><span class="p3why">${WHY[r][j]}</span><span class="v2mk ${am?'math':''}">${ans}</span></div>
      </div>
      <svg class="isv" width="${g.W}" height="${g.H}" viewBox="0 0 ${g.W} ${g.H}">
        ${TINT3(g, up, 1)}${AX3(g)}${NUM3(g, R.roots)}<path class="icv" d="${g.d}"/>
        ${PAINT3(g, up, false, 1)}${eq && R.roots.length ? `<g class="gs" data-s="2">${PAINT3(g, up, true)}</g>` : ''}${dots}</svg>
    </div>`;
}
function PAIR3(r, j){
  const R = ROW3[r], a = j, b = j+1, sa = SIGN3[a], sb = SIGN3[b];
  const lw = j===0 ? '＞ は 上、＜ は 下 を 塗る。' : '≧ は 上、≦ は 下。　＝ が ある ので x軸上も 塗る。';
  const x2 = R.roots.length ? (j===0 ? `＝ が ない → x軸上は 塗らない → <b>白丸</b>。` : `＝ が ある → x軸上も 塗る → <b>黒丸</b>。`) : `x軸と 交わらない ので、x軸上の 点は ない。`;
  return `
  <div class="card abs dcard v2 p3 p3pair">${EQTAPE}
    ${LIST3(r,a,b)}
    <div class="v2c p3pc">${HALF3(r,a)}${HALF3(r,b)}</div>
  </div>
  ${cbar([
    `${NO3[r*4+a]} と ${NO3[r*4+b]}。　同じ グラフで 不等号 だけ ちがう。`,
    lw + (r>0 && j===0 ? '' : ''),
    x2,
    `${NO3[r*4+a]} ${WHY[r][a]} → <b>${ANS3[r][a]}</b>。　${NO3[r*4+b]} ${WHY[r][b]} → <b>${ANS3[r][b]}</b>。`])}`;
}
/* 段の はじめ：グラフを 大きく */
const HEAD3 = ['x軸と 2点で 交わる', 'x軸と 1点で 接する', 'x軸と 交わらない'];
function ROWHEAD(r){
  const R = ROW3[r], g = SG({...R.o});
  return `
  <div class="card abs dcard v2 p3">${EQTAPE}
    <div class="v2c" style="left:60px">
      <div class="v2kw"><div class="v2sm">${['1','2','3'][r]}段目　<span class="math">y ＝ ${R.f}</span></div><div class="v2big"><span class="v2mk">${HEAD3[r]}</span></div></div>
      <div class="p3g" style="left:150px"><svg class="isv" width="${g.W}" height="${g.H}" viewBox="0 0 ${g.W} ${g.H}">${AX3(g)}${NUM3(g, R.roots)}<path class="icv" d="${g.d}"/></svg></div>
    </div>
  </div>
  ${cbar([`${['1','2','3'][r]}段目の グラフ。　この グラフで 不等号を 変えて 4問。　テンポよく 塗って 答えよう！`])}`;
}

/* 段の 終わり：プリントの 配置で 答えを 書きこむ（グラフは 印刷の 形） */
function WRITE(r){
  const y0 = [78,204,348][r], cx = [62.8,182.9,303,423.1], box = [[167.8,202],[311.8,346],[455.8,490]][r];
  const R = ROW3[r];
  const svg = [], items = [];
  SIGN3.forEach((sg,j)=>{
    const L = cx[j], up = j%2===0, eq = j>=2;
    const sc = 10.5, ay = [y0+64, y0+64, y0+70][r], xv = L+53.7;
    const g = {W:600, H:600, ay, X:x=>xv+(x-1)*sc, Y:x=>ay-((x-1)**2+R.o.c)*sc};
    const hw = Math.sqrt(((ay-(y0+18))/sc - R.o.c)); let d=''; for(let i=0;i<=40;i++){ const x=1-hw+2*hw*i/40; d+=(i?'L':'M')+f1(g.X(x))+' '+f1(g.Y(x))+' '; } g.d=d;
    const id='w3_'+(++CL3);
    const clip = up ? `<rect x="${L}" y="${y0}" width="110" height="${f1((eq?ay:ay-.6)-y0)}"/>` : `<rect x="${L}" y="${f1(eq?ay:ay+.6)}" width="110" height="60"/>`;
    svg.push(`<line x1="${L+12}" y1="${ay}" x2="${L+100}" y2="${ay}" stroke="#555" stroke-width=".7"/><polygon points="${L+102},${ay} ${L+98.5},${ay-1.5} ${L+98.5},${ay+1.5}" fill="#555"/><text class="pgt" x="${L+98}" y="${ay+8}" font-style="italic">x</text>`,
      `<clipPath id="${id}">${clip}</clipPath><path d="${d}" fill="none" stroke="#f08a2a" stroke-width="4" stroke-linecap="round" opacity=".6" clip-path="url(#${id})"/><path d="${d}" fill="none" stroke="#111" stroke-width="1.1"/>`,
      R.roots.map(x=>`<circle cx="${f1(g.X(x))}" cy="${ay}" r="2.4" fill="${eq?'#f2a35e':'#fff'}" stroke="${eq?'#e07a1f':'#e0465e'}" stroke-width=".9"/><text class="pgt" x="${f1(g.X(x)+(R.roots.length>1?(x<1?-4:4):0))}" y="${ay+9}" text-anchor="middle">${x<0?'−'+(-x):x}</text>`).join(''));
    svg.push(`<rect x="${L}" y="${box[0]}" width="107.4" height="34.2" fill="none" stroke="#d9d9d9" stroke-width="1.5"/>`);
    items.push(T([L,y0,L+92,y0+14.3],`${NO3[r*4+j]}<span class="xsp"></span>${R.f} ${sg} 0`,9.6));
    const ans = ANS3[r][j];
    items.push(XA(j+1,[L,box[0],L+107.4,box[1]],ans, ans.length>9?8.6:11, MATHY(ans)?'xan':'xja xan'));
  });
  return ptSlide({clip:[58,y0-4,536,box[1]+4], svg, items, done:4, cm:[
    `${['1','2','3'][r]}段目の 答えを プリントに 書こう。`, ...SIGN3.map((sg,j)=>`${NO3[r*4+j]} ${ANS3[r][j]}`)]});
}

/* まとめ（アニメーションなし） */
const SUMC = (t,a) => `<div class="card dsc p3s"><div class="p3st">${t}</div><div class="p3sa">${a}</div></div>`;
const SUM3 = `
  <div class="end-h"><h2>塗れた 形 → 答え</h2></div>
  <div class="dsum p3sum">${SUMC('全部 塗れた','すべての実数')}${SUMC('塗れる ところが ない','解なし')}${SUMC('1点 だけ 塗れた','x ＝ その 数')}${SUMC('1点 だけ 塗れない','その 数 以外の<br>すべての実数')}</div>
  ${cbar([`塗ったら、塗れた 形を 見て 答える。　範囲 だけで なく「すべての実数」「解なし」「x ＝ □」「□ 以外の すべての実数」も ある。`])}`;

/* ====== プリント問題③-2（No.12 の ⑴〜⒇）：Q3 と 同じ 流れを、根と 不等号から 作る（2026-10-28）
   P = {no, f, s:不等号の 番号（0 ＞・1 ＜・2 ≧・3 ≦）, roots:[小, 大] か [接点] か [], lab:根の 文字, ans, list:[[番号, 式]…], cur} */
function GQ(P){
  const up = P.s%2===0, eq = P.s>=2, sg = SIGN3[P.s], kind = P.roots.length===2 ? 0 : P.roots.length===1 ? 1 : 2;
  const [a, b] = P.roots, m = kind===0 ? (a+b)/2 : kind===1 ? a : 0, lab = P.lab || P.roots.map(x=>x<0?'−'+(-x):''+x);
  const o = kind===0 ? {xv:m, k:1, c:-(((b-a)/2)**2), sc:160/(b-a), vs:80/(((b-a)/2)**2), ay:170, top:10, H:316}
          : kind===1 ? {xv:m, k:1, c:0, sc:40, vs:20, ay:250, top:10} : {xv:0, k:1, c:2, sc:40, vs:20, ay:272, top:10};
  const g = SG(o), u = 1/o.sc*40;                                  // u：1目もり 40px ぶんの x
  const any = !(kind===1 && !up) && !(kind===2 && !up);
  const off = i => P.roots.length>1 ? (i?1:-1)*(lab[i].length>3?62:20) : 0;   // 長い 数（⒇）は 外へ ずらす
  const nums = P.roots.map((x,i)=>`<text class="inum" x="${f1(g.X(x)+off(i))}" y="${g.ay+42}" text-anchor="middle">${lab[i]}</text>`).join('');
  const dots = P.roots.map(x=>DOT3(g, x, eq, 4)).join('');
  const NL = (x,i) => [g.X(x)+off(i), g.ay+32];
  const le = eq, s2 = le ? '≦' : '＜';
  let back='', x3='', w4='';
  if(kind===0 && up){
    const L=[g.X(a)-110, g.ay-48], R=[g.X(b)+110, g.ay-48], c1=CMP3(L, NL(a,0), le), c2=CMP3(NL(b,1), R, le);
    back = `<g class="gs" data-s="6">${c1.band}${c2.band}</g>`;
    x3 = XB3(L,[g.X(a-0.4*u),g.Y(a-0.4*u)]) + XB3(R,[g.X(b+0.4*u),g.Y(b+0.4*u)]);
    w4 = c1.sign + c2.sign + WR3(g.X(a)-200, g.ay+80, `x ${s2} ${lab[0]}`) + WR3(g.X(b)+200, g.ay+80, `${lab[1]} ${s2} x`);
  } else if(kind===0){
    const X=[g.X(m), g.Y(m)+42], c1=CMP3(NL(a,0), X, le), c2=CMP3(X, NL(b,1), le);
    back = `<g class="gs" data-s="6">${c1.band}${c2.band}</g>`;
    x3 = XB3(X,[g.X(m),g.Y(m)]);
    w4 = c1.sign + c2.sign + WR3(g.X(a)-170, g.ay+90, `${lab[0]} ${s2} x`) + WR3(g.X(b)+170, g.ay+90, `x ${s2} ${lab[1]}`);
  } else if(kind===1 && P.s===0){
    const L=[g.X(m)-150, g.ay-80], R=[g.X(m)+150, g.ay-80], N=[g.X(m), g.ay+34], c1=CMP3(L, N, false), c2=CMP3(N, R, false);
    back = `<g class="gs" data-s="6">${c1.band}${c2.band}</g>`;
    x3 = XB3(L,[g.X(m-1.5),g.Y(m-1.5)]) + XB3(R,[g.X(m+1.5),g.Y(m+1.5)]);
    w4 = c1.sign + c2.sign + WR3(g.X(m)-250, g.ay+20, `x ＜ ${lab[0]}`) + WR3(g.X(m)+250, g.ay+20, `${lab[0]} ＜ x`);
  } else if(kind===1 && P.s===3){
    const A=[g.X(m)+110, g.ay-60];
    x3 = XB3(A,[g.X(m),g.ay]); w4 = WR3(g.X(m)+220, g.ay-50, `x ＝ ${lab[0]}`);
  } else if(up){
    const A=[g.X(o.xv+1.4)+100, g.Y(o.xv+1.4)];
    x3 = XB3(A,[g.X(o.xv+1.4),g.Y(o.xv+1.4)]);
    w4 = `<text class="iwr p3wr" x="${f1(g.X(o.xv+1.4)+140)}" y="${f1(g.Y(o.xv+1.4)+10)}">どこでも OK</text>`;
  } else {
    x3 = `<text class="iwr p3wr" x="${f1(g.X(o.xv+2.2))}" y="${f1(g.ay-120)}" style="fill:var(--muted)">x を 置く ところが ない</text>`;
  }
  const why = kind===0 ? [['外側 2か所が 塗れた','内側が 塗れた'],['外側 ＋ x軸上','内側 ＋ x軸上']][eq?1:0][up?0:1]
            : kind===1 ? [`${lab[0]} だけ 塗れない`, '塗れる ところが ない', '全部 塗れた', `${lab[0]} の 点 だけ 塗れた`][P.s]
            : (up ? '全部 塗れた' : '塗れる ところが ない');
  const w2 = P.roots.length ? (eq ? 'x軸上も 塗る' : 'x軸上は 塗らない') : 'x軸上に グラフは ない';
  const am = MATHY(P.ans.replace(/[√()/]/g,'1'));
  const same = P.list.every(q=>q[2]===P.list[0][2]);             // 4問とも 同じ 式 → 不等号 だけ、ちがう 式 → 小さく 式も
  const list = `<div class="p3list">${P.list.map(([n,sgn,f],k)=>`<div class="p3i${same?'':' sm'}${k===P.cur?' on':''}${k<P.cur?' done':''}"><span>${n}</span><span class="math">${same?'':f+' '}${sgn} 0</span></div>`).join('')}</div>`;
  return `
  <div class="card abs dcard v2 p3">${EQTAPE}
    ${list}
    <div class="v2c">
      <div class="p3q math">${P.no}　${P.f} <span class="p3sg" data-o="1">${sg} 0</span></div>
      <div class="p3w lh" data-s="2" data-o="4"><span class="v2mk">${up?'0より 大きい':'0より 小さい'}</span><span class="v2sub lh" data-s="3">（${up?'上':'下'}を 塗る）</span></div>
      <div class="p3w lh" data-s="4" data-o="5"><span class="v2mk">${w2}</span></div>
      <div class="p3w lh" data-s="5" data-o="6"><span class="v2mk">${any?'塗れた ところに x を 置く':'塗れた ところは？'}</span></div>
      <div class="p3w p3a lh" data-s="6"><span class="p3why">${why} →</span><span class="v2mk ${am?'math':''}">${P.ans}</span></div>
      <div class="p3g"><svg class="isv" width="${g.W}" height="${g.H}" viewBox="0 0 ${g.W} ${g.H}">
        ${TINT3(g, up, 3)}${back}${AX3(g)}${nums}<path class="icv" d="${g.d}"/>
        ${any ? PAINT3(g, up, false, 3) : ''}${eq && P.roots.length ? `<g class="gs" data-s="4">${PAINT3(g, up, true)}</g>` : ''}${dots}<g class="gs" data-s="5">${x3}</g><g class="gs" data-s="6">${w4}</g></svg></div>
    </div>
  </div>
  ${ptag('プリント問題③-2')}
  ${cbar([
    `${P.no} ${M(`${P.f.replace(/<sup>2<\/sup>/,'²')} ${sg} 0`)}${P.c0 ? '　' + P.c0 : ''}`,
    `右側の「${sg} 0」に 注目。`,
    `${up?'0より 大きい':'0より 小さい'}。`,
    `${up?'0より 大きい → x軸より <b>上</b> を 塗る。':'0より 小さい → x軸より <b>下</b> を 塗る。'}${any?'':'　…でも グラフは x軸より 下に ない！'}`,
    P.roots.length ? (eq ? `＝ が ある → x軸上も 塗る → <b>黒丸</b>。` : `＝ が ない → x軸上は 塗らない → <b>白丸</b>。`) : `x軸と 交わらない ので、x軸上の 点は ない。`,
    any ? `塗れた ところに <b>x</b> を 置く。` : `塗れた ところが ない ので、x を 置けない。`,
    `${why} → 答え <b>${P.ans}</b>。`])}`;
}
/* No.12 の 20問（4問 ずつ 左の 一覧に 出す） */
const R5 = `${FR('1 − √5',2)}`, R5b = `${FR('1 ＋ √5',2)}`;
const PQ = [
  ['⑴',`x${P2} − x − 2`,0,[-1,2],'x ＜ −1, 2 ＜ x'], ['⑵',`x${P2} − x − 2`,1,[-1,2],'−1 ＜ x ＜ 2'],
  ['⑶',`x${P2} − x − 2`,2,[-1,2],'x ≦ −1, 2 ≦ x'], ['⑷',`x${P2} − x − 2`,3,[-1,2],'−1 ≦ x ≦ 2'],
  ['⑸',`x${P2} − 4x ＋ 4`,0,[2],'2以外の すべての実数'], ['⑹',`x${P2} − 4x ＋ 4`,1,[2],'解なし'],
  ['⑺',`x${P2} − 4x ＋ 4`,2,[2],'すべての実数'], ['⑻',`x${P2} − 4x ＋ 4`,3,[2],'x ＝ 2'],
  ['⑼',`x${P2} − 3x ＋ 4`,0,[],'すべての実数'], ['⑽',`x${P2} − 3x ＋ 4`,1,[],'解なし'],
  ['⑾',`x${P2} − 3x ＋ 4`,2,[],'すべての実数'], ['⑿',`x${P2} − 3x ＋ 4`,3,[],'解なし'],
  ['⒀',`x${P2} − 5x ＋ 6`,2,[2,3],'x ≦ 2, 3 ≦ x'], ['⒁',`x${P2} ＋ 4x ＋ 4`,1,[-2],'解なし'],
  ['⒂',`x${P2} − x ＋ 5`,2,[],'すべての実数'], ['⒃',`x${P2} − 2x`,3,[0,2],'0 ≦ x ≦ 2'],
  ['⒄',`x${P2} ＋ 4x ＋ 4`,0,[-2],'−2以外の すべての実数'], ['⒅',`x${P2} ＋ 2`,1,[],'解なし'],
  ['⒆',`x${P2} − 6x ＋ 9`,2,[3],'すべての実数'],
  ['⒇',`x${P2} − x − 1`,3,[-0.618,1.618],`${R5} ≦ x ≦ ${R5b}`, ['(1−√5)/2','(1＋√5)/2'], `図の 交点は ${M(`${R5}`)} と ${M(`${R5b}`)}。`]];
const PROB12 = PQ.map(([no,f,s,roots,ans,lab,c0],i)=>{ const g0 = Math.floor(i/4)*4;
  return {name:`問 ${no}`, html:GQ({no, f, s, roots, ans, lab, c0, cur:i-g0,
    list:PQ.slice(g0,g0+4).map(q=>[q[0], SIGN3[q[2]], q[1]])})}; });
const PH12 = probHead('プリント問題③-2', '次の 2次不等式を、図を 参考に 解け。', ['⑴〜⑷　x² − x − 2', '⑸〜⑻　x² − 4x ＋ 4', '⑼〜⑿　x² − 3x ＋ 4', '⒀〜⒇　いろいろ'],
  `ここから <b>プリント問題③-2</b>（No.12）。　練習編と 同じ「塗って 答える」で 20問！`);

const PG = [{name:'表紙', html:coverF(KK3, '<span class="mk">2次不等式</span><br>練習編', '塗って 答える', 'テンポよく 12問', POL3, '塗って 答える')}];
for(let r=0;r<3;r++){
  PG.push({name:`${['1','2','3'][r]}段目`, html:ROWHEAD(r)});
  for(let j=0;j<4;j++) PG.push({name:`${NO3[r*4+j]} ${SIGN3[j]} 0`, html:Q3(r,j)});
  PG.push({name:`${['1','2','3'][r]}段目 書きこみ`, html:WRITE(r)});
}
PG.push({name:'まとめ', html:SUM3}, {name:'プリント問題', html:PH12}, ...PROB12, {name:'終', html:endF(KK3 + '　2次不等式 練習編', POL3)});
const DECK = {title:'③-2 2次不等式 練習編', pages:PG};
'''

def add(decks):
    base = open(os.path.join(B, 'v2_base_3-1.js'), encoding='utf-8').read()
    decks['3-2_2次不等式_練習編_v2'] = ('③-2 2次不等式 練習編', base + JS)
