# -*- coding: utf-8 -*-
"""
Refine Mobile View:
1. Ensure closeMobileSidebar() is called at top of switchTab(tabId)
2. Add desktop-only class to Presenter and Print buttons on mobile
3. Compact Excel button text on mobile (.excel-lbl-full / .excel-lbl-short)
4. Ensure topbar layout is ultra-clean on mobile (hamburger, title, lang/theme, excel, search)
5. Add smooth touch scroll & map interactions
"""

import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

build_script_path = r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py"

with open(build_script_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Inject closeMobileSidebar() inside switchTab
switch_target = r'function switchTab(tabId) {'
switch_replacement = r'''function switchTab(tabId) {
      if (typeof closeMobileSidebar === 'function') {
        closeMobileSidebar();
      }'''

if switch_target in code and "if (typeof closeMobileSidebar === 'function')" not in code:
    code = code.replace(switch_target, switch_replacement, 1)
    print("Injected closeMobileSidebar inside switchTab")

# 2. Add responsive Excel label
old_excel_btn = r'''<button class="btn-action highlight" onclick="openExcelModal()" title="تحميل ملفات الإكسيل الأصلية الحسابية">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          <span id="btn-excel-lbl">ملفات الإكسيل الأصلية (Excel Sources)</span>
        </button>'''

new_excel_btn = r'''<button class="btn-action highlight" onclick="openExcelModal()" title="تحميل ملفات الإكسيل الأصلية الحسابية">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          <span class="excel-lbl-full" id="btn-excel-lbl">ملفات الإكسيل الأصلية (Excel Sources)</span>
          <span class="excel-lbl-short" style="display:none;">Excel (.xlsx)</span>
        </button>'''

if old_excel_btn in code:
    code = code.replace(old_excel_btn, new_excel_btn, 1)
    print("Updated Excel button with responsive label")

# 3. Mark Presenter Mode and Print as desktop-only
presenter_btn = r'<button class="btn-action" onclick="openPresenterMode()">'
code = code.replace(presenter_btn, r'<button class="btn-action desktop-only" onclick="openPresenterMode()">', 1)

print_btn = r'<button class="btn-action" onclick="window.print()">'
code = code.replace(print_btn, r'<button class="btn-action desktop-only" onclick="window.print()">', 1)

# 4. Mobile CSS Enhancements
extra_mobile_css = r'''
    .desktop-only { display: inline-flex; }
    
    @media (max-width: 768px) {
      .desktop-only { display: none !important; }
      .excel-lbl-full { display: none !important; }
      .excel-lbl-short { display: inline !important; }

      .topbar {
        padding: 8px 12px !important;
        gap: 8px !important;
      }

      .topbar-actions {
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 6px !important;
      }

      .search-box {
        order: 2;
        width: 100% !important;
        margin-top: 4px;
      }
      .search-box input {
        width: 100% !important;
        height: 34px !important;
      }

      .ctrl-group {
        padding: 2px !important;
      }
      .ctrl-pill {
        padding: 4px 8px !important;
        font-size: 11px !important;
      }

      /* GIS Map touch friendliness */
      #tmg-gis-map {
        height: 360px !important;
        touch-action: pan-x pan-y !important;
      }
      
      /* Make tables easily swipeable with nice gradient fade indicator */
      .table-container {
        position: relative;
        max-width: 100%;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
      }

      /* Make sure inputs don't zoom on iOS */
      input[type="text"], input[type="search"] {
        font-size: 16px !important;
      }
    }
'''

# Inject extra mobile CSS before @media (max-width: 1080px)
needle_css = r'@media (max-width: 1080px) {'
if needle_css in code:
    code = code.replace(needle_css, extra_mobile_css + "\n    " + needle_css, 1)
    print("Injected extra mobile CSS")

with open(build_script_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved build_perfect_dashboard.py")
