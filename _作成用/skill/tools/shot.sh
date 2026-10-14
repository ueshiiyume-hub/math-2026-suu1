#!/usr/bin/env bash
# スライドの「ある場面」を Chrome（ヘッドレス）で撮影する
# 使い方: shot.sh <スライド.html> <幅> <高さ> <スライド番号-ステップ> ...
#   ステップに e を書くと そのスライドの最後の場面（例: 2-e）。0始まり。
#   横長 1280 720 / スマホ縦長 540 960 の 両方で 確かめる。
# FINAL=1 を つけると アニメーションを 止めて 最後の 形で 撮る
# 出力: $OUTDIR（なければ ./_shot）/<幅>_<番号-ステップ>.png
SRC="$1"; W=$2; H=$3; shift 3
OUT="${OUTDIR:-./_shot}"; mkdir -p "$OUT"
# Windows（Git Bash）では Chrome、Linux（クラウド）では /opt/pw-browsers/chromium
if [ -z "$CHROME" ]; then
  if [ -x "/c/Program Files/Google/Chrome/Application/chrome.exe" ]; then CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
  else CHROME="$(ls /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -1)"; fi
fi
DIR="$(cd "$OUT" && (pwd -W 2>/dev/null || pwd))"
for k in "$@"; do
  s=${k%-*}; t=${k#*-}
  python - "$SRC" "$OUT/p.html" "$s" "$t" <<'PY'
import sys
src,dst,s,t=sys.argv[1:]
h=open(src,encoding='utf-8').read()
st='maxStep[si]' if t=='e' else t
h=h.replace('</body>',f'<script>si={s};st={st};fit();render();document.querySelectorAll("*").forEach(e=>e.style.transitionDuration="0s");</script></body>')
import os
if os.environ.get('FINAL'): h=h.replace('</head>','<style>*{transition:none!important;animation-duration:0s!important;animation-delay:0s!important}</style></head>')
open(dst,'w',encoding='utf-8').write(h)
PY
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=$W,$H --virtual-time-budget=4000 --screenshot="$OUT/${W}_$k.png" --no-sandbox "file:///${DIR#/}/p.html" 2>/dev/null
done
