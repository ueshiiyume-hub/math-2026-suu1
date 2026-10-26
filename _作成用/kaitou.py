import sys
import pymupdf as fz

# 使い方: python kaitou.py <プリントの pdf（非公開リポジトリの 数学Ⅰ/）> ../期末考査/kaitou ページの名前 バージョン [解答pdfの 保存先（非公開リポジトリ）]
SRC, OUT = sys.argv[1], sys.argv[2]   # プリントの pdf、出力の フォルダ
RED = (0.63, 0.11, 0.11)
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
                pg.insert_text((x, y), t, fontsize=s, fontname='F' + k, color=RED)
                x += FO[k].text_length(t, s) + (0.08 * s if k == 'I' else 0)
        elif isinstance(it, Frac):
            fs = s * 0.9
            nw, na, nd = measure(it.n, fs)
            dw, da, dd = measure(it.d, fs)
            W = max(nw, dw) + 0.4 * s
            ax = y - 0.3 * s
            pg.draw_line((x + 0.05 * s, ax), (x + W - 0.05 * s, ax), color=RED, width=0.06 * s)
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
                pg.draw_line(a_, b_, color=RED, width=lw)
            draw(pg, it.a, x + 0.58 * s, y, s)
            x += iw + 0.62 * s
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


pen = Pen()
pg = pen


def G(label):
    r = src[pen.no].rect
    pen.cur = ans.new_page(width=r.width, height=r.height)
    for k, v in FONTS.items():
        pen.cur.insert_font(fontname='F' + k, fontfile=v)
    pen.pieces = []
    GROUPS.append([pen.no, label, pen.cur.number, pen.pieces])

# ===== page 1 =====
pen.page(0)
G('①-1 ⑴')
put(pg, '= (x+5)(x−3)'.replace('+', ' + ').replace('−', ' − '), 80, 172)
G('①-1 ⑵')
put(pg, '= (x + 3)(x − 3)', 322, 172)
G('①-1 ⑶')
put(pg, ['= (x + 3)', P('2')], 80, 244)
G('①-1 ⑷')
put(pg, '= x(x + 6)', 322, 244)

def q12(dx, dy, a, b, la, lb, ans, s=13):
    center(pg, a, [63.6 + dx, 357.2 + dy, 117.7 + dx, 382.7 + dy] if dx == 0 or a != 'x' else [304.9, 501.2, 331.6, 526.7], s)
    center(pg, b, [117.7 + dx, 357.2 + dy, 171.8 + dx, 382.7 + dy], s)
    stack(pg, la, [63.6 + dx, 393.2 + dy, 136.6 + dx, 442.3 + dy])
    stack(pg, lb, [141.8 + dx, 393.2 + dy, 214.8 + dx, 442.3 + dy])
    center(pg, ans, [116.9 + dx, 445.4 + dy, 189.4 + dx, 473.8 + dy], s)

G('①-2 ⑴')
q12(0, 0, '(x + 5)', '(x − 3)', ['x + 5 = 0', 'x = −5'], ['x − 3 = 0', 'x = 3'], '−5, 3')
G('①-2 ⑵')
q12(241.3, 0, '(x + 3)', '(x − 3)', ['x + 3 = 0', 'x = −3'], ['x − 3 = 0', 'x = 3'], '−3, 3')
G('①-2 ⑶')
q12(0, 144, '(x + 3)', '(x + 3)', ['x + 3 = 0', 'x = −3'], ['x + 3 = 0', 'x = −3'], '−3')
center(pg, '（重解）', [219.2, 579.6, 286.2, 617.7], 12)
# (4): the first box is narrow
G('①-2 ⑷')
center(pg, 'x', [304.9, 501.2, 331.6, 526.7])
center(pg, '(x + 6)', [331.6, 501.2, 385.7, 526.7])
stack(pg, ['x = 0'], [304.9, 537.2, 377.9, 586.3])
stack(pg, ['x + 6 = 0', 'x = −6'], [383.1, 537.2, 456.1, 586.3])
center(pg, '0, −6', [358.2, 589.4, 430.7, 617.8])

# ===== page 2 =====
pen.page(1)
L, Rx = 76, 317
G('追加問題①-2 ⑴')
lines(pg, ['(x + 1)(x + 2) = 0', 'x = −1, −2'], L, 100)
G('追加問題①-2 ⑵')
lines(pg, ['(x − 7)(x + 2) = 0', 'x = 7, −2'], Rx, 100)
G('追加問題①-2 ⑶')
lines(pg, ['(x + 4)(x − 4) = 0', 'x = −4, 4'], L, 208)
G('追加問題①-2 ⑷')
lines(pg, ['x(x + 8) = 0', 'x = 0, −8'], Rx, 208)
G('追加問題①-2 ⑸')
lines(pg, [['(x − 1)', P('2'), ' = 0'], 'x = 1（重解）'], L, 316)
G('追加問題①-2 ⑹')
lines(pg, [['(x + 4)', P('2'), ' = 0'], 'x = −4（重解）'], Rx, 316)
# 1-3 example
G('①-3 ⑴')
center(pg, '(2x + 3)', [63.6, 466.7, 117.7, 492.2])
center(pg, '(2x − 3)', [117.7, 466.7, 171.8, 492.2])
stack(pg, ['2x + 3 = 0', ['x = −', F('3', '2')]], [63.6, 502.7, 136.6, 562.2])
stack(pg, ['2x − 3 = 0', ['x = ', F('3', '2')]], [141.8, 502.7, 214.8, 562.2])
center(pg, ['−', F('3', '2'), ',  ', F('3', '2')], [116.9, 563.8, 189.4, 592.1])
G('①-3 ⑵')
center(pg, 'x', [304.9, 466.7, 331.6, 492.2])
center(pg, '(2x + 1)', [331.6, 466.7, 385.7, 492.2])
stack(pg, ['x = 0'], [304.9, 502.7, 377.9, 562.2])
stack(pg, ['2x + 1 = 0', ['x = −', F('1', '2')]], [383.1, 502.7, 456.1, 562.2])
center(pg, ['0,  −', F('1', '2')], [358.2, 563.8, 430.7, 592.1])
# extra 1-3
G('追加問題①-3 ⑴')
lines(pg, ['(3x + 2)(3x − 2) = 0', ['x = −', F('2', '3'), ',  ', F('2', '3')]], L, 643)
G('追加問題①-3 ⑵')
lines(pg, ['x(3x − 5) = 0', ['x = 0,  ', F('5', '3')]], Rx, 643)

# ===== page 3 =====
pen.page(2)
def formula(dy, mb, b2, ac, a2, calc, s=13):
    center(pg, mb, [113.7, 241.7 + dy, 157.2, 268.7 + dy], s)
    center(pg, b2, [186.5, 241.7 + dy, 229.9, 268.7 + dy], s)
    center(pg, ac, [229.2, 241.7 + dy, 285.4, 268.7 + dy], s)
    center(pg, a2, [179.9, 273.7 + dy, 239.2, 300.6 + dy], s)
    center(pg, calc, [350.5, 240.6 + dy, 465.2, 267.5 + dy], 12)

G('①-4 ⑴')
formula(0, '5', ['(−5)', P('2')], '−12', '6', '−4×3×1 = −12')
center(pg, F(['5 ± ', R('13')], '6'), [113.7, 304.9, 229.9, 359.9], 15)
G('①-4 ⑵')
formula(180, '−4', ['4', P('2')], '+12', '2', '−4×1×(−3) = 12')
fracbox(pg, ['−4 ± ', R('28')], '2', [113.7, 484.8, 206.9, 539.9])
fracbox(pg, ['−4 ± 2', R('7')], '2', [230.7, 484.8, 323.9, 539.9])
center(pg, ['−2 ± ', R('7')], [348.2, 484.8, 441.3, 539.9], 15)
G('①-4 ⑶')
formula(358.6, '−3', ['3', P('2')], '−8', '4', '−4×2×1 = −8')
fracbox(pg, ['−3 ± ', R('1')], '4', [113.7, 663.4, 206.9, 718.4])
fracbox(pg, '−3 ± 1', '4', [230.7, 663.4, 323.9, 718.4])
center(pg, [F('−3 + 1', '4'), ' = ', F('−2', '4'), ' = −', F('1', '2')], [350.5, 640.5, 500.6, 688.0], 14)
center(pg, [F('−3 − 1', '4'), ' = ', F('−4', '4'), ' = −1'], [350.5, 690.2, 500.6, 737.8], 14)
center(pg, ['−', F('1', '2'), ',  −1'], [230.7, 720.3, 323.9, 775.4], 15)

# ===== page 4 =====
pen.page(3)
def sol(x, y, a, b, c, steps):
    """x = (-b ± √(b²-4ac)) / 2a  then further steps."""
    mb = str(-b).replace('-', M)
    inner = f"{b * b} {'−' if 4 * a * c > 0 else '+'} {abs(4 * a * c)}"
    first = ['x = ', F(mb + ' ± ', R(inner)), F([mb + ' ± ', R(inner)], str(2 * a))]
    first = ['x = ', F([mb + ' ± ', R(inner)], str(2 * a))]
    return lines(pg, [first] + steps, x, y, 12, gap=8)

L, Rx = 76, 317
G('プリント問題①-4 ⑴')
sol(L, 98, 2, -7, 1, [['   = ', F(['7 ± ', R('41')], '4')]])
G('プリント問題①-4 ⑵')
sol(Rx, 98, 3, -5, -1, [['   = ', F(['5 ± ', R('37')], '6')]])
G('プリント問題①-4 ⑶')
sol(L, 260, 1, 6, -2, [['   = ', F(['−6 ± ', R('44')], '2'), ' = ', F(['−6 ± 2', R('11')], '2')],
                       ['   = −3 ± ', R('11')]])
G('プリント問題①-4 ⑷')
sol(Rx, 260, 1, -2, -5, [['   = ', F(['2 ± ', R('24')], '2'), ' = ', F(['2 ± 2', R('6')], '2')],
                        ['   = 1 ± ', R('6')]])
G('プリント問題①-4 ⑸')
sol(L, 440, 2, 5, 2, [['   = ', F(['−5 ± ', R('9')], '4'), ' = ', F('−5 ± 3', '4')],
                      ['x = ', F('−5 + 3', '4'), ',  ', F('−5 − 3', '4')],
                      ['x = −', F('1', '2'), ',  −2']])
G('プリント問題①-4 ⑹')
sol(Rx, 440, 3, 7, 2, [['   = ', F(['−7 ± ', R('25')], '6'), ' = ', F('−7 ± 5', '6')],
                       ['x = ', F('−7 + 5', '6'), ',  ', F('−7 − 5', '6')],
                       ['x = −', F('1', '3'), ',  −2']])

# ===== page 5 =====
pen.page(4)
def formula5(dy, mb, b2, ac, a2, calc, s=13):
    center(pg, mb, [112.9, 133.7 + dy, 156.4, 160.7 + dy], s)
    center(pg, b2, [185.7, 133.7 + dy, 229.2, 160.7 + dy], s)
    center(pg, ac, [228.4, 133.7 + dy, 284.6, 160.7 + dy], s)
    center(pg, a2, [179.2, 165.7 + dy, 238.5, 192.6 + dy], s)
    center(pg, calc, [349.7, 132.6 + dy, 464.5, 159.5 + dy], 12)

G('①-5 ⑴')
formula5(0, '−2', ['2', P('2')], '−4', '2', '−4×1×1 = −4')
fracbox(pg, ['−2 ± ', R('0')], '2', [112.9, 196.8, 206.1, 251.9])
fracbox(pg, '−2 ± 0', '2', [230.0, 196.8, 323.2, 251.9])
fracbox(pg, '−2', '2', [348.5, 196.8, 441.7, 251.9])
center(pg, '−1', [472.0, 196.8, 531.5, 251.9], 16)
center(pg, '重解', [470.0, 163.0, 531.8, 193.7], 13)
G('①-5 ⑵')
formula5(180, '−3', ['3', P('2')], '−20', '2', '−4×1×5 = −20')
fracbox(pg, ['−3 ± ', R('−11')], '2', [112.9, 376.8, 206.1, 431.9])
center(pg, '解なし', [234.1, 385.9, 370.6, 422.8], 15)
G('①-5 まとめ')
center(pg, '解が 2つ', [121, 467, 208, 492], 12)
center(pg, '重解', [281, 467, 368, 492], 12)
center(pg, '解なし', [440, 467, 527, 492], 12)

def sol5(x, y, a, b, c, mid, last):
    mb = str(-b).replace('-', M)
    d4 = 4 * a * c
    inner = f"{b * b} − {d4}" if d4 >= 0 else f"{b * b} + {-d4}"
    first = ['x = ', F([mb + ' ± ', R(inner)], str(2 * a)), '   = ', mid]
    return lines(pg, [first] + last, x, y, 12, gap=8)

G('プリント問題①-5 ⑴')
sol5(L, 552, 1, 4, 4, F(['−4 ± ', R('0')], '2'), ['   = −2', 'x = −2（重解）'])
G('プリント問題①-5 ⑵')
sol5(Rx, 552, 9, -6, 1, F(['6 ± ', R('0')], '18'), [['   = ', F('6', '18'), ' = ', F('1', '3')],
                                                      ['x = ', F('1', '3'), '（重解）']])
G('プリント問題①-5 ⑶')
sol5(L, 678, 1, -1, 3, F(['1 ± ', R('−11')], '2'), ['√ の中がマイナスなので', '解なし'])
G('プリント問題①-5 ⑷')
sol5(Rx, 678, 3, 2, 4, F(['−2 ± ', R('−44')], '6'), ['√ の中がマイナスなので', '解なし'])

# ===== page 6 =====
pen.page(5)
G('①-6 ⑴')
center(pg, '2', [147, 471, 171, 497], 17)
G('①-6 ⑶')
center(pg, '0', [467, 471, 492, 497], 17)
G('①-6 ⑵')
put(pg, '実数解の個数は 1 個（重解）', 230, 492, 11)

def d6(x, y, ex, val, ans):
    lines(pg, [['D = '] + ex, ['   = ' + val], ans], x, y, 12, gap=8)

G('プリント問題①-6 ⑴')
d6(L, 570, [P('') if False else '4', P('2'), ' − 4×1×(−2)'], '16 + 8 = 24 > 0', '実数解の個数は 2 個')
G('プリント問題①-6 ⑵')
d6(Rx, 570, ['(−2)', P('2'), ' − 4×1×4'], '4 − 16 = −12 < 0', '実数解の個数は 0 個')
G('プリント問題①-6 ⑶')
d6(L, 678, ['(−7)', P('2'), ' − 4×2×6'], '49 − 48 = 1 > 0', '実数解の個数は 2 個')
G('プリント問題①-6 ⑷')
d6(Rx, 678, ['12', P('2'), ' − 4×4×9'], '144 − 144 = 0', '実数解の個数は 1 個（重解）')


# ---------- 書き出し ----------
# 背景＝プリントの ページ（そのまま）、その上に 問題ごとの 答えの SVG を 同じ 位置で 重ねる
import os, json
os.makedirs(os.path.join(OUT, 'svg'), exist_ok=True)
NP = max(g[0] for g in GROUPS) + 1
pages = []
for i in range(NP):
    p = src[i]
    open(os.path.join(OUT, 'svg', f'p{i + 1}.svg'), 'w', encoding='utf-8').write(p.get_svg_image())
    pages.append({'w': p.rect.width, 'h': p.rect.height, 'g': []})
for n, (i, label, k, pcs) in enumerate(GROUPS):
    a = ans[k]
    name = f'p{i + 1}_{n + 1:02d}.svg'
    open(os.path.join(OUT, 'svg', name), 'w', encoding='utf-8').write(a.get_svg_image())
    pages[i]['g'].append({'f': name, 'label': label, 'p': pcs})
    src[i].show_pdf_page(src[i].rect, ans, k)        # 答えを 書きこんだ pdf も 作る
src.select(range(NP))
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
