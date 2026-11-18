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

# 2. Update STORAGE_KEY to v45
html = re.sub(r'const STORAGE_KEY = "kyerim_equipment_items_v\d+";', 'const STORAGE_KEY = "kyerim_equipment_items_v45";', html)

# 3. Update Header Metrics & Badges
html = re.sub(r'id="headerItemCountText">.*?</div>', 'id="headerItemCountText">6개 구역 · 87개 핵심 품목</div>', html)
html = re.sub(r'id="headerTotalText">.*?</span>', 'id="headerTotalText">3억 3,475만원</span>', html)
html = re.sub(r'id="sumTotal">.*?</div>', 'id="sumTotal">3억 3,475만원</div>', html)
html = re.sub(r'id="sumTotalWon">.*?</div>', 'id="sumTotalWon">334,754,000원 (1~6구역 전체)</div>', html)

html = re.sub(r'id="sumCardio">.*?</div>', 'id="sumCardio">1억 3,935만원</div>', html)
html = re.sub(r'id="sumXpodium">.*?</div>', 'id="sumXpodium">1억 9,540만원</div>', html)
html = re.sub(r'id="sumXpodiumWon">.*?</div>', 'id="sumXpodiumWon">인테리어·건축 1억 6,500만 · 냉난방·설비 3,040만</div>', html)

html = re.sub(r'id="itemCountBadge">.*?</span>', 'id="itemCountBadge">총 87개 품목</span>', html)

html = re.sub(
    r'id="footSplitSub">.*?</div>',
    'id="footSplitSub">운동기구·라운지(1~4구역) 1억 3,935만원 + 인테리어·냉난방·설비(5~6구역) 1억 9,540만원 · 사업계획서 실시간 연동</div>',
    html
)

html = re.sub(
    r'id="footTotal">[\s\S]*?</div>',
    'id="footTotal">\n          3억 3,475만원 (334,754,000원)\n        </div>',
    html
)

with open("kyerim-equipment.html", "w", encoding="utf-8") as f:
    f.write(html)

print("kyerim-equipment.html updated successfully!")

# Now update kyerim-plan.html
with open("kyerim-plan.html", "r", encoding="utf-8") as f:
    plan_html = f.read()

plan_html = re.sub(
    r"const DEFAULT_EQUIPMENT_TOTAL = \d+;.*",
    "const DEFAULT_EQUIPMENT_TOTAL = 13935; // 1억 3,935만원 (1~4구역)",
    plan_html
)
plan_html = re.sub(
    r"const DEFAULT_INTERIOR_TOTAL = \d+;.*",
    "const DEFAULT_INTERIOR_TOTAL = 19540; // 1억 9,540만원 (5~6구역)",
    plan_html
)
plan_html = re.sub(
    r'id="capexTotalText">.*?</span>',
    'id="capexTotalText">약 3억 3,475만원</span>',
    plan_html
)

with open("kyerim-plan.html", "w", encoding="utf-8") as f:
    f.write(plan_html)

print("kyerim-plan.html updated successfully!")
