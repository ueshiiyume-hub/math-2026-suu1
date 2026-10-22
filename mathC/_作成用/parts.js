/* ====== 数学C の 部品 ====== */

/* 数式：M`z = a + bi`（\ を そのまま 書ける）。KaTeX で かく */
function M(s, ...v){
  const t = typeof s==='string' ? s : String.raw(s, ...v);
  return `<span class="m">${t.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</span>`;
}
/* 出る番：S(番, html, 遅れ秒) */
const S = (n, h, d) => `<span data-s="${n}"${d?` style="--d:${d}s"`:''}>${h}</span>`;
/* 空らん（プリントの 緑の 箱）。答えは n 番で 出る */
const FILL = (n, h, w) => `<span class="fill"${w?` style="min-width:${w}em"`:''}><span data-s="${n}">${h}</span></span>`;
/* 説明欄：cm の i 番目が i 番で 出る（null は とばす） */
const CAP = cm => `<div class="cap">${cm.map((c,i)=>c==null?'':`<p data-m="${i}">${c}</p>`).join('')}</div>`;
/* 見出し */
const HD = (no, title, sec) => `<header class="hd"><span class="no">${no}</span><h2>${title}</h2>${sec?`<span class="sec">${sec}</span>`:''}</header>`;
/* 枠（定義・記法 など） */
const BOX = (label, body) => `<div class="box"><div class="bl">${label}</div><div class="bc">${body}</div></div>`;

/* 表紙 */
function coverSlide(o){
  return `<div class="cover"><div class="k">${o.kicker||'数学C'}</div><div class="n">${o.no}</div>
    <h1>${o.title}</h1><div class="sb">${o.sub||''}</div><div class="ln"></div>
    <div class="ver">${VER}</div></div>`;
}

/* ---- 複素数平面（SVG） ----
   const g = PL({x0:-4,x1:4,y0:-4,y1:4});  g.svg( g.walk(2,2,1) + g.dot(2,2,'P',3) )
   X(x)・Y(y) で 平面の 座標 → SVG の 座標 */
function PL(o){
  const u = o.u||56, pad = o.pad||36;
  const W = (o.x1-o.x0)*u + 2*pad, H = (o.y1-o.y0)*u + 2*pad;
  const X = x => pad + (x-o.x0)*u, Y = y => pad + (o.y1-y)*u;
  const f = v => +v.toFixed(1);
  let base = '';
  if(o.grid!==false){
    for(let x=o.x0; x<=o.x1; x++) base += `<line class="gd" x1="${X(x)}" y1="${Y(o.y0)}" x2="${X(x)}" y2="${Y(o.y1)}"/>`;
    for(let y=o.y0; y<=o.y1; y++) base += `<line class="gd" x1="${X(o.x0)}" y1="${Y(y)}" x2="${X(o.x1)}" y2="${Y(y)}"/>`;
  }
  const ax0 = X(o.x0)-10, ax1 = X(o.x1)+22, ay0 = Y(o.y0)+10, ay1 = Y(o.y1)-22;
  base += `<line class="ax" x1="${ax0}" y1="${Y(0)}" x2="${ax1-8}" y2="${Y(0)}"/><polygon class="axh" points="${ax1},${Y(0)} ${ax1-14},${Y(0)-6} ${ax1-14},${Y(0)+6}"/>`;
  base += `<line class="ax" x1="${X(0)}" y1="${ay0}" x2="${X(0)}" y2="${ay1+8}"/><polygon class="axh" points="${X(0)},${ay1} ${X(0)-6},${ay1+14} ${X(0)+6},${ay1+14}"/>`;
  if(o.xl!==null) base += `<text class="${o.xl?'jp':'it'}" x="${ax1+6}" y="${Y(0)+7}">${o.xl||'x'}</text>`;
  if(o.yl!==null) base += `<text class="${o.yl?'jp':'it'}" x="${X(0)+12}" y="${ay1+4}">${o.yl||'y'}</text>`;
  base += `<text x="${X(0)-24}" y="${Y(0)+26}">O</text>`;
  if(o.ticks!==false) base += `<text x="${X(1)-6}" y="${Y(0)+26}">1</text><text x="${X(0)-20}" y="${Y(1)+8}">1</text>`;
  const g = {X, Y, u, W, H};
  g.svg = (inner, cls) => `<svg class="pl ${cls||''}" viewBox="${-40} ${-10} ${W+90} ${H+20}">${base}${inner||''}</svg>`;
  /* 点：dot(a, b, 名前, 番, {pos:'ne'|'nw'|'se'|'sw', d:遅れ, given:true}) */
  g.dot = (a, b, name, n, op={}) => {
    const p = op.pos||'ne', dx = p.includes('w') ? -14 : 12, dy = p.includes('s') ? 28 : -12;
    const an = p.includes('w') ? 'end' : 'start', cls = op.given ? ' given' : '';
    const at = n==null ? '' : ` data-s="${n}"${op.d?` style="--d:${op.d}s"`:''}`;
    return `<g${at}><circle class="dot${cls}" cx="${X(a)}" cy="${Y(b)}" r="8"/>${name?`<text class="pn${cls}" x="${X(a)+dx}" y="${Y(b)+dy}" text-anchor="${an}">${name}</text>`:''}</g>`;
  };
  /* 原点から 横（実部・青）→ 縦（虚部・橙）に 進む。n 番で 出る。split:true なら 横 n 番・縦 n+1 番 */
  g.walk = (a, b, n, op={}) => {
    const d = op.d||0, nb = n==null ? null : op.split ? n+1 : n, db = op.split ? 0 : d + (a ? .6 : 0);
    /* n が null なら 動かさない（まとめ用） */
    const at = (nn, dd) => nn==null ? '' : ` data-s="${nn}"${op.e?` data-e="${op.e}"`:''} style="--d:${dd}s"`, dr = n==null ? '' : ' dr';
    const neg = v => String(v).replace('-', '−');
    const hd = (x, y, dir, c, nn, dd) => {   // 矢じり
      const s = 11, pts = dir==='r' ? `${x},${y} ${x-s},${y-s*.6} ${x-s},${y+s*.6}` : dir==='l' ? `${x},${y} ${x+s},${y-s*.6} ${x+s},${y+s*.6}`
        : dir==='u' ? `${x},${y} ${x-s*.6},${y+s} ${x+s*.6},${y+s}` : `${x},${y} ${x-s*.6},${y-s} ${x+s*.6},${y-s}`;
      return `<polygon class="hd-${c}" points="${pts}"${at(nn, dd+.5)}/>`;
    };
    let h = '';
    if(a){
      h += `<path class="wk re${dr}" pathLength="1" d="M${X(0)} ${Y(0)} H${X(a)}"${at(n, d)}/>` + hd(X(a), Y(0), a>0?'r':'l', 're', n, d);
      if(op.lab!==false) h += `<text class="re" x="${f((X(0)+X(a))/2)}" y="${Y(0) - 12}" text-anchor="middle"${at(n, d+.3)}>${op.la||neg(a)}</text>`;
    }
    if(b){
      h += `<path class="wk im${dr}" pathLength="1" d="M${X(a)} ${Y(0)} V${Y(b)}"${at(nb, db)}/>` + hd(X(a), Y(b), b>0?'u':'d', 'im', nb, db);
      if(op.lab!==false) h += `<text class="im" x="${X(a) + (a<0 ? -12 : 12)}" y="${f((Y(0)+Y(b))/2)+8}" text-anchor="${a<0?'end':'start'}"${at(nb, db+.3)}>${op.lb||neg(b)}</text>`;
    }
    return h;
  };
  /* 軸を 太く 光らせる（実軸 re／虚軸 im） */
  g.axl = (which, n) => which==='re'
    ? `<line class="axl re" x1="${X(o.x0)}" y1="${Y(0)}" x2="${X(o.x1)}" y2="${Y(0)}" data-s="${n}"/>`
    : `<line class="axl im" x1="${X(0)}" y1="${Y(o.y0)}" x2="${X(0)}" y2="${Y(o.y1)}" data-s="${n}"/>`;
  /* 矢印 (x0,y0)→(x1,y1)。n 番で かく。op: c（k＝黒・g＝深い緑・m＝灰）、dash（点線。かく 動きなし）、d（遅れ）、e（消える番）、w（太さ） */
  g.arr = (x0, y0, x1, y1, n, op={}) => {
    const ax = X(x0), ay = Y(y0), bx = X(x1), by = Y(y1), L = Math.hypot(bx-ax, by-ay) || 1;
    const ux = (bx-ax)/L, uy = (by-ay)/L, hl = 15, hw = 7.5, c = op.c||'k', d = op.d||0;
    const ex = bx - ux*hl*.8, ey = by - uy*hl*.8;
    const at = dd => n==null ? '' : ` data-s="${n}"${op.e?` data-e="${op.e}"`:''} style="--d:${dd}s"`;
    const anim = n!=null && !op.dash;
    const pts = `${f(bx)},${f(by)} ${f(bx-ux*hl-uy*hw)},${f(by-uy*hl+ux*hw)} ${f(bx-ux*hl+uy*hw)},${f(by-uy*hl-ux*hw)}`;
    return `<path class="vc ${c}${op.dash?' dsh':''}${anim?' dr':''}" pathLength="1" d="M${f(ax)} ${f(ay)} L${f(ex)} ${f(ey)}"${op.w?` style="stroke-width:${op.w}"`:''}${at(d)}/>`
      + `<polygon class="vh ${c}" points="${pts}"${at(anim ? d+.5 : d)}/>`;
  };
  /* 原点と (a,b) を 通る 直線（平面の 端まで） */
  g.line = (a, b, n, op={}) => {
    const ks = [o.x1/a, o.x0/a, o.y1/b, o.y0/b].filter(isFinite);
    const k1 = Math.min(...ks.filter(v=>v>0)), k0 = Math.min(...ks.filter(v=>v<0).map(v=>-v));
    return `<line class="ln${n!=null?' dr':''}" pathLength="1" x1="${f(X(-a*k0))}" y1="${f(Y(-b*k0))}" x2="${f(X(a*k1))}" y2="${f(Y(b*k1))}"${n==null?'':` data-s="${n}"`}${op.d?` style="--d:${op.d}s"`:''}/>`;
  };
  /* 動かす：n 番で 出て、少し 遅れて (dx,dy) だけ 平行移動 */
  g.move = (inner, dx, dy, n, op={}) => `<g data-s="${n}"${op.e?` data-e="${op.e}"`:''}><g class="mv" data-o="${n}" style="--tx:${f(dx*u)}px;--ty:${f(-dy*u)}px">${inner}</g></g>`;
  /* 実軸で 折り返す：n 番で 出て、実軸を 折り目に ひっくり返る */
  g.flip = (inner, n, op={}) => `<g data-s="${n}"${op.e?` data-e="${op.e}"`:''}><g class="fl" data-o="${n}" style="transform-origin:0px ${Y(0)}px">${inner}</g></g>`;
  /* 文字 */
  g.text = (x, y, s, cls, n, anchor) => `<text class="${cls||''}" x="${X(x)}" y="${Y(y)}" text-anchor="${anchor||'middle'}"${n==null?'':` data-s="${n}"`}>${s}</text>`;
  return g;
}
