# -*- coding: utf-8 -*-
import re

with open('kyerim-internal.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Extract the SVG plan section exactly as is
svg_match = re.search(r'(<div class="plan">.*?</div>)', orig, re.DOTALL)
if not svg_match:
    raise ValueError("SVG plan not found in kyerim-internal.html")
plan_svg_html = svg_match.group(1)

new_html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>계림 판단 노트 — 소유자 전액투자·위탁운영</title>
<style>
:root{{
  --paper:#F4F5F3; --panel:#FFFFFF; --ink:#1E2227; --ink2:#47505A; --ink3:#77808A;
  --rule:#D6DADE; --rule2:#E8EBED;
  --marker:rgba(255,168,46,.42); --accent:#B9530A; --accent-soft:#FFF0DD;
  --go:#256E44; --go-bg:#E3F1E8; --warn:#8A5D00; --warn-bg:#FAF0D7; --stop:#A93434; --stop-bg:#F7E2E2;
  --z-rig:#DCE6EE; --z-turf:#D5E8C8; --z-sled:#A8CE91; --z-lobby:#F3D6B3; --z-lock:#E1E7EB; --z-hyb:#CFE5C2; --z-met:#D7DEF0; --z-dry:#EEF1F3; --rigc:#7C8794; --z-rec:#C9E6E8;
  --z-ctx:#ECEEF0; --z-ctxline:#AAB2BA;
  --chart-a:#2F6F9F; --chart-b:#B9530A; --chart-grid:#E3E6E9;
  --sans:"Pretendard","Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",system-ui,sans-serif;
  --mono:"SF Mono",ui-monospace,Menlo,Consolas,monospace;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    --paper:#131518; --panel:#1A1D21; --ink:#E6E8EB; --ink2:#B0B7BF; --ink3:#858E97;
    --rule:#2D3238; --rule2:#23272C;
    --marker:rgba(255,168,46,.30); --accent:#FFB05A; --accent-soft:#2A2016;
    --go:#72CC98; --go-bg:#15271D; --warn:#EFC15A; --warn-bg:#29230F; --stop:#EE8B8B; --stop-bg:#2B1717;
    --z-rig:#243240; --z-turf:#22351C; --z-sled:#365A2C; --z-lobby:#463220; --z-lock:#283037; --z-hyb:#22351C; --z-met:#232B44; --z-dry:#22272C; --rigc:#A7B0BA; --z-rec:#1D3A3D;
    --z-ctx:#1D2024; --z-ctxline:#4B525A;
    --chart-a:#79B3E0; --chart-b:#FFB05A; --chart-grid:#2A2F35;
  }}
}}
:root[data-theme="dark"]{{
  --paper:#131518; --panel:#1A1D21; --ink:#E6E8EB; --ink2:#B0B7BF; --ink3:#858E97;
  --rule:#2D3238; --rule2:#23272C;
  --marker:rgba(255,168,46,.30); --accent:#FFB05A; --accent-soft:#2A2016;
  --go:#72CC98; --go-bg:#15271D; --warn:#EFC15A; --warn-bg:#29230F; --stop:#EE8B8B; --stop-bg:#2B1717;
  --z-rig:#243240; --z-turf:#22351C; --z-sled:#365A2C; --z-lobby:#463220; --z-lock:#283037; --z-hyb:#22351C; --z-met:#232B44; --z-dry:#22272C; --rigc:#A7B0BA; --z-rec:#1D3A3D;
  --z-ctx:#1D2024; --z-ctxline:#4B525A;
  --chart-a:#79B3E0; --chart-b:#FFB05A; --chart-grid:#2A2F35;
}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.72;-webkit-font-smoothing:antialiased;word-break:keep-all;overflow-wrap:anywhere}}
.wrap{{max-width:1040px;margin:0 auto;padding:36px 16px 96px}}
.prose{{max-width:700px}}
a{{color:inherit}}
:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
h1,h2,h3{{text-wrap:balance;line-height:1.3;margin:0}}
h1{{font-size:clamp(28px,5vw,40px);font-weight:800;letter-spacing:-.02em}}
h2{{font-size:24px;font-weight:800;letter-spacing:-.01em}}
h3{{font-size:17px;font-weight:700}}
p{{margin:0}}
.hl{{background:linear-gradient(transparent 52%,var(--marker) 52%,var(--marker) 92%,transparent 92%);padding:0 .08em}}
.eyebrow{{font:600 12px/1.4 var(--mono);letter-spacing:.08em;color:var(--accent);text-transform:uppercase}}
.muted{{color:var(--ink2)}}
.small{{font-size:14px}}
.num{{font-variant-numeric:tabular-nums}}

.top{{display:grid;gap:14px;padding-bottom:28px;border-bottom:2px solid var(--ink)}}
.top .meta{{display:flex;flex-wrap:wrap;gap:8px 16px;font:500 13px/1.5 var(--mono);color:var(--ink3)}}
.warnline{{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:700;color:var(--stop);background:var(--stop-bg);padding:6px 12px;border-radius:4px;width:fit-content}}
nav.toc{{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:14px;padding:16px 0 0}}
nav.toc a{{text-decoration:none;color:var(--ink2);border-bottom:1px solid var(--rule)}}
nav.toc a:hover{{color:var(--ink);border-color:var(--ink)}}

section{{padding:48px 0 0;display:grid;gap:18px}}
section > header{{display:grid;gap:6px}}

.verdict{{background:var(--panel);border:1px solid var(--rule);border-left:6px solid var(--accent);padding:22px 22px 24px;display:grid;gap:16px;border-radius:2px}}
.chip{{display:inline-block;font:700 12px/1 var(--sans);padding:6px 10px;border-radius:999px;letter-spacing:.02em}}
.chip.go{{color:var(--go);background:var(--go-bg)}}
.chip.warn{{color:var(--warn);background:var(--warn-bg)}}
.chip.stop{{color:var(--stop);background:var(--stop-bg)}}
.facts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}}
.fact{{border-top:1px solid var(--rule);padding-top:10px;display:grid;gap:2px}}
.fact .k{{font-size:13px;color:var(--ink3)}}
.fact .v{{font-size:28px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums}}
.fact .n{{font-size:13px;color:var(--ink2)}}

.cols3{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}}
.card{{background:var(--panel);border:1px solid var(--rule);padding:18px;display:grid;gap:12px;align-content:start;border-radius:2px}}
.card h3{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.card ol,.card ul{{margin:0;padding-left:20px;display:grid;gap:10px}}
.card li > b{{display:block}}
.card li > span{{color:var(--ink2);font-size:14px}}
.card p{{font-size:14.5px;color:var(--ink2)}}
.bar-go{{border-top:4px solid var(--go)}} .bar-warn{{border-top:4px solid var(--warn)}} .bar-stop{{border-top:4px solid var(--stop)}}
.card li > b .fixed{{font:700 11px/1 var(--sans);color:var(--go);background:var(--go-bg);padding:3px 7px;border-radius:999px;margin-left:6px;vertical-align:2px}}

.tbl{{overflow-x:auto;background:var(--panel);border:1px solid var(--rule);border-radius:2px}}
table{{border-collapse:collapse;width:100%;min-width:640px;font-size:14.5px}}
th,td{{text-align:left;vertical-align:top;padding:12px 14px;border-bottom:1px solid var(--rule2)}}
thead th{{font-size:13px;color:var(--ink3);font-weight:600;background:var(--paper);border-bottom:1px solid var(--rule)}}
tbody tr:last-child td{{border-bottom:0}}
.rec{{background:var(--accent-soft)}}

.calc{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:16px;align-items:start}}
@media (max-width:820px){{.calc{{grid-template-columns:1fr}}}}
.panel{{background:var(--panel);border:1px solid var(--rule);padding:18px;border-radius:2px;display:grid;gap:18px}}
.scen{{display:flex;flex-wrap:wrap;gap:8px}}
.scen button{{font:600 14px var(--sans);padding:8px 14px;border:1px solid var(--rule);background:var(--paper);color:var(--ink);border-radius:999px;cursor:pointer}}
.scen button[aria-pressed="true"]{{background:var(--ink);color:var(--paper);border-color:var(--ink)}}
fieldset{{border:0;margin:0;padding:0;display:grid;gap:14px}}
legend{{font:700 13px var(--sans);color:var(--ink3);padding:0 0 4px;letter-spacing:.02em}}
.ctl{{display:grid;gap:4px}}
.ctl .lab{{display:flex;justify-content:space-between;gap:10px;font-size:14.5px}}
.ctl .lab output{{font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap}}
.ctl .hint{{font-size:12.5px;color:var(--ink3);line-height:1.5}}
input[type=range]{{width:100%;accent-color:var(--accent);height:24px;margin:0}}
.chk{{display:flex;gap:10px;align-items:flex-start;font-size:14.5px}}
.chk input{{width:18px;height:18px;margin-top:3px;accent-color:var(--accent)}}
.out{{display:grid;gap:14px}}
.month{{display:grid;grid-template-columns:1fr auto;gap:6px 12px;font-size:15px;font-variant-numeric:tabular-nums}}
.month .t{{color:var(--ink2)}}
.month .v{{text-align:right;font-weight:600}}
.month .sum{{border-top:1px solid var(--rule);padding-top:6px;font-weight:800}}
.month .cmp{{font-size:13px;color:var(--ink3);grid-column:1 / -1;text-align:right;margin-top:-4px}}
.big3{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}}
@media (max-width:480px){{.big3{{grid-template-columns:1fr}}}}
.big4{{grid-template-columns:repeat(2,minmax(0,1fr))}}
.big3 > div{{border-top:1px solid var(--rule);padding-top:8px}}
.big3 .k{{font-size:12.5px;color:var(--ink3)}}
.big3 .v{{font-size:22px;font-weight:800;letter-spacing:-.01em;font-variant-numeric:tabular-nums}}
.big3 .v.bad{{color:var(--stop)}}
.big3 .n{{font-size:12px;color:var(--ink3);line-height:1.4}}

.charts{{display:grid;gap:14px}}
.chartbox{{background:var(--paper);border:1px solid var(--rule);padding:14px;border-radius:2px;display:grid;gap:8px}}
.chartbox h4{{font-size:13.5px;margin:0;font-weight:700}}
.chartbox svg{{width:100%;height:auto;display:block}}
.chartbox .legend{{display:flex;flex-wrap:wrap;gap:12px;font-size:12.5px;color:var(--ink2)}}
.chartbox .legend span{{display:flex;align-items:center;gap:6px}}
.chartbox .legend i{{display:inline-block;width:12px;height:4px;border-radius:2px}}
.notes{{font-size:13.5px;color:var(--ink3);display:grid;gap:4px;margin:0;padding-left:18px}}

/* Chart SVGs */
svg .g{{stroke:var(--chart-grid);stroke-width:1}}
svg .ax{{fill:var(--ink3);font:500 11px var(--mono)}}
svg .fa{{fill:var(--chart-a);fill-opacity:.18}}
svg .la{{stroke:var(--chart-a);stroke-width:2.2;fill:none}}
svg .fb{{fill:var(--chart-b);fill-opacity:.18}}
svg .lb{{stroke:var(--chart-b);stroke-width:2.2;fill:none}}
svg .zero{{stroke:var(--ink);stroke-width:1;stroke-dasharray:3 3;opacity:.6}}
svg .ref{{stroke:var(--ink3);stroke-width:1.2;stroke-dasharray:4 4}}
svg .reflab{{fill:var(--ink3);font:600 11px var(--sans)}}
svg .dota{{fill:var(--chart-a)}}

/* Plan SVG */
.plan{{background:var(--paper);border:1px solid var(--rule);padding:14px;border-radius:2px;overflow:hidden}}
.plan svg{{width:100%;height:auto;display:block}}
.plan .grid line{{stroke:var(--rule2);stroke-width:1}}
.plan .glab text{{fill:var(--ink3);font:600 11px var(--mono);text-anchor:middle}}
.plan .col{{fill:var(--ink);opacity:.85}}
.plan .ext{{stroke:var(--ink);stroke-width:2}}
.plan .z-hyb{{fill:var(--z-hyb)}}
.plan .z-met{{fill:var(--z-met)}}
.plan .z-turf{{fill:var(--z-turf)}}
.plan .z-sled{{fill:var(--z-sled)}}
.plan .z-rig{{fill:var(--z-rig)}}
.plan .z-lobby{{fill:var(--z-lobby)}}
.plan .z-lock{{fill:var(--z-lock)}}
.plan .z-dry{{fill:var(--z-dry)}}
.plan .z-rec{{fill:var(--z-rec)}}
.plan .z-ctx{{fill:var(--z-ctx)}}
.plan .rigline{{stroke:var(--rigc);stroke-width:3;stroke-dasharray:6 3}}
.plan .zlabel{{font:700 13px var(--sans);fill:var(--ink)}}
.plan .zsub{{font:500 11px var(--sans);fill:var(--ink2)}}
.plan .ctxlab{{font:500 11.5px var(--sans);fill:var(--ink3);text-anchor:middle}}

.answer{{background:var(--accent-soft);border-left:4px solid var(--accent);padding:14px 16px;display:grid;gap:6px;border-radius:2px}}
.answer h4{{margin:0;font-size:14.5px;color:var(--accent)}}
.answer ul{{margin:0;padding-left:18px;display:grid;gap:6px;font-size:14.5px}}
.check{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:10px}}
.check > div{{background:var(--panel);border:1px solid var(--rule);padding:14px 16px;display:grid;gap:4px;align-content:start;border-radius:2px}}
.check b{{font-size:15px}}
.check span{{font-size:14px;color:var(--ink2)}}
.check em{{font-style:normal;font:600 11.5px var(--mono);color:var(--accent);letter-spacing:.04em}}

.qs{{counter-reset:q;display:grid;gap:12px;margin:0;padding:0;list-style:none}}
.qs li{{counter-increment:q;display:grid;grid-template-columns:36px 1fr;gap:4px 12px;background:var(--panel);border:1px solid var(--rule);padding:14px 16px;border-radius:2px}}
.qs li::before{{content:counter(q);grid-row:span 3;font:800 22px/1.1 var(--mono);color:var(--accent)}}
.qs .say{{font-weight:700}}
.qs .why{{font-size:14px;color:var(--ink2)}}
.qs .tag{{font:600 11.5px var(--mono);color:var(--ink3);letter-spacing:.04em}}

.src{{font-size:13.5px;color:var(--ink2);display:grid;gap:6px;margin:0;padding-left:18px}}
footer{{margin-top:56px;padding-top:16px;border-top:1px solid var(--rule);font-size:13px;color:var(--ink3)}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
@media print{{body{{background:#fff}} .scen,nav.toc{{display:none}} section{{break-inside:avoid-page}}}}
</style>
</head>
<body>
<div class="wrap">

<header class="top">
  <p class="eyebrow">계림동 지하1층 · 내부용 판단 노트 · 위탁운영 개정판</p>
  <h1>할까, 말까 — 의장님 미팅 전에 두 분이 볼 것</h1>
  <p class="warnline">⚠ 두 분만 보세요. 의장님(소유자) 전액투자·위탁운영 조건과 신창점 실적 비교가 들어 있습니다.</p>
  <div class="meta"><span>개정판 · 2026-10-15</span><span>의장님 층 소유(보증금·월세 0원) · 전액투자 위탁운영</span><span>기준: 신창점</span><span>약 230평</span></div>
  <nav class="toc" aria-label="목차">
    <a href="#s1">한눈에</a><a href="#s2">판단표</a><a href="#s3">의장님 속내</a><a href="#s4">수익 계산기</a>
    <a href="#s5">위탁 조건</a><a href="#s6">신창 기준·운영 구조</a><a href="#s7">공간·현장</a><a href="#s8">미팅 질문 순서</a><a href="#s9">근거와 한계</a>
  </nav>
</header>

<section id="s1">
  <header><p class="eyebrow">한눈에</p><h2>의장님이 해당 층 소유자: 보증금·월세 0원, 리스크 없이 순수익 셰어로 갑니다</h2></header>
  <div class="verdict">
    <div><span class="chip go">최종 방향 · 위탁운영 추진</span></div>
    <p class="prose"><span class="hl">의장님이 해당 층(지하 1층 230평)의 실소유자</span>이시므로, <b>보증금과 월세(임대료)는 일체 발생하지 않습니다.</b> 공간·인테리어·장비 등 <span class="hl">모든 시설 투자는 의장님이 100% 부담(소유)</span>하시며, 우리는 프로그램·코칭·회원 관리 등 <b>위탁운영만 전담</b>합니다. 매달 발생하는 <span class="hl">순수익에서 일정 %(성과급)</span>를 정산받으며, 우리 보증금도, 월세 부담도, 장비 상환도, 초기 적자 부담도 전혀 없는 완벽한 「우리 돈 0원」 구조입니다.</p>
    <div class="facts">
      <div class="fact"><span class="k">자리 잡은 뒤 우리 월 성과급</span><span class="v num" data-o="ourM">–</span><span class="n" data-o="ourMCmp">–</span></div>
      <div class="fact"><span class="k">자리 잡은 뒤 의장님 월 순수익</span><span class="v num" data-o="hisM">–</span><span class="n" data-o="hisMCmp">–</span></div>
      <div class="fact"><span class="k">손익분기점(BEP) 회원 수</span><span class="v num" data-o="beMem">–</span><span class="n" data-o="beRev">–</span></div>
    </div>
    <p class="prose muted small">의장님 입장에서도 공실이던 본인 소유 공간에 매달 월세 이상의 안정적인 순수익(약 600~800만원)이 발생하고 건물 가치가 극대화됩니다. 외부에 나가는 임대료가 없기 때문에 손익분기점이 회원 약 55명으로 매우 낮아 서로에게 가장 안전합니다.</p>
  </div>
</section>

<section id="s2">
  <header><p class="eyebrow">판단표</p><h2>이 조건이면 한다, 이러면 안 한다</h2></header>
  <div class="cols3">
    <div class="card bar-go">
      <h3><span class="chip go">꼭 받아야 할 것</span></h3>
      <ol>
        <li><b>의장님이 층 소유자 → 보증금·월세 0원 <span class="fixed">확정</span></b><span>의장님이 해당 층 소유자이므로 보증금과 월 임대료는 없습니다. 시설·장비 전액도 의장님이 투자하며, 우리는 투자금 상환 의무가 없습니다.</span></li>
        <li><b>개업 초기 적자는 의장님 부담 <span class="fixed">확정</span></b><span>회원이 차오르기 전(1~3개월) 발생하는 월 운영비 부족분은 사업자이자 소유자인 의장님이 전액 보전합니다.</span></li>
        <li><b>현장 위탁운영 전권 위임</b><span>코칭 인력 채용·배치, 수업 프로그램 편성, 회원 유치 및 등록 관리는 트레이닝판이 독자적으로 전담합니다.</span></li>
        <li><b>순수익의 일정 %(목표 40%) 성과급</b><span>순수익(매출 − 월 운영비)을 매월 명확히 정산하여 정해진 비율로 수수료를 지급받습니다. 적자 달은 수수료 0원.</span></li>
        <li><b>최소 계약 3~5년 및 일방 해지 방지</b><span>회원이 자리 잡는 데 시간이 걸리므로 계약 기간을 보장하고, 건물 매각 시 위탁계약 승계 또는 중도 해지 시 보상 조항을 둡니다.</span></li>
        <li><b>원상복구 의무 면제</b><span>모든 시설과 장비 소유권이 의장님에게 있으므로 계약 종료 시 철거·원상복구 의무는 없습니다.</span></li>
      </ol>
    </div>
    <div class="card bar-warn">
      <h3><span class="chip warn">협상할 것</span></h3>
      <ul>
        <li><b>위탁운영 수수료율 (30~50%)</b><span>기준은 40%로 제시하고, 의장님의 투자 규모와 관리비 분담 수준에 따라 조율합니다.</span></li>
        <li><b>월 운영비 예산 인정 범위</b><span>코치 인건비(약 600~660만)와 관리비/공과금(약 300만)이 매출에서 실비로 우선 차감되도록 예산안을 확정합니다.</span></li>
        <li><b>회원 주차 및 출입 동선</b><span>지하주차장 무료 지원, 새벽 6시~밤 11시 건물 출입구 개방, 외부 도로변 간판 설치 협의.</span></li>
        <li><b>회복실(사우나 등)은 2단계 선택</b><span>초기 투자비가 커지면 의장님 부담이 늘어나므로, 1단계 체육관 오픈 후 안정화되면 진행합니다.</span></li>
      </ul>
    </div>
    <div class="card bar-stop">
      <h3><span class="chip stop">이러면 안 한다</span></h3>
      <ul>
        <li><b>보증금이나 월세를 별도로 요구할 때</b><span>의장님이 해당 층 소유자인데 보증금이나 월세를 요구하면 위탁운영 구조와 맞지 않습니다.</span></li>
        <li><b>개업 초기 적자를 우리보고 메우라고 할 때</b><span>운영비 적자를 우리가 부담하면 '우리 돈 0원' 원칙이 깨집니다.</span></li>
        <li><b>수수료율이 25% 미만으로 너무 낮을 때</b><span>회원 150명을 채워도 우리 몫이 300만원 미만이면 신창점 대비 관리 투입의 의미가 없습니다.</span></li>
        <li><b>의장님이 수업 시간표나 코칭 방식에 비전문적으로 간섭할 때</b><span>운영 전권이 없으면 프로그램 품질 유지가 어렵습니다.</span></li>
        <li><b>천장 높이(보 아래 3.4m 미만)나 소음/진동 민원으로 수업이 불가할 때</b><span>체육관 등록 및 영업 불가 사유입니다.</span></li>
      </ul>
    </div>
  </div>
</section>

<section id="s3">
  <header><p class="eyebrow">의장님 속내</p><h2>왜 소유자인 의장님이 전액 투자하고 위탁을 맡길까</h2></header>
  <p class="prose">의장님이 본인 소유 공간에 수억 원을 투자하면서 직접 운영하지 않고 우리에게 위탁운영을 맡기는 이유는 명확합니다. 의장님에게도 확실한 이득이 있기 때문입니다.</p>
  <div class="tbl"><table>
    <thead><tr><th style="width:24%">의장님의 진짜 의도</th><th>의장님이 얻는 것</th><th>우리의 접근 전략</th><th>미팅 확인 질문</th></tr></thead>
    <tbody>
      <tr><td><b>① 본인 소유 빈 상가 가치 극대화</b><br><span class="muted small">의장님이 해당 층 소유자 · 관리비만 지출</span></td><td>공실 상가가 하루 100명이 찾는 앵커 시설로 변모하여 건물 전체 활성화 및 자산가치 대폭 상승</td><td>공실 해소와 자산 가치 상승을 강조하며 초기 적자 보전과 주차 지원을 요청</td><td>「비어 있는 동안 고민이 많으셨을 텐데, 활성화 기대가 가장 크시죠?」</td></tr>
      <tr><td><b>② 전문 운영 노하우 부재</b><br><span class="muted small">체육시설을 차리고 싶지만 운영 불가</span></td><td>크로스핏·하이록스 코칭, 공인 자격, 회원 관리 시스템을 완제품으로 탑재</td><td>우리의 지점 운영 실적(신창 등)과 검증된 코칭 역량을 보여주며 신뢰 형성</td><td>「운영과 코칭은 저희 시스템대로 전권을 주셔야 결과가 확실히 납니다.」</td></tr>
      <tr><td><b>③ 본인 건설사 원가 시공</b><br><span class="muted small">인테리어 공사를 직접 진행</span></td><td>공사 이윤 확보 + 시공 원가 절감으로 실질 투자비용 대폭 절감 가능</td><td>공사는 의장님 회사에서 맡고, 우리는 체육관 특화 설계 스펙(바닥, 방음, 리그)을 제공</td><td>「인테리어 공사는 의장님 회사에서 원가에 맞춰 직접 시공해 주실 수 있죠?」</td></tr>
      <tr><td><b>④ 임대료 이상의 안정적 수익</b><br><span class="muted small">공실 월세 0원 vs 순수익 60%</span></td><td>공실 월세 0원에서 매월 600~800만원 순수익 창출 (투자 회수 후 영구 수익)</td><td>합리적인 수수료율(우리가 40%, 의장님이 60%)로 윈윈 구조 구축</td><td>「순수익의 60%를 의장님이 가져가시면 일반 임대료보다 훨씬 수익성이 좋습니다.」</td></tr>
    </tbody>
  </table></div>
</section>

<section id="s4">
  <header><p class="eyebrow">숫자 계산기</p><h2>수익 분배와 투자 회수 계산기</h2></header>
  <p class="prose">의장님 전액투자 + 위탁운영 성과급 모델입니다. <b>의장님이 해당 층 소유자이므로 보증금과 월세는 0원</b>입니다. <b>예상 총매출 = 인원수 × 회원권 월단가</b>이고, <b>순수익 = 매출(수수료 차감 후) − 월 실운영비</b>, <b>우리 성과급 = 순수익 × 성과급 %</b>(적자 시 0원), <b>의장님 몫 = 순수익 − 우리 성과급</b>(적자 시 의장님 부담)입니다.</p>

  <div class="scen" role="group" aria-label="시나리오">
    <button type="button" data-scen="low">보수적 (120명 · 14만)</button>
    <button type="button" data-scen="base" aria-pressed="true">기준안 (150명 · 14만)</button>
    <button type="button" data-scen="high">낙관적 (180명 · 15만)</button>
  </div>

  <div class="calc">
    <div class="panel">
      <fieldset>
        <legend>인원수와 회원권 월단가</legend>
        <div class="ctl">
          <div class="lab"><label for="Members">목표 인원수 (회원 수)</label><output for="Members" id="oMembers"></output></div>
          <input type="range" id="Members" min="50" max="250" step="5" value="150">
          <span class="hint">자리 잡은 뒤 등록 회원 수 (신창 평균 약 191명)</span>
        </div>
        <div class="ctl">
          <div class="lab"><label for="Price">회원권 월단가 (1인당 실수령)</label><output for="Price" id="oPrice"></output></div>
          <input type="range" id="Price" min="10" max="25" step="0.5" value="14">
          <span class="hint">할인·장기권 반영 후 실 결제단가 (신창 기준 약 11~14만원)</span>
        </div>
        <div class="ctl" style="background:var(--paper);padding:8px 12px;border-radius:4px;border:1px solid var(--rule)">
          <div class="lab" style="font-size:13.5px"><span style="color:var(--ink3)">계산된 예상 월 총매출</span><b id="oCalcRev" style="font-size:15px;color:var(--accent)">–</b></div>
        </div>
        <div class="ctl">
          <div class="lab"><label for="T">회원이 차오르는 속도</label><output for="T" id="oT"></output></div>
          <input type="range" id="T" min="1" max="3" step="1" value="2">
          <span class="hint">1: 빠름(3개월) · 2: 보통(6개월) · 3: 느림(9개월)</span>
        </div>
      </fieldset>

      <fieldset>
        <legend>월 실운영비와 성과급 비율 (월세 없음)</legend>
        <div class="ctl"><div class="lab"><label for="O">매달 나가는 실운영비 (월세 0원)</label><output for="O" id="oO"></output></div>
          <input type="range" id="O" min="800" max="1400" step="20" value="1000">
          <span class="hint">코치 인건비 약 660만원 + 공과금·관리비 약 300만원 + 소모품·기타 40만원 (월세 없음)</span></div>
        <div class="ctl"><div class="lab"><label for="Pct">우리 위탁운영 성과급 비율</label><output for="Pct" id="oPct"></output></div>
          <input type="range" id="Pct" min="20" max="60" step="5" value="40">
          <span class="hint">순수익에서 우리가 가져갈 비율 (기준 40% → 의장님 60%)</span></div>
      </fieldset>

      <fieldset>
        <legend>의장님 초기 투자금 (의장님 100% 부담)</legend>
        <div class="ctl"><div class="lab"><label for="I">인테리어 단가 (230평)</label><output for="I" id="oI"></output></div>
          <input type="range" id="I" min="70" max="180" step="10" value="100">
          <span class="hint">의장님 건설사 직영 시공 시 평당 90~110만원선 추정</span></div>
        <div class="ctl"><div class="lab"><label for="E">운동 장비·가전·비품 일체</label><output for="E" id="oE"></output></div>
          <input type="range" id="E" min="8000" max="22000" step="1000" value="12000">
          <span class="hint">유산소 머신, 바벨, 리그, 가전, 전산 등 의장님이 전액 구매</span></div>
        <div class="chk"><input type="checkbox" id="W"><label for="W"><b>2단계 회복실(사우나·냉탕) 포함</b><br><span class="hint">공사비 +7,500만원, 월 관리비 +120만원 (초기엔 미체크 권장)</span></label></div>
      </fieldset>
    </div>

    <div class="panel out">
      <div class="month">
        <span class="t">월 매출 (수수료 4.8% 제외 후)</span><span class="v" data-o="rev"></span>
        <span class="t">월 실운영비 (인건비+관리비, 월세0)</span><span class="v" data-o="cO"></span>
        <span class="t sum">월 순수익 (영업이익)</span><span class="v sum" data-o="profit"></span>
        <span class="t" style="color:var(--accent);font-weight:700">우리 위탁 성과급</span><span class="v" style="color:var(--accent);font-weight:800" data-o="ourM"></span>
        <span class="t" style="color:var(--chart-a);font-weight:700">의장님 몫 (순수익 − 성과급)</span><span class="v" style="color:var(--chart-a);font-weight:800" data-o="hisM"></span>
        <div class="cmp" data-o="cmpSin"></div>
      </div>

      <div class="big3">
        <div><div class="k">우리 자본 투입금</div><div class="v" style="color:var(--go)">0원</div><div class="n">보증금·월세·리스크 0</div></div>
        <div><div class="k">의장님 총 투자금</div><div class="v" data-o="capex"></div><div class="n" data-o="capexN"></div></div>
        <div><div class="k">의장님 투자금 회수 기간</div><div class="v" data-o="payY"></div><div class="n">의장님 몫 순수익으로 회수</div></div>
      </div>

      <div class="big3 big4">
        <div><div class="k">손익분기점(BEP) 매출</div><div class="v" data-o="beRev"></div><div class="n">운영비 충당 기준</div></div>
        <div><div class="k">손익분기점 회원 수</div><div class="v" data-o="beMem"></div><div class="n">월세가 없어 회원 55명이면 흑자</div></div>
      </div>

      <div class="charts">
        <div class="chartbox">
          <h4>24개월 예상 월 매출과 손익분기점</h4>
          <svg id="ch1" viewBox="0 0 520 220" role="img" aria-label="월 매출 추이 그래프"></svg>
          <div class="legend"><span><i style="background:var(--chart-a)"></i>월 매출</span><span><i style="background:var(--ink3)"></i>신창 평균 2,100만</span><span><i style="background:var(--stop)"></i>손익분기 기준</span></div>
        </div>
        <div class="chartbox">
          <h4>의장님 투자금 회수 및 우리 누적 성과급</h4>
          <svg id="ch2" viewBox="0 0 520 220" role="img" aria-label="누적 손익 그래프"></svg>
          <div class="legend"><span><i style="background:var(--chart-a)"></i>의장님 누적 (투자 회수)</span><span><i style="background:var(--accent)"></i>우리 누적 성과급</span></div>
        </div>
      </div>
    </div>
  </div>

  <ul class="notes">
    <li>의장님이 해당 층 소유자이므로 보증금, 월세(임대료), 렌트프리는 일체 발생하지 않습니다.</li>
    <li>우리 성과급은 순수익(매출 − 월 운영비)에 성과급 %를 곱한 금액입니다. 적자 달은 0원입니다.</li>
    <li>초기 개업 적자(1~3개월 차 회원이 덜 찼을 때 발생하는 운영비 부족분)는 사업자인 의장님이 부담합니다.</li>
    <li>카드 수수료·부가세(약 4.8%)는 매출에서 자동 차감 반영됩니다.</li>
  </ul>
</section>

<section id="s5">
  <header><p class="eyebrow">위탁 조건</p><h2>위탁운영 계약 — 꼭 챙겨야 할 3대 조항</h2></header>
  <div class="tbl"><table>
    <thead><tr><th style="width:20%">구분</th><th>일반 임대차 계약</th><th class="rec">의장님 소유 전액투자 위탁운영 (우리 모델)</th><th>단순 지분 동업</th></tr></thead>
    <tbody>
      <tr><td><b>자본 투입</b></td><td>보증금 + 인테리어 + 장비 (수억원 부담)</td><td class="rec"><span class="chip go">우리 돈 0원 (보증금·월세 없음, 의장님 100% 투자)</span></td><td>공동 출자 (수천~수억원)</td></tr>
      <tr><td><b>월 임대료</b></td><td>매달 수백~천만원 고정 지출</td><td class="rec"><span class="chip go">0원 (의장님이 해당 층 소유자)</span></td><td>해당 건물 조건에 따름</td></tr>
      <tr><td><b>초기 적자</b></td><td><span class="chip stop">임차인이 100% 메움</span></td><td class="rec"><span class="chip go">사업자(의장님)가 전액 보전</span></td><td>지분 비율대로 메움</td></tr>
      <tr><td><b>소유권</b></td><td>장비·시설 소유, 원상복구 의무 발생</td><td class="rec">의장님이 100% 소유, 원상복구 의무 없음</td><td>공동 소유 (청산 시 복잡)</td></tr>
      <tr><td><b>우리의 역할과 보상</b></td><td>사업 운영 후 월세 내고 남는 이익</td><td class="rec"><b>전문 위탁운영 + 순수익의 일정 % 수수료</b></td><td>경영 참여 + 배당금 분배</td></tr>
      <tr><td><b>리스크</b></td><td>사업 실패 시 빚과 원상복구 폭탄</td><td class="rec"><span class="chip go">재정적 손실 0 (기회비용만 존재)</span></td><td>출자금 손실 위험</td></tr>
    </tbody>
  </table></div>

  <div class="cols3">
    <div class="card">
      <h3>1. 순수익 정산의 투명성</h3>
      <p><b>순수익 = 총 매출 − 공제 비용(운영비)</b>입니다. 의장님이 해당 층 소유자라 임대료가 나가지 않으므로, 코치 급여(약 600~660만), 4대보험, 공과금(전기·수도·가스), 소모품비, 마케팅비 등 실운영비만 투명하게 차감합니다.</p>
    </div>
    <div class="card">
      <h3>2. 초기 적자 보전 의무</h3>
      <p>오픈 초기 1~3개월 동안 매출이 월 운영비(약 1,000만원)에 미치지 못할 경우, <b>의장님이 즉시 운영 계좌에 부족분을 입금</b>하여 코치 급여와 공과금이 체납되지 않도록 하는 조항이 필수입니다. 이것이 우리 0원 조건의 핵심 방어막입니다.</p>
    </div>
    <div class="card">
      <h3>3. 계약 기간과 중도 해지 보상</h3>
      <p>회원을 모으고 궤도에 올려놓았는데 의장님이 계약을 일방적으로 해지하고 다른 사람을 앉히는 위험을 막아야 합니다. <b>최소 3~5년 계약 기간 보장</b>, 건물 매각 시 위탁계약 승계 의무, 부당 해지 시 최근 6개월 평균 수수료 기준 위약금 조항을 넣습니다.</p>
    </div>
  </div>
</section>

<section id="s6">
  <header><p class="eyebrow">신창 기준 · 운영 구조</p><h2>신창점과 비교해 본 계림 위탁운영의 절대적 우위</h2></header>
  <div class="cols3">
    <div class="card bar-go"><h3>신창점 (직접 임차 운영)</h3>
      <ul>
        <li><b class="num">월 매출 2,100만원</b><span>유효 회원 약 191명 기준</span></li>
        <li><b class="num">고정비 1,450만원 (임대료 660만)</b><span>의장님에게 매달 임대료 660만(곧 700만) 지출</span></li>
        <li><b class="num">월 순이익 약 550만원</b><span>보증금·시설비 투자 및 적자 위험을 안고 거두는 순이익</span></li>
      </ul>
    </div>
    <div class="card bar-go"><h3>계림점 (소유자 전액투자 위탁운영)</h3>
      <ul>
        <li><b class="num">목표 매출 2,100만원 (회원 150명)</b><span>하이록스+크로스핏 듀얼 프로그램</span></li>
        <li><b class="num">월 운영비 약 1,000만원 (월세 0원!)</b><span><b>의장님이 층 소유자라 임대료 0원!</b> (인건비 660만 + 관리비 300만)</span></li>
        <li><b class="num">순수익 1,100만 → 우리 몫 440~550만원</b><span>수수료 40% 시 440만, 50% 시 550만 수령. <b>보증금·월세·리스크 0원!</b></span></li>
      </ul>
    </div>
    <div class="card"><h3>왜 계림이 훨씬 안전한가</h3><p>신창은 매달 660만원의 월세를 남에게 내야 하므로 손익분기점이 높지만, 계림은 <b>의장님 본인 건물(소유 층)이라 월세가 0원</b>입니다. 실운영비(인건비+관리비) 약 1,000만원만 넘기면(회원 약 55~60명) 즉시 흑자로 전환되어 적자 위험이 극도로 낮습니다.</p></div>
  </div>
</section>

<section id="s7">
  <header><p class="eyebrow">공간 · 현장</p><h2>Hyb 존과 Met 존 — 리그 한 줄로 나눕니다</h2></header>
  <p class="prose">하이록스 수업과 크로스핏 수업을 <b>같은 시간에 각자의 존에서</b> 돌립니다. 사선 벽 쪽 띠가 <b>Hyb 존</b>(썰매 레인·트레드밀, 약 74평), 그 아래 삼각형이 <b>Met 존</b>(트인 바닥·바이크, 약 90평)이고, 두 존의 경계에 <b>리그(철봉) 약 25m</b>를 세웁니다. 경계선은 3번 기둥 모서리에서 7번 기둥 쪽으로 사선 벽과 거의 나란히 갑니다.</p>
{plan_svg_html}
  <div class="answer">
    <h4>의장님께 제안할 시설 투자 요약</h4>
    <ul>
      <li><b>1단계 필수 공사</b>: 내부 칸막이벽 완전 철거(한 판 바닥 조성), 바닥 고무블럭 및 잔디 썰매 트랙(25m), 25m 커스텀 리그, 남녀 샤워·탈의실 기본 공사, 냉난방 공조.</li>
      <li><b>2단계 선택 공사</b>: 회복실(사우나 부스·냉탕). 1단계 오픈 후 회원 반응을 보고 추진.</li>
    </ul>
  </div>
</section>

<section id="s8">
  <header><p class="eyebrow">미팅 질문 순서</p><h2>순서가 중요합니다 — 속내부터, 조건은 자연스럽게</h2></header>
  <p class="prose muted">처음부터 수수료 몇 %를 따지기보다, 의장님이 왜 이 제안을 주셨는지 듣고 위탁운영 모델의 안정성을 설득해야 합니다.</p>
  <ol class="qs">
    <li><span class="say">「이 공간 이야기를 저희한테 먼저 꺼내 주신 이유가 궁금합니다.」</span><span class="why">듣기만 합니다. 공실 해결, 시공 물량, 공간 가치 상승 등 의장님의 주된 니즈를 확인합니다.</span><span class="tag">속내 확인</span></li>
    <li><span class="say">「이 건물, 앞으로 3~5년 정도 장기적인 운영이나 개발 계획은 어떻게 보세요?」</span><span class="why">매각이나 재건축 계획 여부를 확인하고, 위탁운영 계약 기간(3~5년)의 토대를 만듭니다.</span><span class="tag">계약 기간</span></li>
    <li><span class="say">「인테리어와 운동 장비 등 초기 투자 예산 규모는 대략 어느 정도로 생각하고 계신가요?」</span><span class="why">의장님 입에서 먼저 투자 가능 금액을 듣습니다. 우리가 먼저 액수를 정하지 않습니다.</span><span class="tag">투자 규모</span></li>
    <li><span class="say">「인테리어 공사는 의장님 회사에서 직접 시공해 주실 수 있죠?」</span><span class="why">원가 시공이 가능함을 확인하고, 체육관 특화 설계 스펙(바닥, 방음, 층고 등)을 전달합니다.</span><span class="tag">시공 주체</span></li>
    <li><span class="say">「의장님이 해당 층 소유자이시니 보증금이나 월세 없이, 시설 전액 투자를 해 주시고 저희는 전문 위탁운영을 맡아 순수익을 셰어하는 방식으로 가고자 합니다. 의장님도 이 방향이 가장 좋으시죠?」</span><span class="why">우리의 핵심 사업 구조를 명확히 제시합니다. 임대차/월세가 아닌 위탁운영으로 확정합니다.</span><span class="tag">사업 구조 확정</span></li>
    <li><span class="say">「오픈 초기 몇 달은 회원이 덜 차서 운영비 적자가 날 텐데, 이 기간 인건비와 공과금 지원은 어떻게 풀어갈까요?」</span><span class="why">초기 적자를 사업자인 의장님이 보전하도록 확답을 받는 핵심 질문입니다.</span><span class="tag">초기 적자 보전</span></li>
    <li><span class="say">「매출에서 코치 인건비와 관리비를 먼저 제하고 남는 순수익에서 수수료를 정산하면 의장님도 공실 월세보다 훨씬 큰 수익을 가져가실 수 있는데, 배분율은 어느 정도가 적당할까요?」</span><span class="why">기준 40%(의장님 60%)를 염두에 두고 의장님의 눈높이를 타진합니다.</span><span class="tag">수익 셰어</span></li>
    <li><span class="say">「관리비와 전기·수도세는 매달 어느 정도 나오고, 건물에서 지원해 주실 수 있는 부분이 있나요?」</span><span class="why">매달 나가는 고정 운영비의 규모를 파악합니다.</span><span class="tag">운영비</span></li>
    <li><span class="say">「회원들 지하주차장 무료 이용은 몇 대, 몇 시간까지 지원해 주실 수 있나요? 지상에서 내려오는 길은 어디가 좋은가요?」</span><span class="why">회원 모집의 결정적 요인인 주차와 출입 동선을 확정합니다.</span><span class="tag">주차 · 출입</span></li>
    <li><span class="say">「철거할 벽 중에 방화벽이 있는지, 천장 보 아래 실제 높이가 얼마나 나오는지 현장에서 확인해보고 싶습니다.」</span><span class="why">공사 가능 여부와 운동 수업 적합성을 물리적으로 검증합니다.</span><span class="tag">현장 실사</span></li>
    <li><span class="say">「공사 시작과 오픈 시기는 언제쯤으로 희망하시나요?」</span><span class="why">내년 초 새해 운동 수요(1~3월)에 맞추어 일정을 제안합니다.</span><span class="tag">일정</span></li>
  </ol>
</section>

<section id="s9">
  <header><p class="eyebrow">근거와 한계</p><h2>이 숫자들과 기준의 출처</h2></header>
  <ul class="src">
    <li><b>신창점 실적</b>: 월 매출 2,100만원, 고정비 1,450만원(임대료 660만원 포함), 순이익 약 550만원은 태준님이 제공해주신 2026년 1~9월 실적 기준입니다.</li>
    <li><b>계림점 운영비 추정</b>: 코치 2명 인건비 약 600~660만원(4대보험 포함), 관리비·전기·수도 공과금 약 300만원, 소모품 및 마케팅비 약 40만원으로 월 약 1,000만원 책정 (월세 0원).</li>
    <li><b>회원권 객단가</b>: 1인당 월 실수령 약 14만원(무제한권 및 횟수권, 장기권 할인 평균 반영). 150명 등록 시 월 매출 약 2,100만원 도출.</li>
    <li><b>인테리어 및 장비 단가</b>: 인테리어 평당 90~110만원(철거, 기본 바닥, 조명, 샤워실), 장비 약 1.2억원(유산소 머신 10대, 바벨·플레이트, 케틀벨·덤벨, 리그 25m, 가전·집기 등).</li>
    <li><b>법적 검토</b>: 의장님이 해당 층 소유자이므로 임대차 계약이 성립하지 않으며, 민법상 위탁운영(위임/용역) 계약을 체결합니다. 따라서 상가임대차보호법의 적용 대상이 아니며, 계약서 내의 계약 기간(3~5년) 및 해지 위약금 조항이 핵심 안전장치입니다.</li>
  </ul>
</section>

<footer>계림 판단 노트 · 위탁운영 개정판 · 2026-10-15 · 트레이닝판 내부용</footer>
</div>

<script>
(function(){{
  const $ = (id) => document.getElementById(id);
  const AREA = 230, PREOPEN = 2000; // 만원
  const SIN = {{ rev: 2100, cost: 1450, rent: 660, net: 550 }};
  const WELL = {{ capex: 7500, opex: 120, perMember: 1 }};
  const TAU = [4, 6, 9], SPEED = ['빠름', '보통', '느림'];
  const SCEN = {{
    low:  {{ Members:120, Price:14, T:3, W:false, O:950, Pct:40, I:90, E:10000 }},
    base: {{ Members:150, Price:14, T:2, W:false, O:1000, Pct:40, I:100, E:12000 }},
    high: {{ Members:180, Price:15, T:1, W:false, O:1050, Pct:40, I:110, E:13000 }}
  }};
  const ids = ['Members','Price','T','O','Pct','I','E'];
  const fmt = (v) => {{
    const r = Math.round(v);
    if (Math.abs(r) >= 10000) return (Math.round(r / 1000) / 10).toLocaleString('ko-KR') + '억원';
    return r.toLocaleString('ko-KR') + '만원';
  }};
  const signed = (v) => (v < 0 ? '− ' : '') + fmt(Math.abs(v));
  const years = (m) => {{
    if (!isFinite(m)) return '10년 넘게';
    const y = Math.floor(m / 12), mo = m % 12;
    return y > 0 ? (mo ? `${{y}}년 ${{mo}}개월` : `${{y}}년`) : `${{mo}}개월`;
  }};
  const read = () => {{ const v = {{}}; ids.forEach(k => v[k] = Number($(k).value)); v.W = $('W').checked; return v; }};
  
  function model(v){{
    const tau = TAU[v.T - 1];
    const ramp = (m) => 1 - 0.75 * Math.exp(-(m - 1) / tau);
    const upl = v.W ? (1 + WELL.perMember / v.Price) : 1;
    const opex = v.O + (v.W ? WELL.opex : 0);
    const capex = AREA * v.I + v.E + PREOPEN + (v.W ? WELL.capex : 0);
    
    // 월 기준 총매출 = 인원수 * 회원권 월단가
    const fullGrossRev = v.Members * v.Price * upl;

    let ourCum = 0, hisCum = -capex, pay = Infinity;
    const revS = [], ourS = [], hisS = [];
    
    for (let m = 1; m <= 120; m++) {{
      const grossRev = fullGrossRev * ramp(m);
      const netRev = grossRev * (1 - 0.048); // 카드수수료 및 부가세 4.8% 제외
      const profit = netRev - opex;
      
      const ourShare = profit > 0 ? profit * v.Pct / 100 : 0;
      const hisShare = profit > 0 ? profit * (100 - v.Pct) / 100 : profit; // 적자는 의장님이 메움
      
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
      + `<line class="ref" x1="${{L}}" x2="${{W-R}}" y1="${{y(r.beRev)}}" y2="${{y(r.beRev)}}" style="stroke:var(--stop)"/><text class="reflab" x="${{W-R+6}}" y="${{y(r.beRev)+4}}" style="fill:var(--stop)">손익분기</text>`;
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
    svg.innerHTML = g + `<line class="zero" x1="${{L}}" x2="${{W-R}}" y1="${{y(0)}}" y2="${{y(0)}}"/><path class="la" d="${{line(his)}}"/><path class="lb" d="${{line(ours)}}"/>` + mark;
  }}

  const set = (k, t) => document.querySelectorAll(`[data-o="${{k}}"]`).forEach(el => el.textContent = t);
  
  function render(){{
    const v = read();
    const gross = v.Members * v.Price;
    $('oMembers').textContent = v.Members + '명';
    $('oPrice').textContent = v.Price + '만원';
    $('oCalcRev').textContent = `${{fmt(gross)}} (${{v.Members}}명 × ${{v.Price}}만)`;
    $('oT').textContent = SPEED[v.T - 1];
    $('oO').textContent = fmt(v.O);
    $('oPct').textContent = v.Pct + '%';
    $('oI').textContent = v.I + '만원/평';
    $('oE').textContent = fmt(v.E);
    
    const r = model(v);
    set('rev', fmt(r.netRevM) + ` (총매출 ${{fmt(r.grossRevM)}})`);
    set('cO', '− ' + fmt(r.opex));
    set('profit', fmt(r.profitM));
    set('ourM', fmt(r.ourM));
    set('hisM', fmt(r.hisM));
    
    const d = r.ourM - SIN.net;
    set('cmpSin', `우리 성과급은 신창 순이익(550만원) 대비 ${{d >= 0 ? '+' : '−'}}${{fmt(Math.abs(d))}} (보증금·월세·리스크 0원)`);
    set('ourMCmp', `수수료 ${{v.Pct}}% 정산 · ${{v.Members}}명 기준`);
    set('hisMCmp', `의장님 몫 ${{100 - v.Pct}}% · 투자금 회수 후 순이익`);
    set('beRev', `월 매출 ${{fmt(r.beRev)}}`);
    set('beMem', `약 ${{r.beMem}}명 (월세 0원 효과)`);
    set('capex', fmt(r.capex));
    set('capexN', `인테리어 ${{fmt(AREA * v.I)}} · 장비 ${{fmt(v.E)}} · 사전비용 ${{fmt(PREOPEN)}}` + (v.W ? ` · 회복실 ${{fmt(WELL.capex)}}` : ''));
    set('payY', years(r.pay));
    
    drawRev(v, r);
    drawCash(r);
  }}

  function summary(){{
    const r = model(Object.assign({{}}, SCEN.base));
    set('ourM', fmt(r.ourM));
    set('hisM', fmt(r.hisM));
    set('beMem', `약 ${{r.beMem}}명 (월세 0원 효과)`);
    set('beRev', `월 매출 ${{fmt(r.beRev)}}`);
    set('payY', years(r.pay));
  }}

  function applyScen(name){{
    const s = SCEN[name];
    ids.forEach(k => $(k).value = s[k]);
    $('W').checked = s.W;
    document.querySelectorAll('[data-scen]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.scen === name)));
    render();
  }}

  document.querySelectorAll('[data-scen]').forEach(b => b.addEventListener('click', () => applyScen(b.dataset.scen)));
  ids.concat('W').forEach(k => $(k).addEventListener('input', () => {{
    document.querySelectorAll('[data-scen]').forEach(b => b.setAttribute('aria-pressed', 'false'));
    render();
  }}));

  summary();
  render();
}})();
</script>
</body>
</html>
'''

with open('kyerim-internal.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully regenerated kyerim-internal.html with owner context. Length:", len(new_html))
