# -*- coding: utf-8 -*-
import re

with open('work/plan.svg', 'r', encoding='utf-8') as f:
    plan_svg_content = f.read()

plan_svg_content = re.sub(r'<svg[^>]+>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" class="w-full h-auto max-h-[460px] mx-auto select-none">', plan_svg_content, count=1)

pitch_html = f'''<!doctype html>
<html lang="ko" class="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>계림동 지하 1층 운동공간 제안서 — 트레이닝판</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
  darkMode: 'class',
  theme: {{
    extend: {{
      colors: {{
        brand: {{ 50: '#fff7ed', 100: '#ffedd5', 500: '#f97316', 600: '#ea580c', 700: '#c2410c' }},
        dark: {{ bg: '#0b0f17', card: '#131926', border: '#232d42', surface: '#1a2234' }}
      }},
      fontFamily: {{
        sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'Apple SD Gothic Neo', 'Noto Sans KR', 'sans-serif'],
        mono: ['SF Mono', 'ui-monospace', 'Menlo', 'Consolas', 'monospace']
      }}
    }}
  }}
}}
</script>
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
body {{ font-feature-settings: "cv02", "cv03", "cv04", "cv11"; }}
</style>
</head>
<body class="bg-dark-bg text-slate-100 font-sans antialiased selection:bg-brand-500 selection:text-white min-h-screen">

<!-- Top Bar -->
<header class="sticky top-0 z-50 backdrop-blur-md bg-dark-bg/85 border-b border-dark-border px-4 lg:px-8 py-3.5">
  <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
    <div class="flex items-center gap-3">
      <a href="index.html" class="flex items-center gap-2 group">
        <span class="w-8 h-8 rounded-lg bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center font-black text-black text-base shadow-lg shadow-brand-500/20 group-hover:scale-105 transition">P</span>
        <div>
          <span class="font-bold text-base tracking-tight text-white group-hover:text-brand-500 transition">트레이닝판</span>
          <span class="text-xs text-slate-400 block -mt-1 font-mono">공간 기획 제안서</span>
        </div>
      </a>
      <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-brand-500/10 text-brand-500 border border-brand-500/30">의장님 미팅용</span>
    </div>

    <nav class="flex items-center gap-2 text-xs sm:text-sm font-medium">
      <a href="#vision" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">공간 비전</a>
      <a href="#program" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">프로그램</a>
      <a href="#layout" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">평면 구상도</a>
      <a href="#value" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">수익 모델</a>
      <a href="#roadmap" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">추진 일정</a>
      <a href="index.html" class="ml-2 px-3 py-1.5 rounded-lg bg-dark-surface text-slate-300 hover:text-white border border-dark-border transition">허브 ↗</a>
    </nav>
  </div>
</header>

<main class="max-w-6xl mx-auto px-4 lg:px-8 py-10 space-y-16 sm:space-y-24">

  <!-- Hero Section -->
  <section id="vision" class="relative rounded-3xl p-8 sm:p-14 bg-gradient-to-br from-dark-card via-dark-card to-dark-surface border border-dark-border shadow-2xl overflow-hidden text-center sm:text-left">
    <div class="absolute -top-32 -right-32 w-[500px] h-[500px] bg-brand-500/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="relative z-10 max-w-3xl space-y-6">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-500/10 border border-brand-500/30 text-brand-400 text-xs font-bold tracking-wide">
        광주 동구 중앙로 358 · 구 이마트 건물 지하 1층 230평
      </div>
      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white leading-[1.15]">
        비어 있던 지하 230평을,<br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-500 via-amber-400 to-amber-200">매일 100명이 찾는 랜드마크로</span>
      </h1>
      <p class="text-base sm:text-xl text-slate-300 leading-relaxed font-light">
        글로벌 메가트렌드 <b class="text-white font-bold">하이록스(HYROX)</b>와 정통 <b class="text-white font-bold">크로스핏</b>을 한 공간에서 동시에.<br class="hidden sm:inline">
        건물 가치를 극대화하고, <span class="text-brand-400 font-semibold underline decoration-brand-500 decoration-2 underline-offset-4">공실 월세 0원 공간에서 매달 안정적인 고수익</span>을 창출하는 전문 위탁운영을 제안드립니다.
      </p>

      <!-- Key Numbers -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-6">
        <div class="bg-dark-bg/60 border border-dark-border rounded-2xl p-4 text-left">
          <div class="text-xs text-slate-400 font-mono">전체 면적</div>
          <div class="text-3xl font-black text-white font-mono mt-1">230<span class="text-base font-normal text-slate-400 ml-1">평</span></div>
          <div class="text-[11px] text-slate-500 mt-1">기둥 간격 8m 탁 트인 바닥</div>
        </div>
        <div class="bg-dark-bg/60 border border-dark-border rounded-2xl p-4 text-left">
          <div class="text-xs text-slate-400 font-mono">동시 듀얼 클래스</div>
          <div class="text-3xl font-black text-brand-500 font-mono mt-1">2<span class="text-base font-normal text-slate-400 ml-1">개 존</span></div>
          <div class="text-[11px] text-slate-500 mt-1">하이록스 존 + 크로스핏 존</div>
        </div>
        <div class="bg-dark-bg/60 border border-dark-border rounded-2xl p-4 text-left">
          <div class="text-xs text-slate-400 font-mono">썰매 트랙 레인</div>
          <div class="text-3xl font-black text-emerald-400 font-mono mt-1">25<span class="text-base font-normal text-slate-400 ml-1">m</span></div>
          <div class="text-[11px] text-slate-500 mt-1">사선벽 활용 광주 최장 길이</div>
        </div>
        <div class="bg-dark-bg/60 border border-dark-border rounded-2xl p-4 text-left">
          <div class="text-xs text-slate-400 font-mono">일일 유동 회원</div>
          <div class="text-3xl font-black text-sky-400 font-mono mt-1">100<span class="text-base font-normal text-slate-400 ml-1">명+</span></div>
          <div class="text-[11px] text-slate-500 mt-1">등록 150~200명 유치 목표</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Why This Space -->
  <section class="space-y-6">
    <div class="border-b border-dark-border pb-4">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Space Feasibility</div>
      <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">운동 시설에 완벽하게 부합하는 지하 공간</h2>
      <p class="text-sm text-slate-400 mt-1">일반 상가로는 활용하기 어려웠던 구조가 피트니스에는 압도적인 차별점이 됩니다.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      <div class="bg-dark-card border border-dark-border rounded-2xl p-6 space-y-3">
        <div class="w-10 h-10 rounded-xl bg-brand-500/10 text-brand-500 flex items-center justify-center font-bold text-lg">01</div>
        <h3 class="text-lg font-bold text-white">160평 넘는 트인 바닥</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          내부 칸막이벽을 철거하고 기둥만 남기면 운동 바닥이 한 판으로 열립니다. 기둥 간격이 약 8m로 넓어 하이록스 스테이션과 크로스핏 바닥을 시원하게 구획할 수 있습니다.
        </p>
      </div>

      <div class="bg-dark-card border border-dark-border rounded-2xl p-6 space-y-3">
        <div class="w-10 h-10 rounded-xl bg-brand-500/10 text-brand-500 flex items-center justify-center font-bold text-lg">02</div>
        <h3 class="text-lg font-bold text-white">사선 벽 → 25m 잔디 썰매 레인</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          어색했던 비스듬한 바깥벽을 따라 약 25m의 직진 썰매 레인이 완성됩니다. 일반 도심 피트니스에서는 설계하기 어려운 전국 최상급 하이록스 규격입니다.
        </p>
      </div>

      <div class="bg-dark-card border border-dark-border rounded-2xl p-6 space-y-3">
        <div class="w-10 h-10 rounded-xl bg-brand-500/10 text-brand-500 flex items-center justify-center font-bold text-lg">03</div>
        <h3 class="text-lg font-bold text-white">지하주차장 직결 비 안 맞는 출입</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          차를 대고 지하 통로를 지나면 곧바로 출입구입니다. 이른 새벽과 늦은 저녁, 비나 눈이 와도 쾌적하게 드나들 수 있어 차량 이용 회원의 선호도가 압도적입니다.
        </p>
      </div>
    </div>
  </section>

  <!-- Program Strategy -->
  <section id="program" class="space-y-6">
    <div class="border-b border-dark-border pb-4">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Dual Program Concept</div>
      <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">하이록스와 크로스핏, 같은 시간에 따로</h2>
      <p class="text-sm text-slate-400 mt-1">한 시간표 안에서 두 가지 클래스가 동시에 돌아가며 공간 가동률을 200%로 끌어올립니다.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="bg-dark-card border border-emerald-500/30 rounded-2xl p-6 sm:p-8 space-y-4 relative overflow-hidden bg-gradient-to-br from-dark-card to-emerald-500/5">
        <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 font-mono">
          ZONE 01 · 약 74평
        </div>
        <h3 class="text-2xl font-black text-white">Hyb 존 (하이록스)</h3>
        <p class="text-xs text-slate-300 leading-relaxed">
          글로벌 피트니스 레이스 하이록스(HYROX) 공식 트레이닝 존입니다. 25m 잔디 썰매 트랙, 무동력 트레드밀, 스키에르그, 샌드백 런지 등 유산소 및 기능성 근지구력 훈련을 집중 운영합니다.
        </p>
        <ul class="text-xs text-slate-400 space-y-1.5 pt-2">
          <li>• 초보자·여성도 부상 없이 즐기는 달리기+소도구 프로그램</li>
          <li>• 국내외 하이록스 대회 준비반 및 주말 시뮬레이션 이벤트</li>
        </ul>
      </div>

      <div class="bg-dark-card border border-brand-500/30 rounded-2xl p-6 sm:p-8 space-y-4 relative overflow-hidden bg-gradient-to-br from-dark-card to-brand-500/5">
        <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full text-xs font-bold bg-brand-500/20 text-brand-400 font-mono">
          ZONE 02 · 약 90평
        </div>
        <h3 class="text-2xl font-black text-white">Met 존 (크로스핏)</h3>
        <p class="text-xs text-slate-300 leading-relaxed">
          역도, 체조, 고강도 인터벌 트레이닝이 펼쳐지는 정통 크로스핏 공간입니다. 바벨 드랍 전용 방음 바닥과 25m 커스텀 리그, 에어바이크, 로잉머신을 완비하여 커뮤니티 파워를 극대화합니다.
        </p>
        <ul class="text-xs text-slate-400 space-y-1.5 pt-2">
          <li>• 1호점~4호점을 통해 검증된 트레이닝판 공인 WOD 시스템</li>
          <li>• 체계적인 레벨별 코칭으로 장기 재등록율 80% 이상 견인</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Floor Plan Layout -->
  <section id="layout" class="space-y-4">
    <div class="border-b border-dark-border pb-3">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Floor Plan Visualization</div>
      <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">230평 공간 배치 및 동선 설계</h2>
      <p class="text-xs sm:text-sm text-slate-400 mt-0.5">사선 벽 쪽 Hyb 존과 메인 Met 존을 중앙 리그 한 줄로 분리한 구상도입니다.</p>
    </div>

    <div class="bg-dark-card border border-dark-border rounded-2xl p-4 sm:p-6 overflow-hidden">
      {plan_svg_content}
    </div>
  </section>

  <!-- Business Model & Owner Value -->
  <section id="value" class="space-y-6">
    <div class="border-b border-dark-border pb-4">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Business Model & ROI</div>
      <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">위탁운영 파트너십 — 의장님이 얻는 확실한 가치</h2>
      <p class="text-sm text-slate-400 mt-1">공실 상태와 비교할 수 없는 수익성과 자산 가치 상승을 보장합니다.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="bg-dark-card border border-dark-border rounded-2xl p-6 space-y-4">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-brand-500"></span>
          수익 분배 구조 (순수익 60% : 40%)
        </h3>
        <p class="text-xs text-slate-300 leading-relaxed">
          의장님이 해당 층 소유자이시므로 <b class="text-white">보증금과 월세는 발생하지 않습니다.</b>
          매출에서 실운영비(코치 인건비+관리비+소모품)만 실비로 차감하고, 남은 <span class="text-brand-400 font-bold">순수익의 60%를 의장님</span>께서 가져가십니다.
        </p>

        <div class="bg-dark-surface/60 border border-dark-border p-4 rounded-xl space-y-2 text-xs">
          <div class="flex justify-between text-slate-300">
            <span>목표 등록 회원 수</span>
            <span class="font-mono font-bold text-white">150명</span>
          </div>
          <div class="flex justify-between text-slate-300">
            <span>예상 월 총매출 (1인 14만 기준)</span>
            <span class="font-mono font-bold text-white">2,100만원</span>
          </div>
          <div class="flex justify-between text-slate-400">
            <span>월 고정 실운영비 (월세 0원, 코치 660만)</span>
            <span class="font-mono font-bold text-rose-400">− 1,000만원</span>
          </div>
          <div class="pt-2 border-t border-dark-border flex justify-between font-bold text-sm text-sky-400">
            <span>의장님 월 몫 (순수익의 60%)</span>
            <span class="font-mono text-base">매달 600 ~ 700만원!</span>
          </div>
        </div>
        <p class="text-[11px] text-slate-400">
          * 일반 상가 임대료(월 300~400만원 선) 대비 약 1.5~2배의 높은 순수익을 지속적으로 창출합니다.
        </p>
      </div>

      <div class="bg-dark-card border border-dark-border rounded-2xl p-6 space-y-4">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
          의장님의 4대 핵심 이점
        </h3>
        <ul class="space-y-3 text-xs text-slate-300">
          <li class="flex items-start gap-2.5">
            <span class="text-emerald-400 font-bold">1.</span>
            <div><b class="text-white">건물 전체 자산가치 극대화</b>: 하루 100여 명이 지하로 드나들며 공실 상가가 건물 전체를 살리는 앵커 테넌트가 됩니다.</div>
          </li>
          <li class="flex items-start gap-2.5">
            <span class="text-emerald-400 font-bold">2.</span>
            <div><b class="text-white">본인 건설사 원가 시공</b>: 인테리어 공사를 의장님 회사에서 직접 맡아 시공 마진 확보 및 원가 절감이 가능합니다.</div>
          </li>
          <li class="flex items-start gap-2.5">
            <span class="text-emerald-400 font-bold">3.</span>
            <div><b class="text-white">운영 리스크 ZERO</b>: 복잡한 코치 채용, 프로그램 기획, 회원 CS, 마케팅은 트레이닝판이 100% 전담합니다.</div>
          </li>
          <li class="flex items-start gap-2.5">
            <span class="text-emerald-400 font-bold">4.</span>
            <div><b class="text-white">투자금 조기 회수 후 영구 수익</b>: 순수익의 60%를 통해 인테리어/장비 원금을 약 3~4년 내 회수하고 이후 순이익을 영구 수취합니다.</div>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- 2 Stage Roadmap -->
  <section id="roadmap" class="space-y-6">
    <div class="border-b border-dark-border pb-4">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Launch Roadmap</div>
      <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">2단계 오픈 및 일정 로드맵</h2>
      <p class="text-sm text-slate-400 mt-1">초기 투자 부담을 줄이기 위해 체육관 메인을 먼저 열고, 회복실을 2단계로 진행합니다.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="p-6 rounded-2xl bg-dark-card border border-brand-500/40 space-y-3">
        <div class="flex items-center justify-between">
          <span class="px-2.5 py-0.5 rounded bg-brand-500 text-black text-xs font-black">1단계 · 메인 오픈 (필수)</span>
          <span class="text-xs font-mono text-brand-400">2027년 1~3월 목표</span>
        </div>
        <h4 class="text-xl font-bold text-white">체육관 및 기본 샤워실</h4>
        <ul class="text-xs text-slate-300 space-y-1.5 pt-1">
          <li>• 내부 칸막이벽 철거 및 오픈 플로어 바닥 조성</li>
          <li>• 25m 잔디 썰매 트랙 + 고무블럭 + 25m 커스텀 리그</li>
          <li>• 남녀 탈의실 및 기본 샤워 부스 시공</li>
          <li>• 사전 등록 프로모션 진행 (새해 운동 성수기 오픈)</li>
        </ul>
      </div>

      <div class="p-6 rounded-2xl bg-dark-card border border-dark-border space-y-3">
        <div class="flex items-center justify-between">
          <span class="px-2.5 py-0.5 rounded bg-dark-surface text-slate-300 text-xs font-semibold">2단계 · 회복실 확장 (선택)</span>
          <span class="text-xs font-mono text-slate-400">오픈 안정화 후 추진</span>
        </div>
        <h4 class="text-xl font-bold text-slate-300">사우나실 & 냉탕 시설</h4>
        <ul class="text-xs text-slate-400 space-y-1.5 pt-1">
          <li>• 탈의실 사이 유보 공간에 사우나 및 냉탕 시공</li>
          <li>• 방수·배관·전기 증설 및 관할 구청 인허가 확인</li>
          <li>• 회원 수 150명 달성 및 운영 안정 후 투자 검토</li>
        </ul>
      </div>
    </div>

    <!-- Timeline Steps -->
    <div class="pt-6">
      <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 text-center">
        <div class="p-3.5 bg-dark-card border border-dark-border rounded-xl space-y-1">
          <div class="text-[10px] text-brand-400 font-mono font-bold">STEP 01</div>
          <div class="text-xs font-bold text-white">현장 실사 & 미팅</div>
          <div class="text-[10px] text-slate-500">천장·공조·조건 합의</div>
        </div>
        <div class="p-3.5 bg-dark-card border border-dark-border rounded-xl space-y-1">
          <div class="text-[10px] text-brand-400 font-mono font-bold">STEP 02</div>
          <div class="text-xs font-bold text-white">위탁 계약 체결</div>
          <div class="text-[10px] text-slate-500">40:60 순수익 배분 확정</div>
        </div>
        <div class="p-3.5 bg-dark-card border border-dark-border rounded-xl space-y-1">
          <div class="text-[10px] text-brand-400 font-mono font-bold">STEP 03</div>
          <div class="text-xs font-bold text-white">설계 및 인테리어</div>
          <div class="text-[10px] text-slate-500">약 2~3개월 (의장님 회사)</div>
        </div>
        <div class="p-3.5 bg-dark-card border border-dark-border rounded-xl space-y-1">
          <div class="text-[10px] text-brand-400 font-mono font-bold">STEP 04</div>
          <div class="text-xs font-bold text-white">사전 등록 & 코치 채용</div>
          <div class="text-[10px] text-slate-500">오픈 1개월 전 모집</div>
        </div>
        <div class="p-3.5 bg-brand-500/10 border border-brand-500/40 rounded-xl space-y-1 col-span-2 sm:col-span-1">
          <div class="text-[10px] text-brand-400 font-mono font-bold">STEP 05</div>
          <div class="text-xs font-bold text-brand-300">그랜드 오픈!</div>
          <div class="text-[10px] text-brand-400 font-mono">2027년 초 목표</div>
        </div>
      </div>
    </div>
  </section>

</main>

<footer class="border-t border-dark-border bg-dark-card/50 py-10 px-4 text-center text-xs text-slate-500 font-mono space-y-2">
  <p>광주 계림동 지하 1층 운동공간 기획 제안서 · 트레이닝판 (TRAININGPAN)</p>
  <p>© 2026 TRAININGPAN. ALL RIGHTS RESERVED.</p>
</footer>

</body>
</html>
'''

with open('kyerim-pitch.html', 'w', encoding='utf-8') as f:
    f.write(pitch_html)

print("Finished generating new kyerim-pitch.html. Size:", len(pitch_html))
