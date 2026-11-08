"""練習プリント「x軸との共有点」①〜⑧（16問）の 解説スライド（2026-11-08）。
プリントは 非公開リポジトリの 数学Ⅰ/練習プリント/（make_renshu.js の PICK と 同じ 並び）。
1問 1ページ。作りは ②-1・②-2 の プリント問題と 同じ（decks_kimatsu2.py の XCOMMON：XQF 因数分解・XQQ 解の公式・XQJ 重解・XQN 解なし）。
解の公式で 重解（③⑴ 4x² − 4x ＋ 1）だけ XQJF を ここで 足す（XQN の 配置で ルートの中が 0）。"""
import os
B = os.path.dirname(os.path.abspath(__file__))

JSR = r'''
const KKR = KIMATSU + '　練習プリント';
const POLR = `<div class="fpol"><div class="fa math">y ＝ 0 と する</div><div class="fv">解の 個数 ＝ 共有点の 個数</div><div class="fb" style="font-size:24px;font-weight:900">16問 チャレンジ</div></div>`;
/* 解の公式で 重解（ルートの中が 0）：XQN と 同じ 配置 */
const XQJF = P => ptSlide({clip:[56,278,510,472],
  svg:[BG([154.8,305.7,197.1,331.2],'xpb'), BG([73.2,333.7,211.7,384.5],'xpb'), BG([107.8,386.9,211.7,437.7],'xpb'), BG([181.2,442.5,246.4,468],'xpk'),
       BG([435.7,281.1,505.6,324.5],'xpr'), BG([435.7,329.4,505.7,358.2],'xpr'), BG([404.9,363.9,505.6,455.2],'xpr'),
       BRC(308.6,386,6), AX(421.4),
       PB({xv:455, yv:421.4, q:0.045, ay:421.4, top:369, s:9, dot:'f', ds:8, ls:10, lab:[[455,P.xl]]})],
  items:[
    T([61.6,308.5,154,325.5],`${P.num}<span class="xsp"></span>${P.eq}`,10.2),
    T([109.8,333.7,118.5,384.5],'=',12,'ac xeqp'), T([109.8,386.9,118.5,437.7],'=',12,'ac xeqp'),
    ...LBL(305.7),
    {s:1, r:[201,307,294,330], h:`<span class="ytag">y ＝ 0 と する</span>`, fs:10.5, cls:'xyt'},
    XA(2,[154.8,305.7,197.1,331.2],'＝ 0',12,'xan xeq0'),
    XA(3,[73.2,333.7,109.8,384.5],'x',12,'xan xr'), XA(3,[118.5,333.7,211.7,384.5],KF(`${P.mb} ± ${SQ(P.in1)}`,P.den),11,'xan xl'),
    XA(4,[118.5,386.9,211.7,437.7],P.x2b,10,'xan xl'),
    XA(5,[181.2,442.5,246.4,468],'重解',12,'xja xred'),
    XA(6,[435.7,281.1,505.6,324.5],P.x,13), XA(7,[435.7,329.4,505.7,358.2],'1 個',13)],
  done:10,
  cm:[
    `${P.num} ${M(P.eqm)} と x軸との 共有点を 求めよう。`,
    `x軸との 共有点 なので <b>y ＝ 0</b> と する。`,
    `式の 右に <b>＝ 0</b>。　${M(P.eq0)}。　${P.how}`,
    `<b>解の公式</b>。　${P.abcT} を 入れる。`,
    `${P.c4}`,
    `ルートの中が 0 → 解は 1つ だけ → <b>重解</b>。`,
    `共有点の <b>x座標</b> は ${P.xm}。`,
    `解が 1つ → 共有点も <b>1個</b>。`,
    `グラフの 概形。　x軸に 共有点を 1つ 打つ。`,
    `下に凸。　x軸に <b>接する</b> ように かく。`,
    `点の 下に x座標 ${P.xm} を 書く。　<b>完成！</b>`]}) + ptag(P.tag);

const LEADR = '次の 2次関数の グラフと x軸との 共有点の x座標と 個数を 求め、グラフの 概形を 書け。';
const RH = (no, title, list, cap) => probHead(`練習プリント${no}`, LEADR, list, cap || `<b>練習プリント${no}</b>「${title}」。　まず 自分で 解いてから 見てね。`).replace('例の 次は', title);
const t = n => `練習プリント${n}`;
const Q = (q, tag) => ({...q, tag});
const KR = (n,d) => KF(n,d);
const PR = [
 ['①', 'まずは 2問（因数分解・解の公式）', [
  XQF({tag:t('①'), num:'⑴', eq:`y ＝ x${P2} − 4x ＋ 3`, eqm:'y ＝ x² − 4x ＋ 3', eq0:'x² − 4x ＋ 3 ＝ 0', how:'たして −4、かけて ＋3',
    fac:'(x − 1)(x − 3)', xs:'1, 3', r:['1','3']}),
  XQQ({tag:t('①'), num:'⑵', eq:`y ＝ x${P2} − 3x ＋ 1`, eqm:'y ＝ x² − 3x ＋ 1', eq0:'x² − 3x ＋ 1 ＝ 0', how:'たして −3、かけて ＋1',
    abcT:'a ＝ 1、b ＝ −3、c ＝ 1', mb:'3', in1:'9 − 4', den:'2', x2:KR(`3 ± ${SQ('5')}`,'2'),
    rl:KR(`3 − ${SQ('5')}`,'2'), rr:KR(`3 ＋ ${SQ('5')}`,'2'), c4:`${M('9 − 4 ＝ 5')}。　${M('x ＝ (3 ± √5)/2')}。`})]],
 ['②', '解の公式で 解く（1）', [
  XQQ({tag:t('②'), num:'⑴', eq:`y ＝ x${P2} ＋ 5x ＋ 3`, eqm:'y ＝ x² ＋ 5x ＋ 3', eq0:'x² ＋ 5x ＋ 3 ＝ 0', how:'たして ＋5、かけて ＋3',
    abcT:'a ＝ 1、b ＝ 5、c ＝ 3', mb:'−5', in1:'25 − 12', den:'2', x2:KR(`−5 ± ${SQ('13')}`,'2'),
    rl:KR(`−5 − ${SQ('13')}`,'2'), rr:KR(`−5 ＋ ${SQ('13')}`,'2'), c4:`${M('25 − 12 ＝ 13')}。　${M('x ＝ (−5 ± √13)/2')}。`}),
  XQQ({tag:t('②'), num:'⑵', eq:`y ＝ x${P2} − x − 3`, eqm:'y ＝ x² − x − 3', eq0:'x² − x − 3 ＝ 0', how:'たして −1、かけて −3',
    abcT:'a ＝ 1、b ＝ −1、c ＝ −3', mb:'1', in1:'1 ＋ 12', den:'2', x2:KR(`1 ± ${SQ('13')}`,'2'),
    rl:KR(`1 − ${SQ('13')}`,'2'), rr:KR(`1 ＋ ${SQ('13')}`,'2'), c4:`${M('1 ＋ 12 ＝ 13')}。　${M('x ＝ (1 ± √13)/2')}。`})]],
 ['③', '解の公式で 解く（2）重解・解なし', [
  XQJF({tag:t('③'), num:'⑴', eq:`y ＝ 4x${P2} − 4x ＋ 1`, eqm:'y ＝ 4x² − 4x ＋ 1', eq0:'4x² − 4x ＋ 1 ＝ 0', how:'x² の 前が 4 → <b>解の公式</b> で 解く。',
    abcT:'a ＝ 4、b ＝ −4、c ＝ 1', mb:'4', in1:'16 − 16', den:'8', x2b:`${KR(`4 ± ${SQ('0')}`,'8')} ＝ ${KR('4','8')} ＝ ${KR('1','2')}`,
    x:KR('1','2'), xl:'1/2', xm:M('1/2'), c4:`${M('16 − 16 ＝ 0')}。　${M('√0 ＝ 0')} なので ${M('x ＝ 4/8 ＝ 1/2')}。`}),
  XQN({tag:t('③'), num:'⑵', eq:`y ＝ x${P2} ＋ 3x ＋ 4`, eqm:'y ＝ x² ＋ 3x ＋ 4', eq0:'x² ＋ 3x ＋ 4 ＝ 0',
    abcT:'a ＝ 1、b ＝ 3、c ＝ 4', mb:'−3', in1:'9 − 16', in2:'−7', den:'2'})]],
 ['④', '因数分解で 解く（1）', [
  XQF({tag:t('④'), num:'⑴', eq:`y ＝ x${P2} − 1`, eqm:'y ＝ x² − 1', eq0:'x² − 1 ＝ 0', how:'2乗 − 2乗',
    fac:'(x ＋ 1)(x − 1)', xs:'−1, 1', r:['−1','1']}),
  XQF({tag:t('④'), num:'⑵', eq:`y ＝ x${P2} ＋ 2x`, eqm:'y ＝ x² ＋ 2x', eq0:'x² ＋ 2x ＝ 0', how:'共通な x で くくる',
    fac:'x(x ＋ 2)', xs:'−2, 0', r:['−2','0']})]],
 ['⑤', '因数分解で 解く（2）', [
  XQJ({tag:t('⑤'), num:'⑴', eq:`<span style="font-size:.88em">y ＝ x${P2} − 8x ＋ 16</span>`, eqm:'y ＝ x² − 8x ＋ 16', eq0:'x² − 8x ＋ 16 ＝ 0',
    how:'たして −8、かけて ＋16', fac:`(x − 4)${P2}`, x:'4'}),
  XQF({tag:t('⑤'), num:'⑵', eq:`y ＝ x${P2} ＋ x − 6`, eqm:'y ＝ x² ＋ x − 6', eq0:'x² ＋ x − 6 ＝ 0', how:'たして ＋1、かけて −6',
    fac:'(x ＋ 3)(x − 2)', xs:'−3, 2', r:['−3','2']})]],
 ['⑥', '因数分解と 解の公式', [
  XQF({tag:t('⑥'), num:'⑴', eq:`y ＝ x${P2} − x − 6`, eqm:'y ＝ x² − x − 6', eq0:'x² − x − 6 ＝ 0', how:'たして −1、かけて −6',
    fac:'(x ＋ 2)(x − 3)', xs:'−2, 3', r:['−2','3']}),
  XQN({tag:t('⑥'), num:'⑵', eq:`y ＝ x${P2} − 3x ＋ 5`, eqm:'y ＝ x² − 3x ＋ 5', eq0:'x² − 3x ＋ 5 ＝ 0',
    abcT:'a ＝ 1、b ＝ −3、c ＝ 5', mb:'3', in1:'9 − 20', in2:'−11', den:'2'})]],
 ['⑦', 'いろいろな 形', [
  XQF({tag:t('⑦'), num:'⑴', eq:`y ＝ 3x${P2} − 5x`, eqm:'y ＝ 3x² − 5x', eq0:'3x² − 5x ＝ 0', how:'共通な x で くくる',
    fac:'x(3x − 5)', xs:`0, ${KR('5','3')}`, r:['0','5/3']}),
  XQQ({tag:t('⑦'), num:'⑵', eq:`y ＝ x${P2} ＋ 4x − 2`, eqm:'y ＝ x² ＋ 4x − 2', eq0:'x² ＋ 4x − 2 ＝ 0', how:'たして ＋4、かけて −2',
    abcT:'a ＝ 1、b ＝ 4、c ＝ −2', mb:'−4', in1:'16 ＋ 8', den:'2', sud:24,
    x2b:`${KR(`−${RDX('4','2',4)} ± ${RDX('2','1',4)}${SQ('6')}`, RDX('2','1',4,true))} <span class="vm">＝ −2 ± ${SQ('6')}</span>`, x2:`−2 ± ${SQ('6')}`,
    rl:`−2 − ${SQ('6')}`, rr:`−2 ＋ ${SQ('6')}`, c4:`${M('16 ＋ 8 ＝ 24')}。　24 を すだれ算 → ${M('√24 ＝ 2√6')}。　2 で 約分 して ${M('x ＝ −2 ± √6')}。`})]],
 ['⑧', 'たすき掛けでも 解ける', [
  XQQ({tag:t('⑧'), num:'⑴', eq:`<span style="font-size:.88em">y ＝ 2x${P2} ＋ 5x ＋ 2</span>`, eqm:'y ＝ 2x² ＋ 5x ＋ 2', eq0:'2x² ＋ 5x ＋ 2 ＝ 0',
    cm2:`式の 右に <b>＝ 0</b>。　${M('2x² ＋ 5x ＋ 2 ＝ 0')}。　x² の 前が 2 → 解の公式で 解く（たすき掛けでも できる）。`,
    abcT:'a ＝ 2、b ＝ 5、c ＝ 2', mb:'−5', in1:'25 − 16', den:'4',
    x2b:`${KR('−5 ± 3','4')} ＝ −2, −${KR('1','2')}`, x2:`−2, −${KR('1','2')}`, rl:'−2', rr:`−${KR('1','2')}`,
    c4:`${M('25 − 16 ＝ 9')}、${M('√9 ＝ 3')}。　${M('(−5 − 3)/4 ＝ −2')}、${M('(−5 ＋ 3)/4 ＝ −1/2')}。　（別解：${M('(2x ＋ 1)(x ＋ 2) ＝ 0')}）`}),
  XQQ({tag:t('⑧'), num:'⑵', eq:`<span style="font-size:.88em">y ＝ 3x${P2} − 5x − 2</span>`, eqm:'y ＝ 3x² − 5x − 2', eq0:'3x² − 5x − 2 ＝ 0',
    cm2:`式の 右に <b>＝ 0</b>。　${M('3x² − 5x − 2 ＝ 0')}。　x² の 前が 3 → 解の公式で 解く（たすき掛けでも できる）。`,
    abcT:'a ＝ 3、b ＝ −5、c ＝ −2', mb:'5', in1:'25 ＋ 24', den:'6',
    x2b:`${KR('5 ± 7','6')} ＝ 2, −${KR('1','3')}`, x2:`−${KR('1','3')}, 2`, rl:`−${KR('1','3')}`, rr:'2',
    c4:`${M('25 ＋ 24 ＝ 49')}、${M('√49 ＝ 7')}。　${M('(5 ＋ 7)/6 ＝ 2')}、${M('(5 − 7)/6 ＝ −1/3')}。　（別解：${M('(3x ＋ 1)(x − 2) ＝ 0')}）`})]]];
const EQS = [['y ＝ x² − 4x ＋ 3','y ＝ x² − 3x ＋ 1'],['y ＝ x² ＋ 5x ＋ 3','y ＝ x² − x − 3'],['y ＝ 4x² − 4x ＋ 1','y ＝ x² ＋ 3x ＋ 4'],['y ＝ x² − 1','y ＝ x² ＋ 2x'],
  ['y ＝ x² − 8x ＋ 16','y ＝ x² ＋ x − 6'],['y ＝ x² − x − 6','y ＝ x² − 3x ＋ 5'],['y ＝ 3x² − 5x','y ＝ x² ＋ 4x − 2'],['y ＝ 2x² ＋ 5x ＋ 2','y ＝ 3x² − 5x − 2']];
/* ① の あと：②〜⑧ は 演習（1枚ずつ 解く → 先生に 丸つけ。わからない ときは ＱＲ コードの ヒント。先生の 指示 11/8） */
const QRI = `<img class="ex8qr" src="@@QRHINT@@" alt="ヒントの ＱＲ コード">`;   // プリントと 同じ ＱＲ（ヒントの ページ）。build の とき 画像を 埋めこむ
const EXS = (s, n, t, sub, extra='') => `<div class="ex8s lh" data-s="${s}"><div class="ex8n">${n}</div><div class="ex8t">${t}</div><div class="ex8b">${sub}</div>${extra}</div>`;
const EX8 = `
  <div class="card abs dcard v2 ex8card">${EQTAPE}
    <div class="ex8h"><span class="v2mk">② 〜 ⑧ は 演習</span></div>
    <div class="ex8row">
      ${EXS(1, '1', '1枚ずつ 解く', '② から 順に　1枚 2問')}
      ${EXS(2, '2', '先生に 丸つけ', '解けたら 見せに 行く')}
      ${EXS(3, '3', 'どんどん 次へ', '終わったら 次の 1枚')}
    </div>
    <div class="ex8hb lh" data-s="4">
      <div class="ex8hl"><div class="ex8n">？</div><div><div class="ex8t">わからない とき</div>
        <div class="ex8b">プリントの ＱＲ コード → ヒント</div>
        <div class="ex8hint">参考に する プリントの Ｎｏ．・例 ／ 解き方の 途中まで</div></div></div>
      ${QRI}
    </div>
  </div>`;   // 「いま やっていること」は 置かない（先生の 指示 11/8）
const PGR = [{name:'表紙', html:coverF(KKR, '<span class="mk">x軸</span>との<br>共有点', '練習プリント ①〜⑧', 'y ＝ 0 と して 解く！', POLR, '16問')}];
PR.forEach(([no, title, qs], i) => {
  PGR.push({name:`${no} ${title}`, html:RH(no, title, EQS[i].map((e,j)=>`${'⑴⑵'[j]} ${e}`))});
  qs.forEach((h,j) => PGR.push({name:`${no}${'⑴⑵'[j]}`, html:h}));
  if(i===0) PGR.push({name:'演習の 進め方', html:EX8});
});
PGR.push({name:'終', html:endF(KKR + '　x軸との共有点', POLR)});
const DECK = {title:'練習プリント x軸との共有点', pages:PGR};
'''

def add(decks):
    import decks_kimatsu2 as k2
    import base64
    # プリント（非公開の 数学Ⅰ/練習プリント/img/qr_hint.png）と 同じ ＱＲ。読むと 公開の ヒントの ページ（期末考査/renshu/x軸との共有点_ヒント.html）
    qr = base64.b64encode(open(os.path.join(B, 'renshu_qr_hint.png'), 'rb').read()).decode()
    decks['練習_x軸との共有点'] = ('練習プリント x軸との共有点', k2.COMMON + k2.XCOMMON + JSR.replace('@@QRHINT@@', 'data:image/png;base64,' + qr))
