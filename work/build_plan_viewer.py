# -*- coding: utf-8 -*-
"""
Generates the dedicated full-screen Master Plan Inspector: plan-viewer.html
Features ultra-smooth pan & zoom, preset focus points, high-res 4K links, and detailed zone inspector drawer.
"""

with open('work/plan.svg', 'r', encoding='utf-8') as f:
    svg_raw = f.read()

# Make sure SVG has an ID and proper classes for pan-zoom
svg_embedded = svg_raw.replace(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400"',
    '<svg id="planSvg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" class="w-full h-full select-none"'
)

html_content = f'''<!DOCTYPE html>
<html lang="ko" class="h-full bg-slate-950 text-slate-100">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>계림 지하1층 마스터플랜 고해상도 인터랙티브 뷰어 (230평 V4.2)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#F0FDF4',
              100: '#DCFCE7',
              400: '#4ADE80',
              500: '#22C55E',
              600: '#16A34A',
              700: '#15803D'
            }}
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
    body {{
      user-select: none;
      -webkit-user-select: none;
      touch-action: none;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 4px;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #334155;
      border-radius: 4px;
    }}
    .btn-pill {{
      transition: all 0.15s ease-in-out;
    }}
    .btn-pill:hover {{
      transform: translateY(-1px);
    }}
    .btn-pill:active {{
      transform: translateY(0);
    }}
  </style>
</head>
<body class="h-full flex flex-col overflow-hidden bg-[#090D16]">

  <!-- Top Navigation Header -->
  <header class="flex-none bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-4 py-2.5 z-40">
    <div class="max-w-[1920px] mx-auto flex items-center justify-between gap-3 flex-wrap">
      <div class="flex items-center gap-3">
        <div class="flex items-center gap-2">
          <a href="kyerim-pitch.html#layout" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium flex items-center gap-1 border border-slate-700 transition">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            공간기획 제안서 ↗
          </a>
        </div>
        <div class="h-4 w-px bg-slate-700 hidden sm:block"></div>
        <div>
          <h1 class="text-sm font-bold text-white flex items-center gap-2">
            <span>계림 지하1층 마스터플랜 (230평 V4.2)</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-brand-500/20 text-brand-400 border border-brand-500/30">ARCHITECTURAL CAD</span>
          </h1>
          <p class="text-[11px] text-slate-400 hidden md:block">
            마우스 휠로 확대/축소, 드래그로 이동 · 구역 버튼 클릭 시 해당 위치로 즉시 자동 줌인
          </p>
        </div>
      </div>

      <!-- Header Action Links -->
      <div class="flex items-center gap-2">
        <a href="plan-4k.png" target="_blank" class="px-3 py-1.5 rounded-lg bg-emerald-950/80 hover:bg-emerald-900 text-emerald-300 border border-emerald-700/60 text-xs font-bold font-mono flex items-center gap-1.5 shadow-sm transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          4K 원본 PNG (3840×2844)
        </a>
        <a href="work/plan.svg" target="_blank" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-mono flex items-center gap-1 transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
          SVG 벡터
        </a>
        <button id="toggleDrawerBtn" class="px-3 py-1.5 rounded-lg bg-sky-950/80 hover:bg-sky-900 text-sky-300 border border-sky-700/60 text-xs font-bold flex items-center gap-1.5 transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          구역 스펙
        </button>
      </div>
    </div>
  </header>

  <!-- Sub-Header: Quick Zone Preset Focus Buttons -->
  <div class="flex-none bg-slate-900/60 border-b border-slate-800/80 px-4 py-2 overflow-x-auto custom-scrollbar z-30">
    <div class="max-w-[1920px] mx-auto flex items-center gap-1.5 min-w-max text-xs">
      <span class="text-[11px] font-mono text-slate-500 font-bold mr-1">QUICK FOCUS:</span>
      <button onclick="zoomPreset('all')" class="btn-pill px-3 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-medium border border-slate-700 flex items-center gap-1.5">
        <span>🌐</span> 전체 마스터플랜
      </button>
      <button onclick="zoomPreset('metcon')" class="btn-pill px-3 py-1 rounded-lg bg-sky-950/80 hover:bg-sky-900 text-sky-300 font-bold border border-sky-700/60 flex items-center gap-1.5">
        <span>🏋️</span> METCON ZONE
      </button>
      <button onclick="zoomPreset('rig')" class="btn-pill px-3 py-1 rounded-lg bg-pink-950/80 hover:bg-pink-900 text-pink-300 font-bold border border-pink-700/60 flex items-center gap-1.5">
        <span>🏗️</span> 트윈 사각 RIG (각 7.2m · 6셀)
      </button>
      <button onclick="zoomPreset('turf')" class="btn-pill px-3 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-purple-300 font-bold border border-purple-800 flex items-center gap-1.5">
        <span>🏃</span> ROX ZONE (3.8m) &amp; 29m TURF
      </button>
      <button onclick="zoomPreset('erg')" class="btn-pill px-3 py-1 rounded-lg bg-lime-950/80 hover:bg-lime-900 text-lime-300 font-bold border border-lime-700/60 flex items-center gap-1.5">
        <span>🚴</span> G4좌측 바이크4 · 수납랙 · ROWs10
      </button>
      <button onclick="zoomPreset('community')" class="btn-pill px-3 py-1 rounded-lg bg-emerald-950/80 hover:bg-emerald-900 text-emerald-300 font-bold border border-emerald-700/60 flex items-center gap-1.5">
        <span>🏃‍♂️</span> 남측 에르그(2m) &amp; 1.5m 복도
      </button>
      <button onclick="zoomPreset('restroom')" class="btn-pill px-3 py-1 rounded-lg bg-indigo-950/80 hover:bg-indigo-900 text-indigo-300 font-bold border border-indigo-700/60 flex items-center gap-1.5">
        <span>🚻</span> 5m 화장실 &amp; 순간온수기실
      </button>
      <button onclick="zoomPreset('lockers')" class="btn-pill px-3 py-1 rounded-lg bg-purple-950/80 hover:bg-purple-900 text-purple-300 font-bold border border-purple-700/60 flex items-center gap-1.5">
        <span>🚿</span> 5m 탈의실 &amp; 5수전 개방형 샤워실
      </button>
      <button onclick="zoomPreset('lounge')" class="btn-pill px-3 py-1 rounded-lg bg-amber-950/80 hover:bg-amber-900 text-amber-300 font-bold border border-amber-700/60 flex items-center gap-1.5">
        <span>🚪</span> 6.55m 웰컴라운지
      </button>
    </div>
  </div>

  <!-- Main Workspace Area -->
  <div class="flex-1 relative flex overflow-hidden">
    
    <!-- Viewport Container (Interactive Canvas) -->
    <main id="viewport" class="flex-1 h-full w-full relative overflow-hidden bg-[#090D16] cursor-grab active:cursor-grabbing">
      
      <!-- Transform Target -->
      <div id="canvas" class="w-full h-full flex items-center justify-center transform-origin-center will-change-transform">
        <div id="svgWrapper" class="w-full h-full max-w-[1600px] max-h-[1100px] p-2 flex items-center justify-center">
          {svg_embedded}
        </div>
      </div>

      <!-- Floating Canvas Info Badge (Bottom Left) -->
      <div class="absolute bottom-5 left-5 z-20 pointer-events-none flex flex-col gap-1.5">
        <div class="bg-slate-900/90 backdrop-blur-md border border-slate-800 rounded-xl px-3.5 py-2 text-xs shadow-xl pointer-events-auto flex items-center gap-3">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-brand-500 animate-pulse"></span>
            <span class="text-slate-400 font-mono text-[11px]">ZOOM:</span>
            <span id="zoomLabel" class="font-mono font-bold text-white text-sm">100%</span>
          </div>
          <div class="h-3 w-px bg-slate-700"></div>
          <span class="text-[11px] text-slate-400 hidden sm:inline">더블클릭: 리셋 · 휠: 줌 · 드래그: 이동</span>
        </div>
      </div>

      <!-- Floating Zoom Controls (Bottom Right) -->
      <div class="absolute bottom-5 right-5 z-20 flex items-center gap-1.5 bg-slate-900/95 backdrop-blur-md border border-slate-800 p-1.5 rounded-2xl shadow-2xl">
        <button onclick="zoomBy(0.8)" title="축소 (Zoom Out)" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center text-lg font-bold border border-slate-700 transition">
          −
        </button>
        <button onclick="resetZoom()" title="기본 크기 (Reset 100%)" class="px-3 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-xs font-bold border border-slate-700 transition">
          1:1
        </button>
        <button onclick="zoomBy(1.25)" title="확대 (Zoom In)" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center text-lg font-bold border border-slate-700 transition">
          +
        </button>
        <div class="h-5 w-px bg-slate-700 mx-1"></div>
        <button onclick="toggleFullscreen()" title="전체화면 (Fullscreen)" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center border border-slate-700 transition">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
        </button>
      </div>

    </main>

    <!-- Side Zone Inspector Drawer -->
    <aside id="inspectorDrawer" class="w-80 md:w-96 flex-none bg-slate-900/95 backdrop-blur-md border-l border-slate-800 h-full overflow-y-auto custom-scrollbar p-5 space-y-6 z-30 transition-all duration-300">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-brand-400"></span>
          <h2 class="text-sm font-bold text-white uppercase tracking-wider font-mono">구역별 세부 스펙 안내</h2>
        </div>
        <button id="closeDrawerBtn" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>

      <div id="inspectorContent" class="space-y-4 text-xs">
        <!-- Default State: Summary of Layout V4.2 -->
        <div class="bg-slate-950/70 border border-slate-800 rounded-2xl p-4 space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-[11px] font-mono text-brand-400 font-bold">MASTER PLAN V4.2</span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-300">전체 230평</span>
          </div>
          <h3 class="text-base font-bold text-white">5m×3 남측 코어 (화장실·남탈의·여탈의) · 1.5m 복도 · 6.55m 웰컴라운지</h3>
          <p class="text-slate-400 leading-relaxed">
            남측 편의 코어를 <b class="text-indigo-300">① 남·여 화장실 통합 블록(5.0×5.5m · 순간 가스온수기 3대 실 포함)</b>, <b class="text-sky-300">② 남자 탈의·개방형 샤워실(5.0×5.5m · 5수전)</b>, <b class="text-purple-300">③ 여자 탈의·개방형 샤워실(5.0×5.5m · 5수전)</b>의 5m×3 균등 모듈로 완성했으며, <b class="text-lime-300">남측 에르그존(2.0m) + 코어 진입 복도(1.5m)</b> 및 <b class="text-amber-300">웰컴라운지(6.55×9.0m · 양문형 출입문)</b>로 직결했습니다.
          </p>
        </div>

        <!-- Workout Zone A: METCON ZONE -->
        <div class="bg-sky-950/20 border border-sky-800/40 rounded-2xl p-4 space-y-2 cursor-pointer hover:border-sky-500 transition" onclick="zoomPreset('rig')">
          <div class="flex items-center justify-between">
            <b class="text-sky-300 text-sm flex items-center gap-1.5">🏋️ W1. 기둥 사이 트윈 사각 스테이션 RIG</b>
            <span class="text-[10px] font-mono text-pink-400 font-bold">각 7.2m×1.8m (2세트) · 총 6스쿼트셀</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            기둥 G4~G5, G5~G6 사이 7.3m 공간에 <b class="text-pink-300">[셀 1.2m + 긴바 1.8m + 셀 1.2m + 긴바 1.8m + 셀 1.2m] 트윈 사각 RIG 세트(각 7.2m×1.8m)</b>를 기둥 세로 중앙(y=188~206)에 배치하여, 남측과 북측 모두 0.5m의 돌출 완충 여유를 두고 <b class="text-emerald-300">총 6개의 스쿼트 셀(세트당 3셀 × 2세트)</b>을 확보했습니다.
          </p>
        </div>

        <!-- Workout Zone B: Dual-Sided RIG & 29.0m HYROX + TURF -->
        <div class="bg-pink-950/20 border border-pink-800/40 rounded-2xl p-4 space-y-2 cursor-pointer hover:border-pink-500 transition" onclick="zoomPreset('turf')">
          <div class="flex items-center justify-between">
            <b class="text-pink-300 text-sm flex items-center gap-1.5">🏃 W2. ROX ZONE(3.8m) + 3레인 터프(3.0m)</b>
            <span class="text-[10px] font-mono text-emerald-400 font-bold">길이 29.0m · 3레인 (좌3·우3 출발)</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            사각 RIG 남측부터 터프 상단까지 <b class="text-purple-300">폭 3.8m × 길이 29.0m의 ROX ZONE 고무매트</b>를 조성하여 바벨 드랍존 및 덤벨/케틀벨/월볼 운동 공간을 확보했으며, 하단 <b class="text-emerald-300">폭 3.0m 3레인 터프(좌 3대 / 우 3대 출발)</b>와 직결됩니다.
          </p>
        </div>

        <!-- Workout Zone C: South Cardio Zone (SkiErg 6 + Curved Treadmill 6) + 1.5m Corridor -->
        <div class="bg-sky-950/20 border border-sky-800/40 rounded-2xl p-4 space-y-2 cursor-pointer hover:border-sky-500 transition" onclick="zoomPreset('community')">
          <div class="flex items-center justify-between">
            <b class="text-sky-300 text-sm flex items-center gap-1.5">🏃‍♂️ W3. 남측 에르그존 (2.0m) &amp; 진입 복도 (1.5m)</b>
            <span class="text-[10px] font-mono text-sky-400 font-bold">폭 15.0m × 깊이 3.5m (2.0m+1.5m)</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            무동력 트레드밀 길이(1.75m)에 맞춰 <b class="text-lime-300">남측 에르그존 깊이를 2.0m</b>(좌측 스키 6대 · 우측 트레드밀 6대)로 최적화하고, 에르그존 축소분(1.0m)과 코어 축소분(0.5m)을 합쳐 <b class="text-amber-300">폭 1.5m의 쾌적한 코어 진입 복도</b>를 확보했습니다.
          </p>
        </div>

        <!-- Workout Zone D: G4 Left BikeErgs & NW Diagonal Wall -->
        <div class="bg-lime-950/20 border border-lime-800/40 rounded-2xl p-4 space-y-2 cursor-pointer hover:border-lime-500 transition" onclick="zoomPreset('erg')">
          <div class="flex items-center justify-between">
            <b class="text-lime-300 text-sm flex items-center gap-1.5">🚴 W4. G4 좌측 바이크 4대 · 사선벽 수납랙 · ROWs 10대</b>
            <span class="text-[10px] font-mono text-lime-400 font-bold">기둥 G4 좌측 &amp; 사선벽 배치</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            기둥 G4 좌측(x=276~318)에 <b class="text-amber-300">바이크에르그 4대(남측 ROX·터프 조망)</b>를 배치하여 G3~G4 사이 2.9m 개방 통로를 확보하고, 북서 사선벽은 <b class="text-slate-200">12m 대형 빌트인 장비 수납랙</b>과 <b class="text-lime-200">ROWs(로잉 10대 직립보관)</b>로 정리했습니다.
          </p>
        </div>

        <!-- Zone 0: Welcome Lounge -->
        <div class="bg-amber-950/20 border border-amber-800/40 rounded-2xl p-4 space-y-2.5 cursor-pointer hover:border-amber-600 transition" onclick="zoomPreset('lounge')">
          <div class="flex items-center justify-between">
            <b class="text-amber-300 text-sm flex items-center gap-1.5">🚪 01. 웰컴 라운지 (내부 비움 · 양문형 도어)</b>
            <span class="text-[10px] font-mono text-amber-400 font-bold">17.85평 (6.55×9.0m · +0.1m 확장)</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            남측 코어 폭이 15.0m(5m×3)로 정리되면서 웰컴라운지 가로 폭이 <b class="text-amber-200">6.45m → 6.55m(17.85평)</b>로 넓어졌습니다. 서측 외벽에 <b class="text-amber-300">폭 2.0m 양문형 출입문(안팎 양방향 개폐)</b>만 표시하고 내부는 추후 구성을 위해 비워 두었습니다.
          </p>
        </div>

        <!-- Zone 1: Restrooms + Instant Gas Water Heater Room -->
        <div class="bg-indigo-950/20 border border-indigo-800/40 rounded-2xl p-4 space-y-2.5 cursor-pointer hover:border-indigo-600 transition" onclick="zoomPreset('restroom')">
          <div class="flex items-center justify-between">
            <b class="text-indigo-300 text-sm flex items-center gap-1.5">🚻 02. 남·여 화장실 &amp; 순간 가스온수기실</b>
            <span class="text-[10px] font-mono text-indigo-400 font-bold">8.3평 (5.0×5.5m · 남/여 각 2.5m)</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            북측 1.5m 복도에서 남·여 각각 독립 진입하며, 중앙 설비벽 양옆으로 <b class="text-emerald-300">세면대 2구씩 대칭 배치</b>하여 배관 효율을 높였습니다. 여자 화장실 대변기 3번 우측 하단 통로에는 <b class="text-emerald-300">슬라이딩 도어로 분리된 벽걸이 순간 가스온수기(3대) 실</b>을 구획했습니다.
          </p>
          <div class="grid grid-cols-2 gap-1.5 pt-1 text-[11px]">
            <div class="bg-indigo-950/40 border border-indigo-800/30 p-2 rounded-lg text-indigo-200">
              <span class="block text-[10px] text-indigo-400 font-mono">남자 (2.5×5.5m · 4.15평)</span>
              세면대 2 + 대변기 2칸 + 소변기 2대 + 좌하단 청소용 수전
            </div>
            <div class="bg-indigo-950/40 border border-indigo-800/30 p-2 rounded-lg text-indigo-200">
              <span class="block text-[10px] text-indigo-400 font-mono">여자 (2.5×5.5m · 4.15평)</span>
              세면대 2 + 대변기 3칸 + 슬라이딩 도어 순간온수기 3대 실
            </div>
          </div>
        </div>

        <!-- Zone 2: Men & Women Lockers (3.4m) + Open Showers (2.0m) -->
        <div class="bg-purple-950/20 border border-purple-800/40 rounded-2xl p-4 space-y-2.5 cursor-pointer hover:border-purple-600 transition" onclick="zoomPreset('lockers')">
          <div class="flex items-center justify-between">
            <b class="text-purple-300 text-sm flex items-center gap-1.5">🚿 03. 남·여 탈의실(3.4m) &amp; 개방형 샤워실(2.0m)</b>
            <span class="text-[10px] font-mono text-purple-400 font-bold">16.6평 (남·여 각 8.3평 · 5.0×5.5m)</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            우측 상단 출입문 진입 시 <b class="text-emerald-300">초록색 진입 통로(시선차단 복도)와 베이지색 시선차단 가벽</b>이 내부 노출을 막아주며, <b class="text-amber-300">옷장 락카 총 24칸</b>과 조적벽(0.1m) 북측면 <b class="text-yellow-300">건식 파우더 거울 3석</b>을 배치했습니다. 좌측 도어로 진입하는 샤워실(2.0m)은 <b class="text-sky-300">남·여 모두 5수전 통일</b> 및 뒤쪽 통로가 뚫린 <b class="text-sky-300">부분 파티션(개방형 샤워실)</b> 구조입니다.
          </p>
          <div class="grid grid-cols-2 gap-1.5 pt-1 text-[11px]">
            <div class="bg-purple-950/40 border border-purple-800/30 p-2 rounded-lg text-purple-200">
              <span class="block text-[10px] text-purple-400 font-mono">남자 (5.0×5.5m · 8.3평)</span>
              시선차단 통로·가벽 + 락카 24칸 + 파우더 3석 + 개방형 5수전
            </div>
            <div class="bg-purple-950/40 border border-purple-800/30 p-2 rounded-lg text-purple-200">
              <span class="block text-[10px] text-purple-400 font-mono">여자 (5.0×5.5m · 8.3평)</span>
              시선차단 통로·가벽 + 락카 24칸 + 파우더 3석 + 개방형 5수전
            </div>
          </div>
        </div>

      </div>
    </aside>

  </div>

  <script>
    (function() {{
      const viewport = document.getElementById('viewport');
      const canvas = document.getElementById('canvas');
      const zoomLabel = document.getElementById('zoomLabel');
      const drawer = document.getElementById('inspectorDrawer');
      const toggleDrawerBtn = document.getElementById('toggleDrawerBtn');
      const closeDrawerBtn = document.getElementById('closeDrawerBtn');

      // State
      let scale = 1.0;
      let tx = 0;
      let ty = 0;
      let isDragging = false;
      let startX = 0;
      let startY = 0;
      let initialPinchDist = 0;
      let initialPinchScale = 1.0;

      // Update Canvas CSS Transform
      function updateTransform(smooth = false) {{
        if (smooth) {{
          canvas.style.transition = 'transform 0.28s cubic-bezier(0.2, 0.8, 0.2, 1)';
        }} else {{
          canvas.style.transition = 'none';
        }}
        canvas.style.transform = `translate(${{tx}}px, ${{ty}}px) scale(${{scale}})`;
        zoomLabel.textContent = Math.round(scale * 100) + '%';
      }}

      // Reset
      window.resetZoom = function() {{
        scale = 1.0;
        tx = 0;
        ty = 0;
        updateTransform(true);
      }};

      // Zoom By Factor
      window.zoomBy = function(factor) {{
        const newScale = Math.min(Math.max(scale * factor, 0.8), 6.0);
        scale = newScale;
        updateTransform(true);
      }};

      // Wheel Zoom Centered at Cursor
      viewport.addEventListener('wheel', (e) => {{
        e.preventDefault();
        const rect = viewport.getBoundingClientRect();
        const mouseX = e.clientX - rect.left - rect.width / 2;
        const mouseY = e.clientY - rect.top - rect.height / 2;

        const zoomFactor = e.deltaY < 0 ? 1.15 : 0.87;
        const newScale = Math.min(Math.max(scale * zoomFactor, 0.8), 6.5);

        // Adjust translation to zoom towards cursor
        tx = mouseX - (mouseX - tx) * (newScale / scale);
        ty = mouseY - (mouseY - ty) * (newScale / scale);
        scale = newScale;

        updateTransform(false);
      }}, {{ passive: false }});

      // Mouse Drag to Pan
      viewport.addEventListener('mousedown', (e) => {{
        if (e.button !== 0) return;
        isDragging = true;
        startX = e.clientX - tx;
        startY = e.clientY - ty;
        viewport.classList.add('cursor-grabbing');
      }});

      window.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        tx = e.clientX - startX;
        ty = e.clientY - startY;
        updateTransform(false);
      }});

      window.addEventListener('mouseup', () => {{
        if (isDragging) {{
          isDragging = false;
          viewport.classList.remove('cursor-grabbing');
        }}
      }});

      // Double Click to Reset
      viewport.addEventListener('dblclick', (e) => {{
        if (scale > 1.2) {{
          resetZoom();
        }} else {{
          scale = 2.0;
          updateTransform(true);
        }}
      }});

      // Touch Events for Mobile / Tablet
      viewport.addEventListener('touchstart', (e) => {{
        if (e.touches.length === 1) {{
          isDragging = true;
          startX = e.touches[0].clientX - tx;
          startY = e.touches[0].clientY - ty;
        }} else if (e.touches.length === 2) {{
          isDragging = false;
          initialPinchDist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
          initialPinchScale = scale;
        }}
      }}, {{ passive: false }});

      viewport.addEventListener('touchmove', (e) => {{
        e.preventDefault();
        if (isDragging && e.touches.length === 1) {{
          tx = e.touches[0].clientX - startX;
          ty = e.touches[0].clientY - startY;
          updateTransform(false);
        }} else if (e.touches.length === 2) {{
          const dist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
          if (initialPinchDist > 0) {{
            const newScale = Math.min(Math.max(initialPinchScale * (dist / initialPinchDist), 0.8), 6.5);
            scale = newScale;
            updateTransform(false);
          }}
        }}
      }}, {{ passive: false }});

      viewport.addEventListener('touchend', () => {{
        isDragging = false;
      }});

      // Preset Zoom Focus Targets in SVG coordinates (0 0 540 400)
      const PRESETS = {{
        all: {{ x: 270, y: 200, s: 1.0 }},
        metcon: {{ x: 380, y: 130, s: 2.1 }},
        rig: {{ x: 401, y: 202, s: 2.5 }},
        turf: {{ x: 341, y: 242, s: 2.2 }},
        treadmill: {{ x: 335, y: 290, s: 2.8 }},
        erg: {{ x: 260, y: 155, s: 2.2 }},
        community: {{ x: 302.5, y: 295, s: 2.8 }},
        restroom: {{ x: 252.5, y: 340, s: 3.4 }},
        lockers: {{ x: 327.5, y: 340, s: 2.8 }},
        lounge: {{ x: 194.75, y: 323, s: 3.0 }}
      }};

      window.zoomPreset = function(name) {{
        const p = PRESETS[name];
        if (!p) return;

        const rect = canvas.getBoundingClientRect();
        // Calculate offset so that (p.x / 540, p.y / 400) aligns to center
        const targetX = (0.5 - (p.x / 540)) * rect.width * p.s;
        const targetY = (0.5 - (p.y / 400)) * rect.height * p.s;

        scale = p.s;
        tx = targetX;
        ty = targetY;
        updateTransform(true);
      }};

      // Fullscreen Toggle
      window.toggleFullscreen = function() {{
        if (!document.fullscreenElement) {{
          document.documentElement.requestFullscreen().catch(err => {{
            console.log("Fullscreen request failed", err);
          }});
        }} else {{
          document.exitFullscreen();
        }}
      }};

      // Drawer Toggle
      function toggleDrawer() {{
        drawer.classList.toggle('hidden');
      }}
      toggleDrawerBtn.addEventListener('click', toggleDrawer);
      closeDrawerBtn.addEventListener('click', () => drawer.classList.add('hidden'));

      // Keyboard Shortcuts
      window.addEventListener('keydown', (e) => {{
        if (e.key === '+' || e.key === '=') zoomBy(1.2);
        if (e.key === '-' || e.key === '_') zoomBy(0.8);
        if (e.key === '0') resetZoom();
        if (e.key === 'f' || e.key === 'F') toggleFullscreen();
        if (e.key === 'Escape' && !drawer.classList.contains('hidden')) {{
          drawer.classList.add('hidden');
        }}
      }});

      // Initial Fit
      resetZoom();
    }})();
  </script>
</body>
</html>
'''

with open('plan-viewer.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created plan-viewer.html successfully! File size:", len(html_content))
