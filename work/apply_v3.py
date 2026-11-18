import re
SVG = open('work/plan-v3.svg.part', encoding='utf-8').read().rstrip('\n')
TOK_L = "--z-hyb:#CFE5C2; --z-met:#D7DEF0; --z-dry:#EEF1F3; --rigc:#7C8794;"
TOK_D = "--z-hyb:#22351C; --z-met:#232B44; --z-dry:#22272C; --rigc:#A7B0BA;"
PLAN_CSS = ".plan .hyb{fill:var(--z-hyb)} .plan .met{fill:var(--z-met)} .plan .dry{fill:var(--z-dry)}\n.plan .rigline{stroke:var(--rigc);stroke-width:4.5;stroke-linecap:round}\n"

def common(s):
    s, n = re.subn(r'    <svg viewBox="100 0 440 400".*?</svg>', lambda m: SVG, s, flags=re.S); assert n == 1, n
    parts = s.split('--z-rec:')
    assert len(parts) == 4, len(parts)
    s = parts[0] + TOK_L + ' --z-rec:' + parts[1] + TOK_D + ' --z-rec:' + parts[2] + TOK_D + ' --z-rec:' + parts[3]
    assert s.count('.plan .col{fill:var(--ink)}') == 1
    s = s.replace('.plan .col{fill:var(--ink)}', PLAN_CSS + '.plan .col{fill:var(--ink)}')
    return s

def rep(s, pairs, path=''):
    for a, b in pairs:
        n = s.count(a); assert n == 1, (path, n, a[:60]); s = s.replace(a, b)
    return s

def sub1(pattern, repl, s):
    s2, n = re.subn(pattern, lambda m: repl, s, flags=re.S); assert n == 1, (pattern[:40], n); return s2

# ---------------- INTERNAL ----------------
p = 'kyerim-internal.html'; s = common(open(p, encoding='utf-8').read())
s = rep(s, [
 ('<div class="fact"><span class="k">적자를 면하는 월 매출</span><span class="v num" data-o="beRev">–</span><span class="n" data-o="beMem">–</span></div>',
  '<div class="fact"><span class="k">신창만큼 남기며 낼 수 있는 최대 임대료</span><span class="v num" data-o="maxRent">–</span><span class="n">임대료 협상의 상한선 · 신창은 지금 660만원</span></div>'),
 ('<p class="prose muted small">형님 쪽에서 보면 임대료로 투자금을 돌려받는 데 <b class="num" data-o="payY">–</b>이 걸립니다(매출의 10% 임대료 가정). 돈 버는 투자로는 매력이 약하니, 형님이 이걸 제안한 이유는 다른 데 있을 가능성이 큽니다(→ <a href="#s3">형님 속내</a>).</p>',
  '<p class="prose muted small">형님 쪽에서 보면 매출의 10% 임대료로는 투자금을 돌려받는 데 <b class="num" data-o="payY">–</b>, 우리 상한선까지 올려도 <b class="num" data-o="payMax">–</b>이 걸립니다. 돈 버는 투자로는 매력이 약하니, 형님이 이걸 제안한 이유는 다른 데 있을 가능성이 큽니다(→ <a href="#s3">형님 속내</a>).</p>'),
 ('<li><b>회복실(사우나·냉탕)을 처음부터 할지</b><span>신고 문제가 있어 2단계를 권합니다(→ 공간·현장).</span></li>',
  '<li><b>회복실은 선택</b><span>예산이 커서 지금은 남녀 탈의실 사이에 자리만 남겨 둡니다.</span></li>'),
 ('<li><b>고정 월세가 높아 신창 수준 매출에서 남는 게 없을 때</b><span>계산기에서 「신창과 같음」으로 놓고 우리 순이익이 두 분이 정한 선 아래면 안 합니다.</span></li>',
  '<li><b>임대료가 상한선을 넘을 때</b><span>신창과 같은 매출에서 신창만큼(550만원) 남기려면 임대료는 최대 약 <b class="num" data-o="maxRent2">–</b>입니다. 그 위로는 신창보다 못한 지점을 하나 더 내는 셈입니다.</span></li>'),
 ('<p class="prose">기준은 <b>신창점 2026년 1~9월 평균</b>(월 매출 2,100만원, 고정비 1,450만원, 순이익 약 550만원)입니다. 다른 지점은 넣지 않았습니다. 막대를 밀면 오른쪽이 바로 바뀝니다.</p>',
  '<p class="prose">기준은 <b>신창점 2026년 1~9월 평균</b>입니다. 월 매출 2,100만원, 고정비 1,450만원(임대료 660만원 포함), 순이익 약 550만원이고, 다른 지점은 넣지 않았습니다. 막대를 밀면 오른쪽이 바로 바뀝니다.</p>'),
 ('<input type="range" id="O" min="900" max="2400" step="10" value="1450">\n          <span class="hint">신창 고정비 1,450만원을 그대로 넣었습니다. 신창 고정비에 임대료가 들어 있다면 그만큼 빼고, 계림이 넓어 늘어나는 관리비·전기료를 더하세요.</span>',
  '<input type="range" id="O" min="600" max="1800" step="10" value="1000">\n          <span class="hint">신창 1,450만원 − 임대료 660만원 = 790만원에서 시작했습니다. 여기에 ① 신창 계산에서 빠진 약 100만원(2,100 − 1,450 = 650인데 순이익은 550) ② 계림이 넓어 늘어날 관리비·전기 약 110만원(추정)을 더해 1,000만원입니다.</span>'),
 ('<label class="chk"><input type="checkbox" id="W"><span>회복실(사우나·냉탕) 포함<br><span class="hint">시공비 7,500만원과 월 운영비 120만원이 늘고, 회원 1인당 매출이 평균 1만원 오른다고 가정</span></span></label>',
  '<label class="chk"><input type="checkbox" id="W"><span>회복실 포함 (선택)<br><span class="hint">사우나·냉탕 공사 약 7,500만원, 월 운영비 120만원, 회원 1인당 매출 +1만원 가정</span></span></label>'),
 ('<span class="hint">추정 1.0~1.4억: 리그·바벨 플랫폼·덤벨·케이블 + 썰매·인조잔디·바이크·로잉·스키·케틀벨.</span>',
  '<span class="hint">추정: 리그 약 25m, 바벨·덤벨·케틀벨, 바이크, 로잉·스키, 썰매·인조잔디, 트레드밀. 트레드밀 대수에 따라 크게 달라져 견적이 필요합니다.</span>'),
 ('<label for="E">장비 (RIG + TURF)</label>', '<label for="E">장비 (Hyb + Met)</label>'),
 ('''        <div class="big3">
          <div><div class="k">개업 초기 우리 적자 (최대)</div><div class="v" data-o="wc3"></div><div class="n">이 돈을 메울 장치가 있어야 0원</div></div>
          <div><div class="k">적자 면하는 월 매출</div><div class="v" data-o="beRev2"></div><div class="n" data-o="beMem2"></div></div>
          <div><div class="k">형님 초기 투자</div><div class="v" data-o="capex"></div><div class="n" data-o="capexN"></div></div>
        </div>''',
  '''        <div class="big3 big4">
          <div><div class="k">개업 초기 우리 적자 (최대)</div><div class="v" data-o="wc3"></div><div class="n">이 돈을 메울 장치가 있어야 0원</div></div>
          <div><div class="k">신창만큼 남기는 최대 임대료</div><div class="v" data-o="maxRent3"></div><div class="n">이 위로는 신창보다 덜 남음</div></div>
          <div><div class="k">적자 면하는 월 매출</div><div class="v" data-o="beRev2"></div><div class="n" data-o="beMem2"></div></div>
          <div><div class="k">형님 초기 투자</div><div class="v" data-o="capex"></div><div class="n" data-o="capexN"></div></div>
        </div>'''),
 ('.big3 > div{border-top:1px solid var(--rule);padding-top:8px}', '.big4{grid-template-columns:repeat(2,minmax(0,1fr))}\n.big3 > div{border-top:1px solid var(--rule);padding-top:8px}'),
 ('<div class="card"><h3>참고할 사례</h3><p>건물주가 인테리어를 대고 수익을 나눈 공유오피스에서 정산 범위·공실 손실 공제로 분쟁이 난 보도가 있습니다(2026-08). 국내 헬스장 임대료 비율의 공개 기준은 없었고, 해외 피트니스 프랜차이즈 로열티가 매출의 8% 수준입니다.</p></div>',
  '<div class="card"><h3>비교할 숫자</h3><p><b>신창은 매출의 약 31%</b>(660만원, VAT 포함, 곧 700만원)를 임대료로 냅니다. 계림을 매출의 10%로 받으면 같은 매출에서 신창보다 월 약 340만원 더 남습니다. 참고로 건물주가 인테리어를 대고 수익을 나눈 공유오피스에서 정산 범위로 분쟁이 난 보도(2026-08)가 있고, 해외 피트니스 프랜차이즈 로열티는 매출의 8% 수준입니다.</p></div>'),
 ('<li><b class="num">고정비 1,450만원 → 순이익 약 550만원</b></li>',
  '<li><b class="num">고정비 1,450만원 → 순이익 약 550만원</b><span>고정비 안에 임대료 660만원(VAT 포함, 곧 700만원 인상 예정). 임대료를 뺀 운영비는 790만원</span></li>'),
 ('<div class="card"><h3>경력 코치를 빼 오면</h3>', '<div class="card"><h3>⚠ 숫자 하나 확인</h3><p>2,100 − 1,450 = <b>650만원</b>인데 순이익을 <b>550만원</b>으로 주셨습니다. 차이 100만원이 카드 수수료·부가세 같은 비용이면 계산기에 이미 넣은 그대로 맞고, 단순 착오면 계림 운영비를 900만원으로 낮추면 됩니다.</p></div>\n    <div class="card"><h3>경력 코치를 빼 오면</h3>'),
 ('<header><p class="eyebrow">공간 · 현장</p><h2>더야드짐 방식: RIG와 TURF를 나란히, 같은 타이머로</h2></header>\n  <p class="prose">호주에서 시작해 100곳 넘게 지점을 낸 더야드짐은 공간을 <b>RIG(근력)</b>와 <b>TURF(컨디셔닝)</b> 두 구역으로 나눕니다. 두 구역에서 서로 다른 수업이 <b>같은 타이머로 동시에</b> 돌아가고, 회복실(사우나·냉수욕)과 로비를 붙입니다. 계림은 내벽을 모두 철거하면 RIG와 TURF를 <b>각각 약 82평</b>으로 나란히 둘 수 있습니다. 미국 지점(약 90평)의 두 배 남짓입니다.</p>',
  '<header><p class="eyebrow">공간 · 현장</p><h2>Hyb 존과 Met 존 — 리그 한 줄로 나눕니다</h2></header>\n  <p class="prose">하이록스 수업과 크로스핏 수업을 <b>같은 시간에 각자의 존에서</b> 돌립니다. 사선 벽 쪽 띠가 <b>Hyb 존</b>(썰매 레인·트레드밀, 약 74평), 그 아래 삼각형이 <b>Met 존</b>(트인 바닥·바이크, 약 90평)이고, 두 존의 경계에 <b>리그(철봉) 약 25m</b>를 세웁니다. 경계선은 3번 기둥 모서리에서 7번 기둥 쪽으로 사선 벽과 거의 나란히 갑니다.</p>'),
 ('<p class="small muted">형광펜 구역 안의 내벽은 기둥만 남기고 전부 철거합니다. 새로 세우는 벽은 탈의·샤워와 회복실뿐이고, 로비·RIG·TURF는 한 판으로 트여 있습니다. 창고는 따로 두지 않고 통로 건너편 사무실을 씁니다.</p>',
  '<p class="small muted">형광펜 구역 안의 내벽은 기둥만 남기고 전부 철거합니다. 새로 세우는 벽은 남녀 탈의·샤워와 그 사이 회복실 자리뿐이고, 로비·Hyb·Met은 한 판으로 트여 있습니다. 회복실을 두게 되면 샤워실에서만 드나들게 해서 젖은 몸이 운동 바닥을 지나지 않습니다. 창고는 통로 건너편 사무실을 씁니다.</p>'),
 ('이 배치에서는 TURF 존의 머신 줄과 썰매 레인 사이 통로로 비워 두었습니다.', '이 배치에서는 트레드밀 줄 바로 오른쪽을 통로로 비워 두었습니다.'),
 ('<span>그래서 로비를 그 문 안에 두고, 탈의·샤워와 회복실을 같은 줄에 이어 「들어와서 씻고 쉬는 띠」로 만들었습니다. 운동은 그 위 한 판에서 합니다.</span>',
  '<span>그래서 로비를 그 문 안에 두고, 남녀 탈의·샤워를 같은 줄에 붙였습니다. 운동은 그 위 한 판에서 합니다. 로비에서 운동 바닥으로 가는 길은 바이크 왼쪽(약 5m 폭)입니다.</span>'),
 ('<div><em>현장에서 볼 것</em><b>바벨 떨어뜨리는 소리·진동</b><span>RIG 존 바벨 플랫폼 아래 방진 공사가 핵심입니다. 위층 1층 상가로 전달됩니다.</span></div>',
  '<div><em>현장에서 볼 것</em><b>바벨 떨어뜨리는 소리·진동</b><span>Met 존 바닥 방진 공사가 핵심입니다. 위층 1층 상가로 전달됩니다.</span></div>\n    <div><em>도면에서 본 것</em><b>리그가 5번 기둥(G열)을 스칩니다</b><span>그려 주신 선대로 놓으면 리그가 기둥 바로 옆(약 25cm)을 지나갑니다. 기둥을 리그 기둥 하나로 끼워 넣거나 리그를 두 토막으로 나누면 됩니다. 길이 25m 리그는 흔치 않아 제작 견적이 필요합니다.</span></div>'),
 ('<div><em>현장에서 물을 것</em><b>회복실 배수·전기</b><span>냉탕 공사는 방수·배수가 핵심이라 옛 화장실 배관 근처에 붙였습니다. 사우나 히터는 9~12kW급이라 전기 증설이 필요할 수 있습니다.</span></div>',
  '<div><em>현장에서 물을 것</em><b>샤워 배수</b><span>옛 화장실 배관이 남자 쪽에 있어, 여자 샤워실은 배수관을 새로 뽑아야 합니다. 아래층 천장으로 뺄 수 있는지 확인합니다.</span></div>'),
 ('<div><em>확인할 것</em><b>인허가 — 특히 회복실</b><span>체력단련장업 신고(운동전용면적 300㎡ 초과면 체육지도자 2명 이상). 건물이 판매시설이라 운동시설로 용도변경 또는 기재변경이 필요합니다. 사우나·냉탕은 회원 전용이어도 목욕장업 신고 대상으로 본 대법원 판례(2017도2793)가 있습니다. <b>부스가 아니라 공사로 사우나실·냉탕을 만들면 「목욕장 시설」로 볼 가능성이 더 큽니다.</b> 목욕장업으로 신고하면 다중이용업소 안전 기준이 붙을 수 있습니다. 동구청 위생과에 서면으로 묻고 2단계를 정합니다.</span></div>',
  '<div><em>확인할 것</em><b>인허가</b><span>체력단련장업 신고(운동전용면적 300㎡ 초과면 체육지도자 2명 이상). 건물이 판매시설이라 운동시설로 용도변경 또는 기재변경이 필요합니다. 회복실을 나중에 하게 되면 목욕장업 신고 대상인지 그때 구청에 묻습니다(회원 전용도 해당된 판례 있음).</span></div>'),
 ("const SIN = { rev: 2100, cost: 1450, net: 550 };", "const SIN = { rev: 2100, cost: 1450, rent: 660, net: 550 };"),
 ("low:  { R:1800, T:3, W:false, O:1450, Pr:10, Fr:0, RF:6, I:100, E:12000 },", "low:  { R:1800, T:3, W:false, O:1000, Pr:10, Fr:0, RF:6, I:100, E:12000 },"),
 ("base: { R:2100, T:2, W:false, O:1450, Pr:10, Fr:0, RF:6, I:100, E:12000 },", "base: { R:2100, T:2, W:false, O:1000, Pr:10, Fr:0, RF:6, I:100, E:12000 },"),
 ("high: { R:2650, T:2, W:true,  O:1500, Pr:10, Fr:0, RF:6, I:100, E:12000 }", "high: { R:2650, T:2, W:false, O:1050, Pr:10, Fr:0, RF:6, I:100, E:12000 }"),
 ('<button type="button" data-scen="high">신창 +25% · 회복실</button>', '<button type="button" data-scen="high">신창 +25%</button>'),
 ("    return { revM, rentM, netM, opex, capex, wc: -minOur, pay, beRev, beMem: Math.ceil(beRev / (PER_MEMBER * upl)), revS, ourS, hisS };",
  "    const maxRent = revM - opex - SIN.net;\n    const payMax = maxRent > 0 ? v.RF + Math.ceil(capex / maxRent) : Infinity;\n    return { revM, rentM, netM, opex, capex, wc: -minOur, pay, payMax, maxRent, beRev, beMem: Math.ceil(beRev / (PER_MEMBER * upl)), revS, ourS, hisS };"),
 ("    set('beRev2', fmt(r.beRev));", "    set('maxRent3', r.maxRent > 0 ? fmt(r.maxRent) : '없음');\n    set('beRev2', fmt(r.beRev));"),
 ("    set('beRev', fmt(r.beRev)); set('beMem', `회원 약 ${r.beMem}명 · 신창은 평균 191명`);",
  "    set('maxRent', fmt(r.maxRent)); set('maxRent2', fmt(r.maxRent)); set('payMax', years(r.payMax));"),
], p)
s = sub1(r'\s*<li><b>더야드짐</b>:.*?</li>', '', s)
open(p, 'w', encoding='utf-8').write(s); print('ok', p)

# ---------------- PITCH ----------------
p = 'kyerim-pitch.html'; s = common(open(p, encoding='utf-8').read())
s = rep(s, [
 ('<p class="lead">근력 구역 <b>RIG</b>와 컨디셔닝 구역 <b>TURF</b>를 한 판에 나란히 두고, 두 수업을 하나의 타이머로 동시에 돌리는 운동 공간을 제안드립니다. 회복실과 라운지까지 갖추고, 운영은 트레이닝판이 맡겠습니다.</p>',
  '<p class="lead"><b>하이록스</b>와 <b>크로스핏</b>을 한 공간에서 동시에. 벽을 털어 만든 한 판의 바닥을 리그 한 줄로 나눠, 두 수업이 같은 시간에 각자의 존에서 돌아가는 운동 공간을 제안드립니다. 운영은 트레이닝판이 맡겠습니다.</p>'),
 ('<div class="stat"><span class="v">82<small>평 ×2</small></span><span class="k">벽을 털고 나란히 놓는 RIG · TURF 두 구역</span></div>',
  '<div class="stat"><span class="v">2<small>개 존</small></span><span class="k">Hyb 존(하이록스) · Met 존(크로스핏), 리그 25m로 구분</span></div>'),
 ('.duo .rigc{border-top:5px solid #5D8DB3}\n.duo .turfc{border-top:5px solid #7FB565}', '.duo .hybc{border-top:5px solid #3E9A55}\n.duo .metc{border-top:5px solid #3A47A0}'),
 ('<header><p class="eyebrow">공간 구상</p><h2>들어와서 씻고 쉬는 띠, 그 위에 한 판의 운동 바닥</h2>', '<header><p class="eyebrow">공간 구상</p><h2>사선 벽 쪽은 Hyb, 그 아래는 Met, 경계에 리그</h2>'),
 ('<p class="small muted">안쪽 벽은 기둥만 남기고 전부 철거합니다. 새로 세우는 벽은 탈의·샤워와 회복실뿐이고, 로비·RIG·TURF는 한 판으로 트여 있습니다. 방화셔터가 내려오는 선은 비워 둡니다.</p>',
  '<p class="small muted">안쪽 벽은 기둥만 남기고 전부 철거합니다. 새로 세우는 벽은 남녀 탈의·샤워와 그 사이 회복실 자리뿐이고, 로비·Hyb·Met은 한 판으로 트여 있습니다. 방화셔터가 내려오는 선은 비워 둡니다.</p>'),
 ('<header><p class="eyebrow">무엇을 하나</p><h2>두 구역 수업, 그리고 회복과 모임</h2></header>', '<header><p class="eyebrow">무엇을 하나</p><h2>하이록스와 크로스핏, 그리고 모임</h2></header>'),
 ('<span class="eyebrow">1단계 · RIG + TURF</span>', '<span class="eyebrow">1단계 · Hyb + Met</span>'),
 ('<li>RIG·TURF 장비와 머신 (약 1.0~1.4억원)</li>', '<li>리그 약 25m, 썰매·인조잔디, 트레드밀·바이크·로잉·스키, 바벨·덤벨·케틀벨 (약 1.0~1.4억원, 트레드밀 대수에 따라)</li>'),
 ('<span class="eyebrow">2단계 · 회복실</span>', '<span class="eyebrow">2단계 · 회복실 (선택)</span>'),
 ('<p class="prose muted">1호점부터 4호점까지 직접 키워 온 수업과 관리 방식을, RIG·TURF라는 새 형식에 담아 운영합니다.</p>', '<p class="prose muted">1호점부터 4호점까지 직접 키워 온 크로스핏 수업과 관리 방식에 하이록스를 더해 운영합니다.</p>'),
 ('<div><h3>수업</h3><p>RIG·TURF 두 구역 프로그램을 짜고, 하이록스 대비반까지 운영합니다.</p></div>', '<div><h3>수업</h3><p>크로스핏과 하이록스 두 프로그램을 같은 시간표에 나란히 짜고, 하이록스 대회 준비반까지 운영합니다.</p></div>'),
], p)
s = sub1(r'<section id="concept">.*?</section>', '''<section id="concept">
  <header><p class="eyebrow">운영 방식</p><h2>하이록스와 크로스핏을, 같은 시간에 따로</h2>
  <p class="prose muted">한 시간에 두 수업이 동시에 열립니다. 회원은 그날 하이록스를 할지 크로스핏을 할지 골라 들어갑니다. 두 존 사이에는 벽 대신 리그(철봉 프레임)가 서 있어, 공간은 하나로 트여 있으면서 수업은 섞이지 않습니다.</p></header>
  <div class="duo">
    <div class="hybc"><span class="k">Hyb 존 · HYROX</span><span class="t">달리고 미는 존</span><p>사선 벽을 따라 썰매 레인 약 25m와 트레드밀 줄. 1km 달리기 8번과 운동 8가지를 번갈아 하는 하이록스를 그대로 연습합니다.</p><ul><li>하이록스 입문반 · 대회 준비반</li><li>썰매 밀기·끌기, 런지, 월볼</li><li>러닝 모임과 연결</li></ul></div>
    <div class="metc"><span class="k">Met 존 · CROSSFIT</span><span class="t">들고 당기는 존</span><p>리그와 트인 바닥에서 바벨·덤벨·케틀벨, 철봉, 바이크로 매일 바뀌는 크로스핏 수업을 합니다.</p><ul><li>매일 바뀌는 WOD</li><li>입문자 반 · 정규 반</li><li>1호점부터 해 온 중심 수업</li></ul></div>
    <div class="timerbar"><span class="clock">RIG 25m</span><span>두 존의 경계에 철봉 프레임 한 줄. 벽이 아니라서 시야는 트여 있고, 양쪽 수업이 모두 씁니다.</span></div>
  </div>
</section>''', s)
s = sub1(r'<div class="zones">.*?</div>\n</section>', '''<div class="zones">
    <div class="zone"><i style="background:var(--z-lobby)"></i><b>로비 · 라운지</b><span class="a">약 22평</span><p>주차장 통로에서 들어오는 서쪽 문 바로 안. 전실(이중문), 데스크, 물 마시는 곳, 수업 전후 머무는 벤치.</p></div>
    <div class="zone"><i style="background:var(--z-hyb)"></i><b>Hyb 존 · 하이록스</b><span class="a">약 74평</span><p>사선 벽을 따라 썰매 레인 약 25m, 방화셔터 선 옆 트레드밀 줄. 로잉·스키는 리그에 걸어 두 존이 같이 씁니다.</p></div>
    <div class="zone"><i style="background:var(--z-met)"></i><b>Met 존 · 크로스핏</b><span class="a">약 90평</span><p>리그 아래 트인 바닥, 바이크 여러 대, 동쪽 벽 장비 랙. 바닥은 방진 고무.</p></div>
    <div class="zone"><i style="background:var(--z-lock)"></i><b>남 · 여 탈의·샤워</b><span class="a">각 약 12평</span><p>탈의실 안쪽에 샤워. 운동 바닥에서 바로 들어갑니다.</p></div>
    <div class="zone"><i style="background:var(--z-rec)"></i><b>회복실 자리 (선택)</b><span class="a">약 12평</span><p>남녀 샤워실 사이. 나중에 사우나·냉탕을 두면 샤워실에서만 드나들어 젖은 몸이 운동 바닥을 지나지 않습니다.</p></div>
    <div class="zone"><i style="background:var(--z-ctx)"></i><b>사무실</b><span class="a">약 9평</span><p>통로 건너편. 장비·물품 창고로 씁니다.</p></div>
  </div>
</section>''', s)
s = sub1(r'<div class="progs">.*?</div>\n</section>', '''<div class="progs">
    <div class="prog"><span class="stage">Hyb 존</span><h3>하이록스</h3><span class="who">달리기·기록 운동을 좋아하는 분</span><p>1km 달리기 8번과 운동 8가지를 번갈아 하는 실내 피트니스 레이스입니다. 썰매 레인과 트레드밀로 대회 코스를 그대로 연습합니다. 입문반과 대회 준비반을 운영합니다.</p></div>
    <div class="prog"><span class="stage">Met 존</span><h3>크로스핏</h3><span class="who">20~40대 직장인 · 새벽·점심·저녁</span><p>매일 바뀌는 고강도 그룹 수업입니다. 코치가 동작 하나하나를 봐 줍니다. 1호점부터 해 온 중심 수업입니다.</p></div>
    <div class="prog"><span class="stage">두 존 함께</span><h3>같은 시간, 두 수업</h3><span class="who">회원이 그날 고름</span><p>같은 시간대에 하이록스와 크로스핏이 나란히 열립니다. 한 회원권으로 두 수업을 오갈 수 있어 지루할 틈이 없습니다.</p></div>
    <div class="prog"><span class="stage">1단계부터</span><h3>커뮤니티</h3><span class="who">회원 · 동네</span><p>주말 단체 운동, 러닝 모임, 동네 하이록스 기록회. 라운지가 이 모임의 거점이 됩니다.</p></div>
  </div>
</section>''', s)
open(p, 'w', encoding='utf-8').write(s); print('ok', p)
