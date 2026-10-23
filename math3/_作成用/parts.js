/* ====== 数学Ⅲ の 部品（数学C の parts.js を 元に した 別もの） ====== */

/* 数式：M`\int x^3\,dx`（\ を そのまま 書ける）。KaTeX で かく。D は 大きい 形（\displaystyle：計算の 行に 使う） */
function M(s, ...v){
  const t = typeof s==='string' ? s : String.raw(s, ...v);
  return `<span class="m">${t.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</span>`;
}
function D(s, ...v){ return M('\\displaystyle ' + (typeof s==='string' ? s : String.raw(s, ...v))); }
/* 出る番：S(番, html, 遅れ秒) */
const S = (n, h, d) => `<span data-s="${n}"${d?` style="--d:${d}s"`:''}>${h}</span>`;
/* 空らん（プリントの 書きこむ ところ）。答えは n 番で 出る */
const FILL = (n, h, w) => `<span class="fill"${w?` style="min-width:${w}em"`:''}><span data-s="${n}">${h}</span></span>`;
/* 説明欄：cm の i 番目が i 番で 出る（null は とばす） */
const CAP = cm => `<div class="cap">${cm.map((c,i)=>c==null?'':`<p data-m="${i}">${c}</p>`).join('')}</div>`;
/* 見出し */
const HD = (no, title, sec) => `<header class="hd"><span class="no">${no}</span><h2>${title}</h2>${sec?`<span class="sec">${sec}</span>`:''}</header>`;
/* 枠（公式・方針 など） */
const BOX = (label, body) => `<div class="box"><div class="bl">${label}</div><div class="bc">${body}</div></div>`;
/* Point の 枠：n 番で 出る（n が null なら はじめから） */
const PT = (n, label, body) => `<div class="pbox"${n==null?'':` data-s="${n}"`}><div class="pl2">${label}</div>${body}</div>`;

/* 計算の 行：[[番, TeX], …]。TeX が '<' で 始まれば html の まま。番が null なら はじめから */
const CALC = (lines, cls) => `<div class="calc ${cls||''}">${lines.map(([n,t])=>
  `<div${n==null?'':` data-s="${n}"`}>${t.startsWith('<') ? t : D(t)}</div>`).join('')}</div>`;
/* 問題 1つ：⑴ と 式 */
const PQ = (tag, tex) => `<div class="pq"><span class="tag">${tag}</span>${D(tex)}</div>`;

/* 表紙 */
function coverSlide(o){
  return `<div class="cover"><div class="k">${o.kicker||'数学Ⅲ'}</div><div class="n">${o.no}</div>
    <h1>${o.title}</h1><div class="sb">${o.sub||''}</div><div class="ln"></div>
    <div class="ver">${VER}</div></div>`;
}

/* 何問かを 格子に 並べる ページ
   o = {no, sec, title, q（上の 問題文 html）, items:[{tag, q:TeX, lines:[[番,TeX],…]}], c1（1列）, side（下に 足す html）, cm} */
function gridPage(o){
  return HD(o.no, o.title, o.sec) + `<div class="bd col st" style="gap:16px">
    ${o.q ? `<div class="q qline">${o.q}</div>` : ''}
    <div class="grid${o.c1?' c1':''}">${o.items.map(it=>`<div class="it"${it.o!=null?` data-o="${it.o}"`:''}>${PQ(it.tag, it.q)}${CALC(it.lines)}</div>`).join('')}</div>
    ${o.side||''}
  </div>` + CAP(o.cm);
}

/* 置換積分の ページ：左＝置きかえの 準備（BOX）と Point、右＝計算
   o = {no, sec, title, tag, q:TeX, prep:[[番,TeX],…], plabel（BOX の 名前）, pt（左に 足す html）, calc:[[番,TeX],…], cm} */
function subPage(o){
  return HD(o.no, o.title, o.sec) + `<div class="bd col st" style="gap:14px">
    ${o.top||''}${PQ(o.tag, o.q)}
    <div class="two">
      <div class="l2">${BOX(o.plabel||'置きかえ', CALC(o.prep))}${o.pt||''}</div>
      ${CALC(o.calc, 'main')}
    </div>
  </div>` + CAP(o.cm);
}
