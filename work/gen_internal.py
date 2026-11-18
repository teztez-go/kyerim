# -*- coding: utf-8 -*-
import re

with open('work/plan.svg', 'r', encoding='utf-8') as f:
    plan_svg_content = f.read()

# Make the SVG responsive
plan_svg_content = re.sub(r'<svg[^>]+>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" class="w-full h-auto max-h-[460px] mx-auto select-none">', plan_svg_content, count=1)

internal_html = f'''<!doctype html>
<html lang="ko" class="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>계림점 내부 판단 전략 노트 — 위탁운영 (40:60)</title>
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
input[type=range] {{ accent-color: #f97316; }}
.tab-active {{ border-bottom: 2px solid #f97316; color: #f97316; font-weight: 700; }}
svg .g {{ stroke: #232d42; stroke-width: 1; }}
svg .ax {{ fill: #64748b; font-size: 11px; font-family: ui-monospace, monospace; }}
svg .fa {{ fill: #f97316; fill-opacity: 0.12; }}
svg .la {{ stroke: #f97316; stroke-width: 2.5; fill: none; }}
svg .lb {{ stroke: #38bdf8; stroke-width: 2.5; fill: none; }}
svg .zero {{ stroke: #475569; stroke-width: 1; stroke-dasharray: 4 4; }}
svg .ref {{ stroke: #64748b; stroke-width: 1.2; stroke-dasharray: 4 4; }}
svg .reflab {{ fill: #94a3b8; font-size: 11px; font-weight: 600; }}
svg .dota {{ fill: #38bdf8; }}
</style>
</head>
<body class="bg-dark-bg text-slate-100 font-sans antialiased selection:bg-brand-500 selection:text-white min-h-screen">

<!-- Top Navigation -->
<header class="sticky top-0 z-50 backdrop-blur-md bg-dark-bg/85 border-b border-dark-border px-4 lg:px-8 py-3.5">
  <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
    <div class="flex items-center gap-3">
      <a href="index.html" class="flex items-center gap-2 group">
        <span class="w-8 h-8 rounded-lg bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center font-black text-black text-base shadow-lg shadow-brand-500/20 group-hover:scale-105 transition">P</span>
        <div>
          <span class="font-bold text-base tracking-tight text-white group-hover:text-brand-500 transition">트레이닝판</span>
          <span class="text-xs text-slate-400 block -mt-1 font-mono">계림점 판단 노트</span>
        </div>
      </a>
      <span class="hidden sm:inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-brand-500/10 text-brand-500 border border-brand-500/30">위탁운영 (40:60)</span>
      <span class="hidden md:inline-block px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">보증금·월세 0원 (소유자)</span>
      <span class="hidden lg:inline-block px-2.5 py-0.5 rounded-full text-xs font-medium bg-sky-500/10 text-sky-400 border border-sky-500/20">코치 전원 채용</span>
    </div>

    <nav class="flex items-center gap-1.5 sm:gap-2 text-xs sm:text-sm font-medium">
      <a href="#summary" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">핵심 요약</a>
      <a href="#calc" class="px-3 py-1.5 rounded-lg bg-brand-500/20 text-brand-400 font-semibold border border-brand-500/30 hover:bg-brand-500/30 transition">수익 계산기</a>
      <a href="#rules" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">판단 기준</a>
      <a href="#sinchang" class="hidden sm:inline-block px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">신창점 비교</a>
      <a href="#questions" class="px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-dark-surface transition">미팅 질문</a>
      <a href="index.html" class="ml-2 px-3 py-1.5 rounded-lg bg-dark-surface text-slate-300 hover:text-white border border-dark-border transition">허브 ↗</a>
    </nav>
  </div>
</header>

<main class="max-w-7xl mx-auto px-4 lg:px-8 py-8 space-y-12">

  <!-- Hero Header -->
  <section id="summary" class="relative rounded-2xl p-6 sm:p-8 bg-gradient-to-br from-dark-card via-dark-card to-dark-surface border border-dark-border shadow-2xl overflow-hidden">
    <div class="absolute -top-24 -right-24 w-96 h-96 bg-brand-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="relative z-10 max-w-3xl space-y-4">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold tracking-wide">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        내부 의사결정 확정안 · 조건부 Go
      </div>
      <h1 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
        의장님 전액투자 + 트레이닝판 위탁운영<br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-500 to-amber-300">순수익 40% : 60% 분배 확정 모델</span>
      </h1>
      <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
        의장님이 해당 층(지하 1층 230평)의 <span class="text-white font-semibold underline decoration-brand-500 decoration-2 underline-offset-4">실소유자이므로 보증금과 월세는 0원</span>입니다.
        인테리어와 장비 전액은 의장님이 투자하며, 우리는 <span class="text-white font-semibold">현장 수업을 직접 뛰지 않고 총괄 운영</span>만 맡습니다.
        <span class="text-brand-400 font-semibold">코치는 전원 채용(월 660만원 실운영비 산입)</span>하여 매출에서 우선 지급하고, 남은 순수익을 <span class="text-brand-400 font-bold">40%(우리) : 60%(의장님)</span>로 나눕니다.
      </p>

      <!-- Key Stat Badges -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4">
        <div class="bg-dark-bg/60 border border-dark-border rounded-xl p-3.5">
          <div class="text-xs text-slate-400">우리 투자금 / 리스크</div>
          <div class="text-2xl font-black text-emerald-400 font-mono mt-0.5">0원</div>
          <div class="text-[11px] text-slate-500 mt-0.5">보증금·월세·상환 없음</div>
        </div>
        <div class="bg-dark-bg/60 border border-dark-border rounded-xl p-3.5">
          <div class="text-xs text-slate-400">목표 인원 (150명) 우리 몫</div>
          <div class="text-2xl font-black text-brand-500 font-mono mt-0.5" data-o="ourM">-</div>
          <div class="text-[11px] text-slate-400 mt-0.5 font-mono">순수익의 40% (월)</div>
        </div>
        <div class="bg-dark-bg/60 border border-dark-border rounded-xl p-3.5">
          <div class="text-xs text-slate-400">목표 인원 의장님 순수익</div>
          <div class="text-2xl font-black text-sky-400 font-mono mt-0.5" data-o="hisM">-</div>
          <div class="text-[11px] text-slate-400 mt-0.5 font-mono">순수익의 60% (월)</div>
        </div>
        <div class="bg-dark-bg/60 border border-dark-border rounded-xl p-3.5">
          <div class="text-xs text-slate-400">손익분기점 (BEP)</div>
          <div class="text-2xl font-black text-amber-400 font-mono mt-0.5" data-o="beMem">-</div>
          <div class="text-[11px] text-slate-500 mt-0.5">월세 0원 효과 (약 55명)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive 40:60 Calculator -->
  <section id="calc" class="space-y-6">
    <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-dark-border pb-4">
      <div>
        <div class="inline-flex items-center gap-2 text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Interactive Simulator</div>
        <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">위탁운영 수익 시뮬레이터 (40:60)</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-0.5">인원수와 회원권 월단가를 움직이면 순수익과 의장님 투자 회수 기간이 실시간으로 계산됩니다.</p>
      </div>

      <!-- Preset Scenarios -->
      <div class="flex items-center gap-1.5 bg-dark-card border border-dark-border p-1 rounded-xl" role="group">
        <button type="button" data-scen="low" class="scen-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition">보수적 (120명·14만)</button>
        <button type="button" data-scen="base" class="scen-btn px-3 py-1.5 rounded-lg text-xs font-semibold bg-brand-500 text-black shadow-md shadow-brand-500/20 transition">기준안 (150명·14만)</button>
        <button type="button" data-scen="high" class="scen-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white transition">낙관적 (180명·15만)</button>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Input Controls (5 Cols) -->
      <div class="lg:col-span-5 bg-dark-card border border-dark-border rounded-2xl p-5 space-y-5">
        <div class="space-y-4">
          <div class="text-xs font-bold text-slate-400 uppercase tracking-wider font-mono flex items-center justify-between">
            <span>1. 매출 변수 (인원수 & 월단가)</span>
            <span class="text-brand-500">실시간 연동</span>
          </div>

          <!-- Members Slider -->
          <div class="space-y-1.5 bg-dark-surface/60 p-3.5 rounded-xl border border-dark-border/60">
            <div class="flex justify-between items-center text-sm font-semibold">
              <label for="Members" class="text-slate-200">목표 인원수 (등록 회원)</label>
              <output for="Members" id="oMembers" class="font-mono text-base font-bold text-brand-400">150명</output>
            </div>
            <input type="range" id="Members" min="50" max="250" step="5" value="150" class="w-full h-2 bg-dark-bg rounded-lg cursor-pointer">
            <div class="flex justify-between text-[11px] text-slate-500 font-mono">
              <span>50명</span>
              <span>신창 평균 191명</span>
              <span>250명</span>
            </div>
          </div>

          <!-- Price Slider -->
          <div class="space-y-1.5 bg-dark-surface/60 p-3.5 rounded-xl border border-dark-border/60">
            <div class="flex justify-between items-center text-sm font-semibold">
              <label for="Price" class="text-slate-200">회원권 월단가 (1인 실수령)</label>
              <output for="Price" id="oPrice" class="font-mono text-base font-bold text-brand-400">14만원</output>
            </div>
            <input type="range" id="Price" min="10" max="25" step="0.5" value="14" class="w-full h-2 bg-dark-bg rounded-lg cursor-pointer">
            <div class="flex justify-between text-[11px] text-slate-500 font-mono">
              <span>10만원 (할인/장기)</span>
              <span>기준 14만</span>
              <span>25만원 (정가권)</span>
            </div>
          </div>

          <!-- Calculated Gross -->
          <div class="p-3 bg-brand-500/10 border border-brand-500/30 rounded-xl flex items-center justify-between">
            <div class="text-xs text-brand-300 font-medium">산출 예상 월 총매출</div>
            <div id="oCalcRev" class="text-base font-black text-brand-400 font-mono">-</div>
          </div>
        </div>

        <div class="space-y-4 pt-2 border-t border-dark-border">
          <div class="text-xs font-bold text-slate-400 uppercase tracking-wider font-mono">2. 월 실운영비 (월세 0원)</div>

          <!-- Opex Slider -->
          <div class="space-y-1.5 bg-dark-surface/60 p-3.5 rounded-xl border border-dark-border/60">
            <div class="flex justify-between items-center text-sm font-semibold">
              <label for="O" class="text-slate-200">월 고정 실운영비</label>
              <output for="O" id="oO" class="font-mono text-base font-bold text-slate-200">1,000만원</output>
            </div>
            <input type="range" id="O" min="800" max="1400" step="20" value="1000" class="w-full h-2 bg-dark-bg rounded-lg cursor-pointer">
            <p class="text-[11px] text-slate-400 leading-relaxed">
              • <b class="text-slate-200">코치 채용 인건비</b>: 약 660만원 (헤드코치 1명 + 코치 1~2명 전원 고용)<br>
              • <b class="text-slate-200">관리비/공과금</b>: 약 300만원 (전기·수도·가스)<br>
              • <b class="text-slate-200">소모품/마케팅</b>: 약 40만원<br>
              • <b class="text-emerald-400 font-bold">임대료(월세)</b>: 0원 (의장님 해당 층 소유)
            </p>
          </div>

          <!-- Profit Share (40:60 fixed visual) -->
          <div class="space-y-1.5 bg-dark-surface/60 p-3.5 rounded-xl border border-dark-border/60">
            <div class="flex justify-between items-center text-sm font-semibold">
              <label for="Pct" class="text-slate-200">순수익 배분 비율</label>
              <span class="font-mono text-sm font-bold text-brand-400">우리 40% : 의장님 60%</span>
            </div>
            <input type="range" id="Pct" min="20" max="60" step="5" value="40" class="w-full h-2 bg-dark-bg rounded-lg cursor-pointer">
            <div class="flex justify-between text-[11px] text-slate-500 font-mono">
              <span>운영 20%</span>
              <span class="text-brand-400 font-bold">확정 40%</span>
              <span>운영 60%</span>
            </div>
          </div>
        </div>

        <div class="space-y-4 pt-2 border-t border-dark-border">
          <div class="text-xs font-bold text-slate-400 uppercase tracking-wider font-mono">3. 의장님 초기 투자비 (의장님 100% 부담)</div>

          <div class="grid grid-cols-2 gap-3">
            <div class="bg-dark-surface/60 p-3 rounded-xl border border-dark-border/60 space-y-1">
              <div class="flex justify-between text-xs font-semibold">
                <label for="I">인테리어 단가</label>
                <output for="I" id="oI" class="font-mono text-brand-400">100만/평</output>
              </div>
              <input type="range" id="I" min="70" max="180" step="10" value="100" class="w-full h-1.5 bg-dark-bg rounded cursor-pointer">
              <div class="text-[10px] text-slate-500">230평 기준 (의장님 시공)</div>
            </div>

            <div class="bg-dark-surface/60 p-3 rounded-xl border border-dark-border/60 space-y-1">
              <div class="flex justify-between text-xs font-semibold">
                <label for="E">운동 장비 일체</label>
                <output for="E" id="oE" class="font-mono text-brand-400">1.2억원</output>
              </div>
              <input type="range" id="E" min="8000" max="22000" step="1000" value="12000" class="w-full h-1.5 bg-dark-bg rounded cursor-pointer">
              <div class="text-[10px] text-slate-500">유산소·바벨·리그 등</div>
            </div>
          </div>

          <label class="flex items-start gap-2.5 p-2.5 rounded-xl bg-dark-surface/40 border border-dark-border/40 cursor-pointer text-xs">
            <input type="checkbox" id="W" class="w-4 h-4 mt-0.5 rounded text-brand-500 accent-brand-500 bg-dark-bg">
            <span class="text-slate-300">
              <b class="text-white">2단계 회복실(사우나·냉탕) 포함하기</b><br>
              <span class="text-slate-500">투자비 +7,500만, 관리비 +120만 (안정 후 2단계 추천)</span>
            </span>
          </label>
        </div>
      </div>

      <!-- Output Results (7 Cols) -->
      <div class="lg:col-span-7 space-y-5">
        <!-- Monthly Breakdown Card -->
        <div class="bg-dark-card border border-dark-border rounded-2xl p-5 space-y-4">
          <div class="flex items-center justify-between border-b border-dark-border pb-3">
            <span class="text-xs font-bold font-mono uppercase tracking-wider text-slate-400">월 손익 및 정산 명세서 (자리 잡은 뒤)</span>
            <span class="text-xs px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-mono">월세 0원 반영</span>
          </div>

          <div class="space-y-2.5 text-sm">
            <div class="flex justify-between items-center text-slate-300">
              <span>월 매출 (카드수수료·부가세 4.8% 차감 후 실입금)</span>
              <span class="font-mono font-semibold text-slate-200" data-o="rev">-</span>
            </div>
            <div class="flex justify-between items-center text-slate-400">
              <span>월 실운영비 (코치 채용 인건비 + 관리비/공과금 + 소모품)</span>
              <span class="font-mono font-semibold text-rose-400" data-o="cO">-</span>
            </div>
            <div class="pt-2 border-t border-dark-border flex justify-between items-center font-bold text-base">
              <span class="text-white">월 순수익 (영업이익)</span>
              <span class="font-mono text-white text-lg" data-o="profit">-</span>
            </div>

            <!-- Distribution Box -->
            <div class="grid grid-cols-2 gap-3 pt-2">
              <div class="p-4 rounded-xl bg-gradient-to-br from-brand-500/15 to-brand-500/5 border border-brand-500/30">
                <div class="flex items-center justify-between text-xs text-brand-300 font-bold">
                  <span>트레이닝판 (우리 몫)</span>
                  <span class="px-1.5 py-0.5 rounded bg-brand-500 text-black text-[10px] font-black">40%</span>
                </div>
                <div class="text-2xl sm:text-3xl font-black text-brand-400 font-mono mt-1" data-o="ourM">-</div>
                <div class="text-[11px] text-slate-400 mt-1">
                  • 자본 0원 투입으로 순수익 수취<br>
                  • 수업 안 뛰고 총괄 운영<br>
                  • 신창 순익(550만)과 동등 수준
                </div>
              </div>

              <div class="p-4 rounded-xl bg-gradient-to-br from-sky-500/15 to-sky-500/5 border border-sky-500/30">
                <div class="flex items-center justify-between text-xs text-sky-300 font-bold">
                  <span>의장님 (소유자/투자자 몫)</span>
                  <span class="px-1.5 py-0.5 rounded bg-sky-400 text-black text-[10px] font-black">60%</span>
                </div>
                <div class="text-2xl sm:text-3xl font-black text-sky-400 font-mono mt-1" data-o="hisM">-</div>
                <div class="text-[11px] text-slate-400 mt-1">
                  • 공실 월세 0원 → 고수익 전환<br>
                  • 투자금 회수 후 영구 순수익<br>
                  • 건물 자산가치 극대화
                </div>
              </div>
            </div>

            <div class="text-xs text-slate-400 bg-dark-surface/60 p-3 rounded-xl border border-dark-border/60" data-o="cmpSin">-</div>
          </div>
        </div>

        <!-- Investment & BEP Stats -->
        <div class="grid grid-cols-3 gap-3">
          <div class="bg-dark-card border border-dark-border rounded-xl p-3.5 space-y-1">
            <span class="text-xs text-slate-400 block">의장님 총 투자금</span>
            <span class="text-lg sm:text-xl font-bold font-mono text-white block" data-o="capex">-</span>
            <span class="text-[10px] text-slate-500 block truncate" data-o="capexN">-</span>
          </div>
          <div class="bg-dark-card border border-dark-border rounded-xl p-3.5 space-y-1">
            <span class="text-xs text-slate-400 block">의장님 원금 회수 기간</span>
            <span class="text-lg sm:text-xl font-bold font-mono text-sky-400 block" data-o="payY">-</span>
            <span class="text-[10px] text-slate-500 block">의장님 몫(60%)으로 회수</span>
          </div>
          <div class="bg-dark-card border border-dark-border rounded-xl p-3.5 space-y-1">
            <span class="text-xs text-slate-400 block">손익분기점 (BEP)</span>
            <span class="text-lg sm:text-xl font-bold font-mono text-amber-400 block" data-o="beRev">-</span>
            <span class="text-[10px] text-slate-500 block" data-o="beMem">-</span>
          </div>
        </div>

        <!-- Charts (SVG) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="bg-dark-card border border-dark-border rounded-xl p-4 space-y-2">
            <div class="flex items-center justify-between text-xs font-semibold text-slate-300">
              <span>24개월 예상 월 매출 & BEP</span>
              <span class="text-[10px] font-mono text-brand-400">Ramp-up</span>
            </div>
            <svg id="ch1" viewBox="0 0 520 220" class="w-full h-auto"></svg>
            <div class="flex items-center gap-3 text-[11px] text-slate-400 justify-end pt-1">
              <span class="flex items-center gap-1.5"><i class="w-2.5 h-1 bg-brand-500 rounded"></i>월 매출</span>
              <span class="flex items-center gap-1.5"><i class="w-2.5 h-1 bg-slate-500 rounded"></i>신창 기준</span>
              <span class="flex items-center gap-1.5"><i class="w-2.5 h-1 bg-rose-500 rounded"></i>손익분기</span>
            </div>
          </div>

          <div class="bg-dark-card border border-dark-border rounded-xl p-4 space-y-2">
            <div class="flex items-center justify-between text-xs font-semibold text-slate-300">
              <span>의장님 투자 회수 & 우리 누적 성과급</span>
              <span class="text-[10px] font-mono text-sky-400">10 Year View</span>
            </div>
            <svg id="ch2" viewBox="0 0 520 220" class="w-full h-auto"></svg>
            <div class="flex items-center gap-3 text-[11px] text-slate-400 justify-end pt-1">
              <span class="flex items-center gap-1.5"><i class="w-2.5 h-1 bg-sky-400 rounded"></i>의장님 누적</span>
              <span class="flex items-center gap-1.5"><i class="w-2.5 h-1 bg-brand-500 rounded"></i>우리 누적</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Go / No-Go Rules -->
  <section id="rules" class="space-y-4">
    <div class="border-b border-dark-border pb-3">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Decision Criteria</div>
      <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">할까, 말까 판단 기준표</h2>
      <p class="text-xs sm:text-sm text-slate-400 mt-0.5">미팅 전 반드시 숙지해야 할 Go 조건과 거절(No-Go) 마지노선입니다.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <!-- GO -->
      <div class="bg-dark-card border border-emerald-500/30 rounded-2xl p-5 space-y-3.5 relative overflow-hidden">
        <div class="absolute top-0 left-0 right-0 h-1 bg-emerald-500"></div>
        <div class="flex items-center justify-between">
          <span class="text-sm font-bold text-emerald-400">반드시 챙길 조건 (Go)</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300">필수</span>
        </div>
        <ul class="space-y-2.5 text-xs text-slate-300">
          <li class="flex items-start gap-2">
            <span class="text-emerald-400 font-bold">✓</span>
            <div><b class="text-white">보증금·월세 0원</b>: 의장님이 층 소유자이므로 외부에 나가는 임대료 일체 없음</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-emerald-400 font-bold">✓</span>
            <div><b class="text-white">시설/장비 전액 투자 & 상환 0원</b>: 의장님이 100% 매입·시공하고 상환 의무 없음</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-emerald-400 font-bold">✓</span>
            <div><b class="text-white">초기 적자 의장님 전액 보전</b>: 개업 초기(1~3개월) 운영비 부족분은 사업자인 의장님이 부담</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-emerald-400 font-bold">✓</span>
            <div><b class="text-white">코치 채용 인건비 우선 지급</b>: 코칭 인건비(약 660만)는 실운영비에 포함하여 매출에서 우선 집행</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-emerald-400 font-bold">✓</span>
            <div><b class="text-white">운영 전권 위임</b>: 프로그램 기획, 코치 채용, 회원 관리 등 현장 전권은 트레이닝판에 위임</div>
          </li>
        </ul>
      </div>

      <!-- Negotiate -->
      <div class="bg-dark-card border border-brand-500/30 rounded-2xl p-5 space-y-3.5 relative overflow-hidden">
        <div class="absolute top-0 left-0 right-0 h-1 bg-brand-500"></div>
        <div class="flex items-center justify-between">
          <span class="text-sm font-bold text-brand-400">미팅 협상 항목</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-brand-500/20 text-brand-300">조율</span>
        </div>
        <ul class="space-y-2.5 text-xs text-slate-300">
          <li class="flex items-start gap-2">
            <span class="text-brand-400 font-bold">•</span>
            <div><b class="text-white">수수료율 40% 확정</b>: 기준 40%로 못박고, 의장님의 투자 범위에 따라 마지노선 35% 방어</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-brand-400 font-bold">•</span>
            <div><b class="text-white">월 운영비 인정 범위</b>: 코치 급여, 공과금, 소모품, 마케팅 실비를 사전에 계약서에 못박기</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-brand-400 font-bold">•</span>
            <div><b class="text-white">회원 주차 무료 지원</b>: 지하주차장 무료 가능 대수 및 2시간 무료 지원 확보</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-brand-400 font-bold">•</span>
            <div><b class="text-white">계약 기간 3~5년</b>: 회원이 자리 잡는 기간 보장 및 중도 해지 시 위약보상금 조항</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-brand-400 font-bold">•</span>
            <div><b class="text-white">2단계 회복실 유보</b>: 초기 투자비를 줄이기 위해 체육관 오픈 후 안정화 시점에 추진</div>
          </li>
        </ul>
      </div>

      <!-- Stop -->
      <div class="bg-dark-card border border-rose-500/30 rounded-2xl p-5 space-y-3.5 relative overflow-hidden">
        <div class="absolute top-0 left-0 right-0 h-1 bg-rose-500"></div>
        <div class="flex items-center justify-between">
          <span class="text-sm font-bold text-rose-400">이러면 거절 (No-Go)</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-500/20 text-rose-300">중단</span>
        </div>
        <ul class="space-y-2.5 text-xs text-slate-300">
          <li class="flex items-start gap-2">
            <span class="text-rose-400 font-bold">✕</span>
            <div><b class="text-white">보증금이나 월세를 요구할 때</b>: 본인 소유 층 위탁운영의 취지와 정면 위배</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-rose-400 font-bold">✕</span>
            <div><b class="text-white">초기 적자를 우리보고 메우라 할 때</b>: 우리 돈 0원 원칙 위반</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-rose-400 font-bold">✕</span>
            <div><b class="text-white">수수료율이 25% 미만일 때</b>: 리소스 투입 대비 신창점 수익 수준 미달</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-rose-400 font-bold">✕</span>
            <div><b class="text-white">수업 편성이나 코칭에 간섭할 때</b>: 서비스 품질 저하 및 갈등 유발</div>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-rose-400 font-bold">✕</span>
            <div><b class="text-white">층고(3.4m 미만)나 환기 불가 시</b>: 크로스핏/체육시설 용도 물리적 불가</div>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Comparison with Sinchang -->
  <section id="sinchang" class="space-y-4">
    <div class="border-b border-dark-border pb-3">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Benchmark Comparison</div>
      <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">기존 신창점 vs 계림 위탁운영 비교</h2>
      <p class="text-xs sm:text-sm text-slate-400 mt-0.5">왜 계림 위탁운영이 재정적으로 훨씬 안전하고 매력적인지 분석합니다.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="bg-dark-card border border-dark-border rounded-2xl p-5 space-y-3">
        <div class="flex items-center justify-between">
          <span class="font-bold text-slate-300">신창점 (직접 임차 운영 방식)</span>
          <span class="text-xs font-mono text-slate-400">보증금 + 월세 있음</span>
        </div>
        <div class="space-y-2 text-xs text-slate-300">
          <div class="flex justify-between py-1 border-b border-dark-border">
            <span>월 평균 매출 (회원 191명)</span>
            <span class="font-mono font-bold text-white">2,100만원</span>
          </div>
          <div class="flex justify-between py-1 border-b border-dark-border text-rose-400">
            <span>고정 임대료 (의장님 월세)</span>
            <span class="font-mono font-bold">− 660만원 (곧 700만)</span>
          </div>
          <div class="flex justify-between py-1 border-b border-dark-border text-slate-400">
            <span>기타 실운영비 (인건비·공과금)</span>
            <span class="font-mono font-bold">− 790만원</span>
          </div>
          <div class="flex justify-between py-1.5 font-bold text-sm text-emerald-400">
            <span>최종 순이익</span>
            <span class="font-mono">약 550만원</span>
          </div>
          <p class="text-[11px] text-slate-400 pt-1 leading-relaxed">
            ⚠ 보증금 수천만원과 시설비 2~3억원을 묶어두고, 매달 660만원의 월세를 무조건 물어야 하는 사업 리스크가 있습니다.
          </p>
        </div>
      </div>

      <div class="bg-dark-card border border-brand-500/40 rounded-2xl p-5 space-y-3 bg-gradient-to-br from-dark-card to-brand-500/5">
        <div class="flex items-center justify-between">
          <span class="font-bold text-brand-400">계림점 (의장님 소유 전액투자 위탁운영)</span>
          <span class="text-xs font-mono px-2 py-0.5 rounded bg-brand-500/20 text-brand-300 font-bold">보증금 0원 · 월세 0원</span>
        </div>
        <div class="space-y-2 text-xs text-slate-300">
          <div class="flex justify-between py-1 border-b border-dark-border">
            <span>목표 월 매출 (회원 150명)</span>
            <span class="font-mono font-bold text-white">2,100만원 (실입금 2,000만)</span>
          </div>
          <div class="flex justify-between py-1 border-b border-dark-border text-emerald-400">
            <span>고정 임대료 (의장님 해당 층 소유)</span>
            <span class="font-mono font-bold">0원!</span>
          </div>
          <div class="flex justify-between py-1 border-b border-dark-border text-slate-400">
            <span>월 실운영비 (코치 전원 채용 인건비+관리비)</span>
            <span class="font-mono font-bold">− 1,000만원</span>
          </div>
          <div class="flex justify-between py-1.5 font-bold text-sm text-brand-400">
            <span>우리 몫 성과급 (순수익 1,000만의 40%)</span>
            <span class="font-mono">월 400 ~ 550만원!</span>
          </div>
          <p class="text-[11px] text-slate-300 pt-1 leading-relaxed">
            💡 <b class="text-white">우리는 자본 투입 0원 + 수업도 직접 안 뜀</b>. 코치를 전원 고용해서 쓰고도 순수익의 40%로 매달 400~550만원을 챙기는 완벽한 안전 자산입니다.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Space & SVG Plan -->
  <section id="space" class="space-y-4">
    <div class="border-b border-dark-border pb-3">
      <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Floor Plan & Zoning</div>
      <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">지하 230평 구역별 레이아웃 구상도</h2>
      <p class="text-xs sm:text-sm text-slate-400 mt-0.5">사선 벽 쪽 Hyb 존(하이록스 25m 레인)과 아래쪽 Met 존(크로스핏)을 중앙 25m 리그로 분리합니다.</p>
    </div>

    <div class="bg-dark-card border border-dark-border rounded-2xl p-4 sm:p-6 overflow-hidden">
      {plan_svg_content}
    </div>
  </section>

  <!-- 11 Step Meeting Questions -->
  <section id="questions" class="space-y-4">
    <div class="border-b border-dark-border pb-3 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
      <div>
        <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Negotiation Roadmap</div>
        <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">미팅 11단계 대화 순서 (전략 가이드)</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-0.5">처음부터 조건을 따지지 않고, 의장님의 니즈를 들으며 자연스럽게 위탁 40:60으로 이끕니다.</p>
      </div>
      <a href="kyerim-meeting-questions.pdf" target="_blank" class="px-3 py-1.5 rounded-lg bg-dark-surface border border-dark-border text-xs font-medium text-slate-300 hover:text-white hover:border-brand-500 transition inline-flex items-center gap-1.5 self-start sm:self-auto">
        <span>📄</span> 질문지 PDF 인쇄
      </a>
    </div>

    <div class="space-y-3">
      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">1</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「이 공간 이야기를 저희한테 먼저 꺼내 주신 이유가 궁금합니다.」</p>
          <p class="text-xs text-slate-400">듣기만 합니다. 공실 해소, 본인 건설사 시공 물량, 공간 가치 상승 등 의장님의 가장 큰 속내를 확인합니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">2</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「이 건물, 앞으로 3~5년 정도 장기적인 운영이나 개발 계획은 어떻게 보세요?」</p>
          <p class="text-xs text-slate-400">매각이나 재건축 계획 여부를 확인하고, 위탁운영 계약 기간(3~5년)의 정당성을 마련합니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">3</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「인테리어와 운동 장비 등 초기 투자 예산 규모는 대략 어느 정도로 생각하고 계신가요?」</p>
          <p class="text-xs text-slate-400">의장님 입에서 먼저 투자 가능 금액을 듣습니다. 우리가 먼저 액수를 못박지 않습니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">4</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「인테리어 공사는 의장님 회사에서 직접 시공해 주실 수 있죠?」</p>
          <p class="text-xs text-slate-400">원가 시공이 가능함을 확인하고, 체육관 특화 설계 스펙(바닥 방음, 리그 설치)을 우리가 지원합니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-brand-500/30 flex gap-3 items-start bg-brand-500/5">
        <span class="w-7 h-7 rounded-lg bg-brand-500 text-black font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">5</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-brand-400">「의장님이 해당 층 소유자이시니 보증금이나 월세 없이, 시설 전액 투자를 해 주시고 저희는 전문 위탁운영을 맡아 순수익을 40:60으로 셰어하는 방식으로 가고자 합니다. 의장님도 이 방향이 가장 좋으시죠?」</p>
          <p class="text-xs text-slate-300">우리의 핵심 사업 구조를 못박습니다. 보증금/월세 없는 위탁운영 40:60 구조를 확정짓는 결정구입니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-brand-500/30 flex gap-3 items-start bg-brand-500/5">
        <span class="w-7 h-7 rounded-lg bg-brand-500 text-black font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">6</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-brand-400">「저희는 본사 총괄 운영만 전담하고 수업은 전문 코치를 전원 채용해 돌릴 계획입니다. 오픈 초기 회원이 덜 찼을 때의 코치 인건비와 관리비는 의장님이 운영 통장으로 보전해 주실 수 있죠?」</p>
          <p class="text-xs text-slate-300">코치 전원 채용 인건비가 실운영비로 산입됨을 알리고, 초기 적자를 사업자인 의장님이 보전하도록 확답을 받습니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">7</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「관리비와 전기·수도세는 매달 어느 정도 나오고, 건물에서 지원해 주실 수 있는 부분이 있나요?」</p>
          <p class="text-xs text-slate-400">고정 지출 규모를 정확히 파악하여 순수익 계산의 신뢰도를 높입니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">8</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「회원들 지하주차장 무료 이용은 몇 대, 몇 시간까지 지원해 주실 수 있나요?」</p>
          <p class="text-xs text-slate-400">회원 등록 결정의 핵심인 주차 지원 조건을 확보합니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">9</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「철거할 벽 중에 방화벽이 있는지, 보 아래 실제 천장 높이가 얼마나 나오는지 현장에서 확인해보고 싶습니다.」</p>
          <p class="text-xs text-slate-400">운동 수업에 물리적으로 지장이 없는지 실측합니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">10</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「사우나·냉탕(회복실)은 공사비가 크니 체육관 오픈 후 자리 잡히면 2단계로 진행하는 게 안전한데 어떠세요?」</p>
          <p class="text-xs text-slate-400">의장님의 초기 투자금 부담을 덜어주어 계약 체결을 앞당깁니다.</p>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-dark-card border border-dark-border flex gap-3 items-start">
        <span class="w-7 h-7 rounded-lg bg-brand-500/20 text-brand-400 font-mono font-bold text-sm flex items-center justify-center flex-shrink-0">11</span>
        <div class="space-y-1">
          <p class="text-sm font-bold text-white">「공사 시작과 오픈 시기는 언제쯤으로 희망하시나요?」</p>
          <p class="text-xs text-slate-400">내년 초 새해 운동 성수기(1~3월) 오픈 일정을 조율합니다.</p>
        </div>
      </div>
    </div>
  </section>

</main>

<footer class="border-t border-dark-border bg-dark-card/50 py-8 px-4 text-center text-xs text-slate-500 font-mono space-y-2">
  <p>계림 운동공간 위탁운영 프로젝트 · 트레이닝판 내부 판단 전략 문서</p>
  <p>© 2026 TRAININGPAN. ALL RIGHTS RESERVED. (대외비 · 의장님 미팅 전 검토용)</p>
</footer>

<script>
(function(){{
  const $ = (id) => document.getElementById(id);
  const AREA = 230, PREOPEN = 2000;
  const SIN = {{ rev: 2100, cost: 1450, rent: 660, net: 550 }};
  const WELL = {{ capex: 7500, opex: 120, perMember: 1 }};
  const TAU = [4, 6, 9], SPEED = ['빠름', '보통', '느림'];
  
  const SCEN = {{
    low:  {{ Members: 120, Price: 14, T: 3, W: false, O: 950, Pct: 40, I: 90, E: 10000 }},
    base: {{ Members: 150, Price: 14, T: 2, W: false, O: 1000, Pct: 40, I: 100, E: 12000 }},
    high: {{ Members: 180, Price: 15, T: 1, W: false, O: 1050, Pct: 40, I: 110, E: 13000 }}
  }};
  
  const ids = ['Members','Price','T','O','Pct','I','E'];
  
  const fmt = (v) => {{
    const r = Math.round(v);
    if (Math.abs(r) >= 10000) return (Math.round(r / 1000) / 10).toLocaleString('ko-KR') + '억원';
    return r.toLocaleString('ko-KR') + '만원';
  }};
  
  const years = (m) => {{
    if (!isFinite(m)) return '10년 초과';
    const y = Math.floor(m / 12), mo = m % 12;
    return y > 0 ? (mo ? `${{y}}년 ${{mo}}개월` : `${{y}}년`) : `${{mo}}개월`;
  }};
  
  const read = () => {{
    const v = {{}};
    ids.forEach(k => v[k] = Number($(k).value));
    v.W = $('W').checked;
    return v;
  }};
  
  function model(v){{
    const tau = TAU[v.T - 1];
    const ramp = (m) => 1 - 0.75 * Math.exp(-(m - 1) / tau);
    const upl = v.W ? (1 + WELL.perMember / v.Price) : 1;
    const opex = v.O + (v.W ? WELL.opex : 0);
    const capex = AREA * v.I + v.E + PREOPEN + (v.W ? WELL.capex : 0);
    
    const fullGrossRev = v.Members * v.Price * upl;
    
    let ourCum = 0, hisCum = -capex, pay = Infinity;
    const revS = [], ourS = [], hisS = [];
    
    for (let m = 1; m <= 120; m++) {{
      const grossRev = fullGrossRev * ramp(m);
      const netRev = grossRev * (1 - 0.048); // 카드수수료 및 부가세 4.8% 제외
      const profit = netRev - opex;
      
      const ourShare = profit > 0 ? profit * v.Pct / 100 : 0;
      const hisShare = profit > 0 ? profit * (100 - v.Pct) / 100 : profit; // 초기 적자는 의장님이 보전
      
      ourCum += ourShare;
      hisCum += hisShare;
      
      if (pay === Infinity && hisCum >= 0) pay = m;
      if (m <= 24) revS.push(netRev);
      ourS.push(ourCum);
      hisS.push(hisCum);
    }}
    
    const grossRevM = fullGrossRev;
    const netRevM = grossRevM * (1 - 0.048);
    const profitM = netRevM - opex;
    const ourM = profitM > 0 ? profitM * v.Pct / 100 : 0;
    const hisM = profitM > 0 ? profitM * (100 - v.Pct) / 100 : profitM;
    const beRev = opex / (1 - 0.048);
    const beMem = Math.ceil(beRev / (v.Price * upl));
    
    return {{ grossRevM, netRevM, opex, profitM, ourM, hisM, capex, pay, beRev, beMem, revS, ourS, hisS }};
  }}

  const line = (pts) => pts.map((p, i) => (i ? 'L' : 'M') + p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' ');
  
  function drawRev(v, r){{
    const svg = $('ch1'), W = 520, H = 220, L = 46, R = 64, T = 12, B = 28;
    const maxY = Math.max(3000, r.grossRevM * 1.3);
    const x = (m) => L + (m - 1) / 23 * (W - L - R), y = (n) => T + (1 - n / maxY) * (H - T - B);
    let g = '';
    for (let n = 0; n <= maxY; n += 1000) g += `<line class="g" x1="${{L}}" x2="${{W-R}}" y1="${{y(n)}}" y2="${{y(n)}}"/><text class="ax" x="${{L-6}}" y="${{y(n)+4}}" text-anchor="end">${{n===0?'0':n/1000+'천만'}}</text>`;
    [1,6,12,18,24].forEach(m => g += `<text class="ax" x="${{x(m)}}" y="${{H-8}}" text-anchor="${{m===1?'start':m===24?'end':'middle'}}">${{m}}개월</text>`);
    const pts = r.revS.map((n, i) => [x(i + 1), y(n)]);
    const area = line(pts) + ` L${{x(24)}} ${{y(0)}} L${{x(1)}} ${{y(0)}} Z`;
    const refs = `<line class="ref" x1="${{L}}" x2="${{W-R}}" y1="${{y(SIN.rev)}}" y2="${{y(SIN.rev)}}"/><text class="reflab" x="${{W-R+6}}" y="${{y(SIN.rev)+4}}">신창</text>`
      + `<line class="ref" x1="${{L}}" x2="${{W-R}}" y1="${{y(r.beRev)}}" y2="${{y(r.beRev)}}" style="stroke:#f43f5e"/><text class="reflab" x="${{W-R+6}}" y="${{y(r.beRev)+4}}" style="fill:#f43f5e">손익분기</text>`;
    svg.innerHTML = g + refs + `<path class="fa" d="${{area}}"/><path class="la" d="${{line(pts)}}"/>`;
  }}
  
  function drawCash(r){{
    const svg = $('ch2'), W = 520, H = 220, L = 52, R = 12, T = 12, B = 28;
    const all = r.ourS.concat(r.hisS, [0]);
    const minV = Math.min(...all), maxV = Math.max(...all), span = (maxV - minV) || 1;
    const x = (m) => L + (m - 1) / 119 * (W - L - R), y = (val) => T + (maxV - val) / span * (H - T - B);
    let g = '';
    const step = span > 60000 ? 20000 : 10000;
    for (let t = Math.ceil(minV / step) * step; t <= maxV; t += step) g += `<line class="g" x1="${{L}}" x2="${{W-R}}" y1="${{y(t)}}" y2="${{y(t)}}"/><text class="ax" x="${{L-6}}" y="${{y(t)+4}}" text-anchor="end">${{t/10000}}억</text>`;
    [1,24,48,72,96,120].forEach(m => g += `<text class="ax" x="${{x(m)}}" y="${{H-8}}" text-anchor="${{m===1?'start':m===120?'end':'middle'}}">${{m===1?'개업':Math.round(m/12)+'년'}}</text>`);
    const ours = r.ourS.map((v, i) => [x(i + 1), y(v)]), his = r.hisS.map((v, i) => [x(i + 1), y(v)]);
    const mark = isFinite(r.pay) ? `<circle class="dota" cx="${{x(r.pay)}}" cy="${{y(0)}}" r="4.5"/>` : '';
    svg.innerHTML = g + `<line class="zero" x1="${{L}}" x2="${{W-R}}" y1="${{y(0)}}" y2="${{y(0)}}"/><path class="lb" d="${{line(his)}}"/><path class="la" d="${{line(ours)}}"/>` + mark;
  }}

  const set = (k, t) => document.querySelectorAll(`[data-o="${{k}}"]`).forEach(el => el.textContent = t);
  
  function render(){{
    const v = read();
    const gross = v.Members * v.Price;
    $('oMembers').textContent = v.Members + '명';
    $('oPrice').textContent = v.Price + '만원';
    $('oCalcRev').textContent = `${{fmt(gross)}} (${{v.Members}}명 × ${{v.Price}}만)`;
    $('oO').textContent = fmt(v.O);
    $('oI').textContent = v.I + '만원/평';
    $('oE').textContent = fmt(v.E);
    
    const r = model(v);
    set('rev', fmt(r.netRevM) + ` (총매출 ${{fmt(r.grossRevM)}})`);
    set('cO', '− ' + fmt(r.opex));
    set('profit', fmt(r.profitM));
    set('ourM', fmt(r.ourM));
    set('hisM', fmt(r.hisM));
    
    const d = r.ourM - SIN.net;
    set('cmpSin', `💡 신창점 순이익(550만원) 대비 ${{d >= 0 ? '+' : '−'}}${{fmt(Math.abs(d))}} (우리는 보증금·월세 0원, 수업 안 뛰고 전원 코치 채용)`);
    set('beRev', `월 매출 ${{fmt(r.beRev)}}`);
    set('beMem', `약 ${{r.beMem}}명 (월세 0원 효과)`);
    set('capex', fmt(r.capex));
    set('capexN', `인테리어 ${{fmt(AREA * v.I)}} · 장비 ${{fmt(v.E)}} · 사전비용 ${{fmt(PREOPEN)}}` + (v.W ? ` · 회복실 ${{fmt(WELL.capex)}}` : ''));
    set('payY', years(r.pay));
    
    drawRev(v, r);
    drawCash(r);
  }}

  function applyScen(name){{
    const s = SCEN[name];
    ids.forEach(k => $(k).value = s[k]);
    $('W').checked = s.W;
    document.querySelectorAll('.scen-btn').forEach(b => {{
      const isCur = b.dataset.scen === name;
      b.classList.toggle('bg-brand-500', isCur);
      b.classList.toggle('text-black', isCur);
      b.classList.toggle('text-slate-400', !isCur);
    }});
    render();
  }}

  document.querySelectorAll('.scen-btn').forEach(b => b.addEventListener('click', () => applyScen(b.dataset.scen)));
  ids.concat('W').forEach(k => $(k).addEventListener('input', () => {{
    document.querySelectorAll('.scen-btn').forEach(b => {{
      b.classList.remove('bg-brand-500', 'text-black');
      b.classList.add('text-slate-400');
    }});
    render();
  }}));

  render();
}})();
</script>
</body>
</html>
'''

with open('kyerim-internal.html', 'w', encoding='utf-8') as f:
    f.write(internal_html)

print("Finished generating new kyerim-internal.html. Size:", len(internal_html))
