# -*- coding: utf-8 -*-

budget_html = '''<!doctype html>
<html lang="ko" class="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>계림점 운영 예산 & 손익 계산기 — 위탁운영 (40:60)</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: { 50: '#fff7ed', 100: '#ffedd5', 500: '#f97316', 600: '#ea580c', 700: '#c2410c' },
        dark: { bg: '#0b0f17', card: '#131926', border: '#232d42', surface: '#1a2234' }
      },
      fontFamily: {
        sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'Apple SD Gothic Neo', 'Noto Sans KR', 'sans-serif'],
        mono: ['SF Mono', 'ui-monospace', 'Menlo', 'Consolas', 'monospace']
      }
    }
  }
}
</script>
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
body { font-feature-settings: "cv02", "cv03", "cv04", "cv11"; }
input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
</style>
</head>
<body class="bg-dark-bg text-slate-100 font-sans antialiased selection:bg-brand-500 selection:text-white min-h-screen">

<!-- Header -->
<header class="sticky top-0 z-50 backdrop-blur-md bg-dark-bg/85 border-b border-dark-border px-4 lg:px-8 py-3.5">
  <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
    <div class="flex items-center gap-3">
      <a href="index.html" class="flex items-center gap-2 group">
        <span class="w-8 h-8 rounded-lg bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center font-black text-black text-base shadow-lg shadow-brand-500/20 group-hover:scale-105 transition">P</span>
        <div>
          <span class="font-bold text-base tracking-tight text-white group-hover:text-brand-500 transition">트레이닝판</span>
          <span class="text-xs text-slate-400 block -mt-1 font-mono">운영 예산 & 손익 계산기</span>
        </div>
      </a>
      <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-brand-500/10 text-brand-500 border border-brand-500/30">순수익 40:60</span>
      <span class="hidden md:inline-block px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">보증금·월세 0원</span>
    </div>

    <nav class="flex items-center gap-2 text-xs sm:text-sm font-medium">
      <a href="#opex" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">월 운영비</a>
      <a href="#calc" class="px-3 py-1.5 rounded-lg bg-brand-500/20 text-brand-400 font-semibold border border-brand-500/30 hover:bg-brand-500/30 transition">손익 계산기</a>
      <a href="#capex" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">초기 장비비</a>
      <a href="index.html" class="ml-2 px-3 py-1.5 rounded-lg bg-dark-surface text-slate-300 hover:text-white border border-dark-border transition">허브 ↗</a>
    </nav>
  </div>
</header>

<main class="max-w-7xl mx-auto px-4 lg:px-8 py-8 space-y-10">

  <!-- Overview Strip -->
  <section class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="bg-dark-card border border-dark-border rounded-2xl p-5 space-y-1">
      <span class="text-xs text-slate-400 font-medium">월 고정 실운영비 합계</span>
      <div class="text-3xl font-black font-mono text-white mt-1" id="sOpex">1,000만원</div>
      <span class="text-xs text-emerald-400 flex items-center gap-1 font-medium mt-1">
        <span>✓</span> 의장님 층 소유로 월세 0원 (인건비 660만 포함)
      </span>
    </div>

    <div class="bg-dark-card border border-dark-border rounded-2xl p-5 space-y-1">
      <span class="text-xs text-slate-400 font-medium">초기 투입 장비/비품 예산</span>
      <div class="text-3xl font-black font-mono text-sky-400 mt-1" id="sCapex">1.2억원</div>
      <span class="text-xs text-slate-400 mt-1">의장님 100% 구매·소유 (상환 의무 없음)</span>
    </div>

    <div class="bg-gradient-to-br from-brand-500/15 via-dark-card to-dark-surface border border-brand-500/40 rounded-2xl p-5 space-y-1">
      <div class="flex justify-between items-center">
        <span class="text-xs text-brand-400 font-bold">회원 150명 시 우리 성과급 (40%)</span>
        <span class="text-[10px] px-1.5 py-0.5 rounded bg-brand-500 text-black font-black">월간</span>
      </div>
      <div class="text-3xl font-black font-mono text-brand-400 mt-1" id="sOurs">400 ~ 550만원</div>
      <span class="text-xs text-slate-300 mt-1">코치 전원 고용 + 리스크 0원 순성과</span>
    </div>
  </section>

  <!-- Interactive Profit Calculator -->
  <section id="calc" class="bg-dark-card border border-brand-500/30 rounded-2xl p-6 sm:p-8 space-y-6">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-border pb-4">
      <div>
        <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Live Formula Calculator</div>
        <h2 class="text-xl sm:text-2xl font-bold text-white mt-0.5">순수익 및 40:60 성과급 계산기</h2>
      </div>
      <span class="text-xs text-slate-400 font-mono bg-dark-surface px-3 py-1 rounded-lg border border-dark-border">
        순수익 = 매출(수수료 차감 후) − 월 실운영비
      </span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
      <div class="space-y-1.5 bg-dark-surface p-3.5 rounded-xl border border-dark-border">
        <label for="cMembers" class="text-xs font-semibold text-slate-300 block">목표 인원수 (명)</label>
        <input type="number" id="cMembers" value="150" step="5" class="w-full bg-dark-bg border border-dark-border rounded-lg px-3 py-2 text-right font-mono font-bold text-lg text-brand-400 focus:outline-none focus:border-brand-500">
        <span class="text-[10px] text-slate-500 block text-right font-mono">신창 평균 191명</span>
      </div>

      <div class="space-y-1.5 bg-dark-surface p-3.5 rounded-xl border border-dark-border">
        <label for="cPrice" class="text-xs font-semibold text-slate-300 block">회원권 월단가 (만원)</label>
        <input type="number" id="cPrice" value="14" step="0.5" class="w-full bg-dark-bg border border-dark-border rounded-lg px-3 py-2 text-right font-mono font-bold text-lg text-brand-400 focus:outline-none focus:border-brand-500">
        <span class="text-[10px] text-slate-500 block text-right font-mono">실입금 평균 14만원</span>
      </div>

      <div class="space-y-1.5 bg-dark-surface p-3.5 rounded-xl border border-dark-border">
        <label for="cFee" class="text-xs font-semibold text-slate-300 block">카드수수료·부가세 (%)</label>
        <input type="number" id="cFee" value="4.8" step="0.1" class="w-full bg-dark-bg border border-dark-border rounded-lg px-3 py-2 text-right font-mono font-bold text-lg text-slate-300 focus:outline-none focus:border-brand-500">
        <span class="text-[10px] text-slate-500 block text-right font-mono">평균 공제율 4.8%</span>
      </div>

      <div class="space-y-1.5 bg-dark-surface p-3.5 rounded-xl border border-dark-border">
        <label for="cPct" class="text-xs font-semibold text-slate-300 block">우리 성과급 비율 (%)</label>
        <input type="number" id="cPct" value="40" step="5" class="w-full bg-dark-bg border border-dark-border rounded-lg px-3 py-2 text-right font-mono font-bold text-lg text-brand-400 focus:outline-none focus:border-brand-500">
        <span class="text-[10px] text-slate-500 block text-right font-mono">확정안 40% (의장님 60%)</span>
      </div>
    </div>

    <!-- Output Dashboard -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 pt-2">
      <div class="bg-dark-bg/80 border border-dark-border p-3.5 rounded-xl space-y-1">
        <span class="text-[11px] text-slate-400 block">월 총매출</span>
        <span class="text-lg font-bold font-mono text-white block" id="oGross">-</span>
        <span class="text-[10px] text-slate-500 block" id="oNet">-</span>
      </div>

      <div class="bg-dark-bg/80 border border-dark-border p-3.5 rounded-xl space-y-1">
        <span class="text-[11px] text-slate-400 block">월 실운영비</span>
        <span class="text-lg font-bold font-mono text-rose-400 block" id="oOpexCalc">1,000만원</span>
        <span class="text-[10px] text-emerald-400 block">월세 0원</span>
      </div>

      <div class="bg-dark-bg/80 border border-dark-border p-3.5 rounded-xl space-y-1">
        <span class="text-[11px] text-slate-400 block">월 순수익 (이익)</span>
        <span class="text-lg font-bold font-mono text-white block" id="oProfit">-</span>
        <span class="text-[10px] text-slate-500 block">분배 전 영업이익</span>
      </div>

      <div class="bg-brand-500/10 border border-brand-500/40 p-3.5 rounded-xl space-y-1">
        <span class="text-[11px] text-brand-300 font-bold block">우리 성과급 (40%)</span>
        <span class="text-xl font-black font-mono text-brand-400 block" id="oOurShare">-</span>
        <span class="text-[10px] text-slate-400 block">트레이닝판 순수익</span>
      </div>

      <div class="bg-sky-500/10 border border-sky-500/40 p-3.5 rounded-xl space-y-1">
        <span class="text-[11px] text-sky-300 font-bold block">의장님 몫 (60%)</span>
        <span class="text-xl font-black font-mono text-sky-400 block" id="oHisShare">-</span>
        <span class="text-[10px] text-slate-400 block">공실 대비 고수익</span>
      </div>

      <div class="bg-dark-bg/80 border border-dark-border p-3.5 rounded-xl space-y-1">
        <span class="text-[11px] text-slate-400 block">손익분기점 (BEP)</span>
        <span class="text-lg font-bold font-mono text-amber-400 block" id="oBep">-</span>
        <span class="text-[10px] text-slate-500 block">이 이상이면 흑자</span>
      </div>
    </div>
  </section>

  <!-- Monthly Operating Costs (OPEX) Table -->
  <section id="opex" class="space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-border pb-3">
      <div>
        <h2 class="text-xl font-bold text-white">월 고정 실운영비 상세 (OPEX)</h2>
        <p class="text-xs text-slate-400 mt-0.5">매달 계림점 통장에서 나가는 실운영비입니다. 의장님이 해당 층 소유자이므로 보증금과 월 임대료는 0원입니다.</p>
      </div>
      <div class="text-sm font-mono font-bold text-brand-400 bg-dark-card px-3 py-1.5 rounded-xl border border-dark-border">
        합계: <span id="opexSum">1,000만원</span> / 월
      </div>
    </div>

    <div class="bg-dark-card border border-dark-border rounded-2xl overflow-hidden">
      <table class="w-full text-left text-xs sm:text-sm">
        <thead class="bg-dark-surface/80 text-slate-400 font-mono border-b border-dark-border">
          <tr>
            <th class="py-3 px-4">항목</th>
            <th class="py-3 px-4">구성 내역</th>
            <th class="py-3 px-4 text-right">월 금액 (만원)</th>
            <th class="py-3 px-4">비고</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-dark-border/60 text-slate-300">
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">헤드코치 인건비</td>
            <td class="py-3 px-4">수업 메인 총괄 코치 1명 채용 (기본급 + 4대보험)</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">380</td>
            <td class="py-3 px-4 text-slate-400">전원 채용 · 현장 책임 코치</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">어시스턴트 코치 인건비</td>
            <td class="py-3 px-4">파트타임/세컨 코치 1~2명 (새벽·저녁 피크타임 수업)</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">280</td>
            <td class="py-3 px-4 text-slate-400">하이록스 & 크로스핏 동시 진행</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">건물 관리비 및 공과금</td>
            <td class="py-3 px-4">지하 230평 기본 관리비 + 전기·수도·공조비</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">300</td>
            <td class="py-3 px-4 text-slate-400">실비 정산 (샤워실·냉난방 가동)</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">센터 운영 소모품 & 비품</td>
            <td class="py-3 px-4">탄막, 청소용품, 구급함, 테이핑, 음향, 통신비</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">25</td>
            <td class="py-3 px-4 text-slate-400">매달 소모되는 물품 실비</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">지역 마케팅 & 프로모션</td>
            <td class="py-3 px-4">계림동 인근 네이버 플레이스 광고, 인스타그램 홍보</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">15</td>
            <td class="py-3 px-4 text-slate-400">신규 회원 유치용 기본 집행비</td>
          </tr>
          <tr class="bg-emerald-500/5 font-semibold">
            <td class="py-3 px-4 text-emerald-400">월 임대료 (월세)</td>
            <td class="py-3 px-4 text-emerald-400">의장님이 해당 층 소유자이므로 임대료 지출 없음</td>
            <td class="py-3 px-4 text-right font-mono text-emerald-400">0</td>
            <td class="py-3 px-4 text-emerald-400">신창점(660만 지출) 대비 절대적 강점</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- Initial Capex Equipment Table -->
  <section id="capex" class="space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-border pb-3">
      <div>
        <h2 class="text-xl font-bold text-white">초기 투입 장비 및 비품 목록 (CAPEX)</h2>
        <p class="text-xs text-slate-400 mt-0.5">오픈 전에 한 번 구매하는 장비입니다. 의장님이 100% 투자·소유하며, 우리는 상환하지 않습니다.</p>
      </div>
      <div class="text-sm font-mono font-bold text-sky-400 bg-dark-card px-3 py-1.5 rounded-xl border border-dark-border">
        합계: 약 1.2억원 (의장님 투자)
      </div>
    </div>

    <div class="bg-dark-card border border-dark-border rounded-2xl overflow-hidden">
      <table class="w-full text-left text-xs sm:text-sm">
        <thead class="bg-dark-surface/80 text-slate-400 font-mono border-b border-dark-border">
          <tr>
            <th class="py-3 px-4">분류</th>
            <th class="py-3 px-4">주요 품목</th>
            <th class="py-3 px-4">규격 및 수량</th>
            <th class="py-3 px-4 text-right">예상 예산 (만원)</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-dark-border/60 text-slate-300">
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">유산소 머신</td>
            <td class="py-3 px-4">무동력 트레드밀, 에어바이크, 컨셉2 로잉머신, 스키에르그</td>
            <td class="py-3 px-4">총 14~16대 (하이록스 공식 스펙)</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">4,200</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">리그 및 바닥재</td>
            <td class="py-3 px-4">25m 맞춤형 철봉 리그 스테이션, 인조잔디 썰매트랙, 50T 고무블럭</td>
            <td class="py-3 px-4">25m 리그 + 160평 바닥재 일체</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">3,500</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">바벨 & 프리웨이트</td>
            <td class="py-3 px-4">공인 올림픽 바벨(남/녀), 범퍼플레이트, 덤벨 세트, 케틀벨</td>
            <td class="py-3 px-4">약 20세트 및 플레이트 1.5톤</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">2,000</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">소도구 & 하이록스</td>
            <td class="py-3 px-4">무게 썰매(Sled) 2대, 샌드백, 월볼, 플라이오 박스, 저항 밴드</td>
            <td class="py-3 px-4">수업 인원 30명 동시 수용 분량</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">1,100</td>
          </tr>
          <tr class="hover:bg-dark-surface/30">
            <td class="py-3 px-4 font-bold text-white">전산·음향·가전</td>
            <td class="py-3 px-4">입출결 키오스크, 프로 사운드 앰프/스피커, 제습기, 냉온수기, PC</td>
            <td class="py-3 px-4">지하층 전용 대형 제습/음향 설비</td>
            <td class="py-3 px-4 text-right font-mono font-semibold text-white">1,200</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

</main>

<footer class="border-t border-dark-border bg-dark-card/50 py-8 px-4 text-center text-xs text-slate-500 font-mono space-y-2">
  <p>광주 계림동 운동공간 운영 예산서 · 트레이닝판 (TRAININGPAN)</p>
  <p>© 2026 TRAININGPAN. ALL RIGHTS RESERVED.</p>
</footer>

<script>
(function(){
  const $ = id => document.getElementById(id);
  const fmt = v => Math.round(v).toLocaleString('ko-KR') + '만원';

  function calculate(){
    const members = parseFloat($('cMembers').value) || 0;
    const price = parseFloat($('cPrice').value) || 0;
    const feePct = parseFloat($('cFee').value) || 0;
    const ourPct = parseFloat($('cPct').value) || 0;
    const opex = 1000; // 고정 실운영비 1,000만원

    const gross = members * price;
    const net = gross * (1 - feePct / 100);
    const profit = net - opex;

    const ourShare = profit > 0 ? profit * (ourPct / 100) : 0;
    const hisShare = profit > 0 ? profit * ((100 - ourPct) / 100) : profit;
    const bepMembers = Math.ceil(opex / (price * (1 - feePct / 100)));

    $('oGross').textContent = fmt(gross);
    $('oNet').textContent = '실입금 ' + fmt(net);
    $('oProfit').textContent = (profit >= 0 ? '+' : '−') + fmt(Math.abs(profit));
    $('oOurShare').textContent = fmt(ourShare);
    $('oHisShare').textContent = (hisShare >= 0 ? '+' : '−') + fmt(Math.abs(hisShare));
    $('oBep').textContent = isFinite(bepMembers) ? bepMembers + '명' : '-';
    $('sOurs').textContent = fmt(ourShare);
  }

  ['cMembers', 'cPrice', 'cFee', 'cPct'].forEach(id => {
    $(id).addEventListener('input', calculate);
  });

  calculate();
})();
</script>
</body>
</html>
'''

with open('kyerim-budget.html', 'w', encoding='utf-8') as f:
    f.write(budget_html)

print("Finished generating new kyerim-budget.html. Size:", len(budget_html))
