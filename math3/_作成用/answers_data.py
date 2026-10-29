r"""プリント（２学期期末考査まで）の 解答の データ。answers.py が これを 読んで integral/解答.html を 作る
SHEETS の 1つ ＝ プリント 1枚：dict(no, title, boxes=[(名前, [行])], groups=[(見出し, [問])])
問：dict(t='⑴', q='TeX', a=['行', …], notes=[(題, ['行', …], 追加の日 or None)])
行：$ が あれば 文字と $TeX$ の まぜ書き、なければ TeX だけ（別行立ての 式）
"""
N = lambda title, lines, add=None: (title, lines, add)

def it(t, q, a, *notes):
    return dict(t=t, q=q, a=a, notes=list(notes))

SHEETS = []

# ---------------------------------------------------------------- ①-1
SHEETS.append(dict(no='①-1', title='$x^n$ の不定積分', boxes=[('公式', [
    r'$\displaystyle\int x^{\alpha}dx=\frac{1}{\alpha+1}x^{\alpha+1}+C$　（ただし $\alpha\neq-1$）',
    r'$\displaystyle\int\frac{1}{x}dx=\log|x|+C$'])],
  groups=[('例', [
    it('⑴', r'\int x^3dx', [r'=\frac{1}{4}x^4+C']),
    it('⑵', r'\int\frac{1}{x^3}dx', [r'=\int x^{-3}dx=-\frac{1}{2}x^{-2}+C', r'=-\frac{1}{2x^2}+C']),
    it('⑶', r'\int\sqrt{x}\,dx', [r'=\int x^{\frac{1}{2}}dx=\frac{2}{3}x^{\frac{3}{2}}+C', r'=\frac{2}{3}x\sqrt{x}+C']),
    it('⑷', r'\int\frac{1}{x}dx', [r'=\log|x|+C']),
    it('⑸', r'\int\frac{1}{\sqrt[3]{x^2}}dx', [r'=\int x^{-\frac{2}{3}}dx=3x^{\frac{1}{3}}+C', r'=3\sqrt[3]{x}+C'])]),
   ('問1（ノート）', [
    it('⑴', r'\int x^5dx', [r'=\frac{1}{6}x^6+C']),
    it('⑵', r'\int\frac{dx}{x^4}', [r'=\int x^{-4}dx=-\frac{1}{3}x^{-3}+C', r'=-\frac{1}{3x^3}+C']),
    it('⑶', r'\int\sqrt[3]{x}\,dx', [r'=\int x^{\frac{1}{3}}dx=\frac{3}{4}x^{\frac{4}{3}}+C', r'=\frac{3}{4}x\sqrt[3]{x}+C']),
    it('⑷', r'\int\frac{dx}{\sqrt{x}}', [r'=\int x^{-\frac{1}{2}}dx=2x^{\frac{1}{2}}+C', r'=2\sqrt{x}+C'])])]))

# ---------------------------------------------------------------- ①-2
SHEETS.append(dict(no='①-2', title='$x^n$ の不定積分　分子が多項式の場合', boxes=[('分子が多項式である場合の不定積分の方針', [
    '分子の各項を分母で割ってから，項ごとに積分する。'])],
  groups=[('例', [
    it('⑴', r'\int\frac{2x-3}{x^2}dx', [r'=\int\left(\frac{2}{x}-\frac{3}{x^2}\right)dx', r'=2\log|x|+\frac{3}{x}+C'])]),
   ('問2', [
    it('⑴', r'\int\left(x^3+\frac{1}{x^3}\right)dx', [r'=\int(x^3+x^{-3})dx=\frac{1}{4}x^4-\frac{1}{2}x^{-2}+C', r'=\frac{1}{4}x^4-\frac{1}{2x^2}+C']),
    it('⑵', r'\int\frac{2x^3+2x-4}{x^2}dx', [r'=\int\left(2x+\frac{2}{x}-\frac{4}{x^2}\right)dx=x^2+2\log|x|+\frac{4}{x}+C'],
       N('【$-\\frac{4}{x^2}$ の積分】', [r'→ $\displaystyle-\int4x^{-2}dx=\frac{-4}{-1}x^{-1}+C=+4x^{-1}+C$', '$-4\\div(-1)$：マイナス÷マイナスでプラス',
                                      r'→ $x^{-1}=\frac{1}{x}$ より $+\frac{4}{x}+C$'], '10/26')),
    it('⑶', r'\int\frac{3x-2}{\sqrt{x}}dx', [r'=\int\left(3x^{\frac{1}{2}}-2x^{-\frac{1}{2}}\right)dx=2x^{\frac{3}{2}}-4x^{\frac{1}{2}}+C', r'=2x\sqrt{x}-4\sqrt{x}+C'],
       N('【$\\sqrt{x}$ を指数に直す】', ['割り算は指数のひき算（$\\frac{x^3}{x^2}=x^{3-2}=x$ と同じ）',
                                   r'→ $\displaystyle\frac{3x}{\sqrt{x}}=\frac{3x^1}{x^{\frac{1}{2}}}=3x^{1-\frac{1}{2}}=3x^{\frac{1}{2}}$',
                                   r'→ $\displaystyle\frac{2}{\sqrt{x}}=\frac{2}{x^{\frac{1}{2}}}=2x^{-\frac{1}{2}}$'], '10/26'),
       N('【分数で割る＝逆数を掛ける】', [r'→ $\displaystyle\frac{3}{\frac{3}{2}}x^{\frac{3}{2}}-\frac{2}{\frac{1}{2}}x^{\frac{1}{2}}+C$',
                                     r'$3\div\frac{3}{2}=3\times\frac{2}{3}=2$，$2\div\frac{1}{2}=2\times2=4$'], '10/26')),
    it('⑷', r'\int\frac{(\sqrt{x}+2)^2}{x}dx', [r'=\int\frac{x+4\sqrt{x}+4}{x}dx', r'=\int\left(1+\frac{4}{\sqrt{x}}+\frac{4}{x}\right)dx=x+8\sqrt{x}+4\log x+C'],
       N('【$\\sqrt{x}$ があるので $x>0$】', [r'→ $\frac{\sqrt{x}}{x}=x^{\frac{1}{2}-1}=x^{-\frac{1}{2}}$，$4\div\frac{1}{2}=4\times2=8$',
                                        r'→ $x>0$ より $\log|x|=\log x$'], '10/26'))])]))

# ---------------------------------------------------------------- ①-3
SHEETS.append(dict(no='①-3', title='三角関数の不定積分', boxes=[('公式', [
    r'$\displaystyle\int\sin x\,dx=-\cos x+C$　　$\displaystyle\int\cos x\,dx=\sin x+C$　　$\displaystyle\int\frac{dx}{\cos^2x}=\tan x+C$'])],
  groups=[('例', [
    it('⑴', r'\int(\sin x+3\cos x)dx', [r'=-\cos x+3\sin x+C']),
    it('⑵', r'\int\tan^2x\,dx', [r'=\int\left(\frac{1}{\cos^2x}-1\right)dx', r'=\tan x-x+C'],
       N('【ヒント】', [r'$1+\tan^2x=\frac{1}{\cos^2x}$']))]),
   ('問3（ノート）', [
    it('⑴', r'\int(1-\sin x)dx', [r'=x+\cos x+C']),
    it('⑵', r'\int\frac{\cos^3x-1}{\cos^2x}dx', [r'=\int\left(\cos x-\frac{1}{\cos^2x}\right)dx=\sin x-\tan x+C']),
    it('⑶', r'\int(2-\tan x)\cos x\,dx', [r'=\int(2\cos x-\sin x)dx=2\sin x+\cos x+C'],
       N('【$\\tan x\\cos x$ の直し方】', [r'→ $\tan x\cos x=\frac{\sin x}{\cos x}\times\cos x=\sin x$', r'→ $-\sin x$ の積分は $+\cos x$（符号に注意）'], '10/26')),
    it('⑷', r'\int\left(\tan^2x-\frac{2}{\cos^2x}\right)dx', [r'=\int\left(-\frac{1}{\cos^2x}-1\right)dx=-\tan x-x+C'],
       N('【$\\tan^2x$ の直し方】', [r'$1+\tan^2x=\frac{1}{\cos^2x}$ より $\tan^2x=\frac{1}{\cos^2x}-1$',
                                  r'→ $\frac{1}{\cos^2x}-1-\frac{2}{\cos^2x}=-\frac{1}{\cos^2x}-1$'], '10/26'))])]))

# ---------------------------------------------------------------- ①-4
SHEETS.append(dict(no='①-4', title='指数関数の不定積分', boxes=[('公式', [
    r'$\displaystyle\int e^x\,dx=e^x+C$　　　$\displaystyle\int a^x\,dx=\frac{a^x}{\log a}+C$'])],
  groups=[('例', [
    it('⑴', r'\int(2e^x+1)dx', [r'=2e^x+x+C']),
    it('⑵', r'\int3^x\,dx', [r'=\frac{3^x}{\log3}+C'])]),
   ('問4', [
    it('⑴', r'\int4e^x\,dx', [r'=4e^x+C']),
    it('⑵', r'\int5^x\,dx', [r'=\frac{5^x}{\log5}+C']),
    it('⑶', r'\int(3x^2-2e^x)dx', [r'=x^3-2e^x+C'])])]))

# ---------------------------------------------------------------- ①-5
SHEETS.append(dict(no='①-5', title='合成関数の不定積分', boxes=[('帳尻合わせ', [
    'まず当たりをつけて、微分して余分に出る数を打ち消す数を掛ける。',
    r'$\displaystyle\int f(ax+b)\,dx=\frac{1}{a}F(ax+b)+C$　（$F(x)$ は $f(x)$ の不定積分）'])],
  groups=[('例', [
    it('⑴', r'\int(2x+3)^4dx', [r'=\frac{1}{2}\cdot\frac{1}{5}(2x+3)^5+C=\frac{1}{10}(2x+3)^5+C'],
       N('【帳尻合わせ】', [r'当たり：$\frac{1}{5}(2x+3)^5$', r'微分すると $\times2$ が余分に出る → $\times\frac{1}{2}$'])),
    it('⑵', r'\int\sin(4x-3)\,dx', [r'=\frac{1}{4}\cdot\{-\cos(4x-3)\}+C=-\frac{1}{4}\cos(4x-3)+C'],
       N('【帳尻合わせ】', [r'当たり：$-\cos(4x-3)$', r'微分すると $\times4$ が余分に出る → $\times\frac{1}{4}$'])),
    it('⑶', r'\int\sqrt{2x+5}\,dx', [r'=\int(2x+5)^{\frac{1}{2}}dx=\frac{1}{2}\cdot\frac{2}{3}(2x+5)^{\frac{3}{2}}+C=\frac{1}{3}(2x+5)\sqrt{2x+5}+C'],
       N('【帳尻合わせ】', [r'当たり：$\frac{2}{3}(2x+5)^{\frac{3}{2}}$', r'微分すると $\times2$ が余分に出る → $\times\frac{1}{2}$']))]),
   ('問5', [
    it('⑴', r'\int(3x+1)^3dx', [r'=\frac{1}{3}\cdot\frac{1}{4}(3x+1)^4+C', r'=\frac{1}{12}(3x+1)^4+C']),
    it('⑵', r'\int e^{2x-3}dx', [r'=\frac{1}{2}e^{2x-3}+C']),
    it('⑶', r'\int\sin(3x+4)\,dx', [r'=\frac{1}{3}\cdot\{-\cos(3x+4)\}+C', r'=-\frac{1}{3}\cos(3x+4)+C']),
    it('⑷', r'\int\cos\left(4x-\frac{\pi}{3}\right)dx', [r'=\frac{1}{4}\sin\left(4x-\frac{\pi}{3}\right)+C']),
    it('⑸', r'\int\sqrt{1-2x}\,dx', [r'=\left(-\frac{1}{2}\right)\cdot\frac{2}{3}(1-2x)^{\frac{3}{2}}+C=-\frac{1}{3}(1-2x)\sqrt{1-2x}+C']),
    it('⑹', r'\int\frac{dx}{3x+5}', [r'=\frac{1}{3}\log|3x+5|+C'],
       N('【帳尻合わせ】', [r'当たり：$\log|3x+5|$　→　微分すると $\frac{1}{3x+5}\times3$（3 倍 大きく 出る）',
                         r'→ $\frac{1}{3}$ を掛けて消す：$\frac{1}{3}\times\frac{1}{3x+5}\times3=\frac{1}{3x+5}$', r'→ 元の式も $\frac{1}{3}$ 倍'], '10/29'))])]))

# ---------------------------------------------------------------- ②-1
T = lambda s: r'\text{' + s + '}'
SHEETS.append(dict(no='②-1', title='置換積分の不定積分', boxes=[('置換積分法', [
    '① $t=$（かたまり）と置く', '② $\\frac{dx}{dt}$ を求め、$dx=$（$t$ の式）$dt$ として変形する', '③ 式を置き換える', '④ 積分し、元に戻す。'])],
  groups=[('例', [
    it('⑴', r'\int x(x-5)^4dx', [r'x-5=t\ \text{とおくと}\ \ x=t+5', r'\text{両辺を}\ t\ \text{で微分すると}\ \ \frac{dx}{dt}=1\ \ \text{よって}\ \ dx=dt',
        r'=\int(t+5)t^4dt=\int(t^5+5t^4)dt', r'=\frac{1}{6}t^6+t^5+C=\frac{1}{6}t^6+\frac{6}{6}t^5+C', r'=\frac{1}{6}t^5(t+6)+C',
        r'=\frac{1}{6}(x-5)^5\{(x-5)+6\}+C=\frac{1}{6}(x+1)(x-5)^5+C'],
       N('【$dx$ の求め方】', ['① $x$ を $t$ の式で表す：$x=t+5$', '② 両辺を $t$ で微分：$\\frac{dx}{dt}=1$', '③ 両辺に $dt$ をかけて：$dx=dt$']),
       N('【$x-5=t$ を そのまま $t$ で微分】', ['各項を $t$ で微分：$x\\to\\frac{dx}{dt}$，$5\\to0$，$t\\to1$', '→ $\\frac{dx}{dt}-0=1$ より $\\frac{dx}{dt}=1$，$dx=dt$'], '10/29'),
       N('【置き換え方】', ['① かたまり：$(x-5)^4\\to t^4$（$\\int x\\,t^4\\,dx$）', '② 前の $x$：$x=t+5$ を使う', '③ $dx$：$dx=dt$ を使う → $\\int(t+5)t^4dt$'], '10/29'),
       N('【分数でくくるコツ】', ['$t^5$ を $\\frac{6}{6}t^5$ と書きかえると', '→ $\\frac{1}{6}t^6+\\frac{6}{6}t^5=\\frac{1}{6}t^5(t+6)$', '$t$ を $x-5$ に戻すときは { } の中も！'])),
    it('⑵', r'\int x(2x+1)^3dx', [r'2x+1=t\ \text{とおくと}\ \ x=\frac{t-1}{2}=\frac{1}{2}t-\frac{1}{2}', r'\text{両辺を}\ t\ \text{で微分すると}\ \ \frac{dx}{dt}=\frac{1}{2}\ \ \text{よって}\ \ dx=\frac{1}{2}dt',
        r'=\int\frac{t-1}{2}\cdot t^3\cdot\frac{1}{2}dt=\frac{1}{4}\int(t^4-t^3)dt', r'=\frac{1}{4}\left(\frac{1}{5}t^5-\frac{1}{4}t^4\right)+C=\frac{1}{20}t^5-\frac{1}{16}t^4+C',
        r'=\frac{4}{80}t^5-\frac{5}{80}t^4+C=\frac{1}{80}t^4(4t-5)+C', r'=\frac{1}{80}(2x+1)^4\{4(2x+1)-5\}+C', r'=\frac{1}{80}(8x-1)(2x+1)^4+C'],
       N('【$dx$ の求め方】', ['$x=\\frac{1}{2}t-\\frac{1}{2}$ を $t$ で微分すると $\\frac{dx}{dt}=\\frac{1}{2}$ → $dx=\\frac{1}{2}dt$', '※ $dx=dt$ ではないので注意！']),
       N('【通分してからくくる】', ['20 と 16 の最小公倍数は 80 → $\\frac{1}{20}=\\frac{4}{80}$，$\\frac{1}{16}=\\frac{5}{80}$', '{ } の中：$4(2x+1)-5=8x-1$']))]),
   ('問6（ノート）', [
    it('⑴', r'\int x(x-4)^3dx', [r'x-4=t\ \text{とおくと}\ \ x=t+4', r'\frac{dx}{dt}=1\ \ \text{よって}\ \ dx=dt', r'=\int(t+4)t^3dt=\int(t^4+4t^3)dt',
        r'=\frac{1}{5}t^5+t^4+C=\frac{1}{5}t^5+\frac{5}{5}t^4+C', r'=\frac{1}{5}t^4(t+5)+C', r'=\frac{1}{5}(x-4)^4\{(x-4)+5\}+C', r'=\frac{1}{5}(x+1)(x-4)^4+C'],
       N('【くくり方】', ['$t^4$ を $\\frac{5}{5}t^4$ にして $\\frac{1}{5}t^4$ でくくる', '{ } の中：$(x-4)+5=x+1$'])),
    it('⑵', r'\int(x-1)(2x+3)^4dx', [r'2x+3=t\ \text{とおくと}\ \ x=\frac{t-3}{2}=\frac{1}{2}t-\frac{3}{2}', r'\frac{dx}{dt}=\frac{1}{2}\ \ \text{よって}\ \ dx=\frac{1}{2}dt',
        r'\text{また}\ \ x-1=\frac{t-3}{2}-\frac{2}{2}=\frac{t-5}{2}', r'=\int\frac{t-5}{2}\cdot t^4\cdot\frac{1}{2}dt=\frac{1}{4}\int(t^5-5t^4)dt',
        r'=\frac{1}{4}\left(\frac{1}{6}t^6-t^5\right)+C=\frac{1}{24}t^6-\frac{1}{4}t^5+C', r'=\frac{1}{24}t^6-\frac{6}{24}t^5+C=\frac{1}{24}t^5(t-6)+C',
        r'=\frac{1}{24}(2x+3)^5\{(2x+3)-6\}+C', r'=\frac{1}{24}(2x-3)(2x+3)^5+C'],
       N('【⑵のポイント】', ['$x-1$ も $t$ の式に直してから置き換える。', '$\\frac{1}{4}t^5=\\frac{6}{24}t^5$ と分母を 24 にそろえて $\\frac{1}{24}t^5$ でくくる。', '{ } の中：$(2x+3)-6=2x-3$']))])]))

# ---------------------------------------------------------------- ②-2
SHEETS.append(dict(no='②-2', title='置換積分の不定積分（√ を t に）', boxes=[],
  groups=[('例', [
    it('⑴', r'\int x\sqrt{x-1}\,dx', [r'\sqrt{x-1}=t\ \text{とおくと}\ \ x-1=t^2\ \ \text{より}\ \ x=t^2+1', r'\text{両辺を}\ t\ \text{で微分すると}\ \ \frac{dx}{dt}=2t\ \ \text{よって}\ \ dx=2t\,dt',
        r'=\int(t^2+1)\cdot t\cdot2t\,dt=\int(2t^4+2t^2)dt', r'=\frac{2}{5}t^5+\frac{2}{3}t^3+C', r'=\frac{6}{15}t^5+\frac{10}{15}t^3+C=\frac{2}{15}t^3(3t^2+5)+C',
        r'\text{ここで}\ \ t^2=x-1,\ \ t^3=t^2\cdot t=(x-1)\sqrt{x-1}', r'=\frac{2}{15}(x-1)\sqrt{x-1}\{3(x-1)+5\}+C', r'=\frac{2}{15}(3x+2)(x-1)\sqrt{x-1}+C'],
       N('【√ をまるごと $t$ とおく】', ['① $\\sqrt{x-1}=t$ の両辺を 2 乗して $x-1=t^2$', '② $x$ を $t$ の式で表す：$x=t^2+1$', '③ 両辺を $t$ で微分：$\\frac{dx}{dt}=2t$ → $dx=2t\\,dt$',
                                    '※ $x-1=t$ とおいても解けるが，$\\sqrt{t}$（$t$ の $\\frac{1}{2}$ 乗）の計算になる。']),
       N('【分数でくくるコツ】', ['$\\frac{2}{5}=\\frac{6}{15}$，$\\frac{2}{3}=\\frac{10}{15}$ と分母を 15 にそろえる', '共通な $\\frac{2}{15}t^3$ でくくると，( ) の中に $3t^2+5$ が残る', '{ } の中：$3(x-1)+5=3x+2$']))]),
   ('問7', [
    it('⑴', r'\int x\sqrt{x+1}\,dx', [r'\sqrt{x+1}=t\ \text{とおくと}\ \ x+1=t^2\ \ \text{より}\ \ x=t^2-1', r'\frac{dx}{dt}=2t\ \ \text{よって}\ \ dx=2t\,dt',
        r'=\int(t^2-1)\cdot t\cdot2t\,dt=\int(2t^4-2t^2)dt', r'=\frac{2}{5}t^5-\frac{2}{3}t^3+C=\frac{6}{15}t^5-\frac{10}{15}t^3+C', r'=\frac{2}{15}t^3(3t^2-5)+C',
        r'=\frac{2}{15}(x+1)\sqrt{x+1}\{3(x+1)-5\}+C', r'=\frac{2}{15}(3x-2)(x+1)\sqrt{x+1}+C'],
       N('【$t$ に戻すとき】', ['$t^2=x+1$，$t^3=(x+1)\\sqrt{x+1}$', '{ } の中：$3(x+1)-5=3x-2$'])),
    it('⑵', r'\int x\sqrt{2-x}\,dx', [r'\sqrt{2-x}=t\ \text{とおくと}\ \ 2-x=t^2\ \ \text{より}\ \ x=2-t^2', r'\frac{dx}{dt}=-2t\ \ \text{よって}\ \ dx=-2t\,dt',
        r'=\int(2-t^2)\cdot t\cdot(-2t)dt=\int(2t^4-4t^2)dt', r'=\frac{2}{5}t^5-\frac{4}{3}t^3+C=\frac{6}{15}t^5-\frac{20}{15}t^3+C', r'=\frac{2}{15}t^3(3t^2-10)+C',
        r'=\frac{2}{15}(2-x)\sqrt{2-x}\{3(2-x)-10\}+C', r'=-\frac{2}{15}(3x+4)(2-x)\sqrt{2-x}+C'],
       N('【符号に注意】', ['$dx=-2t\\,dt$ のマイナスを忘れない', '{ } の中：$3(2-x)-10=-3x-4=-(3x+4)$'])),
    it('⑶', r'\int x\sqrt{2x-1}\,dx', [r'\sqrt{2x-1}=t\ \text{とおくと}\ \ 2x-1=t^2\ \ \text{より}\ \ x=\frac{1}{2}t^2+\frac{1}{2}', r'\frac{dx}{dt}=t\ \ \text{よって}\ \ dx=t\,dt',
        r'=\int\left(\frac{1}{2}t^2+\frac{1}{2}\right)\cdot t\cdot t\,dt=\frac{1}{2}\int(t^4+t^2)dt', r'=\frac{1}{10}t^5+\frac{1}{6}t^3+C=\frac{3}{30}t^5+\frac{5}{30}t^3+C',
        r'=\frac{1}{30}t^3(3t^2+5)+C', r'=\frac{1}{30}(2x-1)\sqrt{2x-1}\{3(2x-1)+5\}+C', r'=\frac{1}{30}(2x-1)\sqrt{2x-1}(6x+2)+C', r'=\frac{1}{15}(3x+1)(2x-1)\sqrt{2x-1}+C'],
       N('【通分してからくくる】', ['10 と 6 の最小公倍数は 30 → $\\frac{1}{10}=\\frac{3}{30}$，$\\frac{1}{6}=\\frac{5}{30}$', '$6x+2=2(3x+1)$ の 2 で約分：$\\frac{1}{30}\\times2=\\frac{1}{15}$'])),
    it('⑷', r'\int\frac{x}{\sqrt{1-x}}dx', [r'\sqrt{1-x}=t\ \text{とおくと}\ \ 1-x=t^2\ \ \text{より}\ \ x=1-t^2', r'\frac{dx}{dt}=-2t\ \ \text{よって}\ \ dx=-2t\,dt',
        r'=\int\frac{1-t^2}{t}\cdot(-2t)dt=\int(2t^2-2)dt', r'=\frac{2}{3}t^3-2t+C=\frac{2}{3}t^3-\frac{6}{3}t+C', r'=\frac{2}{3}t(t^2-3)+C',
        r'=\frac{2}{3}\sqrt{1-x}\{(1-x)-3\}+C', r'=-\frac{2}{3}(x+2)\sqrt{1-x}+C'],
       N('【約分できる】', ['分母の $t$ と $-2t\\,dt$ の $t$ が約分されて消える', '{ } の中：$(1-x)-3=-(x+2)$']))])]))

# ---------------------------------------------------------------- ②-3
SHEETS.append(dict(no='②-3', title='置換積分の不定積分（x で微分する型）', boxes=[],
  groups=[('例', [
    it('⑴', r'\int\sin^2x\cos x\,dx', [r'\sin x=t\ \text{とおくと}', r'\text{両辺を}\ x\ \text{で微分すると}\ \ \cos x=\frac{dt}{dx}\ \ \text{よって}\ \ \cos x\,dx=dt',
        r'=\int(\sin x)^2\cdot\cos x\,dx=\int t^2dt', r'=\frac{1}{3}t^3+C', r'=\frac{1}{3}\sin^3x+C'],
       N('置換のコツ', ['$\\sin x=t$ と置くと，$\\cos x\\,dx=dt$ より $\\int t^2dt$ となることを予見しておく。']),
       N('【②-1 との違い】', ['$x=$（$t$ の式）に直しにくいときは，$t=\\sin x$ のまま両辺を $x$ で微分する', '$\\frac{dt}{dx}=\\cos x$ の両辺に $dx$ をかけて $\\cos x\\,dx=dt$', '式の中の「$\\cos x\\,dx$」をまるごと $dt$ に置きかえる']),
       N('【答えの書き方】', ['$(\\sin x)^3$ は $\\sin^3x$ と書く（$t=\\sin x$ を戻す）'])),
    it('⑵', r'\int xe^{x^2}dx', [r'x^2=t\ \text{とおくと}', r'\text{両辺を}\ x\ \text{で微分すると}\ \ 2x=\frac{dt}{dx}\ \ \text{よって}\ \ x\,dx=\frac{1}{2}dt',
        r'=\int e^{x^2}\cdot x\,dx=\int e^t\cdot\frac{1}{2}dt', r'=\frac{1}{2}\int e^tdt=\frac{1}{2}e^t+C', r'=\frac{1}{2}e^{x^2}+C'],
       N('置換のコツ', ['$x^2=t$ と置くと，$x\\,dx=\\frac{1}{2}dt$ より $\\frac{1}{2}\\int e^tdt$ となることを予見しておく。']),
       N('【$x\\,dx$ をまとめて置きかえる】', ['$2x\\,dx=dt$ の両辺を 2 でわって $x\\,dx=\\frac{1}{2}dt$', '問題の式に「$x\\,dx$」があるので，そのまま $\\frac{1}{2}dt$ に置きかえられる']))]),
   ('問8', [
    it('⑴', r'\int\cos^3x\sin x\,dx', [r'\cos x=t\ \text{とおくと}', r'-\sin x=\frac{dt}{dx}\ \ \text{よって}\ \ \sin x\,dx=-dt', r'=\int t^3\cdot(-1)dt=-\int t^3dt', r'=-\frac{1}{4}t^4+C', r'=-\frac{1}{4}\cos^4x+C'],
       N('【符号に注意】', ['$(\\cos x)\'=-\\sin x$ なので', '$\\sin x\\,dx=-dt$ のマイナスを忘れない'])),
    it('⑵', r'\int3x^2\sqrt{x^3+1}\,dx', [r'x^3+1=t\ \text{とおくと}', r'3x^2=\frac{dt}{dx}\ \ \text{よって}\ \ 3x^2dx=dt', r'=\int\sqrt{t}\,dt=\int t^{\frac{1}{2}}dt', r'=\frac{2}{3}t^{\frac{3}{2}}+C=\frac{2}{3}t\sqrt{t}+C', r'=\frac{2}{3}(x^3+1)\sqrt{x^3+1}+C'],
       N('【$t$ の $\\frac{3}{2}$ 乗の直し方】', ['→ $t^{\\frac{3}{2}}=t\\cdot t^{\\frac{1}{2}}=t\\sqrt{t}$'])),
    it('⑶', r'\int e^x(e^x+1)^2dx', [r'e^x+1=t\ \text{とおくと}', r'e^x=\frac{dt}{dx}\ \ \text{よって}\ \ e^xdx=dt', r'=\int t^2dt', r'=\frac{1}{3}t^3+C', r'=\frac{1}{3}(e^x+1)^3+C'],
       N('【展開しなくてよい】', ['$(e^x)\'=e^x$ なので $e^xdx$ がまるごと $dt$ になる'])),
    it('⑷', r'\int xe^{-x^2}dx', [r'-x^2=t\ \text{とおくと}', r'-2x=\frac{dt}{dx}\ \ \text{よって}\ \ x\,dx=-\frac{1}{2}dt', r'=\int e^t\cdot\left(-\frac{1}{2}\right)dt', r'=-\frac{1}{2}e^t+C', r'=-\frac{1}{2}e^{-x^2}+C'],
       N('【例⑵と同じ形】', ['$-2x\\,dx=dt$ の両辺を $-2$ でわって', '→ $x\\,dx=-\\frac{1}{2}dt$']))])]))

# ---------------------------------------------------------------- ②-4
SHEETS.append(dict(no='②-4', title='置換積分の不定積分（分子が分母の微分）', boxes=[],
  groups=[('例', [
    it('⑴', r'\int\frac{2x}{x^2+1}dx', [r'x^2+1=t\ \text{とおくと}', r'\text{両辺を}\ x\ \text{で微分すると}\ \ 2x=\frac{dt}{dx}\ \ \text{よって}\ \ 2x\,dx=dt',
        r'=\int\frac{1}{x^2+1}\cdot2x\,dx=\int\frac{1}{t}dt', r'=\log|t|+C', r'=\log(x^2+1)+C'],
       N('置換のコツ', ['$x^2+1=t$ と置くと，$2x\\,dx=dt$ より $\\int\\frac{1}{t}dt$ となり，$\\int\\frac{1}{t}dt=\\log|t|+C$ であることも先読みしておく。']),
       N('【| | がはずれる理由】', ['$x^2+1>0$ なので　$\\log|x^2+1|=\\log(x^2+1)$']),
       N('【公式】分子が分母の微分になっているとき', ['→ $\\displaystyle\\int\\frac{g\'(x)}{g(x)}dx=\\log|g(x)|+C$', '（問9 はすべてこの形）'])),
    it('⑵', r'\int\tan x\,dx', [r'\tan x=\frac{\sin x}{\cos x}\ \text{なので}\ \ \int\tan x\,dx=\int\frac{\sin x}{\cos x}dx', r'\cos x=t\ \text{とおくと}',
        r'\text{両辺を}\ x\ \text{で微分すると}\ \ -\sin x=\frac{dt}{dx}\ \ \text{よって}\ \ \sin x\,dx=-dt', r'=\int\frac{1}{\cos x}\cdot\sin x\,dx=\int\frac{1}{t}\cdot(-1)dt=-\int\frac{1}{t}dt',
        r'=-\log|t|+C', r'=-\log|\cos x|+C'],
       N('置換のコツ', ['$\\cos x=t$ と置くと，$\\sin x\\,dx=-dt$ より $-\\int\\frac{1}{t}dt$ となる。']),
       N('【$\\tan x$ はまず $\\frac{\\sin x}{\\cos x}$ に】', ['分母の $\\cos x$ を微分すると $-\\sin x$ で，分子の $\\sin x$ と符号だけちがう', 'だから答えにマイナスが付く']))]),
   ('問9', [
    it('⑴', r'\int\frac{2x-1}{x^2-x+1}dx', [r'x^2-x+1=t\ \text{とおくと}', r'2x-1=\frac{dt}{dx}\ \ \text{よって}\ \ (2x-1)dx=dt', r'=\int\frac{1}{t}dt=\log|t|+C', r'=\log(x^2-x+1)+C'],
       N('【| | をはずせる】', ['→ $x^2-x+1=\\left(x-\\frac{1}{2}\\right)^2+\\frac{3}{4}>0$'])),
    it('⑵', r'\int\frac{x}{x^2-2}dx', [r'x^2-2=t\ \text{とおくと}', r'2x=\frac{dt}{dx}\ \ \text{よって}\ \ x\,dx=\frac{1}{2}dt', r'=\int\frac{1}{t}\cdot\frac{1}{2}dt=\frac{1}{2}\int\frac{1}{t}dt', r'=\frac{1}{2}\log|t|+C', r'=\frac{1}{2}\log|x^2-2|+C'],
       N('【| | は残す】', ['$x^2-2$ は負にもなるので，絶対値はつけたままにする'])),
    it('⑶', r'\int\frac{e^x}{1+e^x}dx', [r'1+e^x=t\ \text{とおくと}', r'e^x=\frac{dt}{dx}\ \ \text{よって}\ \ e^xdx=dt', r'=\int\frac{1}{t}dt=\log|t|+C', r'=\log(1+e^x)+C'],
       N('【| | をはずせる】', ['$1+e^x>0$ なので絶対値はいらない'])),
    it('⑷', r'\int\frac{1}{\tan x}dx', [r'\frac{1}{\tan x}=\frac{\cos x}{\sin x}\ \text{なので}', r'\sin x=t\ \text{とおくと}', r'\cos x=\frac{dt}{dx}\ \ \text{よって}\ \ \cos x\,dx=dt',
        r'=\int\frac{\cos x}{\sin x}dx=\int\frac{1}{t}dt', r'=\log|t|+C', r'=\log|\sin x|+C'],
       N('【$\\frac{1}{\\tan x}$ の直し方】', ['$1\\div\\frac{\\sin x}{\\cos x}=\\frac{\\cos x}{\\sin x}$', '分子の $\\cos x$ は分母 $\\sin x$ の微分']))])]))

# ---------------------------------------------------------------- ③-1〜④-4（解答の 本体は プリントの docx に 書いた もの と 同じ）
A = {}   # no → (例の 解答 [[lines, cm]…], テキストボックスの 空らん, 問の 解答 {表の 順: [[lines, cm]…]})
PI = r"\text{f(x)}"
A['③-1'] = dict(
    ex=[[[r'=x(-\cos x)-\int{1\cdot(-\cos x)}dx', r'=-x\cos x+\int{\cos x}dx', r'=-x\cos x+\sin x+C'],
         ('【部分積分の使い方】', ['$f(x)=x$，$g\'(x)=\\sin x$ とすると', '$f\'(x)=1$，$g(x)=-\\cos x$', '→ $f(x)g(x)-\\int{f\'(x)g(x)}dx$ に入れる'])]],
    box=['$x$', '$\\sin x$', '$1\\cdot(-\\cos x)=-\\cos x$'],
    q=[[
        [[r'=x\sin x-\int{1\cdot\sin x}dx', r'=x\sin x+\cos x+C'], ('【選び方】', ['微分する方 $x$，積分する方 $\\cos x$'])],
        [[r'=x\cdot\left(-\frac{1}{3}\cos 3x\right)-\int{1\cdot\left(-\frac{1}{3}\cos 3x\right)}dx', r'=-\frac{1}{3}x\cos 3x+\frac{1}{3}\int{\cos 3x}dx',
          r'=-\frac{1}{3}x\cos 3x+\frac{1}{9}\sin 3x+C'], ('【積分する方】', ['$\\sin 3x$ を積分すると $-\\frac{1}{3}\\cos 3x$', '（①-5 の帳尻合わせ）'])],
        [[r'=(2x+1)(-\cos x)-\int{2\cdot(-\cos x)}dx', r'=-(2x+1)\cos x+2\int{\cos x}dx', r'=-(2x+1)\cos x+2\sin x+C'],
         ('【微分する方】', ['$2x+1$ を微分すると $2$'])],
        [[r'=(x+1)\cdot\frac{1}{2}\sin 2x-\int{1\cdot\frac{1}{2}\sin 2x}dx', r'=\frac{1}{2}(x+1)\sin 2x-\frac{1}{2}\cdot\left(-\frac{1}{2}\cos 2x\right)+C',
          r'=\frac{1}{2}(x+1)\sin 2x+\frac{1}{4}\cos 2x+C'], ('【積分する方】', ['$\\cos 2x$ を積分すると $\\frac{1}{2}\\sin 2x$'])],
    ]])
A['③-2'] = dict(
    ex=[[[r'=xe^{x}-\int{1\cdot e^{x}}dx', r'=xe^{x}-e^{x}+C', r'=(x-1)e^{x}+C'], None],
        [[r"=\int{(x)'\log x}dx", r'=x\log x-\int{x\cdot\frac{1}{x}}dx', r'=x\log x-\int{1}dx', r'=x\log x-x+C'],
         ('【log x は 1×log x と考える】', ['$1=(x)\'$ とみて，$1$ を積分する方にする', '$\\log x$ は微分すると $\\frac{1}{x}$ になり，約分できる'])]],
    box=['$x$', '$e^{x}$', '$1\\cdot e^{x}=e^{x}$', '$\\log x$', '$1$', '$\\frac{1}{x}\\cdot x=1$'],
    q=[[
        [[r'=(2x-1)e^{x}-\int{2e^{x}}dx', r'=(2x-1)e^{x}-2e^{x}+C', r'=(2x-3)e^{x}+C'], ('【まとめる】', ['$e^{x}$ でくくる：$(2x-1)-2=2x-3$'])],
        [[r'=x\cdot\frac{1}{2}e^{2x}-\int{1\cdot\frac{1}{2}e^{2x}}dx', r'=\frac{1}{2}xe^{2x}-\frac{1}{4}e^{2x}+C', r'=\frac{1}{4}(2x-1)e^{2x}+C'],
         ('【積分する方】', ['$e^{2x}$ を積分すると $\\frac{1}{2}e^{2x}$'])],
        [[r'=x(-e^{-x})-\int{1\cdot(-e^{-x})}dx', r'=-xe^{-x}+\int{e^{-x}}dx', r'=-xe^{-x}-e^{-x}+C', r'=-(x+1)e^{-x}+C'],
         ('【符号に注意】', ['$e^{-x}$ を積分すると $-e^{-x}$'])],
    ], [
        [[r"=\int{(x)'\log 2x}dx", r'=x\log 2x-\int{x\cdot\frac{2}{2x}}dx', r'=x\log 2x-\int{1}dx=x\log 2x-x+C'],
         ('【微分する方】', ['$(\\log 2x)\'=\\frac{2}{2x}=\\frac{1}{x}$'])],
        [[r'=\frac{1}{2}x^{2}\log x-\int{\frac{1}{2}x^{2}\cdot\frac{1}{x}}dx', r'=\frac{1}{2}x^{2}\log x-\frac{1}{2}\int{x}dx', r'=\frac{1}{2}x^{2}\log x-\frac{1}{4}x^{2}+C'],
         ('【選び方】', ['微分する方 $\\log x$，積分する方 $x$'])],
        [[r'=(x^{2}+x)\log x-\int{(x^{2}+x)\cdot\frac{1}{x}}dx', r'=(x^{2}+x)\log x-\int{(x+1)}dx', r'=(x^{2}+x)\log x-\frac{1}{2}x^{2}-x+C'],
         ('【選び方】', ['微分する方 $\\log x$，積分する方 $2x+1$'])],
        [[r"=\int{(x+1)'\log{(x+1)}}dx", r'=(x+1)\log{(x+1)}-\int{(x+1)\cdot\frac{1}{x+1}}dx', r'=(x+1)\log{(x+1)}-x+C'],
         ('【1 を (x+1)′ とみる】', ['$\\frac{1}{x+1}$ と約分できて計算が楽になる'])],
    ]])
A['④-1'] = dict(
    ex=[[[r'=\int{\left(2x+2+\frac{3}{x-1}\right)}dx', r'=x^{2}+2x+3\log\abs{x-1}+C'],
         ('【割り算】', ['$2x^{2}+1$ を $x-1$ で割ると', '商 $2x+2$，余り $3$'])],
        [[r'=\int{\frac{2}{(x-1)(x+1)}}dx=\int{\left(\frac{1}{x-1}-\frac{1}{x+1}\right)}dx', r'=\log\abs{x-1}-\log\abs{x+1}+C', r'=\log\abs{\frac{x-1}{x+1}}+C'],
         ('【部分分数に分解】', ['→ $\\frac{1}{x-1}-\\frac{1}{x+1}=\\frac{(x+1)-(x-1)}{(x-1)(x+1)}=\\frac{2}{x^{2}-1}$'])]],
    box=None,
    q=[[
        [[r'=\int{\left(x-2+\frac{5}{x+2}\right)}dx', r'=\frac{1}{2}x^{2}-2x+5\log\abs{x+2}+C'], ('【割り算】', ['商 $x-2$，余り $5$'])],
        [[r'=\int{\left(x+\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{2x-1}\right)}dx', r'=\frac{1}{2}x^{2}+\frac{1}{2}x+\frac{1}{4}\log\abs{2x-1}+C'],
         ('【割り算】', ['商 $x+\\frac{1}{2}$，余り $\\frac{1}{2}$', '$\\frac{1}{2x-1}$ の積分は $\\frac{1}{2}\\log\\abs{2x-1}$'])],
    ], [
        [[r'=\int{\left(\frac{1}{x}-\frac{1}{x+1}\right)}dx', r'=\log\abs{x}-\log\abs{x+1}+C', r'=\log\abs{\frac{x}{x+1}}+C'], None],
        [[r'=\frac{1}{4}\int{\left(\frac{1}{x-2}-\frac{1}{x+2}\right)}dx', r'=\frac{1}{4}\left(\log\abs{x-2}-\log\abs{x+2}\right)+C', r'=\frac{1}{4}\log\abs{\frac{x-2}{x+2}}+C'],
         ('【係数に注意】', ['$\\frac{1}{x-2}-\\frac{1}{x+2}=\\frac{4}{(x-2)(x+2)}$ なので $\\frac{1}{4}$ 倍'])],
        [[r'=\int{\frac{3}{(x-2)(x+1)}}dx=\int{\left(\frac{1}{x-2}-\frac{1}{x+1}\right)}dx', r'=\log\abs{x-2}-\log\abs{x+1}+C', r'=\log\abs{\frac{x-2}{x+1}}+C'],
         ('【まず因数分解】', ['$x^{2}-x-2=(x-2)(x+1)$'])],
    ]])
A['④-3'] = dict(
    ex=[[[r'=\int{\frac{1-\cos 2x}{2}}dx=\frac{1}{2}\int{(1-\cos 2x)}dx', r'=\frac{1}{2}\left(x-\frac{1}{2}\sin 2x\right)+C=\frac{1}{2}x-\frac{1}{4}\sin 2x+C'],
         ('【公式❶】', ['$\\sin^{2}x=\\frac{1-\\cos 2x}{2}$ で次数を下げる'])],
        [[r'=\int{\frac{1}{2}\sin 2x}dx', r'=\frac{1}{2}\cdot\left(-\frac{1}{2}\cos 2x\right)+C=-\frac{1}{4}\cos 2x+C'],
         ('【公式❸】', ['$\\sin x\\cos x=\\frac{\\sin 2x}{2}$'])]],
    box=None,
    q=[[
        [[r'=\int{\frac{1+\cos 2x}{2}}dx', r'=\frac{1}{2}x+\frac{1}{4}\sin 2x+C'], None],
        [[r'=\int{\frac{1-\cos 4x}{2}}dx', r'=\frac{1}{2}x-\frac{1}{8}\sin 4x+C'], ('【公式❶で x を 2x に】', ['$\\sin^{2}2x=\\frac{1-\\cos 4x}{2}$'])],
        [[r'=\int{(\sin^{2}x+2\sin x\cos x+\cos^{2}x)}dx', r'=\int{(1+\sin 2x)}dx', r'=x-\frac{1}{2}\cos 2x+C'],
         ('【展開して整理】', ['$\\sin^{2}x+\\cos^{2}x=1$，$2\\sin x\\cos x=\\sin 2x$'])],
    ]])
A['④-4'] = dict(
    ex=[[[r'=\int{\frac{1}{2}(\sin 4\theta+\sin 2\theta)}d\theta', r'=\frac{1}{2}\left(-\frac{1}{4}\cos 4\theta-\frac{1}{2}\cos 2\theta\right)+C',
          r'=-\frac{1}{8}\cos 4\theta-\frac{1}{4}\cos 2\theta+C'],
         ('【公式❹】', ['$\\alpha=3\\theta$，$\\beta=\\theta$ とすると', '$\\alpha+\\beta=4\\theta$，$\\alpha-\\beta=2\\theta$'])]],
    box=None,
    q=[[
        [[r'=\int{\frac{1}{2}(\sin 3\theta+\sin\theta)}d\theta', r'=\frac{1}{2}\left(-\frac{1}{3}\cos 3\theta-\cos\theta\right)+C', r'=-\frac{1}{6}\cos 3\theta-\frac{1}{2}\cos\theta+C'],
         ('【公式❹】', ['$\\alpha=2\\theta$，$\\beta=\\theta$'])],
        [[r'=\int{\frac{1}{2}(\cos 3x+\cos x)}dx', r'=\frac{1}{6}\sin 3x+\frac{1}{2}\sin x+C'], ('【公式❺】', ['$\\alpha=2x$，$\\beta=x$'])],
        [[r'=\int{\left\{-\frac{1}{2}(\cos 6x-\cos 2x)\right\}}dx', r'=-\frac{1}{2}\left(\frac{1}{6}\sin 6x-\frac{1}{2}\sin 2x\right)+C',
          r'=-\frac{1}{12}\sin 6x+\frac{1}{4}\sin 2x+C'], ('【公式❻】', ['$\\alpha=4x$，$\\beta=2x$', 'マイナスを忘れない'])],
    ]])
# ④-2 の 空らん（穴）：順番どおり
HOLES = [r'2\sin\alpha\cos\alpha', r'\cos^{2}\alpha-\sin^{2}\alpha', r'1-2\sin^{2}\alpha', r'2\cos^{2}\alpha-1',
         r'\frac{1-\cos 2x}{2}', r'\frac{1+\cos 2x}{2}', r'\frac{\sin 2x}{2}',
         r'2\sin\alpha\cos\beta', r'\frac{1}{2}\left\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\right\}',
         r'2\cos\alpha\cos\beta', r'-2\sin\alpha\sin\beta', r'-2']



def conv(pairs, qs, ts=None):
    out = []
    for k, ((lines, cm), q) in enumerate(zip(pairs, qs)):
        notes = [N(cm[0], cm[1])] if cm else []
        out.append(it('⑴⑵⑶⑷⑸⑹'[k], q, lines, *notes))
    return out

SHEETS.append(dict(no='③-1', title='部分積分の不定積分', boxes=[('部分積分法', [
    r'$\displaystyle\int f(x)g\'(x)\,dx=f(x)g(x)-\int f\'(x)g(x)\,dx$',
    '①【微分する方】$f(x)$ の選び方：微分しやすく、微分後の式が簡単になる方を選ぶ', '②【積分する方】$g\'(x)$ の選び方：積分しやすい方を選ぶ',
    '③「微分した方」と「積分した方」の積が積分できそうかを予想しておく'])],
  groups=[('例', conv(A['③-1']['ex'], [r'\int x\sin x\,dx'])),
          ('問10（ノート）', conv(A['③-1']['q'][0], [r'\int x\cos x\,dx', r'\int x\sin3x\,dx', r'\int(2x+1)\sin x\,dx', r'\int(x+1)\cos2x\,dx']))]))
SHEETS[-1]['groups'][0][1][0]['notes'].insert(0, N('【選び方】', ['微分する方を $x$ とし，積分する方を $\\sin x$ とすると，', '「微分した方」と「積分した方」の積は $1\\cdot(-\\cos x)=-\\cos x$ となり，積分しやすそう。']))

SHEETS.append(dict(no='③-2', title='部分積分の不定積分（eˣ・log x）', boxes=[],
  groups=[('例', conv(A['③-2']['ex'], [r'\int xe^x\,dx', r'\int\log x\,dx'])),
          ('問11（ノート）', conv(A['③-2']['q'][0], [r'\int(2x-1)e^x\,dx', r'\int xe^{2x}\,dx', r'\int xe^{-x}\,dx'])),
          ('問12（ノート）', conv(A['③-2']['q'][1], [r'\int\log2x\,dx', r'\int x\log x\,dx', r'\int(2x+1)\log x\,dx', r'\int\log(x+1)\,dx']))]))
SHEETS[-1]['groups'][0][1][0]['notes'].insert(0, N('【選び方】', ['微分する方を $x$ とし，積分する方を $e^x$ とすると，', '積は $1\\cdot e^x=e^x$ となり，積分しやすそう。']))
SHEETS[-1]['groups'][0][1][1]['notes'].insert(0, N('【選び方】', ['微分する方を $\\log x$ とし，積分する方を $1$ とすると，', '積は $\\frac{1}{x}\\cdot x=1$ となり，積分しやすそう。']))

SHEETS.append(dict(no='④-1', title='分数関数の不定積分', boxes=[('方針', [
    '「分子の次数」が「分母の次数」以上の時には，分子を分母で割って，「商＋余り／分母」の形にする。',
    '置換積分・部分積分が使えず，分母の次数が高い時には，部分分数に分解して，項ごとに積分をする。分母の次数が 1 次ならば積分可能。'])],
  groups=[('例', conv(A['④-1']['ex'], [r'\int\frac{2x^2+1}{x-1}dx', r'\int\frac{2}{x^2-1}dx'])),
          ('問14（ノート）', conv(A['④-1']['q'][0], [r'\int\frac{x^2+1}{x+2}dx', r'\int\frac{2x^2}{2x-1}dx'])),
          ('問16（ノート）', conv(A['④-1']['q'][1], [r'\int\frac{dx}{x(x+1)}', r'\int\frac{dx}{(x-2)(x+2)}', r'\int\frac{3}{x^2-x-2}dx']))]))
SHEETS[-1]['groups'][0][1][1]['notes'].insert(0, N('【使える？】', ['置換積分 → ×（分子が分母の微分でない）　部分積分 → ×']))

# ④-2：空らんを うめた 形で 書く（[[…]] が 答え）
SHEETS.append(dict(no='④-2', title='加法定理から半角の公式・積和の公式を導く', boxes=[('導く 公式', [
    r'❶ $\sin^2x=\frac{1-\cos2x}{2}$　❷ $\cos^2x=\frac{1+\cos2x}{2}$　❸ $\sin x\cos x=\frac{\sin2x}{2}$',
    r'❹ $\sin\alpha\cos\beta=\frac{1}{2}\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\}$',
    r'❺ $\cos\alpha\cos\beta=\frac{1}{2}\{\cos(\alpha+\beta)+\cos(\alpha-\beta)\}$',
    r'❻ $\sin\alpha\sin\beta=-\frac{1}{2}\{\cos(\alpha+\beta)-\cos(\alpha-\beta)\}$'])],
  derive=[
    ('Ⅰ　２倍角の公式', [
      r'加法定理　$\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$，$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ で，$\beta=\alpha$ とおくと',
      r'$\sin2\alpha=$ [[$2\sin\alpha\cos\alpha$]]　　$\cos2\alpha=$ [[$\cos^2\alpha-\sin^2\alpha$]]',
      r'さらに $\sin^2\alpha+\cos^2\alpha=1$ を使うと　$\cos2\alpha=$ [[$1-2\sin^2\alpha$]] $=$ [[$2\cos^2\alpha-1$]]']),
    ('Ⅱ　半角の公式・２倍角の公式の変形（２乗や積を，次数の低い式に直す）', [
      r'Ⅰの式の $\alpha$ を $x$ にかえて，$\sin^2x$，$\cos^2x$，$\sin x\cos x$ について解く。',
      r'$\cos2x=1-2\sin^2x$ より　❶ $\sin^2x=$ [[$\frac{1-\cos2x}{2}$]]',
      r'$\cos2x=2\cos^2x-1$ より　❷ $\cos^2x=$ [[$\frac{1+\cos2x}{2}$]]',
      r'$\sin2x=2\sin x\cos x$ より　❸ $\sin x\cos x=$ [[$\frac{\sin2x}{2}$]]']),
    ('Ⅲ　積和の公式（積を和・差に直す）', [
      r'加法定理　① $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$　② $\sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta$',
      r'　　　　　③ $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$　④ $\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$',
      r'【①＋②】左辺どうし，右辺どうしをたす。右辺の $\cos\alpha\sin\beta$ は打ち消し合って消える。',
      r'$\sin(\alpha+\beta)+\sin(\alpha-\beta)=$ [[$2\sin\alpha\cos\beta$]]',
      r'左辺と右辺を入れかえて，両辺を 2 でわると　$\sin\alpha\cos\beta=$ [[$\frac{1}{2}\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\}$]]　…❹',
      r'【③＋④】$\cos(\alpha+\beta)+\cos(\alpha-\beta)=$ [[$2\cos\alpha\cos\beta$]]　両辺を 2 でわると → ❺',
      r'【③－④】$\cos(\alpha+\beta)-\cos(\alpha-\beta)=$ [[$-2\sin\alpha\sin\beta$]]　両辺を [[$-2$]] でわると → ❻'])],
  groups=[]))

SHEETS.append(dict(no='④-3', title='三角関数の不定積分（次数を下げる）', boxes=[('三角関数の不定積分', [
    '次数が高く，置換・部分積分が使えない時は，④-2 の公式❶〜❸で次数を下げて積分する',
    r'❶ $\sin^2x=\frac{1-\cos2x}{2}$　❷ $\cos^2x=\frac{1+\cos2x}{2}$　❸ $\sin x\cos x=\frac{\sin2x}{2}$'])],
  groups=[('例', conv(A['④-3']['ex'], [r'\int\sin^2x\,dx', r'\int\sin x\cos x\,dx'])),
          ('問17（ノート）', conv(A['④-3']['q'][0], [r'\int\cos^2x\,dx', r'\int\sin^22x\,dx', r'\int(\sin x+\cos x)^2dx']))]))

SHEETS.append(dict(no='④-4', title='三角関数の不定積分（積を和に）', boxes=[('三角関数の不定積分', [
    '三角関数の積は，④-2 の積和の公式❹〜❻で和・差に直してから積分する',
    r'❹ $\sin\alpha\cos\beta=\frac{1}{2}\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\}$',
    r'❺ $\cos\alpha\cos\beta=\frac{1}{2}\{\cos(\alpha+\beta)+\cos(\alpha-\beta)\}$',
    r'❻ $\sin\alpha\sin\beta=-\frac{1}{2}\{\cos(\alpha+\beta)-\cos(\alpha-\beta)\}$'])],
  groups=[('例', conv(A['④-4']['ex'], [r'\int\sin3\theta\cos\theta\,d\theta'])),
          ('問18（ノート）', conv(A['④-4']['q'][0], [r'\int\sin2\theta\cos\theta\,d\theta', r'\int\cos2x\cos x\,dx', r'\int\sin4x\sin2x\,dx']))]))
