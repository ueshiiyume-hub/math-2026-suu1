/* ====== 小道具 ====== */
const K  = (k,t) => `<span class="cc cc-${k} sm">${t}</span>`;
const M  = t => `<span class="math">${t}</span>`;
const S  = (n,html,cls='') => `<span class="r ${cls}" data-s="${n}">${html}</span>`;
const tm = (k,t,o,x='') => `<span class="tm tm-${k}" data-o="${o}"${x}>${t}</span>`;
const TP = (c,css) => `<span class="tape t-${c}" style="${css}"></span>`;
const ab = Math.abs;
const fmt = n => n<0 ? '−'+ab(n) : String(n);
const sgn = n => (n<0 ? '− ' : '＋ ') + ab(n);
const sf  = n => (n<0 ? '−' : '＋') + ab(n);
const P2='<sup>2</sup>', X2='x<sup>2</sup>';
const slotC = (k,txt,f,src) => `<span class="slot slot-${k}"><span class="tm tm-${k} on fly" data-f="${f}" data-src="${src}">${txt}</span></span>`;
const cbar = list => `<div class="card abs cbar">${TP('mint','left:-30px;top:2px;transform:rotate(-38deg)')}${TP('mint','right:-30px;top:2px;transform:rotate(38deg)')}<div class="lab">いま やっていること</div>${list.map((c,i)=>`<div class="cm" data-m="${i}">${c}</div>`).join('')}</div>`;
const SEAL = s => `<div class="abs r done" data-s="${s}" style="left:1146px;top:456px"><div class="seal">完成！</div></div>`;
/* ax²＋bx＋c を 文字列に */
function polyStr(a,b,c){
  let s = `${a===1?'':a===-1?'−':fmt(a)}x${P2}`;
  if(b) s += ` ${b<0?'−':'＋'} ${ab(b)===1?'':ab(b)}x`;
  if(c) s += ` ${c<0?'−':'＋'} ${ab(c)}`;
  return s;
}

/* ====== グラフ（SVG） ====== */
const GW=410, GH=460;
function graphSVG(P,st){
  const {a,p,q,x1,y1}=P;
  const xs=[p-2,p+2,0,x1], ys=[q,y1,0,q+Math.sign(a)*Math.min(ab(a)*4,6)];
  const xmin=Math.min(...xs)-.9, xmax=Math.max(...xs)+.9, ymin=Math.min(...ys)-.9, ymax=Math.max(...ys)+.9;
  const u=Math.min(GW/(xmax-xmin), GH/(ymax-ymin), 48);
  const ox=GW/2-u*(xmin+xmax)/2, oy=GH/2+u*(ymin+ymax)/2;
  const X=x=>+(ox+u*x).toFixed(1), Y=y=>+(oy-u*y).toFixed(1);
  const vx0=-ox/u, vx1=(GW-ox)/u, vy0=(oy-GH)/u, vy1=oy/u;
  let s='';
  for(let i=Math.ceil(vx0);i<=Math.floor(vx1);i++) s+=`<line class="gg" x1="${X(i)}" y1="0" x2="${X(i)}" y2="${GH}"/>`;
  for(let j=Math.ceil(vy0);j<=Math.floor(vy1);j++) s+=`<line class="gg" x1="0" y1="${Y(j)}" x2="${GW}" y2="${Y(j)}"/>`;
  /* 座標軸 */
  s+=`<line class="ax" x1="2" y1="${Y(0)}" x2="${GW-4}" y2="${Y(0)}"/><polygon class="axh" points="${GW+2},${Y(0)} ${GW-11},${Y(0)-6} ${GW-11},${Y(0)+6}"/>`;
  s+=`<line class="ax" x1="${X(0)}" y1="${GH-2}" x2="${X(0)}" y2="6"/><polygon class="axh" points="${X(0)},0 ${X(0)-6},13 ${X(0)+6},13"/>`;
  s+=`<text class="gt it" x="${GW-6}" y="${Y(0)+24}">x</text><text class="gt it" x="${X(0)+10}" y="16">y</text><text class="gt it" x="${X(0)-18}" y="${Y(0)+20}">O</text>`;
  for(let i=Math.ceil(vx0);i<=Math.floor(vx1);i++) if(i) s+=`<line class="tk" x1="${X(i)}" y1="${Y(0)-4}" x2="${X(i)}" y2="${Y(0)+4}"/>`;
  for(let j=Math.ceil(vy0);j<=Math.floor(vy1);j++) if(j) s+=`<line class="tk" x1="${X(0)-4}" y1="${Y(j)}" x2="${X(0)+4}" y2="${Y(j)}"/>`;
  /* 放物線 */
  const yedge = a>0 ? vy1-.15 : vy0+.15;
  const d = Math.min(Math.sqrt((yedge-q)/a), p-vx0-.1, vx1-p-.1);
  let path=''; for(let i=0;i<=80;i++){ const x=p-d+2*d*i/80; path+=(i?'L':'M')+X(x)+' '+Y(a*(x-p)**2+q)+' '; }
  s+=`<path class="curve" data-s="${st.cu}" pathLength="1" d="${path}"/>`;
  /* 頂点（原点のときはラベルなし） */
  const vlab = a>0 ? Y(q)+30 : Y(q)-16;
  if(p||q) s+=`<g class="gs" data-s="${st.pv}"><text class="gt k halo" x="${X(p)+(p<=0?-6:6)}" y="${vlab}" text-anchor="${p<=0?'end':'start'}">(${fmt(p)}, ${fmt(q)})</text></g>`;
  s+=`<g class="pt" data-s="${st.pv}"><circle cx="${X(p)}" cy="${Y(q)}" r="7"/></g>`;
  /* もう1点 */
  if(!P.noPt){
    const [an,dx] = x1>=p ? ['start',11] : ['end',-11];
    s+=`<g class="gs" data-s="${st.ptg}"><text class="gt k halo" x="${X(x1)+dx}" y="${y1===0?Y(y1)-12:Y(y1)+7}" text-anchor="${an}">(${fmt(x1)}, ${fmt(y1)})</text></g>`;
    s+=`<g class="pt" data-s="${st.ptg}"><circle cx="${X(x1)}" cy="${Y(y1)}" r="6"/></g>`;
  }
  if(P.extra) s+=P.extra({X,Y,d,u});
  return `<svg class="graph" width="${GW}" height="${GH}" viewBox="0 0 ${GW} ${GH}">${s}</svg>`;
}

/* ====== 式の読みとり（形・横・縦） ====== */
function readEq(P,st){
  const {a,p,q}=P;
  const aS = a===1 ? '' : a===-1 ? '−' : fmt(a);
  const qT = q===0 ? '' : ` ${q<0?'−':'＋'} ${ab(q)}`;
  const body = p===0 ? `x${P2}` : `(x ${p<0?'＋':'−'} ${ab(p)})${P2}`;
  const eqTxt = `y ＝ ${aS}${body}${qT}`;
  const up = a>0, dir = up ? '下に凸' : '上に凸';
  const aC = a===1 ? 'なし' : a===-1 ? '−' : fmt(a);
  const pC = p===0 ? 'なし' : p<0 ? `＋${-p}` : `−${p}`;
  const qC = q===0 ? 'なし' : `${q<0?'−':'＋'}${ab(q)}`;
  const V = `(${fmt(p)}, ${fmt(q)})`;
  const cm = [
    `基本の形 ${M('y ＝ a(x − p)² ＋ q')} と 見くらべよう。　${K('r',aC)} が <b>形</b>、${K('o',pC)} が <b>横</b>、${K('g',qC)} が <b>縦</b> だよ。`,
    a===1  ? `<b>形</b> は x² の前に 何も 書いていない ので <b>1</b>、つまり <b>＋</b>。　だから グラフの 向きは <b>${dir}</b>。`
    : a===-1 ? `<b>形</b> は ${K('r','−')}（−1 の 1 が 省略されている）。　だから グラフの 向きは <b>${dir}</b>。`
    : `<b>形</b> の ${K('r',aC)} は ${up?'＋':'−'}。　だから グラフの 向きは <b>${dir}</b>。`,
    p===0 ? `<b>横</b> の かっこ が ない ので、頂点の <b>x座標</b> は <b>0</b>。`
          : `<b>横</b> の ${K('o',pC)} は 頂点の <b>x座標</b>。　<b>プラスマイナスが逆転</b> して → <b>${fmt(p)}</b>`,
    q===0 ? `<b>縦</b> の 数 が ない ので、頂点の <b>y座標</b> は <b>0</b>。　　頂点は ${M(V)}。`
          : `<b>縦</b> の ${K('g',qC)} は 頂点の <b>y座標</b>。　<b>そのまま</b> → <b>${fmt(q)}</b>　　頂点は ${M(V)}。`
  ];
  const lb = (s,cls,t) => `<span class="lbl ${cls}"><span class="lh" data-s="${s}">${t}</span></span>`;
  const top = (cls,t) => lb(st.col,`up ${cls}`,t);
  const gtm = (k,o,x='') => `<span class="tm tm-${k} ghost" data-o="${o}"${x}>&nbsp;</span>`;
  const aPart = `<span class="hasl"${p===0?' style="margin-right:20px"':''}>${aS?tm('r',aS,st.col,' data-k="a"'):gtm('r',st.col,' data-k="a"')}${top('lr','形')}${lb(st.dir,'lr',(up?(a===1?'1 →':'＋ →'):'− →')+'<br>'+dir)}</span>`;
  const pPart = p===0
    ? `<span class="hasl">${tm('o',`x${P2}`,st.col,' data-k="p"')}${top('lo','横')}${lb(st.vx,'lo','なし<br>→ 0')}</span>`
    : `( x <span class="hasl">${tm('o',sgn(-p),st.col,' data-k="p"')}${top('lo','横')}${lb(st.vx,'lo','±逆転<br>→ '+fmt(p))}</span> )${P2}`;
  const qPart = `<span class="hasl" style="margin-left:${p===0?20:6}px">${q===0?gtm('g',st.col,' data-k="q"'):tm('g',sgn(q),st.col,' data-k="q"')}${top('lg','縦')}${lb(st.vy,'lg',q===0?'なし<br>→ 0':'そのまま<br>→ '+fmt(q))}</span>`;
  const r0 = `<div class="er" style="margin-top:12px"><span class="lhs">y</span><span class="eqs">＝</span><span>${aPart}${pPart}${qPart}</span></div>`;
  const rowDir = `<div class="arow"><span class="al">向き</span>${slotC('r',dir,st.dir,'a')}</div>`;
  const rowV = `<div class="arow math"><span class="al">頂点</span>(${slotC('o',fmt(p),st.vx,'p')},${slotC('g',fmt(q),st.vy,'q')})</div>`;
  return {aS,qT,eqTxt,up,dir,V,cm,r0,rowDir,rowV};
}
/* 平方完成する前の式（もとの式）。kst：数だけの項を青く光らせる番（なければ光らせない） */
function origRow(o,kst){
  const cpart = o.c ? tm('b',sgn(o.c),kst===undefined?99:kst) : (kst!==undefined ? S(kst,K('b','＋ 0')) : '');
  return `<div class="er orig"><span class="lhs">y</span><span class="eqs">＝</span><span>${polyStr(o.a,o.b,0)} ${cpart}</span><span class="otag">もとの式</span></div>`;
}
function topRows(P,R){
  if(!P.orig) return `<div class="rowsw math" style="font-size:32px">${R.r0}</div>`;
  return `<div class="rowsw math" style="font-size:32px;top:22px">${origRow(P.orig,P.kst)}`
    + R.r0.replace('margin-top:12px','margin-top:34px').replace('<span class="lhs">y</span>','<span class="lhs"></span>') + `</div>`;
}
const LEGEND = `<div class="card abs legend">${TP('lav','right:24px;top:-14px;transform:rotate(-5deg)')}
    <div class="lab">基本の形</div>
    <div class="l1 math">y ＝ ${K('r','a')}(x − ${K('o','p')})${P2} ＋ ${K('g','q')}</div>
    <div class="l2">${K('r','形')}向き　${K('o','横')}x座標　${K('g','縦')}y座標</div>
  </div>`;
const EQTAPE = `${TP('pink','left:-34px;top:4px;transform:rotate(-40deg)')}${TP('pink','right:-34px;top:4px;transform:rotate(40deg)')}`;

/* ====== グラフ・頂点・軸 の 1問 ======
   P = {num, a, p, q}　　y軸との交点を もとの式から読むとき：yint:c, orig:{a,b} */
function genGraph(P){
  const {num,a,p,q}=P;
  const x1 = p!==0 ? 0 : 1;                      // 頂点がy軸上なら x=1 の点
  const y1 = a*(x1-p)**2+q;
  Object.assign(P,{x1,y1});
  const aOne = ab(a)===1;
  const Q1 = `(${fmt(x1)}, ${fmt(y1)})`;
  const eqv = (m) => m===fmt(y1) ? m : `${m} ＝ ${fmt(y1)}`;
  const st={col:1,dir:2,vx:3,vy:4,ax:5,pv:6,cu:7,pt:8};
  const R = readEq(P,st), aS=R.aS, qT=R.qT;

  /* もう1点：1行ずつ［番号, 左に書く式, コメント］ */
  let L, head='もう1点';
  if(P.yint!==undefined){
    const c=P.yint, o=P.orig;
    head='y軸との交点';
    L = [
      ['①', `<span class="math">y ＝ ${polyStr(o.a,o.b,0)} <span class="cc cc-b sm">${sgn(c)}</span></span> なので`,
            `<b>もう1点</b> は <b>y軸との交点</b>。　平方完成する <b>前</b> の もとの式を 見よう。　${c===0?`数だけの項が ないので ${K('b','＋ 0')} と 考えるよ。`:`数だけの項は ${K('b',sgn(c))}。`}`],
      ['②', `y軸との交点は <span class="math" data-k="pt1">(0, <span class="cc cc-b sm">${fmt(c)}</span>)</span>`,
            `y軸上 では ${M('x ＝ 0')}。　x に 0 を 入れると x の項は 全部 0 に なるから、残るのは 数だけの項。　だから y軸との交点は <b>${M(Q1)}</b>。`],
      ['※', `計算不要`, `もとの式の <b>数だけの項</b> が そのまま y座標！　<b>計算しなくても</b> 読みとれるよ。`]
    ];
  } else if(p!==0){
    const subst = `${aS}(0 ${p<0?'＋':'−'} ${ab(p)})${P2}${qT}`;
    const kakko = `${aS}(${fmt(-p)})${P2}${qT}`;
    const sq = p*p;
    const mul = aOne ? `${a<0?'−':''}${sq}${qT}` : `${fmt(a)} × ${sq}${qT}`;
    L = [
      ['①', `y軸上なので <span class="math">x ＝ 0</span><br><span class="math">x ＝ 0</span> を代入`,
            `<b>もう1点</b> 求めよう。　① <b>y軸上</b> の点なので ${M('x ＝ 0')}。　だから ${M('x ＝ 0')} を <b>代入</b> するよ。`],
      ['②', `<span class="math">y ＝ ${subst}</span>`, `② 式の x に 0 を 代入した式。　${M(`y ＝ ${subst}`)}`],
      ['③', `<span class="math">　＝ ${kakko}</span>`, `③ まず <b>括弧の中</b> を 計算。　${M(`0 ${p<0?'＋':'−'} ${ab(p)} ＝ ${fmt(-p)}`)} だから ${M(`y ＝ ${kakko}`)}`],
      ['④', `<span class="math">　＝ ${eqv(mul)}</span>`, `④ <b>全部</b> 計算する。　${M(`y ＝ ${eqv(mul)}`)}`],
      ['⑤', `<span class="math">x ＝ 0, y ＝ ${fmt(y1)}</span> なので<br><span class="math" data-k="pt1">${Q1}</span>`,
            `⑤ だから ${M('x ＝ 0')}、${M(`y ＝ ${fmt(y1)}`)} なので、もう1点は <b>${M(Q1)}</b>。`]
    ];
  } else {
    const subst = aOne ? `${a<0?'−':''}1${P2}${qT}` : `${fmt(a)} × 1${P2}${qT}`;
    const mul = aOne ? `${a<0?'−':''}1${qT}` : `${fmt(a)} × 1${qT}`;
    L = [
      ['①', `頂点が y軸上なので<br><span class="math">x ＝ 1</span> のときを求める`,
            `<b>もう1点</b> 求めよう。　① 頂点が <b>y軸上</b> にあるので、${M('x ＝ 0')} だと 頂点と 同じ点に なってしまう。　だから <b>${M('x ＝ 1')}</b> のときを 求めるよ。`],
      ['②', `<span class="math">y ＝ ${subst}</span>`, `② 式の x に 1 を 代入した式。　${M(`y ＝ ${subst}`)}`],
      ['③', `<span class="math">　＝ ${eqv(mul)}</span>`, `③ <b>全部</b> 計算する。　${M(`y ＝ ${eqv(mul)}`)}`],
      ['④', `<span class="math">x ＝ 1, y ＝ ${fmt(y1)}</span> なので<br><span class="math" data-k="pt1">${Q1}</span>`,
            `④ だから ${M('x ＝ 1')}、${M(`y ＝ ${fmt(y1)}`)} なので、もう1点は <b>${M(Q1)}</b>。`]
    ];
  }
  st.ptg = st.pt + L.length; st.dn = st.ptg + 1;
  if(P.orig){ if(P.yint!==undefined) P.orig.c = P.yint; P.kst = st.pt; }

  const cm = [
    P.yint!==undefined
      ? `${num} 前のスライドで 平方完成 した 式 ${M(R.eqTxt)} を 使って、<b>グラフ</b> と <b>向き・頂点・軸</b> を 答えよう！`
      : (P.intro || `${num} ${M(R.eqTxt)} の <b>グラフ</b> をかいて、<b>向き・頂点・軸</b> を 答えよう！`),
    ...R.cm,
    `軸は 頂点の x座標 を 使って <b>${M(`x ＝ ${fmt(p)}`)}</b>。${p===0?'　（y軸 そのもの だね）':''}`,
    `グラフを かこう。　まず <b>頂点</b> ${M(R.V)} を とる。`,
    `頂点から ${R.dir} の <b>放物線</b> を かこう。`,
    ...L.map(l=>l[2]),
    `点 ${M(Q1)} を グラフに かきこもう。`,
    `<b>完成！</b>　${R.dir}、頂点 ${M(R.V)}、軸 ${M(`x ＝ ${fmt(p)}`)} です。`
  ];
  const n2 = `<div class="nt lh" data-s="${st.pt}" style="--dotc:#f3d58a"><b>【${head}】</b></div>`
    + L.map((l,i)=>`<div class="pl lh" data-s="${st.pt+i}"><span class="no">${l[0]}</span><span>${l[1]}</span></div>`).join('');

  return `
  <div class="pno">${num}</div>
  <div class="card abs eqcard">${EQTAPE}
    ${topRows(P,R)}
    <div class="rowsw" style="top:${P.orig?196:148}px">${n2}</div>
    <div class="divider"></div>
    ${graphSVG(P,st)}
  </div>
  <div class="card abs memo">${TP('yellow','right:22px;top:-14px;transform:rotate(4deg)')}
    <div class="lab">答え</div>
    ${R.rowDir}${R.rowV}
    <div class="arow math"><span class="al">軸</span>x ＝${slotC('o',fmt(p),st.ax,'p')}</div>
    <div class="arow math gray"><span class="al">もう一点</span>${slotC('k',Q1,st.ptg,'pt1')}</div>
  </div>
  ${LEGEND}
  ${SEAL(st.dn)}
  ${cbar(cm)}`;
}

/* ====== 最大値・最小値 の 1問 ====== */
function mmSlide(P){
  const {num,a,p,q}=P;
  Object.assign(P,{x1:p,y1:q,noPt:true});
  const st={col:1,dir:2,vx:3,vy:4,pv:5,cu:6,ext:7,none:8,dn:9};
  const R = readEq(P,st), up=R.up;
  const big = up?'最小値':'最大値', non = up?'最大値':'最小値';
  P.extra = ({X,Y,d,u})=>{
    const bw=136, bx = p>0 ? X(0)-10-bw : X(0)+(p?10:18), by=Y(q)-18;
    let s=`<g class="gs" data-s="${st.ext}">${p?`<line class="gd mmline" x1="${X(p)}" y1="${Y(q)}" x2="${X(0)}" y2="${Y(q)}"/>`:''}
      <circle class="mmring" cx="${X(p)}" cy="${Y(q)}" r="12"/><circle class="mmring d2" cx="${X(p)}" cy="${Y(q)}" r="12"/>
      <g class="popb"><rect class="mmbadge" x="${bx}" y="${by}" width="${bw}" height="36" rx="18"/><text class="mmbt" x="${bx+bw/2}" y="${by+25}" text-anchor="middle">${big} ${fmt(q)}</text></g>
      <text class="gt k halo" x="${X(p)}" y="${up?Y(q)+56:Y(q)-42}" text-anchor="middle" style="font-family:'Zen Maru Gothic';font-weight:900">いちばん${up?'下':'上'}！</text></g>`;
    let arr='';
    [-1,1].forEach(sd=>{
      const xe=p+sd*d, ye=a*d*d+q, ang=Math.atan2(-2*a*d*u, sd*u);
      const hx=X(xe), hy=Y(ye);
      const tri=[[6,0],[-10,-7],[-10,7]].map(([dx,dy])=>`${(hx+dx*Math.cos(ang)-dy*Math.sin(ang)).toFixed(1)},${(hy+dx*Math.sin(ang)+dy*Math.cos(ang)).toFixed(1)}`).join(' ');
      arr+=`<g class="arrw" style="--dx:${(7*Math.cos(ang)).toFixed(1)}px;--dy:${(7*Math.sin(ang)).toFixed(1)}px"><polygon points="${tri}" fill="var(--note)"/></g>`;
    });
    const xe=p-d, ye=a*d*d+q;
    arr+=`<text class="gt halo" x="${X(xe)+10}" y="${Y(ye)+(up?34:-24)}" style="font-family:'Zen Maru Gothic';font-weight:900;fill:var(--note)"><tspan>どこまでも</tspan><tspan x="${X(xe)+10}" dy="22">→ ${non} なし</tspan></text>`;
    s+=`<g class="gs" data-s="${st.none}">${arr}</g>`;
    return s;
  };
  const extT = `x ＝ ${fmt(p)} で、${big} ${fmt(q)}`;
  const cm = [
    P.intro || `${num} ${M(R.eqTxt)} の <b>最大値・最小値</b> を 求めよう！　まず グラフを かいて 考えるよ。`,
    ...R.cm,
    `グラフに <b>頂点</b> ${M(R.V)} を とる。`,
    `頂点から ${R.dir} の <b>放物線</b> を かこう。`,
    `${R.dir} の グラフは 頂点が <b>いちばん${up?'下':'上'}</b>。　だから ${M(`x ＝ ${fmt(p)}`)} の とき <b>${big} ${fmt(q)}</b>。`,
    up ? `グラフの 上の方は <b>どこまでも</b> 大きくなる。　いちばん大きい 値は 決まらないので <b>最大値 なし</b>。`
       : `グラフの 下の方は <b>どこまでも</b> 小さくなる。　いちばん小さい 値は 決まらないので <b>最小値 なし</b>。`,
    `<b>完成！</b>　${up?`最大値 なし、${M(extT)}`:`${M(extT)}、最小値 なし`}。`
  ];
  const notes = `<div class="nt lh" data-s="${st.ext}" style="--dotc:var(--r-bd)">${R.dir} → 頂点が いちばん${up?'下':'上'}<br><span class="math">→ ${extT}</span></div>
    <div class="nt lh" data-s="${st.none}" style="--dotc:var(--b-bd)">${up?'上':'下'}は どこまでも のびる<br>→ ${non} なし</div>`;
  const vs = `<span class="slot slot-w"><span class="tm tm-w2 on fly" data-f="${st.ext}" data-src="q">${extT}</span></span>`;
  const ns = `<span class="slot slot-w"><span class="tm tm-w2 on fly" data-f="${st.none}" data-src="none">なし</span></span>`;
  return `
  <div class="pno">${num}</div>
  <div class="card abs eqcard">${EQTAPE}
    ${topRows(P,R)}
    <div class="rowsw" style="top:${P.orig?200:160}px">${notes}</div>
    <div class="divider"></div>
    ${graphSVG(P,st)}
  </div>
  <div class="card abs memo">${TP('yellow','right:22px;top:-14px;transform:rotate(4deg)')}
    <div class="lab">答え</div>
    ${R.rowDir}${R.rowV}
    <div class="arow"><span class="al">最大値</span>${up?ns:vs}</div>
    <div class="arow"><span class="al">最小値</span>${up?vs:ns}</div>
  </div>
  ${LEGEND}
  ${SEAL(st.dn)}
  ${cbar(cm)}`;
}

/* ====== 平方完成 の 1問 ======
   P = {num, a, b, c}　（y ＝ ax² ＋ bx ＋ c）　next:true なら 最後に「次はグラフ」と添える */
const ARW = `<svg width="34" height="46" viewBox="0 0 44 60"><path d="M10 4 C34 10,36 36,17 46" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/><polygon points="3,52 20,56 12,38" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>`;
const WV = (a,b,html) => `<span class="wv" data-wa="${a}" data-wb="${b}">${html}<span class="wl"></span></span>`;
const ANS = (s,html) => `<span class="ans" data-a="${s}">${html}<span class="ulh"></span><svg class="sl" width="34" height="30" viewBox="0 0 34 30"><path class="s1" d="M8 27 L15 4" pathLength="1"/><path class="s2" d="M21 27 L28 4" pathLength="1"/></svg></span>`;
const hslot = (k,txt,f,x='') => `<span class="slot slot-${k}"${x}><span class="tm tm-${k} on fly" data-f="${f}" data-src="memo-${k}">${txt}</span></span>`;
const hrow = (s,lhs,body,note) =>
  `<div class="er${s===null?'':' lh'}"${s===null?'':` data-s="${s}"`}><span class="lhs">${lhs}</span><span class="eqs">＝</span><span class="bd">${body}</span>${note?`<span class="note">${ARW}<span>${note}</span></span>`:''}</div>`;

function heihoSlide(P){
  const {num,a,b,c}=P, one=(a===1);
  const bb=b/a, h=bb/2, h2=h*h;          // bb：かっこの中の x の係数 / h：その半分
  const g1=-h2, g2=-a*h2, fin=c+g2;      // g1：{ }の中の数 / g2：分配後の数 / fin：最後の定数
  const aS = a===1 ? '' : a===-1 ? '−' : fmt(a);
  const aP = a<0 ? `(${fmt(a)})` : fmt(a);
  const hx = `x ${h<0?'−':'＋'} ${ab(h)}`;
  const ans = `${aS}(${hx})² ${fin<0?'−':'＋'} ${ab(fin)}`;
  const xt = n => `${ab(n)===1?'':ab(n)}x`;   // 1x → x
  const c0 = `${num} ${M('y ＝ '+polyStr(a,b,c))} を <b>平方完成</b> しよう！　平方完成は ${M('a(x − p)² ＋ q')} の形に 書きかえることだよ。`;
  const cm=[c0]; let n=0; const nx=t=>{n++;cm.push(t);return n;};
  const st={};
  const bTxt = one ? `${b<0?'−':'＋'}${xt(b)}` : `x² ${b<0?'−':'＋'} ${xt(b)}`;

  if(one) st.pre = nx(`まず 式の中の <b>x の項</b> に 注目！　<b>波線</b> の部分だよ。`);
  st.col = one
    ? nx(`まず 色分け！　${K('b',bTxt)}（青）が <b>x の項</b>。${c!==0?`　${K('n',sf(c))}（灰）は 数だけの項で、あとで使うよ。`:''}　公式に使うのは 青の <b>${fmt(b)}</b> です。`)
    : nx(`${K('r',aS)} 赤の <b>${fmt(a)}</b> に注目！　点線で囲んだ <b>x² の項と x の項（2項）</b> を ${fmt(a)} で くくりだして、公式を使う準備をするよ。${c!==0?`　${K('n',sf(c))} 灰は 数だけの項なので 外のまま。`:''}`);
  if(!one) st.f1 = nx(`<b>公式を使う準備</b>！　${fmt(a)} で くくりだして、かっこの中を <b>x² ＋ ○x</b> の形にする。　${M(`${fmt(b)}x ÷ ${aP} ＝ ${fmt(bb)}x`)} なので かっこの中は ${M(`x² ${bb<0?'−':'＋'} ${xt(bb)}`)}。　この かっこの中に 公式が 使えるよ。`);
  st.o = nx(`${one?'青の':'かっこの中の'} <b>${fmt(bb)}</b> の <b>半分</b>：${M(`${fmt(bb)} ÷ 2 ＝ ${fmt(h)}`)}。　公式メモの <b>「半分」</b>の欄に 入れよう。`);
  st.g = nx(`つぎは <b>マイナス 半分の2乗</b>。　半分 ${fmt(h)} を 2乗して マイナスを つけて ${M(`−(${fmt(h)})² ＝ −${h2}`)}。　緑の欄に 入れよう。`);
  if(one){
    st.f2 = nx(`公式を使う！　${M('(x ＋ □)² − △')} の形の <b>空らん</b> に、右の 公式メモの 数を 入れていくよ。${c!==0?`　${K('n',sf(c))} 灰は そのまま 後ろに つけるよ。`:''}`);
    st.fo = nx(`まず <b>半分</b>（橙）の <b>${fmt(h)}</b> を メモから □ へ！　${M(`(${hx})²`)}`);
    st.fg = nx(`つぎに <b>マイナス半分の2乗</b>（緑）の <b>${fmt(g1)}</b> を メモから △ へ！　${M(`(${hx})² − ${h2}`)}${c===0?'　これで 平方完成！':''}`);
    if(c!==0){
      st.cw = nx(`つぎに 計算するのは、<b>波線</b> の部分！　${K('g',sf(g1))} と ${K('n',sf(c))} を あわせるよ。`);
      st.f4 = nx(`計算する！　${M(`${fmt(g1)} ${c<0?'−':'＋'} ${ab(c)} ＝ ${fmt(fin)}`)}。　答えは <b>${M('y ＝ '+ans)}</b>。`);
    }
  } else {
    st.f2 = nx(`公式を使う！　かっこの中を ${M('(x ＋ □)² − △')} の形にする。　空らんに 右の 公式メモの 数を 入れていくよ。　まわりの { } は あとで 外すよ。`);
    st.fo = nx(`まず <b>半分</b>（橙）の <b>${fmt(h)}</b> を メモから □ へ！　${M(`(${hx})²`)}`);
    st.fg = nx(`つぎに <b>マイナス半分の2乗</b>（緑）の <b>${fmt(g1)}</b> を メモから △ へ！　${M(`(${hx})² − ${h2}`)}`);
    st.d1 = nx(`<b>分配</b> して { } を 外す！　まず ${fmt(a)} と ${M('( )²')} の分配。　${fmt(a)} が ${M('( )²')} に <b>くっついて</b> ${M(`${aS}(${hx})²`)} になるよ。`);
    st.d2 = nx(`つぎに ${fmt(a)} と ${fmt(g1)} の分配。　<b>かけ算</b> して ${M(`${aP} × (${fmt(g1)}) ＝ ${sf(g2)}`)}。${c===0?`　これで 平方完成！　答えは <b>${M('y ＝ '+ans)}</b>。`:''}`);
    if(c!==0){
      st.d3 = nx(`最後に、{ } の外に あった 灰色の ${K('n',sf(c))} を そのまま 後ろに つけるよ。`);
      st.cw = nx(`つぎに 計算するのは、<b>波線</b> の部分！　${K('g',sf(g2))} と ${K('n',sf(c))} を あわせるよ。`);
      st.f4 = nx(`計算する！　${M(`${fmt(g2)} ${c<0?'−':'＋'} ${ab(c)} ＝ ${fmt(fin)}`)}。　答えは <b>${M('y ＝ '+ans)}</b>。`);
    }
  }
  st.dn = nx(`これで <b>完成</b>！　ここから 頂点は ${M(`(${fmt(-h)}, ${fmt(fin)})`)} と 読みとれるよ。${P.next?'　つぎの スライドで グラフを かこう！':''}`);

  /* 式の行 */
  const L0 = one
    ? `${WV(st.f2,st.fg,`${X2} ${WV(st.pre,st.col,tm('b',`${b<0?'− ':'＋ '}${xt(b)}`,st.col))}`)}${c!==0?tm('n',sgn(c),st.col):''}`
    : `<span class="ct" data-o="${st.col}">${tm('r',aS,st.col)}${X2} ${b<0?'−':'＋'} ${xt(b)}</span> ${c!==0?tm('n',sgn(c),st.col):''}`;
  let rows = hrow(null,'y',L0), dist = '';
  if(one){
    let L1 = `( x ${hslot('o',sgn(h),st.fo)} )${P2} ${c!==0?WV(st.cw,st.f4,`${hslot('g',sgn(g1),st.fg)}${tm('n',sgn(c),st.f2)}`):hslot('g',sgn(g1),st.fg)}`;
    if(c===0) L1 = ANS(st.dn, L1);
    rows += hrow(st.f2,'',L1,'公式を使う');
    if(c!==0) rows += hrow(st.f4,'',ANS(st.f4,`( x ${sgn(h)} )${P2} ${sgn(fin)}`),'計算する');
  } else {
    const lblEnd = c!==0 ? st.cw : st.dn;
    rows += hrow(st.f1,'',`${tm('r',aS,st.f1)}( ${WV(st.f2,st.fg,`${X2} ${tm('b',`${bb<0?'− ':'＋ '}${xt(bb)}`,st.f1)}`)} )${c!==0?tm('n',sgn(c),st.f1):''}`,`公式の準備<br>${fmt(a)} で くくりだす`);
    rows += hrow(st.f2,'',`${tm('r',aS,st.f2,' data-k="r3"')}{ <span class="pg" data-k="par">( x ${hslot('o',sgn(h),st.fo)} )${P2}</span> ${hslot('g',sgn(g1),st.fg,' data-k="grn"')} }${c!==0?tm('n',sgn(c),st.f2):''}`,'公式を使う');
    const lbl = (a0,t) => `<span class="dlbl" data-wa="${a0}" data-wb="${lblEnd}">${t}</span>`;
    const orgC = `<span class="hasl">${tm('o',`${aS}( x ${sgn(h)} )${P2}`,st.d1)}${lbl(st.d1,`${fmt(a)} と ( )² が くっつく`)}</span>`;
    const grnC = `<span class="hasl">${tm('g',sgn(g2),st.d2)}${lbl(st.d2,`${aP} × (${fmt(g1)}) ＝ ${sf(g2)}`)}</span>`;
    const tail = c!==0 ? WV(st.cw,st.f4,`${S(st.d2,grnC)}${S(st.d3,tm('n',sgn(c),st.d3))}`) : S(st.d2,grnC);
    rows += hrow(st.d1,'', c!==0 ? `${orgC}${tail}` : ANS(st.dn,`${orgC}${tail}`), '分配して<br>{ } を外す');
    const dg = (a0,to,hh,dx) => `<g class="dg" data-wa="${a0}" data-wb="${lblEnd}" data-fr="r3" data-to="${to}" data-h="${hh}" data-dx="${dx}"><path pathLength="1" d=""/><polygon points=""/></g>`;
    dist = `<svg class="dist" width="724" height="460">${dg(st.d1,'par',18,0)}${dg(st.d2,'grn',34,12)}</svg>`;
    if(c!==0) rows += hrow(st.f4,'',ANS(st.f4,`${aS}( x ${sgn(h)} )${P2} ${sgn(fin)}`),'計算する');
  }

  return `
  <div class="pno">${num}</div>
  <div class="card abs eqcard">${EQTAPE}<div class="hrows math">${rows}${dist}</div></div>
  <div class="card abs hmemo">${TP('yellow','right:22px;top:-14px;transform:rotate(4deg)')}<div class="lab">公式メモ</div>
    <div class="mrow"><div class="ml">半分</div><div class="mbox bo" data-k="memo-o">${S(st.o,`<span class="cc cc-o">${fmt(h)}</span>`)}</div></div>
    <div class="mrow"><div class="ml">マイナス<br>半分の2乗</div><div class="mbox bg" data-k="memo-g">${S(st.g,`<span class="cc cc-g">${fmt(g1)}</span>`)}</div></div>
  </div>
  <div class="card abs hlegend">${TP('lav','right:24px;top:-14px;transform:rotate(-5deg)')}<div class="lab">色の ルール</div>
    <span class="cc cc-r">x² の前の数</span><span class="cc cc-b">x の項</span>
    <span class="cc cc-n">数だけの項</span><span class="cc cc-o">半分</span>
    <span class="cc cc-g">−半分の2乗</span>
  </div>
  ${SEAL(st.dn)}
  ${cbar(cm)}`;
}

/* ====== 表紙・基本・おわり ====== */
const miniGraph = `<svg width="264" height="250" viewBox="0 0 264 250">
  ${[...Array(12)].map((_,i)=>`<line class="gg" x1="${i*24}" y1="0" x2="${i*24}" y2="250"/>`).join('')}
  ${[...Array(11)].map((_,i)=>`<line class="gg" x1="0" y1="${i*24+10}" x2="264" y2="${i*24+10}"/>`).join('')}
  <line class="ax" x1="0" y1="178" x2="264" y2="178"/><line class="ax" x1="144" y1="250" x2="144" y2="0"/>
  <path d="M 52 20 Q 120 330 188 20" fill="none" stroke="var(--curve)" stroke-width="4" stroke-linecap="round"/>
  <line class="axl" x1="120" y1="0" x2="120" y2="250"/>
  <circle cx="120" cy="175" r="7" fill="var(--accent)" stroke="var(--paper)" stroke-width="2.5"/>
</svg>`;
const cover = (kicker,title,sub,sub2,cap) => `
<div class="card abs cover">${TP('pink','left:-26px;top:-4px;transform:rotate(-38deg)')}${TP('mint','right:-26px;bottom:-4px;transform:rotate(-38deg)')}
  <div class="kicker">${kicker}</div>
  <h1>${title}</h1>
  <div class="r" data-s="1"><div class="sub math">${sub}</div></div>
  <div class="r" data-s="2"><div class="sub2">${sub2}</div></div>
</div>
<div class="card abs polaroid">${TP('yellow','left:92px;top:-14px;transform:rotate(-3deg)')}${miniGraph}<div class="cap">${cap}</div></div>`;
const FORM_SUB = `y ＝ ${K('r','a')}(x − ${K('o','p')})${P2} ＋ ${K('g','q')}`;
const basicWrap = (title,body,cms,tape='blue') => `
<div class="end-h"><h2>${title}</h2></div>
<div class="card abs fcard">${TP(tape,'left:-30px;top:2px;transform:rotate(-40deg)')}${TP(tape,'right:-30px;top:2px;transform:rotate(40deg)')}${body}</div>
${cbar(cms)}`;
const upL = (k,t,s) => `<span class="lbl up l${k}"><span class="lh" data-s="${s}">${t}</span></span>`;
const graphBasic = basicWrap('グラフの 読み方（形・横・縦）', `
  <div class="fr math big" style="margin-top:20px">y ＝ <span class="hasl">${tm('r','a',1)}${upL('r','形',1)}</span>( x − <span class="hasl">${tm('o','p',1)}${upL('o','横',1)}</span> )${P2} ＋ <span class="hasl">${tm('g','q',1)}${upL('g','縦',1)}</span></div>
  <div class="fr mid lh" data-s="2" style="font-size:34px">${K('r','形')} → グラフの <b>向き</b>　＋ なら 下に凸 ∪ 、− なら 上に凸 ∩</div>
  <div class="fr mid lh" data-s="3" style="font-size:34px">${K('o','横')} → 頂点の <b>x座標</b>　<span style="color:var(--accent)">プラスマイナスが逆転！</span></div>
  <div class="fr mid lh" data-s="4" style="font-size:34px">${K('g','縦')} → 頂点の <b>y座標</b>　そのまま</div>
  <div class="fr chk lh" data-s="5">軸は 頂点の x座標 を 使って <span class="math">x ＝ p</span></div>`,
  [
  `2次関数 ${M('y ＝ a(x − p)² ＋ q')} の グラフ。　この形なら 式から そのまま <b>向き・頂点・軸</b> が 読みとれるよ。`,
  `赤の ${K('r','a')} が <b>形</b>、橙の ${K('o','p')} が <b>横</b>、緑の ${K('g','q')} が <b>縦</b>。`,
  `<b>形</b> は グラフの 向き。　プラスなら <b>下に凸</b>、マイナスなら <b>上に凸</b>。`,
  `<b>横</b> は 頂点の x座標。　かっこの中の 数の <b>プラスマイナスが逆転</b> するので 注意！　${M('(x ＋ 1)²')} なら −1。`,
  `<b>縦</b> は 頂点の y座標。　こちらは <b>そのまま</b>。`,
  `軸は 頂点を 通る たての直線 <b>${M('x ＝ p')}</b>。`
]);
const heihoBasic = basicWrap('平方完成の 公式', `
  <div class="fr math big">${X2} ${tm('b','＋ ○x',1)}</div>
  <div class="fr math big lh" data-s="2">＝ ( x ${tm('o','＋ ○の半分',2)} )${P2} ${tm('g','− (○の半分)'+P2,3)}</div>
  <div class="fr math mid lh" data-s="4">例　${X2} ${tm('b','＋ 6x',4)} ＝ ( x ${tm('o','＋ 3',5)} )${P2} ${tm('g','− 9',6)}</div>
  <div class="fr math chk lh" data-s="7">たしかめ：(x ＋ 3)<sup>2</sup> − 9 ＝ x<sup>2</sup> ＋ 6x ＋ 9 − 9 ＝ x<sup>2</sup> ＋ 6x</div>`,
  [
  `平方完成 とは、式を <b>a(x − p)² ＋ q</b> の形に 書きかえること。　まず 公式を 確認しよう！`,
  `${M('x² ＋ ○x')} の <b>○</b>（x の係数）に 注目！　この数を 使って 書きかえるよ。`,
  `かっこの中には ○ の <b>半分</b> を 入れる！　${M('(x ＋ ○の半分)²')}`,
  `展開すると よぶんな ${M('(○の半分)²')} が 出てくる。　それを <b>引いて</b> つじつまを合わせる → <b>マイナス 半分の2乗</b>。`,
  `例で やってみよう。　${M('x² ＋ 6x')} では ○ ＝ 6 です。`,
  `6 の <b>半分</b> は 3。　${M('(x ＋ 3)²')}`,
  `3 の2乗は 9。　引くので <b>− 9</b>。　${M('x² ＋ 6x ＝ (x ＋ 3)² − 9')}`,
  `たしかめ：展開して 9 を 引くと、もとの ${M('x² ＋ 6x')} に もどる！　これが <b>平方完成</b> です。`
], 'lav');
const mmBasic = basicWrap('最大値・最小値の 考え方', `
  <div class="fr mid lh" data-s="1" style="font-size:38px">${K('r','＋')} 下に凸 ∪ → 頂点が いちばん下</div>
  <div class="fr mid lh" data-s="2" style="font-size:36px">→ 頂点で <b style="color:var(--accent)">最小値</b>　／　最大値は <b style="color:var(--accent)">なし</b></div>
  <div class="fr mid lh" data-s="3" style="font-size:38px;margin-top:18px">${K('r','−')} 上に凸 ∩ → 頂点が いちばん上</div>
  <div class="fr mid lh" data-s="4" style="font-size:36px">→ 頂点で <b style="color:var(--accent)">最大値</b>　／　最小値は <b style="color:var(--accent)">なし</b></div>`,
  [
  `2次関数の <b>最大値・最小値</b> は、グラフを かいて 考えるよ。　大事なのは <b>向き</b> と <b>頂点</b>。`,
  `${K('r','＋')} なら 下に凸。　グラフは 頂点が <b>いちばん下</b>。`,
  `だから 頂点の y座標が <b>最小値</b>。　上の方は どこまでも 大きくなるので <b>最大値は なし</b>。`,
  `${K('r','−')} なら 上に凸。　グラフは 頂点が <b>いちばん上</b>。`,
  `だから 頂点の y座標が <b>最大値</b>。　下の方は どこまでも 小さくなるので <b>最小値は なし</b>。`
], 'yellow');
const endHtml = `
<div class="card abs cover" style="height:380px;top:150px">${TP('lav','left:-26px;top:-4px;transform:rotate(-38deg)')}${TP('yellow','right:-26px;top:-4px;transform:rotate(38deg)')}
  <div class="kicker">数学Ⅰ　２学期中間考査対策</div>
  <h1>おつかれさま<br><span class="mk">でした！</span></h1>
</div>
<div class="card abs polaroid">${TP('pink','left:92px;top:-14px;transform:rotate(3deg)')}${miniGraph}<div class="cap">よくできました</div></div>`;
