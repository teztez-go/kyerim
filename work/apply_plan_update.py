with open("kyerim-plan.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update DEFAULT_OPEX
html = html.replace("const DEFAULT_OPEX = 767;", "const DEFAULT_OPEX = 1584;")

# 2. Update inputOpex and rangeOpex
html = html.replace('id="inputOpex" readonly value="767"', 'id="inputOpex" readonly value="1584"')
html = html.replace('id="rangeOpex" min="400" max="1500" step="5" value="767"', 'id="rangeOpex" min="500" max="2500" step="5" value="1584"')

# 3. Update static labels
html = html.replace('id="kpiOpex">−767만원</div>', 'id="kpiOpex">−1,584만원</div>')
html = html.replace('id="wfOpexTxt">767만원</strong>', 'id="wfOpexTxt">1,584만원</strong>')
html = html.replace('실운영비(767만원)', '실운영비(1,584만원)')
html = html.replace('id="heroNetSub">매출 2,550만 − 실운영비 767만</div>', 'id="heroNetSub">매출 3,060만 − 실운영비 1,584만</div>')

# 4. In getSavedOpex(), ensure v8 takes precedence or fallback to DEFAULT_OPEX (1584)
# Let us check getSavedOpex function in kyerim-plan.html
old_get_opex = """function getSavedOpex() {
  const opexFromTable = localStorage.getItem(OPEX_STORAGE_TOTAL);
  if (opexFromTable && !isNaN(Number(opexFromTable))) {
    let val = Number(opexFromTable);
    if (val > 100000) val = Math.round(val / 10000);
    return val;
  }
  return DEFAULT_OPEX;
}"""

new_get_opex = """function getSavedOpex() {
  const opexFromTable = localStorage.getItem(OPEX_STORAGE_TOTAL);
  if (opexFromTable && !isNaN(Number(opexFromTable))) {
    let val = Number(opexFromTable);
    if (val > 100000) val = Math.round(val / 10000);
    if (val >= 1000) return val; // valid if updated
  }
  return DEFAULT_OPEX;
}"""

if old_get_opex in html:
    html = html.replace(old_get_opex, new_get_opex)

with open("kyerim-plan.html", "w", encoding="utf-8") as f:
    f.write(html)

print("kyerim-plan.html updated successfully!")
