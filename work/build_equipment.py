import json

with open('work/gyerim_items.json', 'r', encoding='utf-8') as f:
    gyerim_items = json.load(f)

with open('work/pan3_items.json', 'r', encoding='utf-8') as f:
    pan3_items = json.load(f)

html_content = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>계림점 운동기구 & 공식 장비 명세서 — 트레이닝판</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
  theme: {{
    extend: {{
      colors: {{
        brand: {{ 50: '#fff7ed', 100: '#ffedd5', 500: '#f97316', 600: '#ea580c', 700: '#c2410c' }}
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
input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button {{ -webkit-appearance: none; margin: 0; }}
.is-embedded header {{ display: none !important; }}
.is-embedded main {{ padding-top: 1.5rem !important; }}
.drag-handle {{ cursor: grab; user-select: none; }}
.drag-handle:active {{ cursor: grabbing; }}
tr.dragging {{ opacity: 0.45; background-color: #e0f2fe !important; }}
tr.drag-over-top {{ border-top: 2.5px solid #0284c7 !important; }}
tr.drag-over-bottom {{ border-bottom: 2.5px solid #0284c7 !important; }}
.preset-btn.active {{
  background-color: #0284c7;
  color: white;
  border-color: #0284c7;
  box-shadow: 0 4px 6px -1px rgb(2 132 199 / 0.2);
}}
.cat-pill.active {{
  background-color: #0f172a;
  color: white;
}}
</style>
<script>
if (window.self !== window.top) {{
  document.documentElement.classList.add('is-embedded');
}}
</script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased selection:bg-sky-500 selection:text-white min-h-screen">

<!-- Top Navigation -->
<header class="sticky top-0 z-50 backdrop-blur-md bg-white/90 border-b border-slate-200 px-4 lg:px-8 py-3.5 shadow-sm">
  <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
    <div class="flex items-center gap-3">
      <a href="index.html" class="flex items-center gap-2 group">
        <span class="w-8 h-8 rounded-lg bg-gradient-to-br from-sky-500 to-sky-700 flex items-center justify-center font-black text-white text-base shadow-md shadow-sky-500/20 group-hover:scale-105 transition">P</span>
        <div>
          <div class="flex items-center gap-2">
            <span class="font-bold text-base tracking-tight text-slate-900 group-hover:text-sky-600 transition">트레이닝판 × 계림 운동공간</span>
            <span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-sky-50 text-sky-700 border border-sky-200">2023 Xpodium 실견적 기반</span>
          </div>
          <span class="text-xs text-slate-500 block -mt-0.5 font-mono">운동기구 & 공식 장비 명세서 (CAPEX)</span>
        </div>
      </a>
      <span class="hidden xl:inline-block px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">의장님 100% 매입·자산 소유</span>
    </div>

    <nav class="flex items-center gap-1.5 sm:gap-2 text-xs sm:text-sm font-medium">
      <a href="kyerim-plan.html" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition">사업 계획 & 수익 계산기</a>
      <a href="kyerim-equipment.html" class="px-3 py-1.5 rounded-lg bg-sky-50 text-sky-700 font-bold border border-sky-200 transition">운동기구 명세서</a>
      <a href="kyerim-opex.html" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition">월 운영비 명세서</a>
      <a href="kyerim-pitch.html" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition">공간 기획서</a>
      <a href="index.html" class="ml-2 px-3 py-1.5 rounded-lg bg-slate-100 text-slate-700 hover:text-slate-900 border border-slate-200 transition">허브 ↗</a>
    </nav>
  </div>
</header>

<main class="max-w-7xl mx-auto px-4 lg:px-8 py-8 space-y-6">

  <!-- Preset Selector Header Banner -->
  <div class="bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
      <div>
        <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-sky-50 text-sky-700 font-bold text-xs">
          <span>📜</span> 실거래 견적서 연동 (판 3호점 2023년 Xpodium & 코모 실제 발주 기준)
        </div>
        <h2 class="text-lg sm:text-xl font-bold text-slate-900 mt-1">견적 모드 선택 및 원클릭 비교</h2>
      </div>

      <div class="flex items-center gap-2">
        <div id="saveStatusBadge" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200 transition-all">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
          <span id="saveStatusText">실시간 자동 저장 중</span>
        </div>
      </div>
    </div>

    <!-- 2 Main Preset Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <button type="button" id="btnPresetGyerim" class="preset-btn active text-left p-4 rounded-2xl border-2 transition flex items-start justify-between gap-3 group">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="font-black text-base sm:text-lg">⭐ 계림점 230평 하이록스 & 크로스핏 확장 견적</span>
            <span class="px-2 py-0.5 rounded-md text-[10px] font-bold bg-sky-100 text-sky-800 border border-sky-200 group-[.active]:bg-white/20 group-[.active]:text-white group-[.active]:border-white/30">권장</span>
          </div>
          <p class="text-xs text-slate-500 group-[.active]:text-sky-100 leading-relaxed">
            2023년 Xpodium 및 코모 실단가를 100% 적용하여 230평 대형 공간과 하이록스 공식 종목(스키 6대, 썰매, 잔디트랙, 트레드밀, 고무매트 600장)으로 확장한 최적화 예산
          </p>
        </div>
        <div class="text-right flex-shrink-0 font-mono">
          <div class="text-xl font-black group-[.active]:text-white text-slate-900">약 1.2억원</div>
          <div class="text-[11px] group-[.active]:text-sky-200 text-slate-400">37개 핵심 품목</div>
        </div>
      </button>

      <button type="button" id="btnPresetPan3" class="preset-btn text-left p-4 rounded-2xl border-2 border-slate-200 bg-slate-50/50 hover:bg-slate-100 text-slate-700 transition flex items-start justify-between gap-3 group">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="font-black text-base sm:text-lg text-slate-900 group-[.active]:text-white">📄 판 3호점 실제 납품 견적서 원본 (2023)</span>
            <span class="px-2 py-0.5 rounded-md text-[10px] font-bold bg-slate-200 text-slate-700 group-[.active]:bg-white/20 group-[.active]:text-white group-[.active]:border-white/30">실거래 원본</span>
          </div>
          <p class="text-xs text-slate-500 group-[.active]:text-sky-100 leading-relaxed">
            판 3호점(신창점) 오픈 당시 Xpodium(5,100만) + 코모 Concept2(2,711만)로 실제 결제했던 57개 품목의 단가·수량·합계 100% 원본 데이터
          </p>
        </div>
        <div class="text-right flex-shrink-0 font-mono">
          <div class="text-xl font-black text-slate-900 group-[.active]:text-white">7,348만원</div>
          <div class="text-[11px] text-slate-400 group-[.active]:text-sky-200">57개 전 품목</div>
        </div>
      </button>
    </div>
  </div>

  <!-- Overview Cards -->
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-1">
      <span class="text-xs text-slate-500 font-medium">운동기구 & 공식 장비 합계</span>
      <div class="text-3xl font-black font-mono text-slate-900 mt-1" id="sumTotal">1억 1,988만원</div>
      <div class="text-xs text-slate-400 font-mono mt-0.5" id="sumTotalWon">119,875,000원</div>
      <span class="text-xs text-emerald-600 font-medium flex items-center gap-1 mt-1.5">
        <span>✓</span> 의장님 100% 실물 자산 귀속 (운영사 상환 0원)
      </span>
    </div>

    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-1">
      <span class="text-xs text-slate-500 font-medium flex items-center justify-between">
        <span>Concept2 공식 유산소 (코모)</span>
        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-50 text-emerald-700">정품 수입사</span>
      </span>
      <div class="text-3xl font-black font-mono text-emerald-600 mt-1" id="sumCardio">3,790만원</div>
      <div class="text-xs text-slate-400 font-mono mt-0.5" id="sumCardioWon">37,900,000원</div>
      <span class="text-xs text-slate-500 mt-1 block" id="cardioDesc">로잉 10대 + 바이크 5대 + 스키 6대 + 트레드밀 2대</span>
    </div>

    <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-1">
      <span class="text-xs text-slate-500 font-medium flex items-center justify-between">
        <span>바닥재 / 리그 / 프리웨이트 (Xpodium)</span>
        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-brand-50 text-brand-700">포디움 본사</span>
      </span>
      <div class="text-3xl font-black font-mono text-brand-600 mt-1" id="sumXpodium">8,198만원</div>
      <div class="text-xs text-slate-400 font-mono mt-0.5" id="sumXpodiumWon">81,975,000원</div>
      <span class="text-xs text-slate-500 mt-1 block" id="xpodiumDesc">바닥 600장 + 25m 리그 + 바벨 40자루 + 플레이트 + 덤벨</span>
    </div>
  </div>

  <!-- Main Editable Table Box -->
  <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm space-y-4">
    
    <!-- Table Header Toolbar -->
    <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-slate-200 pb-4">
      <div>
        <div class="flex items-center gap-2">
          <h1 class="text-xl font-bold text-slate-900 flex items-center gap-2">
            <span>🏋️</span> 운동기구 & 공식 장비 명세서
          </h1>
          <span class="text-xs px-2.5 py-0.5 rounded-full font-bold bg-slate-100 text-slate-600 border border-slate-200" id="itemCountBadge">총 37개 품목</span>
        </div>
        <p class="text-xs sm:text-sm text-slate-500 mt-1">
          단가와 수량을 수정하면 품목별 합계 및 총액이 자동 계산되며, <b class="text-sky-600">좌측 핸들(⋮⋮)을 드래그앤드롭</b>하여 품목 순서를 변경할 수 있습니다. (자동 저장)
        </p>
      </div>

      <div class="flex flex-wrap items-center gap-2">
        <div class="relative w-48">
          <input type="text" id="searchInput" placeholder="품목 검색 (로잉, 바벨 등)..." class="w-full pl-8 pr-3 py-1.5 rounded-xl text-xs bg-slate-50 border border-slate-200 focus:bg-white focus:border-sky-500 outline-none transition">
          <span class="absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs">🔍</span>
        </div>

        <button type="button" id="addRowBtn" class="px-3.5 py-1.5 rounded-xl bg-sky-600 hover:bg-sky-700 text-white text-xs font-bold shadow-md shadow-sky-600/20 transition flex items-center gap-1">
          <span>+</span> 품목 추가
        </button>
        <button type="button" id="copyClipboardBtn" class="px-3.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold border border-slate-200 transition flex items-center gap-1" title="엑셀 붙여넣기용 클립보드 복사">
          <span>📋</span> 엑셀 복사
        </button>
        <button type="button" id="resetCurrentBtn" class="px-3.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs font-medium border border-slate-200 transition">
          기본값 복원
        </button>
      </div>
    </div>

    <!-- Category Filter Pills -->
    <div class="flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-none text-xs font-medium" id="categoryFilterBar">
      <button class="cat-pill active px-3 py-1 rounded-lg border border-slate-200 transition whitespace-nowrap" data-cat="ALL">전체 보기</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="유산소 머신">유산소 머신</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="썰매 & 트랙">썰매 & 트랙</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="바닥재">바닥재</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="스테이션 & 랙">스테이션 & 랙</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="바벨">바벨</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="플레이트">플레이트</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="덤벨">덤벨</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="케틀벨">케틀벨</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="소도구">소도구·박스·월볼</button>
      <button class="cat-pill px-3 py-1 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-100 transition whitespace-nowrap" data-cat="배송/설치">배송·설치</button>
    </div>

    <!-- Table Container -->
    <div class="overflow-x-auto">
      <table class="w-full text-left text-sm">
        <thead class="bg-slate-50 text-slate-600 font-semibold border-b border-slate-200 text-xs">
          <tr>
            <th class="py-3 px-3 w-12 text-center" title="드래그앤드롭 핸들">순서</th>
            <th class="py-3 px-3 w-28">공급사</th>
            <th class="py-3 px-3 w-28">분류</th>
            <th class="py-3 px-4 w-60">품목명 (규격)</th>
            <th class="py-3 px-4 w-36 text-right">단가 (원)</th>
            <th class="py-3 px-4 w-24 text-right">수량</th>
            <th class="py-3 px-4 w-44 text-right">합계 (원)</th>
            <th class="py-3 px-4">공식 스펙 및 비고</th>
            <th class="py-3 px-3 text-center w-14">삭제</th>
          </tr>
        </thead>
        <tbody id="equipmentTableBody" class="divide-y divide-slate-100 text-slate-700">
          <!-- Rows injected by JavaScript -->
        </tbody>
        <tfoot class="bg-slate-50 border-t-2 border-slate-300 font-bold text-slate-900">
          <tr>
            <td colspan="4" class="py-4 px-4 text-base">운동기구 & 공식 장비 총합계</td>
            <td colspan="2" class="py-4 px-4 text-right text-xs text-slate-500 font-normal">
              의장님 100% 매입·자산 명의 귀속
            </td>
            <td class="py-4 px-4 text-right font-mono text-xl text-sky-600" id="footTotal">
              1억 1,988만원
            </td>
            <td colspan="2" class="py-4 px-4 text-xs text-slate-500">
              * 사업 계획서 및 회수 시뮬레이터에 실시간 자동 반영됩니다.
            </td>
          </tr>
        </tfoot>
      </table>
    </div>

    <!-- Guidance Note Box -->
    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2 text-xs text-slate-600">
      <div class="font-bold text-slate-900 text-sm flex items-center gap-1.5">
        <span class="w-2.5 h-2.5 rounded-full bg-sky-500"></span>
        2023년 판 3호점 Xpodium & 코모 실견적 기반 산출 및 관리 원칙
      </div>
      <p>• <b>실제 발주 단가 100% 준용</b>: 본 명세서의 품목별 단가는 2023년 판 3호점(신창점) 오픈 당시 <b>Xpodium 본사 및 Concept2 공식 수입원(코모 엔터프라이즈)</b>으로부터 발주했던 최종 견적서 실거래 단가를 기준으로 1원 단위까지 정밀하게 책정되었습니다.</p>
      <p>• <b>계림점(지하 230평) 확장 기준</b>: 3호점(약 100평, 실견적 7,811만원) 대비 2.3배 넓은 공간과 하이록스(HYROX) 공식 트레이닝 클럽 도입에 따라, <b>컨셉2 스키에르그(1대→6대), 25m 잔디트랙 & 경기용 썰매 4대, 무동력 트레드밀, 고무매트 바닥재(350장→600장), 25m 맞춤 철골 리그</b>를 증설하여 총 약 1.2억원 규모로 완성했습니다.</p>
      <p>• <b>의장님 100% 실물 자산 귀속 & 무상환</b>: 모든 장비는 의장님이 100% 매입하여 의장님 명의로 소유하며, 운영사(트레이닝판)의 부채나 상환 의무는 일체 없습니다.</p>
      <p>• <b>압도적 중고 감가상각 방어</b>: Concept2 머신 및 Xpodium 공인 리그, 바벨, 우레탄 플레이트는 피트니스 시장에서 75~80% 이상의 실물 자산 가치를 유지하므로 의장님의 원금 리스크가 극히 안전합니다.</p>
    </div>
  </div>

</main>

<footer class="border-t border-slate-200 bg-white py-8 px-4 text-center text-xs text-slate-400 font-mono space-y-1">
  <p>계림 운동공간 위탁운영 프로젝트 · 운동기구 & 공식 장비 명세서 (CAPEX)</p>
  <p>© 2026 TRAININGPAN. ALL RIGHTS RESERVED.</p>
</footer>

<script>
const PRESET_GYERIM = {json.dumps(gyerim_items, ensure_ascii=False)};
const PRESET_PAN3 = {json.dumps(pan3_items, ensure_ascii=False)};

const STORAGE_KEY = "kyerim_equipment_items_v2";
const TOTAL_STORAGE_KEY = "kyerim_equipment_total_v2";
const MODE_STORAGE_KEY = "kyerim_equipment_mode_v2";
const V1_TOTAL_KEY = "kyerim_equipment_total_v1";

let items = [];
let currentMode = 'gyerim'; // 'gyerim' or 'pan3'
let currentCategory = 'ALL';
let currentSearch = '';
let draggedIndex = null;

function loadData() {{
  const savedMode = localStorage.getItem(MODE_STORAGE_KEY);
  if (savedMode === 'pan3') {{
    currentMode = 'pan3';
  }} else {{
    currentMode = 'gyerim';
  }}

  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {{
    try {{
      items = JSON.parse(saved);
      if (!Array.isArray(items) || items.length === 0) {{
        items = currentMode === 'pan3' ? JSON.parse(JSON.stringify(PRESET_PAN3)) : JSON.parse(JSON.stringify(PRESET_GYERIM));
      }}
    }} catch(e) {{
      items = currentMode === 'pan3' ? JSON.parse(JSON.stringify(PRESET_PAN3)) : JSON.parse(JSON.stringify(PRESET_GYERIM));
    }}
  }} else {{
    items = currentMode === 'pan3' ? JSON.parse(JSON.stringify(PRESET_PAN3)) : JSON.parse(JSON.stringify(PRESET_GYERIM));
  }}
}}

function saveData() {{
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
  localStorage.setItem(MODE_STORAGE_KEY, currentMode);
  const totalWon = calculateTotal();
  const totalManwon = Math.round(totalWon / 10000);
  localStorage.setItem(TOTAL_STORAGE_KEY, totalManwon);
  localStorage.setItem(V1_TOTAL_KEY, totalManwon);
  showSaveIndicator();
}}

function showSaveIndicator() {{
  const badge = document.getElementById("saveStatusBadge");
  const txt = document.getElementById("saveStatusText");
  if (!badge || !txt) return;

  const now = new Date();
  const timeStr = `${{String(now.getHours()).padStart(2, '0')}}:${{String(now.getMinutes()).padStart(2, '0')}}:${{String(now.getSeconds()).padStart(2, '0')}}`;
  
  badge.className = "inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-300 transition-all shadow-sm";
  txt.textContent = `✓ 자동 저장 완료 (${{timeStr}})`;
  
  clearTimeout(badge._timer);
  badge._timer = setTimeout(() => {{
    badge.className = "inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200 transition-all";
    txt.textContent = `실시간 자동 저장 중`;
  }}, 1500);
}}

function calculateTotal() {{
  return items.reduce((sum, item) => sum + (Number(item.price || 0) * Number(item.qty || 0)), 0);
}}

function fmtWon(n) {{
  return Math.round(n).toLocaleString('ko-KR') + '원';
}}

function fmtManwon(n) {{
  const man = Number((n / 10000).toFixed(1));
  if (man >= 10000) {{
    const eok = Math.floor(man / 10000);
    const rem = Number((man % 10000).toFixed(0));
    return `${{eok}}억 ${{rem > 0 ? rem.toLocaleString('ko-KR') + '만' : ''}}원`;
  }}
  return `${{man.toLocaleString('ko-KR')}}만원`;
}}

function render() {{
  const tbody = document.getElementById("equipmentTableBody");
  tbody.innerHTML = "";

  // Update preset button active state
  document.getElementById("btnPresetGyerim").classList.toggle('active', currentMode === 'gyerim');
  document.getElementById("btnPresetPan3").classList.toggle('active', currentMode === 'pan3');

  const filteredItems = items.filter(item => {{
    // Category match
    let matchCat = true;
    if (currentCategory !== 'ALL') {{
      const c = item.category || '';
      matchCat = c.includes(currentCategory);
    }}

    // Search match
    let matchSearch = true;
    if (currentSearch.trim()) {{
      const q = currentSearch.toLowerCase();
      const n = (item.name || '').toLowerCase();
      const s = (item.supplier || '').toLowerCase();
      const c = (item.category || '').toLowerCase();
      matchSearch = n.includes(q) || s.includes(q) || c.includes(q);
    }}

    return matchCat && matchSearch;
  }});

  document.getElementById("itemCountBadge").textContent = `총 ${{items.length}}개 품목 (표시: ${{filteredItems.length}}개)`;

  filteredItems.forEach((item, filteredIdx) => {{
    const realIdx = items.indexOf(item);
    const rowTotal = Number(item.price || 0) * Number(item.qty || 0);

    const tr = document.createElement("tr");
    tr.className = "hover:bg-slate-50/80 transition group";
    tr.id = `row-${{realIdx}}`;
    tr.setAttribute("draggable", "true");
    tr.setAttribute("data-idx", realIdx);

    const sup = item.supplier || 'Xpodium';
    let badgeColorClass = "bg-amber-50 text-amber-800 border-amber-300 hover:bg-amber-100";
    if (sup.includes('코모')) {{
      badgeColorClass = "bg-emerald-50 text-emerald-800 border-emerald-300 hover:bg-emerald-100";
    }} else if (sup.includes('통합')) {{
      badgeColorClass = "bg-slate-100 text-slate-700 border-slate-300 hover:bg-slate-200";
    }} else if (sup === '기타') {{
      badgeColorClass = "bg-zinc-100 text-zinc-700 border-zinc-300 hover:bg-zinc-200";
    }} else if (sup !== 'Xpodium') {{
      badgeColorClass = "bg-indigo-50 text-indigo-800 border-indigo-300 hover:bg-indigo-100";
    }}

    const isPresetSup = ['Xpodium', '코모', '통합', '기타'].includes(sup);

    const supplierSelectHtml = `
      <div class="relative inline-flex items-center">
        <select class="supplier-select appearance-none cursor-pointer text-[11px] font-bold pl-2.5 pr-5 py-1 rounded-full border ${{badgeColorClass}} focus:outline-none focus:ring-2 focus:ring-sky-500/40 transition shadow-2xs" data-idx="${{realIdx}}" title="클릭하여 공급사 변경 (코모 / Xpodium / 직접 입력)">
          <option value="Xpodium" ${{sup === 'Xpodium' ? 'selected' : ''}}>Xpodium</option>
          <option value="코모" ${{sup === '코모' ? 'selected' : ''}}>코모 (컨셉2)</option>
          <option value="통합" ${{sup === '통합' ? 'selected' : ''}}>통합</option>
          <option value="기타" ${{sup === '기타' ? 'selected' : ''}}>기타</option>
          ${{!isPresetSup ? `<option value="${{sup}}" selected>${{sup}}</option>` : ''}}
          <option value="__custom__">✏️ 직접 입력...</option>
        </select>
        <span class="pointer-events-none absolute right-2 text-[8px] text-slate-400">▼</span>
      </div>
    `;

    tr.innerHTML = `
      <td class="py-3 px-3 text-center w-12">
        <div class="drag-handle w-7 h-7 mx-auto rounded-lg hover:bg-slate-200/80 text-slate-400 group-hover:text-slate-600 flex items-center justify-center transition" title="마우스로 잡고 위아래로 끌어 순서 변경">
          <svg class="w-4 h-4 pointer-events-none" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7 2a2 2 0 100 4 2 2 0 000-4zm6 0a2 2 0 100 4 2 2 0 000-4zm-6 6a2 2 0 100 4 2 2 0 000-4zm6 0a2 2 0 100 4 2 2 0 000-4zm-6 6a2 2 0 100 4 2 2 0 000-4zm6 0a2 2 0 100 4 2 2 0 000-4z"/>
          </svg>
        </div>
      </td>
      <td class="py-3 px-2 text-center w-32">
        ${{supplierSelectHtml}}
      </td>
      <td class="py-3 px-3">
        <input type="text" value="${{item.category || ''}}" placeholder="분류" class="w-full text-xs font-semibold text-slate-700 bg-slate-100/60 hover:bg-white focus:bg-white border border-transparent focus:border-sky-400 px-2 py-1 rounded outline-none transition" data-idx="${{realIdx}}" data-field="category">
      </td>
      <td class="py-3 px-4">
        <input type="text" value="${{item.name}}" class="w-full font-semibold text-slate-900 bg-transparent border-b border-transparent focus:border-sky-500 focus:bg-white px-1.5 py-1 rounded outline-none transition" data-idx="${{realIdx}}" data-field="name">
      </td>
      <td class="py-3 px-4 text-right">
        <input type="number" value="${{item.price}}" step="100" min="0" class="w-28 text-right font-mono font-bold text-slate-900 bg-slate-100/60 hover:bg-white focus:bg-white border border-slate-200 focus:border-sky-500 px-2 py-1 rounded outline-none transition" data-idx="${{realIdx}}" data-field="price">
      </td>
      <td class="py-3 px-4 text-right">
        <input type="number" value="${{item.qty}}" min="0" step="1" class="w-16 text-right font-mono font-bold text-slate-900 bg-slate-100/60 hover:bg-white focus:bg-white border border-slate-200 focus:border-sky-500 px-2 py-1 rounded outline-none transition" data-idx="${{realIdx}}" data-field="qty">
      </td>
      <td class="py-3 px-4 text-right font-mono font-bold text-sky-700 text-sm" id="row-total-${{realIdx}}">
        <div>${{fmtWon(rowTotal)}}</div>
        <div class="text-[10px] text-slate-400 font-normal">(${{fmtManwon(rowTotal)}})</div>
      </td>
      <td class="py-3 px-4">
        <input type="text" value="${{item.note || ''}}" placeholder="스펙 및 메모" class="w-full text-xs text-slate-500 bg-transparent border-b border-transparent focus:border-slate-300 focus:bg-white px-1.5 py-1 rounded outline-none transition" data-idx="${{realIdx}}" data-field="note">
      </td>
      <td class="py-3 px-3 text-center">
        <button type="button" class="text-slate-400 hover:text-rose-500 p-1 rounded transition del-btn" data-idx="${{realIdx}}" title="삭제">
          <svg class="w-4 h-4 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
        </button>
      </td>
    `;

    // Drag events for row reordering
    tr.addEventListener("dragstart", (e) => {{
      if (['INPUT', 'BUTTON', 'SELECT'].includes(e.target.tagName)) {{
        if (!e.target.closest('.drag-handle')) {{
          e.preventDefault();
          return;
        }}
      }}
      draggedIndex = realIdx;
      tr.classList.add("dragging");
      e.dataTransfer.effectAllowed = "move";
      e.dataTransfer.setData("text/plain", realIdx.toString());
    }});

    tr.addEventListener("dragend", () => {{
      tr.classList.remove("dragging");
      tbody.querySelectorAll("tr").forEach(r => r.classList.remove("drag-over-top", "drag-over-bottom"));
      draggedIndex = null;
    }});

    tr.addEventListener("dragover", (e) => {{
      e.preventDefault();
      e.dataTransfer.dropEffect = "move";
      if (draggedIndex === null || draggedIndex === realIdx) {{
        tr.classList.remove("drag-over-top", "drag-over-bottom");
        return;
      }}
      const rect = tr.getBoundingClientRect();
      const midY = rect.top + rect.height / 2;
      tr.classList.remove("drag-over-top", "drag-over-bottom");
      if (e.clientY < midY) {{
        tr.classList.add("drag-over-top");
      }} else {{
        tr.classList.add("drag-over-bottom");
      }}
    }});

    tr.addEventListener("dragleave", () => {{
      tr.classList.remove("drag-over-top", "drag-over-bottom");
    }});

    tr.addEventListener("drop", (e) => {{
      e.preventDefault();
      tr.classList.remove("drag-over-top", "drag-over-bottom");
      if (draggedIndex === null || draggedIndex === realIdx) return;

      const rect = tr.getBoundingClientRect();
      const midY = rect.top + rect.height / 2;
      const insertBefore = e.clientY < midY;

      const [movedItem] = items.splice(draggedIndex, 1);
      let targetIdx = realIdx;
      if (draggedIndex < targetIdx && insertBefore) {{
        targetIdx -= 1;
      }} else if (draggedIndex > targetIdx && !insertBefore) {{
        targetIdx += 1;
      }}
      items.splice(targetIdx, 0, movedItem);

      saveData();
      render();
    }});

    tbody.appendChild(tr);
  }});

  updateSummaries();

  // Bind change events
  tbody.querySelectorAll("input").forEach(input => {{
    input.addEventListener("input", e => {{
      const idx = parseInt(e.target.getAttribute("data-idx"));
      const field = e.target.getAttribute("data-field");
      items[idx][field] = (field === "price" || field === "qty") ? (parseFloat(e.target.value) || 0) : e.target.value;
      
      // Update specific row total
      const rowTotal = Number(items[idx].price || 0) * Number(items[idx].qty || 0);
      const rowTotalEl = document.getElementById(`row-total-${{idx}}`);
      if (rowTotalEl) {{
        rowTotalEl.innerHTML = `
          <div>${{fmtWon(rowTotal)}}</div>
          <div class="text-[10px] text-slate-400 font-normal">(${{fmtManwon(rowTotal)}})</div>
        `;
      }}

      saveData();
      updateSummaries();
    }});
  }});

  tbody.querySelectorAll(".del-btn").forEach(btn => {{
    btn.addEventListener("click", e => {{
      const idx = parseInt(e.currentTarget.getAttribute("data-idx"));
      if (confirm(`'${{items[idx].name}}' 품목을 삭제하시겠습니까?`)) {{
        items.splice(idx, 1);
        saveData();
        render();
      }}
    }});
  }});

  tbody.querySelectorAll(".supplier-select").forEach(select => {{
    select.addEventListener("change", e => {{
      const idx = parseInt(e.target.getAttribute("data-idx"));
      const val = e.target.value;
      if (val === "__custom__") {{
        const prev = items[idx].supplier || 'Xpodium';
        const custom = prompt("새로운 공급사명을 직접 입력해주세요:\\n(예: Rogue, 디랙스, 매드캣, 직접제작 등)", prev);
        if (custom && custom.trim()) {{
          items[idx].supplier = custom.trim();
        }} else {{
          e.target.value = prev;
          return;
        }}
      }} else {{
        items[idx].supplier = val;
      }}
      saveData();
      render();
    }});
  }});
}}

function updateSummaries() {{
  let total = 0;
  let cardio = 0;
  let xpodium = 0;

  items.forEach(item => {{
    const rowTotal = Number(item.price || 0) * Number(item.qty || 0);
    total += rowTotal;
    const isComo = (item.supplier || '').includes('코모');
    const cat = item.category || '';
    if (isComo || cat.includes('유산소')) {{
      cardio += rowTotal;
    }} else {{
      xpodium += rowTotal;
    }}
  }});

  document.getElementById("sumTotal").textContent = fmtManwon(total);
  document.getElementById("sumTotalWon").textContent = fmtWon(total);
  document.getElementById("footTotal").textContent = `${{fmtManwon(total)}} (${{fmtWon(total)}})`;

  document.getElementById("sumCardio").textContent = fmtManwon(cardio);
  document.getElementById("sumCardioWon").textContent = fmtWon(cardio);

  document.getElementById("sumXpodium").textContent = fmtManwon(xpodium);
  document.getElementById("sumXpodiumWon").textContent = fmtWon(xpodium);
}}

// Preset switchers
document.getElementById("btnPresetGyerim").addEventListener("click", () => {{
  if (confirm("계림점 230평 확장 견적 세팅(약 1.2억원)을 불러오시겠습니까?\\n(직접 수정한 내용은 덮어씌워집니다)")) {{
    currentMode = 'gyerim';
    items = JSON.parse(JSON.stringify(PRESET_GYERIM));
    saveData();
    render();
  }}
}});

document.getElementById("btnPresetPan3").addEventListener("click", () => {{
  if (confirm("2023년 판 3호점 실제 납품 견적서 원본(7,348만원 / 57개 품목)을 불러오시겠습니까?\\n(직접 수정한 내용은 덮어씌워집니다)")) {{
    currentMode = 'pan3';
    items = JSON.parse(JSON.stringify(PRESET_PAN3));
    saveData();
    render();
  }}
}});

// Category Filter pills
document.querySelectorAll(".cat-pill").forEach(pill => {{
  pill.addEventListener("click", e => {{
    document.querySelectorAll(".cat-pill").forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    currentCategory = pill.getAttribute("data-cat");
    render();
  }});
}});

// Search input
document.getElementById("searchInput").addEventListener("input", e => {{
  currentSearch = e.target.value;
  render();
}});

// Add Row
document.getElementById("addRowBtn").addEventListener("click", () => {{
  items.unshift({{
    id: Date.now(),
    supplier: "Xpodium",
    category: currentCategory !== 'ALL' ? currentCategory : "기타",
    name: "새 품목 (신규 추가)",
    price: 100000,
    qty: 1,
    note: ""
  }});
  saveData();
  render();
}});

// Reset Current
document.getElementById("resetCurrentBtn").addEventListener("click", () => {{
  const modeName = currentMode === 'gyerim' ? '계림점 230평 확장 견적' : '판 3호점 실견적 원본';
  if (confirm(`'${{modeName}}' 기본값으로 복원하시겠습니까?`)) {{
    items = currentMode === 'pan3' ? JSON.parse(JSON.stringify(PRESET_PAN3)) : JSON.parse(JSON.stringify(PRESET_GYERIM));
    saveData();
    render();
  }}
}});

// Copy to Clipboard (TSV for Excel)
document.getElementById("copyClipboardBtn").addEventListener("click", () => {{
  let text = "계림 운동공간 운동기구 & 공식 장비 명세서\\n";
  text += `견적 모드: ${{currentMode === 'gyerim' ? '계림점 230평 확장 견적' : '판 3호점 2023년 납품 실견적'}}\\n`;
  text += "------------------------------------------------------------------------------------------------------\\n";
  text += "순번\\t공급사\\t분류\\t품목명\\t단가(원)\\t수량\\t합계(원)\\t합계(만원)\\t스펙 및 비고\\n";
  
  items.forEach((item, idx) => {{
    const rowTotal = Number(item.price || 0) * Number(item.qty || 0);
    const manwon = (rowTotal / 10000).toFixed(1);
    text += `${{idx + 1}}\\t${{item.supplier}}\\t${{item.category}}\\t${{item.name}}\\t${{item.price}}\\t${{item.qty}}\\t${{rowTotal}}\\t${{manwon}}\\t${{item.note || ''}}\\n`;
  }});

  const total = calculateTotal();
  text += "------------------------------------------------------------------------------------------------------\\n";
  text += `총합계:\\t\\t\\t\\t\\t\\t${{total}}\\t${{(total/10000).toFixed(1)}}만원\\t${{fmtManwon(total)}}\\n`;

  navigator.clipboard.writeText(text).then(() => {{
    alert("명세서 전체 내용이 클립보드에 복사되었습니다.\\n(엑셀(Excel)에 [Ctrl+V] 또는 [Cmd+V]로 바로 붙여넣을 수 있습니다)");
  }}).catch(() => {{
    alert("클립보드 복사 실패");
  }});
}});

// Cross-document hub tab sync
document.querySelectorAll('a[href^="kyerim-"]').forEach(a => {{
  a.addEventListener('click', e => {{
    const href = a.getAttribute('href');
    if (window.parent && window.parent !== window) {{
      window.parent.postMessage({{ type: 'switchTab', src: href }}, '*');
    }}
  }});
}});

loadData();
render();
</script>
</body>
</html>
'''

with open('kyerim-equipment.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully generated kyerim-equipment.html, size:', len(html_content))
