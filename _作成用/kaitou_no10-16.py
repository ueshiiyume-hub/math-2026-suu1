# No.10〜16（③ 2次不等式）の 答え（kaitou.py が 読みこむ。2026-11-11）
# 座標は プリントの pt。印刷された グラフ（画像）は GEO() で 読みとり、その 上に 塗りと 白丸・黒丸を 重ねる
import io
from PIL import Image

LIGHT = 0.45   # 塗りの 濃さ（下の 線が 見える）

def X2(rest, c=''):
    """c x² rest（例：X2(' − 2x − 3')）"""
    return [c + 'x', P('2'), rest]

def _img(xref):
    ex = src.extract_image(xref)
    im = Image.open(io.BytesIO(ex['image'])).convert('RGBA')
    if ex.get('smask'):
        im.putalpha(Image.open(io.BytesIO(src.extract_image(ex['smask'])['image'])).convert('L'))
    return im

def GEO(i):
    """プリントの ページ i の グラフ（放物線の 画像 と x軸の 画像）を 読む → [{xv, yv, q, top, ay, x0, x1}]（上から、左から）"""
    pbs, axs = [], []
    for m in src[i].get_image_info(xrefs=True):
        x0, y0, x1, y1 = m['bbox']
        W, H = m['width'], m['height']
        if W == 173:
            pbs.append((x0, y0, x1, y1, m['xref']))
        elif y1 - y0 < 26 and x1 - x0 > 80 and 240 <= W <= 300:
            axs.append((x0, y0, x1, y1, m['xref']))
    def dark(px, x, y):
        r, g, b, a = px[x, y]
        return a > 100 and r + g + b < 400
    ax = []
    for x0, y0, x1, y1, xr in axs:
        im = _img(xr); px = im.load(); W, H = im.size
        rows = [sum(1 for x in range(W) if dark(px, x, y)) for y in range(H)]
        yb = max(range(H), key=lambda y: rows[y])
        ax.append((x0, x1, y0 + (yb + .5) * (y1 - y0) / H))
    out = []
    for x0, y0, x1, y1, xr in pbs:
        im = _img(xr); px = im.load(); W, H = im.size
        sx, sy = (x1 - x0) / W, (y1 - y0) / H
        cols = [[y for y in range(H) if dark(px, x, y)] for x in range(W)]
        ys = [y for c in cols for y in c]
        bot, top = max(ys), min(ys)
        xb = [x for x in range(W) if cols[x] and max(cols[x]) == bot]
        xt = [x for x in range(W) if cols[x] and min(cols[x]) == top]
        xv = x0 + (sum(xb) / len(xb) + .5) * sx
        tl, tr = x0 + (min(xt) + .5) * sx, x0 + (max(xt) + .5) * sx
        yv, yt = y0 + (bot + .5) * sy - .6, y0 + (top + .5) * sy + .6
        hw = (tr - tl) / 2
        q = (yv - yt) / hw ** 2
        cand = [a for a in ax if a[0] - 2 <= xv <= a[1] + 2]
        ay = min(cand, key=lambda a: abs(a[2] - yv))[2]
        out.append(dict(xv=xv, yv=yv, q=q, top=yt, ay=ay))
    out.sort(key=lambda g: (round(g['ay'] / 20), g['xv']))
    return out

def AXES(i):
    """x軸だけ の 画像（グラフを 書く 枠の 中）の y を 上から"""
    res = []
    for m in src[i].get_image_info(xrefs=True):
        x0, y0, x1, y1 = m['bbox']; W = m['width']
        if y1 - y0 < 26 and x1 - x0 > 80 and 240 <= W <= 300:
            im = _img(m['xref']); px = im.load(); w, h = im.size
            rows = [sum(1 for x in range(w) if px[x, y][3] > 100 and sum(px[x, y][:3]) < 400) for y in range(h)]
            yb = max(range(h), key=lambda y: rows[y])
            res.append(y0 + (yb + .5) * (y1 - y0) / h)
    return sorted(res)

def PAINT(g, mode, eq, draw_curve=False, labs=(), s=7):
    """グラフを 塗る。mode：'up'（上）・'down'（下）・None。eq：＝ が ある（黒丸）。点は x軸との 共有点"""
    xv, yv, q, top, ay = g['xv'], g['yv'], g['q'], g['top'], g['ay']
    hw = ((yv - top) / q) ** .5
    f = lambda x: yv - q * (x - xv) ** 2
    xs = [xv - hw + 2 * hw * i / 160 for i in range(161)]
    if draw_curve:
        pg.draw_polyline([(x, f(x)) for x in xs], color=RED, width=1.2)
    if mode:
        ok = (lambda y: y < ay - 0.15) if mode == 'up' else (lambda y: y > ay + 0.15)
        cur = []
        for x in xs + [None]:
            if x is not None and ok(f(x)):
                cur.append((x, f(x)))
            else:
                if len(cur) > 1:
                    pg.draw_polyline(cur, color=RED, width=3.6, stroke_opacity=LIGHT)
                cur = []
    if yv > ay + 2.2:
        r = ((yv - ay) / q) ** .5; roots = [xv - r, xv + r]
    elif abs(yv - ay) <= 2.2:          # 接する（印刷の 線の 太さ ぶん ずれる）
        roots = [xv]
    else:
        roots = []
    for x in roots:
        pg.draw_circle((x, ay), 2.2, color=RED, fill=RED if eq else (1, 1, 1), width=0.9)
    for x, e in zip(roots, labs):
        w, a, d = measure(e, s)
        lx = x - w / 2 if len(roots) == 1 else (x - w - 3 if x < xv else x + 3)
        draw(pg, e, lx, ay + 4 + a, s)
    piece([xv - hw - 3, top - 3, xv + hw + 3, max(yv, ay) + (14 if labs else 4)])
    return roots

def PAIR(gs, bs):
    """答えの 枠 ごとに、その 上の グラフを 選ぶ（枠の 順＝問題の 順）"""
    out = []
    for b in bs:
        c = [g for g in gs if b[0] < g['xv'] < b[2] and g['ay'] < b[1]]
        out.append((max(c, key=lambda g: g['ay']), b))
    return out

def BOXES(i):
    """答えの 枠（うすい 灰色の 四角）を 上から、左から"""
    bs = []
    for dr in src[i].get_drawings():
        c, r = dr.get('color'), dr['rect']
        if c and not dr.get('fill') and abs(c[0] - 0.85) < 0.03 and r.width > 80:
            bs.append([r.x0, r.y0, r.x1, r.y1])
    return sorted(bs, key=lambda b: (round(b[1]), b[0]))

def AXIS(x0, x1, ay):
    """x軸を かく（白紙の ところに 書く グラフ用）"""
    pg.draw_line((x0, ay), (x1, ay), color=RED, width=0.7)
    pg.draw_polyline([(x1 - 4, ay - 1.8), (x1, ay), (x1 - 4, ay + 1.8)], color=RED, width=0.7)
    draw(pg, 'x', x1 - 4, ay + 9, 7)

def STRIKE2(x0, x1, y):
    """元の 式を 二重線で 消す（③-4、11/8 先生の 指示）"""
    pg.draw_line((x0, y - 1.3), (x1, y - 1.3), color=RED, width=0.8)
    pg.draw_line((x0, y + 1.3), (x1, y + 1.3), color=RED, width=0.8)
    piece([x0, y - 3, x1, y + 3])

LE, GE = '≦', '≧'
SIGNS = ['up', 'down', 'up', 'down']

# ===== No.10 ③-1 練習編 =====
pen.page(9)
G('③-1 塗る ところ')
for r, t in zip([[197.4, 89.8, 244.4, 118.2], [197.4, 143.8, 244.4, 172.2], [197.4, 197.8, 297.4, 226.2], [197.4, 251.8, 297.4, 280.2]],
                ['上', '下', '上 と x軸', '下 と x軸']):
    center(pg, t, r, 13)
ANS10 = [['x < −1,  3 < x', '−1 < x < 3', ['x ', LE, ' −1,  3 ', LE, ' x'], ['−1 ', LE, ' x ', LE, ' 3']],
         ['1以外のすべての実数', '解なし', 'すべての実数', 'x = 1'],
         ['すべての実数', '解なし', 'すべての実数', '解なし']]
g10, b10 = GEO(9), BOXES(9)
for k, (g, b) in enumerate(PAIR(g10, b10)):
    r, j = divmod(k, 4)
    G(f'③-1 {"⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿"[k]}')
    PAINT(g, SIGNS[j], j >= 2)
    center(pg, ANS10[r][j], b, 12)

# ===== No.11 プリント問題③-1 =====
pen.page(10)
ANS11 = [('up', 0, 'x < −1,  2 < x'), ('down', 0, '−1 < x < 2'), ('up', 1, ['x ', LE, ' −1,  2 ', LE, ' x']), ('down', 1, ['−1 ', LE, ' x ', LE, ' 2']),
         ('up', 0, '2以外のすべての実数'), ('down', 0, '解なし'), ('up', 1, 'すべての実数'), ('down', 1, 'x = 2'),
         ('up', 0, 'すべての実数'), ('down', 0, '解なし'), ('up', 1, 'すべての実数'), ('down', 1, '解なし'),
         ('up', 1, ['x ', LE, ' 2,  3 ', LE, ' x']), ('down', 0, '解なし'), ('up', 1, 'すべての実数'), ('down', 1, ['0 ', LE, ' x ', LE, ' 2']),
         ('up', 0, '−2以外のすべての実数'), ('down', 0, '解なし'), ('up', 1, 'すべての実数'),
         ('down', 1, [F(['1 − ', R('5')], '2'), ' ', LE, ' x ', LE, ' ', F(['1 + ', R('5')], '2')])]
g11, b11 = GEO(10), BOXES(10)
NO20 = '⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇'
for k, ((g, b), (m, eq, a_)) in enumerate(zip(PAIR(g11, b11), ANS11)):
    G(f'プリント問題③-1 {NO20[k]}')
    PAINT(g, m, eq)
    center(pg, a_, b, 12)

# ===== No.12 ③-2 2次不等式の解法 =====
pen.page(11)
G('③-2 2次不等式の解き方')
for r, t, s in [([182.9, 109.7, 302.7, 138], 'x軸との共有点', 12), ([163.5, 146.1, 266.2, 174.5], ['y = 0（2次方程式）'], 11),
                ([244.9, 182.1, 282.6, 210.4], '上', 13), ([370.7, 182.1, 408.4, 210.4], '下', 13), ([192, 218.1, 229.8, 246.4], 'x軸', 12)]:
    center(pg, t, r, s)
g12 = GEO(11)
g12s = [g for g in g12 if g['ay'] > 450]          # Step❷ の 印刷された グラフ（⑴・⑵）
g12s.sort(key=lambda g: g['ay'])
for dy, no, eqs, labs, mode, eq, an, gs in [
        (0, '⑴', [X2(' − 2x − 3', 'y = '), X2(' − 2x − 3 = 0'), '(x + 1)(x − 3) = 0', 'x = −1, 3'], ('−1', '3'), 'up', False, 'x < −1,  3 < x', g12s[0]),
        (252, '⑵', [X2(' + 3x + 2', 'y = '), X2(' + 3x + 2 = 0'), '(x + 2)(x + 1) = 0', 'x = −2, −1'], ('−2', '−1'), 'down', True, ['−2 ', LE, ' x ', LE, ' −1'], g12s[1])]:
    G(f'③-2 {no} Step❶')
    for e, y in zip(eqs, (309, 335, 361, 387)):
        center(pg, e, [148, y + dy, 326, y + 22 + dy], 11)
    memo(pg, 'y = 0 とする', 296, 307 + dy, 7)
    gx, ay1 = 420, 384.5 + dy
    PAINT(dict(xv=gx, yv=404.5 + dy, q=0.05, top=312 + dy, ay=ay1), None, True, True, labs)
    G(f'③-2 {no} Step❷')
    PAINT(gs, mode, eq)
    G(f'③-2 {no} Step❸')
    center(pg, an, [323.2, 467.2 + dy, 507.3, 498.3 + dy], 13)

# ===== No.13 ③-3 例 ⑴〜⑷ =====
pen.page(12)
EX13 = [
    ([X2(' + 4x + 2 = 0'), ['x = ', F(['−4 ± ', R('16 − 8')], '2')], ['= ', F(['−4 ± 2', R('2')], '2'), ' = −2 ± ', R('2')]],
     ('two', ([M + '2 − ', R('2')], [M + '2 + ', R('2')])), 'up', True, ['x ', LE, ' −2 − ', R('2'), ',  −2 + ', R('2'), ' ', LE, ' x'], 8),
    ([X2(' + 6x + 9 = 0'), [ '(x + 3)', P('2'), ' = 0'], 'x = −3（重解）'], ('touch', ('−3',)), 'down', False, '解なし', None),
    ([X2(' − 2x + 1 = 0'), ['(x − 1)', P('2'), ' = 0'], 'x = 1（重解）'], ('touch', ('1',)), 'up', False, '1以外のすべての実数', None),
    ([X2(' + 2x + 5 = 0'), ['x = ', F(['−2 ± ', R('4 − 20')], '2'), ' = ', F(['−2 ± ', R('−16')], '2')], '√ の中がマイナス → 解なし'], ('none', ()), 'up', False, 'すべての実数', None)]
ax13 = AXES(12)
for k, (eqs, (kind, labs), mode, eq, an, sud) in enumerate(EX13):
    dy = 162 * k
    G(f'③-3 例{"⑴⑵⑶⑷"[k]}')
    lines(pg, eqs, 68, 134 + dy, 10.5, 9)
    if sud:
        sudare(pg, sud, 205, 132 + dy, 6)
    ay = ax13[k]
    if kind == 'two':
        g = dict(xv=300.4, yv=ay + 22, q=22 / 18 ** 2, top=134 + dy, ay=ay)
    elif kind == 'touch':
        g = dict(xv=300.4, yv=ay, q=0.035, top=134 + dy, ay=ay)
    else:
        g = dict(xv=300.4, yv=ay - 16, q=0.03, top=134 + dy, ay=ay)
    PAINT(g, mode, eq, True, labs, 6.5)
    center(pg, an, [359.6, 207 + dy, 527.3, 238.2 + dy], 12)

# ===== No.14・15 プリント問題③-3（白紙に 書く） =====
def FREE(x, y, eqs, kind, labs, mode, eq, ans, sud=None, eqs_s=10.5):
    """白紙の 問題：左に 計算、右に グラフ（x軸から かく）、下に 答え"""
    lines(pg, eqs, x + 6, y + 20, eqs_s, 9)
    if sud:
        sudare(pg, sud, x + 6, y + 112, 6)
    gx, ay = x + 180, y + 120
    AXIS(gx - 52, gx + 52, ay)
    if kind == 'two':
        g = dict(xv=gx, yv=ay + 22, q=22 / 18 ** 2, top=y + 62, ay=ay)
    elif kind == 'touch':
        g = dict(xv=gx, yv=ay, q=0.035, top=y + 62, ay=ay)
    else:
        g = dict(xv=gx, yv=ay - 16, q=0.03, top=y + 62, ay=ay)
    PAINT(g, mode, eq, True, labs, 6.5)
    w, a, d = measure(['答え  '] + (ans if isinstance(ans, list) else [ans]), 12)
    lines(pg, [['答え  '] + (ans if isinstance(ans, list) else [ans])], x + 6, y + 168, 12)

pen.page(13)
L14, R14 = 62.1, 302.9
P14 = [
    (L14, 76.5, '⑴', [X2(' + 5x + 6 = 0'), '(x + 3)(x + 2) = 0', 'x = −3, −2'], 'two', ('−3', '−2'), 'up', True, ['x ', LE, ' −3,  −2 ', LE, ' x'], None),
    (R14, 76.5, '⑵', [X2(' + 3x − 2 = 0', '2'), '(x + 2)(2x − 1) = 0', ['x = −2, ', F('1', '2')]], 'two', ('−2', F('1', '2')), 'down', False, ['−2 < x < ', F('1', '2')], None),
    (L14, 310.5, '⑶', [X2(' + 3x − 5 = 0'), ['x = ', F(['−3 ± ', R('9 + 20')], '2')], ['  = ', F(['−3 ± ', R('29')], '2')]], 'two',
     (F(['−3 − ', R('29')], '2'), F(['−3 + ', R('29')], '2')), 'down', False, [F(['−3 − ', R('29')], '2'), ' < x < ', F(['−3 + ', R('29')], '2')], None),
    (R14, 310.5, '⑷', [X2(' + 2x − 2 = 0'), ['x = ', F(['−2 ± ', R('4 + 8')], '2')], ['  = ', F(['−2 ± 2', R('3')], '2'), ' = −1 ± ', R('3')]], 'two',
     ([M + '1 − ', R('3')], [M + '1 + ', R('3')]), 'up', True, ['x ', LE, ' −1 − ', R('3'), ',  −1 + ', R('3'), ' ', LE, ' x'], 12),
    (L14, 562.5, '⑸', [X2(' + 5x = 0'), 'x(x + 5) = 0', 'x = −5, 0'], 'two', ('−5', '0'), 'down', True, ['−5 ', LE, ' x ', LE, ' 0'], None),
    (R14, 562.5, '⑹', [X2(' − 4 = 0'), '(x + 2)(x − 2) = 0', 'x = −2, 2'], 'two', ('−2', '2'), 'up', False, 'x < −2,  2 < x', None)]
for x, y, no, eqs, kind, labs, mode, eq, an, sud in P14:
    G(f'プリント問題③-3 {no}')
    FREE(x, y, eqs, kind, labs, mode, eq, an, sud)

pen.page(14)
P15 = [
    (L14, 58.5, '⑺', [X2(' + 4x + 4 = 0'), ['(x + 2)', P('2'), ' = 0'], 'x = −2（重解）'], 'touch', ('−2',), 'up', False, '−2以外のすべての実数'),
    (R14, 58.5, '⑻', [X2(' + 4x + 4 = 0'), ['(x + 2)', P('2'), ' = 0'], 'x = −2（重解）'], 'touch', ('−2',), 'up', True, 'すべての実数'),
    (L14, 310.5, '⑼', [X2(' − 6x + 9 = 0'), ['(x − 3)', P('2'), ' = 0'], 'x = 3（重解）'], 'touch', ('3',), 'down', False, '解なし'),
    (R14, 310.5, '⑽', [X2(' − 6x + 9 = 0'), ['(x − 3)', P('2'), ' = 0'], 'x = 3（重解）'], 'touch', ('3',), 'down', True, 'x = 3'),
    (L14, 544.5, '⑾', [X2(' + 4x + 6 = 0'), ['x = ', F(['−4 ± ', R('16 − 24')], '2')], ['  = ', F(['−4 ± ', R('−8')], '2')], '√ の中がマイナス → 解なし'], 'none', (), 'up', False, 'すべての実数'),
    (R14, 544.5, '⑿', [X2(' + 4x + 6 = 0'), ['x = ', F(['−4 ± ', R('16 − 24')], '2')], ['  = ', F(['−4 ± ', R('−8')], '2')], '√ の中がマイナス → 解なし'], 'none', (), 'down', True, '解なし')]
for x, y, no, eqs, kind, labs, mode, eq, an in P15:
    G(f'プリント問題③-3 {no}')
    FREE(x, y, eqs, kind, labs, mode, eq, an)

# ===== No.16 ③-4 x² の 前が マイナス =====
pen.page(15)
G('③-4 解き方')
STRIKE2(88.5, 172.5, 128.4)
center(pg, '−1', [218.2, 131.4, 255.9, 159.7], 13)
center(pg, X2(' + 6x + 7 < 0'), [73.3, 144.6, 183.9, 172.9], 12)
memo(pg, '新しい式を書いたら、元の式は二重線で消す', 300, 178, 7)
G('③-4 例⑴')
center(pg, X2(' + 6x + 7 < 0'), [62.7, 231.5, 199.9, 263.4], 12)
lines(pg, [X2(' + 6x + 7 = 0'), ['x = ', F(['−6 ± ', R('36 − 28')], '2')], ['= ', F(['−6 ± 2', R('2')], '2'), ' = −3 ± ', R('2')]], 68, 272, 10.5, 9)
sudare(pg, 8, 205, 270, 6)
g16 = [g for g in GEO(15) if g['ay'] > 300]
ay16 = g16[0]['ay'] if g16 else 343.6
PAINT(dict(xv=299.6, yv=ay16 + 22, q=22 / 18 ** 2, top=272, ay=ay16), 'down', False, True, ([M + '3 − ', R('2')], [M + '3 + ', R('2')]), 6.5)
center(pg, ['−3 − ', R('2'), ' < x < −3 + ', R('2')], [358.9, 345.3, 526.6, 376.4], 12)

def FREE4(x, y, org, eqs, labs, mode, eq, ans, sud=None):
    """③-4 の 問題：元の 式（二重線）→ 新しい 式 → 計算 → グラフ → 答え"""
    w, a, d = measure(org, 10.5)
    lines(pg, [org], x + 6, y + 20, 10.5)
    STRIKE2(x + 5, x + 7 + w, y + 20 + a - 3.5)
    FREE(x, y + 18, eqs, 'two', labs, mode, eq, ans, sud)

G('プリント問題③-4 ⑴')
FREE4(L14, 439.5, ['−', *X2(' + x + 2 > 0')], [X2(' − x − 2 < 0'), '(x + 1)(x − 2) = 0', 'x = −1, 2'], ('−1', '2'), 'down', False, '−1 < x < 2')
G('プリント問題③-4 ⑵')
FREE4(R14, 439.5, ['−', *X2(' + 2x + 2 ', )] + [LE, ' 0'], [[*X2(' − 2x − 2 '), GE, ' 0'], ['x = ', F(['2 ± ', R('4 + 8')], '2')], ['= ', F(['2 ± 2', R('3')], '2'), ' = 1 ± ', R('3')]],
      (['1 − ', R('3')], ['1 + ', R('3')]), 'up', True, ['x ', LE, ' 1 − ', R('3'), ',  1 + ', R('3'), ' ', LE, ' x'], 12)
