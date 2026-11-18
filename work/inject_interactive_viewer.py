# -*- coding: utf-8 -*-
"""
Injects full interactive pan & zoom controls and fullscreen modal into kyerim-pitch.html and kyerim-internal.html.
"""
import re

with open('work/plan.svg', 'r', encoding='utf-8') as f:
    master_svg = f.read()

# Responsive embedded SVG
embedded_svg = master_svg.replace(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400"',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" class="w-full h-full select-none"'
)

# -------------------------------------------------------------
# 1. UPDATE KYERIM-PITCH.HTML
# -------------------------------------------------------------
with open('kyerim-pitch.html', 'r', encoding='utf-8') as f:
    pitch_html = f.read()

pitch_layout_section = f'''  <!-- Floor Plan Layout -->
  <section id="layout" class="space-y-6">
    <div class="border-b border-slate-200 pb-3 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
      <div>
        <div class="text-xs font-bold text-brand-600 uppercase tracking-widest font-mono">Master Floor Plan (Architectural Grade · V3.0)</div>
        <h2 class="text-2xl sm:text-3xl font-bold text-slate-900 mt-1">230평 운동공간 마스터플랜 (A안+1안 · 4대 구역 전면 재편 V3.0)</h2>
        <p class="text-xs sm:text-sm text-slate-500 mt-0.5">21m 양면 커스텀 RIG 기준 상단 METCON 존(68평) · 하단 하이록스 스트렝스+4레인 직선 TURF(54.5평) · 수직 ERG ZONE 23대(18.2평) · 좌측 역도+개인운동(19.5평)</p>
      </div>
      <div class="flex items-center gap-2 flex-wrap">
        <span class="px-2.5 py-1 rounded-lg bg-fuchsia-50 text-fuchsia-700 border border-fuchsia-200 text-xs font-bold font-mono">21m 양면 RIG</span>
        <span class="px-2.5 py-1 rounded-lg bg-lime-50 text-lime-700 border border-lime-300 text-xs font-bold font-mono">ERG ZONE 23대</span>
        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-800 border border-slate-300 text-xs font-bold font-mono">4레인 직선 TURF</span>
      </div>
    </div>

    <!-- Interactive SVG Viewer Card -->
    <div class="bg-slate-950 border-2 border-slate-800 rounded-3xl p-3 sm:p-5 shadow-2xl overflow-hidden space-y-3">
      <!-- Top Toolbar -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="px-2.5 py-1 rounded-md bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-[11px] font-mono font-bold flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            INTERACTIVE PAN &amp; ZOOM
          </span>
          <span class="text-xs text-slate-400 hidden lg:inline">마우스 휠로 줌, 드래그로 이동, 더블클릭으로 리셋</span>
        </div>

        <!-- Controls -->
        <div class="flex items-center gap-2 flex-wrap">
          <div class="flex items-center bg-slate-900 border border-slate-800 rounded-xl p-1 gap-1">
            <button id="pZoomOut" class="w-8 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold transition flex items-center justify-center">−</button>
            <button id="pZoomReset" class="px-2.5 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-[11px] font-bold transition">1:1</button>
            <button id="pZoomIn" class="w-8 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold transition flex items-center justify-center">+</button>
            <span id="pZoomBadge" class="px-2 font-mono text-[11px] font-bold text-brand-400 min-w-[42px] text-center">100%</span>
          </div>

          <button id="pFullscreenBtn" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold flex items-center gap-1.5 transition shadow-sm" title="전체화면 팝업 뷰어">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
            <span>전체화면</span>
          </button>

          <a href="plan-viewer.html" target="_blank" class="px-3 py-1.5 rounded-xl bg-sky-950/80 hover:bg-sky-900 text-sky-300 border border-sky-700/60 text-xs font-bold flex items-center gap-1.5 transition">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
            <span>전용 뷰어 웹앱</span>
          </a>

          <a href="plan-4k.png" target="_blank" class="px-3 py-1.5 rounded-xl bg-emerald-950/80 hover:bg-emerald-900 text-emerald-300 border border-emerald-700/60 text-xs font-bold font-mono flex items-center gap-1.5 transition">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            <span>4K 원본</span>
          </a>
        </div>
      </div>

      <!-- Quick Preset Focus Buttons -->
      <div class="flex items-center gap-1.5 overflow-x-auto custom-scrollbar pb-1 text-xs">
        <span class="text-[10px] font-mono text-slate-500 font-bold whitespace-nowrap">구역 자동 줌:</span>
        <button onclick="pPreset('all')" class="px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap">🌐 전체</button>
        <button onclick="pPreset('metcon')" class="px-2.5 py-1 rounded-lg bg-sky-950/80 hover:bg-sky-900 text-sky-300 border border-sky-800/80 font-bold whitespace-nowrap">🏋️ METCON 존 (68평)</button>
        <button onclick="pPreset('rig')" class="px-2.5 py-1 rounded-lg bg-fuchsia-950/80 hover:bg-fuchsia-900 text-fuchsia-300 border border-fuchsia-800/80 font-bold whitespace-nowrap">🩷 21m 양면 RIG</button>
        <button onclick="pPreset('turf')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600 font-bold whitespace-nowrap">🏃 하이록스+4레인 TURF</button>
        <button onclick="pPreset('erg')" class="px-2.5 py-1 rounded-lg bg-lime-950/80 hover:bg-lime-900 text-lime-300 border border-lime-700/80 font-bold whitespace-nowrap">🟢 ERG 존 (23대)</button>
        <button onclick="pPreset('opengym')" class="px-2.5 py-1 rounded-lg bg-amber-950/80 hover:bg-amber-900 text-amber-300 border border-amber-800/80 font-bold whitespace-nowrap">🏋️‍♂️ 역도+개인운동</button>
        <button onclick="pPreset('recovery')" class="px-2.5 py-1 rounded-lg bg-teal-950/80 hover:bg-teal-900 text-teal-300 border border-teal-800/80 font-bold whitespace-nowrap">🧖 리커버리</button>
        <button onclick="pPreset('lockers')" class="px-2.5 py-1 rounded-lg bg-purple-950/80 hover:bg-purple-900 text-purple-300 border border-purple-800/80 font-bold whitespace-nowrap">🚿 락커·샤워실</button>
      </div>

      <!-- Viewport Canvas -->
      <div id="pViewport" class="relative w-full h-[460px] sm:h-[560px] lg:h-[640px] rounded-2xl overflow-hidden bg-[#090D16] border border-slate-800 cursor-grab active:cursor-grabbing">
        <div id="pCanvas" class="w-full h-full flex items-center justify-center transform-origin-center will-change-transform">
          <div class="w-full h-full flex items-center justify-center p-2">
            {embedded_svg}
          </div>
        </div>
        <div class="absolute bottom-3 left-3 pointer-events-none bg-slate-900/90 backdrop-blur-sm border border-slate-800 rounded-lg px-2.5 py-1 text-[11px] text-slate-400 hidden sm:block">
          💡 마우스 휠로 확대/축소, 드래그하여 이동할 수 있습니다.
        </div>
      </div>
    </div>

    <!-- 4 Core Spatial Zones Breakdown -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-2">
      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-amber-500"></span>
          <b class="text-sm font-bold text-slate-900">01. 웰컴 라운지 &amp; 카페 (17.6평 / 6.45×9.0m)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          지하주차장 통로에서 직결되는 메인 관문. 
          남측벽 밀착 인포데스크 &amp; 인바디 존, 슬림 무인 프로틴 바(2.5m) 및 13.7평 오픈 커뮤니티 라운지·스트레칭 매트 존을 갖추었습니다.
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-indigo-500"></span>
          <b class="text-sm font-bold text-slate-900">02. 남녀 독립 화장실 (4.7평 / 2.6×6.0m)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          라운지 직결 진입 호텔식 독립 화장실 (남녀 동일 출입문 위치). 
          남성(대변 2·소변 2·손 세면 여유공간 1.2m 확보), 여성(대변 3·세면 1)으로 파티션 간섭 없는 쾌적 개방형 레이아웃입니다.
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-teal-500"></span>
          <b class="text-sm font-bold text-slate-900">03. 통유리 뷰 리커버리 스위트 (6.4평 / 3.5×6.0m)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          북측 통유리 전망 칠러 급냉탕(3~5℃ Ice Plunge)과 남측 벽 밀착 2단 계단식 편백 건식사우나(우측벽 안전 히터)로 이어지는 럭셔리 웰니스 공간입니다.
        </p>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-4 space-y-2 shadow-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-purple-500"></span>
          <b class="text-sm font-bold text-slate-900">04. 4.5m 동등 락커 &amp; 조적벽 해바라기 샤워실 (16.4평)</b>
        </div>
        <p class="text-xs text-slate-500 leading-relaxed">
          남녀 각 4.5m 폭(8.2평)으로 동일화. 건습식 전실과 부스를 조적벽과 해바라기 수전(남4·여5) 및 강화유리 파티션으로 대체하여 탈의실 깊이를 4.45m로 대폭 확장했습니다. 시선차단 2단 락카 22칸과 스탠딩 중앙 파우더(3석)+세면대(2구)를 완비했습니다.
        </p>
      </div>
    </div>
  </section>'''

# Replace layout section in pitch_html
pitch_html = re.sub(
    r'  <!-- Floor Plan Layout -->.*?  <!-- Business Model & Owner Value -->',
    pitch_layout_section + '\n\n  <!-- Business Model & Owner Value -->',
    pitch_html,
    flags=re.S
)

# Add Fullscreen Modal Markup before </body>
modal_markup = f'''<!-- Fullscreen Plan Modal -->
<div id="pModal" class="fixed inset-0 z-[100] bg-slate-950/95 backdrop-blur-md hidden flex-col p-3 sm:p-5">
  <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-2 flex-none">
    <div class="flex items-center gap-3">
      <span class="text-sm font-bold text-white font-mono flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
        계림동 마스터플랜 전체화면 뷰어 (230평 V3.0 · A안+1안)
      </span>
      <span id="pModalBadge" class="px-2 py-0.5 rounded bg-slate-800 font-mono text-xs text-brand-400 font-bold">100%</span>
    </div>
    <div class="flex items-center gap-2">
      <a href="plan-4k.png" target="_blank" class="px-3 py-1.5 rounded-lg bg-emerald-950 text-emerald-300 border border-emerald-700 text-xs font-mono font-bold">
        4K 다운로드
      </a>
      <button id="pCloseModal" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs border border-slate-700">
        ✕ 닫기 (ESC)
      </button>
    </div>
  </div>

  <div class="flex items-center gap-1.5 overflow-x-auto custom-scrollbar pb-2 mb-2 flex-none text-xs">
    <button onclick="pModalPreset('all')" class="px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800">🌐 전체</button>
    <button onclick="pModalPreset('metcon')" class="px-2.5 py-1 rounded-lg bg-sky-950/80 text-sky-300 border border-sky-700 font-bold">🏋️ METCON 존</button>
    <button onclick="pModalPreset('rig')" class="px-2.5 py-1 rounded-lg bg-fuchsia-950/80 text-fuchsia-300 border border-fuchsia-700 font-bold">🩷 21m 양면 RIG</button>
    <button onclick="pModalPreset('turf')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 border border-slate-600 font-bold">🏃 하이록스+4레인 TURF</button>
    <button onclick="pModalPreset('erg')" class="px-2.5 py-1 rounded-lg bg-lime-950/80 text-lime-300 border border-lime-700 font-bold">🟢 ERG 존 (23대)</button>
    <button onclick="pModalPreset('opengym')" class="px-2.5 py-1 rounded-lg bg-amber-950/80 text-amber-300 border border-amber-700 font-bold">🏋️‍♂️ 역도+개인운동</button>
    <button onclick="pModalPreset('recovery')" class="px-2.5 py-1 rounded-lg bg-teal-950/80 text-teal-300 border border-teal-700 font-bold">🧖 리커버리</button>
    <button onclick="pModalPreset('lockers')" class="px-2.5 py-1 rounded-lg bg-purple-950/80 text-purple-300 border border-purple-700 font-bold">🚿 락커·샤워실</button>
  </div>

  <div id="pModalViewport" class="flex-1 w-full h-full relative overflow-hidden bg-[#090D16] rounded-2xl border border-slate-800 cursor-grab active:cursor-grabbing">
    <div id="pModalCanvas" class="w-full h-full flex items-center justify-center transform-origin-center will-change-transform">
      <div class="w-full h-full flex items-center justify-center p-2">
        {embedded_svg}
      </div>
    </div>
  </div>
</div>

<script>
// Master Plan Pan-Zoom Engine
(function() {{
  function initPanZoom(viewportId, canvasId, badgeId) {{
    const viewport = document.getElementById(viewportId);
    const canvas = document.getElementById(canvasId);
    const badge = document.getElementById(badgeId);
    if (!viewport || !canvas) return null;

    let scale = 1.0;
    let tx = 0;
    let ty = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    function update(smooth = false) {{
      canvas.style.transition = smooth ? 'transform 0.28s cubic-bezier(0.2, 0.8, 0.2, 1)' : 'none';
      canvas.style.transform = `translate(${{tx}}px, ${{ty}}px) scale(${{scale}})`;
      if (badge) badge.textContent = Math.round(scale * 100) + '%';
    }}

    function reset() {{
      scale = 1.0;
      tx = 0;
      ty = 0;
      update(true);
    }}

    function zoom(factor) {{
      scale = Math.min(Math.max(scale * factor, 0.8), 6.0);
      update(true);
    }}

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const rect = viewport.getBoundingClientRect();
      const mouseX = e.clientX - rect.left - rect.width / 2;
      const mouseY = e.clientY - rect.top - rect.height / 2;
      const factor = e.deltaY < 0 ? 1.15 : 0.87;
      const newScale = Math.min(Math.max(scale * factor, 0.8), 6.5);
      tx = mouseX - (mouseX - tx) * (newScale / scale);
      ty = mouseY - (mouseY - ty) * (newScale / scale);
      scale = newScale;
      update(false);
    }}, {{ passive: false }});

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
      update(false);
    }});

    window.addEventListener('mouseup', () => {{
      if (isDragging) {{
        isDragging = false;
        viewport.classList.remove('cursor-grabbing');
      }}
    }});

    viewport.addEventListener('dblclick', () => {{
      if (scale > 1.2) reset();
      else {{ scale = 2.0; update(true); }}
    }});

    // Touch
    let initDist = 0, initScale = 1.0;
    viewport.addEventListener('touchstart', (e) => {{
      if (e.touches.length === 1) {{
        isDragging = true;
        startX = e.touches[0].clientX - tx;
        startY = e.touches[0].clientY - ty;
      }} else if (e.touches.length === 2) {{
        isDragging = false;
        initDist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        initScale = scale;
      }}
    }}, {{ passive: false }});

    viewport.addEventListener('touchmove', (e) => {{
      e.preventDefault();
      if (isDragging && e.touches.length === 1) {{
        tx = e.touches[0].clientX - startX;
        ty = e.touches[0].clientY - startY;
        update(false);
      }} else if (e.touches.length === 2 && initDist > 0) {{
        const dist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        scale = Math.min(Math.max(initScale * (dist / initDist), 0.8), 6.5);
        update(false);
      }}
    }}, {{ passive: false }});

    viewport.addEventListener('touchend', () => {{ isDragging = false; }});

    const PRESETS = {{
      all: {{ x: 270, y: 200, s: 1.0 }},
      metcon: {{ x: 380, y: 125, s: 2.1 }},
      rig: {{ x: 358, y: 197, s: 2.4 }},
      turf: {{ x: 341, y: 242, s: 2.2 }},
      erg: {{ x: 195, y: 220, s: 2.9 }},
      opengym: {{ x: 155, y: 240, s: 3.2 }},
      recovery: {{ x: 273.5, y: 323, s: 3.2 }},
      restroom: {{ x: 235, y: 323, s: 3.2 }},
      lockers: {{ x: 335, y: 323, s: 2.5 }},
      lounge: {{ x: 189, y: 323, s: 3.0 }}
    }};

    function setPreset(name) {{
      const p = PRESETS[name];
      if (!p) return;
      const rect = canvas.getBoundingClientRect();
      tx = (0.5 - (p.x / 540)) * rect.width * p.s;
      ty = (0.5 - (p.y / 400)) * rect.height * p.s;
      scale = p.s;
      update(true);
    }}

    return {{ reset, zoom, setPreset }};
  }}

  const pitchViewer = initPanZoom('pViewport', 'pCanvas', 'pZoomBadge');
  const modalViewer = initPanZoom('pModalViewport', 'pModalCanvas', 'pModalBadge');

  window.pPreset = (name) => pitchViewer && pitchViewer.setPreset(name);
  window.pModalPreset = (name) => modalViewer && modalViewer.setPreset(name);

  document.getElementById('pZoomIn')?.addEventListener('click', () => pitchViewer?.zoom(1.25));
  document.getElementById('pZoomOut')?.addEventListener('click', () => pitchViewer?.zoom(0.8));
  document.getElementById('pZoomReset')?.addEventListener('click', () => pitchViewer?.reset());

  const modal = document.getElementById('pModal');
  const openModalBtn = document.getElementById('pFullscreenBtn');
  const closeModalBtn = document.getElementById('pCloseModal');

  function openModal() {{
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    modalViewer?.reset();
  }}

  function closeModal() {{
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }}

  openModalBtn?.addEventListener('click', openModal);
  closeModalBtn?.addEventListener('click', closeModal);

  window.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) closeModal();
  }});
}})();
</script>
'''

# Remove any previous pModal or PanZoom scripts if present
pitch_html = re.sub(r'<!-- Fullscreen Plan Modal -->.*?</body>', '</body>', pitch_html, flags=re.S)
pitch_html = pitch_html.replace('</body>', modal_markup + '\n</body>')

with open('kyerim-pitch.html', 'w', encoding='utf-8') as f:
    f.write(pitch_html)

print("Updated kyerim-pitch.html successfully!")

# -------------------------------------------------------------
# 2. UPDATE KYERIM-INTERNAL.HTML
# -------------------------------------------------------------
with open('kyerim-internal.html', 'r', encoding='utf-8') as f:
    internal_html = f.read()

# Update Space & Plan section in internal_html
internal_space_section = f'''  <!-- Space & SVG Plan -->
  <section id="space" class="space-y-4">
    <div class="border-b border-dark-border pb-3 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
      <div>
        <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Floor Plan &amp; Zoning Masterplan (V3.0 · A안+1안)</div>
        <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">지하 230평 운동공간 레이아웃 구상도 (V3.0 · 4대 구역 전면 재편)</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-0.5">21m 양면 커스텀 RIG 기준 상단 METCON 존(68평) · 하단 하이록스 스트렝스+4레인 직선 TURF(54.5평) · 수직 ERG ZONE 23대(18.2평) · 좌측 역도+개인운동(19.5평)</p>
      </div>
      <div class="flex items-center gap-2 flex-wrap">
        <span class="px-2.5 py-1 rounded-lg bg-fuchsia-500/10 text-fuchsia-400 border border-fuchsia-500/30 text-xs font-bold font-mono">21m 양면 RIG</span>
        <span class="px-2.5 py-1 rounded-lg bg-lime-500/10 text-lime-400 border border-lime-500/30 text-xs font-bold font-mono">ERG 23대</span>
        <span class="px-2.5 py-1 rounded-lg bg-slate-500/10 text-slate-300 border border-slate-500/30 text-xs font-bold font-mono">4레인 직선 TURF</span>
      </div>
    </div>

    <!-- Interactive Viewer Card -->
    <div class="bg-dark-card border border-dark-border rounded-2xl p-3 sm:p-5 overflow-hidden space-y-3">
      <!-- Top Toolbar -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-dark-border/80 pb-3">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="px-2.5 py-1 rounded-md bg-brand-500/20 text-brand-400 border border-brand-500/30 text-[11px] font-mono font-bold flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-brand-400 animate-pulse"></span>
            INTERACTIVE PAN &amp; ZOOM
          </span>
          <span class="text-xs text-slate-400 hidden lg:inline">마우스 휠로 줌, 드래그로 이동, 더블클릭으로 리셋</span>
        </div>

        <!-- Controls -->
        <div class="flex items-center gap-2 flex-wrap">
          <div class="flex items-center bg-slate-900 border border-dark-border rounded-xl p-1 gap-1">
            <button id="intZoomOut" class="w-8 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold transition flex items-center justify-center">−</button>
            <button id="intZoomReset" class="px-2.5 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-[11px] font-bold transition">1:1</button>
            <button id="intZoomIn" class="w-8 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold transition flex items-center justify-center">+</button>
            <span id="intZoomBadge" class="px-2 font-mono text-[11px] font-bold text-brand-400 min-w-[42px] text-center">100%</span>
          </div>

          <button id="intFullscreenBtn" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-dark-border text-xs font-bold flex items-center gap-1.5 transition" title="전체화면 팝업 뷰어">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
            <span>전체화면</span>
          </button>

          <a href="plan-viewer.html" target="_blank" class="px-3 py-1.5 rounded-xl bg-sky-950/80 hover:bg-sky-900 text-sky-300 border border-sky-700/60 text-xs font-bold flex items-center gap-1.5 transition">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
            <span>전용 뷰어 웹앱</span>
          </a>

          <a href="plan-4k.png" target="_blank" class="px-3 py-1.5 rounded-xl bg-emerald-950/80 hover:bg-emerald-900 text-emerald-300 border border-emerald-700/60 text-xs font-bold font-mono flex items-center gap-1.5 transition">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            <span>4K 원본</span>
          </a>
        </div>
      </div>

      <!-- Quick Preset Focus Buttons -->
      <div class="flex items-center gap-1.5 overflow-x-auto custom-scrollbar pb-1 text-xs">
        <span class="text-[10px] font-mono text-slate-500 font-bold whitespace-nowrap">구역 자동 줌:</span>
        <button onclick="intPreset('all')" class="px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap">🌐 전체</button>
        <button onclick="intPreset('metcon')" class="px-2.5 py-1 rounded-lg bg-sky-950/80 hover:bg-sky-900 text-sky-300 border border-sky-800/80 font-bold whitespace-nowrap">🏋️ METCON 존 (68평)</button>
        <button onclick="intPreset('rig')" class="px-2.5 py-1 rounded-lg bg-fuchsia-950/80 hover:bg-fuchsia-900 text-fuchsia-300 border border-fuchsia-800/80 font-bold whitespace-nowrap">🩷 21m 양면 RIG</button>
        <button onclick="intPreset('turf')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600 font-bold whitespace-nowrap">🏃 하이록스+4레인 TURF</button>
        <button onclick="intPreset('erg')" class="px-2.5 py-1 rounded-lg bg-lime-950/80 hover:bg-lime-900 text-lime-300 border border-lime-700/80 font-bold whitespace-nowrap">🟢 ERG 존 (23대)</button>
        <button onclick="intPreset('opengym')" class="px-2.5 py-1 rounded-lg bg-amber-950/80 hover:bg-amber-900 text-amber-300 border border-amber-800/80 font-bold whitespace-nowrap">🏋️‍♂️ 역도+개인운동</button>
        <button onclick="intPreset('recovery')" class="px-2.5 py-1 rounded-lg bg-teal-950/80 hover:bg-teal-900 text-teal-300 border border-teal-800/80 font-bold whitespace-nowrap">🧖 리커버리</button>
        <button onclick="intPreset('lockers')" class="px-2.5 py-1 rounded-lg bg-purple-950/80 hover:bg-purple-900 text-purple-300 border border-purple-800/80 font-bold whitespace-nowrap">🚿 락커·샤워실</button>
      </div>

      <!-- Viewport Canvas -->
      <div id="intViewport" class="relative w-full h-[460px] sm:h-[560px] lg:h-[640px] rounded-2xl overflow-hidden bg-[#090D16] border border-dark-border cursor-grab active:cursor-grabbing">
        <div id="intCanvas" class="w-full h-full flex items-center justify-center transform-origin-center will-change-transform">
          <div class="w-full h-full flex items-center justify-center p-2">
            {embedded_svg}
          </div>
        </div>
        <div class="absolute bottom-3 left-3 pointer-events-none bg-slate-900/90 backdrop-blur-sm border border-slate-800 rounded-lg px-2.5 py-1 text-[11px] text-slate-400 hidden sm:block">
          💡 마우스 휠로 확대/축소, 드래그하여 이동할 수 있습니다.
        </div>
      </div>
    </div>
  </section>'''

# Replace Space section in internal_html
internal_html = re.sub(
    r'  <!-- Space & SVG Plan -->.*?  <!-- Capex Detail -->',
    internal_space_section + '\n\n  <!-- Capex Detail -->',
    internal_html,
    flags=re.S
)

# Add Modal & Script to internal_html before </body>
internal_modal_markup = f'''<!-- Fullscreen Plan Modal (Internal Review) -->
<div id="intModal" class="fixed inset-0 z-[100] bg-slate-950/95 backdrop-blur-md hidden flex-col p-3 sm:p-5">
  <div class="flex items-center justify-between border-b border-dark-border pb-3 mb-2 flex-none">
    <div class="flex items-center gap-3">
      <span class="text-sm font-bold text-white font-mono flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-brand-400 animate-pulse"></span>
        계림동 마스터플랜 전체화면 뷰어 (230평 V3.0 · A안+1안)
      </span>
      <span id="intModalBadge" class="px-2 py-0.5 rounded bg-slate-800 font-mono text-xs text-brand-400 font-bold">100%</span>
    </div>
    <div class="flex items-center gap-2">
      <a href="plan-4k.png" target="_blank" class="px-3 py-1.5 rounded-lg bg-emerald-950 text-emerald-300 border border-emerald-700 text-xs font-mono font-bold">
        4K 다운로드
      </a>
      <button id="intCloseModal" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs border border-dark-border">
        ✕ 닫기 (ESC)
      </button>
    </div>
  </div>

  <div class="flex items-center gap-1.5 overflow-x-auto custom-scrollbar pb-2 mb-2 flex-none text-xs">
    <button onclick="intModalPreset('all')" class="px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800">🌐 전체</button>
    <button onclick="intModalPreset('metcon')" class="px-2.5 py-1 rounded-lg bg-sky-950/80 text-sky-300 border border-sky-700 font-bold">🏋️ METCON 존</button>
    <button onclick="intModalPreset('rig')" class="px-2.5 py-1 rounded-lg bg-fuchsia-950/80 text-fuchsia-300 border border-fuchsia-700 font-bold">🩷 21m 양면 RIG</button>
    <button onclick="intModalPreset('turf')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 border border-slate-600 font-bold">🏃 하이록스+4레인 TURF</button>
    <button onclick="intModalPreset('erg')" class="px-2.5 py-1 rounded-lg bg-lime-950/80 text-lime-300 border border-lime-700 font-bold">🟢 ERG 존 (23대)</button>
    <button onclick="intModalPreset('opengym')" class="px-2.5 py-1 rounded-lg bg-amber-950/80 text-amber-300 border border-amber-700 font-bold">🏋️‍♂️ 역도+개인운동</button>
    <button onclick="intModalPreset('recovery')" class="px-2.5 py-1 rounded-lg bg-teal-950/80 text-teal-300 border border-teal-700 font-bold">🧖 리커버리</button>
    <button onclick="intModalPreset('lockers')" class="px-2.5 py-1 rounded-lg bg-purple-950/80 text-purple-300 border border-purple-700 font-bold">🚿 4.5m 락커·샤워</button>
  </div>

  <div id="intModalViewport" class="flex-1 w-full h-full relative overflow-hidden bg-[#090D16] rounded-2xl border border-dark-border cursor-grab active:cursor-grabbing">
    <div id="intModalCanvas" class="w-full h-full flex items-center justify-center transform-origin-center will-change-transform">
      <div class="w-full h-full flex items-center justify-center p-2">
        {embedded_svg}
      </div>
    </div>
  </div>
</div>

<script>
// Internal Review Master Plan Pan-Zoom Engine
(function() {{
  function initPanZoom(viewportId, canvasId, badgeId) {{
    const viewport = document.getElementById(viewportId);
    const canvas = document.getElementById(canvasId);
    const badge = document.getElementById(badgeId);
    if (!viewport || !canvas) return null;

    let scale = 1.0;
    let tx = 0;
    let ty = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    function update(smooth = false) {{
      canvas.style.transition = smooth ? 'transform 0.28s cubic-bezier(0.2, 0.8, 0.2, 1)' : 'none';
      canvas.style.transform = `translate(${{tx}}px, ${{ty}}px) scale(${{scale}})`;
      if (badge) badge.textContent = Math.round(scale * 100) + '%';
    }}

    function reset() {{
      scale = 1.0;
      tx = 0;
      ty = 0;
      update(true);
    }}

    function zoom(factor) {{
      scale = Math.min(Math.max(scale * factor, 0.8), 6.0);
      update(true);
    }}

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const rect = viewport.getBoundingClientRect();
      const mouseX = e.clientX - rect.left - rect.width / 2;
      const mouseY = e.clientY - rect.top - rect.height / 2;
      const factor = e.deltaY < 0 ? 1.15 : 0.87;
      const newScale = Math.min(Math.max(scale * factor, 0.8), 6.5);
      tx = mouseX - (mouseX - tx) * (newScale / scale);
      ty = mouseY - (mouseY - ty) * (newScale / scale);
      scale = newScale;
      update(false);
    }}, {{ passive: false }});

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
      update(false);
    }});

    window.addEventListener('mouseup', () => {{
      if (isDragging) {{
        isDragging = false;
        viewport.classList.remove('cursor-grabbing');
      }}
    }});

    viewport.addEventListener('dblclick', () => {{
      if (scale > 1.2) reset();
      else {{ scale = 2.0; update(true); }}
    }});

    // Touch
    let initDist = 0, initScale = 1.0;
    viewport.addEventListener('touchstart', (e) => {{
      if (e.touches.length === 1) {{
        isDragging = true;
        startX = e.touches[0].clientX - tx;
        startY = e.touches[0].clientY - ty;
      }} else if (e.touches.length === 2) {{
        isDragging = false;
        initDist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        initScale = scale;
      }}
    }}, {{ passive: false }});

    viewport.addEventListener('touchmove', (e) => {{
      e.preventDefault();
      if (isDragging && e.touches.length === 1) {{
        tx = e.touches[0].clientX - startX;
        ty = e.touches[0].clientY - startY;
        update(false);
      }} else if (e.touches.length === 2 && initDist > 0) {{
        const dist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        scale = Math.min(Math.max(initScale * (dist / initDist), 0.8), 6.5);
        update(false);
      }}
    }}, {{ passive: false }});

    viewport.addEventListener('touchend', () => {{ isDragging = false; }});

    const PRESETS = {{
      all: {{ x: 270, y: 200, s: 1.0 }},
      metcon: {{ x: 380, y: 125, s: 2.1 }},
      rig: {{ x: 358, y: 197, s: 2.4 }},
      turf: {{ x: 341, y: 242, s: 2.2 }},
      erg: {{ x: 195, y: 220, s: 2.9 }},
      opengym: {{ x: 155, y: 240, s: 3.2 }},
      recovery: {{ x: 273.5, y: 323, s: 3.2 }},
      restroom: {{ x: 235, y: 323, s: 3.2 }},
      lockers: {{ x: 335, y: 323, s: 2.5 }},
      lounge: {{ x: 189, y: 323, s: 3.0 }}
    }};

    function setPreset(name) {{
      const p = PRESETS[name];
      if (!p) return;
      const rect = canvas.getBoundingClientRect();
      tx = (0.5 - (p.x / 540)) * rect.width * p.s;
      ty = (0.5 - (p.y / 400)) * rect.height * p.s;
      scale = p.s;
      update(true);
    }}

    return {{ reset, zoom, setPreset }};
  }}

  const intViewer = initPanZoom('intViewport', 'intCanvas', 'intZoomBadge');
  const intModalViewer = initPanZoom('intModalViewport', 'intModalCanvas', 'intModalBadge');

  window.intPreset = (name) => intViewer && intViewer.setPreset(name);
  window.intModalPreset = (name) => intModalViewer && intModalViewer.setPreset(name);

  document.getElementById('intZoomIn')?.addEventListener('click', () => intViewer?.zoom(1.25));
  document.getElementById('intZoomOut')?.addEventListener('click', () => intViewer?.zoom(0.8));
  document.getElementById('intZoomReset')?.addEventListener('click', () => intViewer?.reset());

  const modal = document.getElementById('intModal');
  const openModalBtn = document.getElementById('intFullscreenBtn');
  const closeModalBtn = document.getElementById('intCloseModal');

  function openModal() {{
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    intModalViewer?.reset();
  }}

  function closeModal() {{
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }}

  openModalBtn?.addEventListener('click', openModal);
  closeModalBtn?.addEventListener('click', closeModal);

  window.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) closeModal();
  }});
}})();
</script>
'''

# Remove any previous intModal or PanZoom scripts if present
internal_html = re.sub(r'<!-- Fullscreen Plan Modal \(Internal Review\) -->.*?</body>', '</body>', internal_html, flags=re.S)
internal_html = internal_html.replace('</body>', internal_modal_markup + '\n</body>')

with open('kyerim-internal.html', 'w', encoding='utf-8') as f:
    f.write(internal_html)

print("Updated kyerim-internal.html successfully!")
