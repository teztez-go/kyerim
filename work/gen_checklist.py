# -*- coding: utf-8 -*-

checklist_html = '''<!doctype html>
<html lang="ko" class="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>계림점 현장 확인 체크리스트 — 트레이닝판</title>
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
</style>
</head>
<body class="bg-dark-bg text-slate-100 font-sans antialiased selection:bg-brand-500 selection:text-white min-h-screen">

<!-- Top Header -->
<header class="sticky top-0 z-50 backdrop-blur-md bg-dark-bg/85 border-b border-dark-border px-4 lg:px-8 py-3.5">
  <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
    <div class="flex items-center gap-3">
      <a href="index.html" class="flex items-center gap-2 group">
        <span class="w-8 h-8 rounded-lg bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center font-black text-black text-base shadow-lg shadow-brand-500/20 group-hover:scale-105 transition">P</span>
        <div>
          <span class="font-bold text-base tracking-tight text-white group-hover:text-brand-500 transition">트레이닝판</span>
          <span class="text-xs text-slate-400 block -mt-1 font-mono">현장 확인 체크리스트</span>
        </div>
      </a>
      <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-brand-500/10 text-brand-500 border border-brand-500/30">인터랙티브 툴</span>
    </div>

    <!-- Tally Bar -->
    <div class="flex items-center gap-3 text-xs font-mono">
      <span class="text-slate-400">진행률: <b id="tDone" class="text-white">0</b>/<span id="tAll">0</span></span>
      <span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 font-bold">의장님께 질문 <b id="tHs">0</b></span>
      <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold">확정 <b id="tOk">0</b></span>
      <a href="index.html" class="ml-2 px-3 py-1.5 rounded-lg bg-dark-surface text-slate-300 hover:text-white border border-dark-border transition">허브 ↗</a>
    </div>
  </div>
</header>

<main class="max-w-4xl mx-auto px-4 lg:px-8 py-8 space-y-8">

  <!-- Intro Card -->
  <div class="p-6 rounded-2xl bg-dark-card border border-dark-border space-y-2">
    <h1 class="text-2xl font-bold text-white">계림점 조건 확인 & 질문 추출표</h1>
    <p class="text-xs sm:text-sm text-slate-400 leading-relaxed">
      각 항목마다 버튼을 눌러 상태를 표시해 주세요. <b class="text-amber-400">"의장님께 물어요"</b>를 누른 항목은 아래쪽에 실시간 질문지로 자동 취합되어 원클릭으로 복사할 수 있습니다.
    </p>
    <div class="flex flex-wrap gap-2 pt-2 text-xs font-medium">
      <span class="px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">✓ 맞아요: 내부 확정</span>
      <span class="px-2.5 py-1 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/30">? 의장님께 물어요: 미팅 질문</span>
      <span class="px-2.5 py-1 rounded-lg bg-sky-500/10 text-sky-400 border border-sky-500/30">⚙ 우리가 결정: 내부 조율</span>
    </div>
  </div>

  <!-- Checklist Groups Container -->
  <div id="groups" class="space-y-6"></div>

  <!-- Live Output Bucket -->
  <div class="p-6 rounded-2xl bg-dark-card border border-brand-500/40 space-y-4">
    <div class="flex items-center justify-between border-b border-dark-border pb-3">
      <h3 class="text-lg font-bold text-white flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
        의장님께 보낼 질문지 리스트 (자동 생성)
      </h3>
      <button type="button" id="copyBtn" class="px-3.5 py-1.5 rounded-xl bg-brand-500 text-black text-xs font-bold hover:bg-brand-400 transition shadow-lg shadow-brand-500/20">
        질문 전체 복사
      </button>
    </div>
    <div id="bHs" class="space-y-2 text-xs sm:text-sm text-slate-300"></div>
  </div>

</main>

<footer class="border-t border-dark-border bg-dark-card/50 py-8 px-4 text-center text-xs text-slate-500 font-mono space-y-2">
  <p>광주 계림동 운동공간 조건 확인표 · 트레이닝판 (TRAININGPAN)</p>
  <p>© 2026 TRAININGPAN. ALL RIGHTS RESERVED.</p>
</footer>

<script>
const ITEMS = [
  {id:"A1", g:"건물 및 공간", t:"지하 1층 면적은 약 230평이다 (메인 220평 + 사무실 10평)", state:"ok"},
  {id:"A2", g:"건물 및 공간", t:"메인 공간 안 칸막이벽은 기둥만 남기고 전부 철거한다", state:"hs"},
  {id:"A3", g:"건물 및 공간", t:"회원은 지하주차장 → 통로 → 서쪽 문으로 직결 출입한다", state:"ok"},
  {id:"A4", g:"건물 및 공간", t:"회원 지하주차장 무료 지원 (가능 대수 및 2시간 무료)", state:"hs"},
  {id:"A5", g:"건물 및 공간", t:"건물 출입 가능 시간 (새벽 6시 ~ 밤 11시 개방)", state:"hs"},
  {id:"A6", g:"건물 및 공간", t:"도로변 외부 간판 설치 가능 위치 및 크기 확인", state:"hs"},
  {id:"A7", g:"건물 및 공간", t:"샤워실 온수/배수 및 전력 용량(러닝머신·공조) 충분 여부", state:"hs"},
  {id:"A8", g:"건물 및 공간", t:"건축물대장상 체육시설(운동시설 760㎡) 용도 적합 여부", state:"hs"},

  {id:"B1", g:"위탁 계약 및 수익 분배", t:"의장님이 해당 층 소유자이므로 보증금과 월세(임대료)는 0원이다", state:"ok"},
  {id:"B2", g:"위탁 계약 및 수익 분배", t:"인테리어 및 운동 장비 전액은 의장님이 투자하며, 우리는 상환하지 않는다", state:"ok"},
  {id:"B3", g:"위탁 계약 및 수익 분배", t:"인테리어 공사는 의장님 회사에서 직접 원가 시공한다", state:"hs"},
  {id:"B4", g:"위탁 계약 및 수익 분배", t:"수익 분배는 순수익의 40%(우리) : 60%(의장님)으로 확정한다", state:"ok"},
  {id:"B5", g:"위탁 계약 및 수익 분배", t:"우리는 수업을 직접 뛰지 않고 총괄 운영하며, 코치는 전원 채용한다", state:"ok"},
  {id:"B6", g:"위탁 계약 및 수익 분배", t:"코치 채용 인건비(월 660만)는 실운영비로 산입하여 매출에서 우선 지급한다", state:"ok"},
  {id:"B7", g:"위탁 계약 및 수익 분배", t:"오픈 초기(1~3개월) 운영비 적자 발생 시 소유자인 의장님이 전액 보전한다", state:"hs"},
  {id:"B8", g:"위탁 계약 및 수익 분배", t:"위탁운영 계약 기간은 기본 3~5년이며 매각 시 승계 조항을 둔다", state:"hs"},
  {id:"B9", g:"위탁 계약 및 수익 분배", t:"사업자등록 및 매출 통장은 의장님(개인/법인) 명의로 개설한다", state:"hs"},

  {id:"C1", g:"운영 및 프로그램", t:"하이록스(Hyb) + 크로스핏(Met) 듀얼 클래스 동시 운영", state:"ok"},
  {id:"C2", g:"운영 및 프로그램", t:"사선벽을 활용해 광주 최장 25m 잔디 썰매 트랙 설치", state:"ok"},
  {id:"C3", g:"운영 및 프로그램", t:"2단계 회복실(사우나·냉탕)은 오픈 안정 후 추진한다", state:"ok"},
  {id:"C4", g:"운영 및 프로그램", t:"오픈 목표 시기는 2027년 1~3월 새해 성수기에 맞춘다", state:"hs"}
];

function render(){
  const container = document.getElementById("groups");
  container.innerHTML = "";

  const groups = [...new Set(ITEMS.map(i => i.g))];

  groups.forEach(gName => {
    const sec = document.createElement("section");
    sec.className = "bg-dark-card border border-dark-border rounded-2xl p-5 space-y-4";
    sec.innerHTML = `<h3 class="text-sm font-bold text-brand-400 font-mono uppercase tracking-wider">${gName}</h3>`;

    const list = document.createElement("div");
    list.className = "space-y-3";

    ITEMS.filter(i => i.g === gName).forEach(item => {
      const row = document.createElement("div");
      row.className = "p-3.5 rounded-xl bg-dark-surface/60 border border-dark-border/60 flex flex-col sm:flex-row sm:items-center justify-between gap-3";

      const title = document.createElement("span");
      title.className = "text-xs sm:text-sm font-medium text-slate-200";
      title.textContent = item.t;

      const btnGroup = document.createElement("div");
      btnGroup.className = "flex items-center gap-1.5 flex-shrink-0 text-xs font-semibold";

      const btnOk = document.createElement("button");
      btnOk.type = "button";
      btnOk.textContent = "확정";
      btnOk.className = `px-2.5 py-1 rounded-lg transition ${item.state === 'ok' ? 'bg-emerald-500 text-black font-bold' : 'bg-dark-bg text-slate-400 hover:text-white'}`;
      btnOk.onclick = () => { item.state = 'ok'; render(); };

      const btnHs = document.createElement("button");
      btnHs.type = "button";
      btnHs.textContent = "의장님께 질문";
      btnHs.className = `px-2.5 py-1 rounded-lg transition ${item.state === 'hs' ? 'bg-amber-400 text-black font-bold' : 'bg-dark-bg text-slate-400 hover:text-white'}`;
      btnHs.onclick = () => { item.state = 'hs'; render(); };

      const btnUs = document.createElement("button");
      btnUs.type = "button";
      btnUs.textContent = "우리 결정";
      btnUs.className = `px-2.5 py-1 rounded-lg transition ${item.state === 'us' ? 'bg-sky-400 text-black font-bold' : 'bg-dark-bg text-slate-400 hover:text-white'}`;
      btnUs.onclick = () => { item.state = 'us'; render(); };

      btnGroup.append(btnOk, btnHs, btnUs);
      row.append(title, btnGroup);
      list.append(row);
    });

    sec.append(list);
    container.append(sec);
  });

  // Tally & Questions
  const total = ITEMS.length;
  const hsItems = ITEMS.filter(i => i.state === 'hs');
  const okItems = ITEMS.filter(i => i.state === 'ok');

  document.getElementById("tAll").textContent = total;
  document.getElementById("tDone").textContent = okItems.length + hsItems.length;
  document.getElementById("tHs").textContent = hsItems.length;
  document.getElementById("tOk").textContent = okItems.length;

  const bHs = document.getElementById("bHs");
  if(hsItems.length === 0){
    bHs.innerHTML = '<p class="text-slate-500 italic">선택된 질문 항목이 없습니다.</p>';
  } else {
    bHs.innerHTML = hsItems.map((item, idx) => `
      <div class="p-2.5 rounded-lg bg-dark-surface/80 border border-dark-border flex items-start gap-2">
        <span class="w-5 h-5 rounded bg-amber-400/20 text-amber-400 font-mono font-bold text-xs flex items-center justify-center flex-shrink-0">${idx+1}</span>
        <span class="text-slate-200">${item.t}</span>
      </div>
    `).join("");
  }
}

document.getElementById("copyBtn").onclick = () => {
  const hsItems = ITEMS.filter(i => i.state === 'hs').map((item, idx) => `${idx+1}. ${item.t}`).join("\\n");
  navigator.clipboard.writeText(hsItems).then(() => {
    alert("의장님께 전달할 질문지 리스트가 클립보드에 복사되었습니다!");
  });
};

render();
</script>
</body>
</html>
'''

with open('kyerim-checklist.html', 'w', encoding='utf-8') as f:
    f.write(checklist_html)

print("Finished generating new kyerim-checklist.html. Size:", len(checklist_html))
