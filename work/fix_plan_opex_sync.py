#!/usr/bin/env python3
"""
Fix OPEX discrepancy between kyerim-plan.html and kyerim-opex.html:
1. Purge legacy obsolete keys (v7, v6, v5, v4, etc.) on load.
2. Update OPEX sync storage key to v3 in both plan and opex files.
3. Fix updateOpexMeta() to check kyerim_opex_items_v8 instead of obsolete keys.
4. Update fallback static HTML labels from 608만/159만 (767만) to 1,116.3만/467.4만 (1,584만).
5. Update equipment sync key in kyerim-plan to v45.
"""

def update_plan():
    with open("kyerim-plan.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update fallback HTML sub labels
    old_sublabels = '''        <div class="flex justify-between text-[11px] text-slate-500 font-mono pt-0.5" id="opexBreakdownText">
          <span id="opexLaborSubLabel">인건비 약 608만</span>
          <span id="opexOpsSubLabel">공과금·관리비 약 159만</span>
        </div>'''
    
    new_sublabels = '''        <div class="flex justify-between text-[11px] text-slate-500 font-mono pt-0.5" id="opexBreakdownText">
          <span id="opexLaborSubLabel">인건비 약 1,116.3만</span>
          <span id="opexOpsSubLabel">관리·공과금 약 467.4만</span>
        </div>'''
    
    assert old_sublabels in html, "Failed to find old sublabels in kyerim-plan.html"
    html = html.replace(old_sublabels, new_sublabels)

    # 2. Update storage keys definition & add legacy key purge
    old_storage_keys = '''// LocalStorage Keys for Persistence & Cross-Page Sync
const KEY_MEMBERS = "kyerim_plan_members";
const KEY_PRICE = "kyerim_plan_price";
const KEY_OPEX = "kyerim_plan_opex_custom";
const KEY_SHARE_PCT = "kyerim_plan_share_pct";
const OPEX_STORAGE_TOTAL = "kyerim_opex_total_v2";

const EQUIPMENT_STORAGE_TOTAL_V2 = "kyerim_equipment_total_v2";
const EQUIPMENT_STORAGE_ITEMS_V2 = "kyerim_equipment_items_v2";
const EQUIPMENT_STORAGE_ITEMS_V43 = "kyerim_equipment_items_v43";
const EQUIPMENT_STORAGE_TOTAL_V1 = "kyerim_equipment_total_v1";
const INTERIOR_STORAGE_TOTAL_V2 = "kyerim_interior_total_v2";'''

    new_storage_keys = '''// LocalStorage Keys for Persistence & Cross-Page Sync
// Purge obsolete cached keys from earlier versions so stale OPEX (767만원) never pollutes calculations
(function purgeLegacyKeys() {
  const LEGACY_KEYS = [
    "kyerim_opex_items_v7",
    "kyerim_opex_items_v6",
    "kyerim_opex_items_v5",
    "kyerim_opex_items_v4",
    "kyerim_opex_items_v3",
    "kyerim_opex_items_v2",
    "kyerim_opex_items_v1",
    "kyerim_opex_total_v1",
    "kyerim_plan_opex_custom"
  ];
  try {
    LEGACY_KEYS.forEach(k => localStorage.removeItem(k));
    const oldTot = localStorage.getItem("kyerim_opex_total_v2");
    if (oldTot && Number(oldTot) < 1000) {
      localStorage.removeItem("kyerim_opex_total_v2");
    }
  } catch (e) {}
})();

const KEY_MEMBERS = "kyerim_plan_members";
const KEY_PRICE = "kyerim_plan_price";
const KEY_SHARE_PCT = "kyerim_plan_share_pct";
const OPEX_STORAGE_TOTAL = "kyerim_opex_total_v3";
const OPEX_STORAGE_ITEMS = "kyerim_opex_items_v8";

const EQUIPMENT_STORAGE_TOTAL_V2 = "kyerim_equipment_total_v2";
const EQUIPMENT_STORAGE_ITEMS_V45 = "kyerim_equipment_items_v45";
const EQUIPMENT_STORAGE_ITEMS_V43 = "kyerim_equipment_items_v43";
const EQUIPMENT_STORAGE_ITEMS_V2 = "kyerim_equipment_items_v2";
const EQUIPMENT_STORAGE_TOTAL_V1 = "kyerim_equipment_total_v1";
const INTERIOR_STORAGE_TOTAL_V2 = "kyerim_interior_total_v2";'''

    assert old_storage_keys in html, "Failed to find old storage keys in kyerim-plan.html"
    html = html.replace(old_storage_keys, new_storage_keys)

    # 3. Update getSavedOpex & updateOpexMeta
    old_opex_funcs = '''function getSavedOpex() {
  const opexFromTable = localStorage.getItem(OPEX_STORAGE_TOTAL);
  if (opexFromTable && !isNaN(Number(opexFromTable))) {
    let val = Number(opexFromTable);
    if (val > 100000) val = Math.round(val / 10000);
    if (val >= 1000) return val; // valid if updated
  }
  return DEFAULT_OPEX;
}

function updateOpexMeta() {
  const CANDIDATE_KEYS = [
    "kyerim_opex_items_v7",
    "kyerim_opex_items_v6",
    "kyerim_opex_items_v5",
    "kyerim_opex_items_v4"
  ];
  let laborWon = 0;
  let opsWon = 0;
  let found = false;

  for (const k of CANDIDATE_KEYS) {
    const raw = localStorage.getItem(k);
    if (raw) {
      try {
        const items = JSON.parse(raw);
        if (Array.isArray(items) && items.length > 0) {
          items.forEach(it => {
            let rowTotal = 0;
            if (it.name.includes("금융이자") || it.isLoan) {
              rowTotal = Math.round(Number(it.price || 0) * (Number(it.qty || 0) / 100) / 12);
            } else if (it.name.includes("사업주공과세") || it.isOwnerTax) {
              rowTotal = Number(it.price || 0);
            } else {
              rowTotal = Number(it.price || 0) * Number(it.qty || 0);
            }

            const isLabor = it.category === 'labor' || (!it.category && (
              it.name.includes("기본급") || it.name.includes("퇴직금") || 
              it.name.includes("수당") || it.name.includes("4대보험") || 
              it.name.includes("소득세") || it.name.includes("코치") || it.name.includes("인건비")
            ));

            if (isLabor) laborWon += rowTotal;
            else opsWon += rowTotal;
          });
          found = true;
          break;
        }
      } catch (e) {}
    }
  }

  const laborEl = document.getElementById("opexLaborSubLabel");
  const opsEl = document.getElementById("opexOpsSubLabel");

  if (found && (laborWon > 0 || opsWon > 0)) {
    const laborMan = (laborWon / 10000).toFixed(1);
    const opsMan = (opsWon / 10000).toFixed(1);
    if (laborEl) laborEl.textContent = `인건비 약 ${laborMan}만`;
    if (opsEl) opsEl.textContent = `공과금·관리비 약 ${opsMan}만`;
    const totalMan = Math.round((laborWon + opsWon) / 10000);
    inOpex.value = totalMan;
    rngOpex.value = totalMan;
  } else {
    if (laborEl) laborEl.textContent = "인건비 약 608만";
    if (opsEl) opsEl.textContent = "공과금·관리비 약 159만";
    inOpex.value = getSavedOpex();
    rngOpex.value = inOpex.value;
  }
}'''

    new_opex_funcs = '''function getSavedOpex() {
  const opexFromTable = localStorage.getItem(OPEX_STORAGE_TOTAL) || localStorage.getItem("kyerim_opex_total_v2");
  if (opexFromTable && !isNaN(Number(opexFromTable))) {
    let val = Number(opexFromTable);
    if (val > 100000) val = Math.round(val / 10000);
    if (val >= 1000) return val; // valid if >= 1,000만원
  }
  return DEFAULT_OPEX;
}

function updateOpexMeta() {
  const CANDIDATE_KEYS = [
    "kyerim_opex_items_v8"
  ];
  let laborWon = 0;
  let opsWon = 0;
  let found = false;

  for (const k of CANDIDATE_KEYS) {
    const raw = localStorage.getItem(k);
    if (raw) {
      try {
        const items = JSON.parse(raw);
        if (Array.isArray(items) && items.length > 0) {
          items.forEach(it => {
            let rowTotal = 0;
            if (it.name && (it.name.includes("금융이자") || it.isLoan)) {
              rowTotal = Math.round(Number(it.price || 0) * (Number(it.qty || 0) / 100) / 12);
            } else if (it.name && (it.name.includes("사업주공과세") || it.isOwnerTax)) {
              rowTotal = Number(it.price || 0);
            } else {
              rowTotal = Number(it.price || 0) * Number(it.qty || 0);
            }

            const isLabor = it.category === 'labor' || (!it.category && (
              it.name.includes("기본급") || it.name.includes("퇴직금") || 
              it.name.includes("수당") || it.name.includes("4대보험") || 
              it.name.includes("소득세") || it.name.includes("코치") || it.name.includes("인건비")
            ));

            if (isLabor) laborWon += rowTotal;
            else opsWon += rowTotal;
          });
          found = true;
          break;
        }
      } catch (e) {}
    }
  }

  const laborEl = document.getElementById("opexLaborSubLabel");
  const opsEl = document.getElementById("opexOpsSubLabel");

  if (found && (laborWon > 0 || opsWon > 0)) {
    const laborMan = (laborWon / 10000).toFixed(1);
    const opsMan = (opsWon / 10000).toFixed(1);
    if (laborEl) laborEl.textContent = `인건비 약 ${laborMan}만`;
    if (opsEl) opsEl.textContent = `관리·공과금 약 ${opsMan}만`;
    const totalMan = Math.round((laborWon + opsWon) / 10000);
    inOpex.value = totalMan;
    rngOpex.value = totalMan;
  } else {
    if (laborEl) laborEl.textContent = "인건비 약 1,116.3만";
    if (opsEl) opsEl.textContent = "관리·공과금 약 467.4만";
    inOpex.value = getSavedOpex();
    rngOpex.value = inOpex.value;
  }
}'''

    assert old_opex_funcs in html, "Failed to find old opex funcs in kyerim-plan.html"
    html = html.replace(old_opex_funcs, new_opex_funcs)

    # 4. Update updateEquipmentMeta to check v45
    old_equip_meta = '''function updateEquipmentMeta() {
  const savedV43 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V43);
  const savedV2 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V2);
  const eqLabelEl = document.getElementById("equipmentCountLabel");
  const intLabelEl = document.getElementById("interiorCountLabel");
  if (savedV43) {
    try {
      const items = JSON.parse(savedV43);
      if (Array.isArray(items) && items.length > 0) {
        const intCount = items.filter(it => it.zone === 'INTERIOR' || it.zone === 'MEP').length;
        const eqCount = items.length - intCount;
        if (eqLabelEl) eqLabelEl.textContent = `1~4구역 ${eqCount}개 품목 실시간 연동`;
        if (intLabelEl) intLabelEl.textContent = `5~6구역 ${intCount}개 품목 실시간 연동`;
        return;
      }
    } catch (e) {}
  }
  if (savedV2 && eqLabelEl) {
    try {
      const items = JSON.parse(savedV2);
      if (Array.isArray(items) && items.length > 0) {
        eqLabelEl.textContent = `총 ${items.length}개 핵심 품목 실견적 연동`;
        return;
      }
    } catch (e) {}
  }
  if (eqLabelEl) eqLabelEl.textContent = "1~4구역 실견적 실시간 연동";
  if (intLabelEl) intLabelEl.textContent = "5~6구역 실견적 실시간 연동";
}'''

    new_equip_meta = '''function updateEquipmentMeta() {
  const savedV45 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V45);
  const savedV43 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V43);
  const saved = savedV45 || savedV43;
  const eqLabelEl = document.getElementById("equipmentCountLabel");
  const intLabelEl = document.getElementById("interiorCountLabel");
  if (saved) {
    try {
      const items = JSON.parse(saved);
      if (Array.isArray(items) && items.length > 0) {
        const intCount = items.filter(it => it.zone === 'INTERIOR' || it.zone === 'MEP').length;
        const eqCount = items.length - intCount;
        if (eqLabelEl) eqLabelEl.textContent = `1~4구역 ${eqCount}개 품목 실시간 연동`;
        if (intLabelEl) intLabelEl.textContent = `5~6구역 ${intCount}개 품목 실시간 연동`;
        return;
      }
    } catch (e) {}
  }
  const savedV2 = localStorage.getItem(EQUIPMENT_STORAGE_ITEMS_V2);
  if (savedV2 && eqLabelEl) {
    try {
      const items = JSON.parse(savedV2);
      if (Array.isArray(items) && items.length > 0) {
        eqLabelEl.textContent = `총 ${items.length}개 핵심 품목 실견적 연동`;
        return;
      }
    } catch (e) {}
  }
  if (eqLabelEl) eqLabelEl.textContent = "1~4구역 82개 품목 실시간 연동";
  if (intLabelEl) intLabelEl.textContent = "5~6구역 5개 품목 실시간 연동";
}'''

    assert old_equip_meta in html, "Failed to find old updateEquipmentMeta in kyerim-plan.html"
    html = html.replace(old_equip_meta, new_equip_meta)

    # 5. Update storage event listener
    old_storage_event = '''window.addEventListener('storage', e => {
  if (
    e.key === OPEX_STORAGE_TOTAL ||
    e.key === "kyerim_opex_items_v7" ||
    e.key === "kyerim_opex_items_v6" ||
    e.key === "kyerim_opex_items_v5" ||
    e.key === EQUIPMENT_STORAGE_TOTAL_V2 ||
    e.key === INTERIOR_STORAGE_TOTAL_V2 ||
    e.key === EQUIPMENT_STORAGE_ITEMS_V43 ||
    e.key === EQUIPMENT_STORAGE_ITEMS_V2 ||
    e.key === EQUIPMENT_STORAGE_TOTAL_V1
  ) {
    updateOpexMeta();
    updateEquipmentMeta();
    calculate();
  }
});'''

    new_storage_event = '''window.addEventListener('storage', e => {
  if (
    e.key === OPEX_STORAGE_TOTAL ||
    e.key === "kyerim_opex_total_v2" ||
    e.key === "kyerim_opex_items_v8" ||
    e.key === EQUIPMENT_STORAGE_TOTAL_V2 ||
    e.key === INTERIOR_STORAGE_TOTAL_V2 ||
    e.key === EQUIPMENT_STORAGE_ITEMS_V45 ||
    e.key === EQUIPMENT_STORAGE_ITEMS_V43 ||
    e.key === EQUIPMENT_STORAGE_ITEMS_V2 ||
    e.key === EQUIPMENT_STORAGE_TOTAL_V1
  ) {
    updateOpexMeta();
    updateEquipmentMeta();
    calculate();
  }
});'''

    assert old_storage_event in html, "Failed to find old storage event in kyerim-plan.html"
    html = html.replace(old_storage_event, new_storage_event)

    with open("kyerim-plan.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("kyerim-plan.html updated successfully.")


def update_opex():
    with open("kyerim-opex.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update TOTAL_STORAGE_KEY
    old_keys = '''const STORAGE_KEY = "kyerim_opex_items_v8";
const TOTAL_STORAGE_KEY = "kyerim_opex_total_v2";'''

    new_keys = '''const STORAGE_KEY = "kyerim_opex_items_v8";
const TOTAL_STORAGE_KEY = "kyerim_opex_total_v3";

// Purge obsolete cached keys from earlier versions
(function purgeLegacyKeys() {
  const LEGACY_KEYS = [
    "kyerim_opex_items_v7",
    "kyerim_opex_items_v6",
    "kyerim_opex_items_v5",
    "kyerim_opex_items_v4",
    "kyerim_opex_items_v3",
    "kyerim_opex_items_v2",
    "kyerim_opex_items_v1",
    "kyerim_opex_total_v1"
  ];
  try {
    LEGACY_KEYS.forEach(k => localStorage.removeItem(k));
  } catch (e) {}
})();'''

    assert old_keys in html, "Failed to find old storage keys in kyerim-opex.html"
    html = html.replace(old_keys, new_keys)

    # 2. In saveData, save both total v3 and total v2 (for backward compat)
    old_save = '''function saveData() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
  const totalWon = calculateTotal();
  const totalManwon = Math.round(totalWon / 10000);
  localStorage.setItem(TOTAL_STORAGE_KEY, totalManwon);
  showSaveIndicator();
}'''

    new_save = '''function saveData() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
  const totalWon = calculateTotal();
  const totalManwon = Math.round(totalWon / 10000);
  localStorage.setItem(TOTAL_STORAGE_KEY, totalManwon);
  localStorage.setItem("kyerim_opex_total_v2", totalManwon);
  showSaveIndicator();
}'''

    assert old_save in html, "Failed to find old saveData in kyerim-opex.html"
    html = html.replace(old_save, new_save)

    with open("kyerim-opex.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("kyerim-opex.html updated successfully.")


if __name__ == "__main__":
    update_plan()
    update_opex()
