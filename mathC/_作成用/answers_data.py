r"""プリント（複素数平面）の 解答の データ。answers.py が これを 読んで complex/解答.html を 作る
元：非公開リポジトリ 2026_mathC_private の 数学C_複素数平面_解答.docx（2026-10-23 版）を 書き写した もの
SHEETS の 1つ ＝ プリントの 1節：dict(no, title, blocks=[…])
ブロック：('box', 名前, [行])・('text', 見出し or None, [行])・('tbl', 見出し or None, [見出し], [[マス…]…])・('group', 見出し, 小さい 文, [問])・('note', 題, [行], 追加の日)
問：it(番号, 問の 文, [答えの 行], 図…, notes=[N(…)])
行：$ か [[ が あれば 文字と $TeX$ の まぜ書き、なければ TeX だけ（別行立ての 式）。[[…]] は プリントの 空らんの 答え
板書から 足す ときは N(題, [行], '10/27') を notes に（オレンジの 枠に なる）
"""
import math
N = lambda title, lines, add=None: (title, lines, add)

def it(t, q, a, *figs, notes=()):
    return dict(t=t, q=q, a=a, figs=list(figs), notes=list(notes))

# ---- 図（SVG）：P(範囲, pts=[(a, b, 名前, 答え?, 位置)], vec=[(x0, y0, x1, y1, 'a'|'d'|'')], poly=[[(a, b)…]], circle=単位円) ----
def P(x0, x1, y0, y1, pts=(), vec=(), poly=(), circle=False, grid=True, u=26):
    pad = 22   # u：1目盛りの 大きさ（どの 図も 同じ 大きさで かく。拡大しない）
    W, H = (x1 - x0) * u + 2 * pad, (y1 - y0) * u + 2 * pad
    X = lambda x: round(pad + (x - x0) * u, 1); Y = lambda y: round(pad + (y1 - y) * u, 1)
    s = []
    if grid:
        s += [f'<line class="gd" x1="{X(x)}" y1="{Y(y0)}" x2="{X(x)}" y2="{Y(y1)}"/>' for x in range(math.ceil(x0), math.floor(x1) + 1)]
        s += [f'<line class="gd" x1="{X(x0)}" y1="{Y(y)}" x2="{X(x1)}" y2="{Y(y)}"/>' for y in range(math.ceil(y0), math.floor(y1) + 1)]
    s.append(f'<line class="ax" x1="{X(x0)-6}" y1="{Y(0)}" x2="{X(x1)+6}" y2="{Y(0)}"/><polygon class="axh" points="{X(x1)+14},{Y(0)} {X(x1)+5},{Y(0)-4} {X(x1)+5},{Y(0)+4}"/>')
    s.append(f'<line class="ax" x1="{X(0)}" y1="{Y(y0)+6}" x2="{X(0)}" y2="{Y(y1)-6}"/><polygon class="axh" points="{X(0)},{Y(y1)-14} {X(0)-4},{Y(y1)-5} {X(0)+4},{Y(y1)-5}"/>')
    s.append(f'<text x="{X(0)-15}" y="{Y(0)+16}">O</text>')
    if grid: s.append(f'<text x="{X(1)-4}" y="{Y(0)+16}">1</text><text x="{X(0)-13}" y="{Y(1)+5}">1</text>')
    if circle: s.append(f'<circle class="uc" cx="{X(0)}" cy="{Y(0)}" r="{u}"/>')
    for pg in poly: s.append('<polygon class="pg" points="' + ' '.join(f'{X(a)},{Y(b)}' for a, b in pg) + '"/>')
    for x_0, y_0, x_1, y_1, c in vec:
        ax, ay, bx, by = X(x_0), Y(y_0), X(x_1), Y(y_1); L = math.hypot(bx - ax, by - ay) or 1; ux, uy = (bx - ax) / L, (by - ay) / L
        s.append(f'<line class="vc {c}" x1="{ax}" y1="{ay}" x2="{round(bx-ux*6,1)}" y2="{round(by-uy*6,1)}"/>'
                 f'<polygon class="pt {"a" if c=="a" else ""}" points="{bx},{by} {round(bx-ux*9-uy*4,1)},{round(by-uy*9+ux*4,1)} {round(bx-ux*9+uy*4,1)},{round(by-uy*9-ux*4,1)}"/>')
    for a, b, name, ans, pos in pts:
        dx = -6 if 'w' in pos else 6; dy = 15 if 's' in pos else -6
        s.append(f'<circle class="pt {"a" if ans else ""}" cx="{X(a)}" cy="{Y(b)}" r="3.5"/>'
                 f'<text class="{"a" if ans else ""}" x="{X(a)+dx}" y="{Y(b)+dy}" text-anchor="{"end" if "w" in pos else "start"}">{name}</text>')
    return f'<svg class="pl" viewBox="0 0 {round(W)} {round(H)}" width="{round(W)}" height="{round(H)}">' + ''.join(s) + '</svg>'

S3, S2 = math.sqrt(3), math.sqrt(2)
SHEETS = []

# ---------------------------------------------------------------- ①-1
SHEETS.append(dict(no='①-1', title='複素数平面', blocks=[
  ('box', '複素数平面', [
    '複素数 $a+bi$ は、実部 $a$ と虚部 $b$ の組で定まるから、座標平面上の点 $\\mathrm{P}(a,\\ b)$ を対応させることができる。',
    'このように、各点が複素数を表すと定められた座標平面を [[複素数平面]] という。',
    'また、$x$ 軸を [[実軸]]、$y$ 軸を [[虚軸]] という。',
    'とくに、原点 O は実数 $0$ を表す。',
    '複素数 $z=a+bi$ を表す点 P を、$\\mathrm{P}(z)$ または $\\mathrm{P}(a+bi)$ と書き、単に点 $z$ ということもある。']),
  ('group', '例', '複素数平面上に、次の 4 点を図示せよ。', [
    it('', '$\\mathrm{P}(2+2i)$，$\\mathrm{Q}(-2+3i)$，$\\mathrm{R}(-2i)$，$\\mathrm{S}(3)$', [],
       P(-3, 4, -3, 4, pts=[(2,2,'P',1,'ne'),(-2,3,'Q',1,'ne'),(0,-2,'R',1,'se'),(3,0,'S',1,'ne')]))]),
  ('group', '問4', '次の複素数を表す点を、複素数平面にかき入れよ。', [
    it('', '$\\mathrm{A}(1+2i)$　$\\mathrm{B}(-2-3i)$　$\\mathrm{C}(3i)$　$\\mathrm{D}(-3)$', [],
       P(-4, 3, -4, 4, pts=[(1,2,'A',1,'ne'),(-2,-3,'B',1,'sw'),(0,3,'C',1,'ne'),(-3,0,'D',1,'nw')]))]),
  ('group', '問5', '右の複素数平面上の点 A，B，C，D，E，F は、それぞれどのような複素数を表しているか。', [
    it('', '点 A〜F', ['A $3+3i$，B $-2+i$，C $-3-3i$', 'D $1-2i$，E $2$，F $2i$'],
       P(-4, 4, -4, 4, pts=[(3,3,'A',0,'ne'),(-2,1,'B',0,'nw'),(-3,-3,'C',0,'sw'),(1,-2,'D',0,'se'),(2,0,'E',0,'ne'),(0,2,'F',0,'ne')]))]),
]))

# ---------------------------------------------------------------- ①-2
SHEETS.append(dict(no='①-2', title='ベクトルと同じように考えられる計算', blocks=[
  ('tbl', '和・差・実数倍・共役　<small>複素数 $z=a+bi$ は，ベクトル $(a,\\ b)$ と同じように図で扱える。</small>', ['計算', '複素数平面での意味', 'ベクトルでは'], [
    ['和　$z_1+z_2$', '点 $z_1$ を，$z_2$ の分だけ [[平行移動]] した点', '$\\overrightarrow{a}+\\overrightarrow{b}$'],
    ['差　$z_1-z_2$', '点 $z_2$ から点 $z_1$ へ向かう矢印を，原点から引いた先', '$\\overrightarrow{a}-\\overrightarrow{b}$'],
    ['実数倍　$kz$', '原点と点 $z$ を通る [[直線]] 上。原点からの距離は $|k|$ 倍', '$k\\overrightarrow{a}$'],
    ['共役　$\\overline{z}=a-bi$', '点 $z$ と [[実軸]] に関して対称な点', '$y$ 座標の符号を変える']]),
  ('group', '例', '$z_1=1+2i$，$z_2=4+i$ のとき，次の点を図示せよ。', [
    it('', '$z_1+z_2$，$z_1-z_2$，$2z_1$，$\\overline{z_1}$', ['$z_1+z_2=5+3i$，$z_1-z_2=-3+i$', '$2z_1=2+4i$，$\\overline{z_1}=1-2i$'],
       P(-4, 6, -3, 5, pts=[(1,2,'z₁',0,'nw'),(4,1,'z₂',0,'se'),(5,3,'z₁+z₂',1,'ne'),(-3,1,'z₁−z₂',1,'nw'),(2,4,'2z₁',1,'ne'),(1,-2,'z̄₁',1,'se')],
         vec=[(1,2,5,3,'d'),(4,1,5,3,'d')]))]),
  ('group', '練習', '$z=-3+2i$，$w=1+i$ のとき，次の点を図示せよ。', [
    it('', '⑴ $z+w$　⑵ $z-w$　⑶ $2w$　⑷ $\\overline{z}$', ['⑴ $z+w=-2+3i$　⑵ $z-w=-4+i$', '⑶ $2w=2+2i$　⑷ $\\overline{z}=-3-2i$'],
       P(-5, 3, -3, 4, pts=[(-3,2,'z',0,'nw'),(1,1,'w',0,'se'),(-2,3,'⑴',1,'ne'),(-4,1,'⑵',1,'nw'),(2,2,'⑶',1,'ne'),(-3,-2,'⑷',1,'sw')]))]),
]))

# ---------------------------------------------------------------- ①-3
SHEETS.append(dict(no='①-3', title='複素数の絶対値', blocks=[
  ('box', '複素数の絶対値', [
    '原点 O と点 $z=a+bi$ の距離を $z$ の [[絶対値]] といい，$|z|$ で表す。',
    '三平方の定理より　$|z|^2=$ [[$a^2+b^2$]]',
    'よって　$|z|=|a+bi|=$ [[$\\sqrt{a^2+b^2}$]]']),
  ('group', '例', '', [it('', '$|3+4i|$ を求めよ。', [r'|3+4i|=\sqrt{3^2+4^2}=\sqrt{25}=5'])]),
  ('group', '練習', '次の複素数の絶対値を求めよ。', [
    it('⑴', '$3-4i$', [r'|3-4i|=\sqrt{3^2+(-4)^2}=\sqrt{25}=5']),
    it('⑵', '$-2i$', [r'|-2i|=\sqrt{0^2+(-2)^2}=2']),
    it('⑶', '$1+\\sqrt{3}i$', [r'|1+\sqrt{3}i|=\sqrt{1^2+(\sqrt{3})^2}=\sqrt{4}=2'])]),
]))

# ---------------------------------------------------------------- ①-4
PR10 = [  # 問10：(番号, z, くくった 形, 極形式)
  ('⑴', r'\sqrt{3}+i', r'2\left(\frac{\sqrt{3}}{2}+\frac{1}{2}i\right)', r'2(\cos30^\circ+i\sin30^\circ)'),
  ('⑵', r'-1+i', r'\sqrt{2}\left(-\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}i\right)', r'\sqrt{2}(\cos135^\circ+i\sin135^\circ)'),
  ('⑶', r'1-i', r'\sqrt{2}\left(\frac{1}{\sqrt{2}}-\frac{1}{\sqrt{2}}i\right)', r'\sqrt{2}(\cos315^\circ+i\sin315^\circ)'),
  ('⑷', r'-1+\sqrt{3}i', r'2\left(-\frac{1}{2}+\frac{\sqrt{3}}{2}i\right)', r'2(\cos120^\circ+i\sin120^\circ)'),
  ('⑸', r'-\sqrt{3}+i', r'2\left(-\frac{\sqrt{3}}{2}+\frac{1}{2}i\right)', r'2(\cos150^\circ+i\sin150^\circ)'),
  ('⑹', r'2+2i', r'2\sqrt{2}\left(\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}i\right)', r'2\sqrt{2}(\cos45^\circ+i\sin45^\circ)'),
  ('⑺', r'i', None, r'\cos90^\circ+i\sin90^\circ'),
  ('⑻', r'-3', None, r'3(\cos180^\circ+i\sin180^\circ)'),
  ('⑼', r'-1-\sqrt{3}i', r'2\left(-\frac{1}{2}-\frac{\sqrt{3}}{2}i\right)', r'2(\cos240^\circ+i\sin240^\circ)'),
  ('⑽', r'\sqrt{3}-i', r'2\left(\frac{\sqrt{3}}{2}-\frac{1}{2}i\right)', r'2(\cos330^\circ+i\sin330^\circ)'),
  ('⑾', r'-2i', None, r'2(\cos270^\circ+i\sin270^\circ)'),
  ('⑿', r'4', None, r'4(\cos0^\circ+i\sin0^\circ)'),
  ('⒀', r'-2-2i', r'2\sqrt{2}\left(-\frac{1}{\sqrt{2}}-\frac{1}{\sqrt{2}}i\right)', r'2\sqrt{2}(\cos225^\circ+i\sin225^\circ)'),
  ('⒁', r'1-\sqrt{3}i', r'2\left(\frac{1}{2}-\frac{\sqrt{3}}{2}i\right)', r'2(\cos300^\circ+i\sin300^\circ)'),
  ('⒂', r'3+\sqrt{3}i', r'2\sqrt{3}\left(\frac{\sqrt{3}}{2}+\frac{1}{2}i\right)', r'2\sqrt{3}(\cos30^\circ+i\sin30^\circ)'),
  ('⒃', r'-\sqrt{6}+\sqrt{2}i', r'2\sqrt{2}\left(-\frac{\sqrt{3}}{2}+\frac{1}{2}i\right)', r'2\sqrt{2}(\cos150^\circ+i\sin150^\circ)')]
SHEETS.append(dict(no='①-4', title='複素数の極形式', blocks=[
  ('box', '複素数の2通りの表し方', [
    '点 P の位置は，次の 2 通りで表せる。',
    '①　実軸方向に $a$，虚軸方向に $b$　→ $z=a+bi$',
    '②　向き $\\theta$ に，長さ $r$　→ 長さ $r$ と向き $\\theta$']),
  ('tbl', None, ['', '意味', '記号', '読み方'], [
    ['長さ $r$', '原点 O からの距離', '$|z|$', '$z$ の絶対値'],
    ['向き $\\theta$', '実軸の正の向きから，左回りに測った角', '$\\arg z$', '$z$ の偏角（arg：argument）']]),
  ('text', None, ['「$\\arg z=60^\\circ$」＝「$z$ は $60^\\circ$ の向きにある」']),
  ('box', '極形式', [
    '長さ $r$，向き $\\theta$ の点 P の座標は　$a=$ [[$r\\cos\\theta$]]，$b=$ [[$r\\sin\\theta$]]',
    'よって　$z=$ [[$r(\\cos\\theta+i\\sin\\theta)$]]',
    'これを $z$ の [[極形式]] という。',
    '$\\theta$ を $z$ の [[偏角]] といい，$\\arg z$ で表す。',
    '（$\\cos\\theta+i\\sin\\theta$：長さ $1$，向き $\\theta$ の数）']),
  ('tbl', '長さと向きを読み取る　<small>点 A〜D の長さと向きを読み取り，極形式と $a+bi$ の形で表せ。</small>', ['点', '長さ $r$', '向き $\\theta$', '極形式', '$a+bi$'], [
    ['A', '[[$2$]]', '[[$30^\\circ$]]', '[[$2(\\cos30^\\circ+i\\sin30^\\circ)$]]', '[[$\\sqrt{3}+i$]]'],
    ['B', '[[$3$]]', '[[$90^\\circ$]]', '[[$3(\\cos90^\\circ+i\\sin90^\\circ)$]]', '[[$3i$]]'],
    ['C', '[[$1$]]', '[[$180^\\circ$]]', '[[$\\cos180^\\circ+i\\sin180^\\circ$]]', '[[$-1$]]'],
    ['D', '[[$2$]]', '[[$225^\\circ$]]', '[[$2(\\cos225^\\circ+i\\sin225^\\circ)$]]', '[[$-\\sqrt{2}-\\sqrt{2}i$]]']]),
  ('group', '例', '偏角 $\\theta$ は $0^\\circ\\leqq\\theta<360^\\circ$ とする。', [
    it('', '$1+i$ を極形式で表せ。', [
      '$r=|1+i|=$ [[$\\sqrt{1^2+1^2}$]] $=$ [[$\\sqrt{2}$]]',
      '$\\cos\\theta=$ [[$\\frac{1}{\\sqrt{2}}$]]，$\\sin\\theta=$ [[$\\frac{1}{\\sqrt{2}}$]]',
      '$0^\\circ\\leqq\\theta<360^\\circ$ より　$\\theta=$ [[$45^\\circ$]]',
      'よって　$1+i=$ [[$\\sqrt{2}$]] $(\\cos$ [[$45^\\circ$]] $+i\\sin$ [[$45^\\circ$]] $)$'],
      notes=[N('Point', ['$r=\\sqrt{a^2+b^2}$', '$\\cos\\theta=\\frac{a}{r}$，$\\sin\\theta=\\frac{b}{r}$'])])]),
  ('text', '特別な角は「くくる」だけ', [
    '絶対値 $r$ でくくると，かっこの中が $\\cos\\theta$，$\\sin\\theta$ の値になる。',
    '$1+i=\\sqrt{2}\\left(\\frac{1}{\\sqrt{2}}+\\frac{1}{\\sqrt{2}}i\\right)=\\sqrt{2}(\\cos$ [[$45^\\circ$]] $+i\\sin$ [[$45^\\circ$]] $)$',
    '$1+\\sqrt{3}i=2($ [[$\\frac{1}{2}$]] $+$ [[$\\frac{\\sqrt{3}}{2}$]] $i)=2(\\cos$ [[$60^\\circ$]] $+i\\sin$ [[$60^\\circ$]] $)$']),
  ('tbl', 'Point', ['$\\theta$', '$0^\\circ$', '$30^\\circ$', '$45^\\circ$', '$60^\\circ$', '$90^\\circ$'], [
    ['$\\sin\\theta$', '$0$', '$\\frac{1}{2}$', '$\\frac{1}{\\sqrt{2}}$', '$\\frac{\\sqrt{3}}{2}$', '$1$'],
    ['$\\cos\\theta$', '$1$', '$\\frac{\\sqrt{3}}{2}$', '$\\frac{1}{\\sqrt{2}}$', '$\\frac{1}{2}$', '$0$'],
    ['$\\tan\\theta$', '$0$', '$\\frac{1}{\\sqrt{3}}$', '$1$', '$\\sqrt{3}$', 'なし']]),
  ('group', '問10', '次の複素数を極形式で表せ。ただし，偏角 $\\theta$ は $0^\\circ\\leqq\\theta<360^\\circ$ とする。', [
    it(n, f'${z}$', ([f'={k}'] if k else []) + [f'={p}']) for n, z, k, p in PR10]),
]))

# ---------------------------------------------------------------- ②-1
SHEETS.append(dict(no='②-1', title='掛け算と長さ・向き', blocks=[
  ('text', '$i$ を掛けると　<small>$1$ に $i$ を次々に掛ける。</small>', [
    '$1\\times i=$ [[$i$]]　　$i\\times i=$ [[$-1$]]　　$(-1)\\times i=$ [[$-i$]]　　$(-i)\\times i=$ [[$1$]]',
    '→ $i$ を掛けると，原点のまわりに [[$90^\\circ$]] 回転',
    '→ $i^2=-1$：$90^\\circ$ 回転を 2 回で反対向き']),
  ('tbl', '掛け算と長さ・向き　<small>次の積を計算し，結果の長さ（絶対値）と向き（偏角）を求めよ。</small>', ['積', '$z_1$ の長さ，向き', '$z_2$ の長さ，向き', '計算した結果', '結果の長さ，向き'], [
    ['$2\\times(1+i)$', '$2$，$0^\\circ$', '$\\sqrt{2}$，$45^\\circ$', '[[$2+2i$]]', '[[$2\\sqrt{2}$，$45^\\circ$]]'],
    ['$i\\times(1+i)$', '$1$，$90^\\circ$', '$\\sqrt{2}$，$45^\\circ$', '[[$-1+i$]]', '[[$\\sqrt{2}$，$135^\\circ$]]'],
    ['$(-1)\\times(1+i)$', '$1$，$180^\\circ$', '$\\sqrt{2}$，$45^\\circ$', '[[$-1-i$]]', '[[$\\sqrt{2}$，$225^\\circ$]]'],
    ['$(1+i)\\times(1+i)$', '$\\sqrt{2}$，$45^\\circ$', '$\\sqrt{2}$，$45^\\circ$', '[[$2i$]]', '[[$2$，$90^\\circ$]]'],
    ['$i\\times(\\sqrt{3}+i)$', '$1$，$90^\\circ$', '$2$，$30^\\circ$', '[[$-1+\\sqrt{3}i$]]', '[[$2$，$120^\\circ$]]'],
    ['$(1+\\sqrt{3}i)(\\sqrt{3}+i)$', '$2$，$60^\\circ$', '$2$，$30^\\circ$', '[[$4i$]]', '[[$4$，$90^\\circ$]]']]),
  ('text', '（計算）', [
    '$2\\times(1+i)=2+2i$', '$i\\times(1+i)=i+i^2=-1+i$', '$(-1)\\times(1+i)=-1-i$', '$(1+i)\\times(1+i)=1+2i+i^2=2i$',
    '$i\\times(\\sqrt{3}+i)=\\sqrt{3}i+i^2=-1+\\sqrt{3}i$', '$(1+\\sqrt{3}i)(\\sqrt{3}+i)=\\sqrt{3}+i+3i+\\sqrt{3}i^2=4i$',
    '→ 長さは [[掛け算]]，向きは [[足し算]]']),
]))

# ---------------------------------------------------------------- ②-2
SHEETS.append(dict(no='②-2', title='複素数の積', blocks=[
  ('box', '複素数の積', [
    '$z_1=r_1(\\cos\\theta_1+i\\sin\\theta_1)$，$z_2=r_2(\\cos\\theta_2+i\\sin\\theta_2)$ のとき',
    '$z_1z_2=$ [[$r_1r_2\\{\\cos(\\theta_1+\\theta_2)+i\\sin(\\theta_1+\\theta_2)\\}$]]']),
  ('box', '式の持つ意味', [
    '大きさ $r$ は [[積]]　…　$|z_1z_2|=$ [[$r_1r_2$]]',
    '偏角 $\\theta$ は [[和]]　…　$\\arg(z_1z_2)=$ [[$\\theta_1+\\theta_2$]]']),
  ('text', '導出', [
    '$z_1z_2=r_1r_2(\\cos\\theta_1+i\\sin\\theta_1)(\\cos\\theta_2+i\\sin\\theta_2)$',
    '$=r_1r_2(\\cos\\theta_1\\cos\\theta_2+i\\cos\\theta_1\\sin\\theta_2+i\\sin\\theta_1\\cos\\theta_2+i^2\\sin\\theta_1\\sin\\theta_2)$',
    '$=r_1r_2\\{(\\cos\\theta_1\\cos\\theta_2-\\sin\\theta_1\\sin\\theta_2)+i(\\sin\\theta_1\\cos\\theta_2+\\cos\\theta_1\\sin\\theta_2)\\}$',
    '$=r_1r_2\\{\\cos(\\theta_1+\\theta_2)+i\\sin(\\theta_1+\\theta_2)\\}$']),
  ('note', 'Point', ['$i^2=-1$，$\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta$，$\\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta$'], None),
  ('group', '例', '', [
    it('', '$z_1=1+i$，$z_2=\\sqrt{3}+i$ のとき，積 $z_1z_2$ の絶対値と偏角を求めよ。また，点 $z_1z_2$ を図示せよ。', [
      r'z_1=\sqrt{2}(\cos45^\circ+i\sin45^\circ)', r'z_2=2(\cos30^\circ+i\sin30^\circ)',
      r'|z_1z_2|=\sqrt{2}\times2=2\sqrt{2}', r'\arg(z_1z_2)=45^\circ+30^\circ=75^\circ'],
      P(-1, 3, -1, 3, u=40, pts=[(1,1,'z₁',0,'se'),(S3,1,'z₂',0,'se'),(S3-1,S3+1,'z₁z₂',1,'ne')], vec=[(0,0,S3-1,S3+1,'a')]))]),
  ('group', '問11', '次の複素数について，積 $z_1z_2$ の絶対値と偏角を求めよ。', [
    it('⑴', '$z_1=2i$，$z_2=3+3i$', [
      r'z_1=2(\cos90^\circ+i\sin90^\circ)', r'z_2=3\sqrt{2}(\cos45^\circ+i\sin45^\circ)',
      '絶対値　$2\\times3\\sqrt{2}=6\\sqrt{2}$', '偏角　$90^\\circ+45^\\circ=135^\\circ$', '（確かめ：$z_1z_2=-6+6i$）'],
      P(-7, 4, -1, 7, pts=[(0,2,'z₁',0,'ne'),(3,3,'z₂',0,'ne'),(-6,6,'z₁z₂',1,'ne')], vec=[(0,0,-6,6,'a')])),
    it('⑵', '$z_1=\\sqrt{3}+i$，$z_2=-1+\\sqrt{3}i$', [
      r'z_1=2(\cos30^\circ+i\sin30^\circ)', r'z_2=2(\cos120^\circ+i\sin120^\circ)',
      '絶対値　$2\\times2=4$', '偏角　$30^\\circ+120^\\circ=150^\\circ$', '（確かめ：$z_1z_2=-2\\sqrt{3}+2i$）'],
      P(-4, 3, -1, 3, pts=[(S3,1,'z₁',0,'se'),(-1,S3,'z₂',0,'ne'),(-2*S3,2,'z₁z₂',1,'nw')], vec=[(0,0,-2*S3,2,'a')]))]),
]))

# ---------------------------------------------------------------- ②-3
SHEETS.append(dict(no='②-3', title='掛け算と回転', blocks=[
  ('box', '複素数の積の図形的な意味', [
    '$2(\\cos60^\\circ+i\\sin60^\\circ)$ を掛ける　＝　「$2$ 倍に伸ばして，$60^\\circ$ 回す」',
    '$z_2=r(\\cos\\theta+i\\sin\\theta)$ のとき，点 $z_1z_2$ は',
    '　点 $z_1$ を原点のまわりに [[$\\theta$]] だけ回転し，原点からの距離を [[$r$]] 倍した点',
    'とくに $r=1$ のとき，点 $z_1(\\cos\\theta+i\\sin\\theta)$ は，点 $z_1$ を原点のまわりに [[$\\theta$]] だけ回転した点']),
  ('box', '原点のまわりの回転（$i=\\cos90^\\circ+i\\sin90^\\circ$ など）', [
    '点 $z_1i$ は，点 $z_1$ を [[$90^\\circ$]] だけ回転した点',
    '点 $-z_1$ は，点 $z_1$ を [[$180^\\circ$]] だけ回転した点',
    '点 $-z_1i$ は，点 $z_1$ を [[$-90^\\circ$]] だけ回転した点',
    '（参考）割り算は逆向きの回転：点 $\\frac{z_1}{z_2}$ は，点 $z_1$ を原点のまわりに [[$-\\theta$]] だけ回転し，原点からの距離を $\\frac{1}{r}$ 倍した点']),
  ('note', 'Point', ['$\\theta$ 回転するには $\\cos\\theta+i\\sin\\theta$ を掛ける'], None),
  ('group', '例', '点 $2+2i$ を，原点のまわりに次の角だけ回転した点を表す複素数を求めよ。', [
    it('⑴', '$90^\\circ$', ['$90^\\circ$ 回転は $i$ を掛けることだから　$(2+2i)i=2i+2i^2=-2+2i$']),
    it('⑵', '$45^\\circ$', [r'(2+2i)(\cos45^\circ+i\sin45^\circ)=(2+2i)\left(\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}i\right)',
                          r'=\frac{1}{\sqrt{2}}(2+2i+2i+2i^2)=\frac{4i}{\sqrt{2}}=2\sqrt{2}i']),
    it('⑶', '$60^\\circ$', [r'(2+2i)(\cos60^\circ+i\sin60^\circ)=(2+2i)\left(\frac{1}{2}+\frac{\sqrt{3}}{2}i\right)',
                          r'=(1+i)(1+\sqrt{3}i)=(1-\sqrt{3})+(1+\sqrt{3})i'],
       P(-3, 3, -1, 3, pts=[(2,2,'2+2i',0,'se'),(-2,2,'⑴',1,'nw'),(0,2*S2,'⑵',1,'ne'),(1-S3,1+S3,'⑶',1,'nw')]))]),
  ('group', '問13', '$z_1=1+\\sqrt{3}i$ とする。点 $z_1$ を原点のまわりに次の角度だけ回転した点を表す複素数を求めよ。', [
    it('⑴', '$30^\\circ$', [r'(1+\sqrt{3}i)(\cos30^\circ+i\sin30^\circ)=(1+\sqrt{3}i)\left(\frac{\sqrt{3}}{2}+\frac{1}{2}i\right)',
                          r'=\frac{\sqrt{3}}{2}+\frac{1}{2}i+\frac{3}{2}i-\frac{\sqrt{3}}{2}=2i']),
    it('⑵', '$60^\\circ$', [r'(1+\sqrt{3}i)(\cos60^\circ+i\sin60^\circ)=(1+\sqrt{3}i)\left(\frac{1}{2}+\frac{\sqrt{3}}{2}i\right)',
                          r'=\frac{1}{2}+\frac{\sqrt{3}}{2}i+\frac{\sqrt{3}}{2}i-\frac{3}{2}=-1+\sqrt{3}i']),
    it('⑶', '$90^\\circ$', ['$90^\\circ$ 回転は $i$ を掛けることだから', r'(1+\sqrt{3}i)i=i+\sqrt{3}i^2=-\sqrt{3}+i'],
       P(-2, 2, -1, 3, pts=[(1,S3,'z₁',0,'ne'),(0,2,'⑴',1,'ne'),(-1,S3,'⑵',1,'nw'),(-S3,1,'⑶',1,'nw')]))]),
]))

# ---------------------------------------------------------------- ③-1
SP = [(1,1),(0,2),(-2,2),(-4,0)]
SHEETS.append(dict(no='③-1', title='ド・モアブルの定理', blocks=[
  ('tbl', '同じ回転のくり返し　<small>$w=\\cos45^\\circ+i\\sin45^\\circ$（長さ $1$，向き $45^\\circ$）を次々に掛ける。（掛け算：長さは掛け算，向きは足し算）</small>',
   ['', '$w$', '$w^2$', '$w^3$', '$w^4$', '$w^8$'], [
    ['向き', '$45^\\circ$', '[[$90^\\circ$]]', '[[$135^\\circ$]]', '[[$180^\\circ$]]', '[[$360^\\circ$]]'],
    ['値', '$w$', '[[$i$]]', '[[$-\\frac{1}{\\sqrt{2}}+\\frac{1}{\\sqrt{2}}i$]]', '[[$-1$]]', '[[$1$]]']]),
  ('text', None, ['→ $w^n$ の向きは [[$45^\\circ\\times n$]]，$w^8=$ [[$1$]]（1周して元に戻る）']),
  ('box', 'ド・モアブルの定理', [
    '$n$ が整数のとき　$(\\cos\\theta+i\\sin\\theta)^n=$ [[$\\cos n\\theta+i\\sin n\\theta$]]',
    '（$\\theta$ 回転を $n$ 回くり返す　＝　$n\\theta$ 回転）']),
  ('group', '例', '', [
    it('', '$(1+i)^4$ の値を求めよ。また，$1+i$，$(1+i)^2$，$(1+i)^3$，$(1+i)^4$ を図示せよ。', [
      '$1+i=\\sqrt{2}(\\cos45^\\circ+i\\sin45^\\circ)$ より',
      r'(1+i)^4=(\sqrt{2})^4(\cos180^\circ+i\sin180^\circ)=4\times(-1)=-4',
      '$(1+i)^2=2i$，$(1+i)^3=-2+2i$，$(1+i)^4=-4$',
      '→ $45^\\circ$ ずつ回転し，原点からの距離は $\\sqrt{2}$ 倍ずつ'],
      P(-5, 2, -1, 3, pts=[(1,1,'1+i',1,'se'),(0,2,'(1+i)²',1,'ne'),(-2,2,'(1+i)³',1,'nw'),(-4,0,'(1+i)⁴',1,'nw')],
        vec=[(0,0,a,b,'a') for a, b in SP]))]),
  ('group', '問16', '次の複素数の値を求めよ。', [
    it('⑴', '$(1+\\sqrt{3}i)^3$', ['$1+\\sqrt{3}i=2(\\cos60^\\circ+i\\sin60^\\circ)$ より',
                               r'(1+\sqrt{3}i)^3=2^3(\cos180^\circ+i\sin180^\circ)=8\times(-1)=-8']),
    it('⑵', '$(1+i)^7$', ['$1+i=\\sqrt{2}(\\cos45^\\circ+i\\sin45^\\circ)$ より',
                        r'(1+i)^7=(\sqrt{2})^7(\cos315^\circ+i\sin315^\circ)', r'=8\sqrt{2}\left(\frac{1}{\sqrt{2}}-\frac{1}{\sqrt{2}}i\right)=8-8i'])]),
]))

# ---------------------------------------------------------------- ③-2
def ngon(n): return [(math.cos(2*math.pi*k/n), math.sin(2*math.pi*k/n)) for k in range(n)]
SHEETS.append(dict(no='③-2', title='1の $n$ 乗根', blocks=[
  ('box', '$n$ 乗根', [
    '$n$ を正の整数，$\\alpha$ を複素数とするとき，方程式 $z^n=\\alpha$ の解を $\\alpha$ の [[$n$ 乗根]] という。',
    '$z^3=1$ の解　＝　$3$ 回掛けると $1$ に戻る数',
    '　→ $1$ 回で [[$120^\\circ$]] 回転する数（円周の $3$ 等分点）']),
  ('note', 'Point', ['$(\\cos\\theta+i\\sin\\theta)^n=\\cos n\\theta+i\\sin n\\theta$', '偏角：$+360^\\circ\\times k$'], None),
  ('group', '例', '', [
    it('', '方程式 $z^3=1$ を解け。', [
      '$z=r(\\cos\\theta+i\\sin\\theta)$ とおくと　$z^3=r^3(\\cos3\\theta+i\\sin3\\theta)$',
      '$1=\\cos0^\\circ+i\\sin0^\\circ$ より',
      '$r^3=1$，$3\\theta=0^\\circ+360^\\circ\\times k$（$k$ は整数）',
      '$r=1$，$\\theta=120^\\circ\\times k$',
      '$0^\\circ\\leqq\\theta<360^\\circ$ より　$k=0,\\ 1,\\ 2$',
      r'z=1,\ -\frac{1}{2}+\frac{\sqrt{3}}{2}i,\ -\frac{1}{2}-\frac{\sqrt{3}}{2}i',
      '解を表す点は，点 $1$ を頂点とする [[正三角形]] の頂点。'],
      P(-1.5, 1.5, -1.5, 1.5, u=70, grid=False, circle=True, poly=[ngon(3)], pts=[(a, b, '', 1, 'ne') for a, b in ngon(3)]))]),
  ('group', '問17', '', [
    it('', '$1$ の $4$ 乗根を求めよ。', [
      '$z=r(\\cos\\theta+i\\sin\\theta)$ とおくと　$z^4=r^4(\\cos4\\theta+i\\sin4\\theta)$',
      '$1$ を極形式で表すと　$1=\\cos0^\\circ+i\\sin0^\\circ$',
      '絶対値と偏角を比較して　$r^4=1$，$4\\theta=0^\\circ+360^\\circ\\times k$',
      'よって　$r=1$，$\\theta=90^\\circ\\times k$',
      '$0^\\circ\\leqq\\theta<360^\\circ$ より　$k=0,\\ 1,\\ 2,\\ 3$（$\\theta=0^\\circ,\\ 90^\\circ,\\ 180^\\circ,\\ 270^\\circ$）',
      'したがって，$1$ の $4$ 乗根は　$1,\\ i,\\ -1,\\ -i$'])]),
  ('group', '問18', '', [
    it('', '問17で求めた $1$ の $4$ 乗根を表す点を，複素数平面上に図示せよ。また，それらの点を結んでできる図形は何か。', [
      '点 $1$ を $1$ つの頂点とする正方形'],
      P(-1.5, 1.5, -1.5, 1.5, u=70, grid=False, circle=True, poly=[ngon(4)], pts=[(1,0,'1',1,'se'),(0,1,'i',1,'ne'),(-1,0,'−1',1,'nw'),(0,-1,'−i',1,'se')]))]),
]))

# ---------------------------------------------------------------- ③-3
SHEETS.append(dict(no='③-3', title='【発展】回転の応用', blocks=[
  ('group', '例', '回転を使って図形の頂点を求める', [
    it('', '原点 O と点 $\\mathrm{A}(2+2i)$ に対して，$\\triangle\\mathrm{OAB}$ が正三角形となる点 B を表す複素数を求めよ。', [
      '点 B は，点 A を原点のまわりに $60^\\circ$ または $-60^\\circ$ 回転した点',
      '$60^\\circ$：$(2+2i)\\left(\\frac{1}{2}+\\frac{\\sqrt{3}}{2}i\\right)=(1-\\sqrt{3})+(1+\\sqrt{3})i$',
      '$-60^\\circ$：$(2+2i)\\left(\\frac{1}{2}-\\frac{\\sqrt{3}}{2}i\\right)=(1+\\sqrt{3})+(1-\\sqrt{3})i$'],
      P(-2, 4, -2, 4, poly=[[(0,0),(2,2),(1-S3,1+S3)],[(0,0),(2,2),(1+S3,1-S3)]], pts=[(2,2,'A',0,'ne'),(1-S3,1+S3,'B',1,'nw'),(1+S3,1-S3,'B',1,'se')]),
      notes=[N('Point', ['$\\cos60^\\circ=\\frac{1}{2}$，$\\sin60^\\circ=\\frac{\\sqrt{3}}{2}$', '$\\cos(-\\theta)=\\cos\\theta$，$\\sin(-\\theta)=-\\sin\\theta$'])])]),
  ('group', '練習', '原点 O と点 $\\mathrm{A}(3+i)$ に対して，正方形 OABC をつくる。（頂点は O，A，B，C の順に反時計回り）', [
    it('⑴', '点 C は，点 A を原点のまわりに何度回転した点か。また，点 C を表す複素数を求めよ。', [
      '$90^\\circ$ 回転した点。', '$90^\\circ$ 回転は $i$ を掛けることだから　$(3+i)i=3i+i^2=-1+3i$']),
    it('⑵', '点 B を表す複素数を求めよ。', [
      '$\\overrightarrow{\\mathrm{OB}}=\\overrightarrow{\\mathrm{OA}}+\\overrightarrow{\\mathrm{OC}}$ より', '$(3+i)+(-1+3i)=2+4i$'],
      P(-2, 4, -1, 5, poly=[[(0,0),(3,1),(2,4),(-1,3)]], pts=[(3,1,'A',0,'se'),(-1,3,'C',1,'nw'),(2,4,'B',1,'ne')]))]),
]))
