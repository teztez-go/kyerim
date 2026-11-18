# -*- coding: utf-8 -*-

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" font-family="Pretendard, Apple SD Gothic Neo, Noto Sans KR, sans-serif">
  <defs>
    <!-- Gradients -->
    <linearGradient id="loungeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB" />
      <stop offset="100%" stop-color="#FEF3C7" />
    </linearGradient>
    <linearGradient id="metGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EEF2FF" />
      <stop offset="100%" stop-color="#E0E7FF" />
    </linearGradient>
    <linearGradient id="hybGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ECFDF5" />
      <stop offset="100%" stop-color="#D1FAE5" />
    </linearGradient>
    <linearGradient id="turfGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <linearGradient id="turfGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#10B981" />
    </linearGradient>
    <linearGradient id="lockerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0F9FF" />
      <stop offset="100%" stop-color="#E0F2FE" />
    </linearGradient>
    <linearGradient id="recovGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0FDFA" />
      <stop offset="100%" stop-color="#CCFBF1" />
    </linearGradient>

    <!-- Drop Shadows -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-opacity="0.08"/>
    </filter>
  </defs>

  <style>
    .grid-line { stroke: #CBD5E1; stroke-width: 0.7; stroke-dasharray: 4 3; }
    .grid-label { font-size: 9px; font-family: ui-monospace, monospace; font-weight: 700; fill: #64748B; }
    .ctx-area { fill: #F1F5F9; stroke: #CBD5E1; stroke-width: 0.8; }
    .outer-wall { fill: none; stroke: #0F172A; stroke-width: 2.8; stroke-linejoin: round; stroke-linecap: round; }
    .inner-wall { fill: none; stroke: #334155; stroke-width: 1.6; stroke-linejoin: round; }
    .partition { fill: none; stroke: #64748B; stroke-width: 1; stroke-dasharray: 3 2; }
    .col-rect { fill: #0F172A; stroke: #334155; stroke-width: 0.8; }
    
    .fire-shutter { stroke: #EF4444; stroke-width: 2.2; stroke-dasharray: 6 3; }
    .circulation { fill: #F8FAFC; stroke: #94A3B8; stroke-width: 1; stroke-dasharray: 4 2; }

    .zone-title { font-size: 11px; font-weight: 800; fill: #0F172A; }
    .zone-sub { font-size: 8.5px; font-weight: 600; fill: #475569; }
    .zone-tag { font-size: 7.5px; font-weight: 700; font-family: ui-monospace, monospace; }
    .item-label { font-size: 7.5px; font-weight: 600; fill: #334155; }
    .turf-label { font-size: 9px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.5px; }

    .door-arc { fill: none; stroke: #EA580C; stroke-width: 1.2; }
    .flow-arrow { fill: none; stroke: #EA580C; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
    .arrow-head { fill: #EA580C; }

    .platform { fill: #CBD5E1; stroke: #64748B; stroke-width: 0.8; rx: 1.5; }
    .rig-beam { stroke: #0F172A; stroke-width: 3.5; stroke-linecap: round; }
    .rig-post { fill: #0F172A; }
    .bench { fill: #E2E8F0; stroke: #94A3B8; stroke-width: 0.6; }
    .eq-rect { fill: #FFFFFF; stroke: #475569; stroke-width: 0.8; rx: 1; }
  </style>

  <!-- BACKGROUND GRID -->
  <g class="grid-layer">
    <!-- Vertical Grid Lines (Columns 3 to 7) -->
    <line x1="162" y1="10" x2="162" y2="390" class="grid-line" />
    <line x1="243" y1="10" x2="243" y2="390" class="grid-line" />
    <line x1="324" y1="10" x2="324" y2="390" class="grid-line" />
    <line x1="405" y1="10" x2="405" y2="390" class="grid-line" />
    <line x1="486" y1="10" x2="486" y2="390" class="grid-line" />

    <!-- Horizontal Grid Lines (Rows E to I) -->
    <line x1="15" y1="368" x2="525" y2="368" class="grid-line" />
    <line x1="15" y1="278" x2="525" y2="278" class="grid-line" />
    <line x1="15" y1="197" x2="525" y2="197" class="grid-line" />
    <line x1="15" y1="116" x2="525" y2="116" class="grid-line" />
    <line x1="15" y1="38" x2="525" y2="38" class="grid-line" />

    <!-- Grid Column Labels -->
    <text x="159" y="11" class="grid-label">3</text>
    <text x="240" y="11" class="grid-label">4</text>
    <text x="321" y="11" class="grid-label">5</text>
    <text x="402" y="11" class="grid-label">6</text>
    <text x="483" y="11" class="grid-label">7</text>

    <!-- Grid Row Labels -->
    <text x="6" y="365" class="grid-label">E</text>
    <text x="6" y="275" class="grid-label">F</text>
    <text x="6" y="194" class="grid-label">G</text>
    <text x="6" y="113" class="grid-label">H</text>
    <text x="6" y="35" class="grid-label">I</text>
  </g>

  <!-- EXTERNAL CONTEXT -->
  <g class="context-layer">
    <!-- Storage Office (통로 건너편 사무실 9평 창고) -->
    <rect x="15" y="305" width="48" height="63" class="ctx-area" rx="2" />
    <text x="39" y="333" class="item-label" text-anchor="middle" font-weight="700">창고·사무실</text>
    <text x="39" y="345" class="zone-tag" fill="#64748B" text-anchor="middle">9평 (비품)</text>

    <!-- Parking Connection Corridor (주차장 연결 통로) -->
    <rect x="63" y="312" width="99" height="56" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="0.8" stroke-dasharray="3 3" />
    <text x="112" y="335" class="item-label" text-anchor="middle" font-weight="700" fill="#0EA5E9">지하주차장 직결 통로</text>
    <text x="112" y="347" class="zone-tag" fill="#64748B" text-anchor="middle">폭 3.0m · 비 안 맞음</text>

    <!-- Entrance Flow Arrow -->
    <line x1="90" y1="355" x2="148" y2="355" class="flow-arrow" />
    <polygon points="146,351 156,355 146,359" class="arrow-head" />
    <text x="123" y="364" class="zone-tag" fill="#EA580C" text-anchor="middle">회원 진입 동선</text>

    <!-- AHU Room (공조실 - 기존 유지) -->
    <rect x="377.5" y="278" width="108.5" height="90" class="ctx-area" />
    <text x="432" y="320" class="item-label" font-weight="800" text-anchor="middle" fill="#475569">공조실 (A.H.U)</text>
    <text x="432" y="333" class="zone-tag" fill="#64748B" text-anchor="middle">건물 핵심 설비구역</text>

    <!-- Loading Dock (남측 하역장) -->
    <rect x="162" y="373" width="120" height="20" fill="#F8FAFC" stroke="#94A3B8" stroke-width="0.8" stroke-dasharray="2 2" rx="1" />
    <text x="222" y="386" class="zone-tag" fill="#475569" text-anchor="middle">▼ 하역장 (중장비·리그·고무블럭 반입 직결)</text>

    <!-- East Bowling Alley Context -->
    <text x="506" y="160" class="zone-tag" fill="#94A3B8" text-anchor="middle" transform="rotate(90 506 160)">볼링장 쪽 (통행 없음 · 비상구만 확보)</text>
  </g>

  <!-- PRIMARY FLOOR ZONES -->
  <g class="zones-layer" filter="url(#shadow)">
    <!-- HYB ZONE FLOOR (하이록스 구역 75평) -->
    <polygon points="162,260 486,75 486,19.4 127.5,229.8 162,278" fill="url(#hybGrad)" stroke="#10B981" stroke-width="1.2" />

    <!-- MET ZONE FLOOR (크로스핏 구역 85평) -->
    <polygon points="162,260 486,75 486,278 243,278 243,260" fill="url(#metGrad)" stroke="#6366F1" stroke-width="1.2" />

    <!-- CLEAN CIRCULATION WALKWAY (안전 보행로 2.5m) -->
    <rect x="238" y="258" width="248" height="20" class="circulation" />
    <text x="350" y="271" class="zone-tag" fill="#64748B" text-anchor="middle">클린 메인 보행로 (샤워실 ↔ 운동존 안전 완충대 · 폭 2.0m)</text>

    <!-- LOBBY & WELCOME LOUNGE (22평) -->
    <rect x="162" y="278" width="81" height="90" fill="url(#loungeGrad)" stroke="#F59E0B" stroke-width="1.4" />

    <!-- MEN LOCKER & SHOWER (남성 탈의·샤워 14평) -->
    <rect x="243" y="278" width="52" height="90" fill="url(#lockerGrad)" stroke="#0284C7" stroke-width="1.2" />

    <!-- WOMEN LOCKER & SHOWER (여성 탈의·샤워 16평) -->
    <rect x="295" y="278" width="57" height="90" fill="url(#lockerGrad)" stroke="#0284C7" stroke-width="1.2" />

    <!-- PHASE 2 RECOVERY SUITE (2단계 리커버리 스위트 7평 / 1단계 스트레칭 룸) -->
    <rect x="352" y="278" width="25.5" height="90" fill="url(#recovGrad)" stroke="#0D9488" stroke-width="1.2" />
  </g>

  <!-- 30M DUAL HYROX TURF RUNWAY (30m 듀얼 잔디 썰매 트랙) -->
  <g class="turf-runway-layer">
    <!-- Turf Base (30m x 3.2m Dual Lane) -->
    <!-- Transformed to match diagonal outer wall slope (dx=358.5, dy=-210.4 -> angle ~ -30.4 deg) -->
    <g transform="translate(178, 222) rotate(-30.4)">
      <!-- Lane 1 (Outer Sled Push Lane) -->
      <rect x="0" y="0" width="275" height="15" fill="url(#turfGrad)" stroke="#047857" stroke-width="0.8" rx="2" />
      <!-- Lane 2 (Inner Sled Pull & Lunges Lane) -->
      <rect x="0" y="16" width="275" height="15" fill="url(#turfGrad2)" stroke="#047857" stroke-width="0.8" rx="2" />

      <!-- Center Dashed Line -->
      <line x1="5" y1="15.5" x2="270" y2="15.5" stroke="#FFFFFF" stroke-width="1.2" stroke-dasharray="8 5" />

      <!-- Distance Markers -->
      <line x1="0" y1="0" x2="0" y2="31" stroke="#FFFFFF" stroke-width="2" />
      <text x="6" y="9" font-size="6.5" font-weight="800" fill="#FFFFFF" font-family="ui-monospace">START</text>
      
      <line x1="50" y1="0" x2="50" y2="31" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="2 2" />
      <text x="50" y="9" font-size="6" font-weight="700" fill="#E6FFFA" text-anchor="middle" font-family="ui-monospace">5m</text>

      <line x1="100" y1="0" x2="100" y2="31" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="2 2" />
      <text x="100" y="9" font-size="6" font-weight="700" fill="#E6FFFA" text-anchor="middle" font-family="ui-monospace">10m</text>

      <line x1="150" y1="0" x2="150" y2="31" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="2 2" />
      <text x="150" y="9" font-size="6" font-weight="700" fill="#E6FFFA" text-anchor="middle" font-family="ui-monospace">15m</text>

      <line x1="200" y1="0" x2="200" y2="31" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="2 2" />
      <text x="200" y="9" font-size="6" font-weight="700" fill="#E6FFFA" text-anchor="middle" font-family="ui-monospace">20m</text>

      <line x1="250" y1="0" x2="250" y2="31" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="2 2" />
      <text x="250" y="9" font-size="6" font-weight="700" fill="#E6FFFA" text-anchor="middle" font-family="ui-monospace">25m</text>

      <line x1="275" y1="0" x2="275" y2="31" stroke="#FFFFFF" stroke-width="2" />
      <text x="268" y="9" font-size="6.5" font-weight="800" fill="#FFFFFF" text-anchor="end" font-family="ui-monospace">30m FINISH</text>

      <!-- Turf Track Main Labels -->
      <text x="135" y="11" class="turf-label" text-anchor="middle">LANE 1 : SLED PUSH 썰매 밀기 30m</text>
      <text x="135" y="27" class="turf-label" text-anchor="middle">LANE 2 : SLED PULL &amp; LUNGES 썰매 당기기 30m</text>
    </g>

    <!-- Start / Finish Deceleration Safety Buffers -->
    <circle cx="170" cy="225" r="9" fill="#F59E0B" fill-opacity="0.2" stroke="#D97706" stroke-width="0.8" stroke-dasharray="2 2" />
    <text x="170" y="227.5" font-size="6" font-weight="800" fill="#B45309" text-anchor="middle">가감속 버퍼</text>

    <circle cx="422" cy="78" r="9" fill="#F59E0B" fill-opacity="0.2" stroke="#D97706" stroke-width="0.8" stroke-dasharray="2 2" />
    <text x="422" y="80.5" font-size="6" font-weight="800" fill="#B45309" text-anchor="middle">가감속 버퍼</text>
  </g>

  <!-- EQUIPMENT & STATIONS -->
  <g class="equipment-layer">
    <!-- 1. HYB ERG BATTERY LINE (Rowers & SkiErgs 10대) -->
    <!-- Concept2 Rowers (6대) -->
    <g transform="translate(245, 185) rotate(-30.4)">
      <rect x="0" y="0" width="22" height="6" class="eq-rect" /><text x="11" y="4.5" font-size="4.5" font-weight="700" fill="#1E293B" text-anchor="middle">ROW 1</text>
      <rect x="0" y="8" width="22" height="6" class="eq-rect" /><text x="11" y="12.5" font-size="4.5" font-weight="700" fill="#1E293B" text-anchor="middle">ROW 2</text>
      <rect x="0" y="16" width="22" height="6" class="eq-rect" /><text x="11" y="20.5" font-size="4.5" font-weight="700" fill="#1E293B" text-anchor="middle">ROW 3</text>
      <rect x="0" y="24" width="22" height="6" class="eq-rect" /><text x="11" y="28.5" font-size="4.5" font-weight="700" fill="#1E293B" text-anchor="middle">ROW 4</text>
      <rect x="0" y="32" width="22" height="6" class="eq-rect" /><text x="11" y="36.5" font-size="4.5" font-weight="700" fill="#1E293B" text-anchor="middle">ROW 5</text>
      <rect x="0" y="40" width="22" height="6" class="eq-rect" /><text x="11" y="44.5" font-size="4.5" font-weight="700" fill="#1E293B" text-anchor="middle">ROW 6</text>
      <text x="11" y="55" font-size="6.5" font-weight="800" fill="#047857" text-anchor="middle">컨셉2 로잉 배터리 6대</text>
    </g>

    <!-- SkiErgs (4대) mounted on diagonal perimeter posts -->
    <g transform="translate(355, 120) rotate(-30.4)">
      <rect x="0" y="0" width="10" height="8" class="eq-rect" fill="#E2E8F0"/><text x="5" y="6" font-size="4.5" font-weight="700" fill="#0F172A" text-anchor="middle">SKI 1</text>
      <rect x="14" y="0" width="10" height="8" class="eq-rect" fill="#E2E8F0"/><text x="19" y="6" font-size="4.5" font-weight="700" fill="#0F172A" text-anchor="middle">SKI 2</text>
      <rect x="28" y="0" width="10" height="8" class="eq-rect" fill="#E2E8F0"/><text x="33" y="6" font-size="4.5" font-weight="700" fill="#0F172A" text-anchor="middle">SKI 3</text>
      <rect x="42" y="0" width="10" height="8" class="eq-rect" fill="#E2E8F0"/><text x="47" y="6" font-size="4.5" font-weight="700" fill="#0F172A" text-anchor="middle">SKI 4</text>
      <text x="26" y="16" font-size="6" font-weight="800" fill="#047857" text-anchor="middle">스키에르그 스테이션 4대</text>
    </g>

    <!-- Curved Treadmills & Echo Bikes (무동력 트레드밀 & 바이크 8대) -->
    <g transform="translate(168, 235)">
      <rect x="0" y="0" width="14" height="7" class="eq-rect" /><text x="7" y="5" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">RUN 1</text>
      <rect x="16" y="0" width="14" height="7" class="eq-rect" /><text x="23" y="5" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">RUN 2</text>
      <rect x="32" y="0" width="14" height="7" class="eq-rect" /><text x="39" y="5" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">RUN 3</text>
      <rect x="48" y="0" width="14" height="7" class="eq-rect" /><text x="55" y="5" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">RUN 4</text>
      
      <rect x="0" y="10" width="14" height="7" class="eq-rect" /><text x="7" y="15" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">BIKE 1</text>
      <rect x="16" y="10" width="14" height="7" class="eq-rect" /><text x="23" y="15" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">BIKE 2</text>
      <rect x="32" y="10" width="14" height="7" class="eq-rect" /><text x="39" y="15" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">BIKE 3</text>
      <rect x="48" y="10" width="14" height="7" class="eq-rect" /><text x="55" y="15" font-size="4" font-weight="700" fill="#334155" text-anchor="middle">BIKE 4</text>
      <text x="31" y="24" font-size="5.5" font-weight="700" fill="#047857" text-anchor="middle">무동력 러너 &amp; 에코바이크 8대</text>
    </g>

    <!-- Wall Ball Targets (월볼 타겟 8개소) along North-East wall -->
    <g transform="translate(442, 28)">
      <line x1="0" y1="0" x2="42" y2="0" stroke="#0F172A" stroke-width="3" />
      <circle cx="6" cy="3" r="2.5" fill="#EF4444" /><text x="6" y="10" font-size="4" font-weight="700" fill="#0F172A" text-anchor="middle">10ft</text>
      <circle cx="16" cy="3" r="2.5" fill="#EF4444" /><text x="16" y="10" font-size="4" font-weight="700" fill="#0F172A" text-anchor="middle">9ft</text>
      <circle cx="26" cy="3" r="2.5" fill="#EF4444" /><text x="26" y="10" font-size="4" font-weight="700" fill="#0F172A" text-anchor="middle">10ft</text>
      <circle cx="36" cy="3" r="2.5" fill="#EF4444" /><text x="36" y="10" font-size="4" font-weight="700" fill="#0F172A" text-anchor="middle">9ft</text>
      <text x="21" y="18" font-size="5.5" font-weight="800" fill="#EF4444" text-anchor="middle">공식 월볼 존 (8 타겟)</text>
    </g>

    <!-- 2. MET ZONE : 12 OLYMPIC LIFTING PLATFORMS (역도 & 크로스핏 플랫폼 12개소) -->
    <g class="platforms-group">
      <!-- Front Row (6 platforms) -->
      <g transform="translate(252, 222)">
        <rect x="0" y="0" width="30" height="26" class="platform" /><line x1="3" y1="13" x2="27" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="5" cy="13" r="2.2" fill="#0F172A"/><circle cx="25" cy="13" r="2.2" fill="#0F172A"/><text x="15" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 01</text>
        <rect x="36" y="0" width="30" height="26" class="platform" /><line x1="39" y1="13" x2="63" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="41" cy="13" r="2.2" fill="#0F172A"/><circle cx="61" cy="13" r="2.2" fill="#0F172A"/><text x="51" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 02</text>
        <rect x="72" y="0" width="30" height="26" class="platform" /><line x1="75" y1="13" x2="99" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="77" cy="13" r="2.2" fill="#0F172A"/><circle cx="97" cy="13" r="2.2" fill="#0F172A"/><text x="87" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 03</text>
        <rect x="108" y="0" width="30" height="26" class="platform" /><line x1="111" y1="13" x2="135" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="113" cy="13" r="2.2" fill="#0F172A"/><circle cx="133" cy="13" r="2.2" fill="#0F172A"/><text x="123" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 04</text>
        <rect x="144" y="0" width="30" height="26" class="platform" /><line x1="147" y1="13" x2="171" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="149" cy="13" r="2.2" fill="#0F172A"/><circle cx="169" cy="13" r="2.2" fill="#0F172A"/><text x="159" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 05</text>
        <rect x="180" y="0" width="30" height="26" class="platform" /><line x1="183" y1="13" x2="207" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="185" cy="13" r="2.2" fill="#0F172A"/><circle cx="205" cy="13" r="2.2" fill="#0F172A"/><text x="195" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 06</text>
      </g>

      <!-- Back Row (6 platforms) -->
      <g transform="translate(252, 178)">
        <rect x="0" y="0" width="30" height="26" class="platform" /><line x1="3" y1="13" x2="27" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="5" cy="13" r="2.2" fill="#0F172A"/><circle cx="25" cy="13" r="2.2" fill="#0F172A"/><text x="15" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 07</text>
        <rect x="36" y="0" width="30" height="26" class="platform" /><line x1="39" y1="13" x2="63" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="41" cy="13" r="2.2" fill="#0F172A"/><circle cx="61" cy="13" r="2.2" fill="#0F172A"/><text x="51" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 08</text>
        <rect x="72" y="0" width="30" height="26" class="platform" /><line x1="75" y1="13" x2="99" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="77" cy="13" r="2.2" fill="#0F172A"/><circle cx="97" cy="13" r="2.2" fill="#0F172A"/><text x="87" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 09</text>
        <rect x="108" y="0" width="30" height="26" class="platform" /><line x1="111" y1="13" x2="135" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="113" cy="13" r="2.2" fill="#0F172A"/><circle cx="133" cy="13" r="2.2" fill="#0F172A"/><text x="123" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 10</text>
        <rect x="144" y="0" width="30" height="26" class="platform" /><line x1="147" y1="13" x2="171" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="149" cy="13" r="2.2" fill="#0F172A"/><circle cx="169" cy="13" r="2.2" fill="#0F172A"/><text x="159" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 11</text>
        <rect x="180" y="0" width="30" height="26" class="platform" /><line x1="183" y1="13" x2="207" y2="13" stroke="#0F172A" stroke-width="1.8"/><circle cx="185" cy="13" r="2.2" fill="#0F172A"/><circle cx="205" cy="13" r="2.2" fill="#0F172A"/><text x="195" y="22" font-size="5" font-weight="700" fill="#475569" text-anchor="middle">PLAT 12</text>
      </g>
    </g>

    <!-- 3. MODULAR STRUCTURAL RIG (Row G 축 정렬 모듈형 리그 21m) -->
    <!-- Runs along Row G (y=156) between Col 4 (243) and Col 6 (405) plus extension -->
    <g class="rig-system">
      <line x1="250" y1="156" x2="435" y2="156" class="rig-beam" />
      <!-- Rig Uprights / Squat Cells -->
      <circle cx="255" cy="156" r="3.2" class="rig-post" />
      <circle cx="275" cy="156" r="2.5" class="rig-post" />
      <circle cx="295" cy="156" r="3.2" class="rig-post" />
      <circle cx="315" cy="156" r="2.5" class="rig-post" />
      <circle cx="335" cy="156" r="3.2" class="rig-post" />
      <circle cx="355" cy="156" r="2.5" class="rig-post" />
      <circle cx="375" cy="156" r="3.2" class="rig-post" />
      <circle cx="395" cy="156" r="2.5" class="rig-post" />
      <circle cx="415" cy="156" r="3.2" class="rig-post" />
      <circle cx="435" cy="156" r="2.5" class="rig-post" />
      
      <!-- Pull-up bars connectors & Gymnastics Rings -->
      <line x1="265" y1="150" x2="265" y2="162" stroke="#0F172A" stroke-width="1.2" />
      <line x1="305" y1="150" x2="305" y2="162" stroke="#0F172A" stroke-width="1.2" />
      <line x1="345" y1="150" x2="345" y2="162" stroke="#0F172A" stroke-width="1.2" />
      <line x1="385" y1="150" x2="385" y2="162" stroke="#0F172A" stroke-width="1.2" />
      <line x1="425" y1="150" x2="425" y2="162" stroke="#0F172A" stroke-width="1.2" />

      <circle cx="345" cy="147" r="1.8" fill="none" stroke="#EA580C" stroke-width="0.9" />
      <circle cx="385" cy="147" r="1.8" fill="none" stroke="#EA580C" stroke-width="0.9" />

      <text x="345" y="141" font-size="7.5" font-weight="800" fill="#0F172A" text-anchor="middle">모듈형 구조 일체형 커스텀 리그 (21m · 풀업 14스테이션 + 스쿼트 10셀)</text>
    </g>

    <!-- 4. COACH COMMAND & MOBILITY HUB (중앙 코칭 센터 & 타이머) -->
    <g transform="translate(310, 162)">
      <!-- 3-Way Overhead LED Timer -->
      <polygon points="14,0 24,14 4,14" fill="#EA580C" stroke="#C2410C" stroke-width="0.8" />
      <text x="14" y="10" font-size="5" font-weight="900" fill="#FFFFFF" text-anchor="middle">360°</text>
      <text x="14" y="24" font-size="6" font-weight="800" fill="#C2410C" text-anchor="middle">3면 디지털 타이머</text>
      <!-- Coach Pod / Whiteboard -->
      <rect x="0" y="27" width="28" height="5" fill="#0F172A" rx="1"/>
      <text x="14" y="31" font-size="4" font-weight="700" fill="#FFFFFF" text-anchor="middle">COACH PODIUM</text>
    </g>

    <!-- 5. EAST EQUIPMENT STORAGE & DUMBBELL WALL (덤벨·원판 랙 14m) -->
    <g transform="translate(470, 115)">
      <rect x="0" y="0" width="12" height="155" fill="#334155" stroke="#0F172A" stroke-width="0.8" rx="1.5" />
      <text x="6" y="80" font-size="7" font-weight="800" fill="#FFFFFF" text-anchor="middle" transform="rotate(90 6 80)">덤벨·케틀벨·바벨 원판 전문 수납랙 (14m)</text>
    </g>
  </g>

  <!-- LOBBY & WET CORE INTERNAL DETAILS -->
  <g class="amenities-detail-layer">
    <!-- Lobby Reception & InBody Consultation Desk -->
    <rect x="172" y="284" width="32" height="12" fill="#FFFFFF" stroke="#D97706" stroke-width="1" rx="2" />
    <text x="188" y="292.5" font-size="5.5" font-weight="800" fill="#B45309" text-anchor="middle">인포데스크 / 인바디</text>

    <!-- Street Shoe Locker & Benches -->
    <rect x="165" y="310" width="8" height="42" class="bench" />
    <text x="169" y="333" font-size="5" font-weight="700" fill="#64748B" text-anchor="middle" transform="rotate(90 169 333)">신발장 &amp; 벤치</text>

    <!-- Community Bar & Protein Shake Island -->
    <rect x="195" y="320" width="40" height="16" fill="#FFFFFF" stroke="#D97706" stroke-width="1" rx="2" />
    <circle cx="203" cy="328" r="3" fill="#FEF3C7" stroke="#F59E0B" stroke-width="0.6"/>
    <circle cx="215" cy="328" r="3" fill="#FEF3C7" stroke="#F59E0B" stroke-width="0.6"/>
    <circle cx="227" cy="328" r="3" fill="#FEF3C7" stroke="#F59E0B" stroke-width="0.6"/>
    <text x="215" y="331" font-size="5.5" font-weight="800" fill="#92400E" text-anchor="middle">프로틴 라운지</text>

    <!-- Men Locker & Shower Details -->
    <!-- Men Dry Vanity -->
    <rect x="248" y="284" width="42" height="6" fill="#FFFFFF" stroke="#0284C7" stroke-width="0.6" />
    <text x="269" y="289" font-size="4.5" font-weight="700" fill="#0369A1" text-anchor="middle">남성 파우더 / 락커 40개</text>
    <!-- Men Wet Showers (6 stalls) -->
    <line x1="243" y1="330" x2="295" y2="330" stroke="#0284C7" stroke-width="0.8" stroke-dasharray="2 2" />
    <rect x="246" y="335" width="7" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="254" y="335" width="7" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="262" y="335" width="7" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="270" y="335" width="7" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="278" y="335" width="7" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="286" y="335" width="7" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <text x="269" y="358" font-size="5.5" font-weight="800" fill="#0369A1" text-anchor="middle">개별 샤워 6부스 (남)</text>

    <!-- Women Locker & Shower Details -->
    <!-- Women Dry Vanity & Powder -->
    <rect x="300" y="284" width="47" height="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="0.6" />
    <text x="323.5" y="290" font-size="4.5" font-weight="700" fill="#0369A1" text-anchor="middle">여성 프리미엄 파우더 / 락커 50개</text>
    <!-- Women Wet Showers (8 stalls) -->
    <line x1="295" y1="330" x2="352" y2="330" stroke="#0284C7" stroke-width="0.8" stroke-dasharray="2 2" />
    <rect x="298" y="335" width="6" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="305" y="335" width="6" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="312" y="335" width="6" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="319" y="335" width="6" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="326" y="335" width="6" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="333" y="335" width="6" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="340" y="335" width="6" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <rect x="346" y="335" width="5" height="10" fill="#BAE6FD" stroke="#0284C7" stroke-width="0.6" rx="1"/>
    <text x="323.5" y="358" font-size="5.5" font-weight="800" fill="#0369A1" text-anchor="middle">개별 샤워 8부스 (여)</text>

    <!-- Phase 2 Recovery Suite (1단계: 스트레칭룸 -> 2단계: 냉수욕&사우나) -->
    <rect x="355" y="300" width="20" height="24" fill="#99F6E4" stroke="#0D9488" stroke-width="0.8" rx="2"/>
    <text x="365" y="311" font-size="4.5" font-weight="800" fill="#0F766E" text-anchor="middle">건식 사우나</text>
    <text x="365" y="319" font-size="4" font-weight="700" fill="#0F766E" text-anchor="middle">(2단계 모듈)</text>
    <rect x="355" y="330" width="20" height="18" fill="#5EEAD4" stroke="#0D9488" stroke-width="0.8" rx="2"/>
    <text x="365" y="340" font-size="4.5" font-weight="800" fill="#0F766E" text-anchor="middle">칠러 냉수욕</text>
    <text x="365" y="348" font-size="4" font-weight="700" fill="#0F766E" text-anchor="middle">(Ice Plunge)</text>
    <text x="365" y="362" font-size="4.5" font-weight="700" fill="#0F766E" text-anchor="middle">1단계: 스트레칭</text>
  </g>

  <!-- WALLS, COLUMNS & OPENINGS -->
  <g class="structure-layer">
    <!-- Perimeter Outer Building Walls -->
    <polygon points="162,368 377.5,368 377.5,278 486,278 486,19.4 127.5,229.8 162,278" class="outer-wall" />

    <!-- Interior Dividing Walls for Lobby & Wet Core -->
    <line x1="162" y1="278" x2="162" y2="368" class="inner-wall" />
    <line x1="243" y1="278" x2="243" y2="368" class="inner-wall" />
    <line x1="295" y1="278" x2="295" y2="368" class="inner-wall" />
    <line x1="352" y1="278" x2="352" y2="368" class="inner-wall" />
    <line x1="377.5" y1="278" x2="377.5" y2="368" class="inner-wall" />
    <line x1="162" y1="278" x2="377.5" y2="278" class="inner-wall" />

    <!-- Structural Columns (8.1m Grid) -->
    <!-- Row F (y=278) -->
    <rect x="158" y="274" width="8" height="8" class="col-rect" />
    <rect x="239" y="274" width="8" height="8" class="col-rect" />
    <rect x="320" y="274" width="8" height="8" class="col-rect" />
    <rect x="401" y="274" width="8" height="8" class="col-rect" />
    <rect x="482" y="274" width="8" height="8" class="col-rect" />

    <!-- Row E (y=368) -->
    <rect x="158" y="364" width="8" height="8" class="col-rect" />
    <rect x="239" y="364" width="8" height="8" class="col-rect" />
    <rect x="320" y="364" width="8" height="8" class="col-rect" />
    
    <!-- Row G (y=197) -->
    <rect x="239" y="193" width="8" height="8" class="col-rect" />
    <rect x="320" y="193" width="8" height="8" class="col-rect" />
    <rect x="401" y="193" width="8" height="8" class="col-rect" />
    <rect x="482" y="193" width="8" height="8" class="col-rect" />

    <!-- Row H (y=116) -->
    <rect x="320" y="112" width="8" height="8" class="col-rect" />
    <rect x="401" y="112" width="8" height="8" class="col-rect" />
    <rect x="482" y="112" width="8" height="8" class="col-rect" />

    <!-- Row I (y=38) -->
    <rect x="482" y="34" width="8" height="8" class="col-rect" />

    <!-- Fire Shutter Line (Col 4, y=162 to 278) -->
    <line x1="243" y1="274" x2="243" y2="162" class="fire-shutter" />
    <text x="247" y="210" font-size="7" font-weight="800" fill="#EF4444" transform="rotate(90 247 210)">법정 방화셔터선 (하부 통로 100% 개방)</text>

    <!-- DOORS & OPENINGS -->
    <!-- Main Entrance Door from Corridor (x=162, y=325 to 345) -->
    <line x1="162" y1="326" x2="162" y2="348" stroke="#FFFFFF" stroke-width="3" />
    <path d="M162 326 A22 22 0 0 1 184 348" class="door-arc" />
    <line x1="162" y1="348" x2="184" y2="348" stroke="#EA580C" stroke-width="1.2" />
    <text x="148" y="322" font-size="6.5" font-weight="800" fill="#EA580C" text-anchor="middle">메인 출입문</text>

    <!-- Glass Transition Door from Lobby to Arena (x=243, y=284 to 300) -->
    <line x1="243" y1="284" x2="243" y2="300" stroke="#FFFFFF" stroke-width="3" />
    <path d="M243 284 A16 16 0 0 1 259 300" class="door-arc" stroke="#0284C7" />

    <!-- Men Locker Door (x=258, y=278) -->
    <line x1="258" y1="278" x2="272" y2="278" stroke="#FFFFFF" stroke-width="3" />
    <path d="M258 278 A14 14 0 0 0 272 292" class="door-arc" stroke="#0284C7" />

    <!-- Women Locker Door (x=310, y=278) -->
    <line x1="310" y1="278" x2="324" y2="278" stroke="#FFFFFF" stroke-width="3" />
    <path d="M324 278 A14 14 0 0 1 310 292" class="door-arc" stroke="#0284C7" />

    <!-- Recovery Suite Door (x=358, y=278) -->
    <line x1="358" y1="278" x2="370" y2="278" stroke="#FFFFFF" stroke-width="3" />
    <path d="M370 278 A12 12 0 0 1 358 290" class="door-arc" stroke="#0D9488" />
  </g>

  <!-- LABELS & CALLOUT BADGES -->
  <g class="labels-layer">
    <!-- ZONE 1: WELCOME LOUNGE -->
    <text x="202" y="306" class="zone-title" text-anchor="middle">웰컴 라운지 &amp; 카페</text>
    <text x="202" y="316" class="zone-sub" text-anchor="middle">리셉션 · 인바디 · 22평</text>

    <!-- ZONE 2: MET ZONE -->
    <g transform="translate(370, 240)">
      <rect x="-65" y="-14" width="130" height="24" fill="#FFFFFF" fill-opacity="0.9" stroke="#6366F1" stroke-width="1" rx="4" filter="url(#shadow)"/>
      <text x="0" y="-1" class="zone-title" fill="#4338CA" text-anchor="middle">MET ZONE · 정통 크로스핏 아레나</text>
      <text x="0" y="8" class="zone-sub" fill="#6366F1" text-anchor="middle">85평 · 50T 방진 바닥 · 올림픽 역도 12스테이션</text>
    </g>

    <!-- ZONE 3: HYB ZONE -->
    <g transform="translate(330, 68)">
      <rect x="-65" y="-14" width="130" height="24" fill="#FFFFFF" fill-opacity="0.9" stroke="#10B981" stroke-width="1" rx="4" filter="url(#shadow)"/>
      <text x="0" y="-1" class="zone-title" fill="#065F46" text-anchor="middle">HYB ZONE · 하이록스 레이스 센터</text>
      <text x="0" y="8" class="zone-sub" fill="#047857" text-anchor="middle">75평 · 30m 듀얼 런웨이 · 에르그 10대 · 월볼 8구역</text>
    </g>

    <!-- Scale Dimension Bar -->
    <g transform="translate(140, 24)">
      <line x1="0" y1="0" x2="81" y2="0" stroke="#0F172A" stroke-width="1.8" />
      <line x1="0" y1="-3" x2="0" y2="3" stroke="#0F172A" stroke-width="1.8" />
      <line x1="81" y1="-3" x2="81" y2="3" stroke="#0F172A" stroke-width="1.8" />
      <text x="40.5" y="-5" font-size="7.5" font-weight="700" fill="#0F172A" text-anchor="middle" font-family="ui-monospace">1 SPAN = 8.1m</text>
    </g>
  </g>
</svg>
'''

with open('work/plan.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved work/plan.svg successfully! Bytes:", len(svg))
