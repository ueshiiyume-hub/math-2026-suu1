"""積分法（プリント ①-1〜）の デッキ
DECKS['ファイル名'] = (題, JS)。JS では const DECK = {title, pages:[{name, html}]} を 作る
部品（M・D・S・FILL・CAP・HD・BOX・PT・CALC・PQ・gridPage・subPage・coverSlide）は parts.js
色：\\A{…}＝橙（変わる ところ）、\\B{…}＝紫（置きかえた t）、\\DP{…}＝深い青（答え）
"""
DECKS = {}

# ---------------------------------------------------------------- ①-1 xⁿ の不定積分
DECKS['1-1_xnの不定積分'] = ('①-1 xⁿ の不定積分', r'''
const NO = '①-1', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:`${M`x^n`} の不定積分`, sub:'指数を 1 増やして、その数で割る'});

/* 公式 */
const p1 = HD(NO, '公式', SEC) + `<div class="bd">
  <div class="l">${BOX('公式', `
    ${D`\int x^{\alpha}\,dx=`}${FILL(1, D`\frac{1}{\A{\alpha+1}}x^{\A{\alpha+1}}+C`, 7)}<br>
    <span data-s="2" style="font-size:24px">ただし　${M`\alpha\neq-1`}</span><br>
    ${D`\int \frac{1}{x}\,dx=`}${FILL(3, D`\log|x|+C`, 6)}`)}
    <div class="pbox" data-s="4"><div class="pl2">確かめ（微分すると 元に 戻る）</div>
      ${D`\left(\frac{1}{\alpha+1}x^{\alpha+1}\right)'=x^{\alpha}`}　　${D`(\log|x|)'=\frac{1}{x}`}</div>
  </div>
</div>` + CAP([
  `不定積分は「微分すると その式に なる 関数」を 探す 計算です。`,
  `${M`x^\alpha`} は、<b class="a">指数を 1 増やして</b>、<b class="a">増やした 指数で 割り</b> ます。`,
  `${M`\alpha=-1`} の ときは ${M`\alpha+1=0`} で 割れないので、この 公式は 使えません。`,
  `その ${M`\alpha=-1`}、つまり ${M`\frac{1}{x}=x^{-1}`} の 積分は ${M`\log|x|`} です。`,
  `微分して 元に 戻れば 正解です。${M`C`} は 積分定数です（答えには 必ず 付けます）。`
]);

/* 手順 と 例⑴⑵ */
const STEP = PT(null, '手順', `① ${M`x^{\alpha}`} の 形に 直す　② 指数を 1 増やし、その数で 割る　③ 分数・根号に 戻す`);
const p2 = gridPage({no:NO, sec:SEC, title:'例　⑴・⑵', q:STEP, items:[
  {tag:'⑴', q:String.raw`\int x^3\,dx`, lines:[[1, String.raw`=\frac{1}{\A{4}}x^{\A{4}}+C`]]},
  {tag:'⑵', q:String.raw`\int \frac{1}{x^3}\,dx`, lines:[[2, String.raw`=\int x^{-3}\,dx`], [3, String.raw`=\frac{1}{\A{-2}}x^{\A{-2}}+C`], [4, String.raw`=\DP{-\frac{1}{2x^2}+C}`]]},
], cm:[
  `手順は 3つ。まず ${M`x^{\alpha}`} の 形に 直すのが ポイントです。`,
  `⑴ 指数 ${M`3`} を 1 増やして ${M`4`}。${M`4`} で 割ります。`,
  `⑵ 分母の ${M`x^3`} は、${M`x^{-3}`} と 書けます。`,
  `指数 ${M`-3`} を 1 増やすと ${M`-2`}。${M`-2`} で 割ります。`,
  `${M`x^{-2}=\frac{1}{x^2}`} と 分数に 戻して 答えます。`
]});

/* 例⑶⑷⑸ */
const p3 = gridPage({no:NO, sec:SEC, title:'例　⑶・⑷・⑸', items:[
  {tag:'⑶', q:String.raw`\int \sqrt{x}\,dx`, lines:[[1, String.raw`=\int x^{\frac{1}{2}}\,dx=\frac{2}{3}x^{\A{\frac{3}{2}}}+C`], [2, String.raw`=\DP{\frac{2}{3}x\sqrt{x}+C}`]]},
  {tag:'⑷', q:String.raw`\int \frac{1}{x}\,dx`, lines:[[3, String.raw`=\DP{\log|x|+C}`]]},
  {tag:'⑸', q:String.raw`\int \frac{1}{\sqrt[3]{x^2}}\,dx`, lines:[[4, String.raw`=\int x^{-\frac{2}{3}}\,dx=3x^{\A{\frac{1}{3}}}+C`], [5, String.raw`=\DP{3\sqrt[3]{x}+C}`]]},
], cm:[
  `根号も 指数で 表せば、同じ 公式が 使えます。`,
  `⑶ ${M`\sqrt{x}=x^{\frac{1}{2}}`}。指数を 1 増やすと ${M`\frac{3}{2}`}。${M`\frac{3}{2}`} で 割る ことは ${M`\frac{2}{3}`} を 掛ける ことです。`,
  `${M`x^{\frac{3}{2}}=x^{1}\cdot x^{\frac{1}{2}}=x\sqrt{x}`} と 根号に 戻します。`,
  `⑷ ${M`\frac{1}{x}=x^{-1}`} は 公式が 使えない 形。${M`\log|x|`} に なります。`,
  `⑸ ${M`\sqrt[3]{x^2}=x^{\frac{2}{3}}`} なので、${M`\frac{1}{\sqrt[3]{x^2}}=x^{-\frac{2}{3}}`}。指数を 1 増やすと ${M`\frac{1}{3}`}、${M`\frac{1}{3}`} で 割ると ${M`\times3`}。`,
  `${M`x^{\frac{1}{3}}=\sqrt[3]{x}`} と 根号に 戻します。`
]});

/* 問1 */
const p4 = gridPage({no:NO, sec:SEC, title:'問1', q:'次の 不定積分を 求めよ。', items:[
  {tag:'⑴', q:String.raw`\int x^5\,dx`, o:1, lines:[[1, String.raw`=\DP{\frac{1}{6}x^6+C}`]]},
  {tag:'⑵', q:String.raw`\int \frac{dx}{x^4}`, o:2, lines:[[2, String.raw`=\int x^{-4}\,dx=-\frac{1}{3}x^{-3}+C`], [3, String.raw`=\DP{-\frac{1}{3x^3}+C}`]]},
  {tag:'⑶', q:String.raw`\int \sqrt[3]{x}\,dx`, o:4, lines:[[4, String.raw`=\int x^{\frac{1}{3}}\,dx=\frac{3}{4}x^{\frac{4}{3}}+C`], [5, String.raw`=\DP{\frac{3}{4}x\sqrt[3]{x}+C}`]]},
  {tag:'⑷', q:String.raw`\int \frac{dx}{\sqrt{x}}`, o:6, lines:[[6, String.raw`=\int x^{-\frac{1}{2}}\,dx=2x^{\frac{1}{2}}+C`], [7, String.raw`=\DP{2\sqrt{x}+C}`]]},
], cm:[
  `${M`\frac{dx}{x^4}`} は ${M`\frac{1}{x^4}\,dx`} の ことです。どれも ${M`x^{\alpha}`} の 形に 直してから 積分します。`,
  `⑴ 指数を 1 増やして ${M`6`}、${M`6`} で 割ります。`,
  `⑵ ${M`\frac{1}{x^4}=x^{-4}`}。指数は ${M`-3`} に なり、${M`-3`} で 割ります。`,
  `分数に 戻して 答えます。`,
  `⑶ ${M`\sqrt[3]{x}=x^{\frac{1}{3}}`}。指数は ${M`\frac{4}{3}`}、${M`\frac{4}{3}`} で 割る ＝ ${M`\frac{3}{4}`} を 掛ける。`,
  `${M`x^{\frac{4}{3}}=x\cdot x^{\frac{1}{3}}=x\sqrt[3]{x}`}。`,
  `⑷ ${M`\frac{1}{\sqrt{x}}=x^{-\frac{1}{2}}`}。指数は ${M`\frac{1}{2}`}、${M`\frac{1}{2}`} で 割る ＝ ${M`2`} を 掛ける。`,
  `${M`x^{\frac{1}{2}}=\sqrt{x}`} と 戻します。`
]});

/* まとめ（アニメーション なし） */
const p5 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('公式', `${D`\int x^{\alpha}\,dx=\frac{1}{\alpha+1}x^{\alpha+1}+C`}（${M`\alpha\neq-1`}）　　${D`\int \frac{1}{x}\,dx=\log|x|+C`}`)}
  <div class="sum">
    <span>${M`\frac{1}{x^n}`}</span><span class="ar">→</span><span>${M`x^{-n}`}</span>
    <span>${M`\sqrt[n]{x^m}`}</span><span class="ar">→</span><span>${M`x^{\frac{m}{n}}`}</span>
  </div>
</div>` + CAP([`まず ${M`x^{\alpha}`} の 形に 直す。①-2 では、分数の 式を 項に 分けて から 積分します。`]);

const DECK = {title:'①-1 xⁿ の不定積分', pages:[
  {name:'表紙', html:p0}, {name:'公式', html:p1}, {name:'例　⑴・⑵', html:p2},
  {name:'例　⑶・⑷・⑸', html:p3}, {name:'問1', html:p4}, {name:'まとめ', html:p5},
]};
''')

# ---------------------------------------------------------------- ①-2 分子が多項式の場合
DECKS['1-2_分子が多項式の場合'] = ('①-2 分子が多項式の場合', r'''
const NO = '①-2', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:`${M`x^n`} の不定積分`, sub:'分子が 多項式の 場合'});

/* 方針 と 例 */
const p1 = HD(NO, '方針', SEC) + `<div class="bd col" style="gap:30px">
  <div class="big" style="font-size:38px">${D`\int\frac{2x-3}{x^2}\,dx`}</div>
  ${BOX('分子が 多項式である 場合の 不定積分の 方針', `${FILL(1, '分子の 各項を 分母で 割ってから、項ごとに 積分する。', 22)}`)}
  <div class="big" data-s="2" style="font-size:36px">${D`\frac{\A{2x}-\A{3}}{x^2}=\frac{\A{2x}}{x^2}-\frac{\A{3}}{x^2}=\frac{2}{x}-3x^{-2}`}</div>
</div>` + CAP([
  `${M`\int\frac{2x-3}{x^2}\,dx`} のような 分数の 式は、そのままでは 積分できません。`,
  `分子の 項を 1つずつ 分母で 割って、${M`x^{\alpha}`} の 項の 和に します。`,
  `こう 分ければ、①-1 の 公式が 使えます。`
]);

const p2 = gridPage({no:NO, sec:SEC, title:'例', q:'次の 不定積分を 求めよ。', c1:true, items:[
  {tag:'⑴', q:String.raw`\int \frac{2x-3}{x^2}\,dx`, lines:[
    [1, String.raw`=\int\left(\frac{\A{2}}{x}-\A{3}x^{-2}\right)dx`],
    [2, String.raw`=\A{2}\log|x|-\A{3}\cdot\frac{1}{-1}x^{-1}+C`],
    [3, String.raw`=\DP{2\log|x|+\frac{3}{x}+C}`]]},
], cm:[
  `分子の 各項を 分母 ${M`x^2`} で 割ります。`,
  `${M`\frac{2x}{x^2}=\frac{2}{x}`}、${M`\frac{3}{x^2}=3x^{-2}`}。`,
  `${M`\frac{1}{x}`} は ${M`\log|x|`}、${M`x^{-2}`} は 指数を 1 増やして ${M`-1`} で 割ります。係数は そのまま 前に 残します。`,
  `${M`-3\cdot(-1)x^{-1}=\frac{3}{x}`}。符号に 気を つけましょう。`
]});

/* 問2 */
const p3 = gridPage({no:NO, sec:SEC, title:'問2　⑴・⑵', q:'次の 不定積分を 求めよ。', c1:true, items:[
  {tag:'⑴', q:String.raw`\int\left(x^3+\frac{1}{x^3}\right)dx`, o:1, lines:[
    [1, String.raw`=\int\left(x^3+x^{-3}\right)dx=\frac{1}{4}x^4-\frac{1}{2}x^{-2}+C`],
    [2, String.raw`=\DP{\frac{1}{4}x^4-\frac{1}{2x^2}+C}`]]},
  {tag:'⑵', q:String.raw`\int\frac{2x^3+2x-4}{x^2}\,dx`, o:3, lines:[
    [3, String.raw`=\int\left(2x+\frac{2}{x}-\frac{4}{x^2}\right)dx`],
    [4, String.raw`=\DP{x^2+2\log|x|+\frac{4}{x}+C}`]]},
], cm:[
  `どちらも、まず ${M`x^{\alpha}`} の 項の 和に します。`,
  `⑴ ${M`\frac{1}{x^3}=x^{-3}`}。指数を 1 増やして ${M`-2`} で 割ります。`,
  `${M`x^{-2}`} を 分数に 戻して 答えます。`,
  `⑵ 分子の 3つの 項を、それぞれ ${M`x^2`} で 割ります。`,
  `${M`2x\to x^2`}、${M`\frac{2}{x}\to2\log|x|`}、${M`-4x^{-2}\to-4\cdot\frac{1}{-1}x^{-1}=\frac{4}{x}`}。符号は 次の ページで くわしく。`
]});
/* 問2⑵ の くわしく：−4/x² の 項（板書と 同じ 流れ） */
const p3b = HD(NO, '問2　⑵　くわしく', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="q qline">${D`-\frac{4}{x^2}`} の 項だけ 取り出して 積分する</div>
    <div class="calc" style="font-size:32px;gap:14px">
      <div>${D`-\int4x^{\A{-2}}\,dx`}</div>
      <div data-s="2">${D`=\frac{\on{4}{a}{-4}}{\on{2}{a}{-1}}x^{\on{2}{a}{-1}}+C`}</div>
      <div data-s="4">${D`=\on{4}{a}{+}4x^{-1}+C`}</div>
      <div data-s="5">${D`=\DP{+\frac{4}{x}+C}`}</div>
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:16px;align-items:stretch;width:420px">
    ${PT(1, '① 指数を 1 増やす', `${M`-2+1=\A{-1}`}`)}
    ${PT(2, '② 増やした 指数で 割る', `${M`-1`} で 割る → 分母に ${M`-1`}`)}
    ${PT(3, '③ 符号', `${M`\frac{-4}{-1}=+4`}（マイナス ÷ マイナス ＝ プラス）`)}
    ${PT(5, '④ 分数に 戻す', `${M`x^{-1}=\frac{1}{x}`}`)}
  </div>
</div>` + CAP([
  `問2⑵ の ${M`-\frac{4}{x^2}`} の 項は、まず ${M`-4x^{-2}`} と 指数で 表します。`,
  `①-1 の 公式どおり、指数 ${M`-2`} を 1 増やすと ${M`-1`}。`,
  `増やした 指数 ${M`-1`} で 割ります。前の ${M`-4`} は 分子に そのまま 残ります。`,
  `${M`\frac{-4}{-1}`}：マイナス どうしの 割り算なので <b class="a">プラス</b> に なります。`,
  `${M`+4x^{-1}`}。ここで 符号を まちがえやすいので 注意します。`,
  `${M`x^{-1}=\frac{1}{x}`} と 分数に 戻して ${M`+\frac{4}{x}`}。これが 答えの 最後の 項です。`
]);

const p4 = gridPage({no:NO, sec:SEC, title:'問2　⑶・⑷', c1:true, items:[
  {tag:'⑶', q:String.raw`\int\frac{3x-2}{\sqrt{x}}\,dx`, o:1, lines:[
    [1, String.raw`=\int\left(3x^{\frac{1}{2}}-2x^{-\frac{1}{2}}\right)dx=2x^{\frac{3}{2}}-4x^{\frac{1}{2}}+C`],
    [2, String.raw`=\DP{2x\sqrt{x}-4\sqrt{x}+C}`]]},
  {tag:'⑷', q:String.raw`\int\frac{\left(\sqrt{x}+2\right)^2}{x}\,dx`, o:3, lines:[
    [3, String.raw`=\int\frac{x+4\sqrt{x}+4}{x}\,dx=\int\left(1+\frac{4}{\sqrt{x}}+\frac{4}{x}\right)dx`],
    [4, String.raw`=\DP{x+8\sqrt{x}+4\log x+C}`]]},
], cm:[
  `根号が 分母に ある ときも、指数で 表せば 同じです。`,
  `⑶ ${M`\frac{3x}{\sqrt{x}}=3x^{\frac{1}{2}}`}、${M`\frac{2}{\sqrt{x}}=2x^{-\frac{1}{2}}`}。${M`3\cdot\frac{2}{3}=2`}、${M`2\cdot2=4`}。指数への 直し方は 次の ページで くわしく。`,
  `${M`x^{\frac{3}{2}}=x\sqrt{x}`}、${M`x^{\frac{1}{2}}=\sqrt{x}`} と 戻します。`,
  `⑷ まず 分子を 展開。${M`(\sqrt{x}+2)^2=x+4\sqrt{x}+4`} を ${M`x`} で 割ります。`,
  `${M`\frac{4}{\sqrt{x}}=4x^{-\frac{1}{2}}\to8\sqrt{x}`}。${M`\sqrt{x}`} が あるので ${M`x>0`}。だから ${M`\log|x|`} は ${M`\log x`} と 書けます。`
]});

/* 問2⑶ の くわしく：x/√x を 指数に 直す（板書と 同じ 流れ） */
const p4b = HD(NO, '問2　⑶　くわしく', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="calc" style="font-size:32px;gap:14px">
      <div>${D`\int\frac{3x-2}{\sqrt{x}}\,dx`}</div>
      <div data-s="1">${D`=\int\left(\frac{3\on{3}{a}{x}}{\on{3}{a}{\sqrt{x}}}-\frac{2}{\on{4}{a}{\sqrt{x}}}\right)dx`}</div>
      <div data-s="5">${D`=\DP{\int\left(3x^{\frac{1}{2}}-2x^{-\frac{1}{2}}\right)dx}`}</div>
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:14px;align-items:stretch;width:440px">
    ${PT(2, 'わり算は 指数の ひき算', `${D`\frac{x^3}{x^2}=x^{3-2}=x^{\A{1}}`}`)}
    ${PT(3, '同じように', `${D`\frac{x}{\sqrt{x}}=\frac{x^{1}}{x^{\frac{1}{2}}}=x^{1-\frac{1}{2}}=x^{\A{\frac{1}{2}}}`}`)}
    ${PT(4, '分母の √x', `${D`\frac{2}{\sqrt{x}}=\frac{2}{x^{\frac{1}{2}}}=2x^{\A{-\frac{1}{2}}}`}`)}
  </div>
</div>` + CAP([
  `問2⑶ を、指数の 形に 直す ところまで くわしく 見ます。`,
  `まず 分子の 各項を 分母 ${M`\sqrt{x}`} で 割り、2つの 分数に 分けます。`,
  `わり算は 指数の ひき算です。たとえば ${M`\frac{x^3}{x^2}=x^{3-2}=x^1`}。`,
  `${M`\sqrt{x}=x^{\frac{1}{2}}`} なので、${M`\frac{x}{\sqrt{x}}=x^{1-\frac{1}{2}}=x^{\frac{1}{2}}`}。`,
  `分母に ある ${M`\sqrt{x}`} は、上に 上げると 指数が マイナス：${M`\frac{1}{\sqrt{x}}=x^{-\frac{1}{2}}`}。`,
  `これで ${M`x^{\alpha}`} の 形に なりました。あとは ①-1 の 公式で 積分します（次の ページ）。`
]);

/* 問2⑶ の くわしく（2）：指数を 1 増やして、分数で 割る */
const p4c = HD(NO, '問2　⑶　くわしく（積分する）', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="calc" style="font-size:32px;gap:14px">
      <div>${D`\int\left(3x^{\frac{1}{2}}-2x^{-\frac{1}{2}}\right)dx`}</div>
      <div data-s="2">${D`=\frac{3}{\on{2}{a}{\frac{3}{2}}}x^{\on{1}{a}{\frac{3}{2}}}-\frac{2}{\on{2}{a}{\frac{1}{2}}}x^{\on{1}{a}{\frac{1}{2}}}+C`}</div>
      <div data-s="4">${D`=\on{3}{dp}{2}x^{\frac{3}{2}}-\on{4}{dp}{4}x^{\frac{1}{2}}+C`}</div>
      <div data-s="5">${D`=\DP{2x\sqrt{x}-4\sqrt{x}+C}`}</div>
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:14px;align-items:stretch;width:440px">
    ${PT(1, '① 指数を 1 増やす', `${D`\frac{1}{2}+1=\A{\frac{3}{2}}`}　${D`-\frac{1}{2}+1=\A{\frac{1}{2}}`}`)}
    ${PT(3, '② 分数で 割る ＝ 逆数を 掛ける', `${D`3\div\frac{3}{2}=3\times\frac{2}{3}=2`}<div data-s="4">${D`2\div\frac{1}{2}=2\times2=4`}</div>`)}
    ${PT(5, '③ 根号に 戻す', `${D`x^{\frac{3}{2}}=x\sqrt{x}`}　${D`x^{\frac{1}{2}}=\sqrt{x}`}`)}
  </div>
</div>` + CAP([
  `指数の 形に できたので、①-1 の 公式で 積分します。`,
  `① それぞれ 指数を 1 増やします。${M`\frac{1}{2}\to\frac{3}{2}`}、${M`-\frac{1}{2}\to\frac{1}{2}`}。`,
  `② 増やした 指数で 割ります。係数 ${M`3`}・${M`2`} の 下に ${M`\frac{3}{2}`}・${M`\frac{1}{2}`} が きます。`,
  `分数で 割る ことは、逆数を 掛ける こと。${M`3\div\frac{3}{2}=3\times\frac{2}{3}=2`}。`,
  `${M`2\div\frac{1}{2}=2\times2=4`}。`,
  `③ ${M`x^{\frac{3}{2}}=x^{1}\cdot x^{\frac{1}{2}}=x\sqrt{x}`}、${M`x^{\frac{1}{2}}=\sqrt{x}`} と 根号に 戻して 答えます。`
]);

/* 問2⑷ の くわしく（板書と 同じ 流れ）：① 展開して x^α に、② 積分して x>0 で log を 直す */
const p4d = HD(NO, '問2　⑷　くわしく', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="calc" style="font-size:30px;gap:12px">
      <div>${D`\int\frac{(\sqrt{x}+2)^2}{x}\,dx`}　<span class="pbox" style="display:inline-block;padding:2px 12px;font-size:24px" data-s="1">${M`x>0`}</span></div>
      <div data-s="2">${D`=\int\frac{x+4\sqrt{x}+4}{x}\,dx`}</div>
      <div data-s="3">${D`=\int\left(\frac{x}{x}+\frac{4\sqrt{x}}{x}+\frac{4}{x}\right)dx`}</div>
      <div data-s="5">${D`=\DP{\int\left(1+4x^{-\frac{1}{2}}+\frac{4}{x}\right)dx}`}</div>
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:14px;align-items:stretch;width:440px">
    ${PT(1, 'x の 範囲', `${M`\sqrt{x}`} が あり、分母が ${M`x`} → ${M`x>0`}`)}
    ${PT(2, '展開', `${D`(\sqrt{x}+2)^2=x+4\sqrt{x}+4`}`)}
    ${PT(4, 'わり算は 指数の ひき算', `${D`\frac{x}{x}=1`}<div>${D`\frac{\sqrt{x}}{x}=\frac{x^{\frac{1}{2}}}{x^{1}}=x^{\frac{1}{2}-1}=x^{\A{-\frac{1}{2}}}`}</div>`)}
  </div>
</div>` + CAP([
  `問2⑷ を、${M`x^{\alpha}`} の 形に 直す ところまで くわしく 見ます。`,
  `まず 注目。${M`\sqrt{x}`} が あり、分母が ${M`x`} なので ${M`x>0`} です（後で 使います）。`,
  `分子を 展開します。${M`(\sqrt{x})^2=x`}、${M`2\cdot\sqrt{x}\cdot2=4\sqrt{x}`}。`,
  `分子の 各項を ${M`x`} で 割り、3つの 分数に 分けます。`,
  `${M`\frac{x}{x}=1`}。${M`\frac{\sqrt{x}}{x}`} は 指数の ひき算で ${M`x^{\frac{1}{2}-1}=x^{-\frac{1}{2}}`}。`,
  `${M`\frac{4}{x}`} は そのまま（${M`\log`} に なる 形）。次の ページで 積分します。`
]);
const p4e = HD(NO, '問2　⑷　くわしく（積分する）', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="calc" style="font-size:31px;gap:14px">
      <div>${D`\int\left(1+4x^{-\frac{1}{2}}+\frac{4}{x}\right)dx`}</div>
      <div data-s="1">${D`=x+\frac{4}{\on{2}{a}{\frac{1}{2}}}x^{\on{1}{a}{\frac{1}{2}}}+4\on{3}{a}{\log|x|}+C`}</div>
      <div data-s="4">${D`=\DP{x+8\sqrt{x}+4\log x+C}`}</div>
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:14px;align-items:stretch;width:440px">
    ${PT(1, '① 指数を 1 増やす', `${D`-\frac{1}{2}+1=\A{\frac{1}{2}}`}`)}
    ${PT(2, '② 分数で 割る ＝ 逆数を 掛ける', `${D`4\div\frac{1}{2}=4\times2=8`}`)}
    ${PT(3, '③ x>0 より', `${D`\log|x|=\log x`}（絶対値は いらない）`)}
  </div>
</div>` + CAP([
  `${M`1`}、${M`4x^{-\frac{1}{2}}`}、${M`\frac{4}{x}`} を 1つずつ 積分します。`,
  `${M`1\to x`}。${M`x^{-\frac{1}{2}}`} は 指数を 1 増やして ${M`\frac{1}{2}`}。`,
  `増やした 指数 ${M`\frac{1}{2}`} で 割る ＝ ${M`2`} を 掛ける。${M`4\div\frac{1}{2}=8`}。`,
  `${M`\frac{4}{x}\to4\log|x|`}。でも はじめに 確かめた とおり ${M`x>0`} なので、${M`|\ \ |`} は はずせます。`,
  `${M`x^{\frac{1}{2}}=\sqrt{x}`} と 根号に 戻して 答えます。`
]);

const p5 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:28px">
  ${BOX('方針', `<span style="font-size:30px">分子の 各項を 分母で 割ってから、項ごとに 積分する。</span>`)}
  <div class="big" style="font-size:34px">${D`\frac{2x-3}{x^2}=\frac{2}{x}-3x^{-2}`}　→　${D`\frac{1}{x}`} は ${D`\log|x|`}</div>
</div>` + CAP([`①-3 では、三角関数の 不定積分を 学びます。`]);

const DECK = {title:'①-2 分子が多項式の場合', pages:[
  {name:'表紙', html:p0}, {name:'方針', html:p1}, {name:'例', html:p2},
  {name:'問2　⑴・⑵', html:p3}, {name:'問2　⑵　くわしく', html:p3b, add:'10/26'}, {name:'問2　⑶・⑷', html:p4}, {name:'問2　⑶　くわしく', html:p4b, add:'10/26'}, {name:'問2　⑶　くわしく（積分する）', html:p4c, add:'10/26'}, {name:'問2　⑷　くわしく', html:p4d, add:'10/26'}, {name:'問2　⑷　くわしく（積分する）', html:p4e, add:'10/26'}, {name:'まとめ', html:p5},
]};
''')

# ---------------------------------------------------------------- ①-3 三角関数の不定積分
DECKS['1-3_三角関数の不定積分'] = ('①-3 三角関数の不定積分', r'''
const NO = '①-3', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'三角関数の不定積分', sub:'微分の 公式を 逆に 読む'});

const p1 = HD(NO, '公式', SEC) + `<div class="bd col" style="gap:24px">
  ${BOX('公式', `<div style="display:flex;gap:44px;flex-wrap:wrap">
    <span>${D`\int\sin x\,dx=`}${FILL(1, D`-\cos x+C`, 5.5)}</span>
    <span>${D`\int\cos x\,dx=`}${FILL(2, D`\sin x+C`, 5.5)}</span>
    <span>${D`\int\frac{dx}{\cos^2x}=`}${FILL(3, D`\tan x+C`, 5.5)}</span></div>`)}
  <div class="pbox" data-s="1"><div class="pl2">確かめ（微分の 公式）</div>
    <span data-s="1">${D`(\cos x)'=-\sin x`}</span>　　<span data-s="2">${D`(\sin x)'=\cos x`}</span>　　<span data-s="3">${D`(\tan x)'=\frac{1}{\cos^2x}`}</span></div>
</div>` + CAP([
  `微分の 公式を 逆に 読めば、積分の 公式に なります。`,
  `${M`\cos x`} を 微分すると ${M`-\sin x`}。だから ${M`\sin x`} の 積分は <b class="a">${M`-\cos x`}</b>。マイナスに 注意です。`,
  `${M`\sin x`} を 微分すると ${M`\cos x`}。だから ${M`\cos x`} の 積分は ${M`\sin x`}。`,
  `${M`\tan x`} を 微分すると ${M`\frac{1}{\cos^2x}`}。だから その 積分は ${M`\tan x`}。`
]);

const p2 = gridPage({no:NO, sec:SEC, title:'例', q:'次の 不定積分を 求めよ。', items:[
  {tag:'⑴', q:String.raw`\int\left(\sin x+3\cos x\right)dx`, lines:[[1, String.raw`=\DP{-\cos x+3\sin x+C}`]]},
  {tag:'⑵', q:String.raw`\int\tan^2x\,dx`, lines:[[3, String.raw`=\int\left(\frac{1}{\cos^2x}-1\right)dx`], [4, String.raw`=\DP{\tan x-x+C}`]]},
], side:PT(2, 'ヒント', `${D`1+\tan^2x=\frac{1}{\cos^2x}`}　より　${D`\tan^2x=\frac{1}{\cos^2x}-1`}`), cm:[
  `公式を そのまま 使います。`,
  `⑴ ${M`\sin x\to-\cos x`}、${M`3\cos x\to3\sin x`}。`,
  `⑵ ${M`\tan^2x`} の 公式は ありません。数学Ⅱ の 式 ${M`1+\tan^2x=\frac{1}{\cos^2x}`} で 書きかえます。`,
  `${M`\tan^2x=\frac{1}{\cos^2x}-1`}。これなら 公式が 使えます。`,
  `${M`\frac{1}{\cos^2x}\to\tan x`}、${M`1\to x`}。`
]});

const p3 = gridPage({no:NO, sec:SEC, title:'問3', q:'次の 不定積分を 求めよ。', items:[
  {tag:'⑴', q:String.raw`\int\left(1-\sin x\right)dx`, o:1, lines:[[1, String.raw`=\DP{x+\cos x+C}`]]},
  {tag:'⑵', q:String.raw`\int\frac{\cos^3x-1}{\cos^2x}\,dx`, o:2, lines:[[2, String.raw`=\int\left(\cos x-\frac{1}{\cos^2x}\right)dx`], [3, String.raw`=\DP{\sin x-\tan x+C}`]]},
  {tag:'⑶', q:String.raw`\int\left(2-\tan x\right)\cos x\,dx`, o:4, lines:[[4, String.raw`=\int\left(2\cos x-\sin x\right)dx`], [5, String.raw`=\DP{2\sin x+\cos x+C}`]]},
  {tag:'⑷', q:String.raw`\int\left(\tan^2x-\frac{2}{\cos^2x}\right)dx`, o:6, lines:[[6, String.raw`=\int\left(-\frac{1}{\cos^2x}-1\right)dx`], [7, String.raw`=\DP{-\tan x-x+C}`]]},
], cm:[
  `公式が 使える 形 ${M`\sin x`}、${M`\cos x`}、${M`\frac{1}{\cos^2x}`} に 直してから 積分します。`,
  `⑴ ${M`-\sin x`} の 積分は ${M`-(-\cos x)=\cos x`}。`,
  `⑵ 分子の 各項を ${M`\cos^2x`} で 割ります（①-2 と 同じ）。`,
  `${M`\cos x\to\sin x`}、${M`\frac{1}{\cos^2x}\to\tan x`}。`,
  `⑶ 展開すると ${M`\tan x\cos x=\frac{\sin x}{\cos x}\cdot\cos x=\sin x`}。（次の ページで くわしく）`,
  `${M`2\cos x\to2\sin x`}、${M`-\sin x\to\cos x`}。`,
  `⑷ ${M`\tan^2x=\frac{1}{\cos^2x}-1`} を 使うと、${M`\frac{1}{\cos^2x}-1-\frac{2}{\cos^2x}=-\frac{1}{\cos^2x}-1`}。（⑶・⑷ は 次の ページから くわしく）`,
  `${M`-\frac{1}{\cos^2x}\to-\tan x`}、${M`-1\to-x`}。`
]});

/* 問3⑶ の くわしく（板書と 同じ 流れ） */
const p3b = HD(NO, '問3　⑶　くわしく', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="calc" style="font-size:32px;gap:16px">
      <div>${D`\int(2-\tan x)\cos x\,dx`}</div>
      <div data-s="1">${D`=\int(2\cos x-\on{2}{a}{\tan x\cos x})\,dx`}</div>
      <div data-s="3">${D`=\int(2\cos x-\on{3}{a}{\sin x})\,dx`}</div>
      <div data-s="4">${D`=\DP{2\sin x+\cos x+C}`}</div>
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:14px;align-items:stretch;width:440px">
    ${PT(1, '① かっこを はずす', `${D`(2-\tan x)\cos x`}<div>${D`=2\cos x-\tan x\cos x`}</div>`)}
    ${PT(2, '② tan x を sin x／cos x に', `${D`\tan x\cos x=\frac{\sin x}{\cos x}\times\cos x`}<div>${D`=\A{\sin x}`}</div>`)}
    ${PT(4, '③ 積分（符号に 注意）', `${M`\int2\cos x\,dx=2\sin x`}<div>${M`\int(-\sin x)\,dx=+\cos x`}</div>`)}
  </div>
</div>` + CAP([
  `問3⑶ を くわしく 見ます。${M`\tan x\cos x`} の まま では 積分できません。`,
  `① かっこを はずします。${M`\cos x`} を それぞれに 掛けます。`,
  `② ${M`\tan x=\frac{\sin x}{\cos x}`} です。${M`\cos x`} を 掛けると 分母の ${M`\cos x`} と 約分されます。`,
  `${M`\tan x\cos x=\sin x`}。これで 公式が 使える 形に なりました。`,
  `③ ${M`2\cos x\to2\sin x`}。${M`\sin x`} の 積分は ${M`-\cos x`} なので、${M`-\sin x`} の 積分は ${M`+\cos x`}。`
]);

/* 問3⑷ の くわしく（板書と 同じ 流れ） */
const p3c = HD(NO, '問3　⑷　くわしく', SEC) + `<div class="bd">
  <div class="l" style="gap:14px">
    <div class="calc" style="font-size:32px;gap:16px">
      <div>${D`\int\left(\on{1}{a}{\tan^2x}-\frac{2}{\cos^2x}\right)dx`}</div>
      <div data-s="2">${D`=\int\left(\on{2}{a}{\frac{1}{\cos^2x}-1}-\frac{2}{\cos^2x}\right)dx`}</div>
      <div data-s="3">${D`=\int\left(\on{3}{a}{-\frac{1}{\cos^2x}}-1\right)dx`}</div>
      <div data-s="4">${D`=\DP{-\tan x-x+C}`}</div>
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:14px;align-items:stretch;width:440px">
    ${PT(1, '① tan²x の 直し方', `${D`1+\tan^2x=\frac{1}{\cos^2x}`}<div>${D`\tan^2x=\A{\frac{1}{\cos^2x}-1}`}</div>`)}
    ${PT(3, '② 1/cos²x を まとめる', `${D`\frac{1}{\cos^2x}-\frac{2}{\cos^2x}=\A{-\frac{1}{\cos^2x}}`}`)}
    ${PT(4, '③ 積分', `${M`\int\frac{dx}{\cos^2x}=\tan x`}　${M`\int1\,dx=x`}`)}
  </div>
</div>` + CAP([
  `問3⑷ を くわしく 見ます。${M`\tan^2x`} の 積分の 公式は ありません。`,
  `① 数学Ⅱ の 式 ${M`1+\tan^2x=\frac{1}{\cos^2x}`} から、${M`\tan^2x=\frac{1}{\cos^2x}-1`}（例⑵ と 同じ）。`,
  `${M`\tan^2x`} を 置きかえます。`,
  `② ${M`\frac{1}{\cos^2x}`} どうしを まとめます。${M`1-2=-1`} なので ${M`-\frac{1}{\cos^2x}`}。`,
  `③ ${M`-\frac{1}{\cos^2x}\to-\tan x`}、${M`-1\to-x`}。`
]);

const p4 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('公式', `${D`\int\sin x\,dx=-\cos x+C`}　　${D`\int\cos x\,dx=\sin x+C`}　　${D`\int\frac{dx}{\cos^2x}=\tan x+C`}`)}
  <div class="q" style="font-size:28px">${M`\tan^2x`} は ${D`\frac{1}{\cos^2x}-1`} に 直してから 積分する</div>
</div>` + CAP([`①-4 では、指数関数の 不定積分を 学びます。`]);

const DECK = {title:'①-3 三角関数の不定積分', pages:[
  {name:'表紙', html:p0}, {name:'公式', html:p1}, {name:'例', html:p2}, {name:'問3', html:p3}, {name:'問3　⑶　くわしく', html:p3b, add:'10/26'}, {name:'問3　⑷　くわしく', html:p3c, add:'10/26'}, {name:'まとめ', html:p4},
]};
''')

# ---------------------------------------------------------------- ①-4 指数関数の不定積分
DECKS['1-4_指数関数の不定積分'] = ('①-4 指数関数の不定積分', r'''
const NO = '①-4', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'指数関数の不定積分', sub:`${M`e^x`} は そのまま、${M`a^x`} は ${M`\log a`} で 割る`});

const p1 = HD(NO, '公式', SEC) + `<div class="bd col" style="gap:24px">
  ${BOX('公式', `<div style="display:flex;gap:60px;flex-wrap:wrap">
    <span>${D`\int e^x\,dx=`}${FILL(1, D`e^x+C`, 5)}</span>
    <span>${D`\int a^x\,dx=`}${FILL(2, D`\frac{a^x}{\A{\log a}}+C`, 5.5)}</span></div>`)}
  <div class="pbox" data-s="1"><div class="pl2">確かめ（微分の 公式）</div>
    <span data-s="1">${D`(e^x)'=e^x`}</span>　　<span data-s="2">${D`(a^x)'=a^x\A{\log a}`}</span></div>
</div>` + CAP([
  `指数関数も、微分の 公式を 逆に 読みます。`,
  `${M`e^x`} は 微分しても ${M`e^x`}。だから 積分しても ${M`e^x`} です。`,
  `${M`a^x`} を 微分すると ${M`\log a`} が 掛かります。積分では 逆に <b class="a">${M`\log a`} で 割り</b> ます。`
]);

const p2 = gridPage({no:NO, sec:SEC, title:'例', q:'次の 不定積分を 求めよ。', items:[
  {tag:'⑴', q:String.raw`\int\left(2e^x+1\right)dx`, lines:[[1, String.raw`=\DP{2e^x+x+C}`]]},
  {tag:'⑵', q:String.raw`\int3^x\,dx`, lines:[[2, String.raw`=\DP{\frac{3^x}{\log3}+C}`]]},
], cm:[
  `公式を そのまま 使います。`,
  `⑴ ${M`2e^x\to2e^x`}、${M`1\to x`}。`,
  `⑵ ${M`a=3`}。${M`\log3`} で 割ります。`
]});

const p3 = gridPage({no:NO, sec:SEC, title:'問4', q:'次の 不定積分を 求めよ。', items:[
  {tag:'⑴', q:String.raw`\int4e^x\,dx`, o:1, lines:[[1, String.raw`=\DP{4e^x+C}`]]},
  {tag:'⑵', q:String.raw`\int5^x\,dx`, o:2, lines:[[2, String.raw`=\DP{\frac{5^x}{\log5}+C}`]]},
  {tag:'⑶', q:String.raw`\int\left(3x^2-2e^x\right)dx`, o:3, lines:[[3, String.raw`=\DP{x^3-2e^x+C}`]]},
], cm:[
  `${M`e^x`} は そのまま、${M`a^x`} は ${M`\log a`} で 割ります。`,
  `⑴ 係数 ${M`4`} は そのまま 残します。`,
  `⑵ ${M`a=5`}。${M`\log5`} で 割ります。`,
  `⑶ ${M`3x^2\to3\cdot\frac{1}{3}x^3=x^3`}、${M`-2e^x\to-2e^x`}。`
]});

const p4 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('公式', `${D`\int e^x\,dx=e^x+C`}　　　${D`\int a^x\,dx=\frac{a^x}{\log a}+C`}`)}
</div>` + CAP([`①-5 では、${M`(2x+3)^4`} のような 合成関数の 不定積分を 学びます。`]);

const DECK = {title:'①-4 指数関数の不定積分', pages:[
  {name:'表紙', html:p0}, {name:'公式', html:p1}, {name:'例', html:p2}, {name:'問4', html:p3}, {name:'まとめ', html:p4},
]};
''')

# ---------------------------------------------------------------- ①-5 合成関数の不定積分（帳尻合わせ）
DECKS['1-5_合成関数の不定積分'] = ('①-5 合成関数の不定積分', r'''
const NO = '①-5', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'合成関数の不定積分', sub:'当たりを つけて、帳尻を 合わせる'});

/* 帳尻合わせ の 1ページ：o = {title, tag, q, guess, diff, fix, lines, cm} */
function adjPage(o){
  return HD(NO, o.title, SEC) + `<div class="bd col st" style="gap:16px">
    ${o.top||''}${PQ(o.tag, o.q)}
    <div class="two aj">
      <div class="adj">
        <div data-s="1"><span class="k">当たり</span>${D(o.guess)}</div>
        <div data-s="2"><span class="k">微分すると</span>${D(o.diff)}</div>
        <div data-s="3"><span class="k">帳尻</span>${o.fix}</div>
      </div>
      ${CALC(o.lines, 'main')}
    </div>
  </div>` + CAP(o.cm);
}

const p1 = adjPage({title:'例　⑴', tag:'⑴', q:String.raw`\int(2x+3)^4\,dx`,
  top:`<div class="q qline">次の 不定積分を 求めよ。</div>`,
  guess:String.raw`\frac{1}{5}(2x+3)^5`, diff:String.raw`\frac{1}{5}\cdot5(2x+3)^4\cdot\A{2}`,
  fix:`${M`\A{\times2}`} が 余分に 出る → ${D`\A{\times\frac{1}{2}}`}`,
  lines:[[4, String.raw`=\A{\frac{1}{2}}\cdot\frac{1}{5}(2x+3)^5+C`], [5, String.raw`=\DP{\frac{1}{10}(2x+3)^5+C}`]],
  cm:[
    `${M`(2x+3)^4`} を 展開するのは 大変です。${M`2x+3`} を ひとかたまりと 見ます。`,
    `${M`x^4`} の 積分と 同じように、まず ${M`\frac{1}{5}(2x+3)^5`} と <b>当たり</b> を つけます。`,
    `微分して 確かめると、中身 ${M`2x+3`} の 微分で <b class="a">${M`\times2`}</b> が 余分に 出て しまいます。`,
    `余分な ${M`\times2`} を 打ち消すため、<b class="a">${M`\frac{1}{2}`} を 掛けて</b> 帳尻を 合わせます。`,
    `当たりに ${M`\frac{1}{2}`} を 掛けた ものが 答えです。`,
    `${M`\frac{1}{2}\cdot\frac{1}{5}=\frac{1}{10}`}。`
  ]});
const p2 = adjPage({title:'例　⑵', tag:'⑵', q:String.raw`\int\sin(4x-3)\,dx`,
  guess:String.raw`-\cos(4x-3)`, diff:String.raw`\sin(4x-3)\cdot\A{4}`,
  fix:`${M`\A{\times4}`} が 余分に 出る → ${D`\A{\times\frac{1}{4}}`}`,
  lines:[[4, String.raw`=\A{\frac{1}{4}}\cdot\left\{-\cos(4x-3)\right\}+C`], [5, String.raw`=\DP{-\frac{1}{4}\cos(4x-3)+C}`]],
  cm:[
    `三角関数でも 同じです。${M`4x-3`} を ひとかたまりと 見ます。`,
    `${M`\sin`} の 積分は ${M`-\cos`}。当たりは ${M`-\cos(4x-3)`}。`,
    `微分すると、中身 ${M`4x-3`} の 微分で ${M`\times4`} が 余分に 出ます。`,
    `${M`\frac{1}{4}`} を 掛けて 帳尻を 合わせます。`,
    `当たりに ${M`\frac{1}{4}`} を 掛けます。`,
    `答えは ${M`-\frac{1}{4}\cos(4x-3)+C`}。`
  ]});
const p3 = adjPage({title:'例　⑶', tag:'⑶', q:String.raw`\int\sqrt{2x+5}\,dx=\int(2x+5)^{\frac{1}{2}}\,dx`,
  guess:String.raw`\frac{2}{3}(2x+5)^{\frac{3}{2}}`, diff:String.raw`(2x+5)^{\frac{1}{2}}\cdot\A{2}`,
  fix:`${M`\A{\times2}`} が 余分に 出る → ${D`\A{\times\frac{1}{2}}`}`,
  lines:[[4, String.raw`=\A{\frac{1}{2}}\cdot\frac{2}{3}(2x+5)^{\frac{3}{2}}+C`], [5, String.raw`=\DP{\frac{1}{3}(2x+5)\sqrt{2x+5}+C}`]],
  cm:[
    `根号は 指数に 直します。${M`\sqrt{2x+5}=(2x+5)^{\frac{1}{2}}`}。`,
    `指数を 1 増やして ${M`\frac{3}{2}`}、${M`\frac{3}{2}`} で 割るので、当たりは ${M`\frac{2}{3}(2x+5)^{\frac{3}{2}}`}。`,
    `微分すると、中身の 微分で ${M`\times2`} が 余分に 出ます。`,
    `${M`\frac{1}{2}`} を 掛けて 帳尻を 合わせます。`,
    `${M`\frac{1}{2}\cdot\frac{2}{3}=\frac{1}{3}`}。`,
    `${M`(2x+5)^{\frac{3}{2}}=(2x+5)\sqrt{2x+5}`} と 根号に 戻します。`
  ]});

/* 公式に まとめる */
const p4 = HD(NO, '公式に まとめる', SEC) + `<div class="bd col" style="gap:28px">
  ${BOX('合成関数の 不定積分', `${D`\int f(\A{a}x+b)\,dx=`}${FILL(1, D`\A{\frac{1}{a}}F(\A{a}x+b)+C`, 9)}<span style="font-size:22px">（${M`F(x)`} は ${M`f(x)`} の 不定積分）</span>`)}
  <div class="q" data-s="2" style="font-size:28px">中身が 1次式 ${M`ax+b`} なら、ふつうに 積分して、<b class="a">${M`x`} の 係数 ${M`a`} で 割る</b>。</div>
</div>` + CAP([
  `例⑴〜⑶ で、毎回 同じ ことを して いました。`,
  `中身の 微分で ${M`\times a`} が 出るので、いつも ${M`\frac{1}{a}`} を 掛けて 帳尻を 合わせます。`,
  `中身が 1次式の ときは、この 形で すぐ 答えが 書けます。`
]);

/* 問5 */
const p5 = gridPage({no:NO, sec:SEC, title:'問5　⑴〜⑶', q:'次の 不定積分を 求めよ。', c1:true, items:[
  {tag:'⑴', q:String.raw`\int(3x+1)^3\,dx`, o:1, lines:[[1, String.raw`=\A{\frac{1}{3}}\cdot\frac{1}{4}(3x+1)^4+C=\DP{\frac{1}{12}(3x+1)^4+C}`]]},
  {tag:'⑵', q:String.raw`\int e^{2x-3}\,dx`, o:2, lines:[[2, String.raw`=\DP{\A{\frac{1}{2}}e^{2x-3}+C}`]]},
  {tag:'⑶', q:String.raw`\int\sin(3x+4)\,dx`, o:3, lines:[[3, String.raw`=\A{\frac{1}{3}}\cdot\left\{-\cos(3x+4)\right\}+C=\DP{-\frac{1}{3}\cos(3x+4)+C}`]]},
], cm:[
  `当たりを つけて、${M`x`} の 係数で 割ります。`,
  `⑴ 当たり ${M`\frac{1}{4}(3x+1)^4`}。中身の 微分で ${M`\times3`} が 出るので ${M`\frac{1}{3}`} を 掛けます。`,
  `⑵ ${M`e^x`} の 積分は ${M`e^x`}。中身の 微分で ${M`\times2`} が 出るので ${M`\frac{1}{2}`} を 掛けます。`,
  `⑶ 当たり ${M`-\cos(3x+4)`}。${M`\times3`} が 出るので ${M`\frac{1}{3}`} を 掛けます。（次の ページから 1問ずつ くわしく）`
]});
const p6 = gridPage({no:NO, sec:SEC, title:'問5　⑷〜⑹', c1:true, items:[
  {tag:'⑷', q:String.raw`\int\cos\left(4x-\frac{\pi}{3}\right)dx`, o:1, lines:[[1, String.raw`=\DP{\A{\frac{1}{4}}\sin\left(4x-\frac{\pi}{3}\right)+C}`]]},
  {tag:'⑸', q:String.raw`\int\sqrt{1-2x}\,dx`, o:2, lines:[[2, String.raw`=\A{\left(-\frac{1}{2}\right)}\cdot\frac{2}{3}(1-2x)^{\frac{3}{2}}+C=\DP{-\frac{1}{3}(1-2x)\sqrt{1-2x}+C}`]]},
  {tag:'⑹', q:String.raw`\int\frac{dx}{3x+5}`, o:3, lines:[[3, String.raw`=\DP{\A{\frac{1}{3}}\log|3x+5|+C}`]]},
], cm:[
  `中身の ${M`x`} の 係数が 負の ときも、同じように 割ります。`,
  `⑷ 当たり ${M`\sin\left(4x-\frac{\pi}{3}\right)`}。${M`\times4`} が 出るので ${M`\frac{1}{4}`}。`,
  `⑸ ${M`x`} の 係数は ${M`-2`}。だから ${M`-\frac{1}{2}`} を 掛けます。符号に 注意。`,
  `⑹ ${M`\frac{1}{x}\to\log|x|`} と 同じで、当たり ${M`\log|3x+5|`}。${M`\times3`} が 出るので ${M`\frac{1}{3}`}。（次の ページから 1問ずつ くわしく）`
]});

/* 問5 の くわしく（10/29 の 板書）：当たり → 微分してみる → k 倍 大きく 出る → 1/k を 掛けて 消す → 元の 式も 1/k 倍
   o = {tag, q, hint（使う 公式）, inner（中身）, guess（当たり）, gd（微分した 形。k の 前まで）, k, kc（消した k）,
        fix（1/k）, fixc（消した 1/k）, f（元の 中身の 式）, ans（1/k・当たり）, fin（整理した 答え。なければ ans まで）} */
function adjDetail(o){
  const R = (n, k, t, e) => `<div class="dr"${n!=null?` data-s="${n}"`:''}${e?` data-e="${e}"`:''}><span class="k">${k}</span>${D(t)}</div>`;
  return HD(NO, `問5　${o.tag}　くわしく`, SEC) + `<div class="bd">
  <div class="l" style="gap:10px">
    ${PQ(o.tag, o.q)}
    <div class="adr">
      ${R(1, '当たり', o.guess)}
      ${R(2, '微分すると', String.raw`\left(${o.guess}\right)'=${o.gd}\times\A{${o.k}}`)}
      <div class="swap">${R(4, '帳尻', String.raw`\left(\A{${o.fix}}\cdot ${o.guess}\right)'=\A{${o.fix}}\times ${o.gd}\times\A{${o.k}}`, 5)}
      ${R(5, '帳尻', String.raw`\left(\A{${o.fix}}\cdot ${o.guess}\right)'=\A{${o.fixc}}\times ${o.gd}\times\A{${o.kc}}=${o.f}`)}</div>
    </div>
    <div class="calc main" style="font-size:27px">
      <div data-s="6">${D(String.raw`${o.q}=\A{${o.fix}}\cdot ${o.guess}+C`)}</div>
      ${o.fin ? `<div data-s="7">${D(String.raw`=\DP{${o.fin}}`)}</div>` : ''}
    </div>
  </div>
  <div class="r bigpt" style="flex-direction:column;gap:12px;align-items:stretch;width:340px">
    ${PT(null, '使う 公式', `<span style="font-size:22px;white-space:nowrap">${D(o.hint)}</span>`)}
    ${PT(3, `${M(o.k)} 倍 大きく 出る`, `中身 ${M(o.inner)} を 微分した ${M(String.raw`\A{${o.k}}`)} が 掛かる`)}
    ${PT(5, `${M(o.fix)} を 掛けて 消す`, `${M(String.raw`\A{${o.fix}}\times\A{${o.k}}=1`)}　→ 元の 式に 戻る`)}
    ${PT(6, '元の 式も', `当たりを ${M(String.raw`\A{${o.fix}}`)} 倍 する`)}
  </div>
</div>` + CAP([
    `中身 ${M(o.inner)} を ひとかたまりと 見て、右上の 公式の 形で 考えます。`,
    `まず <b>当たり</b> を つけて、答えの 式の 形を 書きます。`,
    `本当に 合って いるか、実際に 微分して みます。中身 ${M(o.inner)} の 微分 ${M(o.k)} が 後ろに 出て きます。`,
    `元の 式より <b class="a">${M(o.k)} 倍</b> 大きく 出て しまいました。`,
    `帳尻を 合わせる ため、<b class="a">${M(o.fix)}</b> を 掛けて みます。`,
    `${M(o.fix)} と ${M(o.k)} が 打ち消し合って、元の 式に ぴったり 戻りました。`,
    `だから、当たりの 式も <b class="a">${M(o.fix)} 倍</b> した ものが 答えです。`,
    o.fin ? `整理して 答えます。` : null
  ].filter((c,i)=>i<7||o.fin));
}
const q1 = adjDetail({tag:'⑴', q:String.raw`\int(3x+1)^3\,dx`, hint:String.raw`\int x^3dx=\frac{1}{4}x^4+C`, inner:'3x+1',
  guess:String.raw`\frac{1}{4}(3x+1)^4`, gd:'(3x+1)^3', k:'3', kc:String.raw`\cancel{3}`, fix:String.raw`\frac{1}{3}`, fixc:String.raw`\frac{1}{\cancel{3}}`,
  f:'(3x+1)^3', fin:String.raw`\frac{1}{12}(3x+1)^4+C`});
const q2 = adjDetail({tag:'⑵', q:String.raw`\int e^{2x-3}\,dx`, hint:String.raw`\int e^xdx=e^x+C`, inner:'2x-3',
  guess:'e^{2x-3}', gd:'e^{2x-3}', k:'2', kc:String.raw`\cancel{2}`, fix:String.raw`\frac{1}{2}`, fixc:String.raw`\frac{1}{\cancel{2}}`, f:'e^{2x-3}'});
const q3 = adjDetail({tag:'⑶', q:String.raw`\int\sin(3x+4)\,dx`, hint:String.raw`\int\sin x\,dx=-\cos x+C`, inner:'3x+4',
  guess:String.raw`\{-\cos(3x+4)\}`, gd:String.raw`\sin(3x+4)`, k:'3', kc:String.raw`\cancel{3}`, fix:String.raw`\frac{1}{3}`, fixc:String.raw`\frac{1}{\cancel{3}}`,
  f:String.raw`\sin(3x+4)`, fin:String.raw`-\frac{1}{3}\cos(3x+4)+C`});
const q4 = adjDetail({tag:'⑷', q:String.raw`\int\cos\left(4x-\frac{\pi}{3}\right)dx`, hint:String.raw`\int\cos x\,dx=\sin x+C`, inner:String.raw`4x-\frac{\pi}{3}`,
  guess:String.raw`\sin\left(4x-\frac{\pi}{3}\right)`, gd:String.raw`\cos\left(4x-\frac{\pi}{3}\right)`, k:'4', kc:String.raw`\cancel{4}`, fix:String.raw`\frac{1}{4}`, fixc:String.raw`\frac{1}{\cancel{4}}`,
  f:String.raw`\cos\left(4x-\frac{\pi}{3}\right)`});
const q5 = adjDetail({tag:'⑸', q:String.raw`\int(1-2x)^{\frac{1}{2}}\,dx`, hint:String.raw`\int x^{\frac{1}{2}}dx=\frac{2}{3}x^{\frac{3}{2}}+C`, inner:'1-2x',
  guess:String.raw`\frac{2}{3}(1-2x)^{\frac{3}{2}}`, gd:String.raw`(1-2x)^{\frac{1}{2}}`, k:'(-2)', kc:String.raw`(-\cancel{2})`, fix:String.raw`\left(-\frac{1}{2}\right)`, fixc:String.raw`\left(-\frac{1}{\cancel{2}}\right)`,
  f:String.raw`(1-2x)^{\frac{1}{2}}`, fin:String.raw`-\frac{1}{3}(1-2x)\sqrt{1-2x}+C`});
const q6 = adjDetail({tag:'⑹', q:String.raw`\int\frac{dx}{3x+5}`, hint:String.raw`\int\frac{1}{x}dx=\log|x|+C`, inner:'3x+5',
  guess:String.raw`\log|3x+5|`, gd:String.raw`\frac{1}{3x+5}`, k:'3', kc:String.raw`\cancel{3}`, fix:String.raw`\frac{1}{3}`, fixc:String.raw`\frac{1}{\cancel{3}}`, f:String.raw`\frac{1}{3x+5}`});

const p7 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('合成関数の 不定積分', `${D`\int f(ax+b)\,dx=\frac{1}{a}F(ax+b)+C`}`)}
  <div class="sum">
    <span>当たり</span><span class="ar">→</span><span>${M`ax+b`} を ひとかたまりと 見て 積分</span>
    <span>帳尻</span><span class="ar">→</span><span>中身の 微分で 出る ${M`\times a`} を、${M`\frac{1}{a}`} で 打ち消す</span>
  </div>
</div>` + CAP([`②-1 からは、中身が 1次式で ない ときにも 使える「置換積分法」を 学びます。`]);

const DECK = {title:'①-5 合成関数の不定積分', pages:[
  {name:'表紙', html:p0}, {name:'例　⑴', html:p1}, {name:'例　⑵', html:p2}, {name:'例　⑶', html:p3},
  {name:'公式に まとめる', html:p4}, {name:'問5　⑴〜⑶', html:p5}, {name:'問5　⑴　くわしく', html:q1, add:'10/29'}, {name:'問5　⑵　くわしく', html:q2, add:'10/29'}, {name:'問5　⑶　くわしく', html:q3, add:'10/29'},
  {name:'問5　⑷〜⑹', html:p6}, {name:'問5　⑷　くわしく', html:q4, add:'10/29'}, {name:'問5　⑸　くわしく', html:q5, add:'10/29'}, {name:'問5　⑹　くわしく', html:q6, add:'10/29'}, {name:'まとめ', html:p7},
]};
''')

# ---------------------------------------------------------------- ②-1 置換積分（1次式を t に）
DECKS['2-1_置換積分_1次式'] = ('②-1 置換積分（1次式を t に）', r'''
const NO = '②-1', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'置換積分法', sub:`かたまりを ${M`t`} と おいて、${M`t`} の 積分に する`});

const p1 = HD(NO, '置換積分法の 手順', SEC) + `<div class="bd col" style="gap:24px">
  ${BOX('置換積分法', `<div style="line-height:2.1">
    <div data-s="1">① ${M`\B{t}=`}（かたまり）と おく</div>
    <div data-s="2">② ${M`\frac{dx}{dt}`} を 求め、${M`dx=`}（${M`t`} の 式）${M`dt`} として 変形する</div>
    <div data-s="3">③ 式を すべて ${M`\B{t}`} に 置きかえる</div>
    <div data-s="4">④ ${M`t`} で 積分し、${M`x`} に 戻す</div></div>`)}
</div>` + CAP([
  `①-5 では 中身が 1次式の とき「帳尻合わせ」で 積分しました。${M`x(x-5)^4`} のように 前に ${M`x`} が あると、それでは できません。`,
  `かたまり（ここでは ${M`x-5`}）を 新しい 文字 ${M`\B{t}`} と おきます。`,
  `${M`dx`} も ${M`dt`} の 式に 直します。ここが いちばん 大事な ところです。`,
  `${M`x`}、${M`dx`} を すべて ${M`t`} の 式に して、${M`t`} だけの 積分に します。`,
  `${M`t`} で 積分したら、最後に ${M`t`} を ${M`x`} の 式に 戻します。`
]);

const p2 = subPage({no:NO, sec:SEC, title:'例　⑴', tag:'⑴', q:String.raw`\int x(x-5)^4\,dx`,
  top:`<div class="q qline">次の 不定積分を 求めよ。</div>`,
  prep:[[1, String.raw`x-5=\B{t}\ \text{とおくと}\ \ x=t+5`], [2, String.raw`\frac{dx}{dt}=1\quad\text{よって}\quad dx=dt`]],
  pt:PT(6, '分数で くくる コツ', `${M`t^5`} を ${M`\frac{6}{6}t^5`} と 書きかえると<br>${M`\frac{1}{6}t^6+\frac{6}{6}t^5=\frac{1}{6}t^5(t+6)`}`),
  calc:[[3, String.raw`=\int(\B{t}+5)\B{t}^4\,dt=\int\left(t^5+5t^4\right)dt`], [4, String.raw`=\frac{1}{6}t^6+t^5+C`],
        [5, String.raw`=\frac{1}{6}t^6+\frac{6}{6}t^5+C=\frac{1}{6}t^5(t+6)+C`], [7, String.raw`=\frac{1}{6}(x-5)^5\left\{(x-5)+6\right\}+C`],
        [8, String.raw`=\DP{\frac{1}{6}(x+1)(x-5)^5+C}`]],
  cm:[
    `手順どおりに 進めます。`,
    `① かたまり ${M`x-5`} を ${M`t`} と おきます。前の ${M`x`} も ${M`t`} の 式に したいので、${M`x=t+5`} と 表します。`,
    `② ${M`x=t+5`} の 両辺を ${M`t`} で 微分すると ${M`\frac{dx}{dt}=1`}。両辺に ${M`dt`} を 掛けて ${M`dx=dt`}。`,
    `③ ${M`x\to t+5`}、${M`(x-5)^4\to t^4`}、${M`dx\to dt`} と 置きかえ、展開します。`,
    `④ ${M`t`} で 積分します。`,
    `答えを 整理するため、${M`\frac{1}{6}t^5`} で くくります。`,
    `${M`t^5=\frac{6}{6}t^5`} と 分母を そろえるのが コツです。`,
    `${M`t`} を ${M`x-5`} に 戻します。${M`\{\ \}`} の 中の ${M`t`} も 忘れずに。`,
    `${M`(x-5)+6=x+1`}。`
  ]});

const p3 = subPage({no:NO, sec:SEC, title:'例　⑵', tag:'⑵', q:String.raw`\int x(2x+1)^3\,dx`,
  prep:[[1, String.raw`2x+1=\B{t}\ \text{とおくと}\ \ x=\frac{1}{2}t-\frac{1}{2}`], [2, String.raw`\frac{dx}{dt}=\frac{1}{2}\quad\text{よって}\quad dx=\A{\frac{1}{2}}dt`]],
  pt:PT(2, '注意', `${M`dx=dt`} では ありません。${M`\A{\frac{1}{2}}`} を 忘れない。`),
  calc:[[3, String.raw`=\int\frac{t-1}{2}\cdot t^3\cdot\A{\frac{1}{2}}\,dt=\frac{1}{4}\int\left(t^4-t^3\right)dt`],
        [4, String.raw`=\frac{1}{4}\left(\frac{1}{5}t^5-\frac{1}{4}t^4\right)+C=\frac{1}{20}t^5-\frac{1}{16}t^4+C`],
        [5, String.raw`=\frac{4}{80}t^5-\frac{5}{80}t^4+C=\frac{1}{80}t^4(4t-5)+C`],
        [6, String.raw`=\frac{1}{80}(2x+1)^4\left\{4(2x+1)-5\right\}+C`],
        [7, String.raw`=\DP{\frac{1}{80}(8x-1)(2x+1)^4+C}`]],
  cm:[
    `${M`x`} の 係数が ${M`2`} の ときです。`,
    `① ${M`2x+1=t`} から ${M`x=\frac{t-1}{2}=\frac{1}{2}t-\frac{1}{2}`}。`,
    `② ${M`t`} で 微分すると ${M`\frac{dx}{dt}=\frac{1}{2}`}。だから ${M`dx=\frac{1}{2}dt`}。`,
    `③ ${M`x\to\frac{t-1}{2}`}、${M`(2x+1)^3\to t^3`}、${M`dx\to\frac{1}{2}dt`}。定数 ${M`\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}`} を 前に 出します。`,
    `④ ${M`t`} で 積分します。`,
    `${M`20`} と ${M`16`} の 最小公倍数 ${M`80`} に 通分して、${M`\frac{1}{80}t^4`} で くくります。`,
    `${M`t`} を ${M`2x+1`} に 戻します。`,
    `${M`\{\ \}`} の 中：${M`4(2x+1)-5=8x-1`}。`
  ]});

const p4 = subPage({no:NO, sec:SEC, title:'問6　⑴', tag:'⑴', q:String.raw`\int x(x-4)^3\,dx`,
  top:`<div class="q qline">次の 不定積分を、置換積分法を 利用して 求めよ。</div>`,
  prep:[[1, String.raw`x-4=\B{t}\ \text{とおくと}\ \ x=t+4`], [2, String.raw`\frac{dx}{dt}=1\quad\text{よって}\quad dx=dt`]],
  pt:PT(5, 'くくり方', `${M`t^4`} を ${M`\frac{5}{5}t^4`} に して ${M`\frac{1}{5}t^4`} で くくる`),
  calc:[[3, String.raw`=\int(t+4)t^3\,dt=\int\left(t^4+4t^3\right)dt`], [4, String.raw`=\frac{1}{5}t^5+t^4+C`],
        [5, String.raw`=\frac{1}{5}t^5+\frac{5}{5}t^4+C=\frac{1}{5}t^4(t+5)+C`], [6, String.raw`=\frac{1}{5}(x-4)^4\left\{(x-4)+5\right\}+C`],
        [7, String.raw`=\DP{\frac{1}{5}(x+1)(x-4)^4+C}`]],
  cm:[`例⑴ と 同じ 形です。`, `① ${M`x-4=t`}、${M`x=t+4`}。`, `② ${M`dx=dt`}。`, `③ 置きかえて 展開します。`, `④ ${M`t`} で 積分します。`,
      `${M`\frac{5}{5}t^4`} と 書きかえて、${M`\frac{1}{5}t^4`} で くくります。`, `${M`t`} を ${M`x-4`} に 戻します。`, `${M`(x-4)+5=x+1`}。`]});

const p5 = subPage({no:NO, sec:SEC, title:'問6　⑵', tag:'⑵', q:String.raw`\int(x-1)(2x+3)^4\,dx`,
  prep:[[1, String.raw`2x+3=\B{t}\ \text{とおくと}\ \ x=\frac{1}{2}t-\frac{3}{2}`], [2, String.raw`\frac{dx}{dt}=\frac{1}{2}\quad\text{よって}\quad dx=\frac{1}{2}dt`],
        [3, String.raw`\text{また}\ \ x-1=\frac{t-3}{2}-\frac{2}{2}=\frac{t-5}{2}`]],
  pt:PT(3, 'ポイント', `${M`x-1`} も ${M`t`} の 式に 直してから 置きかえる`),
  calc:[[4, String.raw`=\int\frac{t-5}{2}\cdot t^4\cdot\frac{1}{2}\,dt=\frac{1}{4}\int\left(t^5-5t^4\right)dt`],
        [5, String.raw`=\frac{1}{4}\left(\frac{1}{6}t^6-t^5\right)+C=\frac{1}{24}t^6-\frac{1}{4}t^5+C`],
        [6, String.raw`=\frac{1}{24}t^6-\frac{6}{24}t^5+C=\frac{1}{24}t^5(t-6)+C`],
        [7, String.raw`=\frac{1}{24}(2x+3)^5\left\{(2x+3)-6\right\}+C`],
        [8, String.raw`=\DP{\frac{1}{24}(2x-3)(2x+3)^5+C}`]],
  cm:[`前が ${M`x`} では なく ${M`x-1`} です。`, `① ${M`2x+3=t`} から ${M`x=\frac{t-3}{2}`}。`, `② ${M`dx=\frac{1}{2}dt`}。`,
      `${M`x-1`} も ${M`t`} の 式に します。${M`\frac{t-3}{2}-1=\frac{t-5}{2}`}。`,
      `③ 置きかえます。${M`\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}`} を 前に 出します。`, `④ ${M`t`} で 積分します。`,
      `${M`\frac{1}{4}=\frac{6}{24}`} と 分母を ${M`24`} に そろえ、${M`\frac{1}{24}t^5`} で くくります。`, `${M`t`} を ${M`2x+3`} に 戻します。`, `${M`(2x+3)-6=2x-3`}。`]});

const p6 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:24px">
  ${BOX('置換積分法', `① ${M`t=`}（かたまり）と おく　② ${M`dx=`}（　）${M`dt`}<br>③ すべて ${M`t`} に 置きかえる　④ 積分して ${M`x`} に 戻す`)}
  <div class="sum">
    <span>${M`x`}</span><span class="ar">→</span><span>${M`t`} の 式に（${M`x=t+5`} など）</span>
    <span>${M`dx`}</span><span class="ar">→</span><span>${M`x`} を ${M`t`} で 微分して ${M`dx=\frac{dx}{dt}\,dt`}</span>
    <span>答え</span><span class="ar">→</span><span>分母を そろえて くくり、${M`t`} を ${M`x`} に 戻す</span>
  </div>
</div>` + CAP([`②-2 では、根号 ${M`\sqrt{\ }`} を まるごと ${M`t`} と おきます。`]);

const DECK = {title:'②-1 置換積分（1次式を t に）', pages:[
  {name:'表紙', html:p0}, {name:'置換積分法の 手順', html:p1}, {name:'例　⑴', html:p2}, {name:'例　⑵', html:p3},
  {name:'問6　⑴', html:p4}, {name:'問6　⑵', html:p5}, {name:'まとめ', html:p6},
]};
''')

# ---------------------------------------------------------------- ②-2 置換積分（√ を t に）
DECKS['2-2_置換積分_根号'] = ('②-2 置換積分（√ を t に）', r'''
const NO = '②-2', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'置換積分法', sub:`根号 ${M`\sqrt{\ }`} を まるごと ${M`t`} と おく`});

const p1 = subPage({no:NO, sec:SEC, title:'例', tag:'⑴', q:String.raw`\int x\sqrt{x-1}\,dx`,
  top:`<div class="q qline">次の 不定積分を 求めよ。</div>`,
  prep:[[1, String.raw`\sqrt{x-1}=\B{t}\ \text{とおくと}`], [2, String.raw`x-1=t^2\quad\text{より}\quad x=t^2+1`], [3, String.raw`\frac{dx}{dt}=2t\quad\text{よって}\quad dx=2t\,dt`]],
  pt:PT(7, '戻すとき', `${M`t^2=x-1`}、${M`t^3=t^2\cdot t=(x-1)\sqrt{x-1}`}`),
  calc:[[4, String.raw`=\int\left(t^2+1\right)\cdot\B{t}\cdot2t\,dt=\int\left(2t^4+2t^2\right)dt`], [5, String.raw`=\frac{2}{5}t^5+\frac{2}{3}t^3+C`],
        [6, String.raw`=\frac{6}{15}t^5+\frac{10}{15}t^3+C=\frac{2}{15}t^3\left(3t^2+5\right)+C`],
        [7, String.raw`=\frac{2}{15}(x-1)\sqrt{x-1}\left\{3(x-1)+5\right\}+C`], [8, String.raw`=\DP{\frac{2}{15}(3x+2)(x-1)\sqrt{x-1}+C}`]],
  cm:[
    `根号が ある ときは、<b>根号を まるごと</b> ${M`t`} と おくと 計算が 楽です。`,
    `① ${M`\sqrt{x-1}=t`} と おきます。`,
    `両辺を 2乗して ${M`x-1=t^2`}。${M`x=t^2+1`} と ${M`x`} を ${M`t`} で 表します。`,
    `② ${M`t`} で 微分して ${M`\frac{dx}{dt}=2t`}、${M`dx=2t\,dt`}。`,
    `③ ${M`x\to t^2+1`}、${M`\sqrt{x-1}\to t`}、${M`dx\to2t\,dt`}。根号が 消えました。`,
    `④ ${M`t`} で 積分します。`,
    `分母を ${M`15`} に そろえて、${M`\frac{2}{15}t^3`} で くくります。`,
    `${M`t^3=(x-1)\sqrt{x-1}`}、${M`t^2=x-1`} として ${M`x`} に 戻します。`,
    `${M`3(x-1)+5=3x+2`}。（${M`x-1=t`} と おいても 解けますが、${M`t^{\frac{1}{2}}`} の 計算に なります）`
  ]});

/* 問7（1問 1ページ） */
const Q7 = `<div class="q qline">次の 不定積分を 求めよ。</div>`;
const p2 = subPage({no:NO, sec:SEC, title:'問7　⑴', tag:'⑴', q:String.raw`\int x\sqrt{x+1}\,dx`, top:Q7,
  prep:[[1, String.raw`\sqrt{x+1}=\B{t}\ \text{とおくと}\ \ x=t^2-1`], [2, String.raw`\frac{dx}{dt}=2t\quad\text{よって}\quad dx=2t\,dt`]],
  pt:PT(6, '戻すとき', `${M`t^2=x+1`}、${M`t^3=(x+1)\sqrt{x+1}`}`),
  calc:[[3, String.raw`=\int\left(t^2-1\right)\cdot t\cdot2t\,dt=\int\left(2t^4-2t^2\right)dt`], [4, String.raw`=\frac{2}{5}t^5-\frac{2}{3}t^3+C`],
        [5, String.raw`=\frac{6}{15}t^5-\frac{10}{15}t^3+C=\frac{2}{15}t^3\left(3t^2-5\right)+C`],
        [6, String.raw`=\frac{2}{15}(x+1)\sqrt{x+1}\left\{3(x+1)-5\right\}+C`], [7, String.raw`=\DP{\frac{2}{15}(3x-2)(x+1)\sqrt{x+1}+C}`]],
  cm:[`例と 同じ 手順です。`, `${M`x+1=t^2`} より ${M`x=t^2-1`}。`, `${M`dx=2t\,dt`}。`, `置きかえて 展開します。`, `${M`t`} で 積分します。`,
      `分母を ${M`15`} に そろえて くくります。`, `${M`x`} に 戻します。`, `${M`3(x+1)-5=3x-2`}。`]});
const p3 = subPage({no:NO, sec:SEC, title:'問7　⑵', tag:'⑵', q:String.raw`\int x\sqrt{2-x}\,dx`,
  prep:[[1, String.raw`\sqrt{2-x}=\B{t}\ \text{とおくと}\ \ x=2-t^2`], [2, String.raw`\frac{dx}{dt}=-2t\quad\text{よって}\quad dx=\A{-2t}\,dt`]],
  pt:PT(2, '符号に 注意', `${M`dx=-2t\,dt`} の マイナスを 忘れない`),
  calc:[[3, String.raw`=\int\left(2-t^2\right)\cdot t\cdot(\A{-2t})\,dt=\int\left(2t^4-4t^2\right)dt`], [4, String.raw`=\frac{2}{5}t^5-\frac{4}{3}t^3+C`],
        [5, String.raw`=\frac{6}{15}t^5-\frac{20}{15}t^3+C=\frac{2}{15}t^3\left(3t^2-10\right)+C`],
        [6, String.raw`=\frac{2}{15}(2-x)\sqrt{2-x}\left\{3(2-x)-10\right\}+C`], [7, String.raw`=\DP{-\frac{2}{15}(3x+4)(2-x)\sqrt{2-x}+C}`]],
  cm:[`根号の 中が ${M`2-x`} です。`, `${M`2-x=t^2`} より ${M`x=2-t^2`}。`, `${M`t`} で 微分すると ${M`-2t`}。${M`dx=-2t\,dt`}。`,
      `置きかえて 展開します。${M`(2-t^2)\cdot(-2t^2)=2t^4-4t^2`}。`, `${M`t`} で 積分します。`, `分母を ${M`15`} に そろえて くくります。`, `${M`x`} に 戻します。`,
      `${M`3(2-x)-10=-3x-4=-(3x+4)`}。マイナスを 前に 出します。`]});
const p4 = subPage({no:NO, sec:SEC, title:'問7　⑶', tag:'⑶', q:String.raw`\int x\sqrt{2x-1}\,dx`,
  prep:[[1, String.raw`\sqrt{2x-1}=\B{t}\ \text{とおくと}\ \ x=\frac{1}{2}t^2+\frac{1}{2}`], [2, String.raw`\frac{dx}{dt}=t\quad\text{よって}\quad dx=t\,dt`]],
  pt:PT(7, '約分', `${M`6x+2=2(3x+1)`} の ${M`2`} で 約分<br>${M`\frac{1}{30}\times2=\frac{1}{15}`}`),
  calc:[[3, String.raw`=\int\left(\frac{1}{2}t^2+\frac{1}{2}\right)\cdot t\cdot t\,dt=\frac{1}{2}\int\left(t^4+t^2\right)dt`], [4, String.raw`=\frac{1}{10}t^5+\frac{1}{6}t^3+C`],
        [5, String.raw`=\frac{3}{30}t^5+\frac{5}{30}t^3+C=\frac{1}{30}t^3\left(3t^2+5\right)+C`],
        [6, String.raw`=\frac{1}{30}(2x-1)\sqrt{2x-1}\,(6x+2)+C`], [7, String.raw`=\DP{\frac{1}{15}(3x+1)(2x-1)\sqrt{2x-1}+C}`]],
  cm:[`${M`x`} の 係数が ${M`2`} です。`, `${M`2x-1=t^2`} より ${M`x=\frac{1}{2}t^2+\frac{1}{2}`}。`, `${M`t`} で 微分すると ${M`t`}。${M`dx=t\,dt`}。`,
      `置きかえて、${M`\frac{1}{2}`} を 前に 出します。`, `${M`t`} で 積分します。`, `${M`10`} と ${M`6`} の 最小公倍数 ${M`30`} で そろえて くくります。`,
      `${M`x`} に 戻します。${M`3(2x-1)+5=6x+2`}。`, `${M`6x+2=2(3x+1)`} の ${M`2`} で 約分します。`]});
const p5 = subPage({no:NO, sec:SEC, title:'問7　⑷', tag:'⑷', q:String.raw`\int\frac{x}{\sqrt{1-x}}\,dx`,
  prep:[[1, String.raw`\sqrt{1-x}=\B{t}\ \text{とおくと}\ \ x=1-t^2`], [2, String.raw`\frac{dx}{dt}=-2t\quad\text{よって}\quad dx=-2t\,dt`]],
  pt:PT(3, '約分できる', `分母の ${M`t`} と ${M`-2t\,dt`} の ${M`t`} が 約分されて 消える`),
  calc:[[3, String.raw`=\int\frac{1-t^2}{\A{t}}\cdot\left(-2\A{t}\right)dt=\int\left(2t^2-2\right)dt`], [4, String.raw`=\frac{2}{3}t^3-2t+C`],
        [5, String.raw`=\frac{2}{3}t^3-\frac{6}{3}t+C=\frac{2}{3}t\left(t^2-3\right)+C`],
        [6, String.raw`=\frac{2}{3}\sqrt{1-x}\left\{(1-x)-3\right\}+C`], [7, String.raw`=\DP{-\frac{2}{3}(x+2)\sqrt{1-x}+C}`]],
  cm:[`根号が 分母に ある 形です。`, `${M`1-x=t^2`} より ${M`x=1-t^2`}。`, `${M`dx=-2t\,dt`}。`,
      `置きかえると、分母の ${M`t`} が 約分されます。${M`(1-t^2)\cdot(-2)=2t^2-2`}。`, `${M`t`} で 積分します。`, `分母を ${M`3`} に そろえて くくります。`,
      `${M`t=\sqrt{1-x}`}、${M`t^2=1-x`} として 戻します。`, `${M`(1-x)-3=-(x+2)`}。`]});

const p6 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  <div class="sum">
    <span>${M`\sqrt{ax+b}=t`}</span><span class="ar">→</span><span>2乗して ${M`ax+b=t^2`}、${M`x=`}（${M`t`} の 式）</span>
    <span>${M`dx`}</span><span class="ar">→</span><span>${M`t`} で 微分して ${M`dx=`}（${M`t`} の 式）${M`dt`}</span>
    <span>戻すとき</span><span class="ar">→</span><span>${M`t^2=ax+b`}、${M`t^3=(ax+b)\sqrt{ax+b}`}</span>
  </div>
</div>` + CAP([`②-3 では、${M`x`} を ${M`t`} の 式に 直しにくい ときの 置換を 学びます。`]);

const DECK = {title:'②-2 置換積分（√ を t に）', pages:[
  {name:'表紙', html:p0}, {name:'例', html:p1}, {name:'問7　⑴', html:p2}, {name:'問7　⑵', html:p3},
  {name:'問7　⑶', html:p4}, {name:'問7　⑷', html:p5}, {name:'まとめ', html:p6},
]};
''')

# ---------------------------------------------------------------- ②-3 置換積分（x で 微分する 型）
DECKS['2-3_置換積分_xで微分'] = ('②-3 置換積分（x で 微分する 型）', r'''
const NO = '②-3', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'置換積分法', sub:`${M`t=g(x)`} の まま、${M`x`} で 微分する`});
const XP = '置きかえ（x で 微分）';

const p1 = subPage({no:NO, sec:SEC, title:'例　⑴', tag:'⑴', q:String.raw`\int\sin^2x\A{\cos x}\,dx`, plabel:XP,
  top:`<div class="q qline">次の 不定積分を 求めよ。</div>`,
  prep:[[1, String.raw`\sin x=\B{t}\ \text{とおくと}`], [2, String.raw`\cos x=\frac{dt}{dx}\quad\text{よって}\quad\A{\cos x\,dx}=dt`]],
  pt:PT(2, '②-1 との ちがい', `${M`x=`}（${M`t`} の 式）に 直しにくい ときは、<b>${M`t=\sin x`} の まま 両辺を ${M`x`} で 微分</b> する。`),
  calc:[[3, String.raw`=\int(\sin x)^2\cdot\A{\cos x\,dx}=\int t^2\,dt`], [4, String.raw`=\frac{1}{3}t^3+C`], [5, String.raw`=\DP{\frac{1}{3}\sin^3x+C}`]],
  cm:[
    `${M`\sin x`} を 微分すると ${M`\cos x`}。式の 中に ${M`\sin x`} と その 微分 ${M`\cos x`} が そろって います。`,
    `① ${M`\sin x=t`} と おきます。`,
    `② ${M`x=`} の 形には しにくいので、${M`t=\sin x`} の まま 両辺を ${M`x`} で 微分します。${M`\frac{dt}{dx}=\cos x`} より ${M`\cos x\,dx=dt`}。`,
    `③ ${M`(\sin x)^2\to t^2`}、${M`\cos x\,dx\to dt`}。きれいに ${M`t`} だけに なりました。`,
    `④ ${M`t`} で 積分します。`,
    `${M`t=\sin x`} を 戻します。${M`(\sin x)^3`} は ${M`\sin^3x`} と 書きます。`
  ]});
const p2 = subPage({no:NO, sec:SEC, title:'例　⑵', tag:'⑵', q:String.raw`\int\A{x}e^{x^2}\,dx`, plabel:XP,
  prep:[[1, String.raw`x^2=\B{t}\ \text{とおくと}`], [2, String.raw`2x=\frac{dt}{dx}\quad\text{よって}\quad\A{x\,dx}=\frac{1}{2}dt`]],
  pt:PT(2, 'x dx を まとめて 置きかえる', `${M`2x\,dx=dt`} の 両辺を ${M`2`} で 割って ${M`x\,dx=\frac{1}{2}dt`}`),
  calc:[[3, String.raw`=\int e^{x^2}\cdot\A{x\,dx}=\int e^t\cdot\frac{1}{2}\,dt`], [4, String.raw`=\frac{1}{2}\int e^t\,dt=\frac{1}{2}e^t+C`], [5, String.raw`=\DP{\frac{1}{2}e^{x^2}+C}`]],
  cm:[
    `${M`e^{x^2}`} の 肩の ${M`x^2`} を ${M`t`} と おきます。${M`x^2`} を 微分すると ${M`2x`}。前の ${M`x`} が その なかまです。`,
    `① ${M`x^2=t`} と おきます。`,
    `② 両辺を ${M`x`} で 微分して ${M`2x=\frac{dt}{dx}`}。式に ある「${M`x\,dx`}」の 形に するため、${M`2`} で 割ります。`,
    `③ ${M`e^{x^2}\to e^t`}、${M`x\,dx\to\frac{1}{2}dt`}。`,
    `④ ${M`t`} で 積分します。`,
    `${M`t=x^2`} を 戻します。`
  ]});

const Q8 = `<div class="q qline">次の 不定積分を 求めよ。</div>`;
const p3 = subPage({no:NO, sec:SEC, title:'問8　⑴', tag:'⑴', q:String.raw`\int\cos^3x\A{\sin x}\,dx`, plabel:XP, top:Q8,
  prep:[[1, String.raw`\cos x=\B{t}\ \text{とおくと}`], [2, String.raw`-\sin x=\frac{dt}{dx}\quad\text{よって}\quad\A{\sin x\,dx}=-dt`]],
  pt:PT(2, '符号に 注意', `${M`(\cos x)'=-\sin x`} なので、${M`\sin x\,dx=-dt`} の マイナスを 忘れない`),
  calc:[[3, String.raw`=\int t^3\cdot(-1)\,dt=-\int t^3\,dt`], [4, String.raw`=-\frac{1}{4}t^4+C`], [5, String.raw`=\DP{-\frac{1}{4}\cos^4x+C}`]],
  cm:[`${M`\cos x`} と その 微分（${M`-\sin x`}）が そろって います。`, `${M`\cos x=t`} と おきます。`, `${M`x`} で 微分して ${M`-\sin x=\frac{dt}{dx}`}。${M`\sin x\,dx=-dt`}。`,
      `${M`\cos^3x\to t^3`}、${M`\sin x\,dx\to-dt`}。`, `${M`t`} で 積分します。`, `${M`t=\cos x`} を 戻します。`]});
const p4 = subPage({no:NO, sec:SEC, title:'問8　⑵', tag:'⑵', q:String.raw`\int\A{3x^2}\sqrt{x^3+1}\,dx`, plabel:XP,
  prep:[[1, String.raw`x^3+1=\B{t}\ \text{とおくと}`], [2, String.raw`3x^2=\frac{dt}{dx}\quad\text{よって}\quad\A{3x^2\,dx}=dt`]],
  pt:PT(4, 'ポイント', `${M`t^{\frac{3}{2}}=t\cdot t^{\frac{1}{2}}=t\sqrt{t}`}`),
  calc:[[3, String.raw`=\int\sqrt{t}\,dt=\int t^{\frac{1}{2}}\,dt`], [4, String.raw`=\frac{2}{3}t^{\frac{3}{2}}+C=\frac{2}{3}t\sqrt{t}+C`], [5, String.raw`=\DP{\frac{2}{3}\left(x^3+1\right)\sqrt{x^3+1}+C}`]],
  cm:[`根号の 中 ${M`x^3+1`} を 微分すると ${M`3x^2`}。前に ある ${M`3x^2`} と 同じです。`, `${M`x^3+1=t`} と おきます。`, `${M`x`} で 微分して ${M`3x^2\,dx=dt`}。`,
      `${M`\sqrt{x^3+1}\to\sqrt{t}`}、${M`3x^2\,dx\to dt`}。`, `${M`t`} で 積分し、${M`t^{\frac{3}{2}}=t\sqrt{t}`} と 直します。`, `${M`t=x^3+1`} を 戻します。`]});
const p5 = subPage({no:NO, sec:SEC, title:'問8　⑶', tag:'⑶', q:String.raw`\int\A{e^x}\left(e^x+1\right)^2\,dx`, plabel:XP,
  prep:[[1, String.raw`e^x+1=\B{t}\ \text{とおくと}`], [2, String.raw`e^x=\frac{dt}{dx}\quad\text{よって}\quad\A{e^x\,dx}=dt`]],
  pt:PT(3, '展開しなくて よい', `${M`(e^x)'=e^x`} なので ${M`e^x\,dx`} が まるごと ${M`dt`} に なる`),
  calc:[[3, String.raw`=\int t^2\,dt`], [4, String.raw`=\frac{1}{3}t^3+C`], [5, String.raw`=\DP{\frac{1}{3}\left(e^x+1\right)^3+C}`]],
  cm:[`${M`e^x+1`} を 微分すると ${M`e^x`}。前の ${M`e^x`} と 同じです。`, `${M`e^x+1=t`} と おきます。`, `${M`x`} で 微分して ${M`e^x\,dx=dt`}。`,
      `${M`(e^x+1)^2\to t^2`}、${M`e^x\,dx\to dt`}。展開は いりません。`, `${M`t`} で 積分します。`, `${M`t=e^x+1`} を 戻します。`]});
const p6 = subPage({no:NO, sec:SEC, title:'問8　⑷', tag:'⑷', q:String.raw`\int\A{x}e^{-x^2}\,dx`, plabel:XP,
  prep:[[1, String.raw`-x^2=\B{t}\ \text{とおくと}`], [2, String.raw`-2x=\frac{dt}{dx}\quad\text{よって}\quad\A{x\,dx}=-\frac{1}{2}dt`]],
  pt:PT(2, '例⑵ と 同じ 形', `${M`-2x\,dx=dt`} の 両辺を ${M`-2`} で 割って ${M`x\,dx=-\frac{1}{2}dt`}`),
  calc:[[3, String.raw`=\int e^t\cdot\left(-\frac{1}{2}\right)dt`], [4, String.raw`=-\frac{1}{2}e^t+C`], [5, String.raw`=\DP{-\frac{1}{2}e^{-x^2}+C}`]],
  cm:[`例⑵ と 同じ 形です。肩の ${M`-x^2`} を ${M`t`} と おきます。`, `${M`-x^2=t`} と おきます。`, `${M`x`} で 微分して ${M`-2x=\frac{dt}{dx}`}。${M`-2`} で 割って ${M`x\,dx=-\frac{1}{2}dt`}。`,
      `${M`e^{-x^2}\to e^t`}、${M`x\,dx\to-\frac{1}{2}dt`}。`, `${M`t`} で 積分します。`, `${M`t=-x^2`} を 戻します。`]});

const p7 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('置換の コツ', `式の 中に 「${M`g(x)`}」と「その 微分 ${M`g'(x)`}」が そろって いたら<br>${M`g(x)=t`} と おき、両辺を ${M`x`} で 微分して ${M`g'(x)\,dx=dt`}`)}
  <div class="sum">
    <span>${M`\sin x=t`}</span><span class="ar">→</span><span>${M`\cos x\,dx=dt`}</span>
    <span>${M`\cos x=t`}</span><span class="ar">→</span><span>${M`\sin x\,dx=-dt`}</span>
    <span>${M`x^2=t`}</span><span class="ar">→</span><span>${M`x\,dx=\frac{1}{2}dt`}</span>
  </div>
</div>` + CAP([`②-4 では、分子が 分母の 微分に なって いる 分数の 積分を 学びます。`]);

const DECK = {title:'②-3 置換積分（x で 微分する 型）', pages:[
  {name:'表紙', html:p0}, {name:'例　⑴', html:p1}, {name:'例　⑵', html:p2}, {name:'問8　⑴', html:p3},
  {name:'問8　⑵', html:p4}, {name:'問8　⑶', html:p5}, {name:'問8　⑷', html:p6}, {name:'まとめ', html:p7},
]};
''')

# ---------------------------------------------------------------- ②-4 置換積分（分子が 分母の 微分）
DECKS['2-4_置換積分_分子が分母の微分'] = ('②-4 置換積分（分子が 分母の 微分）', r'''
const NO = '②-4', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'置換積分法', sub:`分子が 分母の 微分 → ${M`\log|\ \ |`}`});
const XP = '置きかえ（x で 微分）';

const p1 = subPage({no:NO, sec:SEC, title:'例　⑴', tag:'⑴', q:String.raw`\int\frac{\A{2x}}{x^2+1}\,dx`, plabel:XP,
  top:`<div class="q qline">次の 不定積分を 求めよ。</div>`,
  prep:[[1, String.raw`x^2+1=\B{t}\ \text{とおくと}`], [2, String.raw`2x=\frac{dt}{dx}\quad\text{よって}\quad\A{2x\,dx}=dt`]],
  pt:PT(5, '| | が はずれる 理由', `${M`x^2+1>0`} なので　${M`\log\left|x^2+1\right|=\log\left(x^2+1\right)`}`),
  calc:[[3, String.raw`=\int\frac{1}{x^2+1}\cdot\A{2x\,dx}=\int\frac{1}{t}\,dt`], [4, String.raw`=\log|t|+C`], [5, String.raw`=\DP{\log\left(x^2+1\right)+C}`]],
  cm:[
    `分母 ${M`x^2+1`} を 微分すると ${M`2x`}。分子と 同じです。`,
    `分母を ${M`t`} と おきます。`,
    `${M`x`} で 微分して ${M`2x\,dx=dt`}。`,
    `分母は ${M`t`}、分子と ${M`dx`} は ${M`dt`} に。${M`\int\frac{1}{t}\,dt`} に なります。`,
    `${M`\frac{1}{t}`} の 積分は ${M`\log|t|`}。`,
    `${M`x^2+1`} は いつも 正なので、絶対値を はずせます。`
  ]});
const p2 = subPage({no:NO, sec:SEC, title:'例　⑵', tag:'⑵', q:String.raw`\int\tan x\,dx=\int\frac{\A{\sin x}}{\cos x}\,dx`, plabel:XP,
  prep:[[1, String.raw`\cos x=\B{t}\ \text{とおくと}`], [2, String.raw`-\sin x=\frac{dt}{dx}\quad\text{よって}\quad\A{\sin x\,dx}=-dt`]],
  pt:PT(4, 'マイナスが 付く わけ', `分母の ${M`\cos x`} を 微分すると ${M`-\sin x`}。分子の ${M`\sin x`} と 符号だけ ちがう`),
  calc:[[3, String.raw`=\int\frac{1}{\cos x}\cdot\A{\sin x\,dx}=\int\frac{1}{t}\cdot(-1)\,dt`], [4, String.raw`=-\int\frac{1}{t}\,dt=-\log|t|+C`], [5, String.raw`=\DP{-\log|\cos x|+C}`]],
  cm:[
    `${M`\tan x`} は まず ${M`\frac{\sin x}{\cos x}`} に 直します。`,
    `分母の ${M`\cos x`} を ${M`t`} と おきます。`,
    `${M`x`} で 微分して ${M`-\sin x=\frac{dt}{dx}`}。${M`\sin x\,dx=-dt`}。`,
    `置きかえると ${M`-\int\frac{1}{t}\,dt`}。`,
    `${M`\frac{1}{t}`} の 積分は ${M`\log|t|`}。マイナスが 付きます。`,
    `${M`\cos x`} は 負にも なるので、絶対値は 残します。`
  ]});

const p3 = HD(NO, '公式に まとめる', SEC) + `<div class="bd col" style="gap:28px">
  ${BOX('分子が 分母の 微分に なって いる とき', `${D`\int\frac{\A{g'(x)}}{g(x)}\,dx=`}${FILL(1, D`\log|g(x)|+C`, 7)}`)}
  <div class="q" data-s="2" style="font-size:27px">${M`g(x)=t`} と おくと ${M`g'(x)\,dx=dt`}。だから ${M`\int\frac{1}{t}\,dt=\log|t|+C`}。</div>
</div>` + CAP([
  `例⑴・⑵ は、どちらも 分子が 分母の 微分（または その 定数倍）でした。`,
  `この 形なら、答えは すぐに ${M`\log|`}分母${M`|`} です。`,
  `置換積分で 確かめると、この 公式に なります。問9 は すべて この 形です。`
]);

const Q9 = `<div class="q qline">次の 不定積分を 求めよ。</div>`;
const p4 = subPage({no:NO, sec:SEC, title:'問9　⑴', tag:'⑴', q:String.raw`\int\frac{\A{2x-1}}{x^2-x+1}\,dx`, plabel:XP, top:Q9,
  prep:[[1, String.raw`x^2-x+1=\B{t}\ \text{とおくと}`], [2, String.raw`2x-1=\frac{dt}{dx}\quad\text{よって}\quad\A{(2x-1)dx}=dt`]],
  pt:PT(4, '| | を はずせる', `${M`x^2-x+1=\left(x-\frac{1}{2}\right)^2+\frac{3}{4}>0`}`),
  calc:[[3, String.raw`=\int\frac{1}{t}\,dt=\log|t|+C`], [4, String.raw`=\DP{\log\left(x^2-x+1\right)+C}`]],
  cm:[`分母 ${M`x^2-x+1`} を 微分すると ${M`2x-1`}。分子と 同じです。`, `分母を ${M`t`} と おきます。`, `${M`(2x-1)dx=dt`}。`,
      `${M`\int\frac{1}{t}\,dt=\log|t|+C`}。`, `平方完成すると いつも 正。絶対値を はずせます。`]});
const p5 = subPage({no:NO, sec:SEC, title:'問9　⑵', tag:'⑵', q:String.raw`\int\frac{\A{x}}{x^2-2}\,dx`, plabel:XP,
  prep:[[1, String.raw`x^2-2=\B{t}\ \text{とおくと}`], [2, String.raw`2x=\frac{dt}{dx}\quad\text{よって}\quad\A{x\,dx}=\frac{1}{2}dt`]],
  pt:PT(5, '| | は 残す', `${M`x^2-2`} は 負にも なるので、絶対値は つけたまま`),
  calc:[[3, String.raw`=\int\frac{1}{t}\cdot\frac{1}{2}\,dt=\frac{1}{2}\int\frac{1}{t}\,dt`], [4, String.raw`=\frac{1}{2}\log|t|+C`], [5, String.raw`=\DP{\frac{1}{2}\log\left|x^2-2\right|+C}`]],
  cm:[`分母を 微分すると ${M`2x`}。分子は ${M`x`} なので、${M`\frac{1}{2}`} 倍の 関係です。`, `分母を ${M`t`} と おきます。`, `${M`2x\,dx=dt`} を ${M`2`} で 割って ${M`x\,dx=\frac{1}{2}dt`}。`,
      `置きかえて ${M`\frac{1}{2}`} を 前に 出します。`, `${M`\frac{1}{2}\log|t|`}。`, `${M`x^2-2`} は 負にも なるので、絶対値は 残します。`]});
const p6 = subPage({no:NO, sec:SEC, title:'問9　⑶', tag:'⑶', q:String.raw`\int\frac{\A{e^x}}{1+e^x}\,dx`, plabel:XP,
  prep:[[1, String.raw`1+e^x=\B{t}\ \text{とおくと}`], [2, String.raw`e^x=\frac{dt}{dx}\quad\text{よって}\quad\A{e^x\,dx}=dt`]],
  pt:PT(4, '| | を はずせる', `${M`1+e^x>0`} なので 絶対値は いらない`),
  calc:[[3, String.raw`=\int\frac{1}{t}\,dt=\log|t|+C`], [4, String.raw`=\DP{\log\left(1+e^x\right)+C}`]],
  cm:[`分母 ${M`1+e^x`} を 微分すると ${M`e^x`}。分子と 同じです。`, `分母を ${M`t`} と おきます。`, `${M`e^x\,dx=dt`}。`, `${M`\log|t|+C`}。`, `${M`e^x>0`} なので ${M`1+e^x>0`}。絶対値を はずせます。`]});
const p7 = subPage({no:NO, sec:SEC, title:'問9　⑷', tag:'⑷', q:String.raw`\int\frac{1}{\tan x}\,dx=\int\frac{\A{\cos x}}{\sin x}\,dx`, plabel:XP,
  prep:[[1, String.raw`\sin x=\B{t}\ \text{とおくと}`], [2, String.raw`\cos x=\frac{dt}{dx}\quad\text{よって}\quad\A{\cos x\,dx}=dt`]],
  pt:PT(0, '1/tan x の 直し方', `${M`1\div\frac{\sin x}{\cos x}=\frac{\cos x}{\sin x}`}。分子の ${M`\cos x`} は 分母 ${M`\sin x`} の 微分`),
  calc:[[3, String.raw`=\int\frac{1}{t}\,dt=\log|t|+C`], [4, String.raw`=\DP{\log|\sin x|+C}`]],
  cm:[`${M`\frac{1}{\tan x}`} は ${M`\frac{\cos x}{\sin x}`} に 直します。分子は 分母の 微分です。`, `分母 ${M`\sin x`} を ${M`t`} と おきます。`, `${M`\cos x\,dx=dt`}。`,
      `${M`\log|t|+C`}。`, `${M`\sin x`} は 負にも なるので、絶対値は 残します。`]});

const p8 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('公式', `${D`\int\frac{g'(x)}{g(x)}\,dx=\log|g(x)|+C`}`)}
  <div class="sum">
    <span>${M`x^2+1`}、${M`1+e^x`}</span><span class="ar">→</span><span>いつも 正。${M`|\ \ |`} を はずす</span>
    <span>${M`x^2-2`}、${M`\cos x`}</span><span class="ar">→</span><span>負にも なる。${M`|\ \ |`} を 残す</span>
  </div>
</div>` + CAP([`③-1 では、積の 形の 積分に 使う「部分積分法」を 学びます。`]);

const DECK = {title:'②-4 置換積分（分子が 分母の 微分）', pages:[
  {name:'表紙', html:p0}, {name:'例　⑴', html:p1}, {name:'例　⑵', html:p2}, {name:'公式に まとめる', html:p3},
  {name:'問9　⑴', html:p4}, {name:'問9　⑵', html:p5}, {name:'問9　⑶', html:p6}, {name:'問9　⑷', html:p7}, {name:'まとめ', html:p8},
]};
''')

# ---------------------------------------------------------------- ③-1 部分積分法
PICK_JS = r'''
/* 部分積分の 1問：左＝選び方（微分する方 橙・積分する方 紫）と 積、右＝計算
   o = {title, tag, q, top, f:[元, 微分], g:[元, 積分], prod, calc, cm} */
function ppPage(o){
  return subPage({no:NO, sec:SEC, title:o.title, tag:o.tag, q:o.q, top:o.top, plabel:'選び方',
    prep:[[1, `<div><span class="tg a">微分する方</span>${M(String.raw`\A{${o.f[0]}}\ \to\ \A{${o.f[1]}}`)}</div>`],
          [2, `<div><span class="tg b">積分する方</span>${M(String.raw`\B{${o.g[0]}}\ \to\ \B{${o.g[1]}}`)}</div>`]],
    pt:PT(3, '微分した方 × 積分した方', `${D(o.prod)}${o.pnote ? `<br>${o.pnote}` : '　→ 積分できる'}`),
    calc:o.calc, cm:o.cm});
}
'''
DECKS['3-1_部分積分'] = ('③-1 部分積分法', r'''
const NO = '③-1', SEC = '数学Ⅲ　積分法';
''' + PICK_JS + r'''
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'部分積分法', sub:'積の 形を「微分する方」と「積分する方」に 分ける'});

const p1 = HD(NO, '部分積分法', SEC) + `<div class="bd col" style="gap:20px">
  ${BOX('部分積分法', `${D`\int\A{f(x)}\B{g'(x)}\,dx=`}${FILL(1, D`\A{f(x)}\B{g(x)}-\int\A{f'(x)}\B{g(x)}\,dx`, 13)}`)}
  <div class="pbox" data-s="2"><div class="pl2">なぜ？（積の 微分から）</div>
    ${CALC([[2, String.raw`\{f(x)g(x)\}'=f'(x)g(x)+f(x)g'(x)`], [3, String.raw`f(x)g(x)=\int f'(x)g(x)\,dx+\int f(x)g'(x)\,dx`]])}</div>
</div>` + CAP([
  `${M`x\sin x`} のような <b>積</b> の 積分に 使う 公式です。`,
  `${M`f(x)`} は <b class="a">微分</b> して、${M`g'(x)`} は <b class="b">積分</b> して 使います。`,
  `なぜ この 式に なるのか。数学Ⅲ の 積の 微分の 公式から 出ます。`,
  `両辺を 積分して、${M`\int f'(x)g(x)\,dx`} を 左に 移せば 公式です。`
]);

const p2 = HD(NO, '選び方', SEC) + `<div class="bd col" style="gap:22px">
  ${BOX('どちらを 微分する？', `<div class="lst">
    <div data-s="1">① <span class="k a">【微分する方】</span>${M`f(x)`}：微分しやすく、微分した 後の 式が 簡単に なる 方</div>
    <div data-s="2">② <span class="k b">【積分する方】</span>${M`g'(x)`}：積分しやすい 方</div>
    <div data-s="3">③「微分した 方」と「積分した 方」の 積が 積分できそうかを 予想しておく</div></div>`)}
</div>` + CAP([
  `公式を 使う 前に、2つの うち どちらを 微分するかを 決めます。`,
  `${M`x`} は 微分すると ${M`1`}。式が 簡単に なるので、微分する 方に 向いて います。`,
  `${M`\sin x`}、${M`\cos x`}、${M`e^x`} は、積分しても 形が ほとんど 変わりません。`,
  `最後に 残る ${M`\int f'(x)g(x)\,dx`} が 積分できれば 成功です。先に 確かめておきます。`
]);

const Q = `<div class="q qline">次の 不定積分を 求めよ。</div>`;
const p3 = ppPage({title:'例', tag:'⑴', q:String.raw`\int x\sin x\,dx`, top:Q,
  f:['x', '1'], g:[String.raw`\sin x`, String.raw`-\cos x`], prod:String.raw`1\cdot(-\cos x)=-\cos x`,
  calc:[[4, String.raw`=\A{x}\cdot\B{(-\cos x)}-\int\A{1}\cdot\B{(-\cos x)}\,dx`], [5, String.raw`=-x\cos x+\int\cos x\,dx`], [6, String.raw`=\DP{-x\cos x+\sin x+C}`]],
  cm:[`${M`x`} と ${M`\sin x`} の 積です。どちらを 微分する 方に するかを 決めます。`,
      `<b class="a">微分する方</b> は ${M`x`}。微分すると ${M`1`} に なり、簡単です。`,
      `<b class="b">積分する方</b> は ${M`\sin x`}。積分すると ${M`-\cos x`}。`,
      `微分した方と 積分した方の 積は ${M`-\cos x`}。これなら 積分できます。`,
      `公式「${M`fg-\int f'g\,dx`}」に 入れます。`,
      `マイナスが 2つで プラスに なります。`,
      `${M`\int\cos x\,dx=\sin x`}。`]});

const p4 = ppPage({title:'問10　⑴', tag:'⑴', q:String.raw`\int x\cos x\,dx`, top:Q,
  f:['x', '1'], g:[String.raw`\cos x`, String.raw`\sin x`], prod:String.raw`1\cdot\sin x=\sin x`,
  calc:[[4, String.raw`=\A{x}\B{\sin x}-\int\A{1}\cdot\B{\sin x}\,dx`], [5, String.raw`=\DP{x\sin x+\cos x+C}`]],
  cm:[`例と 同じ 形です。`, `微分する方は ${M`x`}。`, `積分する方は ${M`\cos x`}。積分すると ${M`\sin x`}。`, `積は ${M`\sin x`}。積分できます。`,
      `公式に 入れます。`, `${M`\int\sin x\,dx=-\cos x`} なので、${M`-(-\cos x)=+\cos x`}。`]});
const p5 = ppPage({title:'問10　⑵', tag:'⑵', q:String.raw`\int x\sin 3x\,dx`,
  f:['x', '1'], g:[String.raw`\sin 3x`, String.raw`-\frac{1}{3}\cos 3x`], prod:String.raw`-\frac{1}{3}\cos 3x`,
  calc:[[4, String.raw`=\A{x}\cdot\B{\left(-\frac{1}{3}\cos 3x\right)}-\int\A{1}\cdot\B{\left(-\frac{1}{3}\cos 3x\right)}dx`],
        [5, String.raw`=-\frac{1}{3}x\cos 3x+\frac{1}{3}\int\cos 3x\,dx`], [6, String.raw`=\DP{-\frac{1}{3}x\cos 3x+\frac{1}{9}\sin 3x+C}`]],
  cm:[`中身が ${M`3x`} です。`, `微分する方は ${M`x`}。`, `${M`\sin 3x`} の 積分は、①-5 の 帳尻合わせで ${M`-\frac{1}{3}\cos 3x`}。`, `積も ${M`\cos 3x`} の 形なので 積分できます。`,
      `公式に 入れます。`, `定数 ${M`\frac{1}{3}`} を 前に 出します。`, `${M`\int\cos 3x\,dx=\frac{1}{3}\sin 3x`}。${M`\frac{1}{3}\cdot\frac{1}{3}=\frac{1}{9}`}。`]});
const p6 = ppPage({title:'問10　⑶', tag:'⑶', q:String.raw`\int(2x+1)\sin x\,dx`,
  f:['2x+1', '2'], g:[String.raw`\sin x`, String.raw`-\cos x`], prod:String.raw`2\cdot(-\cos x)=-2\cos x`,
  calc:[[4, String.raw`=\A{(2x+1)}\B{(-\cos x)}-\int\A{2}\cdot\B{(-\cos x)}\,dx`], [5, String.raw`=-(2x+1)\cos x+2\int\cos x\,dx`], [6, String.raw`=\DP{-(2x+1)\cos x+2\sin x+C}`]],
  cm:[`1次式 ${M`2x+1`} と ${M`\sin x`} の 積です。`, `微分する方は ${M`2x+1`}。微分すると ${M`2`}。`, `積分する方は ${M`\sin x`}。`, `積は ${M`-2\cos x`}。積分できます。`,
      `公式に 入れます。`, `マイナスが 2つで プラス、${M`2`} を 前に 出します。`, `${M`2\int\cos x\,dx=2\sin x`}。`]});
const p7 = ppPage({title:'問10　⑷', tag:'⑷', q:String.raw`\int(x+1)\cos 2x\,dx`,
  f:['x+1', '1'], g:[String.raw`\cos 2x`, String.raw`\frac{1}{2}\sin 2x`], prod:String.raw`\frac{1}{2}\sin 2x`,
  calc:[[4, String.raw`=\A{(x+1)}\cdot\B{\frac{1}{2}\sin 2x}-\int\A{1}\cdot\B{\frac{1}{2}\sin 2x}\,dx`],
        [5, String.raw`=\frac{1}{2}(x+1)\sin 2x-\frac{1}{2}\cdot\left(-\frac{1}{2}\cos 2x\right)+C`], [6, String.raw`=\DP{\frac{1}{2}(x+1)\sin 2x+\frac{1}{4}\cos 2x+C}`]],
  cm:[`中身が ${M`2x`} です。`, `微分する方は ${M`x+1`}。`, `${M`\cos 2x`} の 積分は ${M`\frac{1}{2}\sin 2x`}。`, `積は ${M`\frac{1}{2}\sin 2x`}。積分できます。`,
      `公式に 入れます。`, `${M`\int\sin 2x\,dx=-\frac{1}{2}\cos 2x`}。`, `${M`-\frac{1}{2}\cdot\left(-\frac{1}{2}\right)=+\frac{1}{4}`}。`]});

const p8 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  ${BOX('部分積分法', `${D`\int\A{f(x)}\B{g'(x)}\,dx=\A{f(x)}\B{g(x)}-\int\A{f'(x)}\B{g(x)}\,dx`}`)}
  <div class="sum">
    <span class="a">微分する方</span><span class="ar">→</span><span>${M`x`}、${M`2x+1`} などの 多項式（微分すると 簡単）</span>
    <span class="b">積分する方</span><span class="ar">→</span><span>${M`\sin x`}、${M`\cos 3x`} など（積分しやすい）</span>
  </div>
</div>` + CAP([`③-2 では、${M`e^x`} や ${M`\log x`} を 含む 積の 部分積分を 学びます。`]);

const DECK = {title:'③-1 部分積分法', pages:[
  {name:'表紙', html:p0}, {name:'部分積分法', html:p1}, {name:'選び方', html:p2}, {name:'例', html:p3},
  {name:'問10　⑴', html:p4}, {name:'問10　⑵', html:p5}, {name:'問10　⑶', html:p6}, {name:'問10　⑷', html:p7}, {name:'まとめ', html:p8},
]};
''')

# ---------------------------------------------------------------- ③-2 部分積分（eˣ・log x）
DECKS['3-2_部分積分_指数と対数'] = ('③-2 部分積分（eˣ・log x）', r'''
const NO = '③-2', SEC = '数学Ⅲ　積分法';
''' + PICK_JS + r'''
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'部分積分法', sub:`${M`e^x`} と ${M`\log x`} を 含む 積`});
const Q = `<div class="q qline">次の 不定積分を 求めよ。</div>`;

const p1 = ppPage({title:'例　⑴', tag:'⑴', q:String.raw`\int xe^x\,dx`, top:Q,
  f:['x', '1'], g:['e^x', 'e^x'], prod:String.raw`1\cdot e^x=e^x`,
  calc:[[4, String.raw`=\A{x}\B{e^x}-\int\A{1}\cdot\B{e^x}\,dx`], [5, String.raw`=xe^x-e^x+C`], [6, String.raw`=\DP{(x-1)e^x+C}`]],
  cm:[`${M`x`} と ${M`e^x`} の 積です。`, `微分する方は ${M`x`}。`, `積分する方は ${M`e^x`}。積分しても ${M`e^x`} の まま です。`, `積は ${M`e^x`}。積分できます。`,
      `公式に 入れます。`, `${M`\int e^x\,dx=e^x`}。`, `${M`e^x`} で くくって 整理します。`]});
const p2 = ppPage({title:'例　⑵', tag:'⑵', q:String.raw`\int\log x\,dx`,
  top:PT(null, 'ポイント', `${M`\log x=\B{1}\cdot\A{\log x}`} と 考える。${M`1`} を 積分する方（${M`1=(x)'`}）に する。`),
  f:[String.raw`\log x`, String.raw`\frac{1}{x}`], g:['1', 'x'], prod:String.raw`\frac{1}{x}\cdot x=1`,
  calc:[[4, String.raw`=\int\B{1}\cdot\A{\log x}\,dx=\B{x}\A{\log x}-\int\B{x}\cdot\A{\frac{1}{x}}\,dx`], [5, String.raw`=x\log x-\int1\,dx`], [6, String.raw`=\DP{x\log x-x+C}`]],
  cm:[`${M`\log x`} だけでは 積に 見えません。${M`1\times\log x`} と 考えます。`, `${M`\log x`} は 積分の 公式が ないので、<b class="a">微分する方</b>。微分すると ${M`\frac{1}{x}`}。`,
      `残りの ${M`1`} を <b class="b">積分する方</b> に します。積分すると ${M`x`}。`, `積は ${M`\frac{1}{x}\cdot x=1`}。約分されて 簡単に なります。`,
      `公式に 入れます。`, `${M`x\cdot\frac{1}{x}=1`}。`, `${M`\int1\,dx=x`}。この 結果は 公式として 覚えて おくと 便利です。`]});

const p3 = ppPage({title:'問11　⑴', tag:'⑴', q:String.raw`\int(2x-1)e^x\,dx`, top:Q,
  f:['2x-1', '2'], g:['e^x', 'e^x'], prod:'2e^x',
  calc:[[4, String.raw`=\A{(2x-1)}\B{e^x}-\int\A{2}\B{e^x}\,dx`], [5, String.raw`=(2x-1)e^x-2e^x+C`], [6, String.raw`=\DP{(2x-3)e^x+C}`]],
  cm:[`例⑴ と 同じ 形です。`, `微分する方は ${M`2x-1`}。`, `積分する方は ${M`e^x`}。`, `積は ${M`2e^x`}。`, `公式に 入れます。`, `${M`2\int e^x\,dx=2e^x`}。`, `${M`e^x`} で くくると ${M`(2x-1)-2=2x-3`}。`]});
const p4 = ppPage({title:'問11　⑵', tag:'⑵', q:String.raw`\int xe^{2x}\,dx`,
  f:['x', '1'], g:['e^{2x}', String.raw`\frac{1}{2}e^{2x}`], prod:String.raw`\frac{1}{2}e^{2x}`,
  calc:[[4, String.raw`=\A{x}\cdot\B{\frac{1}{2}e^{2x}}-\int\A{1}\cdot\B{\frac{1}{2}e^{2x}}\,dx`], [5, String.raw`=\frac{1}{2}xe^{2x}-\frac{1}{4}e^{2x}+C`], [6, String.raw`=\DP{\frac{1}{4}(2x-1)e^{2x}+C}`]],
  cm:[`中身が ${M`2x`} です。`, `微分する方は ${M`x`}。`, `${M`e^{2x}`} の 積分は ${M`\frac{1}{2}e^{2x}`}（帳尻合わせ）。`, `積は ${M`\frac{1}{2}e^{2x}`}。`,
      `公式に 入れます。`, `${M`\frac{1}{2}\int e^{2x}\,dx=\frac{1}{2}\cdot\frac{1}{2}e^{2x}=\frac{1}{4}e^{2x}`}。`, `${M`\frac{1}{4}e^{2x}`} で くくります。`]});
const p5 = ppPage({title:'問11　⑶', tag:'⑶', q:String.raw`\int xe^{-x}\,dx`,
  f:['x', '1'], g:['e^{-x}', '-e^{-x}'], prod:'-e^{-x}',
  calc:[[4, String.raw`=\A{x}\B{(-e^{-x})}-\int\A{1}\cdot\B{(-e^{-x})}\,dx`], [5, String.raw`=-xe^{-x}+\int e^{-x}\,dx`], [6, String.raw`=-xe^{-x}-e^{-x}+C`], [7, String.raw`=\DP{-(x+1)e^{-x}+C}`]],
  cm:[`中身が ${M`-x`} です。符号に 注意します。`, `微分する方は ${M`x`}。`, `${M`e^{-x}`} の 積分は ${M`-e^{-x}`}。`, `積は ${M`-e^{-x}`}。`,
      `公式に 入れます。`, `マイナスが 2つで プラス。`, `${M`\int e^{-x}\,dx=-e^{-x}`}。`, `${M`-e^{-x}`} で くくります。`]});

const p6 = ppPage({title:'問12　⑴', tag:'⑴', q:String.raw`\int\log 2x\,dx`, top:Q,
  f:[String.raw`\log 2x`, String.raw`\frac{1}{x}`], g:['1', 'x'], prod:String.raw`\frac{1}{x}\cdot x=1`,
  calc:[[4, String.raw`=\B{x}\A{\log 2x}-\int\B{x}\cdot\A{\frac{1}{x}}\,dx`], [5, String.raw`=x\log 2x-\int1\,dx`], [6, String.raw`=\DP{x\log 2x-x+C}`]],
  cm:[`例⑵ と 同じく、${M`1\times\log 2x`} と 考えます。`, `${M`(\log 2x)'=\frac{2}{2x}=\frac{1}{x}`}。`, `${M`1`} を 積分する方に して ${M`x`}。`, `積は ${M`1`}。`,
      `公式に 入れます。`, `${M`x\cdot\frac{1}{x}=1`}。`, `${M`\int1\,dx=x`}。`]});
const p7 = ppPage({title:'問12　⑵', tag:'⑵', q:String.raw`\int x\log x\,dx`,
  f:[String.raw`\log x`, String.raw`\frac{1}{x}`], g:['x', String.raw`\frac{1}{2}x^2`], prod:String.raw`\frac{1}{x}\cdot\frac{1}{2}x^2=\frac{1}{2}x`,
  calc:[[4, String.raw`=\B{\frac{1}{2}x^2}\A{\log x}-\int\B{\frac{1}{2}x^2}\cdot\A{\frac{1}{x}}\,dx`], [5, String.raw`=\frac{1}{2}x^2\log x-\frac{1}{2}\int x\,dx`], [6, String.raw`=\DP{\frac{1}{2}x^2\log x-\frac{1}{4}x^2+C}`]],
  cm:[`${M`\log x`} が あるときは、${M`\log x`} を 微分する方に します。`, `${M`\log x`} を 微分すると ${M`\frac{1}{x}`}。`, `${M`x`} を 積分すると ${M`\frac{1}{2}x^2`}。`, `積は ${M`\frac{1}{2}x`}。約分されて 積分できます。`,
      `公式に 入れます。`, `${M`\frac{1}{2}x^2\cdot\frac{1}{x}=\frac{1}{2}x`}。`, `${M`\frac{1}{2}\int x\,dx=\frac{1}{4}x^2`}。`]});
const p8 = ppPage({title:'問12　⑶', tag:'⑶', q:String.raw`\int(2x+1)\log x\,dx`,
  f:[String.raw`\log x`, String.raw`\frac{1}{x}`], g:['2x+1', 'x^2+x'], prod:String.raw`\frac{1}{x}\cdot(x^2+x)=x+1`,
  calc:[[4, String.raw`=\B{(x^2+x)}\A{\log x}-\int\B{(x^2+x)}\cdot\A{\frac{1}{x}}\,dx`], [5, String.raw`=(x^2+x)\log x-\int(x+1)\,dx`], [6, String.raw`=\DP{(x^2+x)\log x-\frac{1}{2}x^2-x+C}`]],
  cm:[`ここでも ${M`\log x`} を 微分する方に します。`, `${M`\log x`} を 微分すると ${M`\frac{1}{x}`}。`, `${M`2x+1`} を 積分すると ${M`x^2+x`}。`, `積は ${M`x+1`}。`,
      `公式に 入れます。`, `${M`(x^2+x)\cdot\frac{1}{x}=x+1`}。`, `${M`\int(x+1)\,dx=\frac{1}{2}x^2+x`}。`]});
const p9 = ppPage({title:'問12　⑷', tag:'⑷', q:String.raw`\int\log(x+1)\,dx`,
  f:[String.raw`\log(x+1)`, String.raw`\frac{1}{x+1}`], g:['1', 'x+1'], prod:String.raw`\frac{1}{x+1}\cdot(x+1)=1`,
  pnote:`${M`1`} の 積分を ${M`x`} では なく <b>${M`x+1`}</b> に すると 約分できる`,
  calc:[[4, String.raw`=\B{(x+1)}\A{\log(x+1)}-\int\B{(x+1)}\cdot\A{\frac{1}{x+1}}\,dx`], [5, String.raw`=(x+1)\log(x+1)-\int1\,dx`], [6, String.raw`=\DP{(x+1)\log(x+1)-x+C}`]],
  cm:[`${M`1\times\log(x+1)`} と 考えます。`, `${M`\log(x+1)`} を 微分すると ${M`\frac{1}{x+1}`}。`, `${M`1`} を 積分します。${M`(x+1)'=1`} なので、${M`x+1`} と しても 正しい 積分です。`,
      `${M`x+1`} を 選ぶと、積が ${M`1`} に なります。これが 工夫です。`, `公式に 入れます。`, `${M`(x+1)\cdot\frac{1}{x+1}=1`}。`, `${M`\int1\,dx=x`}。（${M`x+1>0`} なので ${M`\log`} の 中は そのまま）`]});

const p10 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  <div class="sum">
    <span>${M`x`} と ${M`e^x`}</span><span class="ar">→</span><span><b class="a">${M`x`} を 微分</b>、${M`e^x`} を 積分</span>
    <span>${M`\log x`} を 含む</span><span class="ar">→</span><span><b class="a">${M`\log x`} を 微分</b>（${M`\log x`} は 積分しにくい）</span>
    <span>${M`\log x`} だけ</span><span class="ar">→</span><span>${M`1\times\log x`} と 考え、${M`\int\log x\,dx=x\log x-x+C`}</span>
  </div>
</div>` + CAP([`④-1 では、分数関数の 不定積分を 学びます。`]);

const DECK = {title:'③-2 部分積分（eˣ・log x）', pages:[
  {name:'表紙', html:p0}, {name:'例　⑴', html:p1}, {name:'例　⑵', html:p2},
  {name:'問11　⑴', html:p3}, {name:'問11　⑵', html:p4}, {name:'問11　⑶', html:p5},
  {name:'問12　⑴', html:p6}, {name:'問12　⑵', html:p7}, {name:'問12　⑶', html:p8}, {name:'問12　⑷', html:p9}, {name:'まとめ', html:p10},
]};
''')

# ---------------------------------------------------------------- ④-1 分数関数の不定積分
DECKS['4-1_分数関数の不定積分'] = ('④-1 分数関数の不定積分', r'''
const NO = '④-1', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'分数関数の不定積分', sub:'割り算か、部分分数に 分解するか'});

const p1 = HD(NO, '方針', SEC) + `<div class="bd col" style="gap:20px">
  ${BOX('分子の 次数 ≧ 分母の 次数', `${FILL(1, `分子を 分母で 割って、（商）＋ ${M`\frac{\text{余り}}{\text{分母}}`} の 形に する`, 20)}`)}
  ${BOX('分母の 次数が 高い（2次）', `${FILL(2, '部分分数に 分解して、項ごとに 積分する', 16)}<br><span data-s="3" style="font-size:23px">分母が 1次 ${M`\frac{1}{ax+b}`} なら ${M`\frac{1}{a}\log|ax+b|`} で 積分できる</span>`)}
</div>` + CAP([
  `分数の 式は、分子と 分母の 次数を 比べて 方針を 決めます。`,
  `分子の 次数が 大きい（同じ）ときは、整数の 割り算と 同じように 割ります。`,
  `分母の 次数が 高く、置換積分も 部分積分も 使えない ときは、部分分数に 分解します。`,
  `最後は 分母が 1次式の 分数に なり、${M`\log`} で 積分できます。`
]);

/* 左＝変形（割り算・部分分数）、右＝計算 */
function frPage(o){ return subPage({no:NO, sec:SEC, title:o.title, tag:o.tag, q:o.q, top:o.top, plabel:o.lab, prep:o.prep, pt:o.pt, calc:o.calc, cm:o.cm}); }
const Q = `<div class="q qline">次の 不定積分を 求めよ。</div>`;

const p2 = frPage({title:'例　⑴', tag:'⑴', q:String.raw`\int\frac{2x^2+1}{x-1}\,dx`, top:Q, lab:'割り算',
  prep:[[1, String.raw`2x^2+1=(x-1)(\A{2x+2})+\A{3}`], [2, String.raw`\frac{2x^2+1}{x-1}=\A{2x+2}+\frac{\A{3}}{x-1}`]],
  calc:[[3, String.raw`=\int\left(2x+2+\frac{3}{x-1}\right)dx`], [4, String.raw`=\DP{x^2+2x+3\log|x-1|+C}`]],
  cm:[`分子は 2次、分母は 1次。分子の 次数が 大きいので 割ります。`, `${M`2x^2+1`} を ${M`x-1`} で 割ると、商 ${M`2x+2`}、余り ${M`3`}。`,
      `「商 ＋ 余り／分母」の 形に 書きかえます。`, `これなら 項ごとに 積分できます。`, `${M`\frac{3}{x-1}`} の 積分は ${M`3\log|x-1|`}。`]});
const p3 = frPage({title:'例　⑵', tag:'⑵', q:String.raw`\int\frac{2}{x^2-1}\,dx`, lab:'部分分数に 分解',
  top:PT(null, '使える？', `置換積分 → ×（分子が 分母の 微分で ない）　部分積分 → ×`),
  prep:[[1, String.raw`\frac{2}{x^2-1}=\frac{2}{(x-1)(x+1)}`], [2, String.raw`=\frac{1}{x-1}-\frac{1}{x+1}`]],
  pt:PT(2, '確かめ（通分）', `${D`\frac{(x+1)-(x-1)}{(x-1)(x+1)}=\frac{2}{x^2-1}`}`),
  calc:[[3, String.raw`=\int\left(\frac{1}{x-1}-\frac{1}{x+1}\right)dx`], [4, String.raw`=\log|x-1|-\log|x+1|+C`], [5, String.raw`=\DP{\log\left|\frac{x-1}{x+1}\right|+C}`]],
  cm:[`分母が 2次で、分子は ${M`2`}。割り算は できません。置換も 部分積分も 使えません。`, `分母を 因数分解します。`,
      `2つの 分数の 差に 分けます（部分分数分解）。通分して 確かめると 元に 戻ります。`, `分母が 1次の 分数なので、積分できます。`,
      `それぞれ ${M`\log`} に なります。`, `${M`\log A-\log B=\log\frac{A}{B}`} で 1つに まとめます。`]});

const p4 = frPage({title:'問14　⑴', tag:'⑴', q:String.raw`\int\frac{x^2+1}{x+2}\,dx`, top:Q, lab:'割り算',
  prep:[[1, String.raw`x^2+1=(x+2)(\A{x-2})+\A{5}`]],
  calc:[[2, String.raw`=\int\left(x-2+\frac{5}{x+2}\right)dx`], [3, String.raw`=\DP{\frac{1}{2}x^2-2x+5\log|x+2|+C}`]],
  cm:[`分子の 次数が 大きいので 割ります。`, `商 ${M`x-2`}、余り ${M`5`}。`, `「商 ＋ 余り／分母」に して、項ごとに 積分します。`, `${M`\frac{5}{x+2}`} の 積分は ${M`5\log|x+2|`}。`]});
const p5 = frPage({title:'問14　⑵', tag:'⑵', q:String.raw`\int\frac{2x^2}{2x-1}\,dx`, lab:'割り算',
  prep:[[1, String.raw`2x^2=(2x-1)\left(\A{x+\frac{1}{2}}\right)+\A{\frac{1}{2}}`]],
  pt:PT(3, '分母が 2x−1', `${D`\int\frac{dx}{2x-1}=\frac{1}{2}\log|2x-1|`}（${M`x`} の 係数 ${M`2`} で 割る）`),
  calc:[[2, String.raw`=\int\left(x+\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{2x-1}\right)dx`], [3, String.raw`=\DP{\frac{1}{2}x^2+\frac{1}{2}x+\frac{1}{4}\log|2x-1|+C}`]],
  cm:[`分子の 次数が 大きいので 割ります。`, `商 ${M`x+\frac{1}{2}`}、余り ${M`\frac{1}{2}`}。`, `「商 ＋ 余り／分母」に します。`, `${M`\frac{1}{2x-1}`} の 積分は ${M`\frac{1}{2}\log|2x-1|`}。${M`\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}`}。`]});

const Q16 = `<div class="q qline">次の 不定積分を 求めよ。</div>`;
const p6 = frPage({title:'問16　⑴', tag:'⑴', q:String.raw`\int\frac{dx}{x(x+1)}`, top:Q16, lab:'部分分数に 分解',
  prep:[[1, String.raw`\frac{1}{x(x+1)}=\frac{1}{x}-\frac{1}{x+1}`]],
  calc:[[2, String.raw`=\int\left(\frac{1}{x}-\frac{1}{x+1}\right)dx`], [3, String.raw`=\log|x|-\log|x+1|+C`], [4, String.raw`=\DP{\log\left|\frac{x}{x+1}\right|+C}`]],
  cm:[`分母が 2次。部分分数に 分解します。`, `${M`\frac{1}{x}-\frac{1}{x+1}=\frac{(x+1)-x}{x(x+1)}=\frac{1}{x(x+1)}`}。ぴったり 元に 戻ります。`,
      `項ごとに 積分します。`, `それぞれ ${M`\log`} に なります。`, `1つの ${M`\log`} に まとめます。`]});
const p7 = frPage({title:'問16　⑵', tag:'⑵', q:String.raw`\int\frac{dx}{(x-2)(x+2)}`, lab:'部分分数に 分解',
  prep:[[1, String.raw`\frac{1}{x-2}-\frac{1}{x+2}=\frac{\A{4}}{(x-2)(x+2)}`], [2, String.raw`\frac{1}{(x-2)(x+2)}=\A{\frac{1}{4}}\left(\frac{1}{x-2}-\frac{1}{x+2}\right)`]],
  pt:PT(1, '係数に 注意', `差を 通分すると 分子が ${M`4`}。だから ${M`\frac{1}{4}`} 倍 する`),
  calc:[[3, String.raw`=\frac{1}{4}\int\left(\frac{1}{x-2}-\frac{1}{x+2}\right)dx`], [4, String.raw`=\frac{1}{4}\left(\log|x-2|-\log|x+2|\right)+C`], [5, String.raw`=\DP{\frac{1}{4}\log\left|\frac{x-2}{x+2}\right|+C}`]],
  cm:[`まず 差の 形を 作って みます。`, `通分すると 分子が ${M`4`} に なります。元の 分子は ${M`1`} なので…`, `${M`\frac{1}{4}`} 倍 すれば 元の 式です。`,
      `${M`\frac{1}{4}`} を 前に 出して 積分します。`, `それぞれ ${M`\log`} に なります。`, `1つの ${M`\log`} に まとめます。`]});
const p8 = frPage({title:'問16　⑶', tag:'⑶', q:String.raw`\int\frac{3}{x^2-x-2}\,dx`, lab:'部分分数に 分解',
  prep:[[1, String.raw`x^2-x-2=(x-2)(x+1)`], [2, String.raw`\frac{3}{(x-2)(x+1)}=\frac{1}{x-2}-\frac{1}{x+1}`]],
  calc:[[3, String.raw`=\int\left(\frac{1}{x-2}-\frac{1}{x+1}\right)dx`], [4, String.raw`=\log|x-2|-\log|x+1|+C`], [5, String.raw`=\DP{\log\left|\frac{x-2}{x+1}\right|+C}`]],
  cm:[`分母を 因数分解する ところから 始めます。`, `${M`x^2-x-2=(x-2)(x+1)`}。`, `${M`\frac{1}{x-2}-\frac{1}{x+1}=\frac{3}{(x-2)(x+1)}`}。分子の ${M`3`} と ぴったり 合います。`,
      `項ごとに 積分します。`, `それぞれ ${M`\log`} に なります。`, `1つの ${M`\log`} に まとめます。`]});

const p9 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:26px">
  <div class="sum">
    <span>分子の 次数 ≧ 分母</span><span class="ar">→</span><span>割り算して「商 ＋ ${M`\frac{\text{余り}}{\text{分母}}`}」</span>
    <span>分母が 2次</span><span class="ar">→</span><span>因数分解して 部分分数に 分解</span>
    <span>分母が 1次</span><span class="ar">→</span><span>${M`\int\frac{dx}{ax+b}=\frac{1}{a}\log|ax+b|+C`}</span>
  </div>
</div>` + CAP([`④-2 では、三角関数の 積分に 使う 公式を 加法定理から 導きます。`]);

const DECK = {title:'④-1 分数関数の不定積分', pages:[
  {name:'表紙', html:p0}, {name:'方針', html:p1}, {name:'例　⑴', html:p2}, {name:'例　⑵', html:p3},
  {name:'問14　⑴', html:p4}, {name:'問14　⑵', html:p5}, {name:'問16　⑴', html:p6}, {name:'問16　⑵', html:p7}, {name:'問16　⑶', html:p8}, {name:'まとめ', html:p9},
]};
''')

# ---------------------------------------------------------------- ④-2 半角・積和の公式を 導く
DECKS['4-2_半角と積和の公式'] = ('④-2 半角の公式・積和の公式', r'''
const NO = '④-2', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'半角の公式・積和の公式', sub:'加法定理から 導く'});

const LIST = (an) => `<div class="tbl" style="grid-template-columns:auto 1fr;font-size:21px;white-space:nowrap">
  <div class="th">半角の 公式</div><div class="th">（2乗を 1次に）</div>
  <div>❶</div><div>${D`\sin^2x=\frac{1-\cos2x}{2}`}</div><div>❷</div><div>${D`\cos^2x=\frac{1+\cos2x}{2}`}</div>
  <div class="th">2倍角の 公式の 変形</div><div class="th"></div><div>❸</div><div>${D`\sin x\cos x=\frac{\sin2x}{2}`}</div>
</div>`;
const LIST2 = `<div class="tbl" style="grid-template-columns:auto 1fr;font-size:21px;white-space:nowrap">
  <div class="th">積和の 公式</div><div class="th">（積を 和・差に）</div>
  <div>❹</div><div>${D`\sin\alpha\cos\beta=\frac{1}{2}\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\}`}</div>
  <div>❺</div><div>${D`\cos\alpha\cos\beta=\frac{1}{2}\{\cos(\alpha+\beta)+\cos(\alpha-\beta)\}`}</div>
  <div>❻</div><div>${D`\sin\alpha\sin\beta=-\frac{1}{2}\{\cos(\alpha+\beta)-\cos(\alpha-\beta)\}`}</div>
</div>`;
const p1 = HD(NO, 'これから 導く 公式', SEC) + `<div class="bd" style="align-items:flex-start;gap:20px">
  <div class="l">${LIST()}</div><div class="l">${LIST2}</div>
</div>` + CAP([`④-3・④-4 の 積分で 使う 6つの 公式です。どれも 加法定理から 導けます。`]);

const ADD = PT(null, '加法定理', `${M`\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta`}<br>${M`\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta`}`);
const p2 = HD(NO, 'Ⅰ　2倍角の 公式', SEC) + `<div class="bd col st" style="gap:18px">
  ${ADD}
  <div class="q" style="font-size:27px;line-height:2.3">
    ${M`\beta=\alpha`} と おくと<br>
    ${M`\sin2\alpha=`}${FILL(1, M`2\sin\alpha\cos\alpha`, 7)}　　${M`\cos2\alpha=`}${FILL(2, M`\cos^2\alpha-\sin^2\alpha`, 8)}<br>
    さらに ${M`\sin^2\alpha+\cos^2\alpha=1`} を 使うと<br>
    ${M`\cos2\alpha=`}${FILL(3, M`1-2\sin^2\alpha`, 7)}${M`=`}${FILL(4, M`2\cos^2\alpha-1`, 7)}</div>
</div>` + CAP([
  `加法定理で ${M`\beta`} を ${M`\alpha`} に すると、2倍角の 公式に なります。`,
  `${M`\sin\alpha\cos\alpha+\cos\alpha\sin\alpha=2\sin\alpha\cos\alpha`}。`,
  `${M`\cos\alpha\cos\alpha-\sin\alpha\sin\alpha=\cos^2\alpha-\sin^2\alpha`}。`,
  `${M`\cos^2\alpha=1-\sin^2\alpha`} を 入れると ${M`1-2\sin^2\alpha`}。`,
  `${M`\sin^2\alpha=1-\cos^2\alpha`} を 入れると ${M`2\cos^2\alpha-1`}。`
]);

const p3 = HD(NO, 'Ⅱ　半角の 公式（次数を 下げる）', SEC) + `<div class="bd col st" style="gap:22px">
  <div class="q qline">Ⅰの 式の ${M`\alpha`} を ${M`x`} に かえて、${M`\sin^2x`}、${M`\cos^2x`}、${M`\sin x\cos x`} について 解く。</div>
  <div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:16px 24px">
    <div class="it"><div>${M`\cos2x=1-2\sin^2x`} より</div><div class="big" style="font-size:30px">❶ ${D`\sin^2x=`}${FILL(1, D`\frac{1-\cos2x}{2}`, 4)}</div></div>
    <div class="it"><div>${M`\cos2x=2\cos^2x-1`} より</div><div class="big" style="font-size:30px">❷ ${D`\cos^2x=`}${FILL(2, D`\frac{1+\cos2x}{2}`, 4)}</div></div>
    <div class="it"><div>${M`\sin2x=2\sin x\cos x`} より</div><div class="big" style="font-size:30px">❸ ${D`\sin x\cos x=`}${FILL(3, D`\frac{\sin2x}{2}`, 3)}</div></div>
  </div>
</div>` + CAP([
  `2乗や 積を、${M`\cos2x`} や ${M`\sin2x`}（1次）に 直す 形に します。`,
  `${M`2\sin^2x=1-\cos2x`}。両辺を ${M`2`} で 割ります。`,
  `${M`2\cos^2x=1+\cos2x`}。両辺を ${M`2`} で 割ります。`,
  `${M`\sin2x=2\sin x\cos x`} の 両辺を ${M`2`} で 割ります。`
]);

const CS = String.raw`\A{\cos\alpha\sin\beta}`;
const p4 = HD(NO, 'Ⅲ　積和の 公式 ❹', SEC) + `<div class="bd col st" style="gap:16px">
  <div class="calc" style="font-size:25px">
    <div>① ${M(String.raw`\sin(\alpha+\beta)=\sin\alpha\cos\beta+` + CS)}</div>
    <div>② ${M(String.raw`\sin(\alpha-\beta)=\sin\alpha\cos\beta-` + CS)}</div></div>
  <div class="q" style="font-size:26px;line-height:2.2">
    【①＋②】${M`\sin(\alpha+\beta)+\sin(\alpha-\beta)=`}${FILL(2, M`2\sin\alpha\cos\beta`, 6)}<br>
    <span data-s="3">左辺と 右辺を 入れかえて、両辺を 2 で 割ると</span><br>
    ${M`\sin\alpha\cos\beta=`}${FILL(3, M`\frac{1}{2}\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\}`, 12)}　…❹</div>
</div>` + CAP([
  `今度は、加法定理の ${M`\alpha+\beta`} と ${M`\alpha-\beta`} の 式を 使います。`,
  `①と②を たすと、<b class="a">${M`\cos\alpha\sin\beta`}</b> が 打ち消し合って 消えます。`,
  `右辺には ${M`\sin\alpha\cos\beta`} が 2つ 残ります。`,
  `入れかえて 2 で 割ると、積 ${M`\sin\alpha\cos\beta`} を 和で 表す 式 ❹ に なります。`
]);
const p5 = HD(NO, 'Ⅲ　積和の 公式 ❺・❻', SEC) + `<div class="bd col st" style="gap:16px">
  <div class="calc" style="font-size:25px">
    <div>③ ${M`\cos(\alpha+\beta)=\cos\alpha\cos\beta-\A{\sin\alpha\sin\beta}`}</div>
    <div>④ ${M`\cos(\alpha-\beta)=\cos\alpha\cos\beta+\A{\sin\alpha\sin\beta}`}</div></div>
  <div class="q" style="font-size:26px;line-height:2.3">
    【③＋④】${M`\cos(\alpha+\beta)+\cos(\alpha-\beta)=`}${FILL(1, M`2\cos\alpha\cos\beta`, 6)}　両辺を 2 で 割ると → ❺<br>
    【③－④】${M`\cos(\alpha+\beta)-\cos(\alpha-\beta)=`}${FILL(2, M`-2\sin\alpha\sin\beta`, 6)}　両辺を ${FILL(3, M`-2`, 2)} で 割ると → ❻</div>
</div>` + CAP([
  `③と④（${M`\cos`} の 加法定理）を 使います。`,
  `たすと ${M`\sin\alpha\sin\beta`} が 消えて、${M`2\cos\alpha\cos\beta`}。2 で 割れば ❺。`,
  `ひくと ${M`\cos\alpha\cos\beta`} が 消えて、${M`-\sin\alpha\sin\beta`} が 2つ。`,
  `${M`-2`} で 割ると ❻。マイナスが 付くのは この ためです。`
]);

const p6 = HD(NO, 'まとめ', SEC) + `<div class="bd" style="align-items:flex-start;gap:20px">
  <div class="l">${LIST()}</div><div class="l">${LIST2}</div>
</div>` + CAP([`④-3 では ❶〜❸ で 次数を 下げ、④-4 では ❹〜❻ で 積を 和に 直して 積分します。`]);

const DECK = {title:'④-2 半角の公式・積和の公式', pages:[
  {name:'表紙', html:p0}, {name:'これから 導く 公式', html:p1}, {name:'Ⅰ　2倍角の 公式', html:p2}, {name:'Ⅱ　半角の 公式', html:p3},
  {name:'Ⅲ　積和の 公式 ❹', html:p4}, {name:'Ⅲ　積和の 公式 ❺・❻', html:p5}, {name:'まとめ', html:p6},
]};
''')

# ---------------------------------------------------------------- ④-3 三角関数の不定積分（次数を 下げる）
DECKS['4-3_三角関数_次数を下げる'] = ('④-3 三角関数の不定積分（次数を下げる）', r'''
const NO = '④-3', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'三角関数の不定積分', sub:'2乗・積は 公式❶〜❸で 次数を 下げる'});
const F13 = BOX('次数を 下げる 公式（④-2）', `❶ ${D`\sin^2x=\frac{1-\cos2x}{2}`}　　❷ ${D`\cos^2x=\frac{1+\cos2x}{2}`}　　❸ ${D`\sin x\cos x=\frac{\sin2x}{2}`}`);

const p1 = HD(NO, '方針', SEC) + `<div class="bd col" style="gap:24px">
  <div class="q" style="font-size:27px">次数が 高く、置換積分・部分積分が 使えない ときは、<br>④-2 の 公式 ❶〜❸ で <b class="a">次数を 下げて</b> 積分する。</div>
  ${F13}
</div>` + CAP([`${M`\sin^2x`} の 積分の 公式は ありません。${M`\cos2x`}（1次）に 直せば、①-5 の 合成関数の 積分が 使えます。`]);

const p2 = gridPage({no:NO, sec:SEC, title:'例', q:'次の 不定積分を 求めよ。', items:[
  {tag:'⑴', q:String.raw`\int\sin^2x\,dx`, lines:[[1, String.raw`=\int\frac{1-\cos2x}{2}\,dx=\frac{1}{2}\int(1-\cos2x)\,dx`], [2, String.raw`=\frac{1}{2}\left(x-\frac{1}{2}\sin2x\right)+C`], [3, String.raw`=\DP{\frac{1}{2}x-\frac{1}{4}\sin2x+C}`]]},
  {tag:'⑵', q:String.raw`\int\sin x\cos x\,dx`, lines:[[4, String.raw`=\int\frac{1}{2}\sin2x\,dx`], [5, String.raw`=\frac{1}{2}\cdot\left(-\frac{1}{2}\cos2x\right)+C`], [6, String.raw`=\DP{-\frac{1}{4}\cos2x+C}`]]},
], cm:[
  `どちらも 公式で 次数を 下げてから 積分します。`,
  `⑴ 公式 ❶ で ${M`\sin^2x=\frac{1-\cos2x}{2}`}。${M`\frac{1}{2}`} を 前に 出します。`,
  `${M`\cos2x`} の 積分は ${M`\frac{1}{2}\sin2x`}（帳尻合わせ）。`,
  `かっこを はずして 答えます。`,
  `⑵ 公式 ❸ で ${M`\sin x\cos x=\frac{1}{2}\sin2x`}。`,
  `${M`\sin2x`} の 積分は ${M`-\frac{1}{2}\cos2x`}。`,
  `${M`\frac{1}{2}\cdot\left(-\frac{1}{2}\right)=-\frac{1}{4}`}。（置換積分 ${M`\sin x=t`} でも 解けます）`
]});

const p3 = gridPage({no:NO, sec:SEC, title:'問17', q:'次の 不定積分を 求めよ。', items:[
  {tag:'⑴', q:String.raw`\int\cos^2x\,dx`, o:1, lines:[[1, String.raw`=\int\frac{1+\cos2x}{2}\,dx`], [2, String.raw`=\DP{\frac{1}{2}x+\frac{1}{4}\sin2x+C}`]]},
  {tag:'⑵', q:String.raw`\int\sin^2 2x\,dx`, o:3, lines:[[3, String.raw`=\int\frac{1-\cos4x}{2}\,dx`], [4, String.raw`=\DP{\frac{1}{2}x-\frac{1}{8}\sin4x+C}`]]},
  {tag:'⑶', q:String.raw`\int(\sin x+\cos x)^2\,dx`, o:5, lines:[[5, String.raw`=\int(\sin^2x+2\sin x\cos x+\cos^2x)\,dx`], [6, String.raw`=\int(1+\sin2x)\,dx=\DP{x-\frac{1}{2}\cos2x+C}`]]},
], cm:[
  `公式で 次数を 下げてから 積分します。`,
  `⑴ 公式 ❷ で ${M`\cos^2x=\frac{1+\cos2x}{2}`}。`,
  `${M`\frac{1}{2}\int(1+\cos2x)\,dx=\frac{1}{2}\left(x+\frac{1}{2}\sin2x\right)`}。`,
  `⑵ 公式 ❶ の ${M`x`} を ${M`2x`} に かえると ${M`\sin^22x=\frac{1-\cos4x}{2}`}。`,
  `${M`\cos4x`} の 積分は ${M`\frac{1}{4}\sin4x`}。${M`\frac{1}{2}\cdot\frac{1}{4}=\frac{1}{8}`}。`,
  `⑶ まず 展開します。`,
  `${M`\sin^2x+\cos^2x=1`}、${M`2\sin x\cos x=\sin2x`}。${M`\sin2x`} の 積分は ${M`-\frac{1}{2}\cos2x`}。`
]});

const p4 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:24px">
  ${F13}
  <div class="sum">
    <span>${M`\sin^2x`}、${M`\cos^2x`}</span><span class="ar">→</span><span>❶・❷ で ${M`\cos2x`} の 式に</span>
    <span>${M`\sin x\cos x`}</span><span class="ar">→</span><span>❸ で ${M`\frac{1}{2}\sin2x`} に</span>
  </div>
</div>` + CAP([`④-4 では、積和の 公式 ❹〜❻ を 使って 積分します。`]);

const DECK = {title:'④-3 三角関数の不定積分（次数を下げる）', pages:[
  {name:'表紙', html:p0}, {name:'方針', html:p1}, {name:'例', html:p2}, {name:'問17', html:p3}, {name:'まとめ', html:p4},
]};
''')

# ---------------------------------------------------------------- ④-4 三角関数の不定積分（積を 和に）
DECKS['4-4_三角関数_積を和に'] = ('④-4 三角関数の不定積分（積を和に）', r'''
const NO = '④-4', SEC = '数学Ⅲ　積分法';
const p0 = coverSlide({kicker:'数学Ⅲ　積分法', no:NO, title:'三角関数の不定積分', sub:'積は 公式❹〜❻で 和・差に 直す'});
const F46 = BOX('積和の 公式（④-2）', `<div style="display:flex;flex-direction:column;gap:10px;line-height:1.5">
  <div>❹ ${D`\sin\alpha\cos\beta=\frac{1}{2}\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\}`}</div>
  <div>❺ ${D`\cos\alpha\cos\beta=\frac{1}{2}\{\cos(\alpha+\beta)+\cos(\alpha-\beta)\}`}</div>
  <div>❻ ${D`\sin\alpha\sin\beta=-\frac{1}{2}\{\cos(\alpha+\beta)-\cos(\alpha-\beta)\}`}</div></div>`);

const p1 = HD(NO, '方針', SEC) + `<div class="bd col" style="gap:20px">
  <div class="q" style="font-size:27px">三角関数の 積は、積和の 公式 ❹〜❻ で <b class="a">和・差に 直して から</b> 積分する。</div>
  ${F46}
</div>` + CAP([`${M`\sin3\theta\cos\theta`} のような 積は そのまま 積分できません。和に 直せば、1つずつ 積分できます。`]);

/* 左＝公式に あてはめる（α・β）、右＝計算 */
function pdPage(o){ return subPage({no:NO, sec:SEC, title:o.title, tag:o.tag, q:o.q, top:o.top, plabel:o.lab, prep:o.prep, calc:o.calc, cm:o.cm}); }
const Q = `<div class="q qline">次の 不定積分を 求めよ。</div>`;
const p2 = pdPage({title:'例', tag:'⑴', q:String.raw`\int\sin3\theta\cos\theta\,d\theta`, top:Q, lab:'公式 ❹ に あてはめる',
  prep:[[1, String.raw`\alpha=\A{3\theta},\ \beta=\B{\theta}`], [2, String.raw`\alpha+\beta=4\theta,\ \ \alpha-\beta=2\theta`]],
  calc:[[3, String.raw`=\int\frac{1}{2}(\sin4\theta+\sin2\theta)\,d\theta`], [4, String.raw`=\frac{1}{2}\left(-\frac{1}{4}\cos4\theta-\frac{1}{2}\cos2\theta\right)+C`], [5, String.raw`=\DP{-\frac{1}{8}\cos4\theta-\frac{1}{4}\cos2\theta+C}`]],
  cm:[`${M`\sin\times\cos`} の 積なので、公式 ❹ を 使います。`, `${M`\alpha=3\theta`}、${M`\beta=\theta`} と します。`, `${M`\alpha+\beta=4\theta`}、${M`\alpha-\beta=2\theta`}。`,
      `公式 ❹ で 和に 直します。`, `${M`\sin4\theta`} の 積分は ${M`-\frac{1}{4}\cos4\theta`}、${M`\sin2\theta`} は ${M`-\frac{1}{2}\cos2\theta`}。`, `${M`\frac{1}{2}`} を 掛けて 整理します。`]});

const p3 = pdPage({title:'問18　⑴', tag:'⑴', q:String.raw`\int\sin2\theta\cos\theta\,d\theta`, top:Q, lab:'公式 ❹ に あてはめる',
  prep:[[1, String.raw`\alpha=\A{2\theta},\ \beta=\B{\theta}`], [2, String.raw`\alpha+\beta=3\theta,\ \ \alpha-\beta=\theta`]],
  calc:[[3, String.raw`=\int\frac{1}{2}(\sin3\theta+\sin\theta)\,d\theta`], [4, String.raw`=\frac{1}{2}\left(-\frac{1}{3}\cos3\theta-\cos\theta\right)+C`], [5, String.raw`=\DP{-\frac{1}{6}\cos3\theta-\frac{1}{2}\cos\theta+C}`]],
  cm:[`例と 同じく 公式 ❹ です。`, `${M`\alpha=2\theta`}、${M`\beta=\theta`}。`, `${M`\alpha+\beta=3\theta`}、${M`\alpha-\beta=\theta`}。`, `和に 直します。`, `それぞれ 積分します。`, `${M`\frac{1}{2}`} を 掛けて 整理します。`]});
const p4 = pdPage({title:'問18　⑵', tag:'⑵', q:String.raw`\int\cos2x\cos x\,dx`, lab:'公式 ❺ に あてはめる',
  prep:[[1, String.raw`\alpha=\A{2x},\ \beta=\B{x}`], [2, String.raw`\alpha+\beta=3x,\ \ \alpha-\beta=x`]],
  calc:[[3, String.raw`=\int\frac{1}{2}(\cos3x+\cos x)\,dx`], [4, String.raw`=\DP{\frac{1}{6}\sin3x+\frac{1}{2}\sin x+C}`]],
  cm:[`${M`\cos\times\cos`} の 積なので、公式 ❺ です。`, `${M`\alpha=2x`}、${M`\beta=x`}。`, `${M`\alpha+\beta=3x`}、${M`\alpha-\beta=x`}。`, `和に 直します。`, `${M`\cos3x\to\frac{1}{3}\sin3x`}。${M`\frac{1}{2}\cdot\frac{1}{3}=\frac{1}{6}`}。`]});
const p5 = pdPage({title:'問18　⑶', tag:'⑶', q:String.raw`\int\sin4x\sin2x\,dx`, lab:'公式 ❻ に あてはめる',
  prep:[[1, String.raw`\alpha=\A{4x},\ \beta=\B{2x}`], [2, String.raw`\alpha+\beta=6x,\ \ \alpha-\beta=2x`]],
  calc:[[3, String.raw`=\int\left\{-\frac{1}{2}(\cos6x-\cos2x)\right\}dx`], [4, String.raw`=-\frac{1}{2}\left(\frac{1}{6}\sin6x-\frac{1}{2}\sin2x\right)+C`], [5, String.raw`=\DP{-\frac{1}{12}\sin6x+\frac{1}{4}\sin2x+C}`]],
  cm:[`${M`\sin\times\sin`} の 積なので、公式 ❻ です。マイナスに 注意。`, `${M`\alpha=4x`}、${M`\beta=2x`}。`, `${M`\alpha+\beta=6x`}、${M`\alpha-\beta=2x`}。`,
      `差に 直します。前に ${M`-\frac{1}{2}`} が 付きます。`, `${M`\cos6x\to\frac{1}{6}\sin6x`}、${M`\cos2x\to\frac{1}{2}\sin2x`}。`, `${M`-\frac{1}{2}`} を 掛けて 整理します。`]});

const p6 = HD(NO, 'まとめ', SEC) + `<div class="bd col" style="gap:20px">
  ${F46}
  <div class="q" style="font-size:26px">${M`\alpha`}、${M`\beta`} を 決めて ${M`\alpha+\beta`}、${M`\alpha-\beta`} を 計算 → 和・差に 直して 1つずつ 積分</div>
</div>` + CAP([`これで ④ の 三角関数の 積分は 終わりです。`]);

const DECK = {title:'④-4 三角関数の不定積分（積を和に）', pages:[
  {name:'表紙', html:p0}, {name:'方針', html:p1}, {name:'例', html:p2},
  {name:'問18　⑴', html:p3}, {name:'問18　⑵', html:p4}, {name:'問18　⑶', html:p5}, {name:'まとめ', html:p6},
]};
''')
