# -*- coding: utf-8 -*-
import re

with open('work/plan.svg', 'r', encoding='utf-8') as f:
    master_svg = f.read()

# Make SVG responsive for embedding in Tailwind container
embedded_svg = master_svg.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400"', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" class="w-full h-auto max-h-[520px] mx-auto select-none"')

with open('kyerim-pitch.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Key Numbers in Hero
html = re.sub(
    r'<div class="text-3xl font-black text-emerald-600 font-mono mt-1">.*?</div>\s*<div class="text-\[11px\] text-slate-400 mt-1 font-medium">.*?</div>',
    r'<div class="text-3xl font-black text-emerald-600 font-mono mt-1">38<span class="text-base font-normal text-slate-500 ml-1">m</span></div>\n          <div class="text-[11px] text-slate-400 mt-1 font-medium">6m 와이드 그레이 터프</div>',
    html
)
html = re.sub(
    r'사선 외벽 활용 → 30m 듀얼 잔디 런웨이',
    r'사선 외벽 활용 → 6m 와이드 그레이 터프 (38m)',
    html
)

# New Section: Dual Program Strategy
new_program_section = '''  <!-- Program Strategy -->
  <section id="program" class="space-y-6">
    <div class="border-b border-slate-200 pb-4">
      <div class="text-xs font-bold text-brand-600 uppercase tracking-widest font-mono">Dual Program & Spatial Synergy</div>
      <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 mt-1">The Yard Gym 무드 · 6m 와이드 터프 & 24m 롱 커스텀 리그</h2>
      <p class="text-sm text-slate-500 mt-1">시야 방해물 0개 · 85평 완전 개방 아레나. 24m 일체형 롱 리그와 6m 와이드 그레이 터프로 압도적인 프리미엄 감성을 구현했습니다.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- HYB ZONE -->
      <div class="bg-white border-2 border-slate-300 rounded-3xl p-6 sm:p-8 space-y-4 shadow-sm relative overflow-hidden bg-gradient-to-br from-white via-slate-50 to-slate-100/50">
        <div class="flex items-center justify-between">
          <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-black bg-slate-800 text-white font-mono shadow-sm">
            ZONE 01 · 약 75평
          </span>
          <span class="text-xs font-bold text-slate-700 font-mono">THE YARD WIDE TURF</span>
        </div>
        <h3 class="text-2xl font-black text-slate-900">HYB 존 (6m 와이드 그레이 터프 아레나)</h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          'The Yard Gym' 감성의 세련된 차콜 그레이 잔디로 바닥 색상 대비를 최소화한 와이드 터프 존(폭 6.0m × 38m)입니다. 
          하이록스 썰매 밀기/당기기 동시 릴레이와 워킹 런지, 버피 브로드점프를 무제한 자유롭게 수행합니다.
        </p>
        
        <div class="grid grid-cols-2 gap-2 pt-2 text-xs font-medium text-slate-700">
          <div class="bg-white/80 border border-slate-200 rounded-xl p-2.5">
            <b class="text-slate-900 block text-xs">🏁 6m 와이드 그레이 터프</b>
            <span class="text-[11px] text-slate-500">폭 6m × 38m 광활한 잔디 스트립</span>
          </div>
          <div class="bg-white/80 border border-slate-200 rounded-xl p-2.5">
            <b class="text-slate-900 block text-xs">⚡ 공식 하이록스 레이스 멀티 트랙</b>
            <span class="text-[11px] text-slate-500">썰매 배틀 & 런지 동시 인터벌</span>
          </div>
          <div class="bg-white/80 border border-slate-200 rounded-xl p-2.5">
            <b class="text-slate-900 block text-xs">🚀 스타트 웜업 & 썰매 세팅 존</b>
            <span class="text-[11px] text-slate-500">서측 출발 버퍼 및 자유 웜업</span>
          </div>
          <div class="bg-white/80 border border-slate-200 rounded-xl p-2.5">
            <b class="text-slate-900 block text-xs">🎯 공식 규격 월볼 8구역</b>
            <span class="text-[11px] text-slate-500">남성 10ft / 여성 9ft 타겟 완비</span>
          </div>
        </div>
      </div>

      <!-- MET ZONE -->
      <div class="bg-white border-2 border-amber-300 rounded-3xl p-6 sm:p-8 space-y-4 shadow-sm relative overflow-hidden bg-gradient-to-br from-white via-amber-50/20 to-amber-100/30">
        <div class="flex items-center justify-between">
          <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-black bg-amber-600 text-white font-mono shadow-sm">
            ZONE 02 · 약 85평
          </span>
          <span class="text-xs font-bold text-amber-700 font-mono">24M RIG & OPEN ARENA</span>
        </div>
        <h3 class="text-2xl font-black text-slate-900">MET 존 (24m 롱 리그 & 85평 오픈 아레나)</h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          복도 축을 따라 1자로 웅장하게 뻗은 <b>24m 일체형 롱 커스텀 리그</b>(풀업 24인 동시 스테이션 + 스쿼트 8셀)와 <b>85평 완전 개방 오픈 플로어</b>를 구축했습니다. 
          동측 솔리드 벽면은 18m 전면 거울과 체조 핸드스탠드 푸시업(HSPU) 전용 벽면 및 수납랙으로 완성했습니다.
        </p>

        <div class="grid grid-cols-2 gap-2 pt-2 text-xs font-medium text-slate-700">
          <div class="bg-white/80 border border-amber-200 rounded-xl p-2.5">
            <b class="text-amber-700 block text-xs">🏗️ 24m 일체형 롱 커스텀 리그</b>
            <span class="text-[11px] text-slate-500">풀업 24인 동시 + 스쿼트 8셀</span>
          </div>
          <div class="bg-white/80 border border-amber-200 rounded-xl p-2.5">
            <b class="text-amber-700 block text-xs">🤸 18m 전면 거울 & HSPU 벽면</b>
            <span class="text-[11px] text-slate-500">핸드스탠드 푸시업 & 포토존</span>
          </div>
          <div class="bg-white/80 border border-amber-200 rounded-xl p-2.5">
            <b class="text-amber-700 block text-xs">🛡️ 85평 와이드 오픈 플로어</b>
            <span class="text-[11px] text-slate-500">고정 박스 0개 · 20~25인 단체 WOD</span>
          </div>
          <div class="bg-white/80 border border-amber-200 rounded-xl p-2.5">
            <b class="text-amber-700 block text-xs">📦 16m 빌트인 중량 장비 수납랙</b>
            <span class="text-[11px] text-slate-500">원판·덤벨·소도구 벽체 매립 정리</span>
          </div>
        </div>
      </div>
    </div>
  </section>'''

html = re.sub(r'  <!-- Program Strategy -->.*?  <!-- Floor Plan Layout -->', new_program_section + '\n\n  <!-- Floor Plan Layout -->', html, flags=re.S)

# New Layout Section with embedded SVG and deep architectural explanation
new_layout_section = f'''  <!-- Floor Plan Layout -->
  <section id="layout" class="space-y-6">
    <div class="border-b border-slate-200 pb-3 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
      <div>
        <div class="text-xs font-bold text-brand-600 uppercase tracking-widest font-mono">Master Floor Plan (Architectural Grade)</div>
        <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 mt-1">230평 공간구성 마스터플랜 (심층 인터뷰 반영 V2)</h2>
        <p class="text-xs sm:text-sm text-slate-500 mt-0.5">The Yard Gym 감성 차콜 터프(6m×38m) · 복도축 24m 롱 커스텀 리그 · 85평 오픈 아레나 · 남녀화장실 & 통유리 사우나/냉탕.</p>
      </div>
      <div class="flex items-center gap-2">
        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 border border-slate-300 text-xs font-bold font-mono">TURF 6m×38m</span>
        <span class="px-2.5 py-1 rounded-lg bg-amber-50 text-amber-700 border border-amber-200 text-xs font-bold font-mono">24m RIG</span>
        <span class="px-2.5 py-1 rounded-lg bg-sky-50 text-sky-700 border border-sky-200 text-xs font-bold font-mono">OPEN ARENA 85평</span>
      </div>
    </div>

    <!-- Interactive SVG Viewer Card -->
    <div class="bg-slate-950 border-2 border-slate-800 rounded-3xl p-4 sm:p-7 shadow-2xl overflow-hidden">
      {embedded_svg}
    </div>

    <!-- 4 Core Spatial Zones Breakdown -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-2">
      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-amber-500"></span>
          <b class="text-sm font-bold text-slate-900">01. 웰컴 라운지 & 무인 카페 (16평)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          지하주차장 직결 복도에서 들어서는 메인 관문. 
          인포데스크, 인바디 상담, 신발장 전실 및 스마트 무인 프로틴 바를 갖추어 인건비 0원의 24시간 가동형 F&B 구조를 확립했습니다.
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-slate-500"></span>
          <b class="text-sm font-bold text-slate-900">02. 전용 분리 화장실 (남/여 7평)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          락커룸을 거치지 않고 운동 플로어 및 라운지에서 즉시 이용 가능한 독립형 남녀 화장실. 
          남성(소변기 2·대변기 1·세면대), 여성(양변기 2·파우더 세면대)으로 호텔급 청결과 완벽한 프라이버시를 보장합니다.
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-sky-500"></span>
          <b class="text-sm font-bold text-slate-900">03. 스마트 락커 & 샤워실 (24평)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          남성(락커 36개·개별 샤워 4부스), 여성(락커 44개·개별 샤워 5부스·파우더룸)을 남측 배관축에 일체화. 
          완전 분리된 쾌적 단독 샤워룸(남4·여5)과 건습식 전실로 물기 없는 쾌적성을 유지합니다.
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-teal-500"></span>
          <b class="text-sm font-bold text-slate-900">04. 통유리 뷰 리커버리 스위트 (11평)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          편백 건식 사우나와 칠러 냉수욕조(3~5℃ Ice Plunge)에서 <b>전면 내열 강화유리 통창</b>을 통해 24m 롱 리그와 운동 아레나를 바라보며 휴식하는 최고급 웰니스 공간입니다.
        </p>
      </div>
    </div>
  </section>'''

html = re.sub(r'  <!-- Floor Plan Layout -->.*?  <!-- Business Model & Owner Value -->', new_layout_section + '\n\n  <!-- Business Model & Owner Value -->', html, flags=re.S)

# Innovation Comparison Table
new_comparison_section = '''  <!-- Architectural Innovation Comparison: Why this layout beats Claude's previous draft -->
  <section id="comparison" class="space-y-6">
    <div class="border-b border-slate-200 pb-4">
      <div class="text-xs font-bold text-brand-600 uppercase tracking-widest font-mono">Design Evolution & Quality Proof</div>
      <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 mt-1">왜 이번 공간구성이 압도적으로 우수한가?</h2>
      <p class="text-sm text-slate-500 mt-1">기존 구상안(클로드 초안)의 8대 치명적 결함을 심층 인터뷰를 통해 완벽히 해결했습니다.</p>
    </div>

    <div class="bg-white border border-slate-200 rounded-3xl overflow-hidden shadow-sm">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="bg-slate-100/80 border-b border-slate-200 text-slate-700">
              <th class="py-3.5 px-4 font-bold text-slate-900 w-1/5">핵심 설계 항목</th>
              <th class="py-3.5 px-4 font-bold text-slate-500 w-2/5">기존 초안 (클로드 구상안의 한계)</th>
              <th class="py-3.5 px-4 font-black text-brand-700 w-2/5 bg-brand-50/50">안티그래비티 프리미엄 마스터플랜</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-slate-600">
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">1. 공간 개방감 & 첫인상</td>
              <td class="py-3.5 px-4 text-slate-500">25m 대각선 철봉이 방 한가운데를 철책처럼 가로막아 230평이 좁은 삼각 쐐기방 2개로 전락</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">시야 방해물 0개!</span> 대각선 철봉을 없애고 복도 라인을 따라 24m 일체형 리그를 배치하여 문을 열자마자 160평 오픈 아레나가 한눈에 들어오는 압도적 웅장함 구현
              </td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">2. 기둥 간섭 & 안전성</td>
              <td class="py-3.5 px-4 text-slate-500">대각선 리그가 5번 기둥(G열)을 25cm 간격으로 아슬아슬하게 스치며 위험한 틈새와 데드스페이스 양산</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">복도 가로축 일체형 리그 정렬</span>로 기둥 간섭 0%, 공간 낭비 및 충돌 위험 0% 달성
              </td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">3. 터프 런웨이 (Turf Track)</td>
              <td class="py-3.5 px-4 text-slate-500">25m 단선 레인을 좁은 외벽 구석에 쑤셔넣어 가감속 여유 공간이 없고 2인 동시 훈련 불가</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">'The Yard Gym' 감성 6m 와이드 그레이 터프 (38m)</span> 구축으로 썰매 배틀, 런지, 버피 브로드점프 멀티 트랙 구현
              </td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">4. 오픈 플로어 & 자유로운 WOD</td>
              <td class="py-3.5 px-4 text-slate-500">대각선 리그와 고정 플랫폼으로 바닥이 갈가리 찢겨 단체 수업 시 자리 배치가 비좁고 비효율적</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">고정 플랫폼 박스 0개! 85평 완전 개방 오픈 플로어</span>로 설계하여 20~25명 동시 WOD, 바벨 훈련, 체조 서킷을 자유자재로 유연하게 세팅
              </td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">5. 동측 벽면 특화 (HSPU & 거울)</td>
              <td class="py-3.5 px-4 text-slate-500">벽면 전체에 거대한 리그를 붙여 전면 거울이나 체조 벽면 활용이 불가능</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">18m 전면 거울 + 크로스핏 HSPU(핸드스탠드 푸시업) 전용 벽면</span>과 16m 빌트인 장비 랙 및 네온 포토존 완비
              </td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">6. 샤워실 ↔ 운동 공간 분리</td>
              <td class="py-3.5 px-4 text-slate-500">라커룸 문이 운동 공간 한복판으로 열려 씻고 나온 회원이 바벨 떨어지는 공간을 가로질러 이동</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">2.4m 메인 보행 복도</span>를 별도 축으로 설계하여 샤워실 이용자와 24m 리그 및 격렬한 운동 구역 간 간섭을 100% 차단
              </td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">7. 화장실 & 사우나 조망 설계</td>
              <td class="py-3.5 px-4 text-slate-500">화장실이 누락되어 상가 공용 화장실로 나가야 하고, 사우나가 락커룸 깊숙이 막혀 답답한 폐쇄 구조</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">전용 분리형 화장실(복도 직결) + 통유리 뷰 리커버리 스위트</span>: 사우나와 냉탕 안에서 24m 리그와 광활한 아레나를 바라보며 릴랙스하는 최고급 호텔급 웰니스 경험
              </td>
            </tr>
            <tr>
              <td class="py-3.5 px-4 font-bold text-slate-900">8. 코칭 가시성 & 수업 통제</td>
              <td class="py-3.5 px-4 text-slate-500">가운데 세워진 25m 철봉 벽 때문에 코치가 반대편 구역 회원을 전혀 볼 수 없는 심각한 사각지대 발생</td>
              <td class="py-3.5 px-4 bg-brand-50/30 font-semibold text-slate-900">
                <span class="text-brand-600 font-bold">중앙 360도 무장애 시야선 + 3면 디지털 경기용 타이머</span>로 코치 1~2명이 230평 전역의 2개 클래스를 한눈에 완벽 지휘
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>'''

html = re.sub(r'  <!-- Architectural Innovation Comparison: Why this layout beats Claude\'s previous draft -->.*?  <!-- Investment & Revenue Logic -->', new_comparison_section + '\n\n  <!-- Investment & Revenue Logic -->', html, flags=re.S)

# Update Roadmap
html = re.sub(r'30m 듀얼 잔디 런웨이 \+ 올림픽 규격 플랫폼 \+ 16m 아레나 리그', r'6m 와이드 그레이 터프 (38m) + 24m 롱 커스텀 리그 + 18m HSPU 거울벽', html)

with open('kyerim-pitch.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated kyerim-pitch.html successfully! Total length:", len(html))
