# -*- coding: utf-8 -*-
import re

with open('work/plan.svg', 'r', encoding='utf-8') as f:
    master_svg = f.read()

embedded_svg = master_svg.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400"', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 400" class="w-full h-auto max-h-[520px] mx-auto select-none"')

with open('kyerim-internal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Section #space
new_space_section = f'''  <!-- Space & SVG Plan -->
  <section id="space" class="space-y-4">
    <div class="border-b border-dark-border pb-3 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
      <div>
        <div class="text-xs font-bold text-brand-500 uppercase tracking-widest font-mono">Floor Plan & Zoning Masterplan</div>
        <h2 class="text-xl sm:text-2xl font-bold text-white mt-1">지하 230평 구역별 레이아웃 구상도 (혁신 마스터플랜)</h2>
        <p class="text-xs sm:text-sm text-slate-400 mt-0.5">사선 벽 쪽 Hyb 존(하이록스 30m 듀얼 런웨이)과 중앙 Met 존(크로스핏 85평) · 16m 아레나 리그를 동측 벽체에 직결하여 230평 전체 개방감을 극대화했습니다.</p>
      </div>
      <div class="flex items-center gap-2">
        <span class="px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 text-xs font-bold font-mono">HYB 75평</span>
        <span class="px-2.5 py-1 rounded-lg bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 text-xs font-bold font-mono">MET 85평</span>
        <span class="px-2.5 py-1 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/30 text-xs font-bold font-mono">라운지·락커 59평</span>
      </div>
    </div>

    <div class="bg-dark-card border border-dark-border rounded-2xl p-4 sm:p-6 overflow-hidden">
      {embedded_svg}
    </div>
  </section>'''

html = re.sub(r'  <!-- Space & SVG Plan -->.*?  <!-- 11 Step Meeting Questions -->', new_space_section + '\n\n  <!-- 11 Step Meeting Questions -->', html, flags=re.S)

with open('kyerim-internal.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated kyerim-internal.html successfully! Total length:", len(html))
