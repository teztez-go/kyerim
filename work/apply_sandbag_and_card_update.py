#!/usr/bin/env python3
"""
Apply equipment JSON update with bundled sandbags and replace Metric 4 card.
"""
import json, re

# 1. Load user JSON
from inspect_user_json import items as user_items

# 2. Bundle the 3 sandbag items into 1 item in ROX zone
sandbag_items = [it for it in user_items if "샌드백" in it["name"] and it["zone"] == "ROX"]
sandbag_total_won = sum(it["price"] * it["qty"] for it in sandbag_items)
sandbag_total_qty = sum(it["qty"] for it in sandbag_items)

bundled_sandbag = {
    "id": 1794990691981,
    "zone": "ROX",
    "name": "샌드백 3종 세트 (10kg·20kg·30kg 총 25개)",
    "price": sandbag_total_won,
    "qty": 1,
    "note": "10KG 10개(77만) + 20KG 10개(78만) + 30KG 5개(46.5만) 일괄 세트"
}

final_items = []
inserted_sandbag = False
for it in user_items:
    if "샌드백" in it["name"] and it["zone"] == "ROX":
        if not inserted_sandbag:
            final_items.append(bundled_sandbag)
            inserted_sandbag = True
    else:
        final_items.append(it)

print(f"Total final items: {len(final_items)}")
assert len(final_items) == 85

# Compute totals
EQUIP_ZONES = {'METCON', 'ROX', 'ERG', 'LOUNGE'}
INTERIOR_ZONES = {'INTERIOR', 'MEP'}
equip_won = sum(it['price'] * it['qty'] for it in final_items if it['zone'] in EQUIP_ZONES)
interior_won = sum(it['price'] * it['qty'] for it in final_items if it['zone'] in INTERIOR_ZONES)
total_won = equip_won + interior_won

print(f"Equipment Won: {equip_won:,}")
print(f"Interior Won:  {interior_won:,}")
print(f"Total Won:     {total_won:,}")

# Update kyerim-equipment.html
with open("kyerim-equipment.html", "r", encoding="utf-8") as f:
    eq_html = f.read()

# Replace PRESET_GYERIM
json_str = json.dumps(final_items, ensure_ascii=False, indent=2)
preset_pattern = r'const PRESET_GYERIM = \[.*?\];\n\nconst STORAGE_KEY = "kyerim_equipment_items_v\d+";'
preset_replacement = f'const PRESET_GYERIM = {json_str};\n\nconst STORAGE_KEY = "kyerim_equipment_items_v46";'
assert re.search(preset_pattern, eq_html, re.DOTALL), "Failed to match PRESET_GYERIM in kyerim-equipment.html"
eq_html = re.sub(preset_pattern, preset_replacement, eq_html, flags=re.DOTALL)

# Add purge for legacy equipment keys
if "function purgeLegacyEquipKeys" not in eq_html:
    eq_html = eq_html.replace(
        'const STORAGE_KEY = "kyerim_equipment_items_v46";',
        '''const STORAGE_KEY = "kyerim_equipment_items_v46";

// Purge obsolete cached keys from earlier versions
(function purgeLegacyEquipKeys() {
  const LEGACY_KEYS = [
    "kyerim_equipment_items_v45",
    "kyerim_equipment_items_v43",
    "kyerim_equipment_items_v42",
    "kyerim_equipment_items_v41",
    "kyerim_equipment_items_v2"
  ];
  try {
    LEGACY_KEYS.forEach(k => localStorage.removeItem(k));
  } catch (e) {}
})();'''
    )

# Replace Metric 1 (Total)
eq_html = re.sub(r'id="headerTotalText">.*?</span>', 'id="headerTotalText">3억 4,735만원</span>', eq_html)
eq_html = re.sub(r'id="sumTotal">.*?</div>', 'id="sumTotal">3억 4,735만원</div>', eq_html)
eq_html = re.sub(r'id="sumTotalWon">.*?</div>', 'id="sumTotalWon">347,354,000원 (1~6구역 전체)</div>', eq_html)

# Replace Metric 3 (Interior)
eq_html = re.sub(r'id="sumXpodium">.*?</div>', 'id="sumXpodium">2억 800만원</div>', eq_html)
eq_html = re.sub(r'id="sumXpodiumWon">.*?</div>', 'id="sumXpodiumWon">인테리어·건축 1억 6,500만 · 냉난방·설비 4,300만</div>', eq_html)

# Replace Metric 4 ("감가 방어 75%" -> "230평 실평수 기준 시설단가")
old_metric4 = '''        <!-- Metric 4: Real Asset Preservation & Direct Construction -->
        <div class="rounded-2xl bg-slate-800/70 border border-slate-700/80 p-4 sm:p-5">
          <div class="flex items-center justify-between">
            <span class="text-xs text-slate-400 font-medium">직영 원가 시공 & 실물 자산 보존</span>
            <span class="text-[10px] px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 font-bold">100% 소유</span>
          </div>
          <div class="text-2xl sm:text-3xl font-black text-emerald-400 font-mono tabular-nums mt-1.5">감가 방어 75%+</div>
          <div class="text-xs text-slate-400 mt-1">의장님 건설사 직영 시공 · 공인 장비 높은 중고 가치</div>
        </div>'''

new_metric4 = '''        <!-- Metric 4: Cost per Pyeong (230-pyeong) -->
        <div class="rounded-2xl bg-slate-800/70 border border-slate-700/80 p-4 sm:p-5">
          <div class="flex items-center justify-between">
            <span class="text-xs text-slate-400 font-medium">230평 실평수 기준 시설단가</span>
            <span class="text-[10px] px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 font-bold">원가 직영 시공</span>
          </div>
          <div class="text-2xl sm:text-3xl font-black text-emerald-400 font-mono tabular-nums mt-1.5" id="sumPyeongPrice">평당 약 151만원</div>
          <div class="text-xs text-slate-400 mt-1" id="sumPyeongSub">인테리어 평당 90만 + 기구 평당 61만 (업계 대비 40% 절감)</div>
        </div>'''

assert old_metric4 in eq_html, "Failed to find old Metric 4 card in kyerim-equipment.html"
eq_html = eq_html.replace(old_metric4, new_metric4)

# Replace Footer Text
old_foot = '''        <div class="text-xs text-slate-500 mt-0.5" id="footSplitSub">운동기구·라운지(1~4구역) 1억 3,935만원 + 인테리어·냉난방·설비(5~6구역) 1억 9,540만원 · 사업계획서 실시간 연동</div>
        </div>
        <div class="text-left sm:text-right font-mono text-xl sm:text-2xl font-black text-slate-900 tabular-nums" id="footTotal">
          3억 3,475만원 (334,754,000원)
        </div>'''

new_foot = '''        <div class="text-xs text-slate-500 mt-0.5" id="footSplitSub">운동기구·라운지(1~4구역) 1억 3,935만원 + 인테리어·냉난방·설비(5~6구역) 2억 800만원 · 사업계획서 실시간 연동</div>
        </div>
        <div class="text-left sm:text-right font-mono text-xl sm:text-2xl font-black text-slate-900 tabular-nums" id="footTotal">
          3억 4,735만원 (347,354,000원)
        </div>'''

assert old_foot in eq_html, "Failed to find old footer in kyerim-equipment.html"
eq_html = eq_html.replace(old_foot, new_foot)

# Update updateSummaryCards in kyerim-equipment.html to dynamically calculate sumPyeongPrice
old_summary_code = '''  document.getElementById("sumXpodium").textContent = fmtManwon(interiorMepTotal);
  document.getElementById("sumXpodiumWon").textContent = `인테리어·건축 ${fmtManwon(zoneTotals.INTERIOR)} · 냉난방·설비 ${fmtManwon(zoneTotals.MEP)}`;
}'''

new_summary_code = '''  document.getElementById("sumXpodium").textContent = fmtManwon(interiorMepTotal);
  document.getElementById("sumXpodiumWon").textContent = `인테리어·건축 ${fmtManwon(zoneTotals.INTERIOR)} · 냉난방·설비 ${fmtManwon(zoneTotals.MEP)}`;

  const pyeongTotal = Math.round((total / 230) / 10000);
  const pyeongInterior = Math.round((interiorMepTotal / 230) / 10000);
  const pyeongEquip = Math.round((equipLoungeTotal / 230) / 10000);
  const sumPyeongPriceEl = document.getElementById("sumPyeongPrice");
  if (sumPyeongPriceEl) sumPyeongPriceEl.textContent = `평당 약 ${pyeongTotal}만원`;
  const sumPyeongSubEl = document.getElementById("sumPyeongSub");
  if (sumPyeongSubEl) sumPyeongSubEl.textContent = `인테리어 평당 ${pyeongInterior}만 + 기구 평당 ${pyeongEquip}만 (업계 대비 40% 절감)`;
}'''

assert old_summary_code in eq_html, "Failed to find updateSummaryCards in kyerim-equipment.html"
eq_html = eq_html.replace(old_summary_code, new_summary_code)

with open("kyerim-equipment.html", "w", encoding="utf-8") as f:
    f.write(eq_html)
print("kyerim-equipment.html updated successfully.")


# Update kyerim-plan.html
with open("kyerim-plan.html", "r", encoding="utf-8") as f:
    plan_html = f.read()

# Update DEFAULT_INTERIOR_TOTAL
plan_html = plan_html.replace(
    'const DEFAULT_INTERIOR_TOTAL = 19540; // 1억 9,540만원 (5~6구역)',
    'const DEFAULT_INTERIOR_TOTAL = 20800; // 2억 800만원 (5~6구역)'
)

# Update storage keys & listeners for v46
plan_html = plan_html.replace(
    'const EQUIPMENT_STORAGE_ITEMS_V45 = "kyerim_equipment_items_v45";',
    'const EQUIPMENT_STORAGE_ITEMS_V46 = "kyerim_equipment_items_v46";\nconst EQUIPMENT_STORAGE_ITEMS_V45 = "kyerim_equipment_items_v45";'
)

old_equip_meta_plan = '''function updateEquipmentMeta() {
  const savedV45 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V45);
  const savedV43 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V43);
  const saved = savedV45 || savedV43;'''

new_equip_meta_plan = '''function updateEquipmentMeta() {
  const savedV46 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V46);
  const savedV45 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V45);
  const savedV43 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V43);
  const saved = savedV46 || savedV45 || savedV43;'''

assert old_equip_meta_plan in plan_html, "Failed to find updateEquipmentMeta in kyerim-plan.html"
plan_html = plan_html.replace(old_equip_meta_plan, new_equip_meta_plan)

plan_html = plan_html.replace(
    'if (eqLabelEl) eqLabelEl.textContent = "1~4구역 82개 품목 실시간 연동";',
    'if (eqLabelEl) eqLabelEl.textContent = "1~4구역 80개 품목 실시간 연동";'
)

# Update storage listener in plan_html
plan_html = plan_html.replace(
    'e.key === EQUIPMENT_STORAGE_ITEMS_V45 ||',
    'e.key === EQUIPMENT_STORAGE_ITEMS_V46 ||\n    e.key === EQUIPMENT_STORAGE_ITEMS_V45 ||'
)

# Update initial HTML cards in plan_html
plan_html = plan_html.replace(
    '<span class="text-xl font-black font-mono text-slate-900 tabular-nums" id="capexTotalText">약 3억 3,475만원</span>',
    '<span class="text-xl font-black font-mono text-slate-900 tabular-nums" id="capexTotalText">약 3억 4,735만원</span>'
)

plan_html = plan_html.replace(
    '<span class="text-base font-black font-mono text-slate-900" id="interiorSubtotal">2억 6,800만원</span>',
    '<span class="text-base font-black font-mono text-slate-900" id="interiorSubtotal">2억 800만원</span>'
)

plan_html = plan_html.replace(
    '<span class="text-base font-black font-mono text-slate-900" id="equipmentSubtotal">1억 3,323만원</span>',
    '<span class="text-base font-black font-mono text-slate-900" id="equipmentSubtotal">1억 3,935만원</span>'
)

with open("kyerim-plan.html", "w", encoding="utf-8") as f:
    f.write(plan_html)
print("kyerim-plan.html updated successfully.")
