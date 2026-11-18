# -*- coding: utf-8 -*-
"""
Architectural Master Plan SVG Generator (V4.2 CAD Grade)
Reflects Confirmed South Core + Empty Welcome Lounge (Door Only):
- Welcome Lounge: x=162.0~227.5, y=278.0~368.0 (6.55m × 9.0m = 17.85평, empty inside, 2.0m double-swing door on West wall)
- South Erg Zone: x=227.5~377.5, y=278.0~298.0 (15.0m × 2.0m = 9.1평, SkiErg ×6 + Curved Treadmill ×6 [1.75m])
- Core Entry Corridor: x=227.5~377.5, y=298.0~313.0 (15.0m × 1.5m = 6.8평)
- South Core Rooms: x=227.5~377.5, y=313.0~368.0 (15.0m × 5.5m = 25.0평):
  1) Men & Women Restrooms + Instant Gas Water Heater Room: x=227.5~277.5 (5.0m × 5.5m = 8.3평, Men 2.5m + Women 2.5m)
  2) Men Locker (3.4m) + Wall (0.1m) + Open Shower (2.0m, 5 showerheads): x=277.5~327.5 (5.0m × 5.5m = 8.3평)
  3) Women Locker (3.4m) + Wall (0.1m) + Open Shower (2.0m, 5 showerheads): x=327.5~377.5 (5.0m × 5.5m = 8.3평)
"""


def generate_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" font-family="Pretendard, -apple-system, BlinkMacSystemFont, Apple SD Gothic Neo, Noto Sans KR, sans-serif">
  <defs>
    <!-- Dark Architectural Theme Gradients -->
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#090D16" />
    </linearGradient>

    <!-- Arena Floor: Matte Black High-density EPDM Rubber -->
    <linearGradient id="arenaFloorGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#141D2C" />
    </linearGradient>

    <!-- ERG Zone Green/Lime Architectural Accent Gradient -->
    <linearGradient id="ergZoneGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A2E1A" />
      <stop offset="50%" stop-color="#1E3A1E" />
      <stop offset="100%" stop-color="#142616" />
    </linearGradient>

    <!-- Hyrox Strength Rubber Strip Gradient -->
    <linearGradient id="hyroxWeightGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#231F32" />
      <stop offset="100%" stop-color="#1A1829" />
    </linearGradient>

    <!-- Straight 3-Lane Charcoal/Silver Turf Gradient -->
    <linearGradient id="grayTurfGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="50%" stop-color="#3E4C63" />
      <stop offset="100%" stop-color="#2D3748" />
    </linearGradient>

    <!-- Amenity Gradients -->
    <linearGradient id="loungeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2A241C" />
      <stop offset="100%" stop-color="#1C1813" />
    </linearGradient>
    <linearGradient id="toiletGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#151E2E" />
    </linearGradient>
    <linearGradient id="menLockerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E4F6E" />
      <stop offset="100%" stop-color="#0F1A2A" />
    </linearGradient>
    <linearGradient id="womenLockerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4A1D6E" />
      <stop offset="100%" stop-color="#1B1124" />
    </linearGradient>

    <!-- Filters -->
    <filter id="softShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
    <filter id="rigGlow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="1" stdDeviation="1.5" flood-color="#EC4899" flood-opacity="0.5"/>
    </filter>
  </defs>

  <style>
    .grid-line { stroke: #334155; stroke-width: 0.5; stroke-dasharray: 2 3; }
    .dim-line { stroke: #94A3B8; stroke-width: 0.7; }
    .dim-tick { stroke: #94A3B8; stroke-width: 1.0; }
    .dim-text { font-size: 4.4px; font-weight: 700; fill: #CBD5E1; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
    .zone-title { font-size: 6.2px; font-weight: 800; fill: #F8FAFC; }
    .zone-sub { font-size: 4.2px; font-weight: 600; fill: #94A3B8; font-family: ui-monospace, monospace; }
    .outer-wall { fill: none; stroke: #F8FAFC; stroke-width: 2.2; }
    .inner-wall { fill: none; stroke: #64748B; stroke-width: 1.4; }
    .col-box { fill: #0F172A; stroke: #94A3B8; stroke-width: 1.2; }
    .door-swing { fill: none; stroke-dasharray: 1.5 1.5; stroke-width: 0.8; }
  </style>

  <!-- Background Canvas -->
  <rect width="540" height="400" fill="url(#bgDark)" />

  <!-- ================= 1. COLUMN GRID SYSTEM (8.1m SPAN) ================= -->
  <g id="grid-lines">
    <!-- Vertical Column Grid (열3~열6) -->
    <line x1="158" y1="20" x2="158" y2="385" class="grid-line" />
    <line x1="239" y1="20" x2="239" y2="385" class="grid-line" />
    <line x1="320" y1="20" x2="320" y2="385" class="grid-line" />
    <line x1="401" y1="20" x2="401" y2="385" class="grid-line" />
    <line x1="482" y1="20" x2="482" y2="385" class="grid-line" />

    <!-- Horizontal Column Grid (행E~행I) -->
    <line x1="10" y1="364" x2="525" y2="364" class="grid-line" />
    <line x1="10" y1="274" x2="525" y2="274" class="grid-line" />
    <line x1="10" y1="193" x2="525" y2="193" class="grid-line" />
    <line x1="10" y1="112" x2="525" y2="112" class="grid-line" />
    <line x1="10" y1="34" x2="525" y2="34" class="grid-line" />

    <!-- Grid Header Badges -->
    <text x="239" y="14" font-size="5.5" font-weight="700" fill="#64748B" text-anchor="middle" font-family="ui-monospace">열3</text>
    <text x="320" y="14" font-size="5.5" font-weight="700" fill="#64748B" text-anchor="middle" font-family="ui-monospace">열4</text>
    <text x="401" y="14" font-size="5.5" font-weight="700" fill="#64748B" text-anchor="middle" font-family="ui-monospace">열5</text>
    <text x="482" y="14" font-size="5.5" font-weight="700" fill="#64748B" text-anchor="middle" font-family="ui-monospace">열6</text>

    <text x="14" y="367" font-size="5.5" font-weight="700" fill="#64748B" font-family="ui-monospace">E</text>
    <text x="14" y="277" font-size="5.5" font-weight="700" fill="#64748B" font-family="ui-monospace">F</text>
    <text x="14" y="196" font-size="5.5" font-weight="700" fill="#64748B" font-family="ui-monospace">G</text>
    <text x="14" y="115" font-size="5.5" font-weight="700" fill="#64748B" font-family="ui-monospace">H</text>
  </g>

  <!-- ================= 2. TITLE BAR ================= -->
  <g id="title-block">
    <text x="20" y="24" font-size="7.8" font-weight="900" fill="#F8FAFC" letter-spacing="0.1px">계림 지하1층 마스터플랜 (230평 V4.2 · 5m×3 코어 &amp; 6셀 트윈 리그)</text>
    <text x="20" y="33" font-size="4.3" font-weight="700" fill="#94A3B8">웰컴라운지(6.55m) · 남측 에르그(2.0m) + 진입복도(1.5m) + 코어 5.5m[화장실 5m · 남 탈의/샤워 5m · 여 탈의/샤워 5m · 각 5수전 개방형]</text>
  </g>

  <!-- ================= 3. BASE ZONES LAYER ================= -->
  <g id="base-zones" filter="url(#softShadow)">
    <!-- TOTAL ARENA MAIN FLOOR BASE -->
    <polygon points="127.5,229.8 486,19.4 486,278 162,278" fill="url(#arenaFloorGrad)" stroke="#334155" stroke-width="0.8" />

    <!-- ZONE H-1: ROX ZONE (스트렝스 & 웨이트 고무매트 존: x=196~486, y=206~244, 폭 3.8m × 길이 29.0m = 33.4평) -->
    <rect x="196" y="206" width="290" height="38" fill="url(#hyroxWeightGrad)" stroke="#A855F7" stroke-width="0.8" stroke-dasharray="3 2" />

    <!-- ZONE H-2: 29.0m 3-LANE TURF ZONE (하단 동서 직선 3레인 터프: x=196~486, y=244~274, 폭 3.0m × 길이 29.0m = 26.3평) -->
    <rect x="196" y="244" width="290" height="30" fill="url(#grayTurfGrad)" stroke="#94A3B8" stroke-width="1.0" />
    <!-- Turf End & Center Turning Highlight Zones (좌측 1.0m / 중앙 2.0m / 우측 1.0m) -->
    <rect x="196" y="244" width="10" height="30" fill="#F59E0B" fill-opacity="0.18" stroke="#F59E0B" stroke-width="0.6" stroke-dasharray="2 1" />
    <rect x="331" y="244" width="20" height="30" fill="#10B981" fill-opacity="0.20" stroke="#10B981" stroke-width="0.8" stroke-dasharray="2 1" />
    <rect x="476" y="244" width="10" height="30" fill="#F59E0B" fill-opacity="0.18" stroke="#F59E0B" stroke-width="0.6" stroke-dasharray="2 1" />

    <!-- SOUTH AMENITY CORE (y=278~368, 총 깊이 9.0m × 총 폭 21.55m) -->
    <!-- 1. WELCOME LOUNGE (비움 · 문만 표시): x=162.0~227.5, y=278.0~368.0 (6.55m × 9.0m = 17.85평) -->
    <rect x="162" y="278" width="65.5" height="90" fill="url(#loungeGrad)" stroke="#D97706" stroke-width="1.0" />

    <!-- 2-A. SOUTH CARDIO ZONE (에르그존 2.0m): x=227.5~377.5, y=278.0~298.0 (15.0m × 2.0m = 9.1평) -->
    <rect x="227.5" y="278" width="150" height="20" fill="url(#ergZoneGrad)" stroke="#84CC16" stroke-width="0.9" />
    <line x1="162" y1="278" x2="377.5" y2="278" stroke="#84CC16" stroke-width="1.1" stroke-dasharray="4 2" />

    <!-- 2-B. CORE ENTRY CORRIDOR (코어 진입 복도 1.5m): x=227.5~377.5, y=298.0~313.0 (15.0m × 1.5m = 6.8평) -->
    <rect x="227.5" y="298" width="150" height="15" fill="#1E293B" fill-opacity="0.75" stroke="#64748B" stroke-width="0.8" />

    <!-- 3. RESTROOMS + INSTANT GAS WATER HEATER ROOM: x=227.5~277.5, y=313.0~368.0 (5.0m × 5.5m = 8.3평) -->
    <rect x="227.5" y="313" width="50" height="55" fill="url(#toiletGrad)" stroke="#64748B" stroke-width="1.0" />

    <!-- 4. MEN LOCKER (3.4m) + WALL (0.1m) + OPEN SHOWER (2.0m): x=277.5~327.5, y=313.0~368.0 (5.0m × 5.5m = 8.3평) -->
    <rect x="277.5" y="313" width="50" height="34" fill="url(#menLockerGrad)" stroke="#0284C7" stroke-width="1.0" />
    <rect x="277.5" y="348" width="50" height="20" fill="#0369A1" fill-opacity="0.65" stroke="#0284C7" stroke-width="1.0" />

    <!-- 5. WOMEN LOCKER (3.4m) + WALL (0.1m) + OPEN SHOWER (2.0m): x=327.5~377.5, y=313.0~368.0 (5.0m × 5.5m = 8.3평) -->
    <rect x="327.5" y="313" width="50" height="34" fill="url(#womenLockerGrad)" stroke="#A855F7" stroke-width="1.0" />
    <rect x="327.5" y="348" width="50" height="20" fill="#581C87" fill-opacity="0.65" stroke="#A855F7" stroke-width="1.0" />
  </g>

  <!-- ================= 4 & 5. 북서 사선벽 일렬 배치: [1] 빌트인 장비 수납랙 -> [2] ROWs 10대 직립보관 ================= -->
  <g id="erg-zone-machines">
    <g transform="translate(200.0, 187.3) rotate(-30.42)">
      <!-- (A) 빌트인 장비 수납랙 (x=0~120, 길이 12.0m × 깊이 0.75m) -->
      <rect x="0" y="1.5" width="120.0" height="7.5" fill="#1E293B" stroke="#64748B" stroke-width="0.8" rx="1.2" />
      <text x="60.0" y="6.5" font-size="3.1" font-weight="800" fill="#CBD5E1" text-anchor="middle">빌트인 장비 수납랙 (원판·덤벨·케틀벨·월볼)</text>

      <!-- (B) ROWs: 로잉 10대 직립 보관 (장비 수납랙 바로 오른쪽 끝: x=123.5~167.5, 길이 4.4m × 깊이 1.05m) -->
      <rect x="123.5" y="1.5" width="44.0" height="10.5" fill="#142616" stroke="#84CC16" stroke-width="0.8" rx="1.2" />
      <g fill="#0F172A" stroke="#4ADE80" stroke-width="0.55">
        <rect x="125.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="129.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="133.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="137.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="141.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="145.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="149.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="153.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="157.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
        <rect x="161.7" y="2.8" width="3.4" height="7.5" rx="0.5" />
      </g>
      <text x="145.5" y="16.0" font-size="2.6" font-weight="900" fill="#86EFAC" text-anchor="middle">ROWs (로잉 10대 세워서 직립보관)</text>
    </g>
  </g>

  <!-- ================= 6. METCON ZONE (UPPER RIGHT: 크로스핏 & 메트콘 아레나 75평) ================= -->
  <g id="metcon-zone">
    <g stroke="#334155" stroke-width="0.5" stroke-dasharray="2 2" fill="none">
      <rect x="290" y="148" width="32" height="22" rx="1.5" />
      <rect x="330" y="148" width="32" height="22" rx="1.5" />
      <rect x="370" y="148" width="32" height="22" rx="1.5" />
      <rect x="410" y="148" width="32" height="22" rx="1.5" />
      <rect x="370" y="118" width="32" height="22" rx="1.5" />
      <rect x="410" y="118" width="32" height="22" rx="1.5" />
      <rect x="410" y="88" width="32" height="22" rx="1.5" />
    </g>

    <text x="385" y="132" font-size="10.5" font-weight="900" fill="#F8FAFC" text-anchor="middle" letter-spacing="0.8px">METCON ZONE</text>
    <text x="385" y="142" font-size="4.8" font-weight="800" fill="#38BDF8" text-anchor="middle" font-family="ui-monospace">크로스핏 WOD &amp; 바벨·체조 메인 아레나 (내부 기둥간섭 0)</text>

    <path d="M 261.5 176 L 261.5 212" stroke="#A3E635" stroke-width="1.0" stroke-dasharray="2.5 2" />
    <polygon points="261.5,174 259.5,178 263.5,178" fill="#A3E635" />
    <polygon points="261.5,214 259.5,210 263.5,210" fill="#A3E635" />
    <text x="261.5" y="171.0" font-size="2.3" font-weight="900" fill="#BEF264" text-anchor="middle">◀ 메트콘↔터프 통로 (2.9m) ▶</text>
  </g>

  <!-- ================= 6-B. 기둥 G4 좌측: 바이크에르그 4대 (x=276~318, y=190.5~203.5) ================= -->
  <g id="g4-bikeergs">
    <rect x="276.0" y="190.5" width="42.0" height="13.0" fill="#142616" stroke="#84CC16" stroke-width="0.8" stroke-dasharray="2 1.5" rx="1.0" />
    <g fill="#0F172A" stroke="#FBBF24" stroke-width="0.6">
      <rect x="278.0" y="191.8" width="8.5" height="10.2" rx="0.8" />
      <rect x="288.5" y="191.8" width="8.5" height="10.2" rx="0.8" />
      <rect x="299.0" y="191.8" width="8.5" height="10.2" rx="0.8" />
      <rect x="309.5" y="191.8" width="8.5" height="10.2" rx="0.8" />
    </g>
    <g fill="#FBBF24">
      <rect x="279.5" y="200.5" width="5.5" height="1.2" rx="0.3" />
      <rect x="290.0" y="200.5" width="5.5" height="1.2" rx="0.3" />
      <rect x="300.5" y="200.5" width="5.5" height="1.2" rx="0.3" />
      <rect x="311.0" y="200.5" width="5.5" height="1.2" rx="0.3" />
    </g>
    <text x="282.25" y="197.2" font-size="1.8" font-weight="800" fill="#FEF3C7" text-anchor="middle">바이크1</text>
    <text x="292.75" y="197.2" font-size="1.8" font-weight="800" fill="#FEF3C7" text-anchor="middle">바이크2</text>
    <text x="303.25" y="197.2" font-size="1.8" font-weight="800" fill="#FEF3C7" text-anchor="middle">바이크3</text>
    <text x="313.75" y="197.2" font-size="1.8" font-weight="800" fill="#FEF3C7" text-anchor="middle">바이크4</text>
    <text x="297.0" y="186.5" font-size="2.3" font-weight="900" fill="#FDE68A" text-anchor="middle">바이크에르그 4대 (기둥 G4 좌측 ▼)</text>
  </g>

  <!-- ================= 7. CENTER AXIS: 트윈 사각 스테이션 RIG (각 7.2m×1.8m · 총 6스쿼트셀) ================= -->
  <g id="center-column-rig">
    <!-- RIG 세트 1 (G4 ~ G5 기둥 사이: x=328.5~400.5, y=188.0~206.0) -->
    <rect x="328.5" y="188.0" width="72.0" height="18.0" fill="#1E1B4B" fill-opacity="0.65" stroke="#EC4899" stroke-width="1.2" rx="0.8" />
    <g fill="#831843" fill-opacity="0.7" stroke="#F472B6" stroke-width="1.3">
      <rect x="328.5" y="188.0" width="12.0" height="18.0" />
      <rect x="358.5" y="188.0" width="12.0" height="18.0" />
      <rect x="388.5" y="188.0" width="12.0" height="18.0" />
    </g>
    <text x="334.5" y="198.2" font-size="2.0" font-weight="900" fill="#FBCFE8" text-anchor="middle">1.2m셀</text>
    <text x="349.5" y="198.2" font-size="1.9" font-weight="800" fill="#7DD3FC" text-anchor="middle">긴바1.8m</text>
    <text x="364.5" y="198.2" font-size="2.0" font-weight="900" fill="#FBCFE8" text-anchor="middle">1.2m셀</text>
    <text x="379.5" y="198.2" font-size="1.9" font-weight="800" fill="#7DD3FC" text-anchor="middle">긴바1.8m</text>
    <text x="394.5" y="198.2" font-size="2.0" font-weight="900" fill="#FBCFE8" text-anchor="middle">1.2m셀</text>
    <g fill="#F8FAFC">
      <circle cx="328.5" cy="188.0" r="1.1" /><circle cx="340.5" cy="188.0" r="1.1" />
      <circle cx="358.5" cy="188.0" r="1.1" /><circle cx="370.5" cy="188.0" r="1.1" />
      <circle cx="388.5" cy="188.0" r="1.1" /><circle cx="400.5" cy="188.0" r="1.1" />
      <circle cx="328.5" cy="206.0" r="1.1" /><circle cx="340.5" cy="206.0" r="1.1" />
      <circle cx="358.5" cy="206.0" r="1.1" /><circle cx="370.5" cy="206.0" r="1.1" />
      <circle cx="388.5" cy="206.0" r="1.1" /><circle cx="400.5" cy="206.0" r="1.1" />
    </g>

    <!-- RIG 세트 2 (G5 ~ G6 기둥 사이: x=409.5~481.5, y=188.0~206.0) -->
    <rect x="409.5" y="188.0" width="72.0" height="18.0" fill="#1E1B4B" fill-opacity="0.65" stroke="#EC4899" stroke-width="1.2" rx="0.8" />
    <g fill="#831843" fill-opacity="0.7" stroke="#F472B6" stroke-width="1.3">
      <rect x="409.5" y="188.0" width="12.0" height="18.0" />
      <rect x="439.5" y="188.0" width="12.0" height="18.0" />
      <rect x="469.5" y="188.0" width="12.0" height="18.0" />
    </g>
    <text x="415.5" y="198.2" font-size="2.0" font-weight="900" fill="#FBCFE8" text-anchor="middle">1.2m셀</text>
    <text x="430.5" y="198.2" font-size="1.9" font-weight="800" fill="#7DD3FC" text-anchor="middle">긴바1.8m</text>
    <text x="445.5" y="198.2" font-size="2.0" font-weight="900" fill="#FBCFE8" text-anchor="middle">1.2m셀</text>
    <text x="460.5" y="198.2" font-size="1.9" font-weight="800" fill="#7DD3FC" text-anchor="middle">긴바1.8m</text>
    <text x="475.5" y="198.2" font-size="2.0" font-weight="900" fill="#FBCFE8" text-anchor="middle">1.2m셀</text>
    <g fill="#F8FAFC">
      <circle cx="409.5" cy="188.0" r="1.1" /><circle cx="421.5" cy="188.0" r="1.1" />
      <circle cx="439.5" cy="188.0" r="1.1" /><circle cx="451.5" cy="188.0" r="1.1" />
      <circle cx="469.5" cy="188.0" r="1.1" /><circle cx="481.5" cy="188.0" r="1.1" />
      <circle cx="409.5" cy="206.0" r="1.1" /><circle cx="421.5" cy="206.0" r="1.1" />
      <circle cx="439.5" cy="206.0" r="1.1" /><circle cx="451.5" cy="206.0" r="1.1" />
      <circle cx="469.5" cy="206.0" r="1.1" /><circle cx="481.5" cy="206.0" r="1.1" />
    </g>

    <text x="405" y="181.5" font-size="2.4" font-weight="900" fill="#F472B6" text-anchor="middle" letter-spacing="0.05px">기둥 사이 트윈 사각 RIG (각 7.2m×1.8m · [1.2m+1.8m+1.2m+1.8m+1.2m] · 스쿼트 총 6셀)</text>
  </g>

  <!-- ================= 8. ROX ZONE (33.4평) + 29.0m TURF ZONE ================= -->
  <g id="hyrox-and-turf-zone">
    <text x="341" y="222.0" font-size="10.5" font-weight="900" fill="#F8FAFC" text-anchor="middle" letter-spacing="0.8px">ROX ZONE</text>
    <text x="341" y="231.0" font-size="4.5" font-weight="800" fill="#E879F9" text-anchor="middle" font-family="ui-monospace">하이록스 전반부 스트렝스 &amp; 웨이트 아레나 (고무매트 · 폭 3.8m × 길이 29.0m)</text>
    <text x="341" y="238.5" font-size="2.7" font-weight="700" fill="#C084FC" text-anchor="middle">사각 RIG 남측 스쿼트 6셀 · 덤벨·케틀벨·월볼 (잔디 손상 방지 &amp; 바벨 드랍존 3.8m)</text>

    <line x1="196" y1="254.0" x2="486" y2="254.0" stroke="#94A3B8" stroke-width="0.7" stroke-dasharray="5 3" />
    <line x1="196" y1="264.0" x2="486" y2="264.0" stroke="#94A3B8" stroke-width="0.7" stroke-dasharray="5 3" />

    <line x1="206" y1="244" x2="206" y2="274" stroke="#F59E0B" stroke-width="1.3" />
    <line x1="331" y1="244" x2="331" y2="274" stroke="#10B981" stroke-width="1.3" />
    <line x1="351" y1="244" x2="351" y2="274" stroke="#10B981" stroke-width="1.3" />
    <line x1="476" y1="244" x2="476" y2="274" stroke="#F59E0B" stroke-width="1.3" />

    <text x="201" y="242.0" font-size="2.6" font-weight="900" fill="#FBBF24" text-anchor="middle">좌터닝 1m</text>
    <text x="268.5" y="250.5" font-size="3.2" font-weight="900" fill="#E2E8F0" text-anchor="middle" font-family="ui-monospace">◀ 좌측 슬레드 코스 12.5m (3레인) ▶</text>
    <text x="341" y="250.5" font-size="3.0" font-weight="900" fill="#6EE7B7" text-anchor="middle" font-family="ui-monospace">중앙터닝 2.0m</text>
    <text x="413.5" y="250.5" font-size="3.2" font-weight="900" fill="#E2E8F0" text-anchor="middle" font-family="ui-monospace">◀ 우측 슬레드 코스 12.5m (3레인) ▶</text>
    <text x="481" y="242.0" font-size="2.6" font-weight="900" fill="#FBBF24" text-anchor="middle">우터닝 1m</text>

    <g fill="#0F172A" stroke="#10B981" stroke-width="0.7">
      <rect x="207.5" y="246.2" width="5.8" height="5.6" rx="0.8" />
      <rect x="207.5" y="256.2" width="5.8" height="5.6" rx="0.8" />
      <rect x="207.5" y="266.2" width="5.8" height="5.6" rx="0.8" />
    </g>
    <text x="210.4" y="249.8" font-size="1.7" font-weight="900" fill="#6EE7B7" text-anchor="middle">L1▶</text>
    <text x="210.4" y="259.8" font-size="1.7" font-weight="900" fill="#6EE7B7" text-anchor="middle">L2▶</text>
    <text x="210.4" y="269.8" font-size="1.7" font-weight="900" fill="#6EE7B7" text-anchor="middle">L3▶</text>

    <g fill="#0F172A" stroke="#38BDF8" stroke-width="0.7">
      <rect x="468.7" y="246.2" width="5.8" height="5.6" rx="0.8" />
      <rect x="468.7" y="256.2" width="5.8" height="5.6" rx="0.8" />
      <rect x="468.7" y="266.2" width="5.8" height="5.6" rx="0.8" />
    </g>
    <text x="471.6" y="249.8" font-size="1.7" font-weight="900" fill="#7DD3FC" text-anchor="middle">◀R1</text>
    <text x="471.6" y="259.8" font-size="1.7" font-weight="900" fill="#7DD3FC" text-anchor="middle">◀R2</text>
    <text x="471.6" y="269.8" font-size="1.7" font-weight="900" fill="#7DD3FC" text-anchor="middle">◀R3</text>

    <text x="268.5" y="261.2" font-size="4.9" font-weight="900" fill="#F8FAFC" text-anchor="middle">좌측 3대 출발 (12.5m)</text>
    <text x="413.5" y="261.2" font-size="4.9" font-weight="900" fill="#F8FAFC" text-anchor="middle">우측 3대 출발 (12.5m)</text>
    <text x="341" y="271.2" font-size="3.4" font-weight="900" fill="#A7F3D0" text-anchor="middle" font-family="ui-monospace">TURF ZONE (폭 3.0m × 길이 29.0m · 3레인 · 양끝 1m + 12.5m×2 + 중앙 2m)</text>
  </g>

  <!-- ================= 9. EAST WALL (크로스핏 칠판·타이머 H6 & 하이록스 칠판·타이머 G6) ================= -->
  <g id="east-wall-amenities">
    <rect x="482.6" y="124" width="2.2" height="24" fill="#0EA5E9" stroke="#E0F2FE" stroke-width="0.5" rx="0.5" />
    <text x="479.8" y="134.5" font-size="2.7" font-weight="900" fill="#38BDF8" text-anchor="end">크로스핏 칠판·타이머 ◀</text>
    <text x="479.8" y="138.8" font-size="2.2" font-weight="700" fill="#7DD3FC" text-anchor="end">(H6 기둥 측 벽면)</text>

    <rect x="482.6" y="214" width="2.2" height="24" fill="#D946EF" stroke="#FAE8FF" stroke-width="0.5" rx="0.5" />
    <text x="479.8" y="224.5" font-size="2.7" font-weight="900" fill="#F472B6" text-anchor="end">ROX 칠판·타이머 ◀</text>
    <text x="479.8" y="228.8" font-size="2.2" font-weight="700" fill="#F5D0FE" text-anchor="end">(G6 ROX존 벽면)</text>
  </g>

  <!-- ================= 10. SOUTH AMENITY CORE (6.55m LOUNGE + 2.0m ERG + 1.5m CORRIDOR + 5.5m CORE ROOMS) ================= -->
  <g id="amenities-layer">
    <!-- ZONE 1: WELCOME LOUNGE (x=162.0~227.5, y=278.0~368.0, 6.55m × 9.0m = 17.85평 · 내부 비움) -->
    <text x="194.75" y="320.0" font-size="5.8" font-weight="900" fill="#FBBF24" text-anchor="middle">웰컴 라운지</text>
    <text x="194.75" y="327.0" font-size="3.6" font-weight="700" fill="#FDE68A" text-anchor="middle" font-family="ui-monospace">(17.85평 · 6.55×9.0m)</text>

    <!-- ZONE 1-B: SOUTH CARDIO ZONE (폭 2.0m: x=227.5~377.5, y=278.0~298.0) -->
    <!-- West Group: SkiErg ×6 Facing North (▲ 운동구역 방향, x=230.0~295.0, y=279.5~290.5) -->
    <g fill="#0F172A" stroke="#A3E635" stroke-width="0.65">
      <rect x="230.0" y="279.5" width="9.0" height="11.0" rx="0.9" />
      <rect x="241.2" y="279.5" width="9.0" height="11.0" rx="0.9" />
      <rect x="252.4" y="279.5" width="9.0" height="11.0" rx="0.9" />
      <rect x="263.6" y="279.5" width="9.0" height="11.0" rx="0.9" />
      <rect x="274.8" y="279.5" width="9.0" height="11.0" rx="0.9" />
      <rect x="286.0" y="279.5" width="9.0" height="11.0" rx="0.9" />
    </g>
    <g fill="#A3E635">
      <rect x="231.5" y="279.5" width="6.0" height="1.3" />
      <rect x="242.7" y="279.5" width="6.0" height="1.3" />
      <rect x="253.9" y="279.5" width="6.0" height="1.3" />
      <rect x="265.1" y="279.5" width="6.0" height="1.3" />
      <rect x="276.3" y="279.5" width="6.0" height="1.3" />
      <rect x="287.5" y="279.5" width="6.0" height="1.3" />
    </g>
    <text x="234.5" y="286.3" font-size="1.8" font-weight="800" fill="#ECFCCB" text-anchor="middle">▲스키1</text>
    <text x="245.7" y="286.3" font-size="1.8" font-weight="800" fill="#ECFCCB" text-anchor="middle">▲스키2</text>
    <text x="256.9" y="286.3" font-size="1.8" font-weight="800" fill="#ECFCCB" text-anchor="middle">▲스키3</text>
    <text x="268.1" y="286.3" font-size="1.8" font-weight="800" fill="#ECFCCB" text-anchor="middle">▲스키4</text>
    <text x="279.3" y="286.3" font-size="1.8" font-weight="800" fill="#ECFCCB" text-anchor="middle">▲스키5</text>
    <text x="290.5" y="286.3" font-size="1.8" font-weight="800" fill="#ECFCCB" text-anchor="middle">▲스키6</text>
    <text x="262.5" y="295.2" font-size="2.1" font-weight="800" fill="#BEF264" text-anchor="middle">남측 에르그존 (폭 2.0m · 스키6 &amp; 트레드밀6·1.75m)</text>

    <!-- East Group: Curved Treadmill ×6 Facing North (길이 1.75m=17.5px, 폭 0.88m=8.8px, x=301.5~373.3, y=279.2~296.7) -->
    <g fill="#0F172A" stroke="#38BDF8" stroke-width="0.7">
      <rect x="301.5" y="279.2" width="8.8" height="17.5" rx="0.9" />
      <rect x="314.1" y="279.2" width="8.8" height="17.5" rx="0.9" />
      <rect x="326.7" y="279.2" width="8.8" height="17.5" rx="0.9" />
      <rect x="339.3" y="279.2" width="8.8" height="17.5" rx="0.9" />
      <rect x="351.9" y="279.2" width="8.8" height="17.5" rx="0.9" />
      <rect x="364.5" y="279.2" width="8.8" height="17.5" rx="0.9" />
    </g>
    <g fill="#0284C7">
      <rect x="302.7" y="280.0" width="6.4" height="1.5" rx="0.3" />
      <rect x="315.3" y="280.0" width="6.4" height="1.5" rx="0.3" />
      <rect x="327.9" y="280.0" width="6.4" height="1.5" rx="0.3" />
      <rect x="340.5" y="280.0" width="6.4" height="1.5" rx="0.3" />
      <rect x="353.1" y="280.0" width="6.4" height="1.5" rx="0.3" />
      <rect x="365.7" y="280.0" width="6.4" height="1.5" rx="0.3" />
    </g>
    <text x="305.9" y="288.0" font-size="1.8" font-weight="900" fill="#E0F2FE" text-anchor="middle">▲RUN1</text>
    <text x="318.5" y="288.0" font-size="1.8" font-weight="900" fill="#E0F2FE" text-anchor="middle">▲RUN2</text>
    <text x="331.1" y="288.0" font-size="1.8" font-weight="900" fill="#E0F2FE" text-anchor="middle">▲RUN3</text>
    <text x="343.7" y="288.0" font-size="1.8" font-weight="900" fill="#E0F2FE" text-anchor="middle">▲RUN4</text>
    <text x="356.3" y="288.0" font-size="1.8" font-weight="900" fill="#E0F2FE" text-anchor="middle">▲RUN5</text>
    <text x="368.9" y="288.0" font-size="1.8" font-weight="900" fill="#E0F2FE" text-anchor="middle">▲RUN6</text>

    <!-- ZONE 1-C: 1.5m CORE ENTRY CORRIDOR (x=227.5~377.5, y=298.0~313.0) -->
    <line x1="232" y1="305.5" x2="373" y2="305.5" stroke="#FBBF24" stroke-width="0.6" stroke-dasharray="2.5 2" />
    <rect x="262" y="301.2" width="81" height="8.6" rx="1.5" fill="#0F172A" stroke="#F59E0B" stroke-width="0.5" />
    <text x="302.5" y="306.6" font-size="2.5" font-weight="900" fill="#FDE68A" text-anchor="middle">◀ 코어 진입 복도 (폭 1.5m · 화장실/탈의실 진입) ▶</text>


    <!-- ZONE 2: MEN & WOMEN RESTROOMS + INSTANT GAS WATER HEATER ROOM (x=227.5~277.5, y=313.0~368.0, 5.0m × 5.5m = 8.3평) -->
    <!-- Central Vertical Plumbing Partition Wall (x=251.8~253.2) -->
    <rect x="251.8" y="313.0" width="1.4" height="55.0" fill="#64748B" stroke="#CBD5E1" stroke-width="0.4" />

    <!-- (A) Men's Restroom (Left: x=227.5~251.8, y=313.0~368.0, 폭 2.5m × 깊이 5.5m) -->
    <!-- Men Sinks x2 (Green box against central wall top: x=245.8~251.8, y=313.8~326.8) -->
    <rect x="245.8" y="313.8" width="6.0" height="13.0" fill="#10B981" fill-opacity="0.85" stroke="#059669" stroke-width="0.5" />
    <ellipse cx="248.8" cy="317.2" rx="1.6" ry="2.3" fill="#FFFFFF" stroke="#047857" stroke-width="0.4" />
    <ellipse cx="248.8" cy="323.4" rx="1.6" ry="2.3" fill="#FFFFFF" stroke="#047857" stroke-width="0.4" />

    <!-- Men Toilet Stalls 1 & 2 (Beige boxes against central wall middle: x=239.0~251.8, y=327.2~349.2) -->
    <rect x="239.0" y="327.2" width="12.8" height="11.0" fill="#FDE68A" fill-opacity="0.88" stroke="#92400E" stroke-width="0.5" />
    <text x="245.4" y="332.2" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">남자</text>
    <text x="245.4" y="334.8" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">대변기 1</text>

    <rect x="239.0" y="338.2" width="12.8" height="11.0" fill="#FDE68A" fill-opacity="0.88" stroke="#92400E" stroke-width="0.5" />
    <text x="245.4" y="343.2" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">남자</text>
    <text x="245.4" y="345.8" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">대변기 2</text>

    <!-- Men Urinals x2 (Brown box against central wall bottom: x=247.2~251.8, y=351.0~365.5) -->
    <rect x="247.2" y="351.0" width="4.6" height="14.5" fill="#78350F" stroke="#B45309" stroke-width="0.5" />
    <rect x="248.2" y="352.6" width="2.6" height="4.6" rx="0.8" fill="#FFFFFF" />
    <rect x="248.2" y="359.2" width="2.6" height="4.6" rx="0.8" fill="#FFFFFF" />
    <text x="243.5" y="356.5" font-size="1.6" font-weight="800" fill="#F8FAFC" text-anchor="middle">남자</text>
    <text x="243.5" y="358.8" font-size="1.6" font-weight="800" fill="#F8FAFC" text-anchor="middle">소변기2</text>

    <!-- Cleaning Sink (South-West corner: x=228.8~236.6, y=358.8~366.6) -->
    <rect x="228.8" y="358.8" width="7.8" height="7.8" rx="1.6" fill="#0284C7" stroke="#BAE6FD" stroke-width="0.5" />
    <text x="232.7" y="362.2" font-size="1.6" font-weight="900" fill="#FFFFFF" text-anchor="middle">청소용</text>
    <text x="232.7" y="364.5" font-size="1.6" font-weight="900" fill="#FFFFFF" text-anchor="middle">수전</text>

    <text x="233.2" y="328.0" font-size="2.1" font-weight="900" fill="#38BDF8" text-anchor="middle">남자 화장실</text>
    <text x="233.2" y="331.0" font-size="1.6" font-weight="700" fill="#94A3B8" text-anchor="middle">(2.5×5.5m)</text>

    <!-- (B) Women's Restroom + Instant Gas Water Heater Room (Right: x=253.2~277.5, y=313.0~368.0, 폭 2.5m × 깊이 5.5m) -->
    <!-- Women Sinks x2 (Green box against central wall top: x=253.2~259.2, y=313.8~326.8) -->
    <rect x="253.2" y="313.8" width="6.0" height="13.0" fill="#10B981" fill-opacity="0.85" stroke="#059669" stroke-width="0.5" />
    <ellipse cx="256.2" cy="317.2" rx="1.6" ry="2.3" fill="#FFFFFF" stroke="#047857" stroke-width="0.4" />
    <ellipse cx="256.2" cy="323.4" rx="1.6" ry="2.3" fill="#FFFFFF" stroke="#047857" stroke-width="0.4" />
    <text x="263.2" y="321.0" font-size="1.8" font-weight="900" fill="#86EFAC" text-anchor="middle">세면대</text>

    <!-- Women Toilet Stalls 1, 2, 3 (Beige boxes against central wall: x=253.2~266.0, y=327.2~357.2) -->
    <rect x="253.2" y="327.2" width="12.8" height="10.0" fill="#FDE68A" fill-opacity="0.88" stroke="#92400E" stroke-width="0.5" />
    <text x="259.6" y="331.8" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">여자</text>
    <text x="259.6" y="334.4" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">대변기 1</text>

    <rect x="253.2" y="337.2" width="12.8" height="10.0" fill="#FDE68A" fill-opacity="0.88" stroke="#92400E" stroke-width="0.5" />
    <text x="259.6" y="341.8" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">여자</text>
    <text x="259.6" y="344.4" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">대변기 2</text>

    <rect x="253.2" y="347.2" width="12.8" height="10.0" fill="#FDE68A" fill-opacity="0.88" stroke="#92400E" stroke-width="0.5" />
    <text x="259.6" y="351.8" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">여자</text>
    <text x="259.6" y="354.4" font-size="1.8" font-weight="900" fill="#1E293B" text-anchor="middle">대변기 3</text>

    <text x="271.8" y="326.0" font-size="2.1" font-weight="900" fill="#E9D5FF" text-anchor="middle">여자 화장실</text>
    <text x="271.8" y="329.0" font-size="1.6" font-weight="700" fill="#C084FC" text-anchor="middle">(2.5×5.5m)</text>

    <!-- Instant Gas Water Heater Room (South end of Women's Restroom: x=253.2~277.5, y=357.2~368.0) -->
    <rect x="253.2" y="357.2" width="24.3" height="10.8" fill="#0F172A" stroke="#64748B" stroke-width="0.6" />
    <!-- Sliding Door across right aisle (x=266.0~277.2, y=357.2) -->
    <line x1="266.0" y1="357.2" x2="277.2" y2="357.2" stroke="#22C55E" stroke-width="1.2" stroke-dasharray="1.8 0.8" />
    <text x="271.6" y="355.8" font-size="1.4" font-weight="900" fill="#86EFAC" text-anchor="middle">◀슬라이딩도어▶</text>
    <!-- 3 Wall-mounted Instant Gas Water Heaters on South Wall -->
    <rect x="254.2" y="363.2" width="6.8" height="3.2" rx="0.8" fill="#1E3A8A" stroke="#60A5FA" stroke-width="0.5" />
    <rect x="261.9" y="363.2" width="6.8" height="3.2" rx="0.8" fill="#1E3A8A" stroke="#60A5FA" stroke-width="0.5" />
    <rect x="269.6" y="363.2" width="6.8" height="3.2" rx="0.8" fill="#1E3A8A" stroke="#60A5FA" stroke-width="0.5" />
    <text x="265.3" y="361.4" font-size="1.6" font-weight="900" fill="#93C5FD" text-anchor="middle">벽걸이 순간 가스온수기 3대</text>


    <!-- ZONE 3: MEN LOCKER (3.4m) + MASONRY WALL (0.1m) + OPEN SHOWER (2.0m, 5수전) (x=277.5~327.5, y=313.0~368.0, 5.0m × 5.5m = 8.3평) -->
    <!-- Green Privacy Entry Corridor (Top-Right: x=318.0~327.3, y=313.2~334.5) -->
    <rect x="318.0" y="313.2" width="9.3" height="21.3" fill="#10B981" fill-opacity="0.80" stroke="#059669" stroke-width="0.5" />
    <text x="322.6" y="324.0" font-size="1.6" font-weight="900" fill="#022C22" text-anchor="middle" transform="rotate(90 322.6 324.0)">진입통로(시선차단)</text>
    <!-- Beige Privacy Baffle Wall (x=316.3~318.0, y=313.2~334.5) -->
    <rect x="316.3" y="313.2" width="1.7" height="21.3" fill="#FDE68A" stroke="#B45309" stroke-width="0.4" />
    <!-- Right-side Lockers backed against Baffle Wall (4 boxes) -->
    <g fill="#A16207" stroke="#451A03" stroke-width="0.4">
      <rect x="311.5" y="313.2" width="4.8" height="3.7" />
      <rect x="311.5" y="316.9" width="4.8" height="3.7" />
      <rect x="311.5" y="320.6" width="4.8" height="3.7" />
      <rect x="311.5" y="324.3" width="4.8" height="3.7" />
    </g>
    <!-- Left-side Lockers along West Wall (6 boxes) -->
    <g fill="#A16207" stroke="#451A03" stroke-width="0.4">
      <rect x="277.7" y="313.2" width="5.0" height="3.4" />
      <rect x="277.7" y="316.6" width="5.0" height="3.4" />
      <rect x="277.7" y="320.0" width="5.0" height="3.4" />
      <rect x="277.7" y="323.4" width="5.0" height="3.4" />
      <rect x="277.7" y="326.8" width="5.0" height="3.4" />
      <rect x="277.7" y="330.2" width="5.0" height="3.4" />
    </g>
    <text x="283.8" y="319.5" font-size="1.8" font-weight="900" fill="#F8FAFC">옷장락카</text>
    <text x="283.8" y="322.2" font-size="1.8" font-weight="900" fill="#FDE68A">총 24칸</text>

    <text x="299.5" y="328.5" font-size="2.7" font-weight="900" fill="#FFFFFF" text-anchor="middle">남자 탈의실</text>
    <text x="299.5" y="332.0" font-size="1.9" font-weight="800" fill="#BAE6FD" text-anchor="middle">(5.0×3.4m)</text>

    <!-- Dry Powder Mirrors x3 (Yellow capsules on North face of masonry wall) -->
    <rect x="289.0" y="341.8" width="25.0" height="4.6" rx="2.0" fill="none" stroke="#FACC15" stroke-width="0.6" />
    <rect x="290.2" y="342.6" width="6.6" height="3.0" rx="1.2" fill="#FACC15" />
    <rect x="298.2" y="342.6" width="6.6" height="3.0" rx="1.2" fill="#FACC15" />
    <rect x="306.2" y="342.6" width="6.6" height="3.0" rx="1.2" fill="#FACC15" />
    <text x="301.5" y="340.5" font-size="1.9" font-weight="900" fill="#FEF08A" text-anchor="middle">파우더 거울 3개</text>

    <!-- 0.1m Masonry Wall (x=287.5~327.5, y=347.0~348.0) + Left Shower Door (x=278.0~287.5) -->
    <rect x="287.5" y="347.0" width="40.0" height="1.0" fill="#94A3B8" stroke="#E2E8F0" stroke-width="0.4" />
    <rect x="278.0" y="347.0" width="9.5" height="1.0" fill="#020617" stroke="#F8FAFC" stroke-width="0.5" />
    <path d="M 287.5 348.0 A 7.0 7.0 0 0 1 280.5 355.0" class="door-swing" stroke="#BAE6FD" />

    <!-- Men Open Shower Room (x=277.5~327.5, y=348.0~368.0, 5.0×2.0m · 5수전 · 개방형 통로 + 부분 파티션) -->
    <line x1="283.0" y1="352.2" x2="323.5" y2="352.2" stroke="#BAE6FD" stroke-width="0.5" stroke-dasharray="1.8 1.2" />
    <text x="302.5" y="351.0" font-size="1.5" font-weight="800" fill="#E0F2FE" text-anchor="middle">개방형 샤워실 내부 통로 (파티션 뒤 이동)</text>
    <text x="302.5" y="357.2" font-size="2.4" font-weight="900" fill="#FFFFFF" text-anchor="middle">남자 샤워실 (5수전 · 2.0m)</text>
    <!-- 5 Showerheads + 4 Partial Partitions (y=359.5~367.5) -->
    <circle cx="282.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="292.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="302.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="312.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="322.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <line x1="287.5" y1="359.5" x2="287.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />
    <line x1="297.5" y1="359.5" x2="297.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />
    <line x1="307.5" y1="359.5" x2="307.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />
    <line x1="317.5" y1="359.5" x2="317.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />


    <!-- ZONE 4: WOMEN LOCKER (3.4m) + MASONRY WALL (0.1m) + OPEN SHOWER (2.0m, 5수전) (x=327.5~377.5, y=313.0~368.0, 5.0m × 5.5m = 8.3평) -->
    <!-- Green Privacy Entry Corridor (Top-Right: x=368.0~377.3, y=313.2~334.5) -->
    <rect x="368.0" y="313.2" width="9.3" height="21.3" fill="#10B981" fill-opacity="0.80" stroke="#059669" stroke-width="0.5" />
    <text x="372.6" y="324.0" font-size="1.6" font-weight="900" fill="#022C22" text-anchor="middle" transform="rotate(90 372.6 324.0)">진입통로(시선차단)</text>
    <!-- Beige Privacy Baffle Wall (x=366.3~368.0, y=313.2~334.5) -->
    <rect x="366.3" y="313.2" width="1.7" height="21.3" fill="#FDE68A" stroke="#B45309" stroke-width="0.4" />
    <!-- Right-side Lockers backed against Baffle Wall (4 boxes) -->
    <g fill="#A16207" stroke="#451A03" stroke-width="0.4">
      <rect x="361.5" y="313.2" width="4.8" height="3.7" />
      <rect x="361.5" y="316.9" width="4.8" height="3.7" />
      <rect x="361.5" y="320.6" width="4.8" height="3.7" />
      <rect x="361.5" y="324.3" width="4.8" height="3.7" />
    </g>
    <!-- Left-side Lockers along West Wall (6 boxes) -->
    <g fill="#A16207" stroke="#451A03" stroke-width="0.4">
      <rect x="327.7" y="313.2" width="5.0" height="3.4" />
      <rect x="327.7" y="316.6" width="5.0" height="3.4" />
      <rect x="327.7" y="320.0" width="5.0" height="3.4" />
      <rect x="327.7" y="323.4" width="5.0" height="3.4" />
      <rect x="327.7" y="326.8" width="5.0" height="3.4" />
      <rect x="327.7" y="330.2" width="5.0" height="3.4" />
    </g>
    <text x="333.8" y="319.5" font-size="1.8" font-weight="900" fill="#F8FAFC">옷장락카</text>
    <text x="333.8" y="322.2" font-size="1.8" font-weight="900" fill="#FDE68A">총 24칸</text>

    <text x="349.5" y="328.5" font-size="2.7" font-weight="900" fill="#FFFFFF" text-anchor="middle">여자 탈의실</text>
    <text x="349.5" y="332.0" font-size="1.9" font-weight="800" fill="#F5D0FE" text-anchor="middle">(5.0×3.4m)</text>

    <!-- Dry Powder Mirrors x3 -->
    <rect x="339.0" y="341.8" width="25.0" height="4.6" rx="2.0" fill="none" stroke="#FACC15" stroke-width="0.6" />
    <rect x="340.2" y="342.6" width="6.6" height="3.0" rx="1.2" fill="#FACC15" />
    <rect x="348.2" y="342.6" width="6.6" height="3.0" rx="1.2" fill="#FACC15" />
    <rect x="356.2" y="342.6" width="6.6" height="3.0" rx="1.2" fill="#FACC15" />
    <text x="351.5" y="340.5" font-size="1.9" font-weight="900" fill="#FEF08A" text-anchor="middle">파우더 거울 3개</text>

    <!-- 0.1m Masonry Wall (x=337.5~377.5, y=347.0~348.0) + Left Shower Door (x=328.0~337.5) -->
    <rect x="337.5" y="347.0" width="40.0" height="1.0" fill="#94A3B8" stroke="#E2E8F0" stroke-width="0.4" />
    <rect x="328.0" y="347.0" width="9.5" height="1.0" fill="#020617" stroke="#F8FAFC" stroke-width="0.5" />
    <path d="M 337.5 348.0 A 7.0 7.0 0 0 1 330.5 355.0" class="door-swing" stroke="#F5D0FE" />

    <!-- Women Open Shower Room (x=327.5~377.5, y=348.0~368.0, 5.0×2.0m · 5수전 · 개방형 통로 + 부분 파티션) -->
    <line x1="333.0" y1="352.2" x2="373.5" y2="352.2" stroke="#F5D0FE" stroke-width="0.5" stroke-dasharray="1.8 1.2" />
    <text x="352.5" y="351.0" font-size="1.5" font-weight="800" fill="#F5D0FE" text-anchor="middle">개방형 샤워실 내부 통로 (파티션 뒤 이동)</text>
    <text x="352.5" y="357.2" font-size="2.4" font-weight="900" fill="#FFFFFF" text-anchor="middle">여자 샤워실 (5수전 · 2.0m)</text>
    <!-- 5 Showerheads + 4 Partial Partitions -->
    <circle cx="332.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="342.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="352.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="362.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <circle cx="372.5" cy="365.2" r="1.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="0.5" />
    <line x1="337.5" y1="359.5" x2="337.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />
    <line x1="347.5" y1="359.5" x2="347.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />
    <line x1="357.5" y1="359.5" x2="357.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />
    <line x1="367.5" y1="359.5" x2="367.5" y2="367.6" stroke="#E2E8F0" stroke-width="1.1" stroke-linecap="round" />


    <!-- ZONE 6: A.H.U CORE (공조실: x=377.5~486, y=278~368) -->
    <rect x="377.5" y="278" width="108.5" height="90" fill="#0B132B" stroke="#334155" stroke-width="1.0" />
    <text x="444" y="322" font-size="7.5" font-weight="900" fill="#475569" text-anchor="middle">공조실 (A.H.U)</text>
    <text x="444" y="330" font-size="4.0" font-weight="700" fill="#334155" text-anchor="middle">건물 설비 코어 (원형 보존)</text>
  </g>

  <!-- ================= 11. WALLS, COLUMNS & DOORS ================= -->
  <g id="walls-structure">
    <!-- Perimeter Outer Building Walls -->
    <polygon points="162,368 486,368 486,19.4 127.5,229.8 162,278" class="outer-wall" />

    <!-- Interior Structural Partitions between South Amenities -->
    <line x1="162" y1="278" x2="162" y2="368" class="inner-wall" />
    <line x1="227.5" y1="313" x2="227.5" y2="368" class="inner-wall" />
    <line x1="277.5" y1="313" x2="277.5" y2="368" class="inner-wall" />
    <line x1="327.5" y1="313" x2="327.5" y2="368" class="inner-wall" />
    <line x1="377.5" y1="278" x2="377.5" y2="368" class="inner-wall" />
    <line x1="227.5" y1="313" x2="377.5" y2="313" class="inner-wall" />

    <!-- Structural Columns (8.1m Grid) -->
    <rect x="158" y="274" width="8" height="8" class="col-box" />
    <rect x="239" y="274" width="8" height="8" class="col-box" />
    <rect x="320" y="274" width="8" height="8" class="col-box" />
    <rect x="401" y="274" width="8" height="8" class="col-box" />
    <rect x="482" y="274" width="8" height="8" class="col-box" />

    <rect x="159" y="366.5" width="6" height="4" class="col-box" />
    <rect x="236" y="366.5" width="6" height="4" class="col-box" />
    <rect x="324.5" y="366.5" width="6" height="4" class="col-box" />
    
    <!-- Row G Columns (y=193) -->
    <rect x="239" y="193" width="8" height="8" class="col-box" />
    <rect x="320" y="193" width="8" height="8" class="col-box" />
    <rect x="401" y="193" width="8" height="8" class="col-box" />
    <rect x="482" y="193" width="8" height="8" class="col-box" />
    <text x="324" y="198" font-size="2.6" font-weight="900" fill="#94A3B8" text-anchor="middle">G4</text>
    <text x="405" y="198" font-size="2.6" font-weight="900" fill="#94A3B8" text-anchor="middle">G5</text>
    <text x="486" y="198" font-size="2.6" font-weight="900" fill="#94A3B8" text-anchor="middle">G6</text>

    <rect x="316" y="109" width="8" height="8" class="col-box" />
    <rect x="401" y="112" width="8" height="8" class="col-box" />
    <rect x="482" y="112" width="8" height="8" class="col-box" />
    <rect x="482" y="34" width="8" height="8" class="col-box" />

    <!-- DOORS & OPENINGS -->
    <!-- 1. Welcome Lounge Double-Swing Main Entrance Door (양문형 출입문 2.0m · 안팎 개폐: x=162, y=322~342) -->
    <line x1="162" y1="322" x2="162" y2="342" stroke="#090D16" stroke-width="2.6" />
    <!-- Inward Swing Arcs (Top leaf y=322..332, Bottom leaf y=332..342) -->
    <path d="M172 322 A10 10 0 0 1 162 332" class="door-swing" stroke="#F59E0B" />
    <path d="M172 342 A10 10 0 0 0 162 332" class="door-swing" stroke="#F59E0B" />
    <!-- Outward Swing Arcs -->
    <path d="M152 322 A10 10 0 0 0 162 332" class="door-swing" stroke="#F59E0B" stroke-opacity="0.65" />
    <path d="M152 342 A10 10 0 0 1 162 332" class="door-swing" stroke="#F59E0B" stroke-opacity="0.65" />
    <line x1="162" y1="322" x2="170" y2="325.5" stroke="#FBBF24" stroke-width="1.2" />
    <line x1="162" y1="342" x2="170" y2="338.5" stroke="#FBBF24" stroke-width="1.2" />
    <text x="145" y="314" font-size="4.4" font-weight="800" fill="#F59E0B" text-anchor="middle">양문형 출입문</text>
    <text x="145" y="319" font-size="3.1" font-weight="700" fill="#FDE68A" text-anchor="middle">(2.0m · 안팎개폐)</text>

    <!-- 2. Men's Restroom North Door (x=229.5~238.5, y=313.0) -->
    <rect x="229.5" y="312.3" width="9.0" height="1.4" fill="#020617" stroke="#F8FAFC" stroke-width="0.5" />
    <path d="M238.5 313.0 A9.0 9.0 0 0 1 229.5 322.0" class="door-swing" stroke="#94A3B8" />

    <!-- 3. Women's Restroom North Door (x=266.5~275.5, y=313.0) -->
    <rect x="266.5" y="312.3" width="9.0" height="1.4" fill="#020617" stroke="#F8FAFC" stroke-width="0.5" />
    <path d="M266.5 313.0 A9.0 9.0 0 0 0 275.5 322.0" class="door-swing" stroke="#C084FC" />

    <!-- 4. Men's Locker Room North-Right Door (x=318.0~327.0, y=313.0) -->
    <rect x="318.0" y="312.3" width="9.0" height="1.4" fill="#020617" stroke="#F8FAFC" stroke-width="0.5" />
    <path d="M318.0 313.0 A9.0 9.0 0 0 0 327.0 322.0" class="door-swing" stroke="#86EFAC" />

    <!-- 5. Women's Locker Room North-Right Door (x=368.0~377.0, y=313.0) -->
    <rect x="368.0" y="312.3" width="9.0" height="1.4" fill="#020617" stroke="#F8FAFC" stroke-width="0.5" />
    <path d="M368.0 313.0 A9.0 9.0 0 0 0 377.0 322.0" class="door-swing" stroke="#86EFAC" />
  </g>

  <!-- ================= 12. EXACT ARCHITECTURAL DIMENSIONS (치수선 체계) ================= -->
  <g id="dimension-lines">
    <!-- Top Dimension Line for 1 SPAN (8.1m Column Grid) -->
    <g transform="translate(320, 24)">
      <line x1="0" y1="0" x2="81" y2="0" class="dim-line" stroke="#E2E8F0" stroke-width="1.2" />
      <line x1="0" y1="-3" x2="0" y2="3" class="dim-tick" stroke="#E2E8F0" stroke-width="1.4" />
      <line x1="81" y1="-3" x2="81" y2="3" class="dim-tick" stroke="#E2E8F0" stroke-width="1.4" />
      <text x="40.5" y="-4" class="dim-text" fill="#E2E8F0" text-anchor="middle">1 SPAN = 8.1m (기둥 간격)</text>
    </g>

    <!-- Right-side Vertical Depth Dimensions for 1.8m RIG + ROX ZONE (3.8m) + TURF (3.0m) at x=494 -->
    <line x1="494" y1="188" x2="494" y2="206" class="dim-line" stroke="#F472B6" stroke-width="1.0" />
    <line x1="491" y1="188" x2="497" y2="188" class="dim-tick" stroke="#F472B6" stroke-width="1.2" />
    <line x1="491" y1="206" x2="497" y2="206" class="dim-tick" stroke="#F472B6" stroke-width="1.2" />
    <text x="499" y="198.5" class="dim-text" fill="#F472B6" text-anchor="start">RIG 1.8m</text>

    <line x1="494" y1="206" x2="494" y2="244" class="dim-line" stroke="#C084FC" stroke-width="1.0" />
    <line x1="491" y1="206" x2="497" y2="206" class="dim-tick" stroke="#C084FC" stroke-width="1.2" />
    <line x1="491" y1="244" x2="497" y2="244" class="dim-tick" stroke="#C084FC" stroke-width="1.2" />
    <text x="499" y="226.5" class="dim-text" fill="#E9D5FF" text-anchor="start">ROX 3.8m</text>

    <line x1="494" y1="244" x2="494" y2="274" class="dim-line" stroke="#6EE7B7" stroke-width="1.0" />
    <line x1="491" y1="244" x2="497" y2="244" class="dim-tick" stroke="#6EE7B7" stroke-width="1.2" />
    <line x1="491" y1="274" x2="497" y2="274" class="dim-tick" stroke="#6EE7B7" stroke-width="1.2" />
    <text x="499" y="260.5" class="dim-text" fill="#6EE7B7" text-anchor="start">터프 3.0m</text>

    <!-- South Core Width Dimensions Chain (at y=376) -->
    <line x1="162" y1="376" x2="227.5" y2="376" class="dim-line" stroke="#FBBF24" />
    <line x1="162" y1="373" x2="162" y2="379" class="dim-tick" stroke="#FBBF24" />
    <line x1="227.5" y1="373" x2="227.5" y2="379" class="dim-tick" stroke="#FBBF24" />
    <text x="194.75" y="383" class="dim-text" fill="#FDE68A" text-anchor="middle">6.55m (라운지)</text>

    <line x1="227.5" y1="376" x2="277.5" y2="376" class="dim-line" />
    <line x1="277.5" y1="373" x2="277.5" y2="379" class="dim-tick" />
    <text x="252.5" y="383" class="dim-text" text-anchor="middle">5.0m (남·여 화장실)</text>

    <line x1="277.5" y1="376" x2="327.5" y2="376" class="dim-line" stroke="#38BDF8" />
    <line x1="327.5" y1="373" x2="327.5" y2="379" class="dim-tick" stroke="#38BDF8" />
    <text x="302.5" y="383" class="dim-text" fill="#38BDF8" text-anchor="middle">5.0m (남자 탈의·샤워)</text>

    <line x1="327.5" y1="376" x2="377.5" y2="376" class="dim-line" stroke="#C084FC" />
    <line x1="377.5" y1="373" x2="377.5" y2="379" class="dim-tick" stroke="#C084FC" />
    <text x="352.5" y="383" class="dim-text" fill="#C084FC" text-anchor="middle">5.0m (여자 탈의·샤워)</text>

    <line x1="162" y1="389" x2="377.5" y2="389" class="dim-line" stroke="#FBBF24" stroke-width="1.0" />
    <line x1="162" y1="386" x2="162" y2="392" class="dim-tick" stroke="#FBBF24" stroke-width="1.2" />
    <line x1="377.5" y1="386" x2="377.5" y2="392" class="dim-tick" stroke="#FBBF24" stroke-width="1.2" />
    <text x="270" y="396" class="dim-text" fill="#FBBF24" font-weight="800" text-anchor="middle">남측 총 폭 = 21.55m (에르그 2.0m + 진입복도 1.5m + 코어 5.5m[탈의 3.4m·벽 0.1m·샤워 2.0m] = 깊이 9.0m)</text>

    <!-- Right-side Vertical Depth Dimensions for South Core (at x=383) -->
    <line x1="383" y1="278" x2="383" y2="298" class="dim-line" stroke="#A3E635" />
    <line x1="380" y1="278" x2="386" y2="278" class="dim-tick" stroke="#A3E635" />
    <line x1="380" y1="298" x2="386" y2="298" class="dim-tick" stroke="#A3E635" />
    <text x="388" y="290" class="dim-text" fill="#BEF264" text-anchor="start">에르그 2.0m</text>

    <line x1="383" y1="298" x2="383" y2="313" class="dim-line" stroke="#FBBF24" />
    <line x1="380" y1="313" x2="386" y2="313" class="dim-tick" stroke="#FBBF24" />
    <text x="388" y="307" class="dim-text" fill="#FDE68A" text-anchor="start">복도 1.5m</text>

    <line x1="383" y1="313" x2="383" y2="368" class="dim-line" stroke="#C084FC" />
    <line x1="380" y1="347.5" x2="385" y2="347.5" class="dim-tick" stroke="#C084FC" />
    <line x1="380" y1="368" x2="386" y2="368" class="dim-tick" stroke="#C084FC" />
    <text x="388" y="332" class="dim-text" fill="#E9D5FF" text-anchor="start">탈의실 3.4m</text>
    <text x="388" y="360" class="dim-text" fill="#E9D5FF" text-anchor="start">샤워실 2.0m</text>

    <!-- West Parking Direct Passage Dimension = 3.0m (at x=118, y=320~350) -->
    <line x1="118" y1="320" x2="118" y2="350" class="dim-line" stroke="#F59E0B" />
    <polygon points="118,320 116.5,323 119.5,323" fill="#F59E0B" />
    <polygon points="118,350 116.5,347 119.5,347" fill="#F59E0B" />
    <text x="132" y="356" class="dim-text" fill="#F59E0B" font-weight="800" text-anchor="middle">통로 3.0m</text>
  </g>

  <!-- ================= 13. WEST ENTRANCE & STORAGE ================= -->
  <g id="west-entry">
    <rect x="20" y="310" width="90" height="58" fill="#1E293B" stroke="#475569" stroke-width="1.0" rx="3" />
    <text x="65" y="336" font-size="6.0" font-weight="800" fill="#F8FAFC" text-anchor="middle">창고 · 코치실</text>
    <text x="65" y="345" font-size="4.2" font-weight="600" fill="#94A3B8" text-anchor="middle">(9평 · 비품/코치)</text>

    <!-- Flow Arrow from Parking -->
    <line x1="120" y1="334" x2="152" y2="334" stroke="#F59E0B" stroke-width="2.2" stroke-linecap="round" />
    <polygon points="154,334 146,330 146,338" fill="#F59E0B" />
    <text x="136" y="344" font-size="4.2" font-weight="800" fill="#F59E0B" text-anchor="middle">회원 입장 동선 ▶</text>
    <text x="65" y="380" font-size="4.2" font-weight="700" fill="#94A3B8">▼ 하역장 (중장비·리그 직결 반입)</text>
  </g>
</svg>'''
    return svg


if __name__ == '__main__':
    svg_content = generate_svg()
    with open('work/plan.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Master Plan V4.2 SVG written successfully! Size:", len(svg_content))
