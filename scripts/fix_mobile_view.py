# -*- coding: utf-8 -*-
"""
Mobile View Comprehensive Fix:
1. Add Hamburger toggle button in Topbar
2. Add Mobile Sidebar Backdrop overlay
3. Add Mobile Open/Close slide drawer animations & JS
4. Auto-close sidebar on tab selection
5. Responsive Topbar (search, buttons, titles)
6. Compact card padding, double-bezel, and KPI grids on small screens
7. Leaflet Map touch & height responsiveness on mobile
8. Table scrollability with touch smooth physics
9. Modal sizing for phones
"""

import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

build_script_path = r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py"

with open(build_script_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add Mobile Backdrop right after <body>
body_tag = r'<body>'
backdrop_html = r'''<body>
  <!-- Mobile Sidebar Backdrop Overlay -->
  <div id="sidebar-backdrop" class="sidebar-backdrop" onclick="closeMobileSidebar()"></div>'''

if backdrop_html not in code:
    code = code.replace(body_tag, backdrop_html, 1)
    print("Added sidebar backdrop")

# 2. Add Hamburger Button to Topbar
topbar_page_title = r'<header class="topbar">' + "\n" + r'      <div class="page-title">'
hamburger_html = r'''<header class="topbar">
      <!-- Mobile Hamburger Toggle Button -->
      <button class="btn-hamburger" id="btn-mobile-nav" onclick="toggleMobileSidebar()" aria-label="تبديل القائمة">
        <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>

      <div class="page-title">'''

if hamburger_html not in code:
    code = code.replace(topbar_page_title, hamburger_html, 1)
    print("Added hamburger button in topbar")

# 3. Add Mobile Sidebar Close button inside sidebar header
brand_div = r'<div class="brand">' + "\n" + r'      <div class="brand-icon">T</div>'
brand_with_close = r'''<div class="brand" style="justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <div class="brand-icon">T</div>
        <div>
          <div class="brand-title" id="lbl-brand-title">استخبارات طلعت مصطفى</div>
          <div class="brand-subtitle" id="lbl-brand-sub">درع الفحص النافي للجهالة</div>
        </div>
      </div>
      <button class="btn-close-sidebar" onclick="closeMobileSidebar()" aria-label="إغلاق">&times;</button>
    </div>'''

# Replace old brand header
old_brand = r'<div class="brand">' + "\n" + r'      <div class="brand-icon">T</div>' + "\n" + r'      <div>' + "\n" + r'        <div class="brand-title" id="lbl-brand-title">استخبارات طلعت مصطفى</div>' + "\n" + r'        <div class="brand-subtitle" id="lbl-brand-sub">درع الفحص النافي للجهالة</div>' + "\n" + r'      </div>' + "\n" + r'    </div>'
if old_brand in code:
    code = code.replace(old_brand, brand_with_close, 1)
    print("Added close button inside sidebar brand")

# 4. Inject Comprehensive Mobile CSS
mobile_css_target = r'@media (max-width: 1080px) {'
mobile_css_replacement = r'''/* ==========================================================================
       MOBILE RESPONSIVENESS & TOUCH CONTROLS ENGINE
       ========================================================================== */
    .sidebar-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      z-index: 45;
      opacity: 0;
      transition: opacity 0.25s ease;
    }
    .sidebar-backdrop.active {
      display: block;
      opacity: 1;
    }

    .btn-hamburger {
      display: none;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      width: 40px;
      height: 40px;
      border-radius: 9px;
      cursor: pointer;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }
    .btn-hamburger:hover {
      background: var(--accent-cyan);
      color: #fff;
      border-color: var(--accent-cyan);
    }

    .btn-close-sidebar {
      display: none;
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-size: 26px;
      cursor: pointer;
      line-height: 1;
      padding: 0 4px;
    }

    @media (max-width: 1080px) {
      .grid-2, .grid-3, .grid-2-1 { grid-template-columns: 1fr; }
      
      .btn-hamburger { display: inline-flex; }
      .btn-close-sidebar { display: block; }
      
      .sidebar {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        width: 300px;
        max-width: 85vw;
        height: 100vh;
        z-index: 50;
        transform: translateX(-100%);
        box-shadow: 0 0 50px rgba(0, 0, 0, 0.6);
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      }
      
      html[dir="rtl"] .sidebar {
        left: auto;
        right: 0;
        transform: translateX(100%);
      }
      
      .sidebar.mobile-open {
        transform: translateX(0) !important;
      }
      
      .main-wrapper {
        width: 100%;
        max-width: 100vw;
      }

      .topbar {
        padding: 0 16px;
        gap: 10px;
      }

      .page-title {
        font-size: 14.5px;
      }
    }

    @media (max-width: 768px) {
      .topbar {
        height: auto;
        min-height: 58px;
        padding: 8px 12px;
        flex-wrap: wrap;
        gap: 8px;
      }

      .page-title {
        font-size: 13.5px;
        gap: 6px;
      }

      .badge-status {
        display: none; /* Hide on mobile to save precious header space */
      }

      .topbar-actions {
        width: 100%;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 6px;
      }

      .search-box {
        flex: 1;
        min-width: 140px;
      }
      .search-box input {
        width: 100%;
        padding: 6px 28px 6px 10px;
        font-size: 11.5px;
      }
      html[dir="rtl"] .search-box input {
        padding: 6px 10px 6px 28px;
      }
      .search-box input:focus {
        width: 100%;
      }

      .btn-action {
        padding: 6px 10px;
        font-size: 11px;
      }

      .content-area {
        padding: 14px 10px;
        gap: 16px;
      }

      .card {
        padding: 15px 12px;
        border-radius: 11px;
      }

      .card-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
        margin-bottom: 12px;
      }

      .kpi-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 8px !important;
      }

      .kpi-card {
        padding: 12px 10px !important;
      }

      .kpi-title {
        font-size: 10.5px !important;
      }

      .kpi-value {
        font-size: 18px !important;
      }

      .chart-box {
        height: 240px !important;
      }

      #tmg-gis-map {
        height: 380px !important;
      }

      .modal-box {
        width: 96% !important;
        max-width: 96vw !important;
        padding: 16px 12px !important;
        max-height: 92vh !important;
        border-radius: 12px !important;
      }

      .table-container {
        -webkit-overflow-scrolling: touch;
      }

      th, td {
        padding: 9px 8px;
        font-size: 11px;
      }

      #bs-year-selector {
        flex-wrap: wrap;
      }
      #bs-year-selector button {
        padding: 4px 7px;
        font-size: 10.5px;
      }
    }

    @media (max-width: 480px) {
      .kpi-grid {
        grid-template-columns: 1fr !important;
      }
      
      .btn-action.hide-xs {
        display: none !important;
      }
    }

    @media (max-width: 1080px) {'''

if mobile_css_target in code:
    code = code.replace(mobile_css_target, mobile_css_replacement, 1)
    print("Injected Comprehensive Mobile CSS")

# 5. Inject Mobile Sidebar JS Functions
js_sidebar_target = r'function switchTab(tabId) {'
js_sidebar_functions = r'''
    // Mobile Sidebar Drawer Handlers
    function toggleMobileSidebar() {
      const sidebar = document.querySelector('.sidebar');
      const backdrop = document.getElementById('sidebar-backdrop');
      if (sidebar) sidebar.classList.toggle('mobile-open');
      if (backdrop) backdrop.classList.toggle('active');
    }

    function closeMobileSidebar() {
      const sidebar = document.querySelector('.sidebar');
      const backdrop = document.getElementById('sidebar-backdrop');
      if (sidebar) sidebar.classList.remove('mobile-open');
      if (backdrop) backdrop.classList.remove('active');
    }

    ''' + js_sidebar_target

if js_sidebar_target in code:
    code = code.replace(js_sidebar_target, js_sidebar_functions, 1)
    print("Injected Mobile Sidebar JS Functions")

# 6. Make switchTab close mobile drawer automatically
switch_tab_body = r'document.querySelectorAll(\'.tab-pane\').forEach(p => p.classList.remove(\'active\'));'
switch_tab_replacement = r'''closeMobileSidebar();
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));'''

if switch_tab_body in code:
    code = code.replace(switch_tab_body, switch_tab_replacement, 1)
    print("Updated switchTab to auto-close mobile sidebar")

with open(build_script_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated build_perfect_dashboard.py with mobile overhaul")
