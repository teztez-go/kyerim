import json, re

with open("work/latest_equipment.json", "r", encoding="utf-8") as f:
    items = json.load(f)

js_items = json.dumps(items, ensure_ascii=False, indent=2)

with open("kyerim-equipment.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace PRESET_GYERIM
html = re.sub(
    r"const PRESET_GYERIM = \[[\s\S]*?\];\s*const STORAGE_KEY",
    f"const PRESET_GYERIM = {js_items};\n\nconst STORAGE_KEY",
    html
)

# 2. Update STORAGE_KEY to v44
html = html.replace('const STORAGE_KEY = "kyerim_equipment_items_v43";', 'const STORAGE_KEY = "kyerim_equipment_items_v44";')

# 3. Update Header Metrics & Badges
html = html.replace('id="headerItemCountText">6개 구역 · 57개 핵심 품목</div>', 'id="headerItemCountText">6개 구역 · 87개 핵심 품목</div>')
html = html.replace('id="headerTotalText">4억 123만원</span>', 'id="headerTotalText">3억 4,735만원</span>')
html = html.replace('id="sumTotal">4억 123만원</div>', 'id="sumTotal">3억 4,735만원</div>')
html = html.replace('id="sumTotalWon">401,228,000원 (1~6구역 전체)</div>', 'id="sumTotalWon">347,354,000원 (1~6구역 전체)</div>')

html = html.replace('id="sumCardio">1억 3,323만원</div>', 'id="sumCardio">1억 3,935만원</div>')
html = html.replace('id="sumXpodium">2억 6,800만원</div>', 'id="sumXpodium">2억 800만원</div>')
html = html.replace('id="sumXpodiumWon">인테리어·건축 2억 1,900만 · 냉난방·설비 4,900만</div>', 'id="sumXpodiumWon">인테리어·건축 1억 6,500만 · 냉난방·설비 4,300만</div>')

html = html.replace('id="itemCountBadge">총 57개 품목</span>', 'id="itemCountBadge">총 87개 품목</span>')

html = html.replace(
    'id="footSplitSub">운동기구·라운지(1~4구역) 1억 3,323만원 + 인테리어·냉난방·설비(5~6구역) 2억 6,800만원 · 사업계획서 실시간 연동</div>',
    'id="footSplitSub">운동기구·라운지(1~4구역) 1억 3,935만원 + 인테리어·냉난방·설비(5~6구역) 2억 800만원 · 사업계획서 실시간 연동</div>'
)

html = html.replace(
    'id="footTotal">\n          4억 123만원 (401,228,000원)\n        </div>',
    'id="footTotal">\n          3억 4,735만원 (347,354,000원)\n        </div>'
)

with open("kyerim-equipment.html", "w", encoding="utf-8") as f:
    f.write(html)

print("kyerim-equipment.html updated successfully!")

# Now update kyerim-plan.html
with open("kyerim-plan.html", "r", encoding="utf-8") as f:
    plan_html = f.read()

plan_html = plan_html.replace(
    "const DEFAULT_EQUIPMENT_TOTAL = 13323; // 1억 3,323만원 (1~4구역)",
    "const DEFAULT_EQUIPMENT_TOTAL = 13935; // 1억 3,935만원 (1~4구역)"
)
plan_html = plan_html.replace(
    "const DEFAULT_INTERIOR_TOTAL = 26800; // 2억 6,800만원 (5~6구역)",
    "const DEFAULT_INTERIOR_TOTAL = 20800; // 2억 800만원 (5~6구역)"
)
plan_html = plan_html.replace(
    'id="capexTotalText">약 4억 123만원</span>',
    'id="capexTotalText">약 3억 4,735만원</span>'
)

with open("kyerim-plan.html", "w", encoding="utf-8") as f:
    f.write(plan_html)

print("kyerim-plan.html updated successfully!")
