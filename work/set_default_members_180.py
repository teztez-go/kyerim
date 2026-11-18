#!/usr/bin/env python3
"""
Set 180 as default members count across kyerim-plan.html:
- Update initial HTML hero basis text and KPI formulas to 180.
- Update preset chips: 150명 (보수), 180명 (기본), 210명 (성장), 240명 (만실).
- In loadState, ensure 180 is loaded and any legacy cached 150 is migrated to 180.
- In purgeLegacyKeys, remove cached 150.
"""

with open("kyerim-plan.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hero basis text
old_hero = '<span>기준 시나리오: <strong class="text-white font-mono" id="heroBasisText">150명 · 월 17만원</strong></span>'
new_hero = '<span>기준 시나리오: <strong class="text-white font-mono" id="heroBasisText">180명 · 월 17만원</strong></span>'
assert old_hero in html, "Failed to find old hero basis text"
html = html.replace(old_hero, new_hero)

# 2. Preset chips
old_chips = '''        <div class="flex items-center justify-between gap-1 pt-0.5">
          <button type="button" data-member-preset="150" class="preset-chip px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">150명 (기본)</button>
          <button type="button" data-member-preset="180" class="preset-chip active px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">180명 (목표)</button>
          <button type="button" data-member-preset="210" class="preset-chip px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">210명 (성장)</button>
          <button type="button" data-member-preset="240" class="preset-chip px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">240명 (만실)</button>
        </div>'''

new_chips = '''        <div class="flex items-center justify-between gap-1 pt-0.5">
          <button type="button" data-member-preset="150" class="preset-chip px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">150명 (보수)</button>
          <button type="button" data-member-preset="180" class="preset-chip active px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">180명 (기본)</button>
          <button type="button" data-member-preset="210" class="preset-chip px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">210명 (성장)</button>
          <button type="button" data-member-preset="240" class="preset-chip px-2 py-1 rounded-md text-[11px] font-mono font-medium bg-white border border-slate-200 text-slate-600 hover:border-slate-400 transition">240명 (만실)</button>
        </div>'''
assert old_chips in html, "Failed to find old preset chips"
html = html.replace(old_chips, new_chips)

# 3. KPI Revenue formula and revenue
old_kpi_rev = '''            <span class="text-[11px] text-slate-400 font-mono" id="kpiRevenueFormula">150명 × 17.0만원</span>
          </div>
          <div class="text-2xl sm:text-3xl font-black font-mono text-slate-900 tabular-nums mt-2" id="kpiRevenue">2,550만원</div>'''

new_kpi_rev = '''            <span class="text-[11px] text-slate-400 font-mono" id="kpiRevenueFormula">180명 × 17.0만원</span>
          </div>
          <div class="text-2xl sm:text-3xl font-black font-mono text-slate-900 tabular-nums mt-2" id="kpiRevenue">3,060만원</div>'''
assert old_kpi_rev in html, "Failed to find old KPI revenue formula"
html = html.replace(old_kpi_rev, new_kpi_rev)

# 4. Principle card 1 summary label & slider labels
old_c1 = '''          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-800">회원 수 연동 시뮬레이션</span>
            <span class="font-mono font-black text-sm text-slate-900" id="card1SummaryLabel">150명 · 순수익 1,783만원</span>
          </div>
          <input type="range" id="card1RangeMembers" min="40" max="250" step="5" value="180" class="w-full h-1.5 bg-slate-200 rounded-lg appearance-none cursor-pointer">
          <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>40명</span>
            <span>150명 (기본)</span>
            <span>180명 (목표)</span>
            <span>240명 (만실)</span>
          </div>'''

new_c1 = '''          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-800">회원 수 연동 시뮬레이션</span>
            <span class="font-mono font-black text-sm text-slate-900" id="card1SummaryLabel">180명 · 순수익 1,476만원</span>
          </div>
          <input type="range" id="card1RangeMembers" min="40" max="250" step="5" value="180" class="w-full h-1.5 bg-slate-200 rounded-lg appearance-none cursor-pointer">
          <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>40명</span>
            <span>150명 (보수)</span>
            <span>180명 (기본)</span>
            <span>240명 (만실)</span>
          </div>'''
assert old_c1 in html, "Failed to find old card1 summary"
html = html.replace(old_c1, new_c1)

# 5. Purge cached 150 in purgeLegacyKeys
old_purge = '''    const oldTot = localStorage.getItem("kyerim_opex_total_v2");
    if (oldTot && Number(oldTot) < 1000) {
      localStorage.removeItem("kyerim_opex_total_v2");
    }'''

new_purge = '''    const oldTot = localStorage.getItem("kyerim_opex_total_v2");
    if (oldTot && Number(oldTot) < 1000) {
      localStorage.removeItem("kyerim_opex_total_v2");
    }
    const oldMem = localStorage.getItem("kyerim_plan_members");
    if (oldMem === "150") {
      localStorage.removeItem("kyerim_plan_members");
    }'''
assert old_purge in html, "Failed to find old purge block"
html = html.replace(old_purge, new_purge)

# 6. In loadState, migrate 150 to 180
old_load = '''function loadState() {
  const m = localStorage.getItem(KEY_MEMBERS);
  const p = localStorage.getItem(KEY_PRICE);
  const s = localStorage.getItem(KEY_SHARE_PCT);
  const o = getSavedOpex();

  inMembers.value = m !== null ? m : DEFAULT_MEMBERS;
  rngMembers.value = inMembers.value;'''

new_load = '''function loadState() {
  const m = localStorage.getItem(KEY_MEMBERS);
  const p = localStorage.getItem(KEY_PRICE);
  const s = localStorage.getItem(KEY_SHARE_PCT);
  const o = getSavedOpex();

  let finalMembers = m !== null ? Number(m) : DEFAULT_MEMBERS;
  if (finalMembers === 150) finalMembers = DEFAULT_MEMBERS; // migrate legacy 150 to default 180
  inMembers.value = finalMembers;
  rngMembers.value = inMembers.value;'''
assert old_load in html, "Failed to find old loadState"
html = html.replace(old_load, new_load)

# 7. Scenario table label
old_scen = '''    { label: "기본 기준", badge: "기본 안", m: 150 },
    { label: "기본 목표", badge: "핵심 타깃", m: 180, isTarget: true },'''

new_scen = '''    { label: "보수 안착", badge: "보수 기준", m: 150 },
    { label: "기본 목표", badge: "기본 기준", m: 180, isTarget: true },'''
assert old_scen in html, "Failed to find old scenario labels"
html = html.replace(old_scen, new_scen)

with open("kyerim-plan.html", "w", encoding="utf-8") as f:
    f.write(html)
print("kyerim-plan.html updated with 180 default members.")
