/* ====== ２学期期末考査まで：共通の小道具 ====== */
const KIMATSU = '数学Ⅰ　２学期期末考査まで';
/* 表紙・おわりの 写真の中身：式が 変わる様子 */
const fpol = (a,b,msg) => `<div class="fpol"><div class="fa math">${a}</div><div class="fv">↓ ${msg}</div><div class="fb math">${b}</div></div>`;
const coverF = (kicker,title,sub,sub2,pol,cap) => `
<div class="card abs cover">${TP('pink','left:-26px;top:-4px;transform:rotate(-38deg)')}${TP('mint','right:-26px;bottom:-4px;transform:rotate(-38deg)')}
  <div class="kicker">${kicker}</div>
  <h1>${title}</h1>
  <div class="r" data-s="1"><div class="sub">${sub}</div></div>
  <div class="r" data-s="2"><div class="sub2">${sub2}</div></div>
  ${typeof VER!=='undefined' ? `<div class="ver">${VER}</div>` : ''}
</div>
<div class="card abs polaroid">${TP('yellow','left:92px;top:-14px;transform:rotate(-3deg)')}${pol}<div class="cap">${cap}</div></div>`;
const endF = (kicker,pol,cap='よくできました') => `
<div class="card abs cover" style="height:380px;top:150px">${TP('lav','left:-26px;top:-4px;transform:rotate(-38deg)')}${TP('yellow','right:-26px;top:-4px;transform:rotate(38deg)')}
  <div class="kicker">${kicker}</div>
  <h1>おつかれさま<br><span class="mk">でした！</span></h1>
</div>
<div class="card abs polaroid">${TP('pink','left:92px;top:-14px;transform:rotate(3deg)')}${pol}<div class="cap">${cap}</div></div>`;

/* ====== 因数分解：4つのパターン ====== */
/* 文字の公式は 使わず、実際の式＋色の数＋キーワード で 見せる */
const KW = t => `<span class="kw">${t}</span>`;
/* 色だけ つける（枠なし）：b 青、g 緑、r 赤 */
const CT = (k,t) => `<span class="ct-${k}">${t}</span>`;
const PAT = [
  {no:'⑴', name:'たして・かけて',
   expr:`x${P2} ${CT('b','＋ 2')}x ${CT('g','− 15')}`, res:`(x ＋ 5)(x − 3)`,
   kw:`${CT('b','たして ＋2')}　${CT('g','かけて −15')}`},
  {no:'⑵', name:'2乗 − 2乗',
   expr:`x${P2} ${CT('g','− 9')}`, res:`(x ＋ 3)(x − 3)`,
   kw:`x の項が ない　${CT('g','9 ＝ 3²')}`},
  {no:'⑶', name:'同じ (　) が 2つ',
   expr:`x${P2} ${CT('b','＋ 6')}x ${CT('g','＋ 9')}`, res:`(x ＋ 3)${P2}`,
   kw:`${CT('b','たして ＋6')}　${CT('g','かけて ＋9')}　→ 2乗で まとめる`},
  {no:'⑷', name:'共通因数で くくる',
   expr:`${CT('r','x')}${P2} ＋ 6${CT('r','x')}`, res:`${CT('r','x')}(x ＋ 6)`,
   kw:`数だけの項が ない　${CT('r','x')} で くくる`}
];
/* 4つのパターンを 一覧で 見せる（アニメーションなし） */
function patOverview(title, cms){
  const tp = ['pink','mint','yellow','lav'];
  const card = (p,i) => `<div class="pcw p${i+1}"><div class="card pc">${TP(tp[i],'left:50%;margin-left:-58px;top:-14px;transform:rotate(-2deg)')}
      <div class="pc-h"><span class="pc-no">${p.no}</span>${p.name}</div>
      <div class="pc-f math">${p.expr} ＝ ${p.res}</div>
      <div class="pc-k">${p.kw}</div></div></div>`;
  return `<div class="end-h"><h2>${title}</h2></div>
  <div class="pcards">${PAT.map(card).join('')}</div>
  ${cbar(cms)}`;
}

/* ====== 因数分解の 1問 ======
   左：式の変形（もとの式 → 答え）、右：考え方（大きく見せる）、下：ことばの説明 */
const frow = (s,eq,body) =>
  `<div class="fxr${s===null?'':' lh'}"${s===null?'':` data-s="${s}"`}><span class="eqs">${eq}</span><span class="bd">${body}</span></div>`;
const tgoal = (s,html) => `<div class="tg lh" data-s="${s}">${html}</div>`;
/* 考え方の 1段。n：番号、label：何をするか、big：大きく見せる式、sub：補足
   s を [問いの番, 答えの番] にすると、問いを先に出し、次のクリックで答えを出す */
const tstep = (s,n,label,big,sub='') => {
  const [sl,sb] = Array.isArray(s) ? s : [s,s];
  return `<div class="ts lh" data-s="${sl}"><div class="ts-n">${n}</div><div><div class="ts-l">${label}</div><div class="ts-m math lh" data-s="${sb}">${big}</div>${sub?`<div class="ts-s">${sub}</div>`:''}</div></div>`;
};
function fxSlide({num,pat,rows,thinkLab,think,cm,done}){
  const p = PAT[pat];
  return `
  <div class="pno">${num}</div>
  <div class="card abs fxcard">${EQTAPE}<div class="fxpat">${p.no} ${p.name}</div><div class="fxrows math">${rows}</div></div>
  <div class="card abs think">${TP('yellow','right:30px;top:-14px;transform:rotate(4deg)')}<div class="lab">${thinkLab}</div>${think}</div>
  <div class="abs r done fxdone" data-s="${done}"><div class="seal">完成！</div></div>
  ${cbar(cm)}`;
}

/* 分数（neg：マイナスを 前に つける） */
const FR = (n,d,neg) => `${neg?'−':''}<span class="fr"><span>${n}</span><span>${d}</span></span>`;

/* ====== 2次方程式（因数分解で解く）の 1問 ======
   プリントと同じ形：もとの式 → 青と橙の ( ) ＝ 0 → それぞれ ＝ 0 → x ＝
   P = {num, eq, fb, fo, wb, wo, bl, ol, ab, ao, jyu, merge, point, ofirst, tall, cm}
   bl/ol = {a:'x', t:'＋ 5', v:'−5'}：「x ＋ 5 ＝ 0」→ クリックで 移項の矢印と「x ＝ −5」。t が なければ「x ＝ v」の 1行
   d:'2', f:FR(…) を つけると 3行目「x ＝ f」（両辺 ÷ d）を足す（①-3）
   答えの数は 答えの枠へ 飛んでいく */
/* 矢印（線＋先の三角） */
function qArrow(x1,y1,x2,y2,c){
  const a=Math.atan2(y2-y1,x2-x1), L=14, W=7, bx=x2-L*Math.cos(a), by=y2-L*Math.sin(a);
  const p=[[x2,y2],[bx-W*Math.sin(a),by+W*Math.cos(a)],[bx+W*Math.sin(a),by-W*Math.cos(a)]].map(q=>q.map(v=>v.toFixed(1)).join(',')).join(' ');
  return `<line x1="${x1}" y1="${y1}" x2="${bx.toFixed(1)}" y2="${by.toFixed(1)}" stroke="${c}"/><polygon points="${p}" fill="${c}"/>`;
}
function eqSlide(P){
  let n = 0; const st = {lab: ++n, fac: ++n};   // 矢印「因数分解」→ もう一回 クリックで 式
  if(P.point) st.pt = ++n;
  const ns = B => B.t ? (B.d ? [++n, ++n, ++n] : [++n, ++n]) : [++n];
  if(P.ofirst){ st.o = ns(P.ol); st.b = ns(P.bl); }   // ⑷：( ) の方から 先に
  else        { st.b = ns(P.bl); st.o = ns(P.ol); }
  st.ans = ++n;
  if(P.merge) st.mg = ++n;          // ⑶：同じ答えを 1つに まとめる
  if(P.jyu) st.jyu = ++n;
  const done = P.jyu ? st.jyu : st.ans;
  const L = 48, BX = 48, BW = P.tall ? 290 : 280, OX = P.tall ? BX + BW + 16 : 352;
  const bx = L + P.wb/2, ox = L + P.wb + P.wo/2;
  /* 箱の中：「x ＋ 5 ＝ 0」→ 移項の矢印が のびてから「x ＝ −5」（＝ の位置を そろえた 2行） */
  const box = (B,ss,k) => {
    const ln = (s,l,r,cls='') => [l,'＝',r].map((h,i)=>`<span class="qc${i} lh${cls}" data-s="${s}">${h}</span>`).join('');
    const val = `<span${k?` data-k="${k}"`:''}>${B.v}</span>`;
    if(!B.t) return `<div class="qlines">${ln(ss[0],B.a,val)}</div>`;
    const v2 = B.d ? B.v : val;
    const l3 = B.d ? ln(ss[2],'x',`<span data-k="${k}">${B.f}</span><span class="qdiv">÷${B.d}</span>`) : '';
    return `<div class="qlines">${ln(ss[0],`${B.a} ${tm('r',`<span class="mvt">${B.t}</span>`,ss[1])}`,'0')}${ln(ss[1],B.a,tm('r',`<span class="mvv">${v2}</span>`,ss[1]),' late')}${l3}</div>`
         + `<svg class="mva"><g class="gs" data-s="${ss[1]}"><path pathLength="1" d=""/><polygon points=""/></g></svg>`;
  };
  const ans = P.merge
    ? `${slotC('b',P.ab,st.ans,'ab')}<span class="qdup" data-o="${st.mg}"><span class="qcm">,</span>${slotC('o',P.ao,st.ans,'ao')}</span>`
    : P.ao
    ? `${slotC('b',P.ab,st.ans,'ab')}<span class="qcm">,</span>${slotC('o',P.ao,st.ans,'ao')}`
    : slotC('b',P.ab,st.ans,'ab');
  return `
  <div class="pno">${P.num}</div>
  <div class="card abs qecard${P.tall?' qtall':''}">${EQTAPE}
    <div class="q0 math">${P.eq}</div>
    <div class="qlab" style="left:${L+P.wb+P.wo+100}px"><svg class="gs" data-s="${st.lab}" width="46" height="76" viewBox="0 0 46 76"><path pathLength="1" d="M10 6 C44 14,44 52,18 64" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/><polygon points="6,68 26,72 17,52" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg><span class="lh" data-s="${st.lab}">因数分解</span></div>
    <div class="q1 math lh" data-s="${st.fac}"><span class="qf qf-b" style="width:${P.wb}px"><span>${P.fb}</span></span><span class="qf qf-o" style="width:${P.wo}px"><span>${P.fo}</span></span><span class="qz">＝ 0</span></div>
    <svg class="qarr" width="700" height="60" viewBox="0 0 700 60">
      <g class="gs" data-s="${st.b[0]}">${qArrow(bx,4,bx,56,'var(--b-ink)')}</g>
      <g class="gs" data-s="${st.o[0]}">${qArrow(ox,4,OX+BW/2,56,'var(--o-ink)')}</g>
    </svg>
    <div class="qb qb-b math lh" data-s="${st.b[0]}" style="left:${BX}px;width:${BW}px">${box(P.bl,st.b,'ab')}</div>
    <div class="qb qb-o math lh" data-s="${st.o[0]}" style="left:${OX}px;width:${BW}px">${box(P.ol,st.o,'ao')}</div>
    <div class="q3 math"><span class="qx">x ＝</span><span class="qa">${ans}</span>${P.jyu?`<span class="qjyu lh" data-s="${st.jyu}">重解</span>`:''}</div>
    <div class="qpt${P.point?' lh':''}"${P.point?` data-s="${st.pt}"`:''}>${TP('yellow','right:20px;top:-14px;transform:rotate(4deg)')}<div class="lab">ポイント</div>
      <div class="qpt-m math"><span class="qs qs-b"></span> × <span class="qs qs-o"></span> ＝ 0</div>
      <div class="qpt-t">→ どちらかが 0</div>
    </div>
  </div>
  <div class="abs r done qdone" data-s="${done}"><div class="seal">完成！</div></div>
  ${cbar(P.cm)}`;
}

/* 移項の矢印を、＋5 の下から −5 の上へ かく（engine.js の relayout から 呼ばれる） */
function layoutExtra(root){
  root.querySelectorAll('.qb').forEach(b=>{
    const t=b.querySelector('.mvt'), v=b.querySelector('.mvv'), g=b.querySelector('.mva g');
    if(!t||!v||!g) return;
    const [bx,by]=pos(b), r=e=>{ const [x,y]=pos(e); return [x-bx,y-by,e.offsetWidth,e.offsetHeight]; };
    const [tx,ty,tw,th]=r(t.closest('.tm')), [vx,vy,vw]=r(v.closest('.tm'));
    const x1=tx+tw/2, y1=ty+th+2, x2=vx+vw/2, y2=vy-2, d=(y2-y1)*.9;
    g.querySelector('path').setAttribute('d',`M${x1} ${y1} C${x1} ${y1+d} ${x2} ${y2-d} ${x2} ${y2-10}`);
    g.querySelector('polygon').setAttribute('points',`${x2-7},${y2-12} ${x2+7},${y2-12} ${x2},${y2}`);
  });
}

/* ====== 解の公式（①-4）：プリントの 枠の 位置を そのまま 拡大して 再現する ======
   座標は プリント（PDF）の pt。 KS 倍して、問題番号の 行を 原点に する。
   生徒は プリントに 書きこむので、枠の 位置・形は 変えない。 */
const KS = 2.05, KX0 = 62, KL = 24, KT = 18;
const kpos = (y0) => (x1,y1,x2,y2) => `left:${(KL+(x1-KX0)*KS).toFixed(1)}px;top:${(KT+(y1-y0)*KS).toFixed(1)}px;width:${((x2-x1)*KS).toFixed(1)}px;height:${((y2-y1)*KS).toFixed(1)}px`;
/* ルート：√ を SVG で かいて、上の 線と つなげる（文字の √ だと 線と ずれる） */
const SQ = t => `<span class="rt"><svg class="rts" viewBox="0 0 10 20" preserveAspectRatio="none"><path d="M0.6 12.4 L2.6 11.2 L5.4 19.4 L9.6 0.6 L10 0.6"/></svg><span class="ov">${t}</span></span>`;
/* 解の公式（色つき）：a 赤、b 緑、c 青 */
const KA = t => `<span class="ka">${t}</span>`, KB = t => `<span class="kb">${t}</span>`, KC = t => `<span class="kc">${t}</span>`;
const FORMULA = (big) => `<span class="kfx math${big?' big':''}">x ＝ <span class="kfr"><span>−${KB('b')} ± ${SQ(`${KB('b')}${P2} − 4${KA('a')}${KC('c')}`)}</span><span>2${KA('a')}</span></span></span>`;

/* 1問。P = {num, eq, abc, y0, b1:[-b], b2:[b²], b3:[-4ac], calc, b4:[2a], row2:[…], cm}
   各 枠は [出る番, 中身]。row2 は 下の段（プリントの 問題ごとに 形が ちがう）
   notes：[[番, ⑴ の座標 [x1,y1,x2,y2], 中身]]（枠の 近くの 小さな 計算メモ） */
function kfSlide(P){
  const at = kpos(P.y0);
  const wrap = h => /^<div class="khf"/.test(h) ? h : `<span class="kwr">${h}</span>`;
  const bx = (cls,r,[s,h],x='') => `<div class="kb0 ${cls}" style="${at(...r)}"${x}>${h!==undefined?`<div class="kin lh" data-s="${s}">${wrap(h)}</div>`:''}</div>`;
  const tx = (r,h,cls='') => `<div class="ktx ${cls}" style="${at(...r)}"><span class="kwr">${h}</span></div>`;
  const Y = P.y0, d = y => y - 210.2 + Y;          // ⑴ の 位置を 基準に、問題ごとの ずれ
  // ルート記号と 分数の線（SVG、pt → px）
  const X = x => (KL+(x-KX0)*KS).toFixed(1), YY = y => (KT+(y-Y)*KS).toFixed(1);
  const svg = `<svg class="ksv" width="1184" height="490">
    <polyline points="${X(176)},${YY(d(252))} ${X(180)},${YY(d(249.5))} ${X(184.5)},${YY(d(262))} ${X(189)},${YY(d(238.2))} ${X(290.3)},${YY(d(238.2))}" fill="none" stroke="var(--ink)" stroke-width="2.4" stroke-linejoin="round"/>
    <line x1="${X(112.5)}" y1="${YY(d(271.1))}" x2="${X(300.4)}" y2="${YY(d(271.1))}" stroke="var(--ink)" stroke-width="2.4"/>
    ${(P.lines||[]).map(([x1,y,x2])=>`<line x1="${X(x1)}" y1="${YY(y)}" x2="${X(x2)}" y2="${YY(y)}" stroke="var(--ink)" stroke-width="2"/>`).join('')}
    ${(P.arrows||[]).map(([x1,y1,x2,y2])=>`<g class="gs" data-s="${P.arrowS}">${qArrow(+X(x1),+YY(y1),+X(x2),+YY(y2),'var(--note)')}</g>`).join('')}
  </svg>`;
  return `
  <div class="card abs kcard">
    ${tx([KX0,Y,340,Y+14.4],`${P.num}　${P.eq}`,'ktitle math')}
    <div class="kabc lh" data-s="${P.abc[0]}" style="${at(230,Y-2,520,Y+16)}">${P.abc[1]}</div>
    ${tx([76,d(261.1),112,d(281.1)],'x ＝','kxe math')}
    ${tx([157.2,d(241.7),176,d(268.7)],'±','kpm math')}
    ${bx('kpb',[113.7,d(241.7),157.2,d(268.7)],P.b1)}
    ${bx('kpb',[186.5,d(241.7),229.9,d(268.7)],P.b2)}
    ${bx('kpr',[229.2,d(241.7),285.4,d(268.7)],P.b3)}
    ${bx('kpb',[179.9,d(273.7),239.2,d(300.6)],P.b4)}
    ${tx([350.4,d(225.7),460,d(235.7)],'−4ac の計算','klab')}
    ${(P.notes||[]).map(([s,r,h])=>`<div class="knote lh" data-s="${s}" style="${at(r[0],d(r[1]),r[2],d(r[3]))}"><span class="kwr">${h}</span></div>`).join('')}
    ${bx('kpr kcalc',[350.5,d(240.6),465.2,d(267.5)],P.calc)}
    ${P.row2.map(r=>r.t ? tx(r.r,r.t,'kxe math') : bx(r.c,r.r,r.v)).join('')}
    ${svg}
    <div class="kref">${TP('lav','right:20px;top:-14px;transform:rotate(-4deg)')}<div class="lab">解の公式</div>${FORMULA()}</div>
  </div>
  <div class="abs r done kdone" data-s="${P.done}"><div class="seal">完成！</div></div>
  ${cbar(P.cm)}`;
}
/* 分数（枠の中：上と下に 分けて 書く） */
const KF = (n,dn) => `<span class="kfr"><span>${n}</span><span>${dn}</span></span>`;
/* 枠の中を 上下に 分けて 書く（プリントに 分数の線が 印刷されている 枠） */
const KH = (n,dn) => `<div class="khf"><span>${n}</span><span>${dn}</span></div>`;

/* ====== プリントの 画像を 背景に 置き、空らんに 答えを 出す（①-6〜③-4） ======
   P = {img, clip:[x1,y1,x2,y2]（PDF の pt）, items:[…], svg:[…], cm, done}
   items：{s:番, r:[x1,y1,x2,y2], h:'中身', fs:文字の大きさ(pt), al:'l'|'c'}　空らんの 答え
          {m:番, e:消える番, r:[…]}　マーカー（強調の わく）
   svg  ：PB(…) などの 文字列（座標は PDF の pt のまま） */
function pgSlide(P){
  const [cx1,cy1,cx2,cy2] = P.clip, w = cx2-cx1, h = cy2-cy1;
  const s = Math.min(1150/w, 466/h, P.max||2.6);
  const W = w*s, H = h*s, L = (1184-W)/2, T = (490-H)/2;
  const X = x => (L+(x-cx1)*s).toFixed(1), Y = y => (T+(y-cy1)*s).toFixed(1);
  const R = r => `left:${X(r[0])}px;top:${Y(r[1])}px;width:${((r[2]-r[0])*s).toFixed(1)}px;height:${((r[3]-r[1])*s).toFixed(1)}px`;
  const it = P.items.map(o => o.m!==undefined
    ? `<div class="pgm"${o.e?` data-wa="${o.m}" data-wb="${o.e}"`:` data-wa="${o.m}" data-wb="99"`} style="${R(o.r)}"></div>`
    : `<div class="pga ${o.al==='l'?'al':''} lh" data-s="${o.s}" style="${R(o.r)};font-size:${((o.fs||11)*s).toFixed(1)}px"><span class="kwr">${o.h}</span></div>`).join('');
  return `
  <div class="card abs pgcard">
    <img class="pgimg" src="${P.img}" style="left:${L.toFixed(1)}px;top:${T.toFixed(1)}px;width:${W.toFixed(1)}px;height:${H.toFixed(1)}px" alt="">
    <svg class="pgsv" style="left:${L.toFixed(1)}px;top:${T.toFixed(1)}px" width="${W.toFixed(1)}" height="${H.toFixed(1)}" viewBox="${cx1} ${cy1} ${w} ${h}">${(P.svg||[]).join('')}</svg>
    ${it}
  </div>
  ${P.done ? `<div class="abs r done pgdone" data-s="${P.done}"><div class="seal">完成！</div></div>` : ''}
  ${cbar(P.cm)}`;
}
/* 放物線（PDF の pt で）：y ＝ yv − q (x − xv)²（下に凸。画面では 上に 開く）
   o = {xv, yv, q, ay:x軸の y, top:かき始める y, s:かく番, lab:[[x,'文字'],…], dot:'o'|'f'|null, ds:点の番,
        paint:'up'|'down'|'all'|'up0'|null, ps:塗る番, draw:false（すでに 印刷されている 線に 塗るだけ）} */
function PB(o){
  const xh = Math.sqrt(Math.max(0,(o.yv-o.top)/o.q));
  const f = x => o.yv - o.q*(x-o.xv)**2;
  const path = (a,b) => { let d=''; const n=60; for(let i=0;i<=n;i++){ const x=a+(b-a)*i/n; d+=(i?'L':'M')+x.toFixed(2)+' '+f(x).toFixed(2)+' '; } return d; };
  const x1 = o.xv-xh, x2 = o.xv+xh;
  const rr = o.yv>o.ay+0.01 ? Math.sqrt((o.yv-o.ay)/o.q) : (Math.abs(o.yv-o.ay)<0.01 ? 0 : null);
  const roots = rr===null ? [] : rr===0 ? [o.xv] : [o.xv-rr, o.xv+rr];
  let s = '';
  if(o.draw!==false) s += `<path class="curve pgc" data-s="${o.s}" pathLength="1" d="${path(x1,x2)}"/>`;
  if(o.paint){
    let seg = [];
    if(o.paint==='all' || o.paint==='up0' || (o.paint==='up' && roots.length<2)) seg = [[x1,x2]];
    else if(o.paint==='up') seg = [[x1,roots[0]],[roots[1],x2]];
    else if(o.paint==='down' && roots.length===2) seg = [[roots[0],roots[1]]];
    s += `<g class="gs" data-s="${o.ps}">${seg.map(([a,b])=>`<path class="pgp" d="${path(a,b)}"/>`).join('')}</g>`;
  }
  if(o.dot) s += `<g class="gs" data-s="${o.ds??o.s}">${roots.map(x=>`<circle class="pgd ${o.dot==='o'?'op':''}" cx="${x.toFixed(2)}" cy="${o.ay}" r="2.6"/>`).join('')}</g>`;
  if(o.lab) s += `<g class="gs" data-s="${o.ls??o.s}">${o.lab.map(([x,t])=>`<text class="pgt" x="${x}" y="${o.ay+9}" text-anchor="middle">${t}</text>`).join('')}</g>`;
  return s;
}

/* ====== プリントの 配置どおりに 部品で 組み立てる（画像は 使わない） ======
   P = {clip:[x1,y1,x2,y2]（PDF の pt）, items:[{s:番, r:[x1,y1,x2,y2], h, fs:pt, cls, al}], svg:[…], cm, done}
   s が ない item は 最初から 出ている（プリントに 印刷されている 部分） */
function ptSlide(P){
  const [cx1,cy1,cx2,cy2] = P.clip, w = cx2-cx1, h = cy2-cy1;
  const s = Math.min(1150/w, 466/h, P.max||2.8);
  const W = w*s, H = h*s, L = (1184-W)/2, T = (490-H)/2;
  const X = x => (L+(x-cx1)*s).toFixed(1), Y = y => (T+(y-cy1)*s).toFixed(1);
  const R = r => `left:${X(r[0])}px;top:${Y(r[1])}px;width:${((r[2]-r[0])*s).toFixed(1)}px;height:${((r[3]-r[1])*s).toFixed(1)}px`;
  const it = P.items.map(o => o.m!==undefined
    ? `<div class="pgm" data-wa="${o.m}" data-wb="${o.e||99}" style="${R(o.r)}"></div>`
    : `<div class="pte ${o.cls||''} ${o.al==='c'?'ac':''}${o.s!==undefined?' lh':''}"${o.s!==undefined?` data-s="${o.s}"`:''} style="${R(o.r)};font-size:${((o.fs||10.5)*s).toFixed(1)}px"><span class="kwr">${o.h}</span></div>`).join('');
  return `
  <div class="card abs ptcard">
    <svg class="pgsv" style="left:${L.toFixed(1)}px;top:${T.toFixed(1)}px" width="${W.toFixed(1)}" height="${H.toFixed(1)}" viewBox="${cx1} ${cy1} ${w} ${h}">${(P.svg||[]).join('')}</svg>
    ${it}
  </div>
  ${P.done ? `<div class="abs r done pgdone" data-s="${P.done}"><div class="seal">完成！</div></div>` : ''}
  ${cbar(P.cm)}`;
}
/* プリントの 緑の 太い 矢印（pt） */
const GARW = (x1,y1,x2,y2,s) => { const ym=(y1+y2)/2, hh=(y2-y1)*.28, hx=x2-(y2-y1)*.55;
  return `<g class="gs" data-s="${s}"><polygon points="${x1},${ym-hh} ${hx},${ym-hh} ${hx},${y1} ${x2},${ym} ${hx},${y2} ${hx},${ym+hh} ${x1},${ym+hh}" fill="#c9dca6"/></g>`; };

/* ====== プリント問題（例の あと）：見出しの ページと、問題の ページの 印（2026-10-28） ======
   probHead('プリント問題①-4', '次の 2次方程式を 解け。', ['⑴ …', …])：問題の 一覧の ページ（アニメーション なし）
   ptag('プリント問題①-4')：問題の ページの 左上（番号の 丸の 横）に 付ける 印 */
const probHead = (title, lead, list, cap) => `
  <div class="card abs ncard phcard">${EQTAPE}
    <div class="ph-k">例の 次は</div>
    <div class="ph-h">◎${title}</div>
    <div class="ph-t">${lead}</div>
    <div class="ph-l math">${list.map(x=>`<span>${x}</span>`).join('')}</div>
  </div>
  ${cbar([cap || `ここから <b>${title}</b>。　例と 同じ 手順で 解いて いこう！　まず 自分で 解いてから 見てね。`])}`;
const ptag = t => `<div class="ptag">${t}</div>`;
