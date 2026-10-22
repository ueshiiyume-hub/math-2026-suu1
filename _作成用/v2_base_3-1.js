/* ③-1 ver 2.0 の 土台：ver 1.4 の 部品の 写し（ver 1.4 を 直しても ver 2.0 は 変わらない） */

const IMG = s => s;
const A = (s,r,h,fs,al) => ({s,r,h,fs,al});
const MK = (m,r,e) => ({m,r,e});
const JA = t => `<span class="ja">${t}</span>`;
const FX = (n,d) => KF(n,d);

/* x軸との 共有点（②-1・②-2）の 部品（プリントの 配置どおり。座標は PDF の pt。生徒が 書きこむので 枠の 位置は 変えない）
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


const WB = r => `<rect x="${r[0]}" y="${r[1]}" width="${(r[2]-r[0]).toFixed(1)}" height="${(r[3]-r[1]).toFixed(1)}" fill="#fff"/>`;
const KK = KIMATSU + '　③-1';
const POL = `<div class="fpol"><div class="fa math">x${P2} − 2x − 3 ＞ 0</div><div class="fv">グラフを 塗る</div><div class="fb math">x ＜ −1, 3 ＜ x</div></div>`;

/* ===== 大きい グラフ（px）。y ＝ k(x − r1)(x − r2) を 下に凸で かく。x軸 ＝ 水面 ===== */
function IG(o){
  const W = o.W||660, H = o.H||410, ay = o.ay;
  const X = x => W/2 + (x-o.cx)*o.sc, Y = x => ay - o.k*(x-o.r[0])*(x-o.r[1]);
  const m = (o.r[0]+o.r[1])/2, c0 = (m-o.r[0])*(m-o.r[1]);
  const hw = Math.sqrt((ay-o.top)/o.k - c0), xa = m-hw, xb = m+hw;
  const path = (a,b) => { let d=''; for(let i=0;i<=60;i++){ const x=a+(b-a)*i/60; d+=(i?'L':'M')+X(x).toFixed(1)+' '+Y(x).toFixed(1)+' '; } return d; };
  const f = n => n.toFixed(1);
  const g = {X, Y, ay, W, H, xa, xb, r:o.r, path};
  let wave=''; for(let x=14;x<=W-28;x+=4) wave+=(x===14?'M':'L')+x+' '+(ay+3*Math.sin(x/9)).toFixed(1)+' ';
  g.base = (o.water ? `<g class="${o.ws!==undefined?'gs':''}"${o.ws!==undefined?` data-s="${o.ws}"`:''}><rect class="iwater" x="14" y="${ay}" width="${W-28}" height="${H-ay-6}"/><path class="iwave" d="${wave}"/>
      <text class="iwl" x="22" y="34">水の 上（<tspan font-style="italic">y</tspan> ＞ 0）</text><text class="iwl in" x="22" y="${H-16}">水の 中（<tspan font-style="italic">y</tspan> ＜ 0）</text></g>` : '')
    + `<rect class="itint" data-s="${o.tint??99}" x="14" y="10" width="${W-28}" height="${ay-10}"/>
    <line class="iax" x1="10" y1="${ay}" x2="${W-16}" y2="${ay}"/><polygon class="iah" points="${W-2},${ay} ${W-20},${ay-9} ${W-20},${ay+9}"/>
    <text class="ixl" x="${W-24}" y="${ay+38}">x</text>
    ${o.r.map(x=>`<text class="inum" x="${f(X(x))}" y="${ay+44}" text-anchor="middle">${x<0?'−'+(-x):x}</text>`).join('')}
    <path class="icv${o.cs!==undefined?' gs':''}"${o.cs!==undefined?` data-s="${o.cs}"`:''} d="${path(xa,xb)}"/>`;
  /* 塗る：a から b まで（コースターと 同じ 速さで のびる） */
  g.seg = (a,b,s) => `<g class="ipaint" data-s="${s}"><path pathLength="1" d="${path(a,b)}"/></g>`;
  /* 水面の 点：open＝白丸、さもなくば 黒丸 */
  g.dot = (x,s,open) => `<g class="gs" data-s="${s}"><circle class="iend ${open?'op':''}" cx="${f(X(x))}" cy="${ay}" r="12"/></g>`;
  /* OK・ダメ の 札（グラフの 上に） */
  g.tag = (x,s,ok,txt,dx=0) => `<g class="gs" data-s="${s}"><text class="itag ${ok?'ok':'ng'}" x="${f(X(x)+dx)}" y="${f(Y(x)+(Y(x)<ay?-26:44))}" text-anchor="middle">${txt}</text></g>`;
  /* 塗れた 部分に 置く x の 札 */
  g.xmark = (x,s) => `<g class="gs" data-s="${s}"><circle class="ixb" cx="${f(X(x)+(x<m?-34:34))}" cy="${f(Y(x))}" r="24"/><text class="ixt" x="${f(X(x)+(x<m?-34:34))}" y="${f(Y(x)+10)}" text-anchor="middle">x</text></g>`;
  /* 高さ y の 矢印（x軸 から グラフの 点まで） */
  g.hgt = (x,s,lab,e=99,left=false) => { const up = Y(x)<ay; return `<g class="gs ihg" data-s="${s}" data-o="${e}"><line class="ihl ${up?'up':'dn'}" x1="${f(X(x))}" y1="${ay}" x2="${f(X(x))}" y2="${f(Y(x)+(up?10:-10))}"/><polygon class="ihh ${up?'up':'dn'}" points="${f(X(x)-8)},${f(Y(x)+(up?14:-14))} ${f(X(x)+8)},${f(Y(x)+(up?14:-14))} ${f(X(x))},${f(Y(x))}"/><circle class="ipc" cx="${f(X(x))}" cy="${f(Y(x))}" r="8"/><text class="ihtx ${up?'up':'dn'}" text-anchor="${left?'end':'start'}" x="${f(X(x)+(left?-14:14))}" y="${f(up?(ay+Y(x))/2+8:Y(x)+34)}">${lab}</text></g>`; };
  /* スタート地点で 待つ 乗り物（s 番で 出て、e 番で 消える） */
  g.wait = (kind,s,e) => `<div class="iwait lh" data-s="${s}" data-o="${e}" style="left:${f(X(xa)-32)}px;top:${f(Y(xa)-30)}px">${RIDER(kind,false)}</div>`;
  g.svg = (...parts) => `<svg class="isv" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${parts.join('')}</svg>`;
  /* コースター（レール＝放物線 に そって 走る）。wa 番で 走り、wb 番で 消える */
  /* 乗り物（鳥号・魚号）が レール（放物線）に そって 進む。wa 番で 走り、wb 番で 消える。ng＝息が できない（くるしい 顔） */
  g.ride = (a,b,wa,wb,kind,ng) => `<div class="iride${ng?' ng':''}" data-wa="${wa}" data-wb="${wb}" style="offset-path:path('${path(a,b)}')">${RIDER(kind,ng)}${ng?'<span class="ibub">くるしい…</span>':''}</div>`;
  return g;
}

/* 鳥号・魚号の 絵（ng＝くるしい 顔） */
const RIDER = (kind, ng) => {
  const eye = (x,y) => ng ? `<path d="M${x-3} ${y-3} l6 6 M${x+3} ${y-3} l-6 6" stroke="#333" stroke-width="2" stroke-linecap="round"/>` : `<circle cx="${x}" cy="${y}" r="3" fill="#333"/><circle cx="${x+1}" cy="${y-1}" r="1" fill="#fff"/>`;
  const sad = (x,y) => ng ? `<path d="M${x-3} ${y+1} q3 -3 6 0" fill="none" stroke="#333" stroke-width="1.8" stroke-linecap="round"/>` : '';
  const ani = kind==='fish'
    ? `<path d="M14 18 L6 8 L6 28 Z" fill="#f08a2a"/><ellipse cx="32" cy="18" rx="18" ry="12" fill="#5aa9e6"/><path d="M26 7 q6 -7 12 0" fill="#3f86c4"/>${eye(40,15)}${sad(44,21)}`
    : `<circle cx="32" cy="16" r="13" fill="#ffd34d"/><path d="M19 18 q6 -10 14 -2 q-6 7 -14 2 Z" fill="#f5b400"/><path d="M44 14 l10 4 l-10 4 Z" fill="#f08a2a"/>${eye(38,12)}${sad(40,20)}`;
  return `<svg width="64" height="48" viewBox="0 0 64 48">${ani}<path d="M4 26 L60 26 L56 40 L8 40 Z" fill="#e0465e"/><rect x="4" y="25" width="56" height="4" rx="2" fill="#c0304a"/><circle cx="16" cy="43" r="5" fill="#4a4560"/><circle cx="48" cy="43" r="5" fill="#4a4560"/></svg>`; };
/* 説明の 中の 小さな アイコン */
const ICON = kind => `<span class="iicon">${RIDER(kind,false)}</span>`;
const IP = (s,h,cls='') => `<div class="ipr lh ${cls}" data-s="${s}">${h}</div>`;
const EQ1 = `x${P2} − 2x − 3 ＞ 0`, EQ2 = `x${P2} ＋ 3x ＋ 2 ≦ 0`;
/* ②-1 と 同じ くらい しゅっと した 放物線 */
const G1 = {ay:220, cx:1, sc:80, k:42, r:[-1,3], top:22};
const G2 = {ay:220, cx:-1.5, sc:160, k:330, r:[-2,-1], top:22};

/* ===== 2枚目：考え方 ===== */
const gk = IG({...G1, tint:3, cs:1});
const s0 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ig">${gk.svg(gk.base)}</div>
    <div class="ipn">
      <div class="ipr ibig math">${EQ1}</div>
      <div class="ipr ja0">って どういう こと？</div>
      ${IP(1,`x${P2} − 2x − 3 を <b class="math">y</b> と おく<br><span class="math">y ＝ x${P2} − 2x − 3</span>`)}
      ${IP(2,`「＞ 0」は <b class="math">y ＞ 0</b>`)}
      ${IP(3,`y ＞ 0 ＝ グラフが <b>x軸より 上</b>`)}
      ${IP(4,`グラフが x軸より 上に なる <b>x</b> を 探す 問題！`,'ikey')}
    </div>
  </div>
  ${cbar([
    `初めての <b>2次不等式</b>。　${M('x² − 2x − 3 ＞ 0')} って、どういう 意味だろう？`,
    `左の 式 ${M('x² − 2x − 3')} を <b>y</b> と おく。　すると、おなじみの 2次関数の グラフが かける。`,
    `「${M('x² − 2x − 3')} が 0 より 大きい」は「<b>y が 0 より 大きい</b>」と 同じ。`,
    `y ＞ 0 は、グラフの 点が <b>x軸より 上</b> に ある ところ。`,
    `つまり 2次不等式は、グラフが x軸より 上（または 下）に なる <b>x の 範囲</b> を 探す 問題！`])}`;

/* ===== 3枚目：2次不等式の 解き方（プリントの 枠どおり） ===== */
const s1 = ptSlide({clip:[60,84,535,252],
  svg:[`<rect class="xpb" x="62.1" y="85" width="470.9" height="165.9"/>`,
       WB([182.9,109.7,302.7,138]), WB([163.5,146.1,266.2,174.5]), WB([244.9,182.1,282.6,210.4]), WB([370.7,182.1,408.4,210.4]), WB([192,218.1,229.8,246.4])],
  items:[
    T([71.9,94.5,250,109],'<span class="ja" style="font-weight:900">2次不等式の解き方</span>',12),
    T([80.6,116.5,128,130],'<span class="ja"><i class="nv">Step</i>❶</span>'), T([80.6,188.8,128,202.3],'<span class="ja"><i class="nv">Step</i>❷</span>'), T([80.6,224.8,128,238.3],'<span class="ja"><i class="nv">Step</i>❸</span>'),
    T([129.3,116.5,182.9,130],'<span class="ja">2次関数の</span>',9.2), T([304.5,116.5,420,130],'<span class="ja">の問題として解く。</span>',9.2),
    T([129.3,152.5,163.5,166],'<span class="ja">つまり、</span>',8.7), T([268,152.5,380,166],'<span class="ja">を解き、グラフを書く。</span>',9.2),
    T([129.3,188.8,244.9,202.3],`<span class="ja">グラフを塗る。<i class="math">y</i> ＞ 0の時、</span>`,8.7), T([284.4,188.8,370.7,202.3],`<span class="ja">を塗る。<i class="math">y</i> ＜ 0の時、</span>`,8.7), T([410.2,188.8,460,202.3],'<span class="ja">を塗る。</span>',9.2),
    T([129.3,224.8,192,238.3],'<span class="ja">塗れた場所を</span>',9.2), T([231.6,224.8,320,238.3],'<span class="ja">方向で答える。</span>',9.2),
    XA(1,[182.9,109.7,302.7,138],'x軸との共有点',11,'xja xan'), XA(2,[163.5,146.1,266.2,174.5],'y ＝ 0（2次方程式）',9.5,'xja xan'),
    XA(3,[244.9,182.1,282.6,210.4],'上',13,'xja xan'), XA(4,[370.7,182.1,408.4,210.4],'下',13,'xja xan'), XA(5,[192,218.1,229.8,246.4],'x軸',12,'xja xan')],
  cm:[
    `2次不等式の 解き方は 3つの <i class="nv">Step</i>。　空らんを うめよう。`,
    `<i class="nv">Step</i>❶：グラフと x軸の 関係を 見る → 2次関数の <b>x軸との 共有点</b> の 問題。`,
    `x軸との 共有点 → <b>y ＝ 0</b>（2次方程式）を 解いて、グラフを かく。　②-1 と 同じ！`,
    `<i class="nv">Step</i>❷：y ＞ 0 は x軸より <b>上</b> → 上を 塗る。`,
    `y ＜ 0 は x軸より <b>下</b> → 下を 塗る。`,
    `<i class="nv">Step</i>❸：塗れた 場所を <b>x軸</b> 方向で 答える（x の 範囲で 答える）。`]});

/* ===== 例の プリントの 配置（⑴ dy＝0、⑵ dy＝252）。phase 1：<i class="nv">Step</i>❶ ／ 2：<i class="nv">Step</i>❷・❸ ===== */
function PR(o){
  const dy = o.dy, Yd = y => y+dy, R = r => [r[0],r[1]+dy,r[2],r[3]+dy];
  const ph1 = o.phase===1, sx = n => ph1 ? n : undefined;
  const pv = o.pv;      // 印刷された グラフ：xv, yv, q
  const top = Yd(440), ay = Yd(492);
  const hw = Math.sqrt((pv.yv+dy-top)/pv.q); let d='';
  const rr = Math.sqrt((pv.yv+dy-ay)/pv.q), r1 = pv.xv-rr, r2 = pv.xv+rr, Yc = x => (pv.yv+dy)-pv.q*(x-pv.xv)**2;
  for(let i=0;i<=50;i++){ const x=pv.xv-hw+2*hw*i/50; d+=(i?'L':'M')+x.toFixed(2)+' '+((pv.yv+dy)-pv.q*(x-pv.xv)**2).toFixed(2)+' '; }
  const L = (s,r,h,fs=11) => s===undefined ? T(R(r),h,fs,'xan') : XA(s,R(r),h,fs,'xan xl');
  const items = [
    T(R([62.3,281.5,200,297.5]),`${o.no}<span class="xsp"></span>${o.eq}`,11),
    T(R([73.5,304.5,119,323]),'<span class="ja"><i class="nv">Step</i>❶</span>',10.5,'ac'), T(R([73.5,428.9,119,447.4]),'<span class="ja"><i class="nv">Step</i>❷</span>',10.5,'ac'), T(R([286.7,428.9,332.3,447.4]),'<span class="ja"><i class="nv">Step</i>❸</span>',10.5,'ac'),
    T([r1-14,ay+1.5,r1+6,ay+12.5],`<span style="font-size:.8em">${o.lab[0]}</span>`,8.5,'ac'), T([r2-6,ay+1.5,r2+14,ay+12.5],`<span style="font-size:.8em">${o.lab[1]}</span>`,8.5,'ac'),
    L(sx(1),[148,309,326,331],o.c[0]), {s:sx(2), r:R([262,310,326,330]), h:`<span class="ytag">y ＝ 0 と する</span>`, fs:7.8, cls:'xyt'},
    L(sx(2),[148,335,326,357],o.c[1]), L(sx(3),[148,361,326,383],o.c[2]), L(sx(4),[148,387,326,409],o.c[3]),
    ...(ph1 ? [] : [XA(8,R([323.2,467.2,507.3,498.3]),o.ans,13),
       ...o.rw.map((h,i)=>({s:5+2*i, r:[333+i*86,Yd(449),411+i*86,Yd(463)], h:h, fs:11, cls:'xan xwr', al:'c'}))])];
  const svg = [
    `<rect class="xpb" x="73.5" y="${Yd(304.5)}" width="45.5" height="18.5"/><rect class="xpb" x="73.5" y="${Yd(428.9)}" width="45.5" height="18.5"/><rect class="xpb" x="286.7" y="${Yd(428.9)}" width="45.6" height="18.5"/>`,
    `<rect class="xpb" x="142.8" y="${Yd(305.4)}" width="184" height="109.8"/><rect class="xpb" x="354.2" y="${Yd(305.4)}" width="137.2" height="109.8"/><rect class="xpr" x="323.2" y="${Yd(467.2)}" width="184.1" height="31.1"/>`,
    `<line x1="373.5" y1="${Yd(384.5)}" x2="467" y2="${Yd(384.5)}" stroke="#555" stroke-width=".7"/><polygon points="469,${Yd(384.5)} 465.5,${Yd(383)} 465.5,${Yd(386)}" fill="#555"/><text class="pgt" x="465" y="${Yd(392)}" font-style="italic">x</text>`,
    `<line x1="140" y1="${ay}" x2="268" y2="${ay}" stroke="#333" stroke-width=".8"/><polygon points="271,${ay} 266.5,${ay-1.8} 266.5,${ay+1.8}" fill="#333"/><text class="pgt" x="265" y="${ay+11}" font-style="italic" style="font-size:9px">x</text>`,
    `<path d="${d}" fill="none" stroke="#111" stroke-width="1.6"/>`,
    ph1 ? PB({xv:o.gx, yv:Yd(404.5), q:0.05, ay:Yd(384.5), top:Yd(312), s:6, dot:'f', ds:5, ls:7, lab:[[o.gx-20,o.lab[0]],[o.gx+20,o.lab[1]]]})
        : PB({xv:pv.xv, yv:pv.yv+dy, q:pv.q, ay, top, draw:false, paint:o.paint, ps:1, dot:o.dot, ds:2})];
  if(!ph1){
    /* x を 置く（塗れた ところと 点線で つなぐ）→ 数と 斜めに 比べる（うすい 帯 ＋ 不等号）*/
    const f = n => n.toFixed(1);
    const P = o.out ? {L:[r1,ay+2], R:[r2,ay+2]} : {L:[r1-4,ay+9], R:[r2+4,ay+9]};
    const X = o.out ? [{at:[r1-22,ay-11], to:[r1-7,Yc(r1-7)]}, {at:[r2+22,ay-11], to:[r2+7,Yc(r2+7)]}]
                    : [{at:[pv.xv,ay+36], to:[pv.xv,Yc(pv.xv)+1.5]}];
    const pairs = o.out ? [[X[0].at,P.L,4],[P.R,X[1].at,6]] : [[P.L,X[0].at,4],[X[0].at,P.R,6]];   // [小さい 方, 大きい 方, 番]
    const le = o.dot==='f';
    pairs.forEach(([A,B,st])=>{
      const mx=(A[0]+B[0])/2, my=(A[1]+B[1])/2, ang=Math.atan2(B[1]-A[1],B[0]-A[0])*180/Math.PI, len=Math.hypot(B[0]-A[0],B[1]-A[1])+16;
      const tr = `translate(${f(mx)} ${f(my)}) rotate(${f(ang)})`;
      svg.splice(4,0,`<g class="gs" data-s="${st}"><rect class="iband2" x="${f(-len/2)}" y="-7" width="${f(len)}" height="14" rx="7" transform="${tr}"/></g>`);
      svg.push(`<g class="gs" data-s="${st}"><path class="ilt pt" d="M3.5 -3.5 L-3.5 0 L3.5 3.5${le?' M-3.5 2.6 L3.5 6.1':''}" transform="${tr}"/></g>`);
    });
    svg.push(`<g class="gs" data-s="3">${X.map(x=>`<line class="ixln pt" x1="${f(x.at[0])}" y1="${f(x.at[1])}" x2="${f(x.to[0])}" y2="${f(x.to[1])}"/><circle class="ixdot" cx="${f(x.to[0])}" cy="${f(x.to[1])}" r="1.4"/><circle class="ixb" cx="${f(x.at[0])}" cy="${f(x.at[1])}" r="5.2"/><text class="ixt pt" x="${f(x.at[0])}" y="${f(x.at[1]+2.4)}" text-anchor="middle">x</text>`).join('')}</g>`);
  }
  if(!ph1) svg.push(PB({xv:o.gx, yv:Yd(404.5), q:0.05, ay:Yd(384.5), top:Yd(312), dot:'f', lab:[[o.gx-20,o.lab[0]],[o.gx+20,o.lab[1]]]}).replace(/class="curve pgc" data-s="undefined"/,'class="curve pgc show"').replace(/class="gs" data-s="undefined"/g,'class="gs show"'));
  return ptSlide({clip:[60,278+dy,535,(ph1||o.out?526:544)+dy], svg, items, done: ph1 ? 7 : 8, cm:o.cm});
}
const P1 = {dy:0, no:'⑴', eq:EQ1, gx:420, lab:['−1','3'], pv:{xv:201.9, yv:520, q:0.0581},
  c:[`y ＝ x${P2} − 2x − 3`, `x${P2} − 2x − 3 ＝ 0`, '(x ＋ 1)(x − 3) ＝ 0', 'x ＝ −1, 3'], ans:'x ＜ −1, 3 ＜ x', paint:'up', dot:'o', out:true, rw:['x ＜ −1','3 ＜ x']};
const P2_ = {dy:252, no:'⑵', eq:EQ2, gx:420, lab:['−2','−1'], pv:{xv:201.9, yv:520, q:0.0581},
  c:[`y ＝ x${P2} ＋ 3x ＋ 2`, `x${P2} ＋ 3x ＋ 2 ＝ 0`, '(x ＋ 2)(x ＋ 1) ＝ 0', 'x ＝ −2, −1'], ans:'−2 ≦ x ≦ −1', paint:'down', dot:'f', out:false, rw:['−2 ≦ x','x ≦ −1']};
const STEP1CM = (P,fac,why) => [
  `${P.no} ${M(P.eq.replace(/<sup>2<\/sup>/,'²'))}。　<b><i class="nv">Step</i>❶</b>：2次関数の x軸との 共有点の 問題として 解く。`,
  `左の 式を y と おく。　${M(P.c[0].replace(/<sup>2<\/sup>/,'²'))}。`,
  `x軸との 共有点 → <b>y ＝ 0</b> と する。　${M(P.c[1].replace(/<sup>2<\/sup>/,'²'))}。`,
  `${why} → <b>因数分解</b>。　${M(fac)}。`,
  `${M(P.c[3])}。　これが グラフと x軸の 共有点。`,
  `右の グラフ。　x軸に 共有点を 2つ 打つ。`,
  `下に凸の 放物線を、2つの 点を 通るように かく。`,
  `点の 下に x座標を 書く。　<i class="nv">Step</i>❶ <b>完成！</b>`];

/* ===== 例⑴ ===== */
const s2 = PR({...P1, phase:1, cm:STEP1CM(P1,'(x ＋ 1)(x − 3) ＝ 0','たして −2、かけて −3')});
/* ===== Step❷ を 2枚に：A「どこを 塗る？」（理屈だけ）・B「左から 塗る」（作業だけ） =====
   o = {no, eq（タイトル）, ex（左の 式）, rel（' ＞ 0' など）, up（上を 塗る か）, kind（'bird'|'fish'）, G（グラフ）, cm} */
function WHERE(o){
  const g = IG({...o.G, ay:150, top:14, W:900, H:300, water:true});
  const dim = o.up ? `<rect x="14" y="${g.ay}" width="${g.W-28}" height="${g.H-g.ay}" fill="var(--paper)" opacity=".72"/>`
                   : `<rect x="14" y="0" width="${g.W-28}" height="${g.ay}" fill="var(--paper)" opacity=".72"/>`;
  const box = o.up ? `<rect class="ifocus" x="16" y="4" width="${g.W-32}" height="${g.ay-8}" rx="10"/>`
                   : `<rect class="ifocus" x="16" y="${g.ay+4}" width="${g.W-32}" height="${g.H-g.ay-12}" rx="10"/>`;
  const ah = o.up ? 110 : 230;
  return `
  <div class="card abs dcard">${EQTAPE}
    <div class="ieq math"><span class="iex" data-o="1">${o.ex}</span><span class="iey" data-o="1">y</span><span class="ile">${o.rel}</span></div>
    <div class="iarr gs" data-s="2"><svg width="60" height="${ah}" viewBox="0 0 60 ${ah}"><path d="M30 4 L30 ${ah-30}" stroke="#e0465e" stroke-width="8" stroke-linecap="round"/><polygon points="10,${ah-40} 50,${ah-40} 30,${ah-4}" fill="#e0465e"/></svg></div>
    <div class="iga">${g.svg(g.base, `<g class="gs" data-s="2">${dim}${box}</g>`)}
      <div class="ifish lh" data-s="3" style="${o.up?'left:500px;top:24px':'left:520px;top:190px'}">${RIDER(o.kind,false)}<span>${o.kind==='bird'?'鳥':'魚'}は ここなら 息が できる！</span></div></div>
  </div>
  ${cbar(o.cm)}`;
}
/* segs：[[a,b,ok],…]（3つ）、dots：[x,open]（2つ）、caps：8つ（0〜7番） */
function RIDE(o){
  const g = IG({...o.G, ay:190, top:12, W:1100, H:400, water:true});
  const S = o.segs.map(([a,b])=>[a==='L'?g.xa:a, b==='R'?g.xb:b, ]);
  const st = [1,3,5];
  const hl = S.map(([a,b],i)=>`<path class="ihl2 gs" data-s="${st[i]}" data-o="${st[i]+1}" d="${g.path(a,b)}"/>`).join('');
  const paint = S.map(([a,b],i)=>o.segs[i][2] ? g.seg(a,b,st[i]) : '').join('');
  const dots = o.dots.map(([x,open],i)=>g.dot(x,[2,4][i],open)).join('');
  const rides = S.map(([a,b],i)=>g.ride(a, i===2 ? a+(b-a)*0.75 : b, st[i], i<2?st[i+1]:99, o.kind, !o.segs[i][2])).join('');
  const caps = o.caps.map((h,i)=>`<div class="icap lh" data-s="${i}" data-o="${i<o.caps.length-1?i+1:99}">${h}</div>`).join('');
  return `
  <div class="card abs dcard">${EQTAPE}
    <div class="ititle math">${o.no}　${o.eq}</div>
    ${caps}
    <div class="igb">${g.svg(g.base.replace('class="icv"','class="icv ifaint"'), hl, paint)}
      ${g.wait(o.kind,0,1)}${rides}
      <svg class="isv iov" width="${g.W}" height="${g.H}" viewBox="0 0 ${g.W} ${g.H}">${dots}</svg></div>
  </div>
  ${cbar(o.cm)}`;
}

const s3a = WHERE({no:'⑴', ex:`x${P2} − 2x − 3`, rel:' ＞ 0', up:true, kind:'bird', G:{cx:1, sc:100, k:30, r:[-1,3]}, cm:[
  `⑴ ${M('x² − 2x − 3 ＞ 0')}。　グラフの <b>どこ</b> を 塗れば いい？`,
  `Step❶ で ${M('y ＝ x² − 2x − 3')} と おいた。　だから 左の 式は <b>y</b>。　この 不等式は <b>y ＞ 0</b>。`,
  `y は グラフの 点の 高さ。　y ＞ 0 は 高さが プラス → x軸（水面）より <b>上</b>、つまり <b>空</b>。`,
  `空が すきな <b>鳥</b> が コースターに 乗って 出発！　鳥が 息が できる ところを 塗ろう。`]});
const s3b = RIDE({no:'⑴', eq:EQ1, kind:'bird', G:{cx:1, sc:140, k:40, r:[-1,3]},
  segs:[['L',-1,true],[-1,3,false],[3,'R',true]], dots:[[-1,true],[3,true]],
  caps:['左から コースターが 進む','空 → 息が できる → <b>塗る！</b>','−1 は 水面 → ○ 塗れない','水の 中 → くるしい…','3 も 水面 → ○ 塗れない','空 → また <b>塗る！</b>','塗れたのは <b>ここ</b>！'],
  cm:[
  `左から 順に 見て いく。　鳥は 空なら 息が できる。`,
  `はじめは 空（水の 上）→ 息が できる → <b>塗る</b>。`,
  `−1 で ちょうど 水面（y ＝ 0）。　「0 ＞ 0」は まちがい → 塗れない → 中が 空っぽの <b>白丸</b>。`,
  `−1 から 3 の 間は 水の 中 → 鳥は くるしい → 塗らない。`,
  `3 で また 水面。　ここも 塗れない → <b>白丸</b>。`,
  `3 より 少しでも 右なら また 空 → 白丸の 先を <b>塗る</b>。`,
  `塗れたのは −1 より 左 と 3 より 右 の 2か所。`]});

/* ⑴ Step❸：塗れた ところに x を 置き、−1・3 と 斜めに 並べて 不等号で 比べる → 下に 式として 書き直す */
/* 比べる 組：xs＝x を 置く 側（'L'：数の 左上、'R'：数の 右上）、r＝比べる 数、xc＝線で つなぐ グラフ上の x、s＝出る 番 */
const CMP = (g, side, r, xc, sx, s, out) => {
  const f = n => n.toFixed(1), nx = g.X(r), ny = g.ay+34;
  const bx = side==='L' ? nx-120 : nx+120, by = g.ay-44;
  const cx = g.X(xc), cy = g.Y(xc);
  const mx = (bx+nx)/2, my = (by+ny)/2, ang = Math.atan2(ny-by, nx-bx)*180/Math.PI;
  const rot = side==='L' ? ang : ang-180;
  const len = Math.hypot(nx-bx, ny-by) + 76;
  const tx = side==='L' ? nx-70 : nx+70, ty = g.ay+150;
  /* 斜めの 帯（マーカーで なぞった ような うすい 色）を x と 数の 後ろに */
  const band = `<g class="gs" data-s="${s}"><rect class="iband2" x="${f(-len/2)}" y="-30" width="${f(len)}" height="60" rx="30" transform="translate(${f(mx)} ${f(my)}) rotate(${f(ang)})"/>
</g>`;
  return {band, rest:`<g class="gs" data-s="${s}"><path class="ilt" d="M16 -16 L-16 0 L16 16" transform="translate(${f(mx)} ${f(my)}) rotate(${f(rot)})"/></g>
    <g class="gs" data-s="${sx}"><line class="ixln" x1="${f(bx)}" y1="${f(by)}" x2="${f(cx)}" y2="${f(cy)}"/><circle class="ixdot" cx="${f(cx)}" cy="${f(cy)}" r="6"/>
      <circle class="ixb" cx="${f(bx)}" cy="${f(by)}" r="24"/><text class="ixt" x="${f(bx)}" y="${f(by+10)}" text-anchor="middle">x</text></g>
    <g class="gs" data-s="${s+1}"><path class="iarw" d="M${f(mx)} ${f(my+34)} Q${f((mx+tx)/2-10)} ${f(ty-60)} ${f(tx)} ${f(ty-40)}"/><polygon class="iarh" points="${f(tx-8)},${f(ty-50)} ${f(tx+8)},${f(ty-46)} ${f(tx)},${f(ty-32)}"/>
      <text class="iwr" x="${f(tx)}" y="${f(ty)}" text-anchor="middle">${out.replace(/x/g,'<tspan font-style="italic">x</tspan>')}</text></g>`}; };
const b1 = IG({...G1, ay:190, H:420});
const C1L = CMP(b1,'L',-1,-1.35,1,2,'x ＜ −1'), C1R = CMP(b1,'R',3,3.35,1,4,'3 ＜ x');
const s4 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ititle math">⑴　${EQ1}　<span class="istep"><i class="nv">Step</i>❸ 答える</span></div>
    <div class="ig">${b1.svg(C1L.band, C1R.band, b1.base, b1.seg(b1.xa,-1,0), b1.seg(3,b1.xb,0), b1.dot(-1,0,true), b1.dot(3,0,true), C1L.rest, C1R.rest)}</div>
    <div class="ipn3">
      <div class="ians lh" data-s="6"><span class="math">x ＜ −1, 3 ＜ x</span></div>
      <div class="itip2 lh" data-s="6">白丸 → ＜　　黒丸 → ≦</div>
    </div>
  </div>
  ${cbar([
    `<b><i class="nv">Step</i>❸ 答える</b>。　塗れた ところの x は どんな 数？`,
    `塗れた 2か所に <b>x</b> を 置く。　x軸の 近くに 置くと −1、3 と 並ぶ。`,
    `左：x は −1 より 左 → −1 より <b>小さい</b>。　−1 は 白丸 なので ＝ の ない <b>＜</b>。`,
    `斜めの ままでは 読みにくいので、式に 書き直して ${M('x ＜ −1')}。`,
    `右：x は 3 より 右 → 3 より <b>大きい</b>。　3 も 白丸 → <b>＜</b>。`,
    `書き直して ${M('3 ＜ x')}。`,
    `2つを 「,」で 並べて ${M('x ＜ −1, 3 ＜ x')}。　<b>完成！</b>`])}`;

const s5 = PR({...P1, phase:2, cm:[
  `プリントに 書きこもう。　<i class="nv">Step</i>❷ の グラフ。`,
  `x軸より 上の 部分（外側の 2本）を 塗る。`,
  `端の −1、3 は 白丸（含まない）。`,
  `<i class="nv">Step</i>❸。　塗れた 2か所に <b>x</b> を 置く。`,
  `左：x は −1 より 左 → 小さい。　白丸 なので <b>＜</b>。`,
  `書き直して ${M('x ＜ −1')}。`,
  `右：x は 3 より 右 → 大きい。　白丸 なので <b>＜</b>。`,
  `書き直して ${M('3 ＜ x')}。`,
  `<i class="nv">Step</i>❸ の 枠に ${M('x ＜ −1, 3 ＜ x')}。　<b>完成！</b>`]});

/* ===== 例⑵ ===== */
const s6 = PR({...P2_, phase:1, cm:STEP1CM(P2_,'(x ＋ 2)(x ＋ 1) ＝ 0','たして ＋3、かけて ＋2')});
const s7a = WHERE({no:'⑵', ex:`x${P2} ＋ 3x ＋ 2`, rel:' ≦ 0', up:false, kind:'fish', G:{cx:-1.5, sc:200, k:300, r:[-2,-1]}, cm:[
  `⑵ ${M('x² ＋ 3x ＋ 2 ≦ 0')}。　グラフの <b>どこ</b> を 塗れば いい？`,
  `Step❶ で ${M('y ＝ x² ＋ 3x ＋ 2')} と おいた。　だから 左の 式は <b>y</b>。　この 不等式は <b>y ≦ 0</b>。`,
  `y は グラフの 点の 高さ。　y ≦ 0 は 高さが 0 以下 → x軸（水面）より <b>下</b>、つまり <b>水の 中</b>。`,
  `水の 中が すきな <b>魚</b> が コースターに 乗って 出発！　魚が 息が できる ところを 塗ろう。`]});
const s7b = RIDE({no:'⑵', eq:EQ2, kind:'fish', G:{cx:-1.5, sc:260, k:300, r:[-2,-1]},
  segs:[['L',-2,false],[-2,-1,true],[-1,'R',false]], dots:[[-2,false],[-1,false]],
  caps:['左から コースターが 進む','空 → くるしい…','−2 は 水面 → ● 塗れる','水の 中 → <b>塗る！</b>','−1 も 水面 → ● 塗れる','空 → くるしい…','塗れたのは <b>ここ</b>！'],
  cm:[
  `左から 順に 見て いく。　魚は 水の 中なら 息が できる。`,
  `はじめは 空（水の 上）。　魚は 息が できない → 塗らない。`,
  `−2 で ちょうど 水面（y ＝ 0）。　「0 ≦ 0」は 正しい → 塗れる → 中まで 塗った <b>黒丸</b>。`,
  `−2 から −1 の 間は 水の 中 → 息が できる → <b>塗る</b>。`,
  `−1 で また 水面。　「0 ≦ 0」は 正しい → <b>黒丸</b>。`,
  `−1 より 右は 空 → くるしい → 塗らない。`,
  `塗れたのは −2 から −1 の 1か所 だけ。`]});

/* ⑵ Step❸ */
const b2 = IG({...G2});
const s8 = `
  <div class="card abs dcard">${EQTAPE}
    <div class="ititle math">⑵　${EQ2}　<span class="istep"><i class="nv">Step</i>❸ 答える</span></div>
    <div class="ig">${b2.svg(b2.base, b2.seg(-2,-1,0), b2.dot(-2,0,false), b2.dot(-1,0,false),
      `<g class="gs" data-s="1"><circle class="ixb" cx="${b2.X(-1.5)}" cy="${b2.Y(-1.5)+46}" r="24"/><text class="ixt" x="${b2.X(-1.5)}" y="${b2.Y(-1.5)+56}" text-anchor="middle">x</text></g>`,
      `<g class="gs" data-s="2"><text class="iblab" x="${b2.X(-2)-40}" y="${b2.Y(-1.5)+56}" text-anchor="middle">−2 ≦</text></g>`,
      `<g class="gs" data-s="3"><text class="iblab" x="${b2.X(-1)+40}" y="${b2.Y(-1.5)+56}" text-anchor="middle">≦ −1</text></g>`)}</div>
    <div class="ipn">
      <div class="ipr">塗れた ところ の x は？</div>
      ${IP(1,`塗れた 1か所に <b class="math">x</b> を 置く`,'isub')}
      ${IP(2,`x は −2 より <b>大きい</b>（右）<br>−2 は 黒丸 → <span class="math">−2 ≦ x</span>`,'isub')}
      ${IP(3,`x は −1 より <b>小さい</b>（左）<br>−1 も 黒丸 → <span class="math">x ≦ −1</span>`,'isub')}
      <div class="ians lh" data-s="4"><span class="math">−2 ≦ x ≦ −1</span></div>
      ${IP(5,`x が 2つに <b>はさまれる</b> 形`,'itip')}
    </div>
  </div>
  ${cbar([
    `⑵ の <b><i class="nv">Step</i>❸ 答える</b>。　塗れた ところは 真ん中の 1か所。`,
    `塗れた 部分に <b>x</b> を 置く。`,
    `x は −2 より 右 ＝ <b>大きい</b>。　−2 は 黒丸（塗れる）なので ${M('−2 ≦ x')}。`,
    `x は −1 より 左 ＝ <b>小さい</b>。　−1 も 黒丸 なので ${M('x ≦ −1')}。`,
    `まとめて ${M('−2 ≦ x ≦ −1')}。`,
    `x が −2 と −1 に <b>はさまれる</b> 形。　黒丸 なので ≦。　<b>完成！</b>`])}`;

const s9 = PR({...P2_, phase:2, cm:[
  `プリントに 書きこもう。　<i class="nv">Step</i>❷ の グラフ。`,
  `x軸より 下の 部分（真ん中の 1本）を 塗る。`,
  `端の −2、−1 は 黒丸（含む）。`,
  `<i class="nv">Step</i>❸。　塗れた ところに <b>x</b> を 置く。`,
  `x は −2 より 右 → 大きい。　黒丸 なので <b>≦</b>。`,
  `書き直して ${M('−2 ≦ x')}。`,
  `x は −1 より 左 → 小さい。　黒丸 なので <b>≦</b>。`,
  `書き直して ${M('x ≦ −1')}。`,
  `2つを まとめて、<i class="nv">Step</i>❸ の 枠に ${M('−2 ≦ x ≦ −1')}。　<b>完成！</b>`]});

/* ===== まとめ（アニメーションなし） ===== */
const MG2 = (out) => {
  const W=320, H=150, ay=out?95:60, r1=out?120:130, r2=out?200:190, m=(r1+r2)/2, k=out?0.022:0.05;
  const Y = x => ay - k*(x-r1)*(x-r2), top=8, c0=(m-r1)*(m-r2), hw=Math.sqrt((ay-top)/k - c0);
  const P = (a,b) => { let d=''; for(let i=0;i<=40;i++){ const x=a+(b-a)*i/40; d+=(i?'L':'M')+x.toFixed(1)+' '+Y(x).toFixed(1)+' '; } return d; };
  const seg = out ? P(m-hw,r1)+P(r2,m+hw) : P(r1,r2);
  return `<svg class="imsv" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><line x1="16" y1="${ay}" x2="${W-18}" y2="${ay}"/><polygon points="${W-6},${ay} ${W-20},${ay-7} ${W-20},${ay+7}"/>
    <path class="mc" d="${P(m-hw,m+hw)}"/><path class="mp" d="${seg}"/>${[r1,r2].map(x=>`<circle class="${out?'op':''}" cx="${x}" cy="${ay}" r="8"/>`).join('')}
    <text x="${r1}" y="${ay+30}" text-anchor="middle">${out?'−1':'−2'}</text><text x="${r2}" y="${ay+30}" text-anchor="middle">${out?'3':'−1'}</text></svg>`; };
const s10 = `
  <div class="end-h"><h2>2次不等式の 答え方</h2></div>
  <div class="dsum">
    <div class="card dsc isc c1">${MG2(true)}<div class="dsc-s math">${EQ1}</div><div class="isr">＞ → <b>鳥</b> ${ICON('bird')} 上を 塗る → <b>外側</b> 2本</div><div class="dsc-n math">x ＜ −1, 3 ＜ x</div></div>
    <div class="card dsc isc c2">${MG2(false)}<div class="dsc-s math">${EQ2}</div><div class="isr">≦ → <b>魚</b> ${ICON('fish')} 下を 塗る → <b>内側</b> 1本</div><div class="dsc-n math">−2 ≦ x ≦ −1</div></div>
  </div>
  ${cbar([`＝ が ない（＞、＜）→ <b>白丸</b>・答えも <b>＜</b>。　＝ が ある（≧、≦）→ <b>黒丸</b>・答えも <b>≦</b>。　並びは 数直線と 同じ 左 → 右。`])}`;

