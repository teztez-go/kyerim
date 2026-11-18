import json
from inspect_user_json import items as user_items

# Bundle the 3 sandbags
new_items = []
sandbag_items = []
for it in user_items:
    if "샌드백" in it["name"] and it["zone"] == "ROX":
        sandbag_items.append(it)
    else:
        new_items.append(it)

sandbag_total_won = sum(it["price"] * it["qty"] for it in sandbag_items)
sandbag_total_qty = sum(it["qty"] for it in sandbag_items)
print(f"Sandbag total: {sandbag_total_won:,}원, qty: {sandbag_total_qty}")

# Find insertion position for bundled sandbag (where sandbags were in ROX)
# In user_items, where was the first sandbag?
first_sandbag_idx = next(i for i, it in enumerate(user_items) if "샌드백" in it["name"])

bundled_sandbag = {
    "id": 1794990691981,
    "zone": "ROX",
    "name": "샌드백 3종 세트 (10kg·20kg·30kg 총 25개)",
    "price": sandbag_total_won,
    "qty": 1,
    "note": "10KG 10개(77만) + 20KG 10개(78만) + 30KG 5개(46.5만) 일괄 세트"
}

# Insert bundled sandbag into new_items
# Let's see the ROX items order
rox_idx = next(i for i, it in enumerate(new_items) if it["zone"] == "ROX")
# Let's insert where sandbags were
final_items = []
inserted = False
for it in user_items:
    if "샌드백" in it["name"] and it["zone"] == "ROX":
        if not inserted:
            final_items.append(bundled_sandbag)
            inserted = True
    else:
        final_items.append(it)

print(f"Final items count: {len(final_items)}")

# Calculate totals
EQUIP_ZONES = {'METCON', 'ROX', 'ERG', 'LOUNGE'}
INTERIOR_ZONES = {'INTERIOR', 'MEP'}

equip_won = sum(it['price'] * it['qty'] for it in final_items if it['zone'] in EQUIP_ZONES)
interior_won = sum(it['price'] * it['qty'] for it in final_items if it['zone'] in INTERIOR_ZONES)
total_won = equip_won + interior_won

print(f"Equipment total: {equip_won:,}원 ({round(equip_won/10000):,}만원)")
print(f"Interior total:  {interior_won:,}원 ({round(interior_won/10000):,}만원)")
print(f"Total CAPEX:     {total_won:,}원 ({round(total_won/10000):,}만원)")

pyeong = 230
print(f"평당 총액: {round(total_won / pyeong):,}원 (평당 약 {round((total_won / pyeong) / 10000, 1)}만원)")
print(f"평당 인테리어: {round(interior_won / pyeong):,}원 (평당 약 {round((interior_won / pyeong) / 10000, 1)}만원)")
print(f"평당 기구: {round(equip_won / pyeong):,}원 (평당 약 {round((equip_won / pyeong) / 10000, 1)}만원)")
