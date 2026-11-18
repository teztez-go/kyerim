import json, re

with open("latest_items.json", "r", encoding="utf-8") as f:
    items = json.load(f)

js_items = json.dumps(items, ensure_ascii=False, indent=2)

with open("kyerim-opex.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace DEFAULT_OPEX
html = re.sub(
    r"const DEFAULT_OPEX = \[[\s\S]*?\];\s*const STORAGE_KEY",
    f"const DEFAULT_OPEX = {js_items};\n\nconst STORAGE_KEY",
    html
)

# 2. Update STORAGE_KEY to v8
html = html.replace('const STORAGE_KEY = "kyerim_opex_items_v7";', 'const STORAGE_KEY = "kyerim_opex_items_v8";')

# 3. Update loadData candidate keys logic
old_load = """function loadData() {
  const CANDIDATE_KEYS = [
    STORAGE_KEY,
    "kyerim_opex_items_v6",
    "kyerim_opex_items_v5",
    "kyerim_opex_items_v4",
    "kyerim_opex_items_v3",
    "kyerim_opex_items_v2"
  ];

  let saved = null;
  for (const k of CANDIDATE_KEYS) {
    const val = localStorage.getItem(k);
    if (val) {
      saved = val;
      break;
    }
  }"""

new_load = """function loadData() {
  const saved = localStorage.getItem(STORAGE_KEY);"""

if old_load in html:
    html = html.replace(old_load, new_load)
else:
    print("WARNING: old_load not found exactly")

# 4. Update Header Metrics & Badges
html = html.replace('id="cardTotalBadge">21개 항목</span>', 'id="cardTotalBadge">23개 항목</span>')
html = html.replace('id="sumTotal">7,670,490원</div>', 'id="sumTotal">15,836,850원</div>')
html = html.replace('id="sumTotalSub">약 767만원 · 매출에서 우선 공제</div>', 'id="sumTotalSub">약 1,584만원 · 매출에서 우선 공제</div>')

html = html.replace('id="cardLaborBadge">8개 항목</span>', 'id="cardLaborBadge">9개 항목</span>')
html = html.replace('id="sumLabor">6,083,450원</div>', 'id="sumLabor">11,162,910원</div>')
html = html.replace('id="sumLaborSub">약 608.3만원 (79.3%)</div>', 'id="sumLaborSub">약 1,116.3만원 (70.5%)</div>')

html = html.replace('id="cardOpsBadge">13개 항목</span>', 'id="cardOpsBadge">14개 항목</span>')
html = html.replace('id="sumOps">1,587,040원</div>', 'id="sumOps">4,673,940원</div>')
html = html.replace('id="sumOpsSub">약 158.7만원 (20.7%)</div>', 'id="sumOpsSub">약 467.4만원 (29.5%)</div>')

html = html.replace('id="tableHeaderBadge">2대 카테고리 (21개 항목)</span>', 'id="tableHeaderBadge">2대 카테고리 (23개 항목)</span>')

html = html.replace('id="btnFilterAllCount">21개</span> · <span id="btnFilterAllSum">767만</span>', 'id="btnFilterAllCount">23개</span> · <span id="btnFilterAllSum">1584만</span>')
html = html.replace('id="btnFilterLaborCount">8개</span> · <span id="btnFilterLaborSum">608.3만</span>', 'id="btnFilterLaborCount">9개</span> · <span id="btnFilterLaborSum">1116.3만</span>')
html = html.replace('id="btnFilterOpsCount">13개</span> · <span id="btnFilterOpsSum">158.7만</span>', 'id="btnFilterOpsCount">14개</span> · <span id="btnFilterOpsSum">467.4만</span>')

html = html.replace('id="footSummaryLabor">6,083,450원</span>', 'id="footSummaryLabor">11,162,910원</span>')
html = html.replace('id="footSummaryOps">1,587,040원</span>', 'id="footSummaryOps">4,673,940원</span>')
html = html.replace('id="footSummarySum">\n              7,670,490원\n            </td>', 'id="footSummarySum">\n              15,836,850원\n            </td>')
html = html.replace('id="footTotal">\n              7,670,490원\n            </td>', 'id="footTotal">\n              15,836,850원\n            </td>')
html = html.replace('id="footTotalSub">\n              (약 767만원 · 계산기 및 대시보드에 실시간 자동 반영)', 'id="footTotalSub">\n              (약 1,584만원 · 계산기 및 대시보드에 실시간 자동 반영)')

# 5. Remove temporary export box code
html = re.sub(r"// Temporary export helper[\s\S]*?\}\)\(\);\s*", "", html)

with open("kyerim-opex.html", "w", encoding="utf-8") as f:
    f.write(html)

print("kyerim-opex.html updated successfully!")
