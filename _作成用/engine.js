/* ====== 組み立て・操作 ====== */
const stage = document.getElementById('stage');
const pages = DECK.pages.map(x=>x.html), names = DECK.pages.map(x=>x.name);
document.title = DECK.title;
/* スライドの種類（スマホの縦レイアウトで使う） */
const kind = h => /pgcard|ptcard|dcard|dsum/.test(h)?'pg' : /kcard/.test(h)?'k' : /kfcard/.test(h)?'f' : /qecard/.test(h)?'q' : /ncard/.test(h)?'n' : /class="pcards/.test(h)?'p' : /fxcard/.test(h)?'x' : /class="hrows/.test(h)?'h' : /class="graph"/.test(h)?'g' : /wcard/.test(h)?'w' : /fcard/.test(h)?'b' : 'c';
stage.innerHTML = pages.map(h=>`<section class="slide t-${kind(h)}">${h}</section>`).join('');
(function italicVars(){
  const w=document.createTreeWalker(stage,NodeFilter.SHOW_TEXT);
  const nodes=[]; while(w.nextNode()) nodes.push(w.currentNode);
  nodes.forEach(n=>{
    if(!/[A-Za-z]/.test(n.nodeValue)) return;
    if(n.parentNode.closest && (n.parentNode.closest('svg')||n.parentNode.closest('i'))) return;
    const f=document.createDocumentFragment();
    n.nodeValue.split(/([A-Za-z])/).forEach(t=>{
      if(/^[A-Za-z]$/.test(t)){const i=document.createElement('i');i.className='v';i.textContent=t;f.appendChild(i);}
      else if(t) f.appendChild(document.createTextNode(t));
    });
    n.parentNode.replaceChild(f,n);
  });
})();
(function backdrop(){
  const bg=document.getElementById('bg');
  const items=[['dot',3,12,1.6,'#f5c2cc'],['star',6,80,2.6,'#f8e2a2'],['dot',95,8,1.2,'#bfe5d0'],['star',92,60,2.2,'#d8cdf1'],
               ['dot',50,4,1,'#c4d8f2'],['star',30,94,1.8,'#f5c2cc'],['dot',70,95,1.4,'#f8e2a2'],['dot',97,90,2,'#f5c2cc'],['star',2,45,1.6,'#c4d8f2']];
  items.forEach(([k,l,t,z,c],i)=>{
    const d=document.createElement('div'); d.className='deco '+k;
    d.style.cssText=`left:${l}%;top:${t}%;width:${z}vmin;height:${z}vmin;--c:${c};--t:${5+(i%3)}s;--d:${-i*.9}s`;
    bg.appendChild(d);
  });
})();

const els = [...stage.querySelectorAll('.slide')];
const stepAttr = e => [e.dataset.s,e.dataset.o,e.dataset.m,e.dataset.f,e.dataset.a,e.dataset.wa].filter(v=>v!==undefined).map(Number).filter(v=>v<90);
const maxStep = els.map(el => Math.max(0,...[...el.querySelectorAll('[data-s],[data-o],[data-m],[data-f],[data-a],[data-wa]')].flatMap(stepAttr)));

/* 飛んでくる数：出発点までの距離を測る */
function pos(el){
  let x=0,y=0;
  while(el && !el.classList.contains('slide')){
    x+=el.offsetLeft; y+=el.offsetTop;
    const p=el.offsetParent;
    if(p && !p.classList.contains('slide')){ x+=p.clientLeft; y+=p.clientTop; }
    el=p;
  }
  return [x,y];
}
function layoutFly(root){
  root.querySelectorAll('.fly').forEach(e=>{
    const src=e.closest('.slide').querySelector(`[data-k="${e.dataset.src}"]`);
    if(!src) return;
    const [sx,sy]=pos(src), [tx,ty]=pos(e);
    e.style.setProperty('--fx',((sx+src.offsetWidth/2)-(tx+e.offsetWidth/2))+'px');
    e.style.setProperty('--fy',((sy+src.offsetHeight/2)-(ty+e.offsetHeight/2))+'px');
  });
}
/* 分配線：かっこの外の数の上から、かっこの中の2つの上へ アーチを描く */
function layoutDist(root){
  root.querySelectorAll('.dist').forEach(svg=>{
    const sl=svg.closest('.slide'), base=pos(svg.parentElement);
    const rel=el=>{ const [x,y]=pos(el); return [x-base[0], y-base[1], el.offsetWidth, el.offsetHeight]; };
    svg.querySelectorAll('.dg').forEach(g=>{
      const fr=sl.querySelector(`[data-k="${g.dataset.fr}"]`), to=sl.querySelector(`[data-k="${g.dataset.to}"]`);
      if(!fr||!to) return;
      const [fx,fy,fw]=rel(fr), [tx,ty,tw]=rel(to), H=+g.dataset.h, dx=+g.dataset.dx;
      const x1=fx+fw/2+dx, y1=fy-2, x2=tx+tw/2, y2=ty-4;
      g.querySelector('path').setAttribute('d',`M${x1} ${y1} C${x1} ${y1-H} ${x2} ${y2-H-10} ${x2} ${y2-14}`);
      g.querySelector('polygon').setAttribute('points',`${x2-8},${y2-15} ${x2+8},${y2-15} ${x2},${y2}`);
    });
  });
}
const relayout = r => { layoutFly(r); layoutDist(r); if(typeof layoutExtra==='function') layoutExtra(r); };
if(document.fonts&&document.fonts.ready) document.fonts.ready.then(()=>relayout(stage));
const bar = document.getElementById('bar'), ui = document.getElementById('ui');
const jump = document.getElementById('jump');
jump.innerHTML='<a class="home" href="目次.html">目次</a><span>ジャンプ</span>'+names.map((n,i)=>`<button data-i="${i}">${n}</button>`).join('');
jump.addEventListener('click',e=>{
  e.stopPropagation();
  const b=e.target.closest('button'); if(!b) return;
  stopAuto(); si=+b.dataset.i; st=0; render(); b.blur();
});
let si = 0, st = 0, timer = null, layoutTimer = null;

function render(){
  relayout(els[si]);
  clearTimeout(layoutTimer); layoutTimer=setTimeout(()=>relayout(els[si]),700);
  els.forEach((el,i)=>{
    const past=i<si, now=i===si;
    el.querySelectorAll('[data-f]').forEach(e=>e.classList.toggle('go', past || (now && +e.dataset.f<=st)));
    el.querySelectorAll('[data-a]').forEach(e=>e.classList.toggle('ul-on', past || (now && +e.dataset.a<=st)));
    el.querySelectorAll('[data-wa]').forEach(e=>e.classList.toggle('wv-on', now && +e.dataset.wa<=st && st<+e.dataset.wb));
    el.classList.toggle('active', now);
    el.classList.toggle('past', past);
    el.querySelectorAll('[data-s]').forEach(e=>e.classList.toggle('show', past || (now && +e.dataset.s<=st)));
    el.querySelectorAll('[data-o]').forEach(e=>{ e.classList.toggle('on', past || (now && +e.dataset.o<=st)); e.classList.toggle('cur', now && +e.dataset.o===st); });
    el.querySelectorAll('[data-m]').forEach(e=>e.classList.toggle('cur', now && +e.dataset.m===st));
  });
  const total = maxStep.reduce((a,m)=>a+m+1,0);
  const done = maxStep.slice(0,si).reduce((a,m)=>a+m+1,0)+st+1;
  bar.style.width = (done/total*100)+'%';
  [...jump.querySelectorAll('button')].forEach(b=>b.classList.toggle('on',+b.dataset.i===si));
  ui.textContent = `${si+1} / ${els.length}　←→ 進む・戻る　P 自動再生　Home 最初から　F 全画面　H 表示を隠す　T 明暗${typeof INK!=='undefined'?'　W 書きこむ':''}`;
}
function next(){ if(st<maxStep[si]) st++; else if(si<els.length-1){si++;st=0;} else stopAuto(); render(); }
function prev(){ if(st>0) st--; else if(si>0){si--;st=maxStep[si];} render(); }
function stopAuto(){ if(timer){ clearInterval(timer); timer=null; } }
function toggleAuto(){ if(timer) stopAuto(); else timer=setInterval(next,4000); }

document.addEventListener('keydown',e=>{
  const k=e.key;
  if(['ArrowRight','ArrowDown',' ','Enter','PageDown'].includes(k)){e.preventDefault();stopAuto();next();}
  else if(['ArrowLeft','ArrowUp','Backspace','PageUp'].includes(k)){e.preventDefault();stopAuto();prev();}
  else if(k==='Home'){stopAuto();si=0;st=0;render();}
  else if(k==='End'){stopAuto();si=els.length-1;st=maxStep[si];render();}
  else if(k==='p'||k==='P'){toggleAuto();}
  else if(k==='f'||k==='F'){ try{ if(document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen(); }catch(_){} }
  else if(k==='h'||k==='H'){ ui.classList.toggle('hide'); bar.classList.toggle('hide'); jump.classList.toggle('hide'); }
  else if(k==='t'||k==='T'){
    if(typeof toggleTheme==='function') toggleTheme();
    else { const d=document.documentElement;
      const dark = d.dataset.theme ? d.dataset.theme==='dark' : matchMedia('(prefers-color-scheme: dark)').matches;
      d.dataset.theme = dark ? 'light' : 'dark'; }
  }
});
document.addEventListener('click',e=>{ if(e.target.closest('a')) return; stopAuto(); if(e.clientX < document.documentElement.clientWidth/3) prev(); else next(); });
/* 画面に合わせる：縦長（スマホ）なら 720×1280、横長なら 1280×720 */
function fit(){
  const vw = document.documentElement.clientWidth, vh = document.documentElement.clientHeight;   // スマホでは innerWidth がずれることがある
  const portrait = vh > vw;
  document.body.classList.toggle('portrait', portrait);
  const W = portrait?720:1280, H = portrait?1280:720, avail = vh - (portrait?52:0);
  stage.style.setProperty('--s', Math.min(vw/W, avail/H));
  jump.style.top = portrait ? (vh-46)+'px' : '';   // スマホでは画面の下にそろえる
  jump.style.bottom = portrait ? 'auto' : '';
  relayout(els[si]);
}
addEventListener('resize',fit); fit(); render();
