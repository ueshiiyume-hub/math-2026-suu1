/* ====== 組み立て・操作（数学Ⅲ。数学C の engine.js を 元に した 別もの） ======
   DECK = {title, pages:[{name, html}]}。
   data-s（その番で 出る）・data-e（その番で 消える）・data-o（その番で 色が つく）・cap の p[data-m]（その番の 説明）から 段数を 数える。 */
const stage = document.getElementById('stage');
const names = DECK.pages.map(p=>p.name);
document.title = DECK.title;
stage.innerHTML = DECK.pages.map(p=>`<section class="slide">${p.html}</section>`).join('');

/* 数式：<span class="m">TeX</span> を KaTeX で かく。\A{…}＝橙（変わる ところ）、\B{…}＝紫（置きかえ t）、\DP{…}＝深い青（答え）、\on{番}{a|b|dp}{…}＝その番で 色が つく */
const KX = {throwOnError:false, trust:true, strict:false, macros:{
  '\\A':'\\htmlClass{a}{#1}', '\\B':'\\htmlClass{b}{#1}', '\\DP':'\\htmlClass{dp}{#1}', '\\MU':'\\htmlClass{mu}{#1}',
  '\\BOX':'\\htmlClass{bx}{#1}',
  '\\on':'\\htmlData{o=#1, c=#2}{#3}'}};
stage.querySelectorAll('.m').forEach(e=>{
  if(typeof katex==='undefined') return;
  try{ katex.render(e.textContent, e, KX); }catch(_){}
});

const els = [...stage.querySelectorAll('.slide')];
const nums = e => ['s','e','o','m'].map(k=>e.dataset[k]).filter(v=>v!==undefined).map(Number);
const maxStep = els.map(el => Math.max(0, ...[...el.querySelectorAll('[data-s],[data-e],[data-o],[data-m]')].flatMap(nums)));

const bar = document.getElementById('bar'), ui = document.getElementById('ui'), jump = document.getElementById('jump');
jump.innerHTML = `<button id="themebtn" title="明るく／暗く（T）"></button><button class="tocbtn" title="目次">≡ 目次</button><span class="pgno"></span>
  <div class="tocbg"></div><div class="tocp"><div class="toch"><b>${DECK.title}</b><button class="tocx" title="閉じる">✕</button></div>
  <a class="home" href="index.html">← スライドの 一覧へ</a>
  <div class="tocl">${names.map((n,i)=>`<button class="ti" data-i="${i}">${n}</button>`).join('')}</div></div>`;
window.paintTheme = () => { const b=document.getElementById('themebtn'); b.textContent = isDark() ? '☀' : '☾'; };
paintTheme();
const tocOpen = on => { jump.classList.toggle('open', on); if(on){ const c=jump.querySelector('.ti.on'); if(c) c.scrollIntoView({block:'center'}); } };
jump.addEventListener('click', e=>{
  if(e.target.closest('a')) return;
  e.stopPropagation();
  if(e.target.closest('#themebtn')) return toggleTheme();
  if(e.target.closest('.tocbtn')) return tocOpen(!jump.classList.contains('open'));
  if(e.target.closest('.tocx,.tocbg')) return tocOpen(false);
  const b = e.target.closest('.ti'); if(!b) return;
  stopAuto(); si = +b.dataset.i; st = 0; render(); tocOpen(false);
});

let si = 0, st = 0, timer = null;
function render(){
  els.forEach((el,i)=>{
    const now = i===si, t = now ? st : -1;   // ほかの ページは 何も 出ていない 状態に もどす（入った とき 動きが 見える）
    el.classList.toggle('active', now);
    el.querySelectorAll('[data-s],[data-e]').forEach(e=>{
      const s = e.dataset.s===undefined ? 0 : +e.dataset.s, x = e.dataset.e===undefined ? 1e9 : +e.dataset.e;
      e.classList.toggle('show', s<=t && t<x);
    });
    el.querySelectorAll('[data-o]').forEach(e=>{ e.classList.toggle('on', +e.dataset.o<=t); e.classList.toggle('cur', +e.dataset.o===t); });
    /* 説明：今の 番 以下で いちばん 新しい もの */
    const ps = [...el.querySelectorAll('.cap [data-m]')];
    const best = ps.filter(p=>+p.dataset.m<=t).pop();
    ps.forEach(p=>p.classList.toggle('cur', p===best));
  });
  const total = maxStep.reduce((a,m)=>a+m+1,0), done = maxStep.slice(0,si).reduce((a,m)=>a+m+1,0)+st+1;
  bar.style.width = (done/total*100)+'%';
  jump.querySelectorAll('.ti').forEach(b=>b.classList.toggle('on', +b.dataset.i===si));
  jump.querySelector('.pgno').textContent = `${si+1} / ${els.length}`;
  ui.textContent = '←→ 進む・戻る　P 自動再生　F 全画面　H 表示を隠す　T 明暗　W 書きこむ';
}
function next(){ if(endOpen()) return; if(st<maxStep[si]) st++; else if(si<els.length-1){ si++; st=0; } else { stopAuto(); return endShow(true); } render(); }
function prev(){ if(endOpen()) return endShow(false); if(st>0) st--; else if(si>0){ si--; st=maxStep[si]; } render(); }

/* 終わりの パネル：最後の ページの 先で 出す。次の プリント・もう一度・一覧 を 選ぶ */
const endp = document.createElement('div'); endp.id = 'endp'; stage.appendChild(endp);
(function(){
  const i = SERIES.findIndex(d=>d.f===ME), nx = SERIES[i+1], pv = SERIES[i-1];
  const url = d => `${d.f}.html?v=${encodeURIComponent(d.v)}`;
  endp.innerHTML = `<div class="ein">
    <div class="ek">${DECK.title}</div><div class="eh">おわり</div>
    ${nx ? `<a class="enext" href="${url(nx)}"><span class="el">次の プリントへ</span><span class="en">${nx.no}</span><span class="et">${nx.t}</span><span class="ea">→</span></a>`
         : `<div class="elast">この 単元の スライドは ここまで です</div>`}
    <div class="ebtns"><button class="eagain">↺ もう一度 最初から</button>
      ${pv ? `<a href="${url(pv)}">← 前の プリント（${pv.no}）</a>` : ''}<a href="index.html">≡ スライドの 一覧へ</a></div>
    <div class="elist">${SERIES.map(d=>`<a class="${d.f===ME?'me':''}" href="${url(d)}"><b>${d.no}</b>${d.t}</a>`).join('')}</div>
    <button class="eback">← 最後の ページに 戻る</button></div>`;
  endp.querySelectorAll('.m').forEach(e=>{ try{ katex.render(e.textContent, e, KX); }catch(_){} });
  endp.querySelector('.eagain').addEventListener('click', e=>{ e.stopPropagation(); endShow(false); si=0; st=0; render(); });
  endp.querySelector('.eback').addEventListener('click', e=>{ e.stopPropagation(); endShow(false); });
})();
function endOpen(){ return endp.classList.contains('open'); }
function endShow(on){ endp.classList.toggle('open', on); if(on){ bar.style.width='100%'; jump.querySelector('.pgno').textContent='おわり'; } else render(); }
function stopAuto(){ if(timer){ clearInterval(timer); timer=null; } }
function toggleAuto(){ if(timer) stopAuto(); else timer=setInterval(next,4000); }

document.addEventListener('keydown', e=>{
  const k = e.key;
  if(['ArrowRight','ArrowDown',' ','Enter','PageDown'].includes(k)){ e.preventDefault(); stopAuto(); next(); }
  else if(['ArrowLeft','ArrowUp','Backspace','PageUp'].includes(k)){ e.preventDefault(); stopAuto(); prev(); }
  else if(k==='Home'){ stopAuto(); si=0; st=0; render(); }
  else if(k==='End'){ stopAuto(); si=els.length-1; st=maxStep[si]; render(); }
  else if(k==='p'||k==='P') toggleAuto();
  else if(k==='f'||k==='F'){ try{ if(document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen(); }catch(_){} }
  else if(k==='h'||k==='H'){ ui.classList.toggle('hide'); bar.classList.toggle('hide'); jump.classList.toggle('hide'); }
  else if(k==='t'||k==='T') toggleTheme();
  else if(k==='Escape'){ tocOpen(false); if(endOpen()) endShow(false); }
});
/* 画面の 左 1/3 を 押すと 戻る、それ以外は 進む */
document.addEventListener('click', e=>{
  if(e.target.closest('a,button,#jump,#inkbar,#endp')) return;
  stopAuto(); if(e.clientX < document.documentElement.clientWidth/3) prev(); else next();
});
/* 画面に 合わせる：縦長（スマホ）なら 720×1280、横長なら 1280×720 */
function fit(){
  const vw = document.documentElement.clientWidth, vh = document.documentElement.clientHeight;
  const portrait = vh > vw;
  document.body.classList.toggle('portrait', portrait);
  const W = portrait?720:1280, H = portrait?1280:720;
  stage.style.setProperty('--s', Math.min(vw/W, vh/H));
}
addEventListener('resize', fit);
/* URL の #3-2 で 4ページ目の 2番から 始める（撮影・リンク用）。#3-e は その ページの 最後。?final で 動きを 止める */
(function(){
  const m = location.hash.match(/^#(\d+)-(\d+|e)$/); if(!m) return;
  si = Math.min(+m[1], els.length-1); st = m[2]==='e' ? maxStep[si] : Math.min(+m[2], maxStep[si]);
})();
if(/final/.test(location.search)) document.body.classList.add('final');
fit(); render();
if(location.hash==='#end') endShow(true);
