import sys, os
import pymupdf as fz

# 使い方: python kaitou.py <1-6 または 7-9> <プリントの pdf（非公開リポジトリの 数学Ⅰ/）> ../期末考査/kaitou ページの名前 バージョン [解答pdfの 保存先（非公開リポジトリ）]
# 答えは プリントの まとまりごとに kaitou_no1-6.py・kaitou_no7-9.py に 書く（まとまりを 足すときは kaitou_no◯-◯.py を 足す）
PART = sys.argv.pop(1)
SRC, OUT = sys.argv[1], sys.argv[2]   # プリントの pdf、出力の フォルダ
RED = (0.63, 0.11, 0.11)
PALE = (0.80, 0.52, 0.52)   # 小さな メモ（b² の 値 など）は 薄い 赤
COL = [RED]
FONTS = {
    'R': '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',
    'I': '/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf',
    'G': '/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf',
}
FO = {k: fz.Font(fontfile=v) for k, v in FONTS.items()}


# ---------- mini math layout ----------
class Frac:
    def __init__(s, n, d): s.n, s.d = n, d
class Sqrt:
    def __init__(s, a): s.a = a
class Sup:
    def __init__(s, a): s.a = a
class Strike:
    """斜線で 消す（ルートの中が 0 の とき の「± 0」。板書と 同じ、2026-10-30）"""
    def __init__(s, a): s.a = a
ORANGE = (0.94, 0.48, 0.07)

def runs(text):
    out = []
    for c in text:
        if c.isascii() and c.isalpha():
            k = 'I'
        elif FO['R'].has_glyph(ord(c)) and not ('　' <= c):
            k = 'R'
        else:
            k = 'G'
        if out and out[-1][0] == k:
            out[-1][1] += c
        else:
            out.append([k, c])
    return out

def items(e):
    return e if isinstance(e, list) else [e]

def measure(e, s):
    """returns (width, ascent, descent) ascent/descent positive."""
    w, a, d = 0, 0, 0
    for it in items(e):
        if isinstance(it, str):
            for k, t in runs(it):
                w += FO[k].text_length(t, s) + (0.08 * s if k == 'I' else 0)
            a, d = max(a, 0.72 * s), max(d, 0.22 * s)
        elif isinstance(it, Frac):
            fs = s * 0.9
            nw, na, nd = measure(it.n, fs)
            dw, da, dd = measure(it.d, fs)
            w += max(nw, dw) + 0.4 * s
            ax = 0.3 * s
            a = max(a, ax + 0.12 * s + nd + na)
            d = max(d, -ax + 0.12 * s + da + dd)
        elif isinstance(it, Sqrt):
            iw, ia, idd = measure(it.a, s)
            w += iw + 0.62 * s
            a, d = max(a, ia + 0.14 * s), max(d, idd + 0.04 * s)
        elif isinstance(it, Strike):
            sw, sa, sd = measure(it.a, s)
            w += sw; a, d = max(a, sa), max(d, sd)
        elif isinstance(it, Sup):
            sw, sa, sd = measure(it.a, s * 0.62)
            w += sw + 0.05 * s
            a = max(a, 0.42 * s + sa)
    return w, a, d

def draw(pg, e, x, y, s):
    """draw expression with baseline y starting at x; returns end x."""
    for it in items(e):
        if isinstance(it, str):
            for k, t in runs(it):
                pg.insert_text((x, y), t, fontsize=s, fontname='F' + k, color=COL[0])
                x += FO[k].text_length(t, s) + (0.08 * s if k == 'I' else 0)
        elif isinstance(it, Frac):
            fs = s * 0.9
            nw, na, nd = measure(it.n, fs)
            dw, da, dd = measure(it.d, fs)
            W = max(nw, dw) + 0.4 * s
            ax = y - 0.3 * s
            pg.draw_line((x + 0.05 * s, ax), (x + W - 0.05 * s, ax), color=COL[0], width=0.06 * s)
            draw(pg, it.n, x + (W - nw) / 2, ax - 0.12 * s - nd, fs)
            draw(pg, it.d, x + (W - dw) / 2, ax + 0.12 * s + da, fs)
            x += W
        elif isinstance(it, Sqrt):
            iw, ia, idd = measure(it.a, s)
            top = y - ia - 0.08 * s
            bot = y + idd * 0.6
            lw = 0.055 * s
            p = [(x + 0.04 * s, y - 0.3 * s), (x + 0.16 * s, y - 0.36 * s),
                 (x + 0.3 * s, bot), (x + 0.5 * s, top), (x + 0.62 * s + iw, top)]
            for a_, b_ in zip(p, p[1:]):
                pg.draw_line(a_, b_, color=COL[0], width=lw)
            draw(pg, it.a, x + 0.58 * s, y, s)
            x += iw + 0.62 * s
        elif isinstance(it, Strike):
            x1 = draw(pg, it.a, x, y, s)
            pg.draw_line((x - 0.1 * s, y + 0.12 * s), (x1 + 0.1 * s, y - 0.62 * s), color=ORANGE, width=0.09 * s)
            x = x1
        elif isinstance(it, Sup):
            x = draw(pg, it.a, x + 0.03 * s, y - 0.42 * s, s * 0.62) + 0.02 * s
    return x

def piece(r):
    """答えを かくす ときの 枠（1つずつ タップで 見せる）"""
    pen.pieces.append([round(v, 1) for v in r])


def put(pg, e, x, y, s=13):
    w, a, d = measure(e, s)
    piece([x, y - a, x + w, y + d])
    return draw(pg, e, x, y, s)

def center(pg, e, r, s=13, rec=True):
    """center e in rect r=[x0,y0,x1,y1]; shrink if needed."""
    if rec:
        piece(r)
    x0, y0, x1, y1 = r
    while True:
        w, a, d = measure(e, s)
        if (w <= x1 - x0 - 4 and a + d <= y1 - y0 - 2) or s < 7:
            break
        s -= 0.5
    draw(pg, e, (x0 + x1 - w) / 2, (y0 + y1) / 2 + (a - d) / 2, s)

def stack(pg, es, r, s=12):
    """several lines centered in rect r."""
    piece(r)
    x0, y0, x1, y1 = r
    while True:
        ms = [measure(e, s) for e in es]
        H = sum(a + d for _, a, d in ms) + 2 * (len(es) - 1)
        if (H <= y1 - y0 - 2 and max(w for w, _, _ in ms) <= x1 - x0 - 4) or s < 7:
            break
        s -= 0.5
    y = (y0 + y1) / 2 - H / 2
    for e, (w, a, d) in zip(es, ms):
        draw(pg, e, (x0 + x1 - w) / 2, y + a, s)
        y += a + d + 2

def memo(pg, e, cx, y, s=7.5):
    """枠の 近くに 小さく 薄い 字で 書く メモ（cx を 中心、y が 下の 端）"""
    w, a, d = measure(e, s)
    piece([cx - w / 2, y - a - d, cx + w / 2, y])
    COL[0] = PALE
    draw(pg, e, cx - w / 2, y - d, s)
    COL[0] = RED


def sudare(pg, n, x, y, s=7.5):
    """すだれ算（素因数分解）を 薄い 字で：2 ) 44 → 2 ) 22 → 11、その 下に √44 ＝ 2√11（板書、2026-10-30）。
    x, y：左上。2つ そろった 数は 赤い 丸、のこりは オレンジの 四角"""
    m, rows = n, []
    p = 2
    while p * p <= m:
        if m % p == 0:
            rows.append((p, m)); m //= p
        else:
            p += 1
    ps = [r[0] for r in rows] + ([m] if m > 1 else [])
    cnt = {}
    for q in ps:
        cnt[q] = cnt.get(q, 0) + 1
    out = inn = 1
    for q, c in cnt.items():
        out *= q ** (c // 2)
        inn *= q ** (c % 2)
    used = {}
    def mark(q, cx, cy):
        used[q] = used.get(q, 0) + 1
        if used[q] <= 2 * (cnt[q] // 2):
            pg.draw_circle((cx, cy), s * 0.62, color=(0.88, 0.45, 0.5), width=0.5)
        else:
            pg.draw_rect(fz.Rect(cx - s * 0.6, cy - s * 0.62, cx + s * 0.6, cy + s * 0.62), color=(0.94, 0.6, 0.3), width=0.5)
    h = s * 1.35
    COL[0] = PALE
    for i, (q, v) in enumerate(rows):
        yb = y + (i + 1) * h
        draw(pg, str(q), x, yb - s * 0.25, s)
        mark(q, x + s * 0.25, yb - s * 0.55)
        draw(pg, str(v), x + s * 1.5, yb - s * 0.25, s)
        bx, top = x + s * 0.98, yb - h + s * 0.1      # 割り算の「)」：丸く 曲げて、下の 横線に つなぐ
        pg.draw_bezier((bx, top), (bx + s * 0.38, top + h * 0.25), (bx + s * 0.38, yb - h * 0.25), (bx + s * 0.08, yb), color=PALE, width=0.45)
        pg.draw_line((bx + s * 0.08, yb), (x + s * 3.5, yb), color=PALE, width=0.4)
    yb = y + (len(rows) + 1) * h
    if m > 1:
        draw(pg, str(m), x + s * 1.5, yb - s * 0.25, s)
        mark(m, x + s * 1.5 + measure(str(m), s)[0] / 2, yb - s * 0.55)
    res = [R(str(n)), ' = ' + (str(out) if out > 1 else '')] + ([R(str(inn))] if inn > 1 else [])
    draw(pg, res, x - s * 0.2, yb + s * 1.3, s)
    COL[0] = RED
    w = max(s * 3.4, measure(res, s)[0])
    piece([x - s * 0.4, y, x + w, yb + s * 1.6])


def parab(pg, xv, yv, q, ay, top, roots=(), labs=(), s=7, box=None, mid=False):
    """グラフの 概形：下に凸の 放物線 y ＝ yv − q (x − xv)²（pt）。roots の x に 点、その 下に labs（放物線の 外がわ。mid＝True で 点の 真下）"""
    hw = ((yv - top) / q) ** 0.5
    pts = [(xv - hw + 2 * hw * i / 60, yv - q * (2 * hw * i / 60 - hw) ** 2) for i in range(61)]
    pg.draw_polyline(pts, color=RED, width=1.2)
    for x in roots:
        pg.draw_circle((x, ay), 1.9, color=RED, fill=RED)
    for x, e in zip(roots, labs):
        w, a, d = measure(e, s)
        lx = x - w / 2 if len(roots) == 1 or mid else (x - w - 1 if x < xv else x + 1)
        draw(pg, e, lx, ay + 3 + a, s)
    piece(box or [xv - hw - 2, top - 2, xv + hw + 2, ay + 16])


def fracbox(pg, n, d, r, s=13):
    """box with a printed fraction bar in the middle."""
    x0, y0, x1, y1 = r
    m = (y0 + y1) / 2
    piece(r)
    center(pg, n, [x0, y0 + 1, x1, m - 1], s, False)
    center(pg, d, [x0, m + 1, x1, y1 - 1], s, False)

def lines(pg, ls, x, y, s=12, gap=6):
    """free writing: list of lines from top y."""
    for e in ls:
        w, a, d = measure(e, s)
        piece([x, y, x + w, y + a + d])
        draw(pg, e, x, y + a, s)
        y += a + d + gap
    return y

F, R, P = Frac, Sqrt, Sup
M = '−'

# 答えは 問題ごとに 白紙の ページへ 書く（あとで 1問ずつ SVG に する）
src = fz.open(SRC)
ans = fz.open()
GROUPS = []          # [ページ番号, 見出し, 白紙ページの 番号]


class Pen:
    """今の 問題の 白紙ページへ 書く（draw の pg として 渡す）"""
    def page(self, i):
        self.no = i

    def insert_text(self, *a, **k):
        self.cur.insert_text(*a, **k)

    def draw_line(self, *a, **k):
        self.cur.draw_line(*a, **k)

    def draw_circle(self, *a, **k):
        self.cur.draw_circle(*a, **k)

    def draw_rect(self, *a, **k):
        self.cur.draw_rect(*a, **k)

    def draw_bezier(self, *a, **k):
        self.cur.draw_bezier(*a, **k)

    def draw_polyline(self, *a, **k):
        self.cur.draw_polyline(*a, **k)


pen = Pen()
pg = pen


def G(label):
    r = src[pen.no].rect
    pen.cur = ans.new_page(width=r.width, height=r.height)
    for k, v in FONTS.items():
        pen.cur.insert_font(fontname='F' + k, fontfile=v)
    pen.pieces = []
    GROUPS.append([pen.no, label, pen.cur.number, pen.pieces])

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'kaitou_no{PART}.py'), encoding='utf-8').read())


# ---------- 書き出し ----------
# 背景＝プリントの ページ（そのまま）、その上に 問題ごとの 答えの SVG を 同じ 位置で 重ねる
import os, json
os.makedirs(os.path.join(OUT, 'svg'), exist_ok=True)
# 答えの ある ページだけ 出す（No.7〜 の 解答を 足しても、ページ番号＝プリントの No. の まま）
USED = sorted({g[0] for g in GROUPS})
pages = {}
for i in USED:
    p = src[i]
    open(os.path.join(OUT, 'svg', f'p{i + 1}.svg'), 'w', encoding='utf-8').write(p.get_svg_image())
    pages[i] = {'no': i + 1, 'w': p.rect.width, 'h': p.rect.height, 'g': []}
for n, (i, label, k, pcs) in enumerate(GROUPS):
    a = ans[k]
    name = f'p{i + 1}_{n + 1:02d}.svg'
    open(os.path.join(OUT, 'svg', name), 'w', encoding='utf-8').write(a.get_svg_image())
    pages[i]['g'].append({'f': name, 'label': label, 'p': pcs})
    src[i].show_pdf_page(src[i].rect, ans, k)        # 答えを 書きこんだ pdf も 作る
pages = [pages[i] for i in USED]
src.select(USED)
src.subset_fonts()
if len(sys.argv) > 5:      # 答えを 書きこんだ pdf は 非公開リポジトリへ（公開リポジトリに プリントの pdf は 置かない）
    src.save(sys.argv[5], garbage=3, deflate=True)

B = os.path.dirname(os.path.abspath(__file__))
TITLE = sys.argv[3] if len(sys.argv) > 3 else '解答'
VER = sys.argv[4] if len(sys.argv) > 4 else ''
h = open(os.path.join(B, 'kaitou.html'), encoding='utf-8').read()
h = h.replace('{{TITLE}}', TITLE).replace('{{VER}}', VER)
h = h.replace('{{PAGES}}', json.dumps(pages, ensure_ascii=False))
h = h.replace('<!--THEME-->', open(os.path.join(B, 'theme.html'), encoding='utf-8').read())
open(os.path.join(OUT, TITLE + '.html'), 'w', encoding='utf-8').write(h)
print('ok', len(GROUPS), 'groups')
