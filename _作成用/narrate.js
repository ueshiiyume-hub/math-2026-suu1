/* ナレーション（narrate.py が 組みこむ）。NARR = {dir, s:{スライド番号:{f:mp3, h:版, m:[各 番の 始まりの 秒]}}}
   「▶ 音声」で 再生。読み終えた 番で 次の 番へ、スライドの 終わりで 次の スライドへ 自動で 進む。
   再生中に 手で 進める・戻すと、その 番の ところから 読み直す。N キーでも 再生・停止 */
(function(){
  const au = new Audio(); au.preload = 'auto';
  let on = false, cur = -1, mine = false, gapT = null, raf = 0;
  const S = i => NARR.s[i];
  const btn = document.createElement('button'); btn.id = 'narbtn'; btn.type = 'button';
  const hint = document.createElement('div'); hint.id = 'narhint'; hint.textContent = '▶ 音声つきで 見る（タップ）';
  document.body.appendChild(hint);
  function paint(){ btn.innerHTML = on ? '❚❚ 音声を 止める<span class="nbar"></span>' : '▶ 音声'; btn.classList.toggle('on', on); hint.hidden = true; }
  (document.getElementById('jump') || document.body).appendChild(btn);
  function step(){ mine = true; next(); mine = false; }
  function gap(){                       // 音声の ない 番・スライド：少し 待って 進む
    clearTimeout(gapT);
    gapT = setTimeout(()=>{ if(!on) return; if(endOpen()){ stop(); return; } step(); if(endOpen()) stop(); else play(); }, 900);
  }
  function play(){
    clearTimeout(gapT); cancelAnimationFrame(raf);
    const s = S(si);
    if(!s || st >= s.m.length){ au.pause(); cur = -1; return gap(); }
    const t = s.m[st];
    const go = () => { au.currentTime = t; au.play().then(watch).catch(()=>stop()); };
    if(cur !== si){ cur = si; au.src = NARR.dir + s.f + '?v=' + s.h; au.addEventListener('loadedmetadata', go, {once:true}); au.load(); }
    else go();
  }
  function watch(){                     // 次の 番の 始まりを 過ぎたら 進める
    cancelAnimationFrame(raf);
    const tick = () => {
      if(!on || au.paused) return;
      const s = S(si);
      if(s && st + 1 < s.m.length && au.currentTime >= s.m[st + 1]) step();
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
  }
  au.addEventListener('ended', ()=>{
    if(!on) return;
    if(st < maxStep[si]){ step(); return gap(); }   // 原稿より 番が 多い ときは 少しずつ 進める
    step();
    if(endOpen()) stop(); else play();
  });
  function start(){ on = true; paint(); play(); }
  function stop(){ on = false; clearTimeout(gapT); cancelAnimationFrame(raf); au.pause(); paint(); }
  btn.addEventListener('click', e=>{ e.stopPropagation(); on ? stop() : start(); });
  hint.addEventListener('click', e=>{ e.stopPropagation(); start(); });
  document.addEventListener('keydown', e=>{ if(e.key==='n'||e.key==='N') on ? stop() : start(); });
  const _render = render;                       // 手で 動かしたら、その 番から 読み直す
  render = function(){ _render(); if(on && !mine) play(); };
  paint(); hint.hidden = false;
})();
