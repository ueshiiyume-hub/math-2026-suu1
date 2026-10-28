/* ====== 手書き（授業中に スライドの上から 書きこむ） ======
   右上の ✏ ボタン か W キーで 書く。やめる ときは 右下の 大きな「スライドに 戻る」（または W・Esc）。ペンの 後ろ（消しゴム側）で なぞると 消える。
   ペン（Surface ペンなど）で 画面に さわると、自動で 書くモードに なる。
   書いた線は スライドごとに 残る（ページを 開き直すと 消える）。
   線は 台紙（1280×720 / 720×1280）の 座標で 覚えるので、画面の 大きさが 変わっても ずれない。 */
var INK = {on:false, color:'#e0465e', tool:'pen', w:3.5, strokes:{}, cur:null};
(function(){
  const cv = document.createElement('canvas'); cv.id = 'ink'; document.body.appendChild(cv);
  const ctx = cv.getContext('2d');
  const bar = document.createElement('div'); bar.id = 'inkbar';
  const COLORS = [['#e0465e','赤'],['#1f3f9e','青'],['#f07a12','オレンジ'],['#1f9a4a','緑'],['#33303d','黒']];
  const SIZES = [[3.5,'細'],[5,'太']];   // 細 が 最初
  bar.innerHTML = `<button class="ink-tg" title="書きこむ（W）">✏</button>
    <span class="ink-tools">${COLORS.map(([c,n])=>`<button class="ink-c" data-c="${c}" title="${n}" style="--c:${c}"></button>`).join('')}
    <span class="ink-sep"></span>${SIZES.map(([w,n])=>`<button class="ink-w" data-w="${w}" title="${n}"><i style="width:${w*2}px;height:${w*2}px"></i></button>`).join('')}<span class="ink-sep"></span>
    <button class="ink-er" title="消しゴム（E）">消</button><button class="ink-un" title="1つ戻す（Ctrl+Z）">↶</button>
    <button class="ink-cl" title="このページを 全部 消す">全消</button></span>`;
  document.body.appendChild(bar);
  /* 書くモードから スライドに 戻る：大きな ボタンを 右下に 出す（右上の ✏ は 小さくて 押しにくい ため、2026-10-28） */
  const back = document.createElement('button'); back.id = 'inkback'; back.type = 'button';
  back.innerHTML = '<span class="ib-i">▶</span>スライドに 戻る'; back.title = '書くのを やめて スライドを 進める（W・Esc）';
  back.addEventListener('pointerdown', e=>e.stopPropagation());
  back.addEventListener('click', e=>{ e.stopPropagation(); e.preventDefault(); setOn(false); back.blur(); });
  document.body.appendChild(back);
  const key = () => si + (document.body.classList.contains('portrait') ? 'p' : 'l');
  const list = () => (INK.strokes[key()] ||= []);
  /* 画面の点 ⇔ 台紙の点 */
  const box = () => stage.getBoundingClientRect();
  const sz  = () => document.body.classList.contains('portrait') ? [720,1280] : [1280,720];
  const toStage = (x,y) => { const b=box(), [W,H]=sz(); return [(x-b.left)/b.width*W, (y-b.top)/b.height*H]; };
  function size(){
    const r = devicePixelRatio || 1;
    cv.width = innerWidth * r; cv.height = innerHeight * r;
    cv.style.width = innerWidth + 'px'; cv.style.height = innerHeight + 'px';
    draw();
  }
  function draw(){
    const r = devicePixelRatio || 1, b = box(), [W] = sz(), k = b.width / W;
    ctx.setTransform(r,0,0,r,0,0); ctx.clearRect(0,0,innerWidth,innerHeight);
    ctx.setTransform(r*k,0,0,r*k,r*b.left,r*b.top);
    ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    for(const s of list()){
      ctx.strokeStyle = s.c; ctx.lineWidth = s.w; ctx.beginPath();
      s.p.forEach(([x,y],i)=> i ? ctx.lineTo(x,y) : ctx.moveTo(x,y));
      if(s.p.length===1) ctx.lineTo(s.p[0][0]+.1, s.p[0][1]);
      ctx.stroke();
    }
  }
  function erase(x,y){
    const L = list(), n = L.length;
    for(let i=L.length-1;i>=0;i--) if(L[i].p.some(([a,b])=>Math.hypot(a-x,b-y)<16)) L.splice(i,1);
    if(L.length!==n) draw();
  }
  function setOn(v){
    INK.on = v; document.body.classList.toggle('inking', v);
    if(!v) INK.cur = null;
  }
  function setTool(t,c){
    INK.tool = t; if(c) INK.color = c;
    bar.querySelectorAll('.ink-c').forEach(b=>b.classList.toggle('sel', t==='pen' && b.dataset.c===INK.color));
    bar.querySelector('.ink-er').classList.toggle('sel', t==='er');
    bar.querySelectorAll('.ink-w').forEach(b=>b.classList.toggle('sel', +b.dataset.w===INK.w));
  }
  function start(e){
    e.preventDefault(); try{ cv.setPointerCapture(e.pointerId); }catch(_){}
    const p = toStage(e.clientX,e.clientY);
    /* ペンの 後ろ（消しゴム側）で さわったら 消しゴム。Surface ペンなどは buttons に 32 が 入る */
    const back = e.pointerType==='pen' && (e.button===5 || (e.buttons & 32));
    if(INK.tool==='er' || back){ INK.cur = {er:true}; erase(...p); return; }
    INK.cur = {c:INK.color, w:INK.w, p:[p]}; list().push(INK.cur); draw();
  }
  cv.addEventListener('pointerdown', e=>{ if(INK.on) start(e); });
  /* ペンを 近づけた（さわる前の ホバー）時点で、ブラウザの スクロール・拡大の 判定を 止める。
     止めないと、ペンで さわって すぐ 書き始めた線が 0.3秒ほどで 打ち切られる（pointercancel） */
  const penSeen = e => { if(e.pointerType==='pen') document.body.classList.add('pen-dev'); };
  ['pointerover','pointermove','pointerdown'].forEach(t=>document.addEventListener(t, penSeen, {capture:true, passive:true}));
  /* ペンで 画面に さわったら、自動で 書くモードに する（ボタンや リンクは ふつうに 押せる） */
  let skipClick = false;
  document.addEventListener('pointerdown', e=>{
    if(INK.on || e.pointerType!=='pen' || e.target.closest('#inkbar,#jump,a,button')) return;
    setOn(true); if(INK.tool!=='er') setTool('pen'); skipClick = true; start(e);
  }, true);
  document.addEventListener('click', e=>{ if(skipClick){ skipClick = false; e.stopPropagation(); e.preventDefault(); } }, true);
  cv.addEventListener('pointermove', e=>{
    if(!INK.cur) return;
    const evs = e.getCoalescedEvents ? e.getCoalescedEvents() : [e];
    for(const ev of evs){
      const p = toStage(ev.clientX,ev.clientY);
      if(INK.cur.er) erase(...p); else INK.cur.p.push(p);
    }
    if(!INK.cur.er) draw();
  });
  const end = () => { INK.cur = null; };
  cv.addEventListener('pointerup', end); cv.addEventListener('pointercancel', end);
  cv.addEventListener('click', e=>e.stopPropagation());
  bar.addEventListener('click', e=>{
    e.stopPropagation();
    const b = e.target.closest('button'); if(!b) return;
    if(b.classList.contains('ink-tg')){ setOn(!INK.on); if(INK.on) setTool('pen'); }
    else if(b.classList.contains('ink-c')) setTool('pen', b.dataset.c);
    else if(b.classList.contains('ink-w')){ INK.w = +b.dataset.w; setTool('pen'); }
    else if(b.classList.contains('ink-er')) setTool('er');
    else if(b.classList.contains('ink-un')){ list().pop(); draw(); }
    else if(b.classList.contains('ink-cl')){ INK.strokes[key()] = []; draw(); }
    b.blur();
  });
  document.addEventListener('keydown', e=>{
    const k = e.key;
    if(k==='w'||k==='W'){ setOn(!INK.on); if(INK.on) setTool('pen'); }
    else if(INK.on && (k==='e'||k==='E')) setTool(INK.tool==='er' ? 'pen' : 'er');
    else if(INK.on && k==='Escape') setOn(false);
    else if(k==='h'||k==='H') bar.classList.toggle('hide');
    else if((e.ctrlKey||e.metaKey) && (k==='z'||k==='Z')){ e.preventDefault(); list().pop(); draw(); }
  });
  /* ページを めくったら、そのページの 線を かく */
  const r0 = render; render = function(){ r0(); draw(); };
  addEventListener('resize', size);
  setTool('pen'); size();
})();
