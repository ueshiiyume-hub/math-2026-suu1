"""スライドに 機械音声の ナレーションを 付ける（2026-10-31、試作）

使い方:  python _作成用/narrate.py 1-1_因数分解の復習
  1. 原稿 _作成用/narration/<デッキ>.txt を 読む（スライド 1枚ごとに「== 番号 名前 ==」で 区切る。1行 ＝ 1番）
  2. 原稿が 変わった スライドだけ pyopenjtalk で 音声を 作り直す（1枚 ＝ mp3 1つ。期末考査/jugyo/audio/<デッキ>/）
  3. 期末考査/jugyo/<デッキ>.html に 音声の 再生を 足して <デッキ>_音声.html を 書く
     （再生中は 読み終えた 番で 次の 番へ、スライドの 終わりで 次の スライドへ 自動で 進む）
要るもの: pip install pyopenjtalk、ffmpeg
"""
import sys, os, re, json, hashlib, subprocess, tempfile
import numpy as np

B = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(B)
JUGYO = os.path.join(ROOT, '期末考査', 'jugyo')
SR = 48000
GAP = 0.45            # 番と 番の 間（秒）
EMPTY = 0.8           # 原稿の ない 番の 長さ（秒）
VOICE = dict(speed=1.1, half_tone=0.0)   # 声の 設定（変えると 全部 作り直し）


def parse(path):
    """原稿 → {スライド番号(0から): [(番, 文), …]}"""
    slides, cur = {}, None
    for ln in open(path, encoding='utf-8').read().splitlines():
        t = ln.strip()
        if not t or t.startswith('#'):
            continue
        m = re.match(r'^==\s*(\d+)', t)
        if m:
            cur = int(m.group(1)) - 1
            slides[cur] = []
            continue
        m = re.match(r'^(\d+)\s*[:：]\s*(.*)$', t)
        if cur is None or not m:
            sys.exit(f'原稿の 書き方が ちがう 行：{ln}')
        slides[cur].append((int(m.group(1)), m.group(2).strip()))
    return slides


def synth(lines):
    """1枚ぶんの 音声（numpy）と、各 番の 始まりの 秒"""
    import pyopenjtalk
    last = max(k for k, _ in lines)
    say = dict(lines)
    parts, marks, t = [], [], 0.0
    for k in range(last + 1):
        marks.append(round(t, 3))
        txt = say.get(k, '')
        if txt and txt != '＿':
            x, sr = pyopenjtalk.tts(re.sub(r'[ 　]', '', txt), **VOICE)   # 空白は 読みやすさ用（間が 空きすぎる ので 消す。間は 「、」で）
            assert sr == SR
            x = np.concatenate([x, np.zeros(int(SR * GAP))])
        else:
            x = np.zeros(int(SR * EMPTY))
        parts.append(x)
        t += len(x) / SR
    return np.concatenate(parts), marks


def to_mp3(x, path):
    pcm = np.clip(x, -32768, 32767).astype('<i2').tobytes()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-',
                    '-ar', '24000', '-b:a', '48k', path], input=pcm, check=True)


def main(deck):
    src = os.path.join(B, 'narration', deck + '.txt')
    man_p = os.path.join(B, 'narration', deck + '.json')
    adir = os.path.join(JUGYO, 'audio', deck)
    os.makedirs(adir, exist_ok=True)
    slides = parse(src)
    man = json.load(open(man_p, encoding='utf-8')) if os.path.exists(man_p) else {}
    new, made = {}, []
    for i, lines in sorted(slides.items()):
        h = hashlib.sha1(json.dumps([lines, VOICE], ensure_ascii=False).encode()).hexdigest()[:10]
        f = f's{i + 1:02d}.mp3'
        old = man.get(str(i))
        if old and old['h'] == h and os.path.exists(os.path.join(adir, f)):
            new[str(i)] = old
            continue
        x, marks = synth(lines)
        to_mp3(x, os.path.join(adir, f))
        new[str(i)] = {'f': f, 'h': h, 'm': marks}
        made.append(i + 1)
    for k, v in man.items():                     # 原稿から 消した スライドの 音声は 消す
        if k not in new and os.path.exists(os.path.join(adir, v['f'])):
            os.remove(os.path.join(adir, v['f']))
    json.dump(new, open(man_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # スライドに 組みこむ
    html = open(os.path.join(JUGYO, deck + '.html'), encoding='utf-8').read()
    data = {'dir': f'audio/{deck}/', 's': {int(k): v for k, v in new.items()}}
    add = (f'<style>{open(os.path.join(B, "narrate.css"), encoding="utf-8").read()}</style>\n'
           f'<script>const NARR = {json.dumps(data, ensure_ascii=False)};</script>\n'
           f'<script>{open(os.path.join(B, "narrate.js"), encoding="utf-8").read()}</script>\n')
    html = html.replace('</body>', add + '</body>', 1)
    open(os.path.join(JUGYO, deck + '_音声.html'), 'w', encoding='utf-8').write(html)
    print(f'ok {deck}：作り直した スライド {made if made else "なし"}（全 {len(new)} 枚）')


if __name__ == '__main__':
    main(sys.argv[1])
