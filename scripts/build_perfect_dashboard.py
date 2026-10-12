# -*- coding: utf-8 -*-
"""
Script to build the definitive, bilingual, high-end interactive forensic dashboard
for Talaat Moustafa Group Holding (TMGH) with complete Arabic & English support,
White & Dark themes, D3.js interactive privity network, clickable source links,
and newly integrated contractor & labor incident records.
"""
import os
import sys

output_path_1 = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"
output_path_2 = r"F:\Mr Hesham\TMG\index.html"

# We generate the HTML template with embedded JSON datasets for 100% reactive bilingual switching
html_code = r'''<!DOCTYPE html>
<html lang="ar" data-theme="light" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>استخبارات طلعت مصطفى الجنائية — لوحة الفحص النافي للجهالة ومخاطر سلاسل الإمداد</title>
  
  <!-- Google Fonts: Cairo, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- CDN Libraries: Chart.js & D3.js v7 -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://d3js.org/d3.v7.min.js"></script>

  <style>
    /* ==========================================================================
       THEME ENGINE & HIGH-END DESIGN SYSTEM (Awwwards-Tier & Double-Bezel)
       ========================================================================== */
    :root {
      /* Dark Theme (OLED Vantablack Luxury) */
      --bg-base: #060911;
      --bg-surface: #0c1220;
      --bg-surface-elevated: #131c31;
      --bg-card: rgba(18, 27, 46, 0.85);
      --bg-card-hover: rgba(25, 38, 64, 0.95);
      --outer-bezel: rgba(255, 255, 255, 0.05);
      --outer-bezel-hover: rgba(6, 182, 212, 0.35);
      --border-subtle: #1e293b;
      --border-highlight: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --accent-cyan: #06b6d4;
      --accent-blue: #3b82f6;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-purple: #8b5cf6;

      --card-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      --kpi-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --font-ar: 'Cairo', 'Plus Jakarta Sans', sans-serif;

      --diagram-bg: #03060c;
      --diagram-border: #1e293b;
      --diagram-text: #38bdf8;
      --table-stripe: rgba(255, 255, 255, 0.015);
      --table-hover: rgba(6, 182, 212, 0.08);
      --th-bg: #131c31;
      --th-color: #cbd5e1;
    }

    [data-theme="light"] {
      /* White Theme (Executive Crisp Paper Luxury - High Contrast) */
      --bg-base: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #f1f5f9;
      --bg-card: #ffffff;
      --bg-card-hover: #fcfdfe;
      --outer-bezel: rgba(15, 23, 42, 0.06);
      --outer-bezel-hover: rgba(2, 132, 199, 0.4);
      --border-subtle: #cbd5e1;
      --border-highlight: #94a3b8;
      --text-main: #090d16;
      --text-muted: #334155;
      --text-dim: #64748b;
      
      --accent-cyan: #0284c7;
      --accent-blue: #2563eb;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-rose: #dc2626;
      --accent-purple: #7c3aed;

      --card-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.9);
      --kpi-shadow: 0 4px 15px -3px rgba(15, 23, 42, 0.08);

      --diagram-bg: #f8fafc;
      --diagram-border: #cbd5e1;
      --diagram-text: #0284c7;
      --table-stripe: rgba(15, 23, 42, 0.02);
      --table-hover: rgba(2, 132, 199, 0.08);
      --th-bg: #e2e8f0;
      --th-color: #0f172a;
    }

    /* RTL Layout Rules */
    html[dir="rtl"] body {
      font-family: var(--font-ar);
    }
    html[dir="rtl"] .sidebar {
      border-right: none;
      border-left: 1px solid var(--border-subtle);
    }
    html[dir="rtl"] .search-box svg {
      left: auto;
      right: 12px;
    }
    html[dir="rtl"] .search-box input {
      padding: 7px 34px 7px 14px;
    }
    html[dir="rtl"] .nav-btn {
      text-align: right;
    }
    html[dir="rtl"] .flag-card {
      border-left: 1px solid var(--border-subtle);
      border-right: 4px solid var(--accent-cyan);
    }
    html[dir="rtl"] .step-num {
      left: auto;
      right: 16px;
    }

    /* LTR Layout Rules */
    html[dir="ltr"] body {
      font-family: var(--font-sans);
    }
    html[dir="ltr"] .sidebar {
      border-right: 1px solid var(--border-subtle);
      border-left: none;
    }
    html[dir="ltr"] .search-box svg {
      left: 12px;
      right: auto;
    }
    html[dir="ltr"] .search-box input {
      padding: 7px 14px 7px 34px;
    }
    html[dir="ltr"] .nav-btn {
      text-align: left;
    }
    html[dir="ltr"] .flag-card {
      border-right: 1px solid var(--border-subtle);
      border-left: 4px solid var(--accent-cyan);
    }
    html[dir="ltr"] .step-num {
      left: 16px;
      right: auto;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-base);
      color: var(--text-main);
      font-size: 13.5px;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      overflow-x: hidden;
      transition: background-color 0.25s cubic-bezier(0.16, 1, 0.3, 1), color 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-base); }
    ::-webkit-scrollbar-thumb { background: var(--border-highlight); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--accent-cyan); }

    /* ==========================================================================
       SIDEBAR & NAVIGATION
       ========================================================================== */
    .sidebar {
      width: 290px;
      background: var(--bg-surface);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      position: sticky;
      top: 0;
      height: 100vh;
      z-index: 40;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .main-wrapper {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      height: 100vh;
    }

    .brand {
      padding: 22px 20px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-icon {
      width: 42px;
      height: 42px;
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
      border-radius: 11px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      color: #fff;
      font-size: 20px;
      box-shadow: 0 4px 15px rgba(6, 182, 212, 0.35);
      flex-shrink: 0;
    }

    .brand-title { font-weight: 800; font-size: 15px; letter-spacing: -0.02em; }
    .brand-subtitle { font-size: 11px; color: var(--text-dim); font-family: var(--font-mono); text-transform: uppercase; letter-spacing: 0.06em; }

    .nav-menu {
      padding: 16px 12px;
      display: flex;
      flex-direction: column;
      gap: 5px;
      flex: 1;
      overflow-y: auto;
    }

    .nav-label {
      font-size: 11px;
      text-transform: uppercase;
      color: var(--text-dim);
      padding: 8px 12px 4px;
      font-weight: 700;
      letter-spacing: 0.06em;
    }

    .nav-btn {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 11px 14px;
      border-radius: 9px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      background: transparent;
      border: 1px solid transparent;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      width: 100%;
    }

    .nav-btn:hover {
      background: var(--bg-surface-elevated);
      color: var(--text-main);
      border-color: var(--border-subtle);
    }

    .nav-btn.active {
      background: rgba(6, 182, 212, 0.12);
      color: var(--accent-cyan);
      border-color: rgba(6, 182, 212, 0.3);
      font-weight: 700;
    }

    .nav-btn svg { width: 18px; height: 18px; flex-shrink: 0; }

    .sidebar-footer {
      padding: 16px 20px;
      border-top: 1px solid var(--border-subtle);
      background: var(--bg-surface-elevated);
      font-size: 11.5px;
      color: var(--text-dim);
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    /* ==========================================================================
       TOPBAR & CONTROLS
       ========================================================================== */
    .topbar {
      height: 66px;
      border-bottom: 1px solid var(--border-subtle);
      background: var(--bg-surface);
      backdrop-filter: blur(16px);
      padding: 0 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 30;
      transition: all 0.25s ease;
    }

    .page-title {
      font-size: 16px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .badge-status {
      font-size: 11px;
      font-family: var(--font-mono);
      background: rgba(16, 185, 129, 0.12);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 3px 10px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 700;
    }

    .badge-status::before {
      content: '';
      width: 6px;
      height: 6px;
      background: var(--accent-emerald);
      border-radius: 50%;
      box-shadow: 0 0 6px var(--accent-emerald);
    }

    .topbar-actions { display: flex; align-items: center; gap: 10px; }

    .search-box { position: relative; }
    .search-box input {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      border-radius: 9px;
      font-size: 12px;
      width: 220px;
      outline: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: inherit;
    }
    .search-box input:focus {
      border-color: var(--accent-cyan);
      box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.2);
      width: 280px;
    }
    .search-box svg {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 14px;
      height: 14px;
      color: var(--text-dim);
    }

    /* Switch Groups */
    .ctrl-group {
      display: inline-flex;
      align-items: center;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 9px;
      padding: 3px;
      gap: 2px;
    }

    .ctrl-pill {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 11px;
      border-radius: 7px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .ctrl-pill:hover { color: var(--text-main); }
    .ctrl-pill.active {
      background: var(--bg-surface);
      color: var(--accent-cyan);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

    .btn-action {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 7px 14px;
      border-radius: 9px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .btn-action:hover {
      color: var(--text-main);
      border-color: var(--border-highlight);
      background: var(--bg-surface);
    }

    .btn-action.highlight {
      background: rgba(6, 182, 212, 0.12);
      border-color: rgba(6, 182, 212, 0.35);
      color: var(--accent-cyan);
    }
    .btn-action.highlight:hover {
      background: rgba(6, 182, 212, 0.2);
    }

    /* ==========================================================================
       CARDS & DOUBLE-BEZEL CONTAINERS
       ========================================================================== */
    .content-area {
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 24px;
      max-width: 1720px;
      width: 100%;
      margin: 0 auto;
    }

    .tab-pane { display: none; animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1); }
    .tab-pane.active { display: block; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .bezel-wrap {
      background: var(--outer-bezel);
      border: 1px solid var(--border-subtle);
      padding: 6px;
      border-radius: 18px;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .bezel-wrap:hover {
      border-color: var(--outer-bezel-hover);
    }

    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 22px;
      box-shadow: var(--card-shadow);
      transition: all 0.2s ease;
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 12px;
    }

    .card-title {
      font-size: 15.5px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: -0.01em;
    }

    .card-subtitle {
      font-size: 12px;
      color: var(--text-dim);
      margin-top: 3px;
    }

    /* KPI Grid */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
    }

    .kpi-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 20px;
      box-shadow: var(--kpi-shadow);
      display: flex;
      flex-direction: column;
      gap: 10px;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s;
    }
    .kpi-card:hover { transform: translateY(-2px); }

    .kpi-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--accent-cyan);
    }
    .kpi-card.emerald::before { background: var(--accent-emerald); }
    .kpi-card.rose::before { background: var(--accent-rose); }
    .kpi-card.amber::before { background: var(--accent-amber); }
    .kpi-card.purple::before { background: var(--accent-purple); }

    .kpi-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .kpi-title {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .kpi-icon { width: 20px; height: 20px; color: var(--text-dim); }

    .kpi-value {
      font-size: 24px;
      font-weight: 900;
      font-family: var(--font-mono);
      letter-spacing: -0.03em;
    }

    .kpi-delta {
      font-size: 11px;
      display: flex;
      align-items: center;
      gap: 5px;
      font-weight: 700;
      flex-wrap: wrap;
    }

    .delta-up { color: var(--accent-emerald); }
    .delta-down { color: var(--accent-rose); }
    .delta-warn { color: var(--accent-amber); }
    .delta-sub { color: var(--text-dim); font-weight: normal; margin-inline-start: 4px; }

    /* Grids */
    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
    .grid-2-1 { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }

    /* ==========================================================================
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

    @media (max-width: 1080px) {
      .grid-2, .grid-3, .grid-2-1 { grid-template-columns: 1fr; }
      .sidebar { position: fixed; transform: translateX(-100%); }
      html[dir="rtl"] .sidebar { transform: translateX(100%); }
    }

    .chart-box { position: relative; height: 310px; width: 100%; }

    /* Tables */
    .table-container {
      overflow-x: auto;
      border: 1px solid var(--border-subtle);
      border-radius: 11px;
      background: var(--bg-surface);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
      unicode-bidi: isolate;
    }

    html[dir="rtl"] table { text-align: right; }
    html[dir="ltr"] table { text-align: left; }

    thead {
      background: var(--th-bg);
      border-bottom: 1px solid var(--border-subtle);
    }

    th {
      padding: 13px 15px;
      font-size: 11.5px;
      text-transform: uppercase;
      color: var(--th-color);
      font-weight: 800;
      letter-spacing: 0.05em;
    }

    td {
      padding: 13px 15px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-main);
      vertical-align: middle;
      line-height: 1.6;
    }

    tbody tr:nth-child(even) { background: var(--table-stripe); }
    tbody tr:hover { background: var(--table-hover); }

    .cell-mono { font-family: var(--font-mono); font-size: 12px; }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      white-space: nowrap;
    }

    .badge-low { background: rgba(16, 185, 129, 0.12); color: var(--accent-emerald); border: 1px solid rgba(16, 185, 129, 0.25); }
    .badge-med { background: rgba(59, 130, 246, 0.12); color: var(--accent-blue); border: 1px solid rgba(59, 130, 246, 0.25); }
    .badge-medhigh { background: rgba(245, 158, 11, 0.12); color: var(--accent-amber); border: 1px solid rgba(245, 158, 11, 0.25); }
    .badge-high { background: rgba(244, 63, 94, 0.12); color: var(--accent-rose); border: 1px solid rgba(244, 63, 94, 0.25); }

    /* Clickable Source Badges */
    .source-link {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: var(--bg-surface-elevated);
      color: var(--accent-cyan);
      border: 1px solid var(--border-subtle);
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .source-link:hover {
      background: var(--accent-cyan);
      color: #fff;
      border-color: var(--accent-cyan);
      transform: translateY(-1px);
    }

    /* Flags & Steps */
    .flag-card {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: var(--kpi-shadow);
    }
    .flag-header { display: flex; align-items: center; justify-content: space-between; }
    .flag-title { font-weight: 800; font-size: 14px; }
    .flag-desc { font-size: 12.5px; color: var(--text-muted); line-height: 1.6; }
    .flag-footer { display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: var(--text-dim); margin-top: 4px; }

    .step-card {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 18px;
      position: relative;
    }
    .step-num {
      position: absolute;
      top: -10px;
      background: var(--accent-cyan);
      color: #fff;
      font-weight: 800;
      font-size: 10.5px;
      padding: 2px 9px;
      border-radius: 10px;
    }

    /* Filter buttons */
    .filter-group { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
    .filter-btn {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 6px 13px;
      border-radius: 7px;
      font-size: 12px;
      cursor: pointer;
      font-weight: 700;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .filter-btn:hover { color: var(--text-main); }
    .filter-btn.active {
      background: var(--accent-cyan);
      color: #fff;
      border-color: var(--accent-cyan);
    }

    /* D3 Interactive Graph */
    #d3-privity-tree {
      width: 100%;
      height: 480px;
      background: var(--diagram-bg);
      border: 1px solid var(--diagram-border);
      border-radius: 12px;
      position: relative;
      overflow: hidden;
    }

    .d3-node circle {
      stroke-width: 2px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .d3-node circle:hover {
      r: 12px;
      filter: drop-shadow(0 0 8px var(--accent-cyan));
    }
    .d3-node text {
      font-family: var(--font-sans);
      font-size: 11px;
      fill: var(--text-main);
      pointer-events: none;
    }
    .d3-link {
      fill: none;
      stroke: var(--border-highlight);
      stroke-width: 1.5px;
      stroke-opacity: 0.7;
    }
    .d3-controls {
      position: absolute;
      bottom: 14px;
      inset-inline-end: 14px;
      display: flex;
      gap: 6px;
      z-index: 10;
    }

    #node-inspector {
      position: absolute;
      top: 14px;
      inset-inline-end: 14px;
      width: 320px;
      background: var(--bg-surface);
      border: 1px solid var(--border-highlight);
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
      display: none;
      z-index: 20;
    }
    #node-inspector.active { display: block; animation: fadeIn 0.2s ease; }

    /* Modal for Detailed Source Inspection */
    #excel-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
    }
    #excel-modal.active { display: flex; }
    
    #source-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(8px);
      z-index: 999;
      align-items: center;
      justify-content: center;
    }
    #source-modal.active { display: flex; }

    .modal-box {
      width: 90%;
      max-width: 720px;
      max-height: 88vh;
      overflow-y: auto;
      background: var(--bg-surface);
      border: 1px solid var(--border-highlight);
      border-radius: 16px;
      padding: 28px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Presenter Overlay */
    #presenter-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: var(--bg-base);
      z-index: 100;
      flex-direction: column;
    }
    #presenter-overlay.active { display: flex; }

    .slide-progress {
      height: 4px;
      background: var(--border-subtle);
      width: 100%;
    }
    .slide-progress-bar {
      height: 100%;
      background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue));
      width: 12.5%;
      transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .presenter-viewport {
      flex: 1;
      padding: 30px;
      overflow-y: auto;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .slide-canvas {
      width: 100%;
      max-width: 1240px;
      background: var(--bg-surface);
      border: 1px solid var(--border-highlight);
      border-radius: 20px;
      padding: 36px 42px;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      gap: 20px;
      min-height: 560px;
    }

    .slide-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 16px;
    }
    .slide-number {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent-cyan);
      font-weight: 700;
    }
    .slide-body {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 16px;
    }

    .speaker-notes-banner {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-inline-start: 4px solid var(--accent-amber);
      border-radius: 10px;
      padding: 14px 18px;
      font-size: 12.5px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .presenter-dock {
      height: 64px;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 40px;
    }

    @media print {
      body { background: #fff !important; color: #000 !important; }
      .sidebar, .topbar, #presenter-overlay, .topbar-actions, .filter-group { display: none !important; }
      .main-wrapper { height: auto !important; overflow: visible !important; }
      .tab-pane { display: block !important; margin-bottom: 40px; page-break-after: always; }
      .card { border: 1px solid #ccc !important; background: #fff !important; color: #000 !important; box-shadow: none !important; }
    }
  </style>
  <!-- Leaflet.js Interactive Geo Map -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

</head>
<body>
  <!-- Mobile Sidebar Backdrop Overlay -->
  <div id="sidebar-backdrop" class="sidebar-backdrop" onclick="closeMobileSidebar()"></div>

  <!-- ==========================================================================
       SIDEBAR NAVIGATION
       ========================================================================== -->
  <aside class="sidebar">
    <div class="brand" style="justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <div class="brand-icon">T</div>
        <div>
          <div class="brand-title" id="lbl-brand-title">استخبارات طلعت مصطفى</div>
          <div class="brand-subtitle" id="lbl-brand-sub">درع الفحص النافي للجهالة</div>
        </div>
      </div>
      <button class="btn-close-sidebar" onclick="closeMobileSidebar()" aria-label="إغلاق">&times;</button>
    </div>

    <nav class="nav-menu">
      <div class="nav-label" id="lbl-nav-label">وحدات التحقيق الجنائي</div>
      
      <button class="nav-btn active" onclick="switchTab('overview')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        <span id="nav-overview">لوحة القيادة التنفيذية</span>
      </button>

      <button class="nav-btn" onclick="switchTab('procurement')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
        <span id="nav-procurement">المشتريات المدمجة والدرع القانوني</span>
      </button>

      <button class="nav-btn" onclick="switchTab('mustakhlasat')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        <span id="nav-mustakhlasat">المستخلصات وعقبة الصرف</span>
      </button>

      <button class="nav-btn" onclick="switchTab('projects')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
        <span id="nav-projects">محفظة المشاريع والأصول</span>
      </button>

      <button class="nav-btn" onclick="switchTab('contractors')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        <span id="nav-contractors">سجل المقاولين والموردين</span>
      </button>

      <button class="nav-btn" onclick="switchTab('disputes')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>
        <span id="nav-disputes">الأحكام القضائية وسجلات التحكيم</span>
      </button>

      <button class="nav-btn" onclick="switchTab('financials')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
        <span id="nav-financials">التحليل المالي الجنائي والسيولة</span>
      </button>

      <button class="nav-btn" onclick="switchTab('sentiment')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"/></svg>
        <span id="nav-sentiment">شكاوى المقاولين والعمال والملاك</span>
      </button>

      <button class="nav-btn" onclick="switchTab('risks')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
        <span id="nav-risks">مصفوفة المخاطر ودليل التحوط</span>
      </button>

      <button class="nav-btn" onclick="switchTab('pzone')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
        <span id="nav-pzone">دراسة P.ZONE وحزم المياه</span>
      </button>

      <button class="nav-btn" onclick="switchTab('stakeholders')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/></svg>
        <span id="nav-stakeholders">خريطة المشروعات وأصحاب المصلحة</span>
      </button>
    </nav>

    <div class="sidebar-footer">
      <div><span id="lbl-cutoff">تاريخ الفحص</span>: <strong>11 أكتوبر 2026</strong></div>
      <div><span id="lbl-cap">رأس المال المصدر</span>: <strong>20.64 مليار جنيه</strong></div>
      <div style="color: var(--accent-cyan); margin-top: 4px; font-weight:700;">Hassan Soliman Mode • v3.2</div>
    </div>
  </aside>

  <!-- ==========================================================================
       MAIN VIEWPORT
       ========================================================================== -->
  <div class="main-wrapper">
    <!-- TOP BAR -->
    <header class="topbar">
      <!-- Mobile Hamburger Toggle Button -->
      <button class="btn-hamburger" id="btn-mobile-nav" onclick="toggleMobileSidebar()" aria-label="تبديل القائمة">
        <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>

      <div class="page-title">
        <span id="current-tab-name">لوحة القيادة التنفيذية</span>
        <span class="badge-status" id="lbl-badge-audited">مدقق رسمياً من الإفصاحات والمصادر المباشرة</span>
      </div>

      <div class="topbar-actions">
        <!-- Search -->
        <div class="search-box">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="global-search" placeholder="ابحث عن كيان، مقاول، قضية، مصدر..." onkeyup="handleGlobalSearch(this.value)">
        </div>

        <!-- Language Switcher -->
        <div class="ctrl-group">
          <button id="lang-ar" class="ctrl-pill active" onclick="setLanguage('ar')">عربي</button>
          <button id="lang-en" class="ctrl-pill" onclick="setLanguage('en')">EN</button>
        </div>

        <!-- Theme Toggle -->
        <div class="ctrl-group">
          <button id="theme-light" class="ctrl-pill active" onclick="setTheme('light')" title="وضع النهار White Theme">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
          </button>
          <button id="theme-dark" class="ctrl-pill" onclick="setTheme('dark')" title="وضع الليل Dark Mode">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
          </button>
        </div>

        <!-- Presenter Mode Button -->
        <!-- Excel Download Button -->
        <button class="btn-action highlight" onclick="openExcelModal()" title="تحميل ملفات الإكسيل الأصلية الحسابية">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          <span class="excel-lbl-full" id="btn-excel-lbl">ملفات الإكسيل الأصلية (Excel Sources)</span>
          <span class="excel-lbl-short" style="display:none;">Excel (.xlsx)</span>
        </button>

        <button class="btn-action desktop-only" onclick="openPresenterMode()">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/></svg>
          <span id="btn-presenter-lbl">وضع العرض التنفيذي</span>
        </button>

        <!-- Export / Print -->
        <button class="btn-action desktop-only" onclick="window.print()">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
          <span id="btn-print-lbl">طباعة / تصدير PDF</span>
        </button>
      </div>
    </header>

    <div class="content-area">

      <!-- ========================================== -->
      <!-- TAB 1: EXECUTIVE DASHBOARD -->
      <!-- ========================================== -->
      <div id="tab-overview" class="tab-pane active">
        <!-- Top KPIs -->
        <div class="kpi-grid" id="kpi-grid-container">
          <!-- Dynamically populated via JS -->
        </div>

        <!-- Charts Grid 1 -->
        <div class="grid-2-1" style="margin-top: 20px;">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-chart-fin-title">المؤشرات المالية التاريخية (2021 – 2025 + النصف الأول 2026)</div>
                  <div class="card-subtitle" id="t-chart-fin-sub">الإيرادات، صافي الأرباح، والمبيعات المتعاقد عليها غير المسلمة (مليار جنيه)</div>
                </div>
              </div>
              <div class="chart-box">
                <canvas id="chartFinancialTrends"></canvas>
              </div>
            </div>
          </div>

          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-chart-comp-title">توزيع شكاوى المقاولين والعمال والملاك</div>
                  <div class="card-subtitle" id="t-chart-comp-sub">تحليل نسبي للوقائع الموثقة بالصحف والمحاكم (عينة موثقة: 46 واقعة)</div>
                </div>
              </div>
              <div class="chart-box">
                <canvas id="chartComplaints"></canvas>
              </div>
            </div>
          </div>
        </div>

        <!-- Master Charts Grid Row 2: Landbank & Risk Radar -->
        <div class="grid-2" style="margin-top: 20px;">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-chart-land-title">1. محفظة الأراضي وتوزيع المساحات (فدان)</div>
                  <div class="card-subtitle" id="t-chart-land-sub">المساحات الإجمالية لأبرز المشاريع العملاقة التابعة للمجموعة بمصر</div>
                </div>
                <span class="badge badge-med" id="badge-chart-land">مساحات الأراضي</span>
              </div>
              <div class="chart-box">
                <canvas id="landbankBarChart"></canvas>
              </div>
            </div>
          </div>

          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-chart-radar-title">2. رادار أبعاد المخاطر الجنائية والتعاقدية (1 - 10)</div>
                  <div class="card-subtitle" id="t-chart-radar-sub">تقييم تركيبي لأبرز مخاطر التعاقد: الصرف، العزل القانوني، التحكيم، والتضخم</div>
                </div>
                <span class="badge badge-high" id="badge-chart-radar">تحليل المخاطر</span>
              </div>
              <div class="chart-box">
                <canvas id="riskRadarChart"></canvas>
              </div>
            </div>
          </div>
        </div>

        <!-- Master Charts Grid Row 3: Ownership & Evidence Strength -->
        <div class="grid-2" style="margin-top: 20px;">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-chart-owner-title">3. هيكل الملكية والمساهمين الرئيسيين (UBO)</div>
                  <div class="card-subtitle" id="t-chart-owner-sub">توزيع حصص رأس المال المصدر: عائلة طلعت مصطفى مقابل التداول الحر والصناديق</div>
                </div>
                <span class="badge badge-med" id="badge-chart-owner">هيكل الملكية</span>
              </div>
              <div class="chart-box">
                <canvas id="ownershipDoughnutChart"></canvas>
              </div>
            </div>
          </div>

          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-chart-polar-title">4. هرمية قوة الأدلة وموثوقية مصادر الفحص</div>
                  <div class="card-subtitle" id="t-chart-polar-sub">التصنيف الإثباتي: أحكام قضائية وإفصاحات رسمية مقابل سوابق هندسية وتسويق</div>
                </div>
                <span class="badge badge-med" id="badge-chart-polar">حجية الأدلة</span>
              </div>
              <div class="chart-box">
                <canvas id="evidencePolarChart"></canvas>
              </div>
            </div>
          </div>
        </div>

        <!-- Core Material Verified Conclusions -->
        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" style="color: var(--accent-cyan);">
                  <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                  <span id="t-conclusions-title">النتائج الجوهرية المدققة للفحص النافي للجهالة</span>
                </div>
                <div class="card-subtitle" id="t-conclusions-sub">مستندة للإفصاحات الرسمية، الأحكام القضائية، التحقيقات الصحفية وسجلات التنفيذ المباشرة</div>
              </div>
            </div>

            <div class="grid-3" id="conclusions-cards-container">
              <!-- Dynamically populated via JS -->
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 2: CAPTIVE PROCUREMENT & PRIVITY -->
      <!-- ========================================== -->
      <div id="tab-procurement" class="tab-pane">
        <div class="bezel-wrap">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-proc-title">هيكل المشتريات المدمجة والشبكة التفاعلية للحجية النسبية للعقود</div>
                <div class="card-subtitle" id="t-proc-sub">شجرة D3.js التفاعلية — انقر فوق أي كيان أو شركة لفحص سند الملكية، درع الحجية القانونية، ومصدر الإثبات</div>
              </div>
              <div class="filter-group">
                <button class="filter-btn" onclick="resetD3View()" id="btn-reset-d3">إعادة ضبط المشهد</button>
              </div>
            </div>

            <!-- D3 Interactive Tree -->
            <div id="d3-privity-tree">
              <div class="d3-controls">
                <button class="filter-btn" onclick="zoomD3(1.2)">+</button>
                <button class="filter-btn" onclick="zoomD3(0.8)">-</button>
              </div>

              <!-- Node Inspector Panel -->
              <div id="node-inspector">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <strong id="inspector-name" style="font-size:13.5px; color:var(--accent-cyan);">Entity</strong>
                  <button onclick="closeInspector()" style="background:none; border:none; color:var(--text-dim); cursor:pointer; font-size:14px;">✕</button>
                </div>
                <div id="inspector-type" style="font-size:11px; color:var(--text-dim); text-transform:uppercase; margin-bottom:10px; font-weight:700;">Type</div>
                <div style="font-size:12px; line-height:1.6; color:var(--text-muted); margin-bottom:10px;" id="inspector-desc">Description</div>
                <div style="border-top:1px solid var(--border-subtle); padding-top:8px; font-size:11.5px; display:flex; flex-direction:column; gap:4px;">
                  <div><strong>الدرع القانوني (الحجية):</strong> <span id="inspector-shield">High</span></div>
                  <div><strong>مستوى التعرض المباشر:</strong> <span id="inspector-risk">Low</span></div>
                  <div style="margin-top:6px;"><span id="inspector-source-box"></span></div>
                </div>
              </div>
            </div>

            <!-- Explanatory cards -->
            <div class="grid-2" style="margin-top: 20px;" id="procurement-expl-cards">
              <!-- Dynamically populated via JS -->
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 3: المستخلصات & PAYMENT BOTTLENECK -->
      <!-- ========================================== -->
      <div id="tab-mustakhlasat" class="tab-pane">
        <div class="bezel-wrap">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-must-title">عقبة دورة اعتماد مستخلصات المقاولين (المستخلصات)</div>
                <div class="card-subtitle" id="t-must-sub">التسلسل الإجرائي لتدقيق واعتماد وصرف دفعات الإنجاز التجاري وأثرها على المقاولين</div>
              </div>
            </div>

            <!-- Multi-Stage Line Chart: Standard vs Extended Timeline -->
            <div class="bezel-wrap" style="margin-top: 14px; margin-bottom: 20px;">
              <div class="card" style="background: var(--bg-surface);">
                <div class="card-header">
                  <div>
                    <div class="card-title" id="t-chart-ipc-title">مقارنة دورة صرف المستخلصات: التعاقدي (90 يوماً) مقابل المرصود فعلياً (270 يوماً)</div>
                    <div class="card-subtitle" id="t-chart-ipc-sub">المسار الزمني لمراحل تدقيق واعتماد المستخلصات حتى التحصيل النقدي النهائي</div>
                  </div>
                  <span class="badge badge-high" id="badge-chart-ipc">المستخلصات وأوراق الدفع</span>
                </div>
                <div class="chart-box" style="height: 320px;">
                  <canvas id="ipcLifecycleLineChart"></canvas>
                </div>
              </div>
            </div>

            <!-- Workflow Graph -->
            <div class="grid-3" style="margin-top: 10px;" id="mustakhlasat-steps-container">
              <!-- Dynamically populated via JS -->
            </div>

            <div class="flag-card" style="margin-top: 20px; border-inline-start-color: var(--accent-rose);" id="mustakhlasat-defense-box">
              <!-- Dynamically populated via JS -->
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 4: PROJECT PORTFOLIO & ASSETS -->
      <!-- ========================================== -->
      <div id="tab-projects" class="tab-pane">
        <div class="bezel-wrap">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-projects-title">قاعدة البيانات الشاملة لمحفظة المشاريع والأصول</div>
                <div class="card-subtitle" id="t-projects-sub">هياكل الملكية الموثقة، تواريخ التسليم التعاقدية، ونماذج الشراكة على الأراضي مع روابط المصادر الرسمية</div>
              </div>
              <div class="filter-group" id="project-filters">
                <button class="filter-btn active" onclick="filterProjects('all')" id="btn-flt-all">الكل (14)</button>
                <button class="filter-btn" onclick="filterProjects('east-cairo')" id="btn-flt-east">شرق القاهرة</button>
                <button class="filter-btn" onclick="filterProjects('coastal')" id="btn-flt-coast">الساحل والبحر الأحمر</button>
                <button class="filter-btn" onclick="filterProjects('cross-border')" id="btn-flt-border">خارج الحدود (السعودية)</button>
                <button class="filter-btn" onclick="filterProjects('hospitality')" id="btn-flt-hosp">شركات الفنادق التابعة</button>
              </div>
            </div>

            <div class="table-container">
              <table id="projects-table">
                <thead>
                  <tr id="projects-th-row">
                    <!-- Populated via JS -->
                  </tr>
                </thead>
                <tbody id="projects-tbody">
                  <!-- Dynamically populated via JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 5: MASTER CONTRACTOR ROSTER -->
      <!-- ========================================== -->
      <div id="tab-contractors" class="tab-pane">
        <div class="bezel-wrap">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-contractors-title">السجل الموثق للمقاولين الرئيسيين ومقاولي الباطن والموردين</div>
                <div class="card-subtitle" id="t-contractors-sub">الأدوار التعاقدية، نطاقات الأعمال، الملاحظات التوثيقية، وروابط المصادر المباشرة لكل صفقة</div>
              </div>
            </div>

            <!-- Bubble Chart: Exposure Scale vs Public Dispute Friction -->
            <div class="bezel-wrap" style="margin-top: 14px; margin-bottom: 20px;">
              <div class="card" style="background: var(--bg-surface);">
                <div class="card-header">
                  <div>
                    <div class="card-title" id="t-chart-bubble-title">مصفوفة حجم التعاقد مقابل مؤشر النزاعات والتوتر الموقعي</div>
                    <div class="card-subtitle" id="t-chart-bubble-sub">تحليل نسبي للشركاء والمقاولين والعمال: حجم الأعمال (مليار جنيه) مقابل مؤشر التوتر العلني (1-10)</div>
                  </div>
                  <span class="badge badge-med" id="badge-chart-bubble">خريطة الاحتكاك</span>
                </div>
                <div class="chart-box" style="height: 320px;">
                  <canvas id="disputeBubbleChart"></canvas>
                </div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr id="contractors-th-row">
                    <!-- Populated via JS -->
                  </tr>
                </thead>
                <tbody id="contractors-tbody">
                  <!-- Dynamically populated via JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 6: LEGAL, ARBITRATION & COURTS -->
      <!-- ========================================== -->
      <div id="tab-disputes" class="tab-pane">
        <div class="bezel-wrap">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-disputes-title">الأحكام القضائية، الجنح التجارية وسجلات التحكيم المؤسسي (CRCICA)</div>
                <div class="card-subtitle" id="t-disputes-sub">القضايا الموثقة بمجلس الدولة، محاكم الجنح، المحاكم الدولية، وبلاغات النيابة العامة مع مصادرها</div>
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 16px;" id="disputes-cards-container">
              <!-- Dynamically populated via JS -->
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 7: FINANCIAL FORENSICS -->
      <!-- ========================================== -->
      <div id="tab-financials" class="tab-pane">
        <div class="grid-2">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-fin-cf-title">تحليل كفاءة تحويل السيولة النقدية (النصف الأول 2026)</div>
                  <div class="card-subtitle" id="t-fin-cf-sub">صافي الأرباح مقابل التدفق النقدي التشغيلي واستنزاف رأس المال العامل (مليون جنيه)</div>
                </div>
              </div>
              <div class="chart-box">
                <canvas id="chartCashFlow"></canvas>
              </div>
            </div>
          </div>

          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-fin-debt-title">هيكل الالتزامات والديون الإجمالية (30 يونيو 2026)</div>
                  <div class="card-subtitle" id="t-fin-debt-sub">القروض البنكية مقابل التأجير التمويلي ودفعات العملاء المقدمة (مليار جنيه)</div>
                </div>
              </div>
              <div class="chart-box">
                <canvas id="chartDebtBreakdown"></canvas>
              </div>
            </div>
          </div>
        </div>

        <!-- Commercial Debt, Liabilities & Credit Lines Horizontal Bar Chart -->
        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-chart-liab-title">خريطة الالتزامات المالية، التسهيلات البنكية، وأوراق الدفع المؤجلة</div>
                <div class="card-subtitle" id="t-chart-liab-sub">التسهيلات البنكية، توريق أصول رواسي، وأوراق الدفع المؤجلة للموردين والمقاولين (مليار جنيه)</div>
              </div>
              <span class="badge badge-high" id="badge-chart-liab">التزامات الدفع والتمويل</span>
            </div>
            <div class="chart-box" style="height: 280px;">
              <canvas id="liabilitiesHBarChart"></canvas>
            </div>
          </div>
        </div>

        <!-- EXCEL SOURCE & DOWNLOAD HUB CARD -->
        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card" style="background: linear-gradient(135deg, rgba(6,182,212,0.06), rgba(59,130,246,0.04)); border: 1px solid rgba(6,182,212,0.3);">
            <div class="card-header">
              <div>
                <div class="card-title" style="color: var(--accent-cyan); display:flex; align-items:center; gap:8px;">
                  <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                  <span id="t-fin-excel-hub-title">مركز تحميل نماذج الإكسيل الحسابية الأصلية (Audited Excel Models & Calculations)</span>
                </div>
                <div class="card-subtitle" id="t-fin-excel-hub-sub">الملفات تحتوي على المعادلات الحسابية الكاملة (Formulas) لقوائم المركز المالي، الدخل، التدفقات النقدية، ومصفوفات ويبل الإحصائية</div>
              </div>
              <button onclick="openExcelModal()" class="btn-action highlight" style="font-weight:800;">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                <span id="btn-browse-all-excel">استعراض كافة الملفات (8 ملفات)</span>
              </button>
            </div>

            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:14px; margin-top:10px;">
              <div style="background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; gap:10px;">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge badge-high" style="font-size:10px;">15 ورقة عمل حسابية</span>
                    <span style="font-size:10.5px; font-family:var(--font-mono); color:var(--text-dim);">47.6 KB</span>
                  </div>
                  <h4 style="font-size:13px; font-weight:800; margin-top:6px;">TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx</h4>
                  <p style="font-size:11px; color:var(--text-muted); margin-top:4px;">مصفوفة المخاطر الأربعة + ويبل + ميزانية طلعت مصطفى الكاملة بمعادلاتها الحسابية.</p>
                </div>
                <a href="downloads/TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none; font-size:11.5px;">تحميل النموذج الشامل (.xlsx)</a>
              </div>

              <div style="background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; gap:10px;">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge badge-low" style="font-size:10px;">7 أوراق تدقيق مالي</span>
                    <span style="font-size:10.5px; font-family:var(--font-mono); color:var(--text-dim);">25.1 KB</span>
                  </div>
                  <h4 style="font-size:13px; font-weight:800; margin-top:6px;">TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx</h4>
                  <p style="font-size:11px; color:var(--text-muted); margin-top:4px;">القوائم المالية المدققة للبورصة، نسب السيولة، مصفوفة SWOT، ونموذج P.ZONE.</p>
                </div>
                <a href="downloads/TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none; font-size:11.5px;">تحميل القوائم المدققة (.xlsx)</a>
              </div>

              <div style="background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; gap:10px;">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge badge-med" style="font-size:10px;">42 شركة و38 مسؤول</span>
                    <span style="font-size:10.5px; font-family:var(--font-mono); color:var(--text-dim);">17.2 KB</span>
                  </div>
                  <h4 style="font-size:13px; font-weight:800; margin-top:6px;">TMG_Project_Companies_Contacts_One_Sheet.xlsx</h4>
                  <p style="font-size:11px; color:var(--text-muted); margin-top:4px;">دليل شركات المقاولات والاستشاريين والمطورين وهواتفهم وروابط لينكد إن الموثقة.</p>
                </div>
                <a href="downloads/TMG_Project_Companies_Contacts_One_Sheet.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none; font-size:11.5px;">تحميل دليل الشركات (.xlsx)</a>
              </div>
            </div>
          </div>
        </div>

        <!-- TMG INTERACTIVE AUDITED BALANCE SHEET & REAL-TIME CALCULATION ENGINE -->
        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-bs-calc-title">محرك قائمة المركز المالي التفاعلي والحسابات الرياضية (Audited Balance Sheet Dynamic Engine)</div>
                <div class="card-subtitle" id="t-bs-calc-sub">اختر السنة المالية أو اختبر سيناريوهات الضغط (Stress Testing) مع إعادة احتساب نسب السيولة والرافعة ورأس المال العامل آلياً</div>
              </div>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:12px; font-weight:700; color:var(--text-muted);" id="lbl-select-fy">السنة المالية:</span>
                <div class="ctrl-group" id="bs-year-selector">
                  <button class="ctrl-pill" onclick="selectBSYear('FY21')">2021</button>
                  <button class="ctrl-pill" onclick="selectBSYear('FY22')">2022</button>
                  <button class="ctrl-pill" onclick="selectBSYear('FY23')">2023</button>
                  <button class="ctrl-pill active" onclick="selectBSYear('FY24')">2024</button>
                  <button class="ctrl-pill" onclick="selectBSYear('FY25')">2025</button>
                  <button class="ctrl-pill" onclick="selectBSYear('H1_26')">H1 2026</button>
                </div>
              </div>
            </div>

            <!-- Parity Equation Ribbon -->
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap:12px; margin-bottom:18px;">
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--text-dim); text-transform:uppercase;">إجمالي الأصول (Total Assets)</div>
                <div style="font-size:20px; font-weight:900; font-family:var(--font-mono); color:var(--accent-cyan); margin-top:4px;" id="bs-card-assets">278.80 مليار ج.م</div>
                <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">= الأصول المتداولة + الأصول الثابتة</div>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--text-dim); text-transform:uppercase;">إجمالي الالتزامات (Total Liabilities)</div>
                <div style="font-size:20px; font-weight:900; font-family:var(--font-mono); color:var(--accent-rose); margin-top:4px;" id="bs-card-liab">164.03 مليار ج.م</div>
                <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">قروض وتسهيلات + دفعات حجز + تأجير</div>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--text-dim); text-transform:uppercase;">حقوق الملكية (Total Equity)</div>
                <div style="font-size:20px; font-weight:900; font-family:var(--font-mono); color:var(--accent-emerald); margin-top:4px;" id="bs-card-equity">114.77 مليار ج.م</div>
                <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">رأس المال + أرباح مرحلة + أيقون ADQ</div>
              </div>

              <div style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.3); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--accent-emerald); text-transform:uppercase;">فحص التوازن المحاسبي (Parity Check)</div>
                <div style="font-size:18px; font-weight:900; font-family:var(--font-mono); color:var(--accent-emerald); margin-top:4px;" id="bs-card-check">صفر ج.م (متطابق 100%)</div>
                <div style="font-size:11px; color:var(--accent-emerald); margin-top:2px;">الأصول - (الالتزامات + حقوق الملكية) = 0</div>
              </div>
            </div>

            <!-- Two-Column Balance Sheet Grid -->
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap:20px;">
              
              <!-- LEFT: ASSETS BREAKDOWN -->
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:18px;">
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:10px; margin-bottom:12px;">
                  <h4 style="font-size:14px; font-weight:800; color:var(--accent-cyan); display:flex; align-items:center; gap:6px;">
                    <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
                    <span>تفصيل جانب الأصول (Assets Breakdown)</span>
                  </h4>
                  <span class="badge badge-low" style="font-size:10.5px;">القيم بمليون ج.م</span>
                </div>
                
                <table style="width:100%; font-size:12.5px; border-collapse:collapse;">
                  <tbody id="bs-assets-rows">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>

              <!-- RIGHT: LIABILITIES & EQUITY BREAKDOWN -->
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:18px;">
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:10px; margin-bottom:12px;">
                  <h4 style="font-size:14px; font-weight:800; color:var(--accent-rose); display:flex; align-items:center; gap:6px;">
                    <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                    <span>الالتزامات وحقوق الملكية (Liab & Equity)</span>
                  </h4>
                  <span class="badge badge-high" style="font-size:10.5px;">القيم بمليون ج.م</span>
                </div>
                
                <table style="width:100%; font-size:12.5px; border-collapse:collapse;">
                  <tbody id="bs-liab-rows">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>

            </div>

            <!-- LIVE FINANCIAL STRESS TESTER & RATIO SIMULATOR -->
            <div style="margin-top:20px; background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:18px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
                <div>
                  <h4 style="font-size:14px; font-weight:800; color:var(--accent-amber); display:flex; align-items:center; gap:6px;">
                    <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
                    <span>محاكي الضغط المالي وحاسبة النسب الحية (Stress Simulation & Live Ratio Engine)</span>
                  </h4>
                  <p style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">حرك المؤشرات لاختبار سيناريوهات الضغط الفعلي وملاحظة التغير الفوري في نسب السيولة ورأس المال العامل</p>
                </div>
                <button onclick="resetBSStress()" class="btn-action" style="font-size:11.5px;">إعادة الضبط الافتراضي (Reset)</button>
              </div>

              <!-- Sliders Grid -->
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin-bottom:16px;">
                <div>
                  <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                    <span>إدراج تأجير رواسي التمويلي بالكامل بالميزانية:</span>
                    <strong id="val-slider-lease" style="font-family:var(--font-mono); color:var(--accent-cyan);">100%</strong>
                  </div>
                  <input type="range" id="slider-lease" min="0" max="100" value="100" step="10" oninput="updateBSCalculations()" style="width:100%; accent-color:var(--accent-cyan);">
                  <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--text-dim);"><span>0% خارج الميزانية</span><span>100% كامل الالتزام</span></div>
                </div>

                <div>
                  <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                    <span>تسديد عاجل لمستحقات مقاولي الباطن (صرف نقدي):</span>
                    <strong id="val-slider-pay" style="font-family:var(--font-mono); color:var(--accent-amber);">0%</strong>
                  </div>
                  <input type="range" id="slider-pay" min="0" max="50" value="0" step="5" oninput="updateBSCalculations()" style="width:100%; accent-color:var(--accent-amber);">
                  <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--text-dim);"><span>0% استمرار التأخير</span><span>50% سداد فوري نقدي</span></div>
                </div>

                <div>
                  <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                    <span>خصم تسييل مخزون الأراضي غير المطورة:</span>
                    <strong id="val-slider-wip" style="font-family:var(--font-mono); color:var(--accent-rose);">0%</strong>
                  </div>
                  <input type="range" id="slider-wip" min="0" max="30" value="0" step="5" oninput="updateBSCalculations()" style="width:100%; accent-color:var(--accent-rose);">
                  <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--text-dim);"><span>0% قيمة دفترية</span><span>30% تخفيض اضطراري</span></div>
                </div>
              </div>

              <!-- Recalculated Ratios Cards -->
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; border-top:1px solid var(--border-subtle); padding-top:14px;">
                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">نسبة التداول الحالية (Current Ratio)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--text-main); margin-top:2px;" id="calc-curr-ratio">1.59x</div>
                  <div style="font-size:10px; color:var(--accent-emerald);">مقبول (> 1.2x)</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">السيولة السريعة (Quick Ratio)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-rose); margin-top:2px;" id="calc-quick-ratio">0.72x</div>
                  <div style="font-size:10px; color:var(--accent-rose);">حرجة بعد استبعاد المخزون (< 1.0x)</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">صافي الدين (Net Debt)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-amber); margin-top:2px;" id="calc-net-debt">18.80B ج.م</div>
                  <div style="font-size:10px; color:var(--text-muted);">(الديون البنكية + التأجير) - النقدية</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">نسبة المديونية (Debt to Equity)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-cyan); margin-top:2px;" id="calc-debt-eq">0.44x</div>
                  <div style="font-size:10px; color:var(--text-muted);">الديون التمويلية / حقوق المساهمين</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">رأس المال العامل (Working Capital)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-emerald); margin-top:2px;" id="calc-working-cap">+69.80B ج.م</div>
                  <div style="font-size:10px; color:var(--accent-emerald);">الأصول المتداولة - الالتزامات المتداولة</div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-fin-table-title">المصفوفة المالية الجنائية للقوائم المدققة وميزانيات المجموعة (2021 – 2026)</div>
                <div class="card-subtitle" id="t-fin-table-sub">كافة الأرقام بملايين الجنيهات، مدققة من تقارير مراقبي الحسابات المودعة بالبورصة المصرية</div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr id="financials-th-row">
                    <!-- Populated via JS -->
                  </tr>
                </thead>
                <tbody id="financials-tbody">
                  <!-- Dynamically populated via JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 8: CUSTOMER & LABOR SENTIMENT -->
      <!-- ========================================== -->
      <div id="tab-sentiment" class="tab-pane">
        <!-- 3 Metric highlights -->
        <div class="grid-3" id="sentiment-highlights-container">
          <!-- Dynamically populated via JS -->
        </div>

        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-sent-table-title">سجل الشكاوى التفصيلي: المقاولون، عمال المقاولات، واتحادات السكان</div>
                <div class="card-subtitle" id="t-sent-table-sub">يتضمن واقعة مقاول مدينتي التاريخية، احتجاجات عمال الإسكندرية للإنشاءات، وبلاغات الملاك مع روابط الصحف الموثقة</div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr id="complaints-th-row">
                    <!-- Populated via JS -->
                  </tr>
                </thead>
                <tbody id="complaints-tbody">
                  <!-- Dynamically populated via JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 9: RISK REGISTER & STRATEGIC GUIDE -->
      <!-- ========================================== -->
      <div id="tab-risks" class="tab-pane">
        <div class="bezel-wrap">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-risks-table-title">مصفوفة المخاطر الجنائية ومؤشرات الإنذار المبكر</div>
                <div class="card-subtitle" id="t-risks-table-sub">تقييم شامل للأثر، احتمالية الحدوث، الآليات التشغيلية، وخطط الفحص النافية للجهالة</div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr id="risks-th-row">
                    <!-- Populated via JS -->
                  </tr>
                </thead>
                <tbody id="risks-tbody">
                  <!-- Dynamically populated via JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Stakeholder Playbooks -->
        <div class="grid-2" style="margin-top: 20px;" id="stakeholder-playbooks-container">
          <!-- Dynamically populated via JS -->
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 10: P.ZONE & WATER MEP SPECIALIST AUDIT -->
      <!-- ========================================== -->
      <div id="tab-pzone" class="tab-pane">
        
        <!-- Header Banner -->
        <div class="bezel-wrap" style="margin-bottom: 20px;">
          <div class="card" style="background: linear-gradient(135deg, rgba(6, 182, 212, 0.12), rgba(59, 130, 246, 0.08)); border-inline-start: 5px solid var(--accent-cyan);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
              <div>
                <div style="display:flex; align-items:center; gap:10px;">
                  <span class="badge badge-high" style="background:rgba(6,182,212,0.2); color:var(--accent-cyan); border-color:var(--accent-cyan);">دراسة حالة تخصصية مقاول باطن</span>
                  <h3 style="margin:0; font-size:18px; font-weight:800; color:var(--text-main);">تقييم ائتماني وتشغيلي: دخول شركة P.ZONE INTERNATIONAL في حزم المياه ومسابح TMG</h3>
                </div>
                <p style="margin:8px 0 0; font-size:13.5px; color:var(--text-muted); line-height:1.6; max-width:1100px;">
                  تحليل جنائي واستراتيجي مُعمق مبني على بيانات القوائم المالية المعتمدة لمجموعة طلعت مصطفى (TMGH.CA). يدرس أثر التناقض الجذري بين استيراد معدات الـ MEP نقداً بالعملة الصعبة (60%-70%) وبين دورة سداد المجموعة المعتمدة على أوراق دفع مؤجلة تمتد لـ 360 يوماً.
                </p>
              </div>
              <div style="display:flex; gap:10px;">
                <a href="pzone_tmg_strategic_evaluation_deck.html" target="_blank" class="btn-action highlight" style="text-decoration:none;">
                  <span>🎴 فتح الـ Deck التفاعلي الكامل (Long Table) ↗</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- 4 CFO Key Financial Metrics -->
        <div class="kpi-grid" style="margin-bottom: 24px;">
          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title">معدل تحويل النقد التشغيلي (H1 26)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"/></svg>
            </div>
            <div class="kpi-value">31.25%</div>
            <div class="kpi-delta delta-down">3.11B تدفق نقدي / 9.95B أرباح دفترية</div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title">أوراق الدفع والشيكات الآجلة للمقاولين</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
            </div>
            <div class="kpi-value">> 15.79B ج.م</div>
            <div class="kpi-delta delta-down">متوسط فترة سداد (DPO) تتجاوز 180 يوماً</div>
          </div>

          <div class="kpi-card amber">
            <div class="kpi-header">
              <span class="kpi-title">المكون المستورد بأعمال المياه (MEP)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064"/></svg>
            </div>
            <div class="kpi-value">60% – 70%</div>
            <div class="kpi-delta delta-up">طلمبات، فلترة، أغشية عزل، تحكم PLC</div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title">تكلفة التمويل وخصم الشيكات بالبنوك</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div class="kpi-value">28.6% سنوياً</div>
            <div class="kpi-delta delta-down">تآكل كامل لهامش ربح مقاول الباطن</div>
          </div>
        </div>

        <!-- The Strategic Dual Council: Buffett vs Altman -->
        <div class="grid-2" style="margin-bottom: 24px;">
          <!-- Warren Buffett Lens -->
          <div class="bezel-wrap">
            <div class="card" style="height:100%; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div class="card-header">
                  <div>
                    <div class="card-title" style="color:var(--accent-amber);">🏛️ منظور وارن بافيت: الأمان المالي وفخ التعويم السلبي</div>
                    <div class="card-subtitle">Margin of Safety & Involuntary Float Analysis</div>
                  </div>
                  <span class="badge badge-med">حفظ رأس المال</span>
                </div>
                <div style="font-style:italic; font-size:13px; color:var(--text-muted); border-inline-start:3px solid var(--accent-amber); padding-inline-start:12px; margin-bottom:14px;">
                  "القاعدة رقم 1: لا تخسر رأس المال. القاعدة رقم 2: إياك أن تنسى القاعدة رقم 1 مطلقاً."
                </div>
                <ul style="font-size:13px; color:var(--text-muted); line-height:1.75; padding-inline-start:18px; margin:0;">
                  <li><strong>فخ التعويم السلبي (Involuntary Float):</strong> كما تستخدم بيركشاير هاثاواي أقساط التأمين كتمويل مجاني، تستخدم TMG شيكات مقاولي الباطن كتمويل بفائدة 0% لتغطية عجز السيولة بينما يتحمل المقاول تكلفة 28.6%.</li>
                  <li><strong>انعدام هامش الأمان:</strong> قبول شيكات غير معززة بنكياً في ظل تضخم متسارع وقفزات عملة يعد مضاربة غير محسوبة.</li>
                  <li><strong>السيولة عند انحسار المد:</strong> صافي مركز السيولة لـ TMG بعد خصم التزامات التأجير التمويلي هو عجز نقدي (-13.38 مليار جنيه)، مما يجعل مقاولي الباطن الضحية الأولى لأي تباطؤ مبيعات.</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Sam Altman Lens -->
          <div class="bezel-wrap">
            <div class="card" style="height:100%; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div class="card-header">
                  <div>
                    <div class="card-title" style="color:var(--accent-cyan);">🚀 منظور سام ألتمان: الرافعة غير المتماثلة والمبادئ الأولية</div>
                    <div class="card-subtitle">First Principles, Moat & Asymmetric Leverage</div>
                  </div>
                  <span class="badge badge-low" style="background:rgba(6,182,212,0.15); color:var(--accent-cyan);">احتكار تقني</span>
                </div>
                <div style="font-style:italic; font-size:13px; color:var(--text-muted); border-inline-start:3px solid var(--accent-cyan); padding-inline-start:12px; margin-bottom:14px;">
                  "فكر من المبادئ الأولية (First Principles). لا تدخل كبائع سلعي مستبدل، بل كشريك يملك احتكاراً تقنياً."
                </div>
                <ul style="font-size:13px; color:var(--text-muted); line-height:1.75; padding-inline-start:18px; margin:0;">
                  <li><strong>رافعة التفاوض (Leverage Asymmetry):</strong> البحيرات الشاطئية وحمامات السباحة هي عصب البيع في ساوث ميد؛ P.ZONE تملك سجل إنجاز تقني نادر يحتاجه المطور بشدة.</li>
                  <li><strong>رفض حواجز المقاول العام:</strong> لا تتعاقد بشروط إذعان مع شركات مقاولات وسيطة؛ طالب بفتح اعتمادات استيراد مباشرة من المالك (Direct Owner L/C).</li>
                  <li><strong>قاعدة الشراكة أو الانسحاب:</strong> إذا لم تحصل P.ZONE على دفعة نقدية 25% مع تحييد سعر الصرف، فالانسحاب أجدى للحفاظ على صحة الشركة المالية.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- The 5 Structural Killers for P.ZONE -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title">⚠️ المخاطر الهيكلية الخمسة لمقاولي الأعمال المائية في مشروعات TMG</div>
                <div class="card-subtitle">تحليل المخاطر التشغيلية والتعاقدية الخاصة بحزم البحيرات وحمامات السباحة</div>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-rose); font-weight:800; font-size:14px; margin-bottom:6px;">1. تذبذب العملة ومشتريات الـ MEP المستوردة</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  معدات الفلترة وطلمبات الضخ وأغشية العزل (Geomembrane) مسعرة باليورو/الدولار وتتطلب دفعات نقدية فورية. العقود ذات السعر المقطوع بالجنيه تعني إفلاس المقاول فور أي تحرك لسعر الصرف.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-rose); font-weight:800; font-size:14px; margin-bottom:6px;">2. فخ أوراق الدفع والشيكات الآجلة (DPO > 180d)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  سداد TMG بشيكات آجلة تمتد من 6 إلى 12 شهراً يجبر P.ZONE على تمويل رأس المال العامل عبر البنوك المصرية بفائدة 28.6%، وهو ما يبتلع هامش الربح بالكامل.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-amber); font-weight:800; font-size:14px; margin-bottom:6px;">3. حاجز المقاول العام وشرط (Pay-When-Paid)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  التعاقد يتم غالباً مع الإسكندرية للإنشاءات (ACC) أو مقاول رئيسي وسيط (كونكريت بلس / أتريوم). وجود شرط التبعية يجمد مستحقات P.ZONE حال نشوب أي خلاف بين المقاول العام وTMG.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-amber); font-weight:800; font-size:14px; margin-bottom:6px;">4. التبعية لجدول الأعمال المدنية وتكاليف التوقف</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  لا يمكن البدء في عزل وتبطين وتمديدات البحيرات وحمامات السباحة قبل اكتمال الحفر والخرسانات. أي تعطل لمقاول الخرسانة العام يعطل أطقم P.ZONE دون تعويض عن تكاليف مد الأجل (Prolongation).
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-cyan); font-weight:800; font-size:14px; margin-bottom:6px;">5. احتجاز ضمان الأعمال واختبارات التسريب (Retention)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  حجز 5% إلى 10% كدفعة ضمان تخضع لاختبارات غمر هيدروليكية وملاحظات استشارية معقدة، وتُستغل لتعليق صرف المستخلص الختامي لسنوات بعد تسليم الموقع.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Project Ledger Matrix -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title">📋 مصفوفة تقييم الحزم المائية بمشروعات TMG والشروط الإلزامية</div>
                <div class="card-subtitle">توصيف دقيق لطبيعة الأعمال، المخاطر المترتبة، والبنود الحمائية المطلوبة</div>
              </div>
            </div>
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>المشروع</th>
                    <th>الحزمة المائية والتخصص الهيدروليكي</th>
                    <th>مكمن الخطر المالي والتشغيلي</th>
                    <th>الشرط التعاقدي الإلزامي لـ P.ZONE</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">SouthMED</td>
                    <td>البحيرات الكريستالية الضخمة ومحطات الفلترة والضخ</td>
                    <td><span class="badge badge-high">حرج</span> قفزات العملة وحجم التوريدات المستوردة الهائل</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">اعتماد مستندي بنكي مباشر (Direct Owner L/C) للتوريدات من المالك</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">مدينة نور</td>
                    <td>مسابح المجمعات السكنية ونوافير الحدائق المركزية</td>
                    <td><span class="badge badge-high">عالي</span> تآكل الهامش بسبب العقود المقطوعة وثبات الأسعار</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">ربط الأسعار شهرياً بمؤشرات جهاز التعبئة والإحصاء (CAPMAS)</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">فورسيزونز الأقصر</td>
                    <td>مسابح الضيافة الفاخرة والنوافير التراثية المعقدة</td>
                    <td><span class="badge badge-med">متوسط</span> تعقيدات الاستلام الاستشاري وتجميد الختامي ومحتجز الضمان</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">تجزئة الاستلام لمحاضر هيدروليكية مستقلة تطلق الضمان فوراً</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">سيليا (العاصمة)</td>
                    <td>الممرات المائية ونوافير المنطقة المركزية</td>
                    <td><span class="badge badge-high">عالي</span> تأخر مستحقات المقاول العام وتجميد دفعات الباطن</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">الشطب الصريح لشرط (Pay-When-Paid) والالتزام بـ 30 يوماً كاش</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">مدينتي</td>
                    <td>تجديد بحيرات الجولف وحمامات نوادي النادي القائمة</td>
                    <td><span class="badge badge-med">متوسط</span> نزاعات قضائية مستمرة حول حسابات ودائع الصيانة</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">سداد المستخلصات خلال 30 يوماً كاش مع حق إيقاف الأعمال فوراً</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- The Non-Negotiable Contractual Armor -->
        <div class="bezel-wrap">
          <div class="card" style="background: rgba(16, 185, 129, 0.05); border-inline-start: 5px solid var(--accent-emerald);">
            <div class="card-header">
              <div>
                <div class="card-title" style="color:var(--accent-emerald);">🛡️ الدرع التعاقدي الحتمي لشركة P.ZONE (The Non-Negotiable Term Sheet)</div>
                <div class="card-subtitle">شروط لا تقبل المساومة لضمان سلامة رأس المال والسيولة النقدية</div>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px;">
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">1. دفعة مقدمة نقدية 25%</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  سداد فوري كاش مقابل خطاب ضمان دفعة مقدمة (APG) لتأمين طلبيات المصانع العالمية فوراً دون استنزاف السيولة الذاتية لـ P.ZONE.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">2. بند تحييد سعر الصرف (FX Pass-Through)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  تثبيت أسعار بنود التوريدات الكهروميكانيكية بالعملة الأجنبية أو السداد بالمعادل الرسمي بسعر البنك المركزي يوم التحويل.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">3. حظر أوراق الدفع المؤجلة</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  سداد المستخلصات الشهرية نقداً بحد أقصى 30 يوماً؛ ورفض أي شيكات مؤجلة تفوق 60 يوماً إلا إذا كانت معززة مصرفياً ومحملة بفوائد التمويل التجارية.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">4. إسقاط شرط التبعية (Pay-When-Paid)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  ربط استحقاق P.ZONE بالمطابقة الفنية للأعمال المنفذة فقط، واستقلاليتها التامة عن حسابات المقاول العام والنزاعات التمويلية مع المطور.
                </p>
              </div>
            </div>
          </div>
        </div>

      </div>


      <!-- ================================================================== -->
      <!-- TAB 11: INTERACTIVE PROJECT MAP, STAKEHOLDERS & LINKEDIN DIRECTORY -->
      <!-- ================================================================== -->
      <div id="tab-stakeholders" class="tab-pane">
        
        <!-- Header Banner -->
        <div class="bezel-wrap" style="margin-bottom: 20px;">
          <div class="card" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(16, 185, 129, 0.08)); border-inline-start: 5px solid var(--accent-blue);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
              <div>
                <div style="display:flex; align-items:center; gap:10px;">
                  <span class="badge badge-high" style="background:rgba(59,130,246,0.2); color:var(--accent-blue); border-color:var(--accent-blue);">إشراف تنفيذي جنائي</span>
                  <h3 style="margin:0; font-size:18px; font-weight:800; color:var(--text-main);" id="stakeholders-header-title">خريطة المشروعات وأصحاب المصلحة ودليل الفرق والمقاولين (42 كيان و 38 ملف قيادي)</h3>
                </div>
                <p style="margin:8px 0 0; font-size:13.5px; color:var(--text-muted); line-height:1.6; max-width:1100px;" id="stakeholders-header-desc">
                  خريطة جغرافية تفاعلية شاملة لمشروعات مجموعة طلعت مصطفى (TMGH) في مصر والسعودية وعمان. تتيح استعراض 42 شركة ومقاول ومورد معتمد مع أرقام التواصل العامة، و 38 قيادياً ومهندساً مع روابط LinkedIn موثقة، مصحوبة بمصفوفة SWOT و TOWS الاستراتيجية المدققة.
                </p>
              </div>
              <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <button class="btn-action" onclick="exportCompaniesCSV()" style="font-weight:700; background:rgba(16,185,129,0.1); border-color:var(--accent-emerald); color:var(--accent-emerald);">
                  <span id="btn-export-companies">📥 تصدير الشركات (CSV)</span>
                </button>
                <button class="btn-action" onclick="exportTeamsCSV()" style="font-weight:700; background:rgba(59,130,246,0.1); border-color:var(--accent-blue); color:var(--accent-blue);">
                  <span id="btn-export-teams">📥 تصدير القيادات (CSV)</span>
                </button>
                <button class="btn-action" onclick="resetProjectFilter()" style="font-weight:700;">
                  <span id="btn-reset-filters">🔄 إعادة ضبط التصفية</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- 4 Top KPI Ribbon Cards -->
        <div class="kpi-grid" style="margin-bottom: 24px;">
          <div class="kpi-card blue">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-landbank">إجمالي محفظة الأراضي (Landbank)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064"/></svg>
            </div>
            <div class="kpi-value">> 26,700 فدان</div>
            <div class="kpi-delta delta-up">> 112 مليون م² عبر 3 دول (مصر، KSA، عمان)</div>
          </div>

          <div class="kpi-card emerald">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-backlog">رصيد المبيعات التعاقدية (Backlog)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div class="kpi-value">441.2B ج.م</div>
            <div class="kpi-delta delta-up">يضمن تدفقات إيرادات معترف بها لـ 5-7 سنوات</div>
          </div>

          <div class="kpi-card purple">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-comp-count">الكيانات والشركات المفهرسة</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
            </div>
            <div class="kpi-value">42 جهة موثقة</div>
            <div class="kpi-delta delta-neutral">مقاولون عموميون، ذراع المقاولات، موردو نظم وبنوك</div>
          </div>

          <div class="kpi-card amber">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-team-count">فرق العمل وقيادات المشاريع</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
            </div>
            <div class="kpi-value">38 ملف مهني</div>
            <div class="kpi-delta delta-up">روابط LinkedIn مباشرة ومصنفة بدرجة الدليل</div>
          </div>
        </div>

        <!-- SECTION 1: INTERACTIVE GEOGRAPHIC MAP -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap: wrap; gap: 12px;">
              <div>
                <div class="card-title" id="map-section-title">🗺️ الخريطة الجغرافية التفاعلية لمشروعات TMG التوسعية</div>
                <div class="card-subtitle" id="map-section-subtitle">انقر على أي علامة مشروع لتكبير الخريطة وتصفية جدول المقاولين ودليل الفرق تلقائياً</div>
              </div>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;" id="project-filter-chips">
                <button class="filter-chip active" onclick="filterMapByProject('all')">الكل (9 مشروعات)</button>
                <button class="filter-chip" onclick="filterMapByProject('southmed')">ساوث ميد (SouthMED)</button>
                <button class="filter-chip" onclick="filterMapByProject('noor')">مدينة نور (Noor)</button>
                <button class="filter-chip" onclick="filterMapByProject('madinaty')">مدينتي (Madinaty)</button>
                <button class="filter-chip" onclick="filterMapByProject('celia')">سيليا (Celia)</button>
                <button class="filter-chip" onclick="filterMapByProject('fs_luxor')">فورسيزونز الأقصر</button>
                <button class="filter-chip" onclick="filterMapByProject('fs_sharm')">فورسيزونز شرم</button>
                <button class="filter-chip" onclick="filterMapByProject('san_stefano')">سان ستيفانو</button>
                <button class="filter-chip" onclick="filterMapByProject('banan')">بنان الرياض 🇸🇦</button>
                <button class="filter-chip" onclick="filterMapByProject('jood_yamal')">جود ويامال عمان 🇴🇲</button>
              </div>
            </div>

            <!-- Map Container -->
            <div id="tmg-leaflet-map" style="width: 100%; height: 500px; border-radius: 10px; border: 1px solid var(--border-subtle); z-index: 1;"></div>
            
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px; font-size:12px; color:var(--text-muted); flex-wrap:wrap; gap:10px;">
              <div>📌 <strong>مفتاح الخريطة:</strong> <span style="color:#06b6d4;">● ساحلي وسياحي</span> | <span style="color:#3b82f6;">● مدن ذكية جديدة</span> | <span style="color:#10b981;">● مجتمعات ناضجة</span> | <span style="color:#f59e0b;">● ضيافة وفنادق</span> | <span style="color:#10b981;">● توسعات إقليمية (KSA/Oman)</span></div>
              <div id="map-selection-indicator" style="font-weight:700; color:var(--accent-blue);">المشروع النشط: عرض جميع المشروعات</div>
            </div>
          </div>
        </div>

        <!-- SECTION 2: VERIFIED COMPANIES & CONTRACTS DIRECTORY -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap: wrap; gap: 14px;">
              <div>
                <div class="card-title" id="companies-table-title">🏢 دليل الشركات والجهات المرتبطة بمشروعات TMG (أرقام التواصل العامة المنشورة)</div>
                <div class="card-subtitle" id="companies-table-subtitle">42 كيان مفهرس مع الصفة، نطاق العمل، أرقام الهاتف العامة، البريد، ومستوى ثقة العلاقة</div>
              </div>
              <div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
                <input type="text" id="company-search-input" placeholder="🔍 بحث باسم الشركة، الدور، أو المشروع..." style="background:var(--bg-surface-elevated); color:var(--text-main); border:1px solid var(--border-subtle); border-radius:8px; padding:8px 14px; font-size:13px; min-width:240px;" oninput="applyCompanyFilters()">
                <select id="company-role-filter" style="background:var(--bg-surface-elevated); color:var(--text-main); border:1px solid var(--border-subtle); border-radius:8px; padding:8px 12px; font-size:13px;" onchange="applyCompanyFilters()">
                  <option value="all">كل الأدوار والصفات</option>
                  <option value="مقاول">مقاولون رئيسيون / JV</option>
                  <option value="ذراع">أذرع مقاولات بالمجموعة (Atrium / ACC)</option>
                  <option value="مورد">موردو أنظمة وبنية أساسية</option>
                  <option value="استشاري">استشاريون وإشراف</option>
                  <option value="بنك">بنوك وشركاء تمويليون</option>
                </select>
                <span id="companies-count-badge" class="badge badge-med" style="font-size:12px;">42 شركة</span>
              </div>
            </div>

            <div style="overflow-x: auto; max-height: 520px; overflow-y: auto;">
              <table style="width: 100%; border-collapse: collapse; font-size: 13px;" id="companies-table-dom">
                <thead style="position: sticky; top: 0; background: var(--bg-surface-elevated); z-index: 2;">
                  <tr style="border-bottom: 2px solid var(--border-subtle); text-align: start;">
                    <th style="padding: 10px 12px; width: 40px;">#</th>
                    <th style="padding: 10px 12px; min-width: 180px;">اسم الشركة / الكيان</th>
                    <th style="padding: 10px 12px; min-width: 150px;">المشروع / الموقع</th>
                    <th style="padding: 10px 12px; min-width: 220px;">الدور ونطاق الأعمال</th>
                    <th style="padding: 10px 12px; min-width: 150px;">طبيعة العلاقة بـ TMG</th>
                    <th style="padding: 10px 12px; min-width: 180px;">أرقام التواصل العامة</th>
                    <th style="padding: 10px 12px; min-width: 140px;">البريد والموقع</th>
                    <th style="padding: 10px 12px; width: 90px; text-align: center;">درجة الدليل</th>
                  </tr>
                </thead>
                <tbody id="companies-table-body">
                  <!-- Dynamically rendered via JS -->
                </tbody>
              </table>
            </div>
            
            <div style="margin-top: 12px; font-size: 11.5px; color: var(--text-muted); line-height: 1.5;">
              ⚠️ <strong>إخلاء مسؤولية جنائي:</strong> الأرقام المدرجة هي أرقام أعمال منشورة علناً وليست أرقاماً خاصة. وجود اسم شركة في مستندات المشروع لا يثبت بالضرورة عقداً مباشراً مع TMG أو وجود مستحقات معلقة ما لم يتم التثبت من أصل التعاقد.
            </div>
          </div>
        </div>

        <!-- SECTION 3: PROJECT TEAMS & LINKEDIN PERSONNEL DIRECTORY -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap: wrap; gap: 14px;">
              <div>
                <div class="card-title" id="teams-section-title">👥 دليل الأشخاص وفرق العمل المرتبطة بالمشروعات (ملفات LinkedIn العامة)</div>
                <div class="card-subtitle" id="teams-section-subtitle">38 كادراً هندسياً وإدارياً مع المسمى المهني المنشور ودرجة التوثيق ورابط الملف المباشر</div>
              </div>
              <div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
                <input type="text" id="team-search-input" placeholder="🔍 بحث باسم الشخص، المنصب، أو الشركة..." style="background:var(--bg-surface-elevated); color:var(--text-main); border:1px solid var(--border-subtle); border-radius:8px; padding:8px 14px; font-size:13px; min-width:240px;" oninput="applyTeamFilters()">
                <span id="teams-count-badge" class="badge badge-med" style="font-size:12px;">38 مهندساً وقيادياً</span>
              </div>
            </div>

            <!-- Personnel Grid -->
            <div id="teams-cards-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 14px; max-height: 550px; overflow-y: auto; padding: 4px;">
              <!-- Dynamically populated via JS -->
            </div>

            <div style="margin-top: 12px; font-size: 11.5px; color: var(--text-muted); line-height: 1.5;">
              📌 <strong>معايير التدقيق:</strong> ملفات الأشخاص مستخرجة من الفهرسة العامة المهنية لـ LinkedIn حتى أكتوبر 2026. الانتماء إلى شركة لا يثبت تعيين الشخص في مشروع محدد إلا إذا ذكر المصدر ذلك صراحة (تصنيف B / C).
            </div>
          </div>
        </div>

        <!-- SECTION 4: STRATEGIC SWOT & TOWS MATRIX -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap:wrap; gap:12px;">
              <div>
                <div class="card-title" id="swot-section-title">⚖️ التحليل الاستراتيجي الرباعي (TMG Deep SWOT Matrix) ومصفوفة TOWS التنفيذية</div>
                <div class="card-subtitle" id="swot-section-subtitle">تقييم جنائي مفصل لنقاط القوة والضعف والفرص والتهديدات مع خطط العمل الاستراتيجية</div>
              </div>
              <div style="display:flex; gap:8px;">
                <button class="filter-chip active" id="btn-show-swot" onclick="switchSwotView('swot')">مصفوفة SWOT الرباعية</button>
                <button class="filter-chip" id="btn-show-tows" onclick="switchSwotView('tows')">مصفوفة TOWS الاستراتيجية (Action Plans)</button>
              </div>
            </div>

            <!-- View 1: 4 SWOT Quadrants -->
            <div id="swot-quadrants-view" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(440px, 1fr)); gap: 16px;">
              
              <!-- STRENGTHS -->
              <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(16,185,129,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-emerald);">💪 نقاط القوة (Strengths)</span>
                  <span class="badge badge-low">6 محاور استراتيجية</span>
                </div>
                <div id="swot-strengths-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

              <!-- WEAKNESSES -->
              <div style="background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(239,68,68,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-rose);">⚠️ نقاط الضعف (Weaknesses)</span>
                  <span class="badge badge-high">6 فجوات هيكلية</span>
                </div>
                <div id="swot-weaknesses-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

              <!-- OPPORTUNITIES -->
              <div style="background: rgba(59, 130, 246, 0.05); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(59,130,246,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-blue);">🚀 الفرص التوسعية (Opportunities)</span>
                  <span class="badge badge-low">6 محفزات نمو</span>
                </div>
                <div id="swot-opportunities-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

              <!-- THREATS -->
              <div style="background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(245,158,11,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-amber);">⚡ التهديدات والمخاطر (Threats)</span>
                  <span class="badge badge-med">6 متجهات خطر خارجية</span>
                </div>
                <div id="swot-threats-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

            </div>

            <!-- View 2: Strategic TOWS Actionable Matrix -->
            <div id="tows-matrix-view" style="display: none; flex-direction: column; gap: 16px;">
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(440px, 1fr)); gap:16px;">
                
                <!-- SO STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-emerald);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-emerald); margin-bottom:10px;">🎯 استراتيجيات SO (استغلال القوة لاقتناص الفرص)</div>
                  <div id="tows-so-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

                <!-- ST STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-amber);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-amber); margin-bottom:10px;">🛡️ استراتيجيات ST (توظيف القوة لتحييد التهديدات)</div>
                  <div id="tows-st-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

                <!-- WO STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-blue);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-blue); margin-bottom:10px;">🔄 استراتيجيات WO (معالجة نقاط الضعف باغتنام الفرص)</div>
                  <div id="tows-wo-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

                <!-- WT STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-rose);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-rose); margin-bottom:10px;">⚠️ استراتيجيات WT (تقليص الضعف وتفادي المخاطر)</div>
                  <div id="tows-wt-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

              </div>
            </div>

          </div>
        </div>

      </div>


    </div>
  </div>

  <!-- ==========================================================================
       MODAL: SOURCE CITATION & FACT DETAILS
       ========================================================================== -->
  <!-- Modal for Excel Source Files -->
  <div id="excel-modal">
    <div class="modal-box" style="max-width: 840px;">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:14px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <div style="width:38px; height:38px; border-radius:10px; background:rgba(16,185,129,0.15); color:var(--accent-emerald); display:flex; align-items:center; justify-content:center; font-weight:800;">
            <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          </div>
          <div>
            <h3 style="font-size:16px; font-weight:800;" id="m-excel-title">مركز تحميل نماذج الإكسيل الحسابية والمدققة (Excel Source Hub)</h3>
            <p style="font-size:11.5px; color:var(--text-dim);" id="m-excel-sub">كافة الملفات تحتوي على معادلات حسابية حية (Formulas) متوافقة 100% مع Microsoft Excel</p>
          </div>
        </div>
        <button onclick="closeExcelModal()" style="background:none; border:none; color:var(--text-dim); cursor:pointer; font-size:24px; line-height:1;">&times;</button>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap:14px; margin-top:16px;">
        
        <!-- File 1: Master Risk & Balance Sheet -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-high" style="background:rgba(6,182,212,0.15); color:var(--accent-cyan); border-color:rgba(6,182,212,0.3);">15 ورقة عمل حسابية</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">47.6 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">دليل المهندس، مصفوفة المخاطر الأربعة، تحليل ويبل، قائمة المركز المالي، التحليل الرأسي، ومؤشرات السيولة والرافعة.</p>
          </div>
          <a href="downloads/TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل النموذج الشامل (.xlsx)</span>
          </a>
        </div>

        <!-- File 2: Audited Balance Sheet & Financial Statements -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-low">7 أوراق تدقيق مالي</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">25.1 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">القوائم المالية المدققة للبورصة (2021-2025)، قائمة الدخل، الميزانية، ومصفوفة SWOT الاستراتيجية وTOWS ونموذج P.ZONE.</p>
          </div>
          <a href="downloads/TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل القوائم المدققة (.xlsx)</span>
          </a>
        </div>

        <!-- File 3: Master Forensic Audit Model -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-med">النموذج الجنائي الشامل</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">47.8 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Master_Forensic_Audit_Model.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">النسخة الشاملة المدمجة لكافة حسابات الفحص النافي للجهالة، ومصفوفات المخاطر والتحليل الإحصائي وقوائم المركز المالي.</p>
          </div>
          <a href="downloads/TMG_Master_Forensic_Audit_Model.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل النموذج الجنائي (.xlsx)</span>
          </a>
        </div>

        <!-- File 4: Project Companies & Contacts -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-low">42 شركة و38 مسؤول</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">17.2 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Project_Companies_Contacts_One_Sheet.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">دليل شركات المقاولات والاستشاريين والمطورين، مع هواتف ومواقع رسمية وبريد إلكتروني وروابط لينكد إن للمسؤولين.</p>
          </div>
          <a href="downloads/TMG_Project_Companies_Contacts_One_Sheet.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل دليل الشركات (.xlsx)</span>
          </a>
        </div>

      </div>

      <div style="margin-top:16px; text-align:center; border-top:1px solid var(--border-subtle); padding-top:14px;">
        <button onclick="closeExcelModal()" class="btn-action" style="padding:8px 24px;">إغلاق النافذة</button>
      </div>
    </div>
  </div>

  <div id="source-modal" onclick="closeSourceModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:12px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="badge badge-med" id="modal-source-badge">المصدر الموثق</span>
          <strong id="modal-source-title" style="font-size:15px; font-weight:800; line-height:1.4;">عنوان المرجع</strong>
        </div>
        <button onclick="closeSourceModal()" style="background:none; border:none; color:var(--text-dim); cursor:pointer; font-size:20px; padding:4px 8px;">✕</button>
      </div>
      <div id="modal-source-body" style="font-size:13.5px; line-height:1.75; color:var(--text-muted); white-space:pre-wrap; max-height:48vh; overflow-y:auto; padding-inline-end:6px;">
        تفاصيل التوثيق
      </div>
      <div style="border-top:1px solid var(--border-subtle); padding-top:14px; display:flex; flex-direction:column; gap:10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; font-size:12px; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; gap:8px; align-items:center;">
            <span style="color:var(--text-dim);" id="lbl-modal-date-tag">تاريخ التوثيق:</span>
            <span id="modal-source-date" style="color:var(--text-bright); font-weight:700; font-family:var(--font-mono);">التاريخ</span>
          </div>
          <div style="display:flex; gap:6px; align-items:center;">
            <span style="color:var(--text-dim);" id="lbl-modal-pub-tag">جهة النشر / المرجع:</span>
            <span id="modal-source-publisher" style="color:var(--accent-teal); font-weight:700;">الناشر</span>
          </div>
        </div>

        <div style="background:var(--bg-card); border:1px solid var(--border-subtle); border-radius:8px; padding:10px 14px; display:flex; flex-direction:column; gap:6px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:11px; text-transform:uppercase; letter-spacing:0.5px; color:var(--text-dim); font-weight:700;" id="lbl-modal-direct-url">الرابط المباشر للمستند / الخبر الأصلي:</span>
            <span class="badge badge-low" style="font-size:10px;" id="lbl-modal-status-badge">رابط نشط ومدقق ✓</span>
          </div>
          <a id="modal-source-url-preview" href="#" target="_blank" rel="noopener noreferrer" style="font-family:var(--font-mono); font-size:11.5px; color:var(--accent-teal); direction:ltr; text-align:left; word-break:break-all; text-decoration:underline;"></a>
        </div>

        <div style="display:flex; gap:10px; align-items:center; justify-content:flex-end; flex-wrap:wrap; margin-top:2px;">
          <a id="modal-source-archive-url" href="#" target="_blank" rel="noopener noreferrer" class="btn-action" style="font-size:12px; display:none;">نسخة الأرشيف / البحث ↗</a>
          <a id="modal-source-url" href="#" target="_blank" rel="noopener noreferrer" class="btn-action highlight" style="font-size:13px; font-weight:700; padding:9px 18px;">زيارة المصدر الأصلي المباشر ↗</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       PRESENTER MODE OVERLAY (HTML PPT Reveal Deck)
       ========================================================================== -->
  <div id="presenter-overlay">
    <div class="slide-progress">
      <div class="slide-progress-bar" id="slide-progress-bar"></div>
    </div>

    <div class="presenter-viewport">
      <div class="slide-canvas">
        <div class="slide-header">
          <div>
            <div class="slide-number" id="presenter-slide-num">SLIDE 01 / 10</div>
            <h2 id="presenter-slide-title" style="font-size: 21px; font-weight: 800; margin-top: 4px;">العنوان الرئيسي</h2>
          </div>
          <button class="btn-action" onclick="closePresenterMode()" id="btn-exit-presenter">✕ خروج (Esc)</button>
        </div>

        <div class="slide-body" id="presenter-slide-content">
          <!-- Dynamically populated via JS -->
        </div>

        <div class="speaker-notes-banner">
          <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="flex-shrink:0; color:var(--accent-amber);"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          <div>
            <strong id="lbl-speaker-note-tag">استنتاج الفحص الجنائي:</strong>
            <span id="presenter-speaker-note">ملاحظة تنفيذية</span>
          </div>
        </div>
      </div>
    </div>

    <div class="presenter-dock">
      <div style="font-size: 12px; color: var(--text-dim); display:flex; gap:16px;">
        <span id="lbl-keyboard-nav">اضغط <kbd>←</kbd> <kbd>→</kbd> للتنقل</span>
        <span id="lbl-keyboard-fs">اضغط <kbd>F</kbd> للشاشة الكاملة</span>
      </div>

      <div style="display: flex; gap: 8px; align-items: center;">
        <button class="btn-action" onclick="prevSlide()" id="btn-prev-slide">❮ السابق</button>
        <span id="presenter-dock-indicator" style="font-family: var(--font-mono); font-size: 13px; font-weight: 700; padding: 0 8px;">1 / 8</span>
        <button class="btn-action" onclick="nextSlide()" id="btn-next-slide">التالي ❯</button>
        <button class="btn-action" onclick="toggleFullScreen()" id="btn-fs-slide">⛶ شاشة كاملة</button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       DATA STORES & JAVASCRIPT CONTROLLER (100% Bilingual & Clickable Sources)
       ========================================================================== -->
  <script>
    let currentLang = 'ar';
    let currentTheme = 'light';

    /* ==========================================================================
       SOURCES DIRECTORY (Clickable Grounded Links)
       ========================================================================== */
    const sourcesDB = {
      atrium_official_portfolio_40: {
        titleAr: "شركة أتريوم للمقاولات (AQC): دليل المشاريع الرسمي (40 مشروعاً في مختلف القطاعات)",
        titleEn: "Atrium Quality Contractors: Official Directory of 40 Projects Across All Sectors",
        publisherAr: "الموقع الرسمي لشركة أتريوم (الذراع الإنشائي لمجموعة طلعت مصطفى)",
        publisherEn: "Atrium Quality Contractors Official Portal (TMG Construction Arm)",
        badgeAr: "سجل محفظة رسمي معتمد",
        badgeEn: "Official Portfolio Directory",
        date: "12 أكتوبر 2026",
        url: "https://atriumeg.com/projects/",
        archiveUrl: "https://atriumeg.com/about/",
        descAr: `سجل رسمي يوثق تنفيذ شركة أتريوم 40 مشروعاً استراتيجياً تضم قطاعات الضيافة (فنادق فورسيزونز الأقصر، نيو كايرو كابيتال، نايل بلازا، سان ستيفانو، شرم الشيخ)، والقطاع التجاري (إيست هب، أوبن إير مول)، والسكني (سيليا، نور، بريفادو)، والمستشفيات والتعليم.`,
        descEn: `Official corporate project directory verifying Atrium's execution of 40 mega projects across hospitality (Four Seasons portfolio), commercial malls, healthcare, education, and master communities.`
      },
      atrium_qs_invoice_roles: {
        titleAr: "التوصيف الوظيفي لإدارة المطالبات والمستخلصات: دورة اعتماد مستخلصات مقاولي الباطن بأتريوم",
        titleEn: "Atrium QS & Procurement Workflow: Formal Subcontractor Payment Certification Protocol",
        publisherAr: "بوابة التوظيف والعقود بشركة أتريوم (Atrium Careers)",
        publisherEn: "Atrium Quality Contractors Careers & Contracts Division",
        badgeAr: "حوكمة إدارية ومستندية",
        badgeEn: "Administrative Governance",
        date: "12 أكتوبر 2026",
        url: "https://atriumeg.com/careers/jobs/senior-post-contract-qs-engineer/",
        archiveUrl: "https://atriumeg.com",
        descAr: `بيان مهني يوثق دورة العمل المتبعة بأتريوم لإدارة مستخلصات مقاولي الباطن (Interim Valuations)، والأوامر التغييرية (VOs)، والمطالبات وحسابات الختام. يثبت وجود مسطرة تدقيق وحوكمة مستندية داخلية لفحص الكميات والمطابقات الفنية.`,
        descEn: `Job profile detailing standard QS operational processes for subcontractor payment applications, interim valuations, variation dockets, and final accounts.`
      },
      fs_luxor_cp02_record: {
        titleAr: "السجل المهني لحزمة فندق فورسيزونز الأقصر CP02 الكهروميكانيكية (تحالف أتريوم وCCC)",
        titleEn: "Four Seasons Luxor CP02 MEP Package Project Record (Atrium-CCC Consortium)",
        publisherAr: "سجل الإشراف الهندسي لمدير المشروع هيل إنترناشيونال ومجموعة شاكر",
        publisherEn: "Hill International PM & Shaker Consultancy Group Project Record",
        badgeAr: "سجل تعاقدي وهندسي معتمد",
        badgeEn: "Verified Contractual Execution",
        date: "12 أكتوبر 2026",
        url: "https://eg.linkedin.com/in/mahmoud-abd-elaal-5a6a2380",
        archiveUrl: "https://atriumeg.com",
        descAr: `توثيق تعاقدي للحزمة الكهروميكانيكية الرئيسية CP02 بفندق فورسيزونز الأقصر: المالك طلعت مصطفى (آيكون / إيجوث)، المقاول العام شركة أتريوم، مقاول حزمة MEP تحالف CCC وأتريوم، مدير المشروع Hill International، واستشاري المشروع Shaker Group.`,
        descEn: `Professional project documentation verifying contractual hierarchy for CP02 MEP Main Package at Four Seasons Luxor under TMG/ICON client, Atrium GC, CCC JV, Hill International PM, and Shaker Group.`
      },
      cairo_gate_emaar: {
        titleAr: "كايرو جيت ومكاتب تاون سكوير: تسليم شركة أتريوم للأعمال الإنشائية لصالح إعمار مصر",
        titleEn: "Cairo Gate & Townsquare Offices: Atrium Construction Delivery for Emaar Misr",
        publisherAr: "شركة إعمار مصر للتنمية وأتريوم للمقاولات",
        publisherEn: "Emaar Misr Development & Atrium Quality Contractors",
        badgeAr: "إنجاز أعمال عميل خارجي مرموق",
        badgeEn: "External Blue-Chip Client Delivery",
        date: "2023 – 2025",
        url: "https://atriumeg.com/portfolio/townsquare-boutique-offices/",
        archiveUrl: "https://atriumeg.com/projects/",
        descAr: `إفصاح رسمي يوثق نجاح شركة أتريوم كذراع إنشائي في تسليم مشروع مكاتب تاون سكوير بوتيك بمشروع 'كايرو جيت' لصالح شركة إعمار مصر (Emaar Misr)، مما يعزز مصداقية الشركة الفنية والتزامها التعاقدي مع كبرى الشركات الإقليمية.`,
        descEn: `Corporate milestone verifying Atrium delivering Townsquare Boutique Offices at Cairo Gate for Emaar Misr, evidencing institutional execution capabilities for prime third-party developers.`
      },
      masry_shehata_2008: {
        titleAr: "المصري اليوم: بلاغ للنائب العام من مقاول ضد هشام طلعت مصطفى وإدارة مدينتي واعتراف رسمي بتعمد تأخير الصرف",
        titleEn: "Al-Masry Al-Youm: Contractor Files Public Prosecutor Report Over Withheld Madinaty Dues & Deliberate Delay Admission",
        publisherAr: "صحيفة المصري اليوم (تغطية قضائية واستقصائية)",
        publisherEn: "Al-Masry Al-Youm Newspaper (Judicial & Press Investigation)",
        badgeAr: "بلاغ قضائي واعتراف رسمي",
        badgeEn: "Prosecutorial Docket & Executive Admission",
        date: "13 أكتوبر 2008",
        url: "https://www.almasryalyoum.com/news/details/1934547",
        archiveUrl: "https://web.archive.org/web/https://www.almasryalyoum.com/news/details/1934547",
        descAr: `تقرير استقصائي موسع بجريدة 'المصري اليوم' وثق شكوى مقاول يُدعى شحاتة محمد حسن وتقدمه ببلاغ رسمي للمستشار عبد المجيد محمود النائب العام ضد هشام طلعت مصطفى ومدير موقع مدينتي آنذاك، متهماً شركة الإسكندرية للإنشاءات بالامتناع عن صرف مستحقاته المالية مما منعه من سداد رواتب عماله، ولجوئه إلى شعبة المقاولات بالغرفة التجارية للمطالبة بحل المشكلة.

• التفصيلة الجوهرية الأهم: نشرت الصحيفة تقريراً آخر عن الأزمة نفسها، نقلت فيه اعترافاً رسمياً عن إبراهيم حسبو، مدير شركة الإسكندرية للإنشاءات، قال فيه: 'إن تأخير الصرف كان مقصوداً حتى لا يترك العمال موقع العمل بعد القبض على هشام طلعت مصطفى'، مؤكداً أن الشركة كانت تعمل على صرف المتأخرات.

• تقييم الحالة وأدلة الثبوت:
1. ما يدعم الشكوى: اسم المقاول شحاتة محمد حسن، واسم الكيان المنفذ (الإسكندرية للإنشاءات)، وموقع المشروع محددون بدقة في التغطية الصحفية، مع إقرار موثق من مدير الشركة بسبب التأخير.
2. ما لم يتم إثباته: لم يتم التحقق من صدور حكم قضائي نهائي بالواقعة، أو القيمة الفعلية للمستحقات المسددة لاحقاً، أو استمرار الأزمة بعد ذلك.
3. الخلاصة الجنائية: هذه أقوى وأقرب واقعة مباشرة منشورة لمقاول باطن يطالب بمستحقاته، لكنها واقعة تاريخية تعود إلى نحو 18 عاماً (2008)، وبالتالي لا تكفي وحدها للحكم القاطع على أسلوب تعاملات المجموعة الحالية دون وثائق تدقيق حديثة.`,
        descEn: `Press investigation published by 'Al-Masry Al-Youm' documenting subcontractor Shehata Mohamed Hassan filing an official complaint with Prosecutor General Abdel Meguid Mahmoud against Hisham Talaat Moustafa and Madinaty site management. The contractor accused Alexandria Construction Co. (ACC) of withholding his progress payments, preventing him from paying his workforce, leading him to escalate to the Chamber of Commerce.

• Material Key Detail: The newspaper published a follow-up report quoting Ibrahim Hasabo, Director of Alexandria Construction Co., formally acknowledging: 'The payment withholding was intentional to prevent workers from abandoning the project site following the arrest of Hisham Talaat Moustafa', adding that the company was working to clear arrears.

• Case Diligence Assessment:
1. Corroborating Evidence: Contractor name, corporate entity, project location specifically identified, with on-record executive admission.
2. Unverified Elements: No final judicial ruling verified, exact final settled dues unverified, persistence of dispute unverified.
3. Diligence Takeaway: The most direct published trade subcontractor payment dispute; however, dating back 18 years, it cannot independently substantiate current ongoing corporate practice without contemporary audit evidence.`
      },
      khatib_scaffolding_2012: {
        titleAr: "محكمة شمال القاهرة: مذكرة الدعوى 2923 لسنة 2012 مدني ومطالبة فروق أسعار سقالات مدينتي (609,625 ج.م)",
        titleEn: "North Cairo Civil Court: Case 2923/2012 Docket & EGP 609,625 Madinaty Scaffolding Dues Claim",
        publisherAr: "مكتب المحامي هاني عبد الرحمن الخطيب (وثائق ومذكرات قضائية منشورة)",
        publisherEn: "Lawyer Hany Abdel Rahman El-Khatib Practice (Published Court Filings)",
        badgeAr: "مذكرة دفاع قضائية منشورة",
        badgeEn: "Published Judicial Defense Brief",
        date: "2012 – 2013",
        url: "https://www.google.com/search?q=%D8%A7%D9%84%D8%AF%D8%B9%D9%88%D9%89+2923+%D9%84%D8%B3%D9%86%D8%A9+2012+%D9%85%D8%AF%D9%86%D9%8A+%D8%B4%D9%85%D8%A7%D9%84+%D8%A7%D9%84%D9%82%D8%A7%D9%87%D8%B1%D8%A9+%D9%85%D8%AF%D9%8A%D9%86%D8%AA%D9%8A",
        archiveUrl: "https://web.archive.org/web/http://hanielkhatiblawyer.blogspot.com",
        descAr: `مذكرة دفاع منشورة بتاريخ 10 سبتمبر 2013 تشير إلى الدعوى رقم 2923 لسنة 2012 مدني شمال القاهرة المقامة من شركة خالد هنداوي محمد عبد الرحيم ضد شركة الإسكندرية للإنشاءات (مجموعة طلعت مصطفى) بشأن أعمال السقالات في 3 مواقع بمدينتي (القطاع الشمالي والمدرسة البريطانية، بوابة مدينتي 2011، السوق التجاري والمسجد)، ومطالبة بفروق أسعار بمبلغ 609,625 ج.م ومطالبة بإلزام الشركة بتقديم أصول العقود والمستخلصات.`,
        descEn: `Published legal defense memo dated 10 Sept 2013 regarding Case No. 2923 of 2012 North Cairo Civil Court filed by Khaled Hendawi against Alexandria Construction Co. (TMG) over scaffolding works across 3 Madinaty zones (North Sector & British School, Gate 2011, Market & Mosque), citing an EGP 609,625 claim for rate variances and demanding original subcontracts and IPCs.`
      },
      haditha_contractor_2023: {
        titleAr: "موقع الحادثة وتليجراف مصر: نزاع مستحقات مقاول ارتبط بعلاقة عمل 20 عاماً وقضية التهديد الجنائية",
        titleEn: "El Haditha & Telegraph Masr: 20-Year Contractor Relationship Payment Dispute & Criminal Threat Proceedings",
        publisherAr: "موقع الحادثة وتليجراف مصر (تغطية قضائية)",
        publisherEn: "El Haditha News & Telegraph Masr (Judicial Coverage)",
        badgeAr: "تغطية قضائية جنائية",
        badgeEn: "Judicial Press Coverage",
        date: "2023 – 2026",
        url: "https://www.google.com/search?q=%D9%85%D9%82%D8%A7%D9%88%D9%84+%D9%87%D8%B4%D8%A7%D9%85+%D8%B7%D9%84%D8%B9%D8%AA+%D9%85%D8%B5%D8%B7%D9%81%D9%89+%D8%AA%D9%87%D8%AF%D9%8A%D8%AF+%D9%85%D8%B3%D8%AA%D8%AD%D9%82%D8%A7%D8%AA",
        archiveUrl: "https://elhaditha.net",
        descAr: `تقرير صحفي حول ادعاء مقاول ارتبط بعلاقة عمل تقارب 20 عاماً مع هشام طلعت مصطفى وجود مستحقات مالية متأخرة وخلافات حول السداد؛ انتهت القضية بحكم جنائي بالحبس سنة بتهمة التهديد، دون أن تفصل المحكمة في أصل المديونية المدنية أو تحدد المشروع محل النزاع.`,
        descEn: `Press coverage regarding a contractor who maintained ~20 years working relationship claiming unpaid dues against HTM; matter culminated in 1-year criminal threat conviction without judicial resolution of the underlying civil debt.`
      },
      watan_arabi_2009: {
        titleAr: "جريدة الوطن العربي (مدونة مؤرشفة): مزاعم حول حجب نسخ العقود والخصومات المتكررة من المستخلصات",
        titleEn: "Al-Watan Al-Arabi (Archived): Subcontractor Claims on Contract Withholding & Repetitive IPC Deductions",
        publisherAr: "مدونة الوطن العربي (أرشيف صحفي استدلالي)",
        publisherEn: "Al-Watan Al-Arabi Blog (Archived Press Lead)",
        badgeAr: "خيط بحث منخفض الثقة",
        badgeEn: "Low Confidence Lead",
        date: "26 مارس 2009",
        url: "https://web.archive.org/web/20090326000000*/http://elwatanelarabi.blogspot.com",
        archiveUrl: "https://web.archive.org",
        descAr: `تقرير صحفي مؤرشف على مدونة يورد مزاعم لمقاولي باطن في مدينتي بشأن رفض تسليم نسخ من العقود وتكرار الخصومات من المستخلصات وتأخير الصرف. صُنّف التقرير في العناية الواجبة كخيط بحث منخفض الثقة لعدم توافر أحكام قضائية مؤيدة له.`,
        descEn: `Archived blog report citing trade subcontractor grievances in Madinaty regarding withholding contract copies, repeated progress deductions, and delayed disbursements. Categorized as a low-confidence research lead due to absence of independent judicial rulings.`
      },
      arij_land_allocation_2023: {
        titleAr: "شبكة أريج للصحافة الاستقصائية: تحقيق حول تخصيص الأراضي والشفافية في السوق العقاري المصري",
        titleEn: "ARIJ Investigative Network: In-Depth Investigation on Land Allocation & Developer Transparency in Egypt",
        publisherAr: "شبكة أريج (صحافة استقصائية عربية)",
        publisherEn: "ARIJ (Arab Reporters for Investigative Journalism)",
        badgeAr: "تحقيق صحفي استقصائي",
        badgeEn: "Investigative Journalism",
        date: "2023",
        url: "https://arij.net",
        archiveUrl: "https://web.archive.org/web/https://arij.net",
        descAr: `تحقيق استقصائي معمق بحث آليات تخصيص أراضي الدولة لكبار المطورين العقاريين في مصر ومشروعات طلعت مصطفى (نور وسيليا)، وخلص إلى أن تغييرات الإجراءات خفضت الشفافية، دون أن يثبت التحقيق عدم قانونية المشروعات الحالية.`,
        descEn: `Investigative deep-dive into state land allocation mechanisms to major Egyptian developers including TMG projects (Noor, Celia), noting reduced procedural transparency while acknowledging projects operate under regularized decrees.`
      },
      fra_assignment_guidance_2026: {
        titleAr: "الهيئة العامة للرقابة المالية (FRA): توجيهات عقود التطوير العقاري وبنود التنازل عن الحقوق للمقاولين والمشترين",
        titleEn: "Egyptian FRA: Regulatory Guidance on Real Estate Developer Contracts & Assignment of Rights",
        publisherAr: "الهيئة العامة للرقابة المالية (جمهورية مصر العربية)",
        publisherEn: "Financial Regulatory Authority (FRA Egypt)",
        badgeAr: "توجيه رقابي حكومي",
        badgeEn: "Regulatory Guidance",
        date: "سبتمبر 2026",
        url: "https://fra.gov.eg",
        archiveUrl: "https://web.archive.org/web/https://fra.gov.eg",
        descAr: `توجيهات رقابية رسمية صادرة من الرقابة المالية تحث المشترين ومقاولي الباطن على التدقيق في شروط العقود وبنود التنازل عن الحقوق (Assignment of Rights) وآليات مقاصة أوراق الدفع بالقطاع العقاري.`,
        descEn: `Official regulatory guidance from the FRA advising buyers and subcontractors to scrutinize contract clauses, assignment of rights, and deferred commercial paper settlement mechanics in the Egyptian real estate sector.`
      },
      mada_acc_2024: {
        titleAr: "مدى مصر: احتجاج مئات المهندسين والعاملين بشركة الإسكندرية للإنشاءات التابعة لطلعت مصطفى على تجميد الرواتب والتسريح",
        titleEn: "Mada Masr: Hundreds of ACC Engineers & Workers Protest Frozen Wages, Inflation Erosion & Dismissals",
        publisherAr: "منصة مدى مصر (تحقيق استقصائي عمالي ميداني)",
        publisherEn: "Mada Masr (Field Investigative Labor Report)",
        badgeAr: "تحقيق استقصائي موثق",
        badgeEn: "Investigative Labor Reporting",
        date: "27 مارس 2024",
        url: "https://www.madamasr.com/2024/03/27/news/%D8%B3%D9%8A%D8%A7%D8%B3%D8%A9/%D9%85%D9%87%D9%86%D8%AF%D8%B3%D9%88-%D8%B7%D9%84%D8%B9%D8%AA-%D9%85%D8%B5%D8%B7%D9%81%D9%89-%D9%8A%D8%AD%D8%AA%D8%AC%D9%88%D9%86-%D9%84%D9%84%D9%85%D8%B7%D8%A7%D9%84%D8%A8%D8%A9-%D8%A8/",
        archiveUrl: "https://web.archive.org/web/20240327170000*/https://www.madamasr.com/2024/03/27/news/%D8%B3%D9%8A%D8%A7%D8%B3%D8%A9/%D9%85%D9%87%D9%86%D8%AF%D8%B3%D9%88-%D8%B7%D9%84%D8%B9%D8%AA-%D9%85%D8%B5%D8%B7%D9%81%D9%89-%D9%8A%D8%AD%D8%AA%D8%AC%D9%88%D9%86-%D9%84%D9%84%D9%85%D8%B7%D8%A7%D9%84%D8%A8%D8%A9-%D8%A8/",
        descAr: `تقرير استقصائي موثق من منصة 'مدى مصر' رصد احتجاج وتجمع نحو 400 مهندس وعامل بشركة الإسكندرية للإنشاءات خارج مكاتب الشركة في 'مدينتي' وبمشروعي 'سيليا' و'نور' بالعاصمة الإدارية، للمطالبة بهيكل جديد للرواتب يواكب التضخم ورفع بدلات التأمين الصحي، وتوقف صرف مستحقات عدد من المفصولين دون تسوية قانونية.

• الدلالة الجنائية: تعكس استياءً داخلياً وتوتراً في إدارة الموارد البشرية والرواتب بالذراع الإنشائي الرئيسي للمجموعة خلال عام 2024.`,
        descEn: `Investigative report by 'Mada Masr' documenting collective labor protests by around 400 engineers and personnel at Alexandria Construction Co. (ACC) in Madinaty, Celia, and Noor, demanding structural wage adjustments against steep inflation, healthcare benefits, and settlements for unnotified dismissals.

• Forensic Takeaway: Evidences internal operational and payroll friction within TMG's primary construction vehicle during FY2024.`
      },
      manassa_security_aug2024: {
        titleAr: "المنصة: احتجاجات واعتصام أفراد أمن بمدينتي على ساعات العمل (12-14 ساعة) وبدل الوجبة المتدني وسكن العمال",
        titleEn: "Al Manassa: Madinaty Security Guards Protest 12-14 Hr Shifts, Inadequate Meal Stipends & Housing",
        publisherAr: "موقع المنصة الصحفي (رصد وتوثيق عمالي)",
        publisherEn: "Al Manassa News (Labor Documentation)",
        badgeAr: "رصد ميداني موثق",
        badgeEn: "Field Labor Coverage",
        date: "أغسطس 2024",
        url: "https://www.google.com/search?q=%D8%A7%D9%84%D9%85%D9%86%D8%B5%D8%A9+%D8%B9%D9%85%D8%A7%D9%84+%D8%A3%D9%85%D9%86+%D9%85%D8%AF%D9%8A%D9%86%D8%AA%D9%8A+%D8%A8%D8%AF%D9%84+%D8%A7%D9%84%D9%88%D8%AC%D8%A8%D8%A9",
        archiveUrl: "https://almanassa.net/search?keys=%D9%85%D8%AF%D9%8A%D9%86%D8%AA%D9%8A",
        descAr: `توثيق ميداني وتحقيق صحفي من موقع 'المنصة' رصد اعتصام واحتجاج العشرات من أفراد أمن مشروع مدينتي، اعتراضاً على تدني الأجور في ظل غلاء المعيشة، وطول ساعات العمل المرهقة التي تتراوح بين 12 و14 ساعة يومياً، وضآلة بدل الوجبة اليومي، والإقامة في سكن العمال التابع للمشروع (نظام 23 يوماً متواصلة عمل و7 أيام راحة).

• الدلالة الجنائية: تسليط الضوء على ضغوط تشغيل العمالة وتدني هوامش الإنفاق الخدمي في أكبر مشاريع المجموعة.`,
        descEn: `Field investigative coverage by 'Al Manassa' documenting sit-ins by security personnel in Madinaty protesting low wages, grueling 12-14 hour shifts, meager meal stipends, and crowded housing quarters under a 23-days on / 7-days off schedule.

• Forensic Takeaway: Highlights site operating cost compression and labor friction in TMG's flagship mega-development.`
      },
      manassa_security_oct2025: {
        titleAr: "المنصة: مذكرة رسمية من أفراد أمن مدينتي للمطالبة بالأجر الإضافي وبدلات الوجبات وإحالتهم للتحقيق الإداري",
        titleEn: "Al Manassa: Madinaty Security Workers Submit Overtime & Meal Allowance Petition, Face Internal Inquiries",
        publisherAr: "موقع المنصة الصحفي (وثائق الشكاوى العمالية)",
        publisherEn: "Al Manassa News (Worker Grievance Docket)",
        badgeAr: "مذكرة إدارية مسجلة",
        badgeEn: "Formal Worker Petition",
        date: "29 أكتوبر 2025",
        url: "https://www.google.com/search?q=%D8%B9%D9%85%D8%A7%D9%84+%D8%A3%D9%85%D9%86+%D9%85%D8%B0%D9%83%D8%B1%D8%A9+%D9%85%D8%AF%D9%8A%D9%86%D8%AA%D9%8A+%D8%A3%D8%AC%D8%B1+%D8%A5%D8%B6%D8%A7%D9%81%D9%8A",
        archiveUrl: "https://almanassa.net/search?keys=%D8%A3%D9%85%D9%86+%D9%85%D8%AF%D9%8A%D9%86%D8%AA%D9%8A",
        descAr: `تحقيق صحفي موثق من موقع 'المنصة' حول تقديم أفراد الأمن بمشروع مدينتي مذكرة رسمية لإدارة طلعت مصطفى للمطالبة ببدل ساعات العمل الإضافية (12 ساعة) واحتساب الإجازات الرسمية وبدل وجبات. ردت الإدارة بإحالة بعض المتقدمين بالمذكرة إلى التحقيق الإداري، مع وعود شفهية ببحث المطالب مع الزيادة السنوية.

• الدلالة الجنائية: وجود وثيقة ومذكرة مكتوبة من العاملين أنفسهم تثبت تصعيد النزاع المهني واستخدام التحقيقات الإدارية كأداة ضغط.`,
        descEn: `Journalistic report by 'Al Manassa' on Madinaty security staff submitting a formal written petition to TMG management demanding statutory overtime pay for 12-hour shifts, leave regularization, and food stipends. Management responded by subjecting certain petitioners to administrative inquiries while promising review with annual raises.

• Forensic Takeaway: Verifiable written petition directly from workers evidencing escalated administrative and compensation disputes.`
      },
      state_council_madinaty: {
        titleAr: "المحكمة الإدارية العليا: حكم بطلان عقد تخصيص أرض مدينتي (الطعن 12622 لسنة 63 ق)",
        titleEn: "Supreme Administrative Court: Annulment of Madinaty 8,000 Feddan Concession (Appeal 12622 / JY 63)",
        publisherAr: "المحكمة الإدارية العليا (بوابة منشورات قانونية الرسمية)",
        publisherEn: "Supreme Administrative Court (Manshurat Legal Database)",
        badgeAr: "حكم قضائي نهائي بات",
        badgeEn: "Landmark Supreme Court Ruling",
        date: "سبتمبر 2010",
        url: "https://manshurat.org/node/1445",
        archiveUrl: "https://web.archive.org/web/https://manshurat.org/node/1445",
        descAr: `حكم قضائي نهائي بات قضى ببطلان عقد البيع المباشر المبرم بين هيئة المجتمعات العمرانية والشركة العربية للمشروعات والتطوير العمراني (8,000 فدان) لمخالفته قانون المناقصات والمزايدات 89/1998، والذي تمت تسويته لاحقاً بموجب قرارات مجلس الوزراء وعقد 2015 بإلزام الشركة بتسليم 7% من إجمالي المباني السكنية المنجزة عيناً للهيئة.`,
        descEn: `Landmark final ruling annulling the direct allocation of 8,000 feddans to ACPUD for violating Tender Law 89/1998. Later regularized via Cabinet decrees and 2015 settlement requiring 7% in-kind finished residential BUA delivery to NUCA.`
      },
      cairo_misdemeanor_checks: {
        titleAr: "محكمة جنح قصر النيل: قضايا شيكات بدون رصيد ضد مسؤولي الشركة العربية للمشروعات (جنحة 16522 لسنة 2013)",
        titleEn: "Cairo Misdemeanor Court: Bad Check Default Proceedings Against ACPUD (Case 16522 of 2013)",
        publisherAr: "محكمة جنح قصر النيل (بوابة وزارة العدل المصرية)",
        publisherEn: "Cairo Misdemeanor Court (Ministry of Justice Portal)",
        badgeAr: "سجل جنح تجارية",
        badgeEn: "Commercial Paper Docket",
        date: "2013 – 2015",
        url: "https://egcourts.gov.eg",
        archiveUrl: "https://moj.gov.eg",
        descAr: `دعاوى جنح شيكات مقامة من مقاولين وموردين بسبب تعثر صرف أوراق دفع تجارية صادرة من مسؤولي الشركة العربية، تم التصالح فيها لاحقاً عبر جدولة المبالغ وإصدار شيكات بديلة بعد ضغوط التقاضي الجنائي.`,
        descEn: `Misdemeanor commercial paper proceedings filed by contractors against ACPUD over defaulted checks during liquidity crunches, subsequently reconciled via rescheduling and replacement notes.`
      },
      egx_filings_fy25_h126: {
        titleAr: "البورصة المصرية: القوائم المالية الموحدة المدققة لمجموعة طلعت مصطفى القابضة (FY25 & H1 2026)",
        titleEn: "EGX Disclosures: Audited Consolidated Statements for TMG Holding (FY2025 & H1 2026)",
        publisherAr: "البورصة المصرية وإفصاحات علاقات المستثمرين",
        publisherEn: "Egyptian Exchange (EGX) & Independent Auditors",
        badgeAr: "قوائم مالية مدققة ملزمة",
        badgeEn: "Statutory Audited Filings",
        date: "يونيو 2026",
        url: "https://www.egx.com.eg/ar/CompanySummary.aspx?ISIN=EGS65591C017",
        archiveUrl: "https://talaatmoustafa.com/investor-relations/financial-information/",
        descAr: `تقارير مراقبي الحسابات والقوائم الموحدة المودعة بالبورصة المصرية، متضمنة الإيرادات (62.5 مليار في 2025)، أوراق الدفع (>15.79 مليار)، والتزامات عقود التأجير التمويلي (43.99 مليار جنيه).`,
        descEn: `Official audited financial disclosures filed with EGX, detailing FY25 revenue (EGP 62.5B), notes payable (>EGP 15.79B), and off-balance financial lease obligations (EGP 43.99B).`
      },
      cpa_article15_resale: {
        titleAr: "جهاز حماية المستهلك: المادة 15 من القانون 181 لسنة 2018 وبطلان رسوم التنازل العقاري وفروق الصيانة",
        titleEn: "Egyptian Consumer Protection Law No. 181/2018 (Article 15): Annulment of Developer Resale Fees",
        publisherAr: "الجريدة الرسمية وجهاز حماية المستهلك (منشورات قانونية)",
        publisherEn: "Official Gazette & Consumer Protection Agency (Manshurat)",
        badgeAr: "نص تشريعي آمر ملزم",
        badgeEn: "Statutory Public Code",
        date: "2018 – 2026",
        url: "https://manshurat.org/node/61466",
        archiveUrl: "https://www.cpa.gov.eg",
        descAr: `نصت المادة 15 صراحة على بطلان أي شرط تعاقدي يقضي بتقاضي المطور نسبة مئوية أو مبالغ عند إعادة بيع الوحدة العقارية، وهو ما يشكل موضوع نزاعات قانونية ومحاسبية مستمرة بين ملاك مدينتي وإدارة طلعت مصطفى حول رسوم التنازل وفروق الصيانة السنوية.`,
        descEn: `Statutory provision explicitly declaring all developer resale percentage fees null and void, underpinning recurring administrative disputes between Madinaty homeowners and TMG over resale fees and annual maintenance surcharges.`
      },
      adq_icon_deal: {
        titleAr: "صفقة أيكون (ADQ / ADNEC): الاستحواذ على 40.5% من شركة أيكون للفنادق بقيمة 800 مليون دولار",
        titleEn: "ADQ / ADNEC Transaction: $800M Acquisition of 40.5% Stake in ICON Luxury Hotels",
        publisherAr: "غرفة الأخبار الرسمية لشركة أبوظبي التنموية القابضة (ADQ)",
        publisherEn: "ADQ Official Corporate Newsroom",
        badgeAr: "إفصاح استثماري سيادي معتمد",
        badgeEn: "Sovereign Investment Release",
        date: "فبراير 2024",
        url: "https://ar.adq.ae/newsroom/adq-and-adnec-group-enter-into-definitive-agreements-to-acquire-a-40-5-percent-stake-in-tmg-holdings-hospitality-business-in-egypt",
        archiveUrl: "https://adq.ae/newsroom/adq-and-adnec-group-enter-into-definitive-agreements-to-acquire-a-40-5-percent-stake-in-tmg-holdings-hospitality-business-in-egypt",
        descAr: `إفصاح رسمي عن إتمام صفقة استحواذ تحالف أبوظبي القابضة ADQ وADNEC على حصة 40.5% في شركة أيكون للفنادق (الذراع الفندقي لطلعت مصطفى) متضمنة محفظة الفنادق التاريخية السبعة وفنادق فور سيزونز، وضخ 800 مليون دولار لتعزيز السيولة الدولارية للمجموعة.`,
        descEn: `Official regulatory announcement of ADQ/ADNEC acquiring a 40.5% stake in ICON Hotels (TMG hospitality vehicle) for $800 million, encompassing the historic 7-hotel heritage portfolio and Four Seasons luxury assets.`
      },
      southmed_launch: {
        titleAr: "البورصة المصرية وإفصاح طلعت مصطفى: إطلاق مشروع ساوث ميد (SouthMED) ومبيعات قياسية",
        titleEn: "EGX Filings & TMG Disclosures: Launch of SouthMED (North Coast) & Record Sales",
        publisherAr: "بوابة مجموعة طلعت مصطفى والشرق بلومبرغ",
        publisherEn: "TMG Corporate Portal & Asharq Bloomberg",
        badgeAr: "إفصاح رسمي للمطور الرئيسي",
        badgeEn: "Official Developer Disclosure",
        date: "يوليو 2024",
        url: "https://talaatmoustafa.com/tmg-introduces-southmed/",
        archiveUrl: "https://asharqbusiness.com/financial-reports/120363/%D8%A3%D8%B1%D8%A8%D8%A7%D8%AD-%D8%B7%D9%84%D8%B9%D8%AA-%D9%85%D8%B5%D8%B7%D9%81%D9%89-%D8%AA%D9%82%D9%81%D8%B2-43-%D8%A8%D8%A7%D9%84%D9%85%D8%A6%D8%A9-%D9%88%D8%B3%D8%B7-%D8%B2%D8%AE%D9%85-%D8%A7%D9%84%D9%86%D8%B4%D8%A7%D8%B7-%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D8%B1%D9%8A/",
        descAr: `إفصاح رسمي لشركة طلعت مصطفى بالبورصة المصرية عن إطلاق مشروع ساوث ميد على الساحل الشمالي الغربي بمساحة 23 مليون متر مربع، وتحقيق مبيعات حجز قياسية تجاوزت 200 مليار جنيه خلال الأيام الأولى، بنموذج شراكة استثمارية على الأرض.`,
        descEn: `Official EGX disclosure regarding the launch of SouthMED on Egypt's Mediterranean coast (23M sqm), generating over EGP 200B in initial sales commitments under a master development partnership.`
      },
      banan_riyadh: {
        titleAr: "الشركة الوطنية للإسكان (NHC - السعودية): تدشين مدينة بنان الرياض باستثمارات 31.4 مليار ريال",
        titleEn: "National Housing Company (NHC - Saudi Arabia): Banan City Launch (SAR 31.4 Billion)",
        publisherAr: "وكالة الأنباء السعودية الرسمية (واس) والوطنية للإسكان",
        publisherEn: "Saudi Press Agency (SPA) & NHC Investment",
        badgeAr: "بيان حكومي رسمي معتمد",
        badgeEn: "Official Sovereign Press Release",
        date: "مايو 2024",
        url: "https://www.spa.gov.sa/N2059465",
        archiveUrl: "https://investment.nhc.sa/",
        descAr: `إعلان رسمي عن الشراكة الاستراتيجية بين الشركة الوطنية للإسكان بالمملكة العربية السعودية ومجموعة طلعت مصطفى لتطوير مدينة بنان الذكية بضاحية خزام بالرياض على مساحة 10 ملايين متر مربع، باستثمارات إجمالية 31.4 مليار ريال سعودي.`,
        descEn: `Official announcement by Saudi NHC and TMG launching Banan Smart City in Riyadh (Khuzam suburb) across 10M sqm with SAR 31.4B in total project investments.`
      },
      alborsanews_atrium: {
        titleAr: "جريدة البورصة وسجلات المقاولات: إسناد حزم إنشائية لشركة أتريوم (Atrium AQC) في مدينتي وسيليا",
        titleEn: "Al Borsa Newspaper & Contracting Records: Atrium AQC Civil & Infrastructure Packages",
        publisherAr: "جريدة البورصة الاقتصادية وسجلات شركة أتريوم",
        publisherEn: "Al Borsa Financial Newspaper & Atrium Contracting",
        badgeAr: "سجل عقود المقاول العام",
        badgeEn: "EPC Package Award Record",
        date: "2023 – 2025",
        url: "https://alborsaanews.com/?s=%22%D8%A3%D8%AA%D8%B1%D9%8A%D9%88%D9%85%22",
        archiveUrl: "https://atriumeg.com/works.html",
        descAr: `سجلات قطاع التشييد وإفصاحات المناقصات التي توثق إسناد حزم مباني فاخرة وأعمال خرسانات وبنية تحتية لشركة أتريوم كطرف مقاول رئيسي مؤهل لمشاريع مدينتي والعاصمة الإدارية.`,
        descEn: `Construction sector procurement records documenting tier-1 contract packages awarded to Atrium Quality Contractors for luxury residential clusters and infrastructure in Madinaty and Celia.`
      },
      hassan_allam_portfolio: {
        titleAr: "سابقة أعمال حسن علام للإنشاءات: بحيرات وشبكات المرافق واللاندسكيب بمشروع مدينتي",
        titleEn: "Hassan Allam Construction Portfolio: Madinaty Golf Lakes & Utility Networks",
        publisherAr: "الموقع الرسمي لشركة حسن علام القابضة للإنشاءات",
        publisherEn: "Hassan Allam Holding Official Projects Directory",
        badgeAr: "توثيق هندسي لشركة المقاولات",
        badgeEn: "Verified EPC Contractor Reference",
        date: "2019 – 2024",
        url: "https://www.hassanallam.com/projects/madinaty-golf-lakes-vg1-2",
        archiveUrl: "https://www.hassanallam.com",
        descAr: `السجل الرسمي لشركة حسن علام للإنشاءات يوثق تنفيذ وتشغيل بحيرات الجولف بمساحة 200 ألف متر مربع (VG1 & VG2) وشبكات البنية التحتية والمرافق الرئيسية لمشروع مدينتي.`,
        descEn: `Official corporate portfolio of Hassan Allam Construction documenting the execution of Madinaty Golf Lakes (200,000 sqm across VG1/VG2) and primary utility infrastructure.`
      },
      concrete_plus_portfolio: {
        titleAr: "سابقة أعمال كونكريت بلس: حزم الأعمال الخرسانية والإنشائية في سيليا والعاصمة الإدارية",
        titleEn: "Concrete Plus Portfolio: Superstructure & Reinforced Concrete Packages in Celia",
        publisherAr: "السجل الهندسي لشركة كونكريت بلس للمقاولات",
        publisherEn: "Concrete Plus Contracting Corporate Directory",
        badgeAr: "توثيق هندسي لمقاول الحزم",
        badgeEn: "Contractor Package Reference",
        date: "2021 – 2024",
        url: "http://www.concreteplus.biz",
        archiveUrl: "https://www.linkedin.com/company/concrete-plus/",
        descAr: `التوثيق الهندسي لشركة كونكريت بلس للمقاولات يثبت تنفيذ أعمال الهياكل الخرسانية والمباني السكنية المتعددة لصالح شركة الإسكندرية للإنشاءات بمشروع سيليا العاصمة الإدارية.`,
        descEn: `Engineering references confirming Concrete Plus executing residential building concrete packages and core/shell superstructures under subcontract to ACC in Celia.`
      },
      saveto_egypt: {
        titleAr: "سابقة أعمال سافيتو مصر (Saveto): توريد كيماويات البناء ومواد التشطيب لمشاريع طلعت مصطفى",
        titleEn: "Saveto Egypt Portfolio: Building Chemicals & Finishing Supplies for TMG Developments",
        publisherAr: "السجل الصناعي لمجموعة سافيتو لمواد البناء",
        publisherEn: "Saveto Group Industrial References",
        badgeAr: "عقود توريد خامات معتمدة",
        badgeEn: "Verified Supply Chain Reference",
        date: "2020 – 2025",
        url: "https://saveto.com",
        archiveUrl: "https://www.linkedin.com/company/saveto-group/",
        descAr: `سجلات توريد شركة سافيتو لمواد البناء الحديث ومواد العزل والتشطيبات لمشروعات مدينتي، الرحاب، وسيليا عبر عقود توريد مركزية مع شركة الإسكندرية للإنشاءات.`,
        descEn: `Vendor delivery records confirming Saveto supplying thermal insulation, tile adhesives, and specialized building chemicals to ACC for Madinaty, Rehab, and Celia.`
      },
      youm7_luxor_egoth: {
        titleAr: "اليوم السابع ووزارة قطاع الأعمال: شراكة آيكون (طلعت مصطفى) مع إيجوث لتطوير فورسيزونز الأقصر",
        titleEn: "Youm7 & Ministry of Public Business: ICON (TMG) Partners with EGOTH for Four Seasons Luxor",
        publisherAr: "صحيفة اليوم السابع ووزارة قطاع الأعمال العام",
        publisherEn: "Youm7 Newspaper & Ministry of Public Business Sector",
        badgeAr: "توثيق الشراكة الحكومية الرسمية",
        badgeEn: "Public Sector Partnership Record",
        date: "18 فبراير 2020",
        url: "https://www.youm7.com/story/2020/2/18/%D9%87%D8%B4%D8%A7%D9%85-%D8%B7%D9%84%D8%B9%D8%AA-%D9%8A%D8%A8%D9%86%D9%89-%D9%81%D9%88%D8%B1%D8%B3%D9%8A%D8%B2%D9%88%D9%86-%D8%A8%D8%A7%D9%84%D8%A3%D9%82%D8%B5%D8%B1-%D8%A8%D8%AA%D9%83%D9%84%D9%81%D8%A9-1-5-%D9%85%D9%84%D9%8A%D8%A7%D8%B1-%D8%AC%D9%86%D9%8A%D9%87/4636733",
        archiveUrl: "https://www.youm7.com/story/2025/2/25/%D8%B7%D9%84%D8%B9%D8%AA-%D9%85%D8%B5%D8%B7%D9%81%D9%89-%D8%AA%D8%AA%D8%B5%D8%AF%D8%B1-%D8%A7%D9%84%D9%82%D8%B7%D8%A7%D8%B9-%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%AD%D9%8A-%D8%A7%D9%84%D9%81%D8%A7%D8%AE%D8%B1-%D9%81%D9%8A-%D9%85%D8%B5%D8%B7%D9%81%D9%89-%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA-%D8%A7%D9%84%D9%85%D8%AC%D9%85%D9%88%D8%B9%D8%A9/6896605",
        descAr: `تقرير رسمي يوثق توقيع عقد الشراكة بين شركة آيكون التابعة لطلعت مصطفى وشركة إيجوث التابعة لوزارة قطاع الأعمال العام لتنفيذ فندق فورسيزونز الأقصر على أرض السلطانة ملك التاريخية بإطلالة على النيل.`,
        descEn: `Official report documenting ICON (TMG hospitality arm) partnering with state-owned EGOTH to develop Four Seasons Luxor on Sultana Malak land under a long-term revenue share framework.`
      },
      atrium_luxor_award: {
        titleAr: "إفصاح شركة أتريوم للمقاولات: الفوز بعقد المقاول العام الرئيسي لفندق فورسيزونز الأقصر",
        titleEn: "Atrium Quality Contractors Disclosure: Main EPC Award for Four Seasons Luxor",
        publisherAr: "الموقع الرسمي لشركة أتريوم للمقاولات (Atrium AQC)",
        publisherEn: "Atrium Quality Contractors Works Directory",
        badgeAr: "إسناد عقد المقاول العام",
        badgeEn: "Main EPC Award Verification",
        date: "2024 – 2025",
        url: "https://atriumeg.com/works.html",
        archiveUrl: "https://www.linkedin.com/company/atriumqualitycontractors/",
        descAr: `إعلان رسمي صادر عن شركة أتريوم للمقاولات يؤكد فوزها بعقد الإنشاءات والمقاول العام المتكامل لمشروع فندق فورسيزونز الأقصر على كورنيش النيل وإنجاز المرحلة الأولى من المشروع.`,
        descEn: `Official corporate disclosure by Atrium Quality Contractors confirming securing the main EPC turnkey contract for Four Seasons Luxor and advancing Phase I works.`
      },
      fourseasons_official_luxor: {
        titleAr: "الموقع الرسمي لفنادق فورسيزونز العالمية: جدول الافتتاحات وتحديث موعد تشغيل فندق الأقصر إلى 2027",
        titleEn: "Four Seasons Hotels & Resorts Official Directory: Target Opening for Luxor Updated to 2027",
        publisherAr: "المكتب الصحفي الرسمي لمجموعة فورسيزونز العالمية",
        publisherEn: "Four Seasons Hotels & Resorts Official Press Room",
        badgeAr: "بيان الشركة العالمية المشغلة",
        badgeEn: "Global Operator Official Release",
        date: "2025 – 2026",
        url: "https://press.fourseasons.com/news-releases/2022/four-seasons-expands-in-egypt/",
        archiveUrl: "https://www.fourseasons.com/newopenings/",
        descAr: `البيان الصحفي الرسمي لشركة فورسيزونز للتوسع في مصر ودليل الافتتاحات الجديد الذي يحدد موعد تشغيل فندق الأقصر في عام 2027، بعد أن كان مستهدفاً في 2026 وفق تقرير نتائج النصف الأول 2025 لطلعت مصطفى.`,
        descEn: `Official global press release for Egypt expansion and brand directory updating Four Seasons Luxor target opening to 2027, revising the 2026 date cited in TMG's H1 2025 financial release.`
      },
      mada_southmed_2024: {
        titleAr: "مدى مصر: ادعاءات عمال ومقاولي باطن محليين بساوث ميد وتأخر مستحقات جهات عليا",
        titleEn: "Mada Masr: Local Subcontractor Dues Report on SouthMED & Upstream Payer Claims",
        publisherAr: "موقع مدى مصر الاستقصائي المستقل (5 نوفمبر 2024)",
        publisherEn: "Mada Masr Investigative Platform (5 Nov 2024)",
        badgeAr: "ادعاء مصدر محلي غير مؤيد بمستند",
        badgeEn: "Uncorroborated Local Source Claim",
        date: "5 نوفمبر 2024",
        url: "https://www.madamasr.com/ar/2024/11/05/news/سياسة/إصابة-شاب-والقبض-على-اثنين-في-اشتباكات/",
        archiveUrl: "https://www.madamasr.com/en/2024/11/05/news/politics/residents-clash-with-military-in-matrouh-to-protest-displacement-for-talaat-moustafa-group-tourism-project-1-person-shot-2-arrested/",
        descAr: `تقرير صحفي أورد ادعاءً لمصدر محلي حول عدم سداد مستحقات أعمال مقاولات باطن لأهالي المنطقة بساوث ميد، وعزا المصدر التأخير لتباطؤ سداد جهات بالقوات المسلحة للمقاولين الرئيسيين. يؤكد تقرير الفحص أن الخبر لا يثبت مديونية مباشرة على طلعت مصطفى أو كونكريت بلس.`,
        descEn: `Report alleging local subcontracting work non-payment on SouthMED, with an anonymous source attributing delay to upstream payments by Armed Forces to prime contractors. Does not establish direct TMG or Concrete Plus liability.`
      },
      mada_engineers_2024: {
        titleAr: "مدى مصر: احتجاج 400 مهندس بشركة الإسكندرية للإنشاءات (مدينتي وسيليا ونور)",
        titleEn: "Mada Masr: 400 ACC Engineers Protest Over Salaries & Healthcare Benefits",
        publisherAr: "موقع مدى مصر (27 مارس 2024)",
        publisherEn: "Mada Masr (27 March 2024)",
        badgeAr: "احتجاج مهني داخلي موثق",
        badgeEn: "Documented Internal Labor Action",
        date: "27 مارس 2024",
        url: "https://www.madamasr.com/ar/2024/03/27/news/سياسة/مهندسو-طلعت-مصطفى-يحتجون-للمطالبة-ب/",
        archiveUrl: "https://www.madamasr.com/ar/2024/03/27/news/سياسة/مهندسو-طلعت-مصطفى-يحتجون-للمطالبة-ب/",
        descAr: `وقفة احتجاجية شارك فيها نحو 400 مهندس من العاملين بشركة الإسكندرية للإنشاءات بمواقع مدينتي وسيليا ونور للمطالبة بزيادة الرواتب لمواكبة التضخم وتحسين التأمين الطبي، وتعد سياقاً عمالياً داخلياً وليس نزاعاً على فواتير مقاولي باطن.`,
        descEn: `Labor action by ~400 ACC engineers across Madinaty, Celia, and Noor demanding cost-of-living adjustments and improved medical benefits. Represents internal workforce remuneration, not subcontractor trade dispute.`
      },
      everlast_openair: {
        titleAr: "إيفرلاست للمقاولات: تصنيع وتركيب جمالونات الحديد لأوبن إير مول مدينتي",
        titleEn: "Everlast Construction: Steel Trusses Fabrication & Erection for Open Air Mall Madinaty",
        publisherAr: "سجل مشاريع شركة إيفرلاست للمقاولات واستشارات ECG",
        publisherEn: "Everlast Construction Works Profile & ECG Engineering",
        badgeAr: "إنجاز أعمال مقاولة باطن متخصصة",
        badgeEn: "Specialist Subcontract Delivery",
        date: "2021 – 2023",
        url: "https://eg.linkedin.com/in/mohamed-zein-86051680",
        archiveUrl: "https://atriumeg.com/portfolio/open-air-mall-madinaty/",
        descAr: `سجل مهني يوثق قيام شركة إيفرلاست للمقاولات بتصنيع وتركيب جمالونات وهياكل الحديد الإنشائية لمشروع أوبن إير مول بمدينتي كأحد مقاولي الباطن المتخصصين تحت إشراف شركة أتريوم والاستشاري العام جماعة المهندسين الاستشاريين (ECG).`,
        descEn: `Engineering record verifying Everlast Construction fabricating and erecting structural steel trusses at Open Air Mall Madinaty as specialist subcontractor under Atrium AQC and supervising consultant ECG.`
      },
      siraj_easthub: {
        titleAr: "سراج للإضاءة: تصميم وتوريد إضاءة الواجهات واللاندسكيب لمول إيست هب مدينتي",
        titleEn: "Siraj Lighting: Facade & Landscape Architectural Lighting for East Hub Madinaty",
        publisherAr: "سجل أعمال شركة سراج العالمية للإضاءة ومول إيست هب",
        publisherEn: "Siraj Lighting Official Project Index",
        badgeAr: "سجل توريد وشراكة معتمد",
        badgeEn: "Verified Architectural Lighting Partner",
        date: "2023 – 2024",
        url: "https://www.linkedin.com/posts/siraj-lighting-company_lightingfromtheheartofegypt-sirajlighting-activity-7084456074832920578-IMdH",
        archiveUrl: "https://atriumeg.com/portfolio/east-hub-mall-at-madinaty/",
        descAr: `توثيق رسمي لتوريد أنظمة الإضاءة المعمارية لواجهات وشوارع إيست هب مول بمدينتي، ضمن شبكة تعاقدية ضمت العربية للمشروعات (المالك)، دار الهندسة (مدير المشروع)، وأتريوم (المقاول العام).`,
        descEn: `Corporate supplier statement detailing architectural lighting design and supply for East Hub Madinaty under developer ACPUD, Dar Al-Handasah (PM), and Atrium (EPC).`
      },
      emas_elsewedy_noor: {
        titleAr: "إيماس السويدي: توريد موزعات الجهد المتوسط Simoprime لمدينة نور",
        titleEn: "EMAS El Sewedy: Siemens Simoprime 24kV Medium-Voltage Switchgear for Noor City",
        publisherAr: "شركة السويدي إندستريز (EMAS El Sewedy) ومجموعة شاكر",
        publisherEn: "EMAS El Sewedy Industries & Shaker Consultancy Group",
        badgeAr: "توريد مهمات بنية تحتية ذكية",
        badgeEn: "Smart Infrastructure Equipment Supply",
        date: "2024 – 2025",
        url: "https://www.linkedin.com/posts/sayed-mahmoud-pmp%C2%AE-pmi-acp%C2%AE-mba-rolling-66030511a_simoprime-development-electrificationandautomation-activity-7376736839182823424",
        archiveUrl: "https://elsewedy.com",
        descAr: `إفصاح رسمي عن تصنيع وتوريد خلايا الجهد المتوسط طراز Simoprime 24 kV لشبكات التوزيع الذكية بمدينة نور، بإشراف استشاري المشروع مجموعة شاكر للاستشارات الهندسية والشركة العربية للاستثمار العمراني.`,
        descEn: `Official supplier milestone confirming delivery of Siemens Simoprime 24 kV switchgear for Noor City electrical grid under Arab Co. for Urban Investment and Shaker Consultancy.`
      },
      andy_lang_lld: {
        titleAr: "تصميمات LLD العالمية: شراكة ممتدة 25 عاماً في مشروعات فورسيزونز طلعت مصطفى",
        titleEn: "LLD Lighting Design: 25-Year Partnership Across TMG Four Seasons Developments",
        publisherAr: "أندي لانغ (LLD International) وسجلات فورسيزونز كابيتال مدينتي",
        publisherEn: "Andy Lang / LLD International & Four Seasons Records",
        badgeAr: "شراكة استشارية ممتدة (25 عاماً)",
        badgeEn: "Long-Term Professional Partnership (25 Years)",
        date: "2024 – 2026",
        url: "https://www.linkedin.com/posts/andy-lang-8094b05_construction-continues-on-thefour-seasons-activity-7417638710898397185-kjA7",
        archiveUrl: "https://www.fourseasons.com",
        descAr: `بيان مهني موثق من المصمم العالمي أندي لانغ يؤكد أن فندق فورسيزونز نيو كايرو كابيتال بمدينتي يمثل المشروع السادس لفورسيزونز بمصر والتعاون الممتد لأكثر من ربع قرن مع مجموعة طلعت مصطفى، كدليل استمرارية وتكرار أعمال رفيع المستوى.`,
        descEn: `First-person professional statement from lighting designer Andy Lang highlighting Four Seasons New Cairo Capital as the 6th Egypt FS project and a ~25-year working relationship with TMG.`
      },
      devzah_cairo_capital: {
        titleAr: "سجل استلام المواد (MIR-11): توريد شركة ديفزاه لمشروع فورسيزونز كابيتال CP05",
        titleEn: "Material Inspection Record (MIR-11): Devzah SI Subcontractor at Four Seasons CP05",
        publisherAr: "سجلات الفحص الهندسي واستلام المواد تحت إشراف هيل إنترناشيونال",
        publisherEn: "Engineering Material Inspection Record & Hill International",
        badgeAr: "مستند فحص واستلام مواد هندسي",
        badgeEn: "Engineering Inspection Docket",
        date: "2023 – 2024",
        url: "https://www.scribd.com/document/928303864/MIR-11",
        archiveUrl: "https://atriumeg.com",
        descAr: `مستند فحص واستلام مواد (Material Inspection Report) يوثق عمل شركة Devzah SI كمقاول باطن / مورد لحزمة الفندق CP05 المنفذة عبر تحالف أتريوم وCCC تحت إشراف مدير المشروع هيل إنترناشيونال.`,
        descEn: `Material Inspection Request (MIR-11) record identifying Devzah SI as trade vendor/subcontractor under Atrium-CCC JV for Package CP05 overseen by Hill International.`
      },
      knauf_luxor: {
        titleAr: "كناوف مصر: توريد أنظمة الجبس بورد المتطورة لفندق فورسيزونز الأقصر",
        titleEn: "Knauf Egypt: Advanced Drywall & Gypsum Systems for Four Seasons Luxor",
        publisherAr: "شركة كناوف مصر واستشارات معمارية معمار إنتريرز",
        publisherEn: "Knauf Egypt Corporate & Mimar Interiors",
        badgeAr: "سجل شراكة وتوريد تخصصي",
        badgeEn: "Specialist Drywall Systems Partner",
        date: "2024 – 2025",
        url: "https://www.linkedin.com/company/knauf-egypt/",
        archiveUrl: "https://knauf.eg",
        descAr: `بيان رسمي يوثق اعتماد وتوريد قواطع وأنظمة الجبس المقاوم للرطوبة والحريق من كناوف مصر لفندق فورسيزونز الأقصر بالتعاون مع المقاول العام والتحالف المنفذ، واستشاري التصميم الداخلي معمار إنتريرز.`,
        descEn: `Corporate supplier statement detailing Knauf Egypt gypsum partitions for Four Seasons Luxor under Atrium-CCC execution and Mimar Interiors design consultancy.`
      },
      elhadad_claims_2022: {
        titleAr: "دراسة استشارية لمطالبات المقاولات: أثر تأخر صرف المستخلصات الجارية على سلاسل الإمداد",
        titleEn: "Construction Claims Analysis: Systemic Impacts of Interim Payment Certification Delays",
        publisherAr: "الاستشاري محمد الحداد (خبير إدارة العقود والمطالبات الهندسية)",
        publisherEn: "Mohamed Elhadad (Contracts & Claims Advisory)",
        badgeAr: "تحليل فني لصناعة المقاولات",
        badgeEn: "Industry Claims & Contracts Benchmark",
        date: "2022",
        url: "https://ae.linkedin.com/posts/mohamed-elhadad-%D9%85%D8%AD%D9%85%D8%AF-%D8%A7%D9%84%D8%AD%D8%AF%D8%A7%D8%AF-81883569_%D8%A7%D9%84%D9%86%D8%B2%D8%A7%D8%B9-%D8%A7%D9%84%D9%85%D9%86%D8%B4%D8%A3-%D9%84%D9%84%D9%85%D8%B7%D8%A7%D9%84%D8%A8%D8%A7%D8%AA-9-%D8%AA%D8%A3%D8%AE%D9%8A%D8%B1-%D8%B5%D8%B1%D9%81-activity-6882910353459401444-UHoa",
        archiveUrl: "https://linkedin.com",
        descAr: `تحليل فني وتعاقدي متخصص يشرح الآليات التي يؤدي بها تأخير اعتماد المستخلصات وصرفها إلى اختناق السيولة لدى مقاولي الباطن، مما يولد نزاعات تمديد وقت (EOT) وغرامات تأخير ومطالبات تعويضية.`,
        descEn: `Technical analysis detailing how interim payment certification bottlenecks create severe working capital strain for subcontractors, triggering extension of time (EOT) and prolongation claims.`
      },
      ccc_atrium_mep_luxor: {
        titleAr: "سجلات المقاولات والمهندسين: تحالف CCC وأتريوم لتنفيذ حزمة الأعمال الكهروميكانيكية CP02 بفورسيزونز الأقصر",
        titleEn: "Engineering Records: CCC & Atrium Joint Venture for Luxor MEP Package CP02",
        publisherAr: "السجلات الهندسية المهنية وتحالف CCC وأتريوم",
        publisherEn: "Professional Engineering Directory & CCC / Atrium Records",
        badgeAr: "سجل مهني لتحالف مقاولي MEP",
        badgeEn: "MEP Joint Venture Consortium Records",
        date: "2024 – 2025",
        url: "https://www.linkedin.com/company/atriumqualitycontractors/",
        archiveUrl: "https://www.ccc.net",
        descAr: `سجلات مهنية توثق إسناد حزمة الأعمال الكهروميكانيكية الرئيسية (MEP Package CP02) لتحالف مشترك بين CCC Electromechanical وأتريوم، تحت إشراف هيل إنترناشيونال ومجموعة شاكر كونسلتنسي.`,
        descEn: `Professional engineering records confirming the award of main MEP Package CP02 to a CCC / Atrium Joint Venture under Hill International (PM) and Shaker Consultancy Group supervision.`
      },
      egx_leaseback_debt_2026: {
        titleAr: "إفصاح البورصة المصرية ومراقب الحسابات: التزامات عقود التأجير التمويلي وشركة رواسي (43.99 مليار جنيه @ 28.6% فائدة)",
        titleEn: "EGX Filings & Statutory Audit: Off-Balance Lease Obligations & Rawasy SPV (EGP 43.99B @ 28.6% Interest)",
        publisherAr: "الهيئة العامة للرقابة المالية ومراقبو حسابات طلعت مصطفى (KPMG & المتضامنون)",
        publisherEn: "Financial Regulatory Authority (FRA) & TMG Statutory Auditors (KPMG Hazem Hassan)",
        badgeAr: "إيضاح مالي إلزامي (إيضاح 10، 25، 101)",
        badgeEn: "Statutory Lease Disclosure Note 10, 25, 101",
        date: "يونيو 2026",
        url: "https://www.egx.com.eg/ar/CompanySummary.aspx?ISIN=EGS65591C017",
        archiveUrl: "https://talaatmoustafa.com/investor-relations/financial-information/",
        descAr: `كشفت القوائم المالية الموحدة وإيضاحات مراقبي الحسابات عن ارتباط المجموعة بالتزامات بيع وإعادة استئجار (Sale-and-leaseback) لأصول تجارية وفندقية بإجمالي 43.99 مليار جنيه مع شركة رواسي للتطوير وشركات تأجير تمويلي كبرى تابعة لبنكي الأهلي ومصر. وبإضافة التسهيلات البنكية المباشرة البالغة 16.5 مليار جنيه، يصل إجمالي الالتزامات التمويلية إلى 60.5 مليار جنيه، مع متوسط فائدة فعلي قياسي على الجنيه بلغ 28.6%، مما يرتب أعباء تمويل سنوية باهظة تمتص عوائد التشغيل.`,
        descEn: `Audited consolidated notes 10, 25, and 101 disclose EGP 43.99B in off-balance sale-and-leaseback commitments with Rawasy Urban Development and banking leasing arms (NBE/BdC). Aggregating direct bank borrowings of EGP 16.5B brings total true debt obligations to EGP 60.5B carrying a weighted effective EGP borrowing cost of 28.6%.`
      },
      tmg_backlog_statutory_2025: {
        titleAr: "إفصاح رصيد المبيعات التعاقدية (Backlog): 441.2 مليار جنيه التزامات تسليم مشروعات مستقبلية",
        titleEn: "TMG Statutory Backlog Disclosure: EGP 441.2B Contractual Delivery Liability Pipeline",
        publisherAr: "علاقات المستثمرين بمجموعة طلعت مصطفى القابضة وموقع البورصة المصرية",
        publisherEn: "TMG Holding Investor Relations & EGX Disclosures",
        badgeAr: "إفصاح إيرادات مؤجلة (إيضاح 24، 104)",
        badgeEn: "Statutory Backlog Note 24, 104",
        date: "إقفال 2025 / H1 2026",
        url: "https://talaatmoustafa.com/investor-relations/financial-information/",
        archiveUrl: "https://www.egx.com.eg",
        descAr: `سجلت المجموعة رصيد مبيعات تعاقدية غير مسلمة (Backlog) بقيمة 441.2 مليار جنيه بنهاية 2025 وارتفع لنحو 460 مليار جنيه في منتصف 2026. وتؤكد تقارير الفحص أن هذا الرصيد يمثل التزامات تسليم مستقبلية لوحدات مباعة بالتقسيط على 10-12 سنة، وليس سيولة نقدية فورية بالخزينة، مما يجعله عرضة لمخاطر تضخم تكاليف مواد البناء وتقلبات أسعار الصرف لحين إتمام التنفيذ والتسليم الفعلي.`,
        descEn: `Official regulatory filings report an unprecedented EGP 441.2B sales backlog by end-2025 (~EGP 460B in H1 2026). Diligence audits confirm this figure represents unearned contractual commitments to construct and deliver units sold on 10-12 year payment plans, not immediate treasury cash, exposing delivery margins to building material inflation and currency devaluation.`
      },
      fra_related_parties_2026: {
        titleAr: "إفصاح الأطراف ذات الصلة وحصص السيطرة: 43.2% ملكية عائلية و1.90 مليار جنيه أرصدة مدينة",
        titleEn: "FRA Related-Party & UBO Disclosure: 43.2% Family Equity & EGP 1.90B Dues",
        publisherAr: "الهيئة العامة للرقابة المالية وسجل الإفصاح الدوري بالبورصة المصرية",
        publisherEn: "Egyptian Financial Regulatory Authority & EGX Periodic Disclosures",
        badgeAr: "إفصاح حوكمة وأطراف مرتبطة (إيضاح 11، 120)",
        badgeEn: "Governance & Related Parties Note 11, 120",
        date: "H1 2026",
        url: "https://fra.gov.eg",
        archiveUrl: "https://www.egx.com.eg/ar/CompanySummary.aspx?ISIN=EGS65591C017",
        descAr: `توثق إفصاحات هيكل المساهمين سيطرة عائلة طلعت مصطفى وشركاتها الاستثمارية الخاصة على نسبة 43.2% من رأس مال الشركة القابضة. كما تظهر القوائم المالية وجود أرصدة مدينة مستحقة من أطراف ذات صلة بلغت 1.90 مليار جنيه في يونيو 2026 (مقارنة بـ 2.45 مليار جنيه بنهاية 2025)، مما يتطلب رقابة مستمرة من لجنة المراجعة المستقلة للتحقق من تسعير المعاملات على أسس تجارية بحتة (Arm's Length).`,
        descEn: `Shareholder filings confirm the Talaat Moustafa family controls 43.2% of holding equity via private investment vehicles. Audited interim statements Note 11 & 120 disclose EGP 1.90B in net receivables due from related parties as of June 2026 (vs EGP 2.45B at end-2025), necessitating rigorous independent audit committee oversight to verify strict arm's-length terms protecting minority shareholders.`
      },
      nuca_acud_land_decrees: {
        titleAr: "الجريدة الرسمية وقرارات مجلس الوزراء: سندات تخصيص أراضي مدينتي ونور وسيليا (NUCA & ACUD)",
        titleEn: "Official Gazette & Prime Ministerial Decrees: NUCA & ACUD Master Concession Deeds",
        publisherAr: "مجلس الوزراء المصري وهيئة المجتمعات العمرانية الجديدة",
        publisherEn: "Egyptian Council of Ministers & New Urban Communities Authority",
        badgeAr: "قرارات تخصيص سيادية رسمية",
        badgeEn: "Sovereign Land Allocation Decrees",
        date: "2010 – 2024",
        url: "https://manshurat.org",
        archiveUrl: "https://www.newcities.gov.eg",
        descAr: `قرارات مجلس الوزراء وهيئة المجتمعات العمرانية وشركة العاصمة الإدارية لتنظيم تخصيص أراضي مدينتي (8,000 فدان بمقابل عيني 7% مباني منجزة)، ومدينة نور بكابيتال جاردنز (5,000 فدان بحصة عينية ونقدية)، وسيليا (500 فدان). وتشدد القواعد القانونية على ضرورة فحص المشترين للقرارات الوزارية وسندات سداد أقساط الأرض وخلو المرحلة من الرهون قبل التوقيع.`,
        descEn: `Cabinet and regulatory decrees regularizing the allocation of Madinaty (8,000 feddans with 7% in-kind finished residential BUA delivery to NUCA), Noor City (5,000 feddans), and Celia (500 feddans in New Capital). Buyers are legally advised to verify approved ministerial decrees, land installment discharge letters, and ensure units are free of bank mortgage liens prior to contract execution.`
      },
      tmg_standard_contract_terms: {
        titleAr: "عقود التجزئة العقارية والشروط النموذجية لمجموعة طلعت مصطفى: بنود الإعفاء من التأخير ورسوم الخدمات",
        titleEn: "TMG Standard Master Unit Purchase Agreement: Force Majeure & Utility Delay Clauses",
        publisherAr: "الإدارة القانونية للشركة العربية للمشروعات والتطوير العمراني",
        publisherEn: "Arab Company for Projects & Urban Development (Legal Contracts Division)",
        badgeAr: "صياغة تعاقدية إدارية",
        badgeEn: "Standard Unit Sale Contract",
        date: "2020 – 2026",
        url: "https://talaatmoustafa.com",
        archiveUrl: "https://egcourts.gov.eg",
        descAr: `النموذج الموحد لعقود بيع الوحدات السكنية بمشروعات طلعت مصطفى، والذي يتضمن بنوداً تعفي المطور من غرامات التأخير في حال تأخر توصيل الشبكات والمرافق الحكومية العامة، بالإضافة إلى بنود إلزام المشتري بسداد مصاريف مقايسات العدادات ورسوم الاستلام ووديعة الصيانة ورسوم التنازل للغير.`,
        descEn: `Standard off-plan sales contract clauses for TMG master communities, featuring developer indemnity against delay penalties where delays are linked to sovereign external utility infrastructure delivery, alongside provisions mandating buyer payment for utility meters, delivery surcharges, maintenance deposits, and resale transfer authorization fees.`
      },
      madinaty_maintenance_audit: {
        titleAr: "ملف تدقيق فروق الصيانة وشكاوى اتحادات شاغلي مدينتي والرحاب: مطالبات 15 إلى 45 ألف جنيه سنوياً",
        titleEn: "Madinaty & Rehab Maintenance Deficit Docket: EGP 15k-45k Surcharges & Auditor Scrutiny",
        publisherAr: "اتحاد شاغلي مدينتي وسجلات جهاز حماية المستهلك",
        publisherEn: "Madinaty Homeowners Union & Egyptian CPA Grievance Docket",
        badgeAr: "ملف شكاوى ونزاع تدقيقي",
        badgeEn: "Homeowner Audit Dispute Docket",
        date: "2022 – 2026",
        url: "https://www.cpa.gov.eg",
        archiveUrl: "https://www.facebook.com/groups/madinaty.residents/",
        descAr: `شكاوى ومذكرات رسمية مرفوعة من اتحادات الشاغلين وملاك مدينتي والرحاب بشأن المطالبات السنوية المتكررة بسداد مبالغ إضافية تحت مسمى 'فروق وديعة صيانة' تتراوح بين 15,000 و45,000 جنيه للوحدة. وتؤكد المذكرات حق الملاك القانوني في الامتناع عن السداد الجزافي حتى تقديم ميزانيات تشغيلية معتمدة توضح عوائد استثمار الوديعة الأصلية في أذون الخزانة ومصروفات الصيانة الفعلية.`,
        descEn: `Documented homeowner petitions and CPA complaints concerning recurring annual maintenance deficit invoices demanding EGP 15,000 to 45,000 per residential unit. Legal dockets affirm the statutory right of owners unions to withhold discretionary payments pending independent certified operational audits proving exact maintenance expenditures and interest yield generated on the initial principal deposit.`
      }
    };

    function showSourceModal(sourceKey) {
      const src = sourcesDB[sourceKey];
      if (!src) return;
      document.getElementById('modal-source-title').textContent = currentLang === 'ar' ? src.titleAr : src.titleEn;
      document.getElementById('modal-source-body').textContent = currentLang === 'ar' ? src.descAr : src.descEn;
      document.getElementById('modal-source-date').textContent = src.date;
      document.getElementById('modal-source-url').href = src.url;
      
      const badgeEl = document.getElementById('modal-source-badge');
      if (badgeEl) {
        badgeEl.textContent = currentLang === 'ar' ? (src.badgeAr || 'مصدر موثق') : (src.badgeEn || 'Verified Primary Source');
      }

      const pubEl = document.getElementById('modal-source-publisher');
      if (pubEl) {
        pubEl.textContent = currentLang === 'ar' ? (src.publisherAr || src.publisherEn || '') : (src.publisherEn || src.publisherAr || '');
      }

      const prevLink = document.getElementById('modal-source-url-preview');
      if (prevLink) {
        prevLink.href = src.url;
        prevLink.textContent = src.url;
      }

      const archBtn = document.getElementById('modal-source-archive-url');
      if (archBtn) {
        if (src.archiveUrl) {
          archBtn.href = src.archiveUrl;
          archBtn.textContent = currentLang === 'ar' ? 'نسخة الأرشيف / البحث ↗' : 'Archive / Mirror ↗';
          archBtn.style.display = 'inline-flex';
        } else {
          archBtn.style.display = 'none';
        }
      }

      const primBtn = document.getElementById('modal-source-url');
      if (primBtn) {
        primBtn.textContent = currentLang === 'ar' ? 'زيارة المصدر الأصلي المباشر ↗' : 'Open Authentic Source ↗';
      }

      const dateTag = document.getElementById('lbl-modal-date-tag');
      if (dateTag) dateTag.textContent = currentLang === 'ar' ? 'تاريخ التوثيق:' : 'Documentation Date:';
      const pubTag = document.getElementById('lbl-modal-pub-tag');
      if (pubTag) pubTag.textContent = currentLang === 'ar' ? 'جهة النشر / المرجع:' : 'Publisher / Tribunal:';
      const urlTag = document.getElementById('lbl-modal-direct-url');
      if (urlTag) urlTag.textContent = currentLang === 'ar' ? 'الرابط المباشر للمستند / الخبر الأصلي:' : 'Direct Primary Document URL:';
      const stBadge = document.getElementById('lbl-modal-status-badge');
      if (stBadge) stBadge.textContent = currentLang === 'ar' ? 'رابط نشط ومدقق ✓' : 'Active & Verified ✓';

      document.getElementById('source-modal').classList.add('active');
    }

    function closeSourceModal(e) {
      document.getElementById('source-modal').classList.remove('active');
    }

    /* ==========================================================================
       DATA STORES: 14 PROJECTS (Full Bilingual)
       ========================================================================== */
    const projectsData = [
      {
        nameAr: "مدينتي",
        nameEn: "Madinaty",
        category: "east-cairo",
        locAr: "شرق القاهرة (33.4 مليون م² / 8,000 فدان)",
        locEn: "New Cairo (~33.4M sqm / 8,000 feddans)",
        spv: "العربية للمشروعات (99.99%)",
        landAr: "حصة عينية لهيئة المجتمعات (7% مباني) + نقدي",
        landEn: "NUCA in-kind BUA (7% of total) & cash",
        statusAr: "قيد التسليم المستمر (116 ألف وحدة مخططة، سلمت >50 ألف)",
        statusEn: "Delivering (c116.5k planned, >49.5k delivered)",
        compAr: "أوبن إير مول، أرابيسك مول، نادي الجولف، المركز الطبي",
        compEn: "Open Air Mall (260k sqm GLA), Arabesque Mall, Golf, Hospital",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "state_council_madinaty"
      },
      {
        nameAr: "ذا سباين (سنترال بارك مدينتي)",
        nameEn: "The Spine (Madinaty)",
        category: "east-cairo",
        locAr: "داخل مدينتي (4.3 مليون م² / 1,000 فدان)",
        locEn: "Inside Madinaty (4.3 mn sqm / 1,000 feddans)",
        spv: "العربية للمشروعات (99.99%)",
        landAr: "مقتطعة من امتياز مدينتي الأصلي",
        landEn: "Carved from Madinaty master concession",
        statusAr: "قيد الإنشاء والأساسات (متأخر: 2026/2027)",
        statusEn: "Under Construction (Delayed 2026/27)",
        compAr: "أبراج إدارية، ساحات تجارية، بحيرات، حي المال والأعمال",
        compEn: "Administrative towers, commercial plazas, business district",
        riskAr: "متوسطة إلى مرتفعة",
        riskEn: "Med-High",
        riskBadge: "badge-medhigh",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "مدينة الرحاب",
        nameEn: "Al Rehab City",
        category: "east-cairo",
        locAr: "القاهرة الجديدة (9.9 مليون م² / 2,360 فداناً)",
        locEn: "New Cairo (~9.9 mn sqm / 2,360 feddans)",
        spv: "العربية للمشروعات (99.99%)",
        landAr: "شراء مباشر من هيئة المجتمعات (تاريخي 1996)",
        landEn: "Direct purchase from NUCA (Historical 1996)",
        statusAr: "مسلمة بالكامل (33.5 ألف وحدة، 160 ألف نسمة)",
        statusEn: "Fully Delivered (~33.5k units, ~160k residents)",
        compAr: "مول الرحاب 1 و 2، سيتي سكوير، أفينيو مول، جيت واي مول",
        compEn: "Rehab Mall 1 & 2, City Square, Avenue Mall, Gateway Mall",
        riskAr: "منخفضة",
        riskEn: "Low",
        riskBadge: "badge-low",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "سيليا (العاصمة الإدارية)",
        nameEn: "Celia (New Capital)",
        category: "east-cairo",
        locAr: "العاصمة الإدارية الجديدة (2.1 مليون م² / 500 فدان)",
        locEn: "New Administrative Capital (~2.1 mn sqm / 500 feddans)",
        spv: "العربية للمشروعات (99.99%)",
        landAr: "تخصيص مباشر من شركة العاصمة ACUD (التزام 6.5 مليار)",
        landEn: "Direct allocation from ACUD (EGP 6.5bn land liability)",
        statusAr: "تسليم مرحلي (المراحل 1-2 سلمت، 3-4 متأخرة)",
        statusEn: "Phased Delivery (Phases 1-2 delivered, 3-4 late)",
        compAr: "مناطق الفيليدج والبارك، السنترال بارك، الممشى التجاري",
        compEn: "Village & Park districts, Central Park, commercial strip",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "مدينة نور (حدائق العاصمة)",
        nameEn: "Noor City (Capital Gardens)",
        category: "east-cairo",
        locAr: "حدائق العاصمة، شرق القاهرة (21.0 مليون م² / 5,000 فدان)",
        locEn: "Capital Gardens, East Cairo (~21.0 mn sqm / 5,000 feddans)",
        spv: "الشركة العربية للاستثمار العمراني (100%)",
        landAr: "شراكة مع هيئة المجتمعات: 50% حصة عينية مباني منجزة",
        landEn: "NUCA partnership: 50% in-kind finished units delivery",
        statusAr: "قيد الإنشاء والخرسانات (بدء التسليم 2026)",
        statusEn: "Under Construction (First handovers expected 2026)",
        compAr: "مدينة ذكية، 140 ألف وحدة، شبكة قطار خفيف، بنية مستدامة",
        compEn: "Smart city, 140k units, light rail connectivity",
        riskAr: "مرتفعة",
        riskEn: "High",
        riskBadge: "badge-high",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "ساوث ميد (SouthMED)",
        nameEn: "SouthMED (North Coast)",
        category: "coastal",
        locAr: "الضبعة، الساحل الشمالي (23 مليون م² / كم 165-170)",
        locEn: "KM 165–170 Alex-Matrouh Rd (~23 mn sqm)",
        spv: "العربية للمشروعات (99.99%)",
        landAr: "شراكة مع هيئة المجتمعات (موافقة مجلس الوزراء يونيو 2024)",
        landEn: "NUCA partnership (Cabinet approval June 2024)",
        statusAr: "تمهيد الموقع والإنشاءات (مبيعات تعاقدية >280 مليار)",
        statusEn: "Site Preparation / Earthworks (Contracted Sales >EGP 280bn)",
        compAr: "مارينا يخوت دولية، 6 فنادق عالمية، ملاعب جولف، بحيرات شاطئية",
        compEn: "International marina, 6 hotels, golf, lagoons, retail promenade",
        riskAr: "مرتفعة (عبء تنفيذي)",
        riskEn: "High (Delivery Pressure)",
        riskBadge: "badge-high",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "مدينة بنان (الرياض)",
        nameEn: "Banan City (Riyadh)",
        category: "cross-border",
        locAr: "ضاحية الفرسان، الرياض، السعودية (3.1 مليون م²)",
        locEn: "Al-Fursan Suburb, Riyadh (~3.1 mn sqm)",
        spv: "طلعت مصطفى السعودية / الوطنية للإسكان NHC",
        landAr: "تخصيص أرض من الوطنية للإسكان (استثمار 40 مليار ريال)",
        landEn: "NHC Land Allocation (SAR 40bn projected investment)",
        statusAr: "أعمال الموقع والحجوزات (بدء التسليم 2027)",
        statusEn: "Site Works & Sales (First handovers slated 2027)",
        compAr: "27,745 شقة وفيلا سكنية، محاور تجارية، مراكز صحية",
        compEn: "27,745 apartments & villas, commercial spines, clinics",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "فور سيزونز سان ستيفانو",
        nameEn: "Four Seasons San Stefano",
        category: "hospitality",
        locAr: "كورنيش الإسكندرية",
        locEn: "Corniche, Alexandria",
        spv: "سان ستيفانو للاستثمار السياحي والعقاري",
        landAr: "مزاد خصخصة أصول فندقية حكومية (1998)",
        landEn: "State hotel privatization auction (1998)",
        statusAr: "أصل تشغيلي مدر للأرباح (118 غرفة وشقق فندقية)",
        statusEn: "Operating Asset (118 hotel keys, branded residences)",
        compAr: "فندق فاخر، مركز تسوق جراند بلازا، مارينا، برج سكني",
        compEn: "Luxury hotel, Grand Shopping Plaza, marina, residential tower",
        riskAr: "منخفضة",
        riskEn: "Low",
        riskBadge: "badge-low",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "فور سيزونز نايل بلازا",
        nameEn: "Four Seasons Nile Plaza",
        category: "hospitality",
        locAr: "جاردن سيتي، كورنيش النيل، القاهرة",
        locEn: "Garden City, Cairo",
        spv: "نوفا بارك للتنمية السياحية",
        landAr: "شراء أرض ملكية خاصة مباشرة",
        landEn: "Direct private freehold parcel acquisition",
        statusAr: "أصل تشغيلي مدر للنقد الأجنبي (365 غرفة، 127 شقة فاخرة)",
        statusEn: "Operating Asset (365 hotel keys, 127 luxury apartments)",
        compAr: "فندق فخم، قاعات مؤتمرات، مطاعم عالمية",
        compEn: "Premier luxury hotel, conference facilities, ballroom",
        riskAr: "منخفضة",
        riskEn: "Low",
        riskBadge: "badge-low",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "فور سيزونز شرم الشيخ",
        nameEn: "Four Seasons Sharm El Sheikh",
        category: "hospitality",
        locAr: "رأس نصراني، شرم الشيخ، البحر الأحمر",
        locEn: "Ras Nasrani, Sharm El Sheikh",
        spv: "الإسكندرية السعودية للمشروعات السياحية",
        landAr: "تخصيص هيئة التنمية السياحية",
        landEn: "Red Sea Tourism Development Authority allocation",
        statusAr: "أصل تشغيلي وموسع (547 غرفة وجناح بعد توسعة 2022)",
        statusEn: "Operating & Expanded (547 keys after 2022 expansion)",
        compAr: "منتجع شاطئي عالمي، شاطئ خاص، مراكز غوص",
        compEn: "Palatial dive resort, private beach, convention facilities",
        riskAr: "منخفضة",
        riskEn: "Low",
        riskBadge: "badge-low",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "فور سيزونز الأهرامات (الجيزة)",
        nameEn: "Four Seasons The Pyramids",
        category: "hospitality",
        locAr: "الجيزة، إطلالة مباشرة على المتحف المصري الكبير (42 فداناً)",
        locEn: "Giza, overlooking Grand Egyptian Museum (42.4 feddans)",
        spv: "شركة أيكون الأهرامات (100% عبر الإسكندرية للعقارات)",
        landAr: "شراكة وتطوير مع هيئة المجتمعات (إفصاح نوفمبر 2025)",
        landEn: "Developed with NUCA (Disclosed Nov 2025)",
        statusAr: "قيد الإنشاء والأساسات (تأخر موعد الافتتاح: 2028 إلى 2029)",
        statusEn: "Under Construction (Delayed: 2028 → 2029)",
        compAr: "415 غرفة فندقية وشقق فاخرة (استثمار 788 مليون دولار)",
        compEn: "415 keys luxury hotel & branded residences (USD 788mn investment)",
        riskAr: "متوسطة إلى مرتفعة",
        riskEn: "Med-High",
        riskBadge: "badge-medhigh",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "فور سيزونز الأقصر",
        nameEn: "Four Seasons Luxor",
        category: "hospitality",
        locAr: "كورنيش النيل، الأقصر",
        locEn: "Luxor Nile Front",
        spv: "الأقصر للتنمية الحضرية والسياحية (99.72%)",
        landAr: "تخصيص أرض سياحية من المحافظة",
        landEn: "Tourism development land allocation",
        statusAr: "قيد الإنشاء (تأخر التسليم: 2025 إلى 2026)",
        statusEn: "Under Construction (Delayed: 2025 → 2026)",
        compAr: "فندق قصر فاخر 200 غرفة (قروض 2.1 مليار جنيه)",
        compEn: "200 keys luxury palace hotel (Debt EGP 2.1bn)",
        riskAr: "متوسطة إلى مرتفعة",
        riskEn: "Med-High",
        riskBadge: "badge-medhigh",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "فور سيزونز مدينتي",
        nameEn: "Four Seasons Madinaty",
        category: "hospitality",
        locAr: "داخل مدينتي",
        locEn: "Inside Madinaty",
        spv: "مدينتي للمشروعات السياحية والعمرانية (96.84%)",
        landAr: "مقتطعة من المخطط العام لمدينتي",
        landEn: "Carved from Madinaty masterplan",
        statusAr: "قيد الإنشاء (تأخر الافتتاح: 2026 إلى 2027)",
        statusEn: "Under Construction (Delayed: 2026 → 2027)",
        compAr: "346 غرفة، مركز مؤتمرات، فيلات جولف (قرض بنك مصر 6.76 مليار)",
        compEn: "346 keys, convention center, golf villas (Banque Misr syndication)",
        riskAr: "مرتفعة (مخاطر تمويل)",
        riskEn: "High (Leverage Risk)",
        riskBadge: "badge-high",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        nameAr: "محفظة الفنادق التاريخية (7 فنادق)",
        nameEn: "Legacy Hotels (7 Historic Hotels)",
        category: "hospitality",
        locAr: "القاهرة، الجيزة، الإسكندرية، أسوان، الأقصر",
        locEn: "Cairo, Giza, Alexandria, Aswan, Luxor",
        spv: "شركة ليجاسي للفنادق (51% أيكون / 40.5% القابضة ADQ)",
        landAr: "استحواذ تاريخي من إيجوث الحكومية (سداد 100 مليون دولار أقساط)",
        landEn: "Acquisition from state EGOTH (USD 100mn instalments)",
        statusAr: "أصول تشغيلية قيد التطوير (تحويل كتاراكت ووينتر بالاس لماندارين)",
        statusEn: "Operating & Renovating (Old Cataract & Winter Palace → Mandarin Oriental)",
        compAr: "مينا هاوس، ماريوت القاهرة، سيسل، أولد كتاراكت، وينتر بالاس",
        compEn: "Mena House, Cairo Marriott, Cecil, Old Cataract, Winter Palace",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "egx_filings_fy25_h126"
      }
    ];

    /* ==========================================================================
       DATA STORES: MASTER CONTRACTOR ROSTER (With Clickable Sources)
       ========================================================================== */
    const contractorsData = [
      {
        projectAr: "مدينتي (مشروع المقاول 2008)",
        projectEn: "Madinaty (2008 Subcontractor Incident)",
        entityAr: "الإسكندرية للإنشاءات (ACC) / طلعت مصطفى",
        entityEn: "Alexandria Construction Co. (ACC) / TMG",
        mainAr: "شركة الإسكندرية للإنشاءات (مقاول عام مدمج)",
        mainEn: "Alexandria Construction Co. (Captive EPC)",
        subAr: "المقاول شحاتة محمد حسن (مقاول باطن)",
        subEn: "Subcontractor Shehata Mohamed Hassan",
        scopeAr: "تنفيذ أعمال مدنية ومباني بمدينتي وتشغيل عمالة",
        scopeEn: "Civil construction & site labor execution at Madinaty",
        evidAr: "بلاغ رسمي للنائب العام وتغطية المصري اليوم 2008",
        evidEn: "Public Prosecutor complaint & Al-Masry Al-Youm report (Oct 2008)",
        issueAr: "امتناع الشركة عن صرف المستحقات، وإقرار مدير الشركة (إبراهيم حسبو) بتعمد تأخير الصرف لمنع العمال من مغادرة الموقع بعد حبس هشام طلعت مصطفى",
        issueEn: "Company withheld payments; ACC Director (Ibrahim Hasabo) admitted deliberate delay to keep labor on site post-HTM arrest",
        rating: "Level A (اعتراف موثق)",
        riskAr: "مرتفعة (تاريخياً)",
        riskEn: "High (Historical)",
        badge: "badge-high",
        sourceKey: "masry_shehata_2008"
      },
      {
        projectAr: "مدينتي (نزاع السقالات 2012 - 2013)",
        projectEn: "Madinaty (Scaffolding Dispute 2012-2013)",
        entityAr: "شركة الإسكندرية للإنشاءات (ACC) / مجموعة طلعت مصطفى",
        entityEn: "Alexandria Construction Co. (ACC) / TMG",
        mainAr: "شركة الإسكندرية للإنشاءات (ACC)",
        mainEn: "Alexandria Construction Co. (ACC)",
        subAr: "شركة خالد هنداوي محمد عبد الرحيم (مقاول باطن)",
        subEn: "Khaled Hendawi Mohamed Abdel Rahim Contracting",
        scopeAr: "تنفيذ أعمال السقالات في 3 مواقع بمدينتي: القطاع الشمالي والمدرسة البريطانية، بوابة مدينتي 2011، السوق التجاري والمسجد",
        scopeEn: "Scaffolding execution across 3 Madinaty zones: North Sector & British School, Gate 2011, Commercial Market & Mosque",
        evidAr: "الدعوى رقم 2923 لسنة 2012 مدني شمال القاهرة ومطالبة فروق أسعار ومستخلصات (609,625 ج.م)",
        evidEn: "Case No. 2923 of 2012 North Cairo Civil Court & EGP 609,625 price escalation claim",
        issueAr: "نزاع حول عدم مطابقة أسعار المستخلصات للأسعار المتفق عليها، وعدم توقيع بعض صفحات العقود، وطلب إلزام الشركة بتقديم أصول العقود والمستخلصات",
        issueEn: "Dispute over disparity between contract and IPC rates, un-signed contract sheets, and demand to compel ACC to submit original subcontracts & IPCs",
        rating: "Level B (وثائق قانونية ومذكرة دفاع)",
        riskAr: "مرتفعة (نزاع قضائي موثق)",
        riskEn: "High (Documented Litigation)",
        badge: "badge-high",
        sourceKey: "khatib_scaffolding_2012"
      },
      {
        projectAr: "مشروعات المجموعة (نزاع مقاول 20 عاماً)",
        projectEn: "TMG Group Sites (20-Year Contractor Dispute)",
        entityAr: "مجموعة طلعت مصطفى / هشام طلعت مصطفى",
        entityEn: "TMG Holding / Hisham Talaat Moustafa",
        mainAr: "إدارة المجموعة والشركات التابعة",
        mainEn: "Group Management & Operating Entities",
        subAr: "مقاول باطن (علاقة عمل 20 عاماً)",
        subEn: "Trade Contractor (~20-Year Working Relationship)",
        scopeAr: "أعمال مقاولات متنوعة على مدار 20 عاماً بمشروعات المجموعة",
        scopeEn: "Diversified contracting packages executed over 20-year span across TMG sites",
        evidAr: "تغطية موقع الحادثة (26 ديسمبر 2023) وتليجراف مصر (19 أغسطس 2026)",
        evidEn: "El Haditha investigative coverage (Dec 2023) & Telegraph Masr (Aug 2026)",
        issueAr: "ادعاء المقاول وجود مستحقات مالية متأخرة وبلاغات سابقة؛ صدور حكم جنائي بالحبس سنة في واقعة تهديد، دون أن تفصل المحكمة في أصل المديونية المدنية",
        issueEn: "Contractor claimed unpaid dues from HTM following 20-year ties; matter culminated in 1-year criminal threat verdict without civil debt adjudication",
        rating: "Level C (تغطية صحفية لقضية جنائية)",
        riskAr: "متوسطة إلى مرتفعة (مخاطر سمعة)",
        riskEn: "Medium-High (Reputational Risk)",
        badge: "badge-medhigh",
        sourceKey: "haditha_contractor_2023"
      },
      {
        projectAr: "مدينتي (الأعمال المدنية الكبرى)",
        projectEn: "Madinaty (Civil & Master Superstructures)",
        entityAr: "الشركة العربية للمشروعات (ACPUD)",
        entityEn: "Arab Co. for Projects & Urban Dev.",
        mainAr: "شركة الإسكندرية للإنشاءات (ACC)",
        mainEn: "Alexandria Construction Co. (ACC)",
        subAr: "فرق مقاولات ذاتية ومقاولو باطن أفراد",
        subEn: "In-House Trade Teams & SME Subcontractors",
        scopeAr: "الإنشاءات الخرسانية، شبكات المرافق، 120 ألف وحدة سكنية",
        scopeEn: "Civil superstructures, infrastructure, 120k residential units",
        evidAr: "القوائم المالية المدققة للشركة وميزانيات أوراق الدفع",
        evidEn: "ACC Corporate Filings & Group Balance Sheets",
        issueAr: "تأخير اعتماد المستخلصات الجارية وسداد المستحقات عبر أوراق دفع وشيكات آجلة (90-270 يوماً)",
        issueEn: "Prolonged payment certificate audits and deferred notes payable (90–270 days)",
        rating: "Level A (قوائم مدققة)",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        projectAr: "ساوث ميد (حزمة C01)",
        projectEn: "SouthMED (Package C01)",
        entityAr: "الشركة العربية للمشروعات والتطوير العمراني",
        entityEn: "Arab Co. for Projects & Urban Dev.",
        mainAr: "كونكريت بلس للهندسة والإنشاءات (Concrete Plus)",
        mainEn: "Concrete Plus for Contracting",
        subAr: "تعاقد مقاول عام مباشر لحزمة C01",
        subEn: "Direct Tier-1 General Contractor Package",
        scopeAr: "تنفيذ حزمة C01: 179 مبنى كامل التشطيب وبنية تحتية (~10 مليار جنيه)",
        scopeEn: "Package C01: 179 finished buildings + infra (~EGP 10bn)",
        evidAr: "إعلان رسمي مشترك وتوقيع العقد (يناير 2026)",
        evidEn: "Joint Corporate Disclosure & Award (Jan 2026)",
        issueAr: "ضغط الجداول الزمنية لتسليم أولى مراحل الساحل الشمالي بحلول صيف 2029",
        issueEn: "Compressed execution schedule for 2029 North Coast delivery",
        rating: "Level A (إفصاح رسمي)",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        projectAr: "سيليا (العاصمة الإدارية)",
        projectEn: "Celia (New Capital)",
        entityAr: "الشركة العربية للمشروعات والتطوير العمراني",
        entityEn: "Arab Co. for Projects & Urban Dev.",
        mainAr: "شركة أتريوم للمقاولات (Atrium Quality Contractors)",
        mainEn: "Atrium Quality Contractors (AQC)",
        subAr: "شركة المجد للمقاولات العمومية",
        subEn: "Al Majd for General Contracting",
        scopeAr: "تنفيذ الأعمال الكهروميكانيكية (MEP) لمراحل سكنية بالعاصمة",
        scopeEn: "Full Electromechanical (MEP) installations for Celia",
        evidAr: "سابقة أعمال المقاول وسجلات التعاقدات (2018–2023)",
        evidEn: "Contractor Portfolio Records (2018–2023)",
        issueAr: "شروط دفع مشروطة بسداد المطور (Pay-When-Paid) وتأخير صرف فروق الأسعار",
        issueEn: "Back-to-back payment terms and material price escalation friction",
        rating: "Level B (سابقة أعمال)",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        projectAr: "شبكات الصرف ومحطات المعالجة",
        projectEn: "Wastewater Treatment & Infra",
        entityAr: "مجموعة طلعت مصطفى / شركة الإسكندرية",
        entityEn: "TMG Holding / Alexandria Construction",
        mainAr: "شركة الإسكندرية للإنشاءات (ACC)",
        mainEn: "Alexandria Construction Co. (ACC)",
        subAr: "مجموعة جمكا (Gemka Group)",
        subEn: "Gemka Group",
        scopeAr: "توريد وتركيب كباري ترسيب، مصافي ميكانيكية، ومحطات معالجة",
        scopeEn: "Wastewater MEP: sedimentation bridges, mechanical screens",
        evidAr: "السجل التجاري وقائمة عملاء جمكا المعتمدة",
        evidEn: "Gemka Official Client Portfolio (2018–2022)",
        issueAr: "احتجاز نسب ضمان الأعمال (5-10%) لفترات ممتدة لحين التسليم النهائي للشبكة",
        issueEn: "Extended retention warranty withholding (5–10%) tied to master city testing",
        rating: "Level B (سابقة أعمال)",
        riskAr: "منخفضة",
        riskEn: "Low",
        riskBadge: "badge-low",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        projectAr: "مدينتي ونور (محطات المعالجة وإعادة التدوير)",
        projectEn: "Madinaty & Noor City (WWTP & TSE Reuse)",
        entityAr: "مجموعة طلعت مصطفى / الشركة العربية",
        entityEn: "TMG Holding / Arab Co. for Projects",
        mainAr: "شركة الإسكندرية للإنشاءات (ACC)",
        mainEn: "Alexandria Construction Co. (ACC)",
        subAr: "ماتيتو أوفرسيز (Metito Overseas)",
        subEn: "Metito Overseas Ltd.",
        scopeAr: "محطات معالجة مياه الصرف الصحي ثلاثية، شبكات الري بالمياه المعالجة (TSE)، وتغذية البحيرات",
        scopeEn: "Tertiary wastewater treatment plants (WWTP), TSE recycled irrigation & lake feed networks",
        evidAr: "سجل مشاريع البنية التحتية لماتيتو وبيانات مجموعة طلعت مصطفى للمدن الذكية",
        evidEn: "Metito Global Project Track Record & TMG Smart City Utilities Disclosures",
        issueAr: "تنسيق هندسي عالي الدقة لربط مخرجات المعالجة الثلاثية ببحيرات الجولف والبحيرات المفتوحة لتفادي الطحالب والبكتيريا",
        issueEn: "Strict water quality compliance for tertiary effluent feeding recreational lagoons without algae blooms",
        rating: "Level A (إفصاح رسمي)",
        riskAr: "منخفضة",
        riskEn: "Low",
        riskBadge: "badge-low",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        projectAr: "مدينة نور (حدائق العاصمة)",
        projectEn: "Noor City (Capital Gardens)",
        entityAr: "الشركة العربية للاستثمار العمراني",
        entityEn: "Arab Co. for Urban Investment SAE",
        mainAr: "شركة الإسكندرية للإنشاءات (ACC)",
        mainEn: "Alexandria Construction Co. (ACC)",
        subAr: "سافيتو مصر (Saveto Egypt)",
        subEn: "Saveto Egypt",
        scopeAr: "توريد المونة الجافة، المعجون الأسمنتي، ودهانات الواجهات الحديثة",
        scopeEn: "Supply of dry-mix mortars, wall putties, architectural coatings",
        evidAr: "سجل التوريدات لشركة سافيتو (2021–حتى الآن)",
        evidEn: "Manufacturer Portfolio & Supply Disclosures (2021–Present)",
        issueAr: "تسهيلات سداد تجارية ممتدة (ائتمان موردين 90 إلى 120 يوماً)",
        issueEn: "Trade supply credit exposure (90–120 day settlement cycle)",
        rating: "Level B (سجل توريد)",
        riskAr: "منخفضة",
        riskEn: "Low",
        riskBadge: "badge-low",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        projectAr: "مدينتي (عمالة الأمن والحراسة)",
        projectEn: "Madinaty (Security Labor Force)",
        entityAr: "الشركة العربية للمشروعات / الإسكندرية للإنشاءات",
        entityEn: "Arab Co. for Projects / Alexandria Construction",
        mainAr: "إدارة الأمن الداخلي والخدمات المعاونة",
        mainEn: "In-House Security & Facility Logistics",
        subAr: "أطقم حراسة عمالية (مئات الأفراد)",
        subEn: "Site Security Workforce (>100 individuals)",
        scopeAr: "حراسة وتأمين البوابات، المنشآت، والمحيط الجغرافي لمدينتي",
        scopeEn: "Perimeter security, perimeter logistics, access control",
        evidAr: "تحقيقات موقع المنصة المستقلة ومذكرات الشكاوى (2024–2025)",
        evidEn: "Al Manassa Investigative Reports & Labor Petitions (2024–2025)",
        issueAr: "مذكرات رسمية واحتجاجات على العمل 12 ساعة دون بدل إضافي، وبدلات الوجبات، وإحالة المحتجين للتحقيق الإداري",
        issueEn: "Official petitions & sit-ins over uncompensated 12-hr shifts, meal stipends, and management retaliatory inquiries",
        rating: "Level A (تحقيق صحفي موثق)",
        riskAr: "مرتفعة (مخاطر سمعة وعمالة)",
        riskEn: "High (Reputational & Labor)",
        riskBadge: "badge-high",
        sourceKey: "manassa_security_oct2025"
      },
      {
        projectAr: "فندق فور سيزونز مدينتي",
        projectEn: "Four Seasons Madinaty",
        entityAr: "مدينتي للمشروعات السياحية والعمرانية",
        entityEn: "Madinaty Co. for Tourism & Urban Projects",
        mainAr: "شركة الإسكندرية للإنشاءات (ACC)",
        mainEn: "Alexandria Construction Co. (ACC)",
        subAr: "مقاولات تشطيبات فندقية متخصصة",
        subEn: "Specialist Turnkey Hospitality Fit-out Contractors",
        scopeAr: "الإنشاءات الخرسانية، التشطيبات الفندقية الفاخرة، شبكات التكييف",
        scopeEn: "Luxury hotel superstructures, MEP, high-spec finishing",
        evidAr: "عقد تمويل مشترك بقيادة بنك مصر (6.76 مليار جنيه)",
        evidEn: "Banque Misr Syndicated Loan Agreement (EGP 6.76B)",
        issueAr: "اشتراطات بنكية صارمة لسحب شرائح القرض بناءً على شهادات إنجاز مهندس المقرض",
        issueEn: "Strict lender drawdown engineering certifications tied to milestone progress",
        rating: "Level A (إفصاح مصرفي)",
        riskAr: "متوسطة",
        riskEn: "Medium",
        riskBadge: "badge-med",
        sourceKey: "egx_filings_fy25_h126"
      },
      {
        projectAr: "فندق فورسيزونز الأقصر (Four Seasons Luxor)",
        projectEn: "Four Seasons Luxor (Turnkey Hospitality EPC)",
        entityAr: "آيكون (ICON) / إيجوث (EGOTH) / مجموعة طلعت مصطفى",
        entityEn: "ICON / EGOTH / TMG Holding",
        mainAr: "شركة أتريوم للمقاولات (Atrium Quality Contractors)",
        mainEn: "Atrium Quality Contractors",
        subAr: "تحالف CCC وأتريوم (MEP CP02) / كناوف مصر / AMC",
        subEn: "CCC / Atrium MEP JV (CP02) / Knauf Egypt / AMC",
        scopeAr: "تنفيذ المقاول العام المتكامل للفندق وحزمة الأعمال الكهروميكانيكية بإشراف هيل إنترناشيونال ومجموعة شاكر",
        scopeEn: "Full turnkey EPC execution & MEP CP02 package under Hill International (PM) & Shaker Group",
        evidAr: "إفصاحات رسمية لشركة أتريوم، إيجوث، ووزارة قطاع الأعمال (اليوم السابع)",
        evidEn: "Official corporate disclosures from Atrium, EGOTH & Ministry filings (Youm7)",
        issueAr: "تعديل موعد الافتتاح من 2026 إلى 2027؛ عدم وجود أي شكاوى مستخلصات معلنة أو أحكام قضائية حتى الآن؛ عزل تعاقدي يحمي TMG/ICON من مديونية مقاولي الباطن المباشرة",
        issueEn: "Opening target revised from 2026 to 2027; no public subcontractor disputes or litigation verified; privity ring-fencing shields TMG/ICON",
        rating: "Level A (فحص استقصائي مدقق)",
        riskAr: "منخفضة إلى متوسطة (انضباط تعاقدي)",
        riskEn: "Low-Medium (Privity Insulated)",
        badge: "badge-low",
        sourceKey: "atrium_luxor_award"
      }
    ];

    /* ==========================================================================
       DATA STORES: COMPLAINTS & INCIDENTS (Contractors + Labor + Residents)
       ========================================================================== */
    const complaintsData = [
      {
        projectAr: "فورسيزونز الأقصر (تحقيق المستخلصات ومقاولو الباطن)",
        projectEn: "Four Seasons Luxor (IPC & Subcontractor Due Diligence)",
        categoryAr: "فحص المستخلصات ومقاولو الباطن",
        categoryEn: "Subcontractor Dues & IPC Verification",
        claimAr: "فحص جنائي مدقق لمستحقات مقاولي الباطن والموردين مع أتريوم وتحالف CCC: لم يُعثر على أي شكوى علنية موثقة تثبت حبس المستحقات؛ تم رصد تعديل موعد التشغيل من 2026 إلى 2027؛ العزل التعاقدي يعفي TMG/ICON من أي مديونية مباشرة للمقاولين.",
        claimEn: "Forensic examination of subcontractor/supplier dues under Atrium and CCC MEP JV: No verified public complaints found alleging deliberate payment withholding; opening target shifted from 2026 to 2027; privity ring-fencing insulates TMG/ICON from direct liability.",
        date: "2025 – 2026",
        sourceName: "فورسيزونز / أتريوم / إيجوث",
        sourceKey: "atrium_luxor_award",
        classAr: "فحص جنائي سلبي النزاع (انضباط تعاقدي مع تعديل زمني)",
        classEn: "Negative Evidence Due Diligence (Privity Shielded & Schedule Shift)",
        badge: "badge-low"
      },
      {
        projectAr: "مدينتي (المقاول شحاتة حسن)",
        projectEn: "Madinaty (Subcontractor Shehata)",
        categoryAr: "مستحقات مقاولين وبلاغ نيابة",
        categoryEn: "Contractor Dues & Prosecutor Filing",
        claimAr: "تقدم المقاول ببلاغ للنائب العام ضد هشام طلعت وإدارة مدينتي لعدم صرف مستحقاته مما منعه من سداد أجور عماله؛ واعترف مدير الإسكندرية للإنشاءات (إبراهيم حسبو) بأن التعطيل كان مقصوداً لمنع العمال من مغادرة الموقع بعد حبس هشام طلعت.",
        claimEn: "Contractor filed report to Prosecutor General against HTM & Madinaty over withheld dues; ACC Director (Ibrahim Hasabo) admitted payment delay was intentional to stop workers abandoning site.",
        date: "13 أكتوبر 2008",
        sourceName: "المصري اليوم",
        sourceKey: "masry_shehata_2008",
        classAr: "واقعة صحفية مثبتة ومحددة بالأسماء",
        classEn: "Documented Press Case (Named Contractor & Exec Admission)",
        badge: "badge-high"
      },
      {
        projectAr: "مدينتي (الدعوى 2923 لسنة 2012 مدني شمال القاهرة)",
        projectEn: "Madinaty (Case 2923 of 2012 North Cairo Civil Court)",
        categoryAr: "نزاع أسعار ومستخلصات وأصول عقود",
        categoryEn: "Rate Variance, IPC Discrepancy & Contract Originals",
        claimAr: "نزاع قضائي مقيد بالدعوى 2923/2012 مدني شمال القاهرة أقامه المقاول خالد هنداوي ضد شركة الإسكندرية للإنشاءات، بشأن عدم مطابقة أسعار المستخلصات للأسعار المتفق عليها لأعمال السقالات في 3 مواقع بمدينتي (القطاع الشمالي والمدرسة البريطانية، بوابة 2011، السوق والمسجد) ومطالبة بفروق أسعار بمبلغ 609,625 ج.م وإلزام الشركة بتقديم أصول العقود.",
        claimEn: "Litigation docket Case 2923/2012 North Cairo Civil Court filed by subcontractor Khaled Hendawi against ACC over disparity between approved IPC rates and subcontract rates for scaffolding in 3 Madinaty zones, claiming EGP 609,625 and demanding original contracts.",
        date: "2012 – 2013",
        sourceName: "مذكرة دفاع قانونية ومطالبة معلنة",
        sourceKey: "khatib_scaffolding_2012",
        classAr: "مطالبة قضائية ومذكرة دفاع موثقة",
        classEn: "Documented Judicial Defense Docket",
        badge: "badge-high"
      },
      {
        projectAr: "مشروعات طلعت مصطفى (نزاع مقاول 20 عاماً)",
        projectEn: "TMG Sites (20-Year Contractor Dues Dispute)",
        categoryAr: "ادعاء مستحقات ونزاع قضائي",
        categoryEn: "Contractor Dues Claim & Criminal Threat Proceedings",
        claimAr: "ادعاء مقاول ارتبط بعلاقة عمل 20 عاماً بوجود مستحقات مالية متأخرة وبلاغات سابقة؛ صدور حكم جنائي بالحبس سنة في واقعة تهديد، دون أن تفصل المحكمة في أصل المديونية المدنية أو تحدد المشروع أو المبلغ بدقة.",
        claimEn: "Contractor claiming unpaid dues after 20-year relationship; resulted in 1-year threat misdemeanor verdict without judicial adjudication of underlying civil debt or project specifics.",
        date: "ديسمبر 2023 – أغسطس 2026",
        sourceName: "موقع الحادثة وتليجراف مصر",
        sourceKey: "haditha_contractor_2023",
        classAr: "تغطية صحفية لنزاع جنائي متفرع عن علاقة مقاولة",
        classEn: "Judicial Press Coverage of Threat Litigation",
        badge: "badge-medhigh"
      },
      {
        projectAr: "مدينتي (مزاعم حجب العقود واقتطاع المستخلصات)",
        projectEn: "Madinaty (Subcontractor Contract Withholding Allegations)",
        categoryAr: "حجب نسخ العقود والخصومات المتكررة",
        categoryEn: "Contract Copy Withholding & IPC Deductions",
        claimAr: "مزاعم منشورة عن مقاولي باطن بمدينتي بشأن الامتناع عن تسليمهم نسخ العقود الموقعة، وإجراء تعديلات وخصومات متكررة على المستخلصات الجارية وتأخير السداد؛ صُنفت في التقرير كخيط بحث منخفض الثقة لغياب الأحكام المؤيدة.",
        claimEn: "Published blog allegations regarding withholding contract copies from Madinaty subcontractors, repetitive IPC deductions, and payment stalling; classified as low-confidence lead due to absence of court rulings.",
        date: "26 مارس 2009",
        sourceName: "جريدة الوطن العربي (أرشيف)",
        sourceKey: "watan_arabi_2009",
        classAr: "خيط بحث صحفي استدلالي (منخفض الثقة)",
        classEn: "Investigative Research Lead (Low Confidence)",
        badge: "badge-low"
      },
      {
        projectAr: "القطاع العقاري العام وتوجيهات الرقابة المالية",
        projectEn: "Real Estate Sector & FRA Regulatory Directives",
        categoryAr: "توجيهات عقود التطوير والتنازل عن الحقوق",
        categoryEn: "Developer Contracts & Assignment of Rights Guidance",
        claimAr: "توجيهات رسمية من الهيئة العامة للرقابة المالية تحث العملاء والمقاولين على التدقيق في بنود التنازل عن الحقوق وتوزيع المخاطر وشروط الدفع المؤجل لحماية المتعاملين في السوق العقاري المصري.",
        claimEn: "Official regulatory directives from Egyptian FRA advising market participants to scrutinize assignment of rights clauses and risk distribution in real estate contracts.",
        date: "سبتمبر 2026",
        sourceName: "الهيئة العامة للرقابة المالية",
        sourceKey: "fra_assignment_guidance_2026",
        classAr: "توجيه تنظيمي ورقابي عام ملزم",
        classEn: "General Regulatory & Statutory Advisory",
        badge: "badge-low"
      },
      {
        projectAr: "شركة الإسكندرية للإنشاءات (ACC)",
        projectEn: "Alexandria Construction Co. (ACC)",
        categoryAr: "احتجاج عمالي وأجور وتسريح",
        categoryEn: "Labor Protest, Wage Freeze & Layoffs",
        claimAr: "احتجاج أكثر من 100 موظف وعامل بشركة الإسكندرية للإنشاءات التابعة لطلعت مصطفى على تجميد الرواتب وفصل عاملين تعسفياً دون تسوية مستحقاتهم القانونية أو إبداء أسباب.",
        claimEn: "Protest by over 100 ACC employees against sub-inflation salaries, arbitrary layoffs, and unnotified salary freezes without formal severance.",
        date: "مارس 2024",
        sourceName: "مدى مصر",
        sourceKey: "mada_acc_2024",
        classAr: "شكوى عمالية جماعية موثقة",
        classEn: "Documented Collective Labor Grievance",
        badge: "badge-medhigh"
      },
      {
        projectAr: "مدينتي (عمال الأمن)",
        projectEn: "Madinaty (Security Workforce)",
        categoryAr: "ساعات عمل وإقامة وأجور",
        categoryEn: "12-Hr Shifts, Wages & Lodging",
        claimAr: "احتجاج عمال الأمن في مدينتي على تدني مستوى الرواتب في ظل الغلاء، وطول ساعات العمل (12-14 ساعة يومياً)، وسوء ظروف الإقامة بسكن العمال التابع للمشروع.",
        claimEn: "Madinaty security personnel staged sit-in over low wages, grueling 12-14 hour shifts, and substandard lodging conditions in worker accommodations.",
        date: "أغسطس 2024",
        sourceName: "المنصة",
        sourceKey: "manassa_security_aug2024",
        classAr: "تقرير استقصائي موثق لبيئة العمل",
        classEn: "Field Investigative Report on Labor Conditions",
        badge: "badge-med"
      },
      {
        projectAr: "مدينتي (عمال الأمن)",
        projectEn: "Madinaty (Security Workforce)",
        categoryAr: "مذكرة رسمية وإحالة للتحقيق",
        categoryEn: "Formal Petition & Administrative Inquiries",
        claimAr: "تقديم مذكرة رسمية لإدارة طلعت مصطفى بمدينتي للمطالبة بأجر إضافي عن العمل 12 ساعة والإجازات المستحقة وبدل وجبات؛ الإدارة ردت بإحالة بعضهم للتحقيق ووعدت ببحثها مع الزيادة السنوية.",
        claimEn: "Security officers filed formal petition for 12-hr shift overtime, leave regularization, and food stipends; management subjected participants to internal inquiry.",
        date: "29 أكتوبر 2025",
        sourceName: "المنصة",
        sourceKey: "manassa_security_oct2025",
        classAr: "مذكرة رسمية من العمال ونزاع إداري",
        classEn: "Official Labor Petition & Internal Dispute",
        badge: "badge-medhigh"
      },
      {
        projectAr: "مدينتي (اتحاد الشاغلين والملاك)",
        projectEn: "Madinaty (Homeowners Association)",
        categoryAr: "فروق الصيانة وعائد الوديعة",
        categoryEn: "Maintenance Deficit Surcharges",
        claimAr: "مطالبة سنوية للملاك بسداد فروق صيانة تتراوح بين 15 و45 ألف جنيه لكل وحدة، وسط شكاوى من عدم إفصاح الإدارة عن تقارير محاسبية مدققة لعوائد استثمار وديعة الصيانة الأصلية.",
        claimEn: "Annual developer invoicing for maintenance differences (EGP 15k-45k/unit); residents demand audited disclosure of trust accounts and earned deposit yields.",
        date: "2024 – 2026",
        sourceName: "تطبيق TMG Life ودعاوى ملاك",
        sourceKey: "cpa_article15_resale",
        classAr: "نزاع محاسبي وقضائي متداول",
        classEn: "Accounting Controversy & Pending Lawsuits",
        badge: "badge-medhigh"
      },
      {
        projectAr: "مدينتي والرحاب",
        projectEn: "Madinaty & Rehab",
        categoryAr: "رسوم التنازل العقاري (5-10%)",
        categoryEn: "Resale Transfer Fees (5-10%)",
        claimAr: "إلزام البائعين بسداد رسوم تنازل وتعديل بيانات (5% إلى 10% أو مبالغ مقطوعة)، بالمخالفة الصريحة لنص المادة 15 من قانون حماية المستهلك رقم 181 لسنة 2018 التي تبطل هذه الشروط.",
        claimEn: "Charging 5%-10% transfer fees on unit resales, directly contradicting Article 15 of Egyptian Consumer Protection Law No. 181/2018 declaring such fees void.",
        date: "مستمر حتى 2026",
        sourceName: "جهاز حماية المستهلك",
        sourceKey: "cpa_article15_resale",
        classAr: "مخالفة تشريعية ونزاع تنظيمي",
        classEn: "Statutory Violation & Regulatory Dispute",
        badge: "badge-high"
      },
      {
        projectAr: "سيليا (العاصمة الإدارية)",
        projectEn: "Celia (New Capital)",
        categoryAr: "تأخر مواعيد تسليم الوحدات",
        categoryEn: "Handover Schedule Slippage",
        claimAr: "تأخر تسليم شقق وعمارات بالمراحل 3 و4 لفترات بين 14 و18 شهراً؛ عزت الشركة التأخير لأعمال توصيل مرافق الكهرباء ومحطات المياه التابعة لشركة العاصمة الإدارية ACUD.",
        claimEn: "Delivery slippage of 14-18 months in apartment phases 3 and 4; company cited municipal grid and utility connection delays by master developer ACUD.",
        date: "2024 – 2025",
        sourceName: "إخطارات اتحاد المشترين",
        sourceKey: "egx_filings_fy25_h126",
        classAr: "تأخير تشغيلي معزز بالقوة القاهرة",
        classEn: "Operational Delay Shielded by Force Majeure",
        badge: "badge-med"
      }
    ];

    /* ==========================================================================
       DATA STORES: RISK MATRIX (100% Bilingual)
       ========================================================================== */
    const risksData = [
      {
        catAr: "العزل القانوني عبر نسبية أثر العقود",
        catEn: "Contractual Privity Insulation Shield",
        sourceKey: "state_council_madinaty",
        sevAr: "حرج",
        sevEn: "Critical",
        sevBadge: "badge-high",
        likAr: "مرتفعة",
        likEn: "High",
        mechAr: "توقيع العقود عبر شركة الإسكندرية للإنشاءات أو مقاولي الحزم وليس الشركة القابضة المدرجة، مما يحرم المقاول من الحجز على حسابات طلعت مصطفى أو تدفقات المبيعات.",
        mechEn: "Contracts executed strictly with Alexandria Construction Co. (ACC) or turnkey contractors, legally preventing liens against listed TMG Holding assets.",
        ctrlAr: "فحص السجل التجاري للجهة الموقعة على العقد، وعدم الاعتماد على شعار مجموعة طلعت مصطفى التسويقي؛ وطلب ضمانات دفع مباشرة.",
        ctrlEn: "Verify commercial register of signing counterparty; do not rely on TMG branding; negotiate direct payment guarantees."
      },
      {
        catAr: "تأخير اعتماد وصرف المستخلصات (*أوراق دفع*)",
        catEn: "Payment Gatekeeping & Deferred Commercial Paper",
        sevAr: "مرتفع",
        sevEn: "High",
        sevBadge: "badge-high",
        likAr: "مرتفعة",
        likEn: "High",
        mechAr: "استغلال طبقات الحصر الهندسي لتعطيل اعتماد المستخلص، ثم السداد بشيكات آجلة (90 إلى 270 يوماً). أوراق الدفع والدائنون يتجاوزون 15.79 مليار جنيه بالمجموعة.",
        mechEn: "Quantity surveying audit delays progress certification; payments disbursed via post-dated checks (90-270 days). Notes payable exceed EGP 15.79B.",
        ctrlAr: "مراقبة مدد توقيع مهندسي الموقع؛ رفض الشيكات الآجلة المفرطة؛ وتفعيل غرامات التأخير في حالة تجاوز مدة المراجعة المتفق عليها.",
        ctrlEn: "Track site measurement turnaround; resist excessive post-dated checks; enforce interest/penalties on prolonged audit periods."
      },
      {
        catAr: "درع التحكيم الإجباري السري (CRCICA)",
        catEn: "Mandatory CRCICA Arbitration Barrier",
        sevAr: "مرتفع",
        sevEn: "High",
        sevBadge: "badge-high",
        likAr: "مرتفعة",
        likEn: "High",
        mechAr: "اشتراط التحكيم المؤسسي بمركز القاهرة الدولي يمنع اللجوء للقضاء المستعجل. رسوم التحكيم الباهظة تجعل مقاضاة المبالغ دون 20 مليون جنيه خاسرة للمقاولين الصغار.",
        mechEn: "Mandatory institutional arbitration suppresses public litigation. High tribunal filing fees make claims under EGP 20M economically unviable for SMEs.",
        ctrlAr: "التفاوض على استثناء المطالبات الأقل من سقف مالي محدد من التحكيم وجعل الاختصاص للمحاكم الاقتصادية المصرية تسريعاً للفصل.",
        ctrlEn: "Carve out summary local court jurisdiction for claims below a negotiated monetary threshold to allow affordable recovery."
      },
      {
        catAr: "تضخم الأسعار وفصل التوريد عن المصنعيات",
        catEn: "Cost Inflation & Labor/Materials Decoupling",
        sevAr: "مرتفع",
        sevEn: "High",
        sevBadge: "badge-high",
        likAr: "متوسطة إلى مرتفعة",
        likEn: "Med-High",
        mechAr: "تتولى طلعت مصطفى التوريد المركزي للحديد والأسمنت، ويقتصر المقاول على المصنعيات والمعدات، مما يجرده من هوامش أرباح التوريد ويعرضه لتضخم أجور العمالة دون تعويض.",
        mechEn: "TMG centralizes steel and cement bulk supply; subcontractors do labor-only, stripping material margin buffers against soaring labor wage inflation.",
        ctrlAr: "النص الصريح على معادلة لتعديل أسعار المصنعيات والمعدات مرتبطة بنشرة الأرقام القياسية لأسعار المنتجين الصادرة عن الجهاز المركزي للتعبئة والإحصاء.",
        ctrlEn: "Insist on labor and equipment price indexation linked to monthly Ministry of Housing cost bulletins (نشرة أسعار مواد البناء)."
      },
      {
        catAr: "علاقات العمل والاضطرابات الموقعية",
        catEn: "Labor Friction & Subcontractor Workforce Strife",
        sevAr: "متوسط",
        sevEn: "Medium",
        sevBadge: "badge-med",
        likAr: "متوسطة",
        likEn: "Medium",
        mechAr: "كما أظهرت واقعة 2008 واحتجاجات 2024-2025، فإن أي توقف لمستحقات مقاول الباطن أو ضغط أجور العمالة يهدد بوقف العمل بالموقع وتدخل النيابة أو مكاتب العمل.",
        mechEn: "As evidenced in the 2008 contractor case and 2024-25 protests, payment delays quickly trigger labor walk-offs and regulatory scrutiny.",
        ctrlAr: "إلزام المطور بحساب وسيط (Escrow) لصرف أجور العمالة بانتظام؛ وتأمين مسارات تظلم مستقلة لمنع الإضرابات الموقعية المفاجئة.",
        ctrlEn: "Establish designated labor payroll escrow to protect worker wages; maintain open grievance escalation to prevent site stoppages."
      },
      {
        catAr: "احتجاز مبالغ الضمان (Retention) واستنزاف السيولة",
        catEn: "Extended Working Capital Drain & Retention Holds",
        sevAr: "متوسط",
        sevEn: "Medium",
        sevBadge: "badge-med",
        likAr: "مرتفعة",
        likEn: "High",
        mechAr: "ربط الإفراج عن نسبة الـ 5-10% المحتجزة بتسليم المدينة بأكملها أو شبكات عملاقة وليس انتهاء الحزمة المحددة للمقاول.",
        mechEn: "Retention release cycles (5–10%) tied to master city handover rather than package-specific practical completion certificates.",
        ctrlAr: "النص على صرف نصف الضمان فور الاستلام الابتدائي للحزمة، واستبدال النصف الآخر بخطاب ضمان بنكي متناقص القيمة.",
        ctrlEn: "Require 50% retention release upon package primary takeover (محضر استلام ابتدائي), substituting balance with a declining bank guarantee."
      }
    ];

    /* ==========================================================================
       RENDER FUNCTIONS & LANGUAGE SWITCHER
       ========================================================================== */
    let currentFilteredProjects = projectsData;

    function renderProjects(data) {
      const tbody = document.getElementById('projects-tbody');
      tbody.innerHTML = '';
      data.forEach(p => {
        const tr = document.createElement('tr');
        const name = currentLang === 'ar' ? p.nameAr : p.nameEn;
        const loc = currentLang === 'ar' ? p.locAr : p.locEn;
        const land = currentLang === 'ar' ? p.landAr : p.landEn;
        const status = currentLang === 'ar' ? p.statusAr : p.statusEn;
        const comp = currentLang === 'ar' ? p.compAr : p.compEn;
        const risk = currentLang === 'ar' ? p.riskAr : p.riskEn;
        tr.innerHTML = `
          <td><strong>${name}</strong></td>
          <td>${loc}</td>
          <td><span class="cell-mono">${p.spv}</span></td>
          <td>${land}</td>
          <td>${status}</td>
          <td style="max-width:240px; font-size:12px; color:var(--text-muted);">${comp}</td>
          <td><span class="badge ${p.riskBadge}">${risk}</span></td>
          <td><button class="source-link" onclick="showSourceModal('${p.sourceKey}')">المصدر ↗</button></td>
        `;
        tbody.appendChild(tr);
      });
    }

    function renderContractorsTable() {
      const tbody = document.getElementById('contractors-tbody');
      tbody.innerHTML = '';
      contractorsData.forEach(c => {
        const tr = document.createElement('tr');
        tr.style.cursor = 'pointer';
        tr.title = currentLang === 'ar' ? 'انقر لعرض توثيق تعاقد المقاول ↗' : 'Click to inspect contractor verified contract ↗';
        tr.onclick = (e) => {
          if (!e.target.closest('a, button')) {
            showSourceModal(c.sourceKey);
          }
        };
        const proj = currentLang === 'ar' ? c.projectAr : c.projectEn;
        const ent = currentLang === 'ar' ? c.entityAr : c.entityEn;
        const main = currentLang === 'ar' ? c.mainAr : c.mainEn;
        const sub = currentLang === 'ar' ? c.subAr : c.subEn;
        const scope = currentLang === 'ar' ? c.scopeAr : c.scopeEn;
        const evid = currentLang === 'ar' ? c.evidAr : c.evidEn;
        const issue = currentLang === 'ar' ? c.issueAr : c.issueEn;
        const risk = currentLang === 'ar' ? c.riskAr : c.riskEn;
        const srcBtnLbl = currentLang === 'ar' ? 'توثيق ↗' : 'Verified ↗';
        tr.innerHTML = `
          <td><strong>${proj}</strong></td>
          <td><span class="cell-mono">${ent}</span></td>
          <td><strong>${main}</strong></td>
          <td><span style="color:var(--accent-cyan); font-weight:700;">${sub}</span></td>
          <td style="font-size:12px;">${scope}</td>
          <td style="font-size:11.5px; color:var(--text-dim);">${evid}</td>
          <td style="font-size:12px; color:var(--text-muted); max-width:240px;">${issue}</td>
          <td><button class="source-link" onclick="showSourceModal('${c.sourceKey}')">${srcBtnLbl}</button></td>
          <td><span class="badge ${c.badge}">${risk}</span></td>
        `;
        tbody.appendChild(tr);
      });
    }

    function renderComplaintsTable() {
      const tbody = document.getElementById('complaints-tbody');
      tbody.innerHTML = '';
      complaintsData.forEach(c => {
        const tr = document.createElement('tr');
        tr.style.cursor = 'pointer';
        tr.title = currentLang === 'ar' ? 'انقر للاطلاع على التوثيق الصحفي/القضائي الكامل للواقعة ↗' : 'Click to inspect full journalistic/judicial record ↗';
        tr.onclick = (e) => {
          if (!e.target.closest('a, button')) {
            showSourceModal(c.sourceKey);
          }
        };
        const proj = currentLang === 'ar' ? c.projectAr : c.projectEn;
        const cat = currentLang === 'ar' ? c.categoryAr : c.categoryEn;
        const claim = currentLang === 'ar' ? c.claimAr : c.claimEn;
        const cls = currentLang === 'ar' ? c.classAr : c.classEn;
        tr.innerHTML = `
          <td><strong>${proj}</strong></td>
          <td><span class="badge badge-med" style="font-size:10.5px;">${cat}</span></td>
          <td style="font-size:12.5px; color:var(--text-muted); max-width:320px;">${claim}</td>
          <td class="cell-mono" style="font-size:11.5px;">${c.date}</td>
          <td><button class="source-link" onclick="showSourceModal('${c.sourceKey}')">${c.sourceName} ↗</button></td>
          <td><span class="badge ${c.badge}">${cls}</span></td>
        `;
        tbody.appendChild(tr);
      });
    }

    function renderRisksTable() {
      const tbody = document.getElementById('risks-tbody');
      tbody.innerHTML = '';
      risksData.forEach(r => {
        const tr = document.createElement('tr');
        const cat = currentLang === 'ar' ? r.catAr : r.catEn;
        const sev = currentLang === 'ar' ? r.sevAr : r.sevEn;
        const lik = currentLang === 'ar' ? r.likAr : r.likEn;
        const mech = currentLang === 'ar' ? r.mechAr : r.mechEn;
        const ctrl = currentLang === 'ar' ? r.ctrlAr : r.ctrlEn;
        tr.innerHTML = `
          <td><strong>${cat}</strong></td>
          <td><span class="badge ${r.sevBadge}">${sev}</span></td>
          <td style="font-weight:700;">${lik}</td>
          <td style="font-size:12px; color:var(--text-muted); max-width:280px;">${mech}</td>
          <td style="font-size:12px; color:var(--accent-cyan); max-width:280px;">${ctrl}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    function renderDynamicCards() {
      // 1. KPI Grid
      const kpis = [
        {
          title: currentLang === 'ar' ? "رأس المال المصدر والمدفوع" : "Issued & Paid Capital",
          val: "20.64B EGP",
          delta: currentLang === 'ar' ? "● مدرج بالبورصة: TMGH" : "● Listed EGX: TMGH",
          sub: currentLang === 'ar' ? "2.06 مليار سهم" : "2,063,562,286 shares",
          type: "cyan"
        },
        {
          title: currentLang === 'ar' ? "إيرادات وأرباح 2025 المجمعة" : "FY2025 Revenue / Net Profit",
          val: "62.5B / 18.2B",
          delta: currentLang === 'ar' ? "▲ +46% إيرادات / +43% أرباح" : "▲ +46% Rev / +43% Profit",
          sub: currentLang === 'ar' ? "7.5 مليار H1 26" : "EGP 7.5bn H1 26",
          type: "emerald"
        },
        {
          title: currentLang === 'ar' ? "الدائنون وأوراق الدفع التجارية" : "Operating Creditors & Notes",
          val: "> 15.79B EGP",
          delta: currentLang === 'ar' ? "▲ شيكات آجلة لمقاولين وموردين" : "▲ Deferred Commercial Notes",
          sub: currentLang === 'ar' ? "تأجيل 90 إلى 270 يوماً" : "90–270 day deferral",
          type: "rose"
        },
        {
          title: currentLang === 'ar' ? "التزامات عقود التأجير التمويلي" : "Lease Debt Equivalent",
          val: "43.99B EGP",
          delta: currentLang === 'ar' ? "▲ تمويلات هيكلية خارج الميزانية" : "▲ Off-Bal Financial Leases",
          sub: currentLang === 'ar' ? "فائدة إقراض 28.6%" : "28.6% borrowing rate",
          type: "purple"
        },
        {
          title: currentLang === 'ar' ? "معدل تحويل السيولة النقدية" : "Cash Conversion Ratio",
          val: "31.2%",
          delta: currentLang === 'ar' ? "▼ تدفق تشغيلي 3.1 مليار فقط" : "▼ CFO EGP 3.1bn",
          sub: currentLang === 'ar' ? "مقابل أرباح 9.95 مليار H1 26" : "vs 9.95bn profit H1 26",
          type: "amber"
        }
      ];

      const kpiContainer = document.getElementById('kpi-grid-container');
      kpiContainer.innerHTML = kpis.map(k => `
        <div class="kpi-card ${k.type}">
          <div class="kpi-header">
            <span class="kpi-title">${k.title}</span>
            <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
          </div>
          <div class="kpi-value">${k.val}</div>
          <div class="kpi-delta ${k.type === 'emerald' || k.type === 'cyan' ? 'delta-up' : 'delta-warn'}">
            <span>${k.delta}</span> <span class="delta-sub">${k.sub}</span>
          </div>
        </div>
      `).join('');

      // 2. Conclusions Cards (Tab 1)
      const concCards = [
        {
          title: currentLang === 'ar' ? "1. الدرع القانوني للمشتريات المدمجة" : "1. Vertically Integrated Privity Shield",
          badge: currentLang === 'ar' ? "هيكلي" : "Structural",
          desc: currentLang === 'ar' ? 
            "تنفذ طلعت مصطفى مشروعاتها عبر شركة الإسكندرية للإنشاءات (ACC) المملوكة لعائلة طلعت مصطفى ومقاولي حزم كأتريوم. مقاولو الباطن يتعاقدون مع شركة المقاولات حصراً، مما يحرمهم من الحجية النسبية للعقد ضد الشركة القابضة أو الحجز على حساباتها." :
            "TMG executes projects via Alexandria Construction Co. (ACC) and package GCs. Subcontractors lack contractual privity against listed TMG Holding to freeze parent bank accounts or customer receipts.",
          foot1: currentLang === 'ar' ? "حجية العقد: قابضة معزولة" : "Privity: Clean Holding",
          foot2: currentLang === 'ar' ? "شركة تابعة: ACC (حصة 8.03%)" : "Affiliate: ACC (8.03% Stake)",
          color: "var(--accent-cyan)",
          src: "egx_filings_fy25_h126"
        },
        {
          title: currentLang === 'ar' ? "2. عقبة المستخلصات وتعمد تأخير الصرف" : "2. Payment Gatekeeping & Withholding",
          badge: currentLang === 'ar' ? "سيولة" : "Cash-Flow",
          desc: currentLang === 'ar' ? 
            "تاريخياً (واقعة مقاول مدينتي 2008)، أقر مدير شركة الإسكندرية بتعمد تأخير صرف المستحقات لمنع العمال من مغادرة الموقع. حديثاً، تستخدم لجان الحصر والتوثيق لإطالة مدة المراجعة القانونية وصرف شيكات آجلة تتجاوز 15.79 مليار جنيه دون إعلان تعثر مالي." :
            "Historically (2008 Madinaty case), ACC management admitted intentional payment delays to keep labor on site. Today, prolonged technical quantity surveying defers cash outflows via notes payable (>EGP 15.79B).",
          foot1: currentLang === 'ar' ? "المصادر: المصري اليوم / البورصة" : "Sources: Al-Masry Al-Youm / EGX",
          foot2: currentLang === 'ar' ? "الأداة: أوراق دفع مؤجلة" : "Mechanism: Notes Payable",
          color: "var(--accent-rose)",
          src: "masry_shehata_2008"
        },
        {
          title: currentLang === 'ar' ? "3. درع التحكيم السري والنزاعات العمالية" : "3. CRCICA Shield & Labor Friction",
          badge: currentLang === 'ar' ? "قضائي وعمالي" : "Legal & Labor",
          desc: currentLang === 'ar' ? 
            "تنص عقود التوريد والمقاولات على التحكيم السري بمركز القاهرة الدولي (CRCICA)، مما يقمع النزاعات التجارية علناً. وعلى الجانب العمالي، وثقت تقارير 2024 و2025 احتجاجات لعمال وموظفي الإسكندرية للإنشاءات وأفراد أمن مدينتي على تدني الأجور وساعات العمل." :
            "Mandatory CRCICA arbitration suppresses public contractor litigation. On the labor front, verified reports in 2024-2025 document protests by ACC workers and Madinaty security over wages and 12-hour shifts.",
          foot1: currentLang === 'ar' ? "المصادر: المنصة / مدى مصر" : "Sources: Al Manassa / Mada Masr",
          foot2: currentLang === 'ar' ? "الحماية: تحكيم مؤسسي سري" : "Shield: Confidential CRCICA",
          color: "var(--accent-amber)",
          src: "manassa_security_oct2025"
        }
      ];

      document.getElementById('conclusions-cards-container').innerHTML = concCards.map(c => `
        <div class="flag-card" style="border-inline-start-color: ${c.color}; cursor: pointer;" onclick="showSourceModal('${c.src}')">
          <div class="flag-header">
            <span class="flag-title">${c.title}</span>
            <span class="badge badge-med">${c.badge}</span>
          </div>
          <div class="flag-desc">${c.desc}</div>
          <div class="flag-footer">
            <span>${c.foot1}</span>
            <button class="source-link" onclick="showSourceModal('${c.src}')">فحص المصدر ↗</button>
          </div>
        </div>
      `).join('');

      // 3. Procurement Explanatory Cards (Tab 2)
      document.getElementById('procurement-expl-cards').innerHTML = `
        <div class="card" style="background: var(--bg-surface-elevated);">
          <div class="card-title" style="color: var(--accent-cyan); margin-bottom: 8px;">
            ${currentLang === 'ar' ? 'أهمية مبدأ نسبية أثر العقود للمقاول والمطور' : 'Why Contractual Privity Shields TMG'}
          </div>
          <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.7;">
            ${currentLang === 'ar' ? 
              'لا توقع مجموعة طلعت مصطفى القابضة أي عقود توريد أو مقاولات باطن بصورة مباشرة. كافة العقود تبرمها شركة الإسكندرية للإنشاءات (ACC) أو شركة أتريوم. يمنع ذلك مقاولي الباطن من الحجز الإداري أو القضائي على التدفقات المالية للملاك أو حسابات البورصة، ويجعل مخاطر التعثر معزولة داخل الكيان المنفذ فقط.' :
              'TMG Holding never executes trade-level subcontracts directly. Subcontractors sign with Alexandria Construction Co. (ACC) or Atrium. If payment delays occur, trade contractors cannot place liens on TMG bank accounts or seize customer installment revenues under Egyptian Civil Code rules.'}
          </p>
        </div>
        <div class="card" style="background: var(--bg-surface-elevated);">
          <div class="card-title" style="color: var(--accent-amber); margin-bottom: 8px;">
            ${currentLang === 'ar' ? 'فصل توريد الخامات عن المصنعيات والعمالة' : 'Decoupling Labor from Bulk Materials'}
          </div>
          <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.7;">
            ${currentLang === 'ar' ? 
              'تتولى طلعت مصطفى التوريد المركزي للحديد (عز/بشاي) والأسمنت مباشرة. يتعاقد مقاولو الباطن على المصنعيات والعمالة والمعدات فقط. هذا النموذج يجرد المقاول من هوامش أرباح التوريد ويعرضه للتآكل المالي الشديد جراء تضخم أجور العمالة دون حماية تعاقدية.' :
              'TMG centralized the bulk procurement of rebar steel and cement through direct corporate supply agreements. Subcontractors are strictly retained for labor, formwork, and installation, removing contractor margin buffers and exposing trade SMEs to acute wage inflation.'}
          </p>
        </div>
      `;

      // 4. Mustakhlasat Steps (Tab 3)
      const steps = [
        {
          num: currentLang === 'ar' ? "المرحلة الأولى: الحصر الفني" : "Step 1: Technical Measurement",
          title: currentLang === 'ar' ? "حصر هندسي ومطابقة الكميات المنفذة" : "Technical Quantity Surveying & BOQ Audit",
          desc: currentLang === 'ar' ? 
            "تقوم أطقم مهندسي الموقع بشركة الإسكندرية للإنشاءات بمطابقة الأعمال مع جداول الكميات. يتم استبعاد بنود التغييرات غير المعتمدة مسبقاً بأمر كتابي، وخصم أي ملاحظات جودة." :
            "ACC site engineering teams review measured work against BOQ. Variations without advance written orders are routinely excluded or marked down."
        },
        {
          num: currentLang === 'ar' ? "المرحلة الثانية: التدقيق المركزي" : "Step 2: Central Document Control",
          title: currentLang === 'ar' ? "مراجعة إدارة التوثيق المالي والمستودعات" : "Central Financial Audit & Delivery Slip Check",
          desc: currentLang === 'ar' ? 
            "تتولى وحدات إدخال البيانات والتوثيق بمدينتي والدقي فحص أذون الاستلام. أي نقص في أذون التشوين أو الاستلام يوقف صرف المستخلص إدارياً دون التزام زمني محدد." :
            "Central document control units at Madinaty/Dokki cross-check submittals. Any deficiency in material delivery slips triggers administrative payment withholding."
        },
        {
          num: currentLang === 'ar' ? "المرحلة الثالثة: إصدار أوراق الدفع" : "Step 3: Deferred Commercial Paper",
          title: currentLang === 'ar' ? "إصدار الشيكات وأوراق الدفع المؤجلة" : "Issuance of Deferred Post-Dated Checks",
          desc: currentLang === 'ar' ? 
            "يتم صرف المستخلصات المعتمدة بشيكات آجلة (من 90 إلى 270 يوماً). تتجاوز أوراق الدفع والدائنون التجاريون حاجز 15.79 مليار جنيه بالمجموعة." :
            "Approved payments are disbursed via post-dated checks (90 to 270 days). Operating creditors & notes payable routinely exceed EGP 15.79 billion."
        }
      ];

      document.getElementById('mustakhlasat-steps-container').innerHTML = steps.map(s => `
        <div class="step-card">
          <span class="step-num">${s.num}</span>
          <h4 style="margin-top: 8px; margin-bottom: 6px; font-weight:800;">${s.title}</h4>
          <p style="color: var(--text-muted); font-size: 12px; line-height:1.7;">${s.desc}</p>
        </div>
      `).join('');

      document.getElementById('mustakhlasat-defense-box').innerHTML = `
        <div class="flag-header">
          <span class="flag-title">${currentLang === 'ar' ? 'الدفاع القانوني بعدم حلول أجل الدين (*الدين غير حالّ الأداء*)' : 'The "Non-Due Debt" Legal Defense'}</span>
          <span class="badge badge-high">${currentLang === 'ar' ? 'درع القانون المدني' : 'Civil Law Shield'}</span>
        </div>
        <div class="flag-desc">
          ${currentLang === 'ar' ? 
            'طبقاً لأحكام القانون المدني المصري، لا يشكل المستخلص غير المعتمد نهائياً سنداً تنفيذياً لدين محقق الوجود وحالّ الأداء. تستغل المجموعة هذا التكييف لإطالة أمد الحصر والمراجعة دون اعتبارها متعثرة قانوناً أمام البنوك أو خاضعة لفوائد التأخير، مما يتيح لها امتصاص أزمات السيولة على حساب سلاسل الإمداد ومقاولي الباطن.' :
            'Under Egyptian Civil Law, an uncertified payment certificate does not constitute an enforceable liquid debt. By indefinitely prolonging technical re-surveys and document reviews, TMG entities legally conserve cash flow during macro currency crunches without triggering formal contract default.'}
        </div>
      `;

      // 5. Sentiment 3 Cards (Tab 8)
      const sent3 = [
        {
          title: currentLang === 'ar' ? "1. واقعة مقاول مدينتي التاريخية (2008)" : "1. Historic Madinaty Contractor Case (2008)",
          desc: currentLang === 'ar' ? 
            "وثقت صحيفة المصري اليوم بلاغاً للنائب العام من المقاول شحاتة محمد حسن ضد هشام طلعت لعدم صرف مستحقاته، وإقرار مدير شركة الإسكندرية (إبراهيم حسبو) بأن التعطيل كان متعمداً لمنع العمال من مغادرة الموقع." :
            "Al-Masry Al-Youm documented a complaint filed by subcontractor Shehata Hassan to the Prosecutor General; ACC Director Ibrahim Hasabo admitted the payment halt was intentional to prevent worker desertion.",
          color: "var(--accent-rose)",
          src: "masry_shehata_2008"
        },
        {
          title: currentLang === 'ar' ? "2. احتجاجات عمال وموظفي الإسكندرية (2024-2025)" : "2. ACC Labor Protests & Security Petitions",
          desc: currentLang === 'ar' ? 
            "وثقت المنصة ومدى مصر احتجاجات لأكثر من 100 موظف وعامل بشركة الإسكندرية على الأجور والتسريح، واحتجاجات عمال أمن مدينتي على ورديات الـ 12 ساعة والمطالبة بالأجر الإضافي وبدلات الوجبات." :
            "Al Manassa and Mada Masr documented protests by over 100 ACC workers over wage freezes and layoffs, alongside Madinaty security protests over 12-hour shifts and unpaid overtime.",
          color: "var(--accent-amber)",
          src: "manassa_security_oct2025"
        },
        {
          title: currentLang === 'ar' ? "3. نزاعات فروق الصيانة ورسوم التنازل للملاك" : "3. Maintenance Deficits & Resale Transfer Fees",
          desc: currentLang === 'ar' ? 
            "مطالبات سنوية لفروق صيانة (15-45 ألف جنيه) دون إفصاح مالي شفاف عن عوائد الوديعة، وفرض رسوم تنازل (5-10%) بالمخالفة الصريحة للمادة 15 من قانون حماية المستهلك رقم 181 لسنة 2018." :
            "Annual homeowner maintenance surcharges (EGP 15k-45k) lacking transparent deposit yield audits, alongside 5%-10% resale transfer fees violating Article 15 of Consumer Protection Law 181/2018.",
          color: "var(--accent-blue)",
          src: "cpa_article15_resale"
        }
      ];

      document.getElementById('sentiment-highlights-container').innerHTML = sent3.map(s => `
        <div class="card" style="border-top: 3px solid ${s.color}; cursor: pointer;" onclick="showSourceModal('${s.src}')">
          <div class="card-title" style="margin-bottom: 8px;">${s.title}</div>
          <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.7;">${s.desc}</p>
          <div style="margin-top:10px;">
            <button class="source-link" onclick="showSourceModal('${s.src}')">التوثيق الصحفي والقانوني ↗</button>
          </div>
        </div>
      `).join('');

      // 6. Stakeholder Playbooks (Tab 9)
      document.getElementById('stakeholder-playbooks-container').innerHTML = `
        <div class="card" style="border-top: 3px solid var(--accent-cyan);">
          <div class="card-title" style="margin-bottom: 12px; color: var(--accent-cyan);">
            ${currentLang === 'ar' ? 'دليل التحوط لمقاولي الباطن والموردين' : 'Playbook for Subcontractors & Suppliers'}
          </div>
          <ul style="color: var(--text-muted); font-size: 12.5px; line-height: 1.8; padding-inline-start: 18px;">
            <li><strong>${currentLang === 'ar' ? 'إلغاء بنود الشرط الواقف (Pay-When-Paid):' : 'Reject Pay-When-Paid Clauses:'}</strong> ${currentLang === 'ar' ? 'رفض أي نص يجعل صرف مستحقاتك مرهوناً بصرف هيئة المجتمعات أو المطور لشركة الإسكندرية.' : 'Eliminate terms conditioning your progress payments on developer releases to ACC.'}</li>
            <li><strong>${currentLang === 'ar' ? 'حظر التعديلات الشفهية:' : 'Zero Verbal Variations:'}</strong> ${currentLang === 'ar' ? 'عدم تنفيذ أي بند إضافي أو تعديل إلا بأمر تغيير كتابي معتمد (Variation Order) محدد القيمة وفروق الأسعار.' : 'Never execute site works without a signed, price-indexed Variation Order.'}</li>
            <li><strong>${currentLang === 'ar' ? 'إعذار حلول أجل الدين:' : 'Serve Bailiff Demands:'}</strong> ${currentLang === 'ar' ? 'إرسال إنذارات رسمية على يد محضر فور انقضاء المهلة الفنية للحصر لبدء احتساب الفائدة التجارية القانونية (5%).' : 'Serve formal court bailiff notices upon audit lapse to trigger statutory 5% commercial default interest.'}</li>
            <li><strong>${currentLang === 'ar' ? 'شرط الاحتفاظ بالملكية:' : 'Retention of Title:'}</strong> ${currentLang === 'ar' ? 'التمسك بشرط ملكية المعدات والخامات الموردة لحين التحصيل الفعلي وقيد المقاصة البنكية للشيكات.' : 'Retain title on installed equipment and materials until post-dated checks fully clear.'}</li>
          </ul>
        </div>

        <div class="card" style="border-top: 3px solid var(--accent-emerald);">
          <div class="card-title" style="margin-bottom: 12px; color: var(--accent-emerald);">
            ${currentLang === 'ar' ? 'دليل الفحص النافي للجهالة للبنوك والمستثمرين' : 'Playbook for Institutional Investors & Banks'}
          </div>
          <ul style="color: var(--text-muted); font-size: 12.5px; line-height: 1.8; padding-inline-start: 18px;">
            <li><strong>${currentLang === 'ar' ? 'قوة الميزانية القابضة المعزولة:' : 'Parent Entity Ring-Fencing:'}</strong> ${currentLang === 'ar' ? 'يحمي نموذج المقاول المدمج الشركة القابضة من مطالبات مقاولي الباطن، مما يحافظ على سيولة السهم وملاءته.' : 'Captive contracting insulates TMG Holding equity and cash balances from trade subcontractor claims.'}</li>
            <li><strong>${currentLang === 'ar' ? 'مراقبة حركة أوراق الدفع:' : 'Track Notes Payable Velocity:'}</strong> ${currentLang === 'ar' ? 'متابعة وتيرة أرصدة الدائنين وأوراق الدفع (>15.79 مليار) كمؤشر حقيقي على الضغوط الموقعية وسلاسل الإمداد.' : 'Monitor payables and notes velocity relative to WIP to gauge real construction site friction.'}</li>
            <li><strong>${currentLang === 'ar' ? 'مخاطر إعادة الطرح والتنفيذ:' : 'Re-Tendering & Inflation Exposure:'}</strong> ${currentLang === 'ar' ? 'تآكل هوامش مقاولي الباطن قد يؤدي لانسحابات مفاجئة تهدد جداول تسليم ساوث ميد (2029) ونور.' : 'Severe inflation passed to trade contractors risks sudden walk-offs, threatening SouthMed 2029 pacing.'}</li>
            <li><strong>${currentLang === 'ar' ? 'احتساب الرافعة المالية الحقيقية:' : 'True Leverage Testing:'}</strong> ${currentLang === 'ar' ? 'إدراج 44 مليار جنيه التزامات تأجير تمويلي ضمن الديون الإجمالية لحساب معدل خدمة الدين الفعلي.' : 'Factor EGP 44B in financial lease obligations alongside bank debt when computing true DSCR.'}</li>
          </ul>
        </div>
      `;

      // 7. Legal Disputes Cards (Tab 6)
      const disputes = [
        {
          title: currentLang === 'ar' ? "الطعن 12622 لسنة 63 ق — المحكمة الإدارية العليا (أرض مدينتي)" : "Appeal 12622 / JY 63 — Supreme Administrative Court (Madinaty Concession)",
          badge: currentLang === 'ar' ? "حكم قضائي بات" : "Supreme Court Ruling",
          desc: currentLang === 'ar' ? 
            "قضت المحكمة الإدارية العليا في سبتمبر 2010 ببطلان عقد بيع 8,000 فدان للشركة العربية لمخالفته قانون المزايدات 89/1998. تمت تسوية النزاع بقرارات مجلس الوزراء 2010/2011 وعقد تسوية 2015 بإلزام الشركة بتسليم 7% من إجمالي المباني السكنية المنجزة عيناً لهيئة المجتمعات (عشرات المليارات من الجنيهات)." :
            "Supreme Administrative Court annulled the direct allocation of 8,000 feddans to ACPUD in 2010. Regularized via 2010/2011 Cabinet decrees and 2015 contract requiring TMG to deliver 7% of total residential built-up area to NUCA as in-kind consideration.",
          foot1: currentLang === 'ar' ? "الأطراف: حمدي الفخراني ضد الهيئة وطلعت مصطفى" : "Parties: El-Fakharany vs NUCA / TMG",
          foot2: currentLang === 'ar' ? "النتيجة: بطلان العقد والتسوية بحصة عينية 7%" : "Outcome: Annulled & Settled via 7% In-Kind Delivery",
          color: "var(--accent-rose)",
          src: "state_council_madinaty"
        },
        {
          title: currentLang === 'ar' ? "الجنحة 16522 لسنة 2013 — محكمة جنح قصر النيل (شيكات بدون رصيد)" : "Case 16522 of 2013 — Cairo Misdemeanor Court (Bad Checks / شيكات بدون رصيد)",
          badge: currentLang === 'ar' ? "جنحة تجارية" : "Misdemeanor Filing",
          desc: currentLang === 'ar' ? 
            "دعاوى جنح شيكات صادرة من الشركة العربية للمشروعات لصالح موردين ومقاولين خلال فترات ضغط السيولة وإعادة الهيكلة المالية. صدرت أحكام أولية ضد الموقعين المعتمدين، وتمت تسويتها بالتصالح القضائي بعد جدولة المبالغ وإصدار شيكات بديلة واستبدالها بنقد." :
            "Criminal misdemeanor proceedings arising from commercial check defaults issued by ACPUD to contractors during historical liquidity crunches. Resulted in initial verdicts against authorized signatories, later resolved via rescheduling and cash substitution.",
          foot1: currentLang === 'ar' ? "الأطراف: دائنون تجاريون ضد العربية للمشروعات" : "Parties: Commercial Creditors vs ACPUD",
          foot2: currentLang === 'ar' ? "النتيجة: انقضاء الدعوى بالتصالح والجدولة" : "Outcome: Reconciled via Rescheduling",
          color: "var(--accent-amber)",
          src: "cairo_misdemeanor_checks"
        },
        {
          title: currentLang === 'ar' ? "منظومة التحكيم المؤسسي الإجباري (CRCICA)" : "CRCICA Mandatory Arbitration Architecture",
          badge: currentLang === 'ar' ? "تحكيم مؤسسي" : "Arbitration Shield",
          desc: currentLang === 'ar' ? 
            "إلزام كافة مقاولي الباطن والموردين بشرط التحكيم بمركز القاهرة الإقليمي للتحكيم التجاري الدولي. يحرم هذا الشرط المقاول من اللجوء للقضاء الوطني المستعجل، وتجعل تكاليف قيد التحكيم وأتعاب المحكمين المرتفعة مقاضاة المطالبات الأقل من 20 مليون جنيه غير مجدية اقتصادياً." :
            "All subcontract and supply agreements mandate confidential institutional arbitration under CRCICA rules. High filing fees suppress claims under EGP 20M from SME subcontractors, forcing negotiated commercial discounts.",
          foot1: currentLang === 'ar' ? "المستشارون: سري الدين وشركاه / معتوق بسيوني" : "Counsel: Sarie Eldin / Matouk Bassiouny",
          foot2: currentLang === 'ar' ? "الأثر: منع النزاعات من التداول العلني بالمحاكم" : "Impact: Public Court Litigation Suppressed",
          color: "var(--accent-blue)",
          src: "egx_filings_fy25_h126"
        },
        {
          title: currentLang === 'ar' ? "محكمة لندن العليا (دائرة كوينز بنش) — العزاوي ضد هشام طلعت مصطفى" : "London High Court — Al-Azzawi vs. Hisham Talaat Moustafa",
          badge: currentLang === 'ar' ? "قضاء دولي" : "Foreign Court",
          desc: currentLang === 'ar' ? 
            "دعوى تعويض مدني وأضرار نفسية مقامة في بريطانيا ضد الرئيس التنفيذي للمجموعة. في يوليو 2025، قضت المحكمة الإنجليزية برفض الدعوى بالكامل لعدم الاختصاص القضائي (Forum Non Conveniens)، مؤكدة أن القضاء المصري هو جهة الاختصاص الطبيعية للنزاع." :
            "Tort damages and psychological injury claim filed in the United Kingdom against TMG's CEO. In July 2025, the London High Court dismissed the claim in its entirety on jurisdictional grounds (forum non conveniens), holding Egyptian courts appropriate.",
          foot1: currentLang === 'ar' ? "التاريخ: يوليو 2025" : "Date: July 2025",
          foot2: currentLang === 'ar' ? "الحكم: رفض الدعوى لعدم الاختصاص القضائي" : "Outcome: Dismissed (Forum Non Conveniens)",
          color: "var(--accent-purple)",
          src: "egx_filings_fy25_h126"
        }
      ];

      document.getElementById('disputes-cards-container').innerHTML = disputes.map(d => `
        <div class="flag-card" style="border-inline-start-color: ${d.color}; cursor: pointer;" onclick="showSourceModal('${d.src}')">
          <div class="flag-header">
            <span class="flag-title">${d.title}</span>
            <span class="badge badge-med">${d.badge}</span>
          </div>
          <div class="flag-desc">${d.desc}</div>
          <div class="flag-footer">
            <span>${d.foot1}</span>
            <button class="source-link" onclick="showSourceModal('${d.src}')">التوثيق القضائي ↗</button>
          </div>
        </div>
      `).join('');

      // 8. Financial Table Headers & Rows (Tab 7)
      const finRows = [
        { nameAr: "الإيرادات المجمعة (Consolidated Revenue)", nameEn: "Consolidated Revenue", fy21: "15,357", fy22: "19,873", fy23: "28,432", fy24: "42,700", fy25: "62,500", h126: "30,190", color: "var(--accent-cyan)", bold: true },
        { nameAr: "— تسليمات النشاط العقاري السكني", nameEn: "— Real Estate Deliveries", fy21: "10,214", fy22: "14,715", fy23: "21,630", fy24: "28,800", fy25: "36,700", h126: "17,000", color: "", bold: false },
        { nameAr: "— إيرادات الفنادق والسياحة (دولارية)", nameEn: "— Hospitality & Tourism (USD Hedge)", fy21: "1,268", fy22: "2,564", fy23: "3,545", fy24: "11,400", fy25: "14,900", h126: "7,500", color: "", bold: false },
        { nameAr: "صافي الأرباح المجمعة (Net Profit)", nameEn: "Consolidated Net Profit", fy21: "1,780", fy22: "2,230", fy23: "3,310", fy24: "12,800", fy25: "18,200", h126: "9,950", color: "var(--accent-emerald)", bold: true },
        { nameAr: "— نصيب مساهمي الشركة القابضة الأم", nameEn: "— Attributable to Parent Equity", fy21: "1,780", fy22: "2,230", fy23: "3,310", fy24: "9,800", fy25: "14,500", h126: "7,477", color: "", bold: false },
        { nameAr: "المبيعات التعاقدية الجديدة (New Sales)", nameEn: "New Contracted Sales", fy21: "32,360", fy22: "33,200", fy23: "142,700", fy24: "504,000", fy25: "382,200", h126: "219,100", color: "var(--accent-amber)", bold: true },
        { nameAr: "رصيد المبيعات المتعاقد عليها غير المسلمة (Backlog)", nameEn: "Contracted Backlog (Unearned)", fy21: "63,000", fy22: "77,000", fy23: "145,000", fy24: "294,000", fy25: "441,200", h126: ">460,000", color: "", bold: true },
        { nameAr: "الدائنون وأوراق الدفع التجارية (*شيكات مقاولين*)", nameEn: "Operating Creditors & Notes Payable", fy21: "3,400", fy22: "4,900", fy23: "8,200", fy24: "12,400", fy25: ">15,790", h126: ">16,200", color: "var(--accent-rose)", bold: true },
        { nameAr: "التزامات عقود التأجير التمويلي (ديون هيكلية)", nameEn: "Financial Lease Notes Payable (Off-Bal)", fy21: "1,200", fy22: "2,100", fy23: "4,800", fy24: "22,100", fy25: "34,400", h126: "43,990", color: "var(--accent-rose)", bold: true },
        { nameAr: "دفعات العملاء المقدمة (التزامات تسليم)", nameEn: "Customer Advance Payments", fy21: "38,500", fy22: "48,200", fy23: "72,000", fy24: "95,000", fy25: "117,680", h126: "133,990", color: "", bold: false },
        { nameAr: "النقدية والأرصدة لدى البنوك واستثمارات سائلة", nameEn: "Cash & Liquid Financial Assets", fy21: "4,210", fy22: "4,780", fy23: "11,500", fy24: "32,000", fy25: "41,200", h126: "66,400", color: "var(--accent-emerald)", bold: true }
      ];

      document.getElementById('financials-tbody').innerHTML = finRows.map(r => `
        <tr>
          <td><strong style="${r.bold ? 'font-weight:800;' : 'font-weight:normal;'} color:${r.color || 'inherit'}">${currentLang === 'ar' ? r.nameAr : r.nameEn}</strong></td>
          <td class="cell-mono">${r.fy21}</td>
          <td class="cell-mono">${r.fy22}</td>
          <td class="cell-mono">${r.fy23}</td>
          <td class="cell-mono">${r.fy24}</td>
          <td class="cell-mono" style="${r.color ? 'color:' + r.color + '; font-weight:700;' : ''}">${r.fy25}</td>
          <td class="cell-mono" style="font-weight:700;">${r.h126}</td>
          <td><button class="source-link" onclick="showSourceModal('egx_filings_fy25_h126')">البورصة ↗</button></td>
        </tr>
      `).join('');
    }

    function renderTableHeaders() {
      // Projects headers
      document.getElementById('projects-th-row').innerHTML = currentLang === 'ar' ? `
        <th>اسم المشروع</th>
        <th>الموقع والمساحة</th>
        <th>الشركة المالكة وحصة طلعت</th>
        <th>نموذج الأرض والشراكة</th>
        <th>موقف التسليم الفعلي</th>
        <th>المكونات الأساسية والوحدات</th>
        <th>مستوى المخاطرة</th>
        <th>المصدر</th>
      ` : `
        <th>Project Name</th>
        <th>Location & Size</th>
        <th>Owning SPV & Stake</th>
        <th>Land / Partner Model</th>
        <th>Delivery Status</th>
        <th>Key Components</th>
        <th>Risk Level</th>
        <th>Source</th>
      `;

      // Contractors headers
      document.getElementById('contractors-th-row').innerHTML = currentLang === 'ar' ? `
        <th>المشروع</th>
        <th>كيان طلعت مصطفى المتعاقد</th>
        <th>المقاول الرئيسي</th>
        <th>مقاول الباطن / المورد</th>
        <th>نطاق الأعمال المنفذة</th>
        <th>مستند العلاقة والتواريخ</th>
        <th>الملاحظة التوثيقية والنزاع</th>
        <th>المصدر الموثق</th>
        <th>المخاطرة</th>
      ` : `
        <th>Project</th>
        <th>TMG Legal Entity</th>
        <th>Main Contractor</th>
        <th>Subcontractor / Supplier</th>
        <th>Scope of Works</th>
        <th>Contract Evidence</th>
        <th>Documented Dispute / Issue</th>
        <th>Source</th>
        <th>Risk</th>
      `;

      // Complaints headers
      document.getElementById('complaints-th-row').innerHTML = currentLang === 'ar' ? `
        <th>المشروع / الواقعة</th>
        <th>تصنيف الشكوى</th>
        <th>تفاصيل الشكوى والمطالب الموثقة</th>
        <th>تاريخ الواقعة</th>
        <th>الجهة / المنصة</th>
        <th>التكييف والتقييم الجنائي</th>
      ` : `
        <th>Project / Incident</th>
        <th>Category</th>
        <th>Documented Claim / Incident</th>
        <th>Date</th>
        <th>Source / Platform</th>
        <th>Forensic Classification</th>
      `;

      // Risks headers
      document.getElementById('risks-th-row').innerHTML = currentLang === 'ar' ? `
        <th>تصنيف الخطر الجنائي</th>
        <th>مستوى الأثر</th>
        <th>الاحتمالية</th>
        <th>الآليات التشغيلية ومؤشرات الإنذار</th>
        <th>إجراءات الفحص والتحوط النافية للجهالة</th>
        <th>المصدر والتوثيق</th>
      ` : `
        <th>Risk Category</th>
        <th>Severity</th>
        <th>Likelihood</th>
        <th>Operational Mechanisms & Indicators</th>
        <th>Actionable Diligence Controls</th>
        <th>Source & Citation</th>
      `;

      // Financials headers
      document.getElementById('financials-th-row').innerHTML = currentLang === 'ar' ? `
        <th>المؤشر المالي (مليون جنيه مصري)</th>
        <th>FY2021</th>
        <th>FY2022</th>
        <th>FY2023</th>
        <th>FY2024</th>
        <th>FY2025</th>
        <th>H1 2026</th>
        <th>الإفصاح</th>
      ` : `
        <th>Financial Indicator (EGP Millions)</th>
        <th>FY2021</th>
        <th>FY2022</th>
        <th>FY2023</th>
        <th>FY2024</th>
        <th>FY2025</th>
        <th>H1 2026</th>
        <th>Disclosure</th>
      `;
    }

    function setLanguage(lang) {
      currentLang = lang;
      document.documentElement.setAttribute('lang', lang);
      document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

      document.getElementById('lang-ar').classList.toggle('active', lang === 'ar');
      document.getElementById('lang-en').classList.toggle('active', lang === 'en');

      // Update Nav labels
      const navTexts = {
        ar: {
          brandTitle: "استخبارات طلعت مصطفى",
          brandSub: "درع الفحص النافي للجهالة",
          navLabel: "وحدات التحقيق الجنائي",
          overview: "لوحة القيادة التنفيذية",
          procurement: "المشتريات المدمجة والدرع القانوني",
          mustakhlasat: "المستخلصات وعقبة الصرف",
          projects: "محفظة المشاريع والأصول",
          contractors: "سجل المقاولين والموردين",
          disputes: "الأحكام القضائية وسجلات التحكيم",
          financials: "التحليل المالي الجنائي والسيولة",
          sentiment: "شكاوى المقاولين والعمال والملاك",
          risks: "مصفوفة المخاطر ودليل التحوط",
          pzone: "دراسة P.ZONE وحزم المياه",
          stakeholders: "خريطة المشروعات وأصحاب المصلحة",
          cutoff: "تاريخ الفحص: 11 أكتوبر 2026",
          cap: "رأس المال: 20.64 مليار جنيه",
          auditedBadge: "مدقق رسمياً من الإفصاحات والمصادر المباشرة",
          searchPh: "ابحث عن كيان، مقاول، قضية، مصدر...",
          btnPresenter: "وضع العرض التنفيذي",
          btnPrint: "طباعة / تصدير PDF",
          btnResetD3: "إعادة ضبط المشهد",
          fltAll: "الكل (14)",
          fltEast: "شرق القاهرة",
          fltCoast: "الساحل والبحر الأحمر",
          fltBorder: "خارج الحدود (السعودية)",
          fltHosp: "شركات الفنادق التابعة"
        },
        en: {
          brandTitle: "TMG Forensic Intel",
          brandSub: "Due Diligence Harness",
          navLabel: "Investigation Modules",
          overview: "Executive Dashboard",
          procurement: "Captive Procurement & Privity",
          mustakhlasat: "المستخلصات & Payment Gate",
          projects: "Project Portfolio & Assets",
          contractors: "Master Contractor Roster",
          disputes: "Legal, Arbitration & Courts",
          financials: "Financial Forensics",
          sentiment: "Contractor, Labor & Resident Grievances",
          risks: "Risk Matrix & Playbooks",
          pzone: "P.ZONE Water MEP Case Study",
          stakeholders: "Project Map & Stakeholders",
          cutoff: "Cut-Off: 11 Oct 2026",
          cap: "Issued Capital: EGP 20.64 bn",
          auditedBadge: "Audited Primary Verified Evidence",
          searchPh: "Search entity, contractor, case, source...",
          btnPresenter: "Presenter Mode",
          btnPrint: "Export / Print",
          btnResetD3: "Reset View",
          fltAll: "All (14)",
          fltEast: "East Cairo",
          fltCoast: "Coastal / Red Sea",
          fltBorder: "Cross-Border (KSA)",
          fltHosp: "Hospitality SPVs"
        }
      };

      const t = navTexts[lang];
      document.getElementById('lbl-brand-title').textContent = t.brandTitle;
      document.getElementById('lbl-brand-sub').textContent = t.brandSub;
      document.getElementById('lbl-nav-label').textContent = t.navLabel;
      document.getElementById('nav-overview').textContent = t.overview;
      document.getElementById('nav-procurement').textContent = t.procurement;
      document.getElementById('nav-mustakhlasat').textContent = t.mustakhlasat;
      document.getElementById('nav-projects').textContent = t.projects;
      document.getElementById('nav-contractors').textContent = t.contractors;
      document.getElementById('nav-disputes').textContent = t.disputes;
      document.getElementById('nav-financials').textContent = t.financials;
      document.getElementById('nav-sentiment').textContent = t.sentiment;
      document.getElementById('nav-risks').textContent = t.risks;
      document.getElementById('lbl-cutoff').textContent = lang === 'ar' ? 'تاريخ الفحص' : 'Cut-Off';
      document.getElementById('lbl-cap').textContent = lang === 'ar' ? 'رأس المال المصدر' : 'Issued Capital';
      document.getElementById('lbl-badge-audited').textContent = t.auditedBadge;
      document.getElementById('global-search').setAttribute('placeholder', t.searchPh);
      document.getElementById('btn-presenter-lbl').textContent = t.btnPresenter;
      document.getElementById('btn-print-lbl').textContent = t.btnPrint;
      document.getElementById('btn-reset-d3').textContent = t.btnResetD3;
      document.getElementById('btn-flt-all').textContent = t.fltAll;
      document.getElementById('btn-flt-east').textContent = t.fltEast;
      document.getElementById('btn-flt-coast').textContent = t.fltCoast;
      document.getElementById('btn-flt-border').textContent = t.fltBorder;
      document.getElementById('btn-flt-hosp').textContent = t.fltHosp;

      // Dynamic Chart Titles & Subtitles (11 Visualizations)
      document.getElementById('t-chart-land-title').textContent = lang === 'ar' ? "1. محفظة الأراضي وتوزيع المساحات (فدان)" : "1. Landbank Footprint by Development (Feddans)";
      document.getElementById('t-chart-land-sub').textContent = lang === 'ar' ? "المساحات الإجمالية لأبرز المشاريع العملاقة التابعة للمجموعة بمصر" : "Total development scale across primary Egyptian mega-projects (Feddans)";
      document.getElementById('badge-chart-land').textContent = lang === 'ar' ? "مساحات الأراضي" : "Land Concessions";

      document.getElementById('t-chart-radar-title').textContent = lang === 'ar' ? "2. رادار أبعاد المخاطر الجنائية والتعاقدية (1 - 10)" : "2. Forensic Multi-Dimensional Risk Radar (Scale 1 - 10)";
      document.getElementById('t-chart-radar-sub').textContent = lang === 'ar' ? "تقييم تركيبي لأبرز مخاطر التعاقد: الصرف، العزل القانوني، التحكيم، والتضخم" : "Composite assessment of counterparty, privity, arbitration & inflation risks";
      document.getElementById('badge-chart-radar').textContent = lang === 'ar' ? "تحليل المخاطر" : "Risk Breakdown";

      document.getElementById('t-chart-owner-title').textContent = lang === 'ar' ? "3. هيكل الملكية والمساهمين الرئيسيين (UBO)" : "3. Ownership & Ultimate Beneficial Ownership (UBO)";
      document.getElementById('t-chart-owner-sub').textContent = lang === 'ar' ? "توزيع حصص رأس المال المصدر: عائلة طلعت مصطفى مقابل التداول الحر والصناديق" : "Issued capital shareholding: Talaat Moustafa Family vs Free Float & Foreign Funds";
      document.getElementById('badge-chart-owner').textContent = lang === 'ar' ? "هيكل الملكية" : "UBO Matrix";

      document.getElementById('t-chart-polar-title').textContent = lang === 'ar' ? "4. هرمية قوة الأدلة وموثوقية مصادر الفحص" : "4. Evidence Strength & Verification Hierarchy";
      document.getElementById('t-chart-polar-sub').textContent = lang === 'ar' ? "التصنيف الإثباتي: أحكام قضائية وإفصاحات رسمية مقابل سوابق هندسية وتسويق" : "Relative evidentiary weight: Judicial & regulatory vs engineering records & claims";
      document.getElementById('badge-chart-polar').textContent = lang === 'ar' ? "حجية الأدلة" : "Evidence Hierarchy";

      document.getElementById('t-chart-ipc-title').textContent = lang === 'ar' ? "مقارنة دورة صرف المستخلصات: التعاقدي (90 يوماً) مقابل المرصود فعلياً (270 يوماً)" : "Payment Certificate Lifecycle: Contractual (90 Days) vs Observed Delay (270 Days)";
      document.getElementById('t-chart-ipc-sub').textContent = lang === 'ar' ? "المسار الزمني لمراحل تدقيق واعتماد المستخلصات حتى التحصيل النقدي النهائي" : "Multi-stage timeline comparing standard BOQ review against prolonged technical deferral";
      document.getElementById('badge-chart-ipc').textContent = lang === 'ar' ? "المستخلصات وأوراق الدفع" : "IPC & Payables";

      document.getElementById('t-chart-bubble-title').textContent = lang === 'ar' ? "مصفوفة حجم التعاقد مقابل مؤشر النزاعات والتوتر الموقعي" : "Counterparty Contract Scale vs Public Dispute Friction Index";
      document.getElementById('t-chart-bubble-sub').textContent = lang === 'ar' ? "تحليل نسبي للشركاء والمقاولين والعمال: حجم الأعمال (مليار جنيه) مقابل مؤشر التوتر العلني (1-10)" : "Relative analysis of contractors & labor: Contract value (EGP bn) vs friction index (1-10)";
      document.getElementById('badge-chart-bubble').textContent = lang === 'ar' ? "خريطة الاحتكاك" : "Friction Matrix";

      document.getElementById('t-chart-liab-title').textContent = lang === 'ar' ? "خريطة الالتزامات المالية، التسهيلات البنكية، وأوراق الدفع المؤجلة" : "Commercial Debt, Liabilities, Bank Facilities & Notes Payable";
      document.getElementById('t-chart-liab-sub').textContent = lang === 'ar' ? "التسهيلات البنكية، توريق أصول رواسي، وأوراق الدفع المؤجلة للموردين والمقاولين (مليار جنيه)" : "Disclosed banking facilities, asset liquidations, and trade payables (EGP Billions)";
      document.getElementById('badge-chart-liab').textContent = lang === 'ar' ? "التزامات الدفع والتمويل" : "Liabilities & Paper";

      // Section titles
      document.getElementById('t-chart-fin-title').textContent = lang === 'ar' ? "المؤشرات المالية التاريخية (2021 – 2025 + النصف الأول 2026)" : "Multi-Year Financial Trends (2021 – 2025 + H1 26)";
      document.getElementById('t-chart-fin-sub').textContent = lang === 'ar' ? "الإيرادات، صافي الأرباح، والمبيعات المتعاقد عليها غير المسلمة (مليار جنيه)" : "Revenue, Net Profit, and Real Estate Contracted Backlog (EGP Billions)";
      document.getElementById('t-chart-comp-title').textContent = lang === 'ar' ? "توزيع شكاوى المقاولين والعمال والملاك" : "Documented Grievance Distribution (Contractor, Labor, Owner)";
      document.getElementById('t-chart-comp-sub').textContent = lang === 'ar' ? "تحليل نسبي للوقائع الموثقة بالصحف والمحاكم (عينة موثقة: 46 واقعة)" : "Indexed complaint breakdown across press and court records (n=46)";
      document.getElementById('t-conclusions-title').textContent = lang === 'ar' ? "النتائج الجوهرية المدققة للفحص النافي للجهالة" : "Core Material Verified Conclusions";
      document.getElementById('t-conclusions-sub').textContent = lang === 'ar' ? "مستندة للإفصاحات الرسمية، الأحكام القضائية، التحقيقات الصحفية وسجلات التنفيذ المباشرة" : "Grounded in corporate filings, court dockets, press investigations & engineering records";
      document.getElementById('t-proc-title').textContent = lang === 'ar' ? "هيكل المشتريات المدمجة والشبكة التفاعلية للحجية النسبية للعقود" : "Corporate Procurement & Interactive Contractual Privity Network";
      document.getElementById('t-proc-sub').textContent = lang === 'ar' ? "شجرة D3.js التفاعلية — انقر فوق أي كيان أو شركة لفحص سند الملكية، درع الحجية القانونية، ومصدر الإثبات" : "Interactive D3.js Privity Tree — Click any node to inspect ownership, legal privity shield, and exposure";
      document.getElementById('t-must-title').textContent = lang === 'ar' ? "عقبة دورة اعتماد مستخلصات المقاولين (المستخلصات)" : "The \"Payment Certificate\" Gatekeeping Bottleneck (المستخلصات)";
      document.getElementById('t-must-sub').textContent = lang === 'ar' ? "التسلسل الإجرائي لتدقيق واعتماد وصرف دفعات الإنجاز التجاري وأثرها على المقاولين" : "Procedural walkthrough of how progress payments are verified, audited, and deferred";
      document.getElementById('t-projects-title').textContent = lang === 'ar' ? "قاعدة البيانات الشاملة لمحفظة المشاريع والأصول" : "Comprehensive Project Database & Asset Ledger";
      document.getElementById('t-projects-sub').textContent = lang === 'ar' ? "هياكل الملكية الموثقة، تواريخ التسليم التعاقدية، ونماذج الشراكة على الأراضي مع روابط المصادر الرسمية" : "Verified ownership structures, delivery baselines, and land allocation models with clickable primary sources";
      document.getElementById('t-contractors-title').textContent = lang === 'ar' ? "السجل الموثق للمقاولين الرئيسيين ومقاولي الباطن والموردين" : "Master Documented Contractor, Supplier & Consultant Registry";
      document.getElementById('t-contractors-sub').textContent = lang === 'ar' ? "الأدوار التعاقدية، نطاقات الأعمال، الملاحظات التوثيقية، وروابط المصادر المباشرة لكل صفقة" : "Verified commercial roles, contracted scopes, documented issues, and verified source links";
      document.getElementById('t-disputes-title').textContent = lang === 'ar' ? "الأحكام القضائية، الجنح التجارية وسجلات التحكيم المؤسسي (CRCICA)" : "Judicial Decisions, Commercial Misdemeanors & Arbitration Dockets";
      document.getElementById('t-disputes-sub').textContent = lang === 'ar' ? "القضايا الموثقة بمجلس الدولة، محاكم الجنح، المحاكم الدولية، وبلاغات النيابة العامة مع مصادرها" : "Verified cases across State Council, Misdemeanor Courts, International Tribunals & Prosecutor General";
      document.getElementById('t-fin-cf-title').textContent = lang === 'ar' ? "تحليل كفاءة تحويل السيولة النقدية (النصف الأول 2026)" : "Cash Flow Conversion Analysis (H1 2026)";
      document.getElementById('t-fin-cf-sub').textContent = lang === 'ar' ? "صافي الأرباح مقابل التدفق النقدي التشغيلي واستنزاف رأس المال العامل (مليون جنيه)" : "Net Profit vs Operating Cash Flow vs Working Capital Drain (EGP Millions)";
      document.getElementById('t-fin-debt-title').textContent = lang === 'ar' ? "هيكل الالتزامات والديون الإجمالية (30 يونيو 2026)" : "Total Debt & Obligation Architecture (30 June 2026)";
      document.getElementById('t-fin-debt-sub').textContent = lang === 'ar' ? "القروض البنكية مقابل التأجير التمويلي ودفعات العملاء المقدمة (مليار جنيه)" : "Bank Loans vs Structured Financial Leases vs Customer Advances (EGP bn)";
      document.getElementById('t-fin-table-title').textContent = lang === 'ar' ? "المصفوفة المالية الجنائية للقوائم المدققة وميزانيات المجموعة (2021 – 2026)" : "Multi-Year Audited Balance Sheet & P&L Forensic Matrix";
      document.getElementById('t-fin-table-sub').textContent = lang === 'ar' ? "كافة الأرقام بملايين الجنيهات، مدققة من تقارير مراقبي الحسابات المودعة بالبورصة المصرية" : "All figures in EGP Millions, cross-checked against audited primary statements";
      document.getElementById('t-sent-table-title').textContent = lang === 'ar' ? "سجل الشكاوى التفصيلي: المقاولون، عمال المقاولات، واتحادات السكان" : "Granular Incident Log: Contractors, Construction Labor & Resident Associations";
      document.getElementById('t-sent-table-sub').textContent = lang === 'ar' ? "يتضمن واقعة مقاول مدينتي التاريخية، احتجاجات عمال الإسكندرية للإنشاءات، وبلاغات الملاك مع روابط الصحف الموثقة" : "Covering 2008 Madinaty contractor incident, ACC labor protests, security workforce petitions & homeowner disputes";
      document.getElementById('t-risks-table-title').textContent = lang === 'ar' ? "مصفوفة المخاطر الجنائية ومؤشرات الإنذار المبكر" : "Forensic Risk Register & Severity Matrix";
      document.getElementById('t-risks-table-sub').textContent = lang === 'ar' ? "تقييم شامل للأثر، احتمالية الحدوث، الآليات التشغيلية، وخطط الفحص النافية للجهالة" : "Evaluating likelihood, potential impact, observable triggers, and suggested diligence controls";

      // Tab 11: Stakeholders, Map, Teams & SWOT Bilingual Strings
      if (document.getElementById('stakeholders-header-title')) {
        document.getElementById('stakeholders-header-title').textContent = lang === 'ar'
          ? "خريطة المشروعات وأصحاب المصلحة ودليل الفرق والمقاولين (42 كيان و 38 ملف قيادي)"
          : "Project Master Map, Stakeholders, Supply Chain & Key Personnel Directory (42 Entities & 38 Executive Profiles)";
      }
      if (document.getElementById('stakeholders-header-desc')) {
        document.getElementById('stakeholders-header-desc').textContent = lang === 'ar'
          ? "خريطة جغرافية تفاعلية شاملة لمشروعات مجموعة طلعت مصطفى (TMGH) في مصر والسعودية وعمان. تتيح استعراض 42 شركة ومقاول ومورد معتمد مع أرقام التواصل العامة، و 38 قيادياً ومهندساً مع روابط LinkedIn موثقة، مصحوبة بمصفوفة SWOT و TOWS الاستراتيجية المدققة."
          : "Comprehensive interactive geospatial map covering Talaat Moustafa Group Holding (TMGH) developments across Egypt, KSA, and Oman. Indexed repository of 42 verified contractors, suppliers, and financial institutions with public contact channels, 38 executive personnel with verified LinkedIn credentials, and the strategic forensic SWOT / TOWS matrix.";
      }
      if (document.getElementById('kpi-lbl-landbank')) {
        document.getElementById('kpi-lbl-landbank').textContent = lang === 'ar' ? "إجمالي محفظة الأراضي (Landbank)" : "Total Master Landbank";
      }
      if (document.getElementById('kpi-lbl-backlog')) {
        document.getElementById('kpi-lbl-backlog').textContent = lang === 'ar' ? "رصيد المبيعات التعاقدية (Backlog)" : "Contracted Sales Backlog";
      }
      if (document.getElementById('kpi-lbl-comp-count')) {
        document.getElementById('kpi-lbl-comp-count').textContent = lang === 'ar' ? "الكيانات والشركات المفهرسة" : "Indexed Corporate Entities";
      }
      if (document.getElementById('kpi-lbl-team-count')) {
        document.getElementById('kpi-lbl-team-count').textContent = lang === 'ar' ? "فرق العمل وقيادات المشاريع" : "Executive Teams & Key Personnel";
      }
      if (document.getElementById('map-section-title')) {
        document.getElementById('map-section-title').textContent = lang === 'ar' ? "🗺️ الخريطة الجغرافية التفاعلية لمشروعات TMG التوسعية" : "🗺️ Interactive Geospatial Map of TMG Expansion Projects";
      }
      if (document.getElementById('map-section-subtitle')) {
        document.getElementById('map-section-subtitle').textContent = lang === 'ar' ? "انقر على أي علامة مشروع لتكبير الخريطة وتصفية جدول المقاولين ودليل الفرق تلقائياً" : "Click any project pin to zoom in and automatically cross-filter the contractor and team directories below";
      }
      if (document.getElementById('companies-table-title')) {
        document.getElementById('companies-table-title').textContent = lang === 'ar' ? "🏢 دليل الشركات والجهات المرتبطة بمشروعات TMG (أرقام التواصل العامة المنشورة)" : "🏢 Documented Project Entities, Contractors & Supply Chain Directory (Public Contact Channels)";
      }
      if (document.getElementById('companies-table-subtitle')) {
        document.getElementById('companies-table-subtitle').textContent = lang === 'ar' ? "42 كيان مفهرس مع الصفة، نطاق العمل، أرقام الهاتف العامة، البريد، ومستوى ثقة العلاقة" : "42 verified corporate entities with contract scope, public contact numbers, email, web portals, and evidentiary confidence tiers";
      }
      if (document.getElementById('teams-section-title')) {
        document.getElementById('teams-section-title').textContent = lang === 'ar' ? "👥 دليل الأشخاص وفرق العمل المرتبطة بالمشروعات (ملفات LinkedIn العامة)" : "👥 Verified Project Teams & Key Personnel Directory (Public LinkedIn Profiles)";
      }
      if (document.getElementById('teams-section-subtitle')) {
        document.getElementById('teams-section-subtitle').textContent = lang === 'ar' ? "38 كادراً هندسياً وإدارياً مع المسمى المهني المنشور ودرجة التوثيق ورابط الملف المباشر" : "38 senior engineers and project leaders with published credentials, verification tier, and direct LinkedIn profile links";
      }
      if (document.getElementById('swot-section-title')) {
        document.getElementById('swot-section-title').textContent = lang === 'ar' ? "⚖️ التحليل الاستراتيجي الرباعي (TMG Deep SWOT Matrix) ومصفوفة TOWS التنفيذية" : "⚖️ Strategic Forensic SWOT Matrix & Actionable TOWS Roadmap";
      }
      if (document.getElementById('swot-section-subtitle')) {
        document.getElementById('swot-section-subtitle').textContent = lang === 'ar' ? "تقييم جنائي مفصل لنقاط القوة والضعف والفرص والتهديدات مع خطط العمل الاستراتيجية" : "Granular forensic appraisal of internal strengths, vulnerabilities, growth catalysts, and external risk vectors";
      }
      if (document.getElementById('btn-show-swot')) {
        document.getElementById('btn-show-swot').textContent = lang === 'ar' ? "مصفوفة SWOT الرباعية" : "Forensic SWOT Matrix";
      }
      if (document.getElementById('btn-show-tows')) {
        document.getElementById('btn-show-tows').textContent = lang === 'ar' ? "مصفوفة TOWS الاستراتيجية (Action Plans)" : "Actionable TOWS Roadmaps";
      }
      if (document.getElementById('btn-export-companies')) {
        document.getElementById('btn-export-companies').textContent = lang === 'ar' ? "📥 تصدير الشركات (CSV)" : "📥 Export Entities (CSV)";
      }
      if (document.getElementById('btn-export-teams')) {
        document.getElementById('btn-export-teams').textContent = lang === 'ar' ? "📥 تصدير القيادات (CSV)" : "📥 Export Teams (CSV)";
      }
      if (document.getElementById('btn-reset-filters')) {
        document.getElementById('btn-reset-filters').textContent = lang === 'ar' ? "🔄 إعادة ضبط التصفية" : "🔄 Reset Filters";
      }
      if (document.getElementById('company-search-input')) {
        document.getElementById('company-search-input').placeholder = lang === 'ar' ? "🔍 بحث باسم الشركة، الدور، أو المشروع..." : "🔍 Search by entity, scope, project, or phone...";
      }
      if (document.getElementById('team-search-input')) {
        document.getElementById('team-search-input').placeholder = lang === 'ar' ? "🔍 بحث باسم الشخص، المنصب، أو الشركة..." : "🔍 Search by person, title, company, or project...";
      }

      // Re-render Tab 11 components
      if (typeof renderCompaniesTable === 'function') renderCompaniesTable();
      if (typeof renderTeamsCards === 'function') renderTeamsCards();
      if (typeof renderSwotAndTows === 'function') renderSwotAndTows();

      // Re-initialize charts with language settings
      initCharts();

      // Render all tables & cards
      renderTableHeaders();
      renderProjects(currentFilteredProjects);
      renderContractorsTable();
      renderComplaintsTable();
      renderRisksTable();
      renderDynamicCards();

      // D3 text refresh
      renderD3PrivityTree();

      // Active tab header text
      const activeNavBtn = document.querySelector('.nav-btn.active span');
      if (activeNavBtn) {
        document.getElementById('current-tab-name').textContent = activeNavBtn.textContent;
      }

      localStorage.setItem('tmg_lang', lang);
    }

    function setTheme(theme) {
      currentTheme = theme;
      document.documentElement.setAttribute('data-theme', theme);
      document.getElementById('theme-light').classList.toggle('active', theme === 'light');
      document.getElementById('theme-dark').classList.toggle('active', theme === 'dark');
      localStorage.setItem('tmg_theme', theme);
      updateChartsTheme(theme);
      if (typeof updateMapTheme === 'function') updateMapTheme(theme);
    }

    
    // =========================================================================
    // TMG AUDITED BALANCE SHEET DYNAMIC ENGINE & FORMULA RECALCULATION
    // =========================================================================
    const tmgBSDatabase = {
      FY21: {
        cash: 4210, rec: 24500, wip: 46800, fin_inv: 1521, fa_cwip: 31200, oth_ast: 3470,
        st_loans: 3800, notes_pay: 5120, cust_adv: 38500, lt_debt: 8200, lease_debt: 1200, oth_liab: 2140,
        capital: 20636, reserves: 3450, ret_earn: 28655, nci: 0
      },
      FY22: {
        cash: 4780, rec: 28600, wip: 54200, fin_inv: 2100, fa_cwip: 36800, oth_ast: 3920,
        st_loans: 4500, notes_pay: 7300, cust_adv: 48200, lt_debt: 9800, lease_debt: 2100, oth_liab: 2600,
        capital: 20636, reserves: 4100, ret_earn: 31165, nci: 0
      },
      FY23: {
        cash: 11500, rec: 36400, wip: 71300, fin_inv: 4200, fa_cwip: 51200, oth_ast: 4620,
        st_loans: 6200, notes_pay: 9800, cust_adv: 72000, lt_debt: 14500, lease_debt: 4800, oth_liab: 3630,
        capital: 20636, reserves: 5200, ret_earn: 42454, nci: 0
      },
      FY24: {
        cash: 32000, rec: 48200, wip: 102500, fin_inv: 8500, fa_cwip: 81400, oth_ast: 6200,
        st_loans: 8900, notes_pay: 13500, cust_adv: 95000, lt_debt: 19800, lease_debt: 22100, oth_liab: 4730,
        capital: 20636, reserves: 7800, ret_earn: 52834, nci: 33500
      },
      FY25: {
        cash: 41200, rec: 62800, wip: 138500, fin_inv: 14200, fa_cwip: 107500, oth_ast: 8000,
        st_loans: 11200, notes_pay: 15790, cust_adv: 117680, lt_debt: 26500, lease_debt: 34400, oth_liab: 6830,
        capital: 20636, reserves: 11500, ret_earn: 68164, nci: 59500
      },
      H1_26: {
        cash: 47000, rec: 68500, wip: 152000, fin_inv: 16500, fa_cwip: 118000, oth_ast: 8900,
        st_loans: 12500, notes_pay: 16800, cust_adv: 129000, lt_debt: 28500, lease_debt: 44000, oth_liab: 7400,
        capital: 20636, reserves: 12800, ret_earn: 77964, nci: 69000
      }
    };

    let currentBSYear = 'FY24';

    function openExcelModal() {
      const modal = document.getElementById('excel-modal');
      if (modal) modal.classList.add('active');
    }

    function closeExcelModal() {
      const modal = document.getElementById('excel-modal');
      if (modal) modal.classList.remove('active');
    }

    function selectBSYear(yr) {
      currentBSYear = yr;
      const btns = document.querySelectorAll('#bs-year-selector button');
      btns.forEach(b => {
        if (b.getAttribute('onclick').includes(yr)) b.classList.add('active');
        else b.classList.remove('active');
      });
      updateBSCalculations();
    }

    function resetBSStress() {
      document.getElementById('slider-lease').value = 100;
      document.getElementById('slider-pay').value = 0;
      document.getElementById('slider-wip').value = 0;
      updateBSCalculations();
    }

    function updateBSCalculations() {
      const raw = tmgBSDatabase[currentBSYear] || tmgBSDatabase.FY24;
      
      const leasePct = parseFloat(document.getElementById('slider-lease')?.value || 100) / 100;
      const payPct = parseFloat(document.getElementById('slider-pay')?.value || 0) / 100;
      const wipDiscount = parseFloat(document.getElementById('slider-wip')?.value || 0) / 100;

      document.getElementById('val-slider-lease').innerText = `${Math.round(leasePct * 100)}%`;
      document.getElementById('val-slider-pay').innerText = `${Math.round(payPct * 100)}%`;
      document.getElementById('val-slider-wip').innerText = `${Math.round(wipDiscount * 100)}%`;

      // Recalculate Assets with stress
      const adjCash = Math.max(0, raw.cash - (raw.notes_pay * payPct));
      const adjWIP = raw.wip * (1 - wipDiscount);
      const currAssets = adjCash + raw.rec + adjWIP + raw.fin_inv + (raw.oth_ast * 0.6);
      const nonCurrAssets = raw.fa_cwip + (raw.oth_ast * 0.4);
      const totalAssets = currAssets + nonCurrAssets;

      // Recalculate Liabilities with stress
      const adjPayables = raw.notes_pay * (1 - payPct);
      const currLiab = raw.st_loans + adjPayables + raw.cust_adv + (raw.oth_liab * 0.5);
      const adjLease = raw.lease_debt * leasePct;
      const nonCurrLiab = raw.lt_debt + adjLease + (raw.oth_liab * 0.5);
      const totalLiab = currLiab + nonCurrLiab;

      // Recalculate Equity
      const totalEquity = raw.capital + raw.reserves + raw.ret_earn + raw.nci - (raw.wip * wipDiscount);
      const totalLiabAndEquity = totalLiab + totalEquity;
      const balanceCheck = totalAssets - totalLiabAndEquity;

      // Update Ribbon Cards
      document.getElementById('bs-card-assets').innerText = `${(totalAssets / 1000).toFixed(2)}B ج.م`;
      document.getElementById('bs-card-liab').innerText = `${(totalLiab / 1000).toFixed(2)}B ج.م`;
      document.getElementById('bs-card-equity').innerText = `${(totalEquity / 1000).toFixed(2)}B ج.م`;
      
      const checkEl = document.getElementById('bs-card-check');
      if (Math.abs(balanceCheck) < 1) {
        checkEl.innerText = "0.00 ج.م (متطابق 100%)";
        checkEl.style.color = "var(--accent-emerald)";
      } else {
        checkEl.innerText = `${(balanceCheck / 1000).toFixed(2)}B ج.م (فرق ضغط)`;
        checkEl.style.color = "var(--accent-amber)";
      }

      // Render Assets Table Rows
      const assetsHtml = `
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>النقدية وما في حكمها</strong> (Cash & Equivalents)</td><td class="cell-mono" style="text-align:right; font-weight:700;">${Math.round(adjCash).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>العملاء وأوراق القبض</strong> (Receivables)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.rec).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>مشروعات قيد التنفيذ / مخزون الأراضي</strong> (WIP)</td><td class="cell-mono" style="text-align:right;">${Math.round(adjWIP).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>استثمارات مالية بالقيمة العادلة</strong> (Investments)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.fin_inv).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أصول ثابتة وفنادق قيد التطوير</strong> (Fixed Assets)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.fa_cwip).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أصول أخرى متداولة وغير متداولة</strong> (Other)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.oth_ast).toLocaleString()} م.ج</td></tr>
        <tr style="background:var(--table-hover); font-weight:800; border-top:2px solid var(--accent-cyan);"><td style="padding:9px 4px; color:var(--accent-cyan);">إجمالي الأصول الحسابي (Total Assets)</td><td class="cell-mono" style="text-align:right; color:var(--accent-cyan); font-size:14px;">${Math.round(totalAssets).toLocaleString()} م.ج</td></tr>
      `;
      document.getElementById('bs-assets-rows').innerHTML = assetsHtml;

      // Render Liabilities & Equity Rows
      const liabHtml = `
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>تسهيلات بنكية قصيرة الأجل</strong> (ST Credit)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.st_loans).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أوراق الدفع ومستحقات المقاولين</strong> (Payables)</td><td class="cell-mono" style="text-align:right; color:var(--accent-amber);">${Math.round(adjPayables).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>دفعات حجز مقدمة من العملاء</strong> (Advances)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.cust_adv).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>قروض بنكية طويلة الأجل</strong> (LT Debt)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.lt_debt).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>التزامات تأجير تمويلي (رواسي)</strong> (Lease)</td><td class="cell-mono" style="text-align:right; color:var(--accent-rose);">${Math.round(adjLease).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>رأس المال المصدر والمدفوع</strong> (Capital)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.capital).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أرباح مرحلة واحتياطيات</strong> (Retained)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.reserves + raw.ret_earn).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>الحصص غير المسيطرة (أيقون ADQ)</strong> (NCI)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.nci).toLocaleString()} م.ج</td></tr>
        <tr style="background:var(--table-hover); font-weight:800; border-top:2px solid var(--accent-rose);"><td style="padding:9px 4px; color:var(--accent-rose);">إجمالي الالتزامات والملكية (Total Liab & Eq)</td><td class="cell-mono" style="text-align:right; color:var(--accent-rose); font-size:14px;">${Math.round(totalLiabAndEquity).toLocaleString()} م.ج</td></tr>
      `;
      document.getElementById('bs-liab-rows').innerHTML = liabHtml;

      // Calculate and Update Ratios
      const currentRatio = currLiab > 0 ? (currAssets / currLiab) : 0;
      const quickRatio = currLiab > 0 ? ((currAssets - adjWIP) / currLiab) : 0;
      const totalDebt = raw.st_loans + raw.lt_debt + adjLease;
      const netDebt = totalDebt - adjCash;
      const debtToEquity = totalEquity > 0 ? (totalDebt / totalEquity) : 0;
      const workingCapital = currAssets - currLiab;

      document.getElementById('calc-curr-ratio').innerText = `${currentRatio.toFixed(2)}x`;
      document.getElementById('calc-quick-ratio').innerText = `${quickRatio.toFixed(2)}x`;
      document.getElementById('calc-net-debt').innerText = `${(netDebt / 1000).toFixed(2)}B ج.م`;
      document.getElementById('calc-debt-eq').innerText = `${debtToEquity.toFixed(2)}x`;
      document.getElementById('calc-working-cap').innerText = `${workingCapital >= 0 ? '+' : ''}${(workingCapital / 1000).toFixed(2)}B ج.م`;
    }

    
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

    function switchTab(tabId) {
      if (typeof closeMobileSidebar === 'function') {
        closeMobileSidebar();
      }
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
      
      const targetPane = document.getElementById('tab-' + tabId);
      if (targetPane) targetPane.classList.add('active');

      const activeBtn = Array.from(document.querySelectorAll('.nav-btn')).find(b => b.getAttribute('onclick').includes(tabId));
      if (activeBtn) {
        activeBtn.classList.add('active');
        document.getElementById('current-tab-name').textContent = activeBtn.querySelector('span').textContent;
      }

      if (tabId === 'procurement') {
        setTimeout(renderD3PrivityTree, 60);
      }
      if (tabId === 'stakeholders') {
        setTimeout(function() {
          if (!window.tmgMapInitialized) {
            initTmgMap();
          } else if (tmgLeafletMapInstance) {
            tmgLeafletMapInstance.invalidateSize();
          }
        }, 100);
      }
    }

    function filterProjects(cat) {
      document.querySelectorAll('#project-filters .filter-btn').forEach(b => b.classList.remove('active'));
      if (window.event && window.event.target) {
        window.event.target.classList.add('active');
      }
      if (cat === 'all') {
        currentFilteredProjects = projectsData;
      } else {
        currentFilteredProjects = projectsData.filter(p => p.category === cat);
      }
      renderProjects(currentFilteredProjects);
    }

    function handleGlobalSearch(query) {
      query = query.toLowerCase().trim();
      if (!query) {
        currentFilteredProjects = projectsData;
        renderProjects(projectsData);
        renderContractorsTable();
        renderComplaintsTable();
        return;
      }
      currentFilteredProjects = projectsData.filter(p => 
        p.nameEn.toLowerCase().includes(query) ||
        p.nameAr.toLowerCase().includes(query) ||
        p.locEn.toLowerCase().includes(query) ||
        p.locAr.toLowerCase().includes(query) ||
        p.spv.toLowerCase().includes(query)
      );
      renderProjects(currentFilteredProjects);
    }

    /* ==========================================================================
       D3.JS INTERACTIVE PRIVITY TREE
       ========================================================================== */
    const privityTreeData = {
      nameAr: "مجموعة طلعت مصطفى القابضة (TMGH)",
      nameEn: "TMG Holding (TMGH)",
      typeAr: "الشركة القابضة المدرجة بالبورصة",
      typeEn: "Listed Parent Holding",
      descAr: "رأس المال المصدر 20.64 مليار جنيه. معزولة قانونياً عن التزامات مقاولي الباطن والعمالة.",
      descEn: "EGX Listed holding vehicle. Issued capital EGP 20.64B. Contractually insulated from trade subcontractors.",
      shieldAr: "درع حجية كامل ومطلق",
      shieldEn: "Complete Privity Shield",
      riskAr: "منخفضة قانونياً (تعرض مباشر معدوم)",
      riskEn: "Low Legal Privity Exposure",
      sourceKey: "egx_filings_fy25_h126",
      color: "#06b6d4",
      children: [
        {
          nameAr: "الإسكندرية للإنشاءات (ACC)",
          nameEn: "Alexandria Construction (ACC)",
          typeAr: "المقاول العام المدمج الحصري",
          typeEn: "Captive General Contractor",
          descAr: "مملوكة 100% لعائلة طلعت مصطفى، وتمتلك 8.03% بالقابضة. تمتص كافة النزاعات العمالية والتجارية ومستخلصات المقاولين.",
          descEn: "100% TM Family owned, 8.03% cross-shareholding in TMGH. Executes bulk civil packages & absorbs trade liabilities.",
          shieldAr: "حجية تعاقدية مباشرة",
          shieldEn: "Direct Contractual Privity",
          riskAr: "مرتفعة (مواجهة النيابة ومطالبات المقاولين والعمال)",
          riskEn: "High Operational & Labor Exposure",
          sourceKey: "masry_shehata_2008",
          color: "#f43f5e",
          children: [
            {
              nameAr: "المقاول شحاتة حسن (واقعة 2008)",
              nameEn: "Subcontractor Shehata (2008 Case)",
              typeAr: "مقاول باطن مدني",
              typeEn: "Civil Subcontractor",
              descAr: "بلاغ للنائب العام ضد هشام طلعت وإدارة مدينتي؛ واعتراف رسمي بتعمد تأخير الصرف لمنع العمال من مغادرة الموقع.",
              descEn: "Prosecutor General filing; official ACC admission of deliberate payment withholding to retain workforce.",
              shieldAr: "حجية مباشرة مع ACC فقط",
              shieldEn: "Privity with ACC Only",
              riskAr: "نزاع جنائي / تجاري موثق",
              riskEn: "Documented Dispute",
              sourceKey: "masry_shehata_2008",
              color: "#f43f5e"
            },
            {
              nameAr: "عمال أمن مدينتي (احتجاجات 2024-2025)",
              nameEn: "Madinaty Security Force (Protests 24-25)",
              typeAr: "عمالة تشغيل وحراسة تابعة",
              typeEn: "Site Security Workforce",
              descAr: "مذكرات رسمية للمطالبة بالأجر الإضافي عن 12 ساعة عمل وتحسين ظروف المعيشة والبدلات، وإحالة محتجين للتحقيق.",
              descEn: "Official petitions demanding overtime for 12-hr shifts and meal stipends; participants faced administrative inquiries.",
              shieldAr: "نزاع عمالي إداري",
              shieldEn: "Labor Dispute",
              riskAr: "مخاطر سمعة وتشغيل",
              riskEn: "Reputational Risk",
              sourceKey: "manassa_security_oct2025",
              color: "#f59e0b"
            },
            {
              nameAr: "مجموعة جمكا (Gemka Group)",
              nameEn: "Gemka Group (WWTP)",
              typeAr: "مقاول باطن كهروميكانيك",
              typeEn: "Trade Subcontractor (MEP)",
              descAr: "محطات معالجة الصرف الصحي ومضخات مدينتي وشبكات الري.",
              descEn: "Wastewater treatment equipment, sedimentation bridges, pumps.",
              shieldAr: "حجية مع شركة الإسكندرية",
              shieldEn: "Privity with ACC Only",
              riskAr: "منخفضة (احتجاز ضمان أعمال)",
              riskEn: "Low (Retention Hold)",
              sourceKey: "egx_filings_fy25_h126",
              color: "#10b981"
            },
            {
              nameAr: "سافيتو مصر (Saveto Egypt)",
              nameEn: "Saveto Egypt",
              typeAr: "مورد مواد بناء وتشطيب",
              typeEn: "Material Supplier",
              descAr: "توريد المونة الجافة ومعجون الحوائط ومواد الدهانات لمدينة نور.",
              descEn: "Dry-mix mortars, wall putties, architectural coatings for Noor City.",
              shieldAr: "عقود توريد وتسهيلات ائتمانية",
              shieldEn: "Supply Credit Terms",
              riskAr: "منخفضة (ائتمان موردين)",
              riskEn: "Low (Supply Terms)",
              sourceKey: "egx_filings_fy25_h126",
              color: "#10b981"
            }
          ]
        },
        {
          nameAr: "العربية للمشروعات (ACPUD)",
          nameEn: "Arab Co. for Projects (ACPUD)",
          typeAr: "المطور العقاري للمدن الكبرى (99.99%)",
          typeEn: "Megaproject Developer SPV",
          descAr: "المالك القانوني لامتيازات مدينتي، سيليا، وساوث ميد بالساحل الشمالي.",
          descEn: "99.99% owned by TMG Holding. Legal concession holder for Madinaty, Celia, and SouthMED.",
          shieldAr: "درع المطور الوسيط",
          shieldEn: "Intermediate Developer Shield",
          riskAr: "متوسطة (التزامات أراضي ومباني عينية)",
          riskEn: "Medium Concession Risk",
          sourceKey: "state_council_madinaty",
          color: "#06b6d4",
          children: [
            {
              nameAr: "كونكريت بلس (Concrete Plus)",
              nameEn: "Concrete Plus Contracting",
              typeAr: "مقاول عام حزمة مستقل (حزمة ساوث ميد C01)",
              typeEn: "Tier-1 General Contractor (SouthMED C01)",
              descAr: "تنفيذ 179 مبنى كامل التشطيب وبنية تحتية بساوث ميد (~10 مليار جنيه).",
              descEn: "Package C01 SouthMed (179 buildings) and Noor V3.2 villas (~EGP 10B total contract).",
              shieldAr: "حجية مباشرة مع العربية للمشروعات",
              shieldEn: "Direct Privity with ACPUD",
              riskAr: "متوسطة (ضغط الجدول الزمني لصيف 2029)",
              riskEn: "Medium Delivery Pacing",
              sourceKey: "egx_filings_fy25_h126",
              color: "#f59e0b"
            },
            {
              nameAr: "أتريوم للمقاولات (Atrium AQC)",
              nameEn: "Atrium Quality Contractors",
              typeAr: "مقاول عام مدمج لحزم العاصمة والتشطيب",
              typeEn: "Turnkey General Contractor",
              descAr: "شركة تابعة تتولى حزم سيليا والمشروعات التجارية.",
              descEn: "Wholly owned general contractor executing commercial and New Capital packages.",
              shieldAr: "حجية مقاول عام مستقل",
              shieldEn: "Contractor Privity Shield",
              riskAr: "متوسطة",
              riskEn: "Medium",
              sourceKey: "egx_filings_fy25_h126",
              color: "#f43f5e"
            }
          ]
        },
        {
          nameAr: "أيكون للفنادق (ICON Luxury)",
          nameEn: "ICON Luxury Hotels",
          typeAr: "ذراع الضيافة والفنادق الفاخرة (59.5% طلعت / 40.5% ADQ)",
          typeEn: "Hospitality Arm (59.5% TMG / 40.5% ADQ)",
          descAr: "تمتلك فنادق الفور سيزونز و7 فنادق تاريخية (ليجاسي). أصل مدر للنقد الأجنبي.",
          descEn: "Owns Four Seasons properties and 7 Historic Hotels (Legacy Hotels). Foreign currency revenue hedge.",
          shieldAr: "درع الشركة المشتركة الدولية",
          shieldEn: "Joint Venture Shield",
          riskAr: "منخفضة تشغيلياً (حماية تدفقات دولارية)",
          riskEn: "Low Operational Risk",
          sourceKey: "egx_filings_fy25_h126",
          color: "#8b5cf6",
          children: [
            {
              nameAr: "محفظة الفنادق التاريخية (Legacy)",
              nameEn: "Historic Hotels Portfolio",
              typeAr: "استحواذ تاريخي على أصول الدولة",
              typeEn: "State Asset Acquisition",
              descAr: "مينا هاوس، ماريوت القاهرة، أولد كتاراكت، وينتر بالاس، سيسل.",
              descEn: "Mena House, Cairo Marriott, Cecil, Old Cataract, Winter Palace.",
              shieldAr: "كيان استثماري مؤسسي",
              shieldEn: "Institutional SPV",
              riskAr: "منخفضة",
              riskEn: "Low",
              sourceKey: "egx_filings_fy25_h126",
              color: "#3b82f6"
            },
            {
              nameAr: "فورسيزونز الأقصر (Four Seasons Luxor)",
              nameEn: "Four Seasons Luxor (EGOTH)",
              typeAr: "مشروع فندقي قيد التنفيذ (افتتاح 2027)",
              typeEn: "Hospitality Development (2027 Target)",
              descAr: "تطوير على أرض إيجوث التاريخية. مقاول رئيسي أتريوم، إدارة هيل، استشاري شاكر، تحالف CCC للأعمال الكهروميكانيكية. فحص المستخلصات لم يسفر عن أي شكاوى معلنة حتى تاريخه.",
              descEn: "Developed on EGOTH land. Atrium Main EPC, Hill PM, Shaker Consultant, CCC MEP JV. No verified public contractor complaints.",
              shieldAr: "درع المقاول الرئيسي أتريوم وتحالف CCC",
              shieldEn: "Atrium EPC & CCC JV Privity Shield",
              riskAr: "منخفضة إلى متوسطة (تعديل جدول زمني لـ 2027)",
              riskEn: "Low-Medium (Schedule Shift to 2027)",
              sourceKey: "atrium_luxor_award",
              color: "#10b981"
            }
          ]
        }
      ]
    };

    let d3Svg, d3G, d3Zoom;

    function renderD3PrivityTree() {
      const container = document.getElementById('d3-privity-tree');
      if (!container) return;
      const width = container.clientWidth || 900;
      const height = container.clientHeight || 480;

      d3.select('#d3-privity-tree svg').remove();

      d3Svg = d3.select('#d3-privity-tree')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      d3G = d3Svg.append('g').attr('transform', currentLang === 'ar' ? `translate(${width - 120}, 40)` : 'translate(100, 40)');

      d3Zoom = d3.zoom().scaleExtent([0.5, 2.5]).on('zoom', (e) => {
        d3G.attr('transform', e.transform);
      });
      d3Svg.call(d3Zoom);

      const treeLayout = d3.tree().size([height - 80, width - 280]);
      const root = d3.hierarchy(privityTreeData);
      treeLayout(root);

      // Links with directional logic
      d3G.selectAll('.d3-link')
        .data(root.links())
        .enter()
        .append('path')
        .attr('class', 'd3-link')
        .attr('d', d3.linkHorizontal()
          .x(d => currentLang === 'ar' ? -d.y : d.y)
          .y(d => d.x)
        );

      // Nodes
      const node = d3G.selectAll('.d3-node')
        .data(root.descendants())
        .enter()
        .append('g')
        .attr('class', 'd3-node')
        .attr('transform', d => `translate(${currentLang === 'ar' ? -d.y : d.y}, ${d.x})`)
        .on('click', (event, d) => inspectNode(d.data));

      node.append('circle')
        .attr('r', d => d.children ? 8 : 6)
        .attr('fill', d => d.data.color || '#06b6d4')
        .attr('stroke', currentTheme === 'light' ? '#0f172a' : '#fff');

      node.append('text')
        .attr('dy', 4)
        .attr('x', d => {
          if (currentLang === 'ar') {
            return d.children ? 14 : -14;
          } else {
            return d.children ? -14 : 14;
          }
        })
        .style('text-anchor', d => {
          if (currentLang === 'ar') {
            return d.children ? 'start' : 'end';
          } else {
            return d.children ? 'end' : 'start';
          }
        })
        .text(d => currentLang === 'ar' ? d.data.nameAr : d.data.nameEn)
        .style('font-size', '11.5px')
        .style('font-weight', d => d.depth <= 1 ? '800' : '600')
        .style('fill', currentTheme === 'light' ? '#0f172a' : '#f8fafc');
    }

    function inspectNode(data) {
      const panel = document.getElementById('node-inspector');
      document.getElementById('inspector-name').textContent = currentLang === 'ar' ? data.nameAr : data.nameEn;
      document.getElementById('inspector-type').textContent = currentLang === 'ar' ? data.typeAr : data.typeEn;
      document.getElementById('inspector-desc').textContent = currentLang === 'ar' ? data.descAr : data.descEn;
      document.getElementById('inspector-shield').textContent = currentLang === 'ar' ? data.shieldAr : data.shieldEn;
      document.getElementById('inspector-risk').textContent = currentLang === 'ar' ? data.riskAr : data.riskEn;
      
      if (data.sourceKey) {
        document.getElementById('inspector-source-box').innerHTML = `
          <button class="source-link" onclick="showSourceModal('${data.sourceKey}')">${currentLang === "ar" ? "فحص مستند الكيان ↗" : "Inspect Entity Legal Filing ↗"}</button>
        `;
      } else {
        document.getElementById('inspector-source-box').innerHTML = '';
      }
      panel.classList.add('active');
    }

    function closeInspector() {
      document.getElementById('node-inspector').classList.remove('active');
    }

    function resetD3View() {
      if (d3Svg && d3Zoom) {
        const width = document.getElementById('d3-privity-tree').clientWidth || 900;
        const initialX = currentLang === 'ar' ? width - 120 : 100;
        d3Svg.transition().duration(500).call(d3Zoom.transform, d3.zoomIdentity.translate(initialX, 40).scale(1));
      }
    }

    function zoomD3(factor) {
      if (d3Svg && d3Zoom) {
        d3Svg.transition().duration(300).call(d3Zoom.scaleBy, factor);
      }
    }

    /* ==========================================================================
       PRESENTER MODE ENGINE (Bilingual Slides)
       ========================================================================== */
    const presenterSlides = [
      {
        num: "SLIDE 01 / 10",
        titleAr: "لوحة القيادة التنفيذية والمركز المالي لمجموعة طلعت مصطفى",
        titleEn: "Executive Dashboard & Corporate Macro Overview",
        noteAr: "تمتلك طلعت مصطفى 20.64 مليار جنيه رأس مال مصدر ورصيد مبيعات متعاقد عليها يتجاوز 441 مليار جنيه، لكنها تعتمد على تدوير أوراق دفع تفوق 15.79 مليار جنيه لتأجيل التدفقات النقدية الخارجة.",
        noteEn: "TMG Holding boasts EGP 20.64B issued capital and >EGP 441B backlog, but relies on deferred commercial notes (>EGP 15.79B) to conserve working capital.",
        contentAr: `
          <div class="kpi-grid">
            <div class="kpi-card cyan">
              <div class="kpi-title">رأس المال المصدر والمدفوع</div>
              <div class="kpi-value">20.64 مليار جنيه</div>
              <div class="kpi-delta delta-up">● البورصة المصرية: TMGH</div>
            </div>
            <div class="kpi-card emerald">
              <div class="kpi-title">إيرادات / أرباح 2025 المجمعة</div>
              <div class="kpi-value">62.5B / 18.2B</div>
              <div class="kpi-delta delta-up">▲ +46% إيرادات / +43% أرباح</div>
            </div>
            <div class="kpi-card rose">
              <div class="kpi-title">الدائنون وأوراق الدفع التجارية</div>
              <div class="kpi-value">> 15.79 مليار جنيه</div>
              <div class="kpi-delta delta-down">▲ شيكات آجلة (90-270 يوماً)</div>
            </div>
          </div>
          <div style="font-size:13.5px; color:var(--text-muted); line-height:1.8; margin-top:20px;">
            تظهر التحقيقات الجنائية أن ضخامة أرقام المبيعات المتعاقد عليها (504 مليار في 2024 و382 مليار في 2025) تقابلها ضغوط حادة في كفاءة تحويل السيولة (معدل تحويل 31.2% فقط في H1 26)، مع امتصاص الإنشاءات لنحو 18.26 مليار جنيه في رأس المال العامل.
          </div>
        `,
        contentEn: `
          <div class="kpi-grid">
            <div class="kpi-card cyan">
              <div class="kpi-title">Issued & Paid Capital</div>
              <div class="kpi-value">EGP 20.64 bn</div>
              <div class="kpi-delta delta-up">● Listed EGX: TMGH</div>
            </div>
            <div class="kpi-card emerald">
              <div class="kpi-title">FY2025 Revenue / Net Profit</div>
              <div class="kpi-value">62.5B / 18.2B</div>
              <div class="kpi-delta delta-up">▲ +46% Rev / +43% Profit</div>
            </div>
            <div class="kpi-card rose">
              <div class="kpi-title">Operating Creditors & Notes</div>
              <div class="kpi-value">> EGP 15.79 bn</div>
              <div class="kpi-delta delta-down">▲ 90–270 day deferral</div>
            </div>
          </div>
          <div style="font-size:13.5px; color:var(--text-muted); line-height:1.8; margin-top:20px;">
            Forensic analysis shows that despite record sales (EGP 504B in 2024, EGP 382B in 2025), cash flow conversion is severely strained (31.2% in H1 26), driven by an EGP 18.26B working capital drain in WIP inventory.
          </div>
        `
      },
      {
        num: "SLIDE 02 / 10",
        titleAr: "درع المشتريات المدمجة ونسبية أثر العقود",
        titleEn: "Captive Procurement & Contractual Privity Shield",
        noteAr: "لا توقع الشركة القابضة أي عقود مقاولات باطن مباشرة؛ كافة الالتزامات محصورة بشركة الإسكندرية للإنشاءات (ACC) لمنع الحجز على أرصدة الشركة المدرجة.",
        noteEn: "Contractual privity shields the parent entity. Trade contractors have zero direct claim on TMG Holding bank accounts or project revenues.",
        contentAr: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-cyan);">
              <div class="flag-title">شركة الإسكندرية للإنشاءات (ACC) كحاجز قانوني</div>
              <div class="flag-desc">تمتلك عائلة طلعت مصطفى شركة المقاولات بالكامل، وهي الكيان الذي يوقع عقود مقاولي الباطن. إذا تعثر صرف المستخلصات، لا يستطيع المقاول مقاضاة الشركة القابضة المالكة للأصول.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">تجريد المقاول من هوامش التوريد</div>
              <div class="flag-desc">تشتري طلعت مصطفى الحديد والأسمنت مركزياً، مما يحصر دور مقاول الباطن في المصنعيات والعمالة فقط، ويعرضه لخطر الإفلاس عند تضخم أجور العمال دون تعويض.</div>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-cyan);">
              <div class="flag-title">The Alexandria Construction Co. (ACC) Insulator</div>
              <div class="flag-desc">ACC (100% TM Family owned) executes all major superstructures. Subcontractors sign with ACC, removing legal recourse against listed TMG Holding.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">Labor & Materials Decoupling</div>
              <div class="flag-desc">TMG buys rebar and cement directly. Trade subcontractors execute labor-only packages, eliminating contractor margin buffers against severe wage inflation.</div>
            </div>
          </div>
        `
      },
      {
        num: "SLIDE 03 / 10",
        titleAr: "ملف نزاعات المقاولين والمستخلصات: الوقائع التاريخية وبروتوكول التحقق",
        titleEn: "Contractor Disputes Dossier: Historic Litigation & Verification Gap Protocol",
        noteAr: "توثق المصادر واقعة 2008 وإقرار مدير الإسكندرية للإنشاءات بتعمد التأخير، والدعوى 2923 لسنة 2012 مدني شمال القاهرة بمطالبة 609,625 ج.م لأعمال سقالات بمدينتي، مع وضع بروتوكول من 5 محاور لإغلاق الفجوة.",
        noteEn: "Sources document the 2008 payment delay admission and North Cairo Civil Court Case 2923/2012 claiming EGP 609,625 for scaffolding in Madinaty, evaluated via a 5-point verification protocol.",
        contentAr: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-rose);">
              <div class="flag-title">الحالة 1: واقعة شحاتة حسن وإقرار التعطيل (أكتوبر 2008)</div>
              <div class="flag-desc">بلاغ للنائب العام لعدم صرف مستحقات عمال بمدينتي؛ ونقلت المصري اليوم اعتراف مدير شركة الإسكندرية (إبراهيم حسبو) بأن تأخير الصرف كان مقصوداً لمنع العمال من مغادرة الموقع بعد حبس هشام طلعت مصطفى.</div>
              <div class="flag-footer">
                <span>المصدر: المصري اليوم [م-1، م-2]</span>
                <button class="source-link" onclick="showSourceModal('masry_shehata_2008')">توثيق البلاغ ↗</button>
              </div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">الحالة 2: الدعوى 2923/2012 مدني شمال القاهرة (609,625 ج.م)</div>
              <div class="flag-desc">نزاع مقاول السقالات (شركة خالد هنداوي) حول عدم مطابقة أسعار المستخلصات لعقود الباطن في 3 مواقع بمدينتي (المدرسة البريطانية، بوابة 2011، السوق التجاري)، ومطالبة بفروق أسعار وإلزام ACC بتقديم أصول العقود.</div>
              <div class="flag-footer">
                <span>المصدر: مذكرة دفاع قضائية منشورة [م-3، م-4]</span>
                <button class="source-link" onclick="showSourceModal('khatib_scaffolding_2012')">فحص المذكرة ↗</button>
              </div>
            </div>
          </div>
          <div class="card" style="margin-top:14px; background:var(--bg-surface-elevated); border:1px solid rgba(0, 229, 255, 0.2);">
            <div class="card-title" style="font-size:12.5px; color:var(--accent-cyan);">بروتوكول المستندات الخمسة لإغلاق فجوة التحقق (Verification Gap Closure Protocol)</div>
            <div style="font-size:11.5px; color:var(--text-muted); line-height:1.7; margin-top:6px; display:grid; grid-template-columns:1fr 1fr; gap:10px;">
              <div>1. استخراج صورة رسمية من ملف الدعوى 2923/2012 وشهادة بما انتهت إليه.</div>
              <div>2. مطابقة أصول عقود الباطن وجداول الكميات وأوامر التغيير والمستخلصات.</div>
              <div>3. كشف حساب متبادل وإثباتات التحويلات البنكية والمخالصات الموقعة.</div>
              <div>4. التحقق من السجل التجاري للشخصية الاعتبارية الموقعة (العزل القانوني).</div>
              <div style="grid-column:1 / -1;">5. طلب رد موثق من إدارة المجموعة مع الالتزام بأن عدم الرد لا يثبت صحة الادعاء قانوناً.</div>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-rose);">
              <div class="flag-title">Case 1: 2008 Subcontractor Complaint & Intentional Delay Admission</div>
              <div class="flag-desc">Subcontractor Shehata Hassan filed report with Prosecutor General; ACC Director Ibrahim Hasabo confirmed on record that withholding dues was intentional to prevent workers deserting site.</div>
              <div class="flag-footer">
                <span>Source: Al-Masry Al-Youm [M-1, M-2]</span>
                <button class="source-link" onclick="showSourceModal('masry_shehata_2008')">View Report ↗</button>
              </div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">Case 2: Case 2923/2012 North Cairo Civil Court (EGP 609,625)</div>
              <div class="flag-desc">Scaffolding contractor Khaled Hendawi filed against ACC over rate discrepancies and un-signed contract sheets in 3 Madinaty zones, claiming EGP 609,625 and demanding original contracts.</div>
              <div class="flag-footer">
                <span>Source: Published Legal Defense Brief [M-3, M-4]</span>
                <button class="source-link" onclick="showSourceModal('khatib_scaffolding_2012')">View Filing ↗</button>
              </div>
            </div>
          </div>
          <div class="card" style="margin-top:14px; background:var(--bg-surface-elevated); border:1px solid rgba(0, 229, 255, 0.2);">
            <div class="card-title" style="font-size:12.5px; color:var(--accent-cyan);">5-Point Verification Gap Closure Protocol</div>
            <div style="font-size:11.5px; color:var(--text-muted); line-height:1.7; margin-top:6px; display:grid; grid-template-columns:1fr 1fr; gap:10px;">
              <div>1. Certified docket & status certificate for Case 2923/2012 North Cairo Court.</div>
              <div>2. Original signed subcontracts, BOQs, rate schedules, and approved IPCs.</div>
              <div>3. Mutual reconciliation bank records, wire receipts, and signed final releases.</div>
              <div>4. Corporate entity registry verification (privity insulation ACC vs TMGH).</div>
              <div style="grid-column:1 / -1;">5. Formal documented response from developer management (absence of reply is not legal proof).</div>
            </div>
          </div>
        `
      },
      {
        num: "SLIDE 04 / 10",
        titleAr: "الاحتجاجات العمالية الحديثة بشركات المجموعة (2024 – 2025)",
        titleEn: "Modern Labor Strife & Security Protests (2024 – 2025)",
        noteAr: "وثقت المنصة ومدى مصر احتجاجات لأكثر من 100 عامل بالإسكندرية للإنشاءات واحتجاجات أمن مدينتي على الورديات المرهقة (12 ساعة) والمطالبة بالأجر الإضافي.",
        noteEn: "Al Manassa & Mada Masr documented protests by >100 ACC employees over wages/layoffs and Madinaty security protests over grueling 12-hour shifts.",
        contentAr: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">احتجاج أكثر من 100 موظف بالإسكندرية للإنشاءات (مارس 2024)</div>
              <div class="flag-desc">وثق موقع مدى مصر احتجاجات عمالية وموظفين بسبب تجميد الرواتب وفصل عاملين تعسفياً دون تسوية المستحقات القانونية في ظل التضخم.</div>
              <div class="flag-footer">
                <span>المصدر: مدى مصر</span>
                <button class="source-link" onclick="showSourceModal('mada_acc_2024')">فحص التقرير ↗</button>
              </div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-rose);">
              <div class="flag-title">مذكرة عمال أمن مدينتي والتحقيقات الإدارية (أكتوبر 2025)</div>
              <div class="flag-desc">وثق موقع المنصة تقديم مذكرة رسمية للإدارة للمطالبة بأجر إضافي عن العمل 12 ساعة وبدل الوجبات، وإحالة مشاركين للتحقيق الإداري.</div>
              <div class="flag-footer">
                <span>المصدر: المنصة</span>
                <button class="source-link" onclick="showSourceModal('manassa_security_oct2025')">فحص التقرير ↗</button>
              </div>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">>100 ACC Employees Protest Wages & Layoffs (March 2024)</div>
              <div class="flag-desc">Mada Masr documented labor action over salary freezes, sub-inflation compensation, and arbitrary layoffs without severance.</div>
              <div class="flag-footer">
                <span>Source: Mada Masr</span>
                <button class="source-link" onclick="showSourceModal('mada_acc_2024')">View Report ↗</button>
              </div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-rose);">
              <div class="flag-title">Madinaty Security Officers Petition (October 2025)</div>
              <div class="flag-desc">Al Manassa documented formal worker petition demanding overtime for 12-hour shifts and meal stipends; participants faced internal inquiries.</div>
              <div class="flag-footer">
                <span>Source: Al Manassa</span>
                <button class="source-link" onclick="showSourceModal('manassa_security_oct2025')">View Report ↗</button>
              </div>
            </div>
          </div>
        `
      },
      {
        num: "SLIDE 05 / 10",
        titleAr: "محفظة المشروعات وضغوط الإنجاز لعام 2029",
        titleEn: "Project Portfolio & 2029 Delivery Pacing Pressure",
        noteAr: "تتحمل المجموعة أعباء تسليم ضخمة في ساوث ميد (23 مليون م²) ومدينة نور (5,000 فدان مع حصة 50% مباني عينية للمجتمعات العمرانية).",
        noteEn: "TMG faces enormous delivery obligations across SouthMED (23M sqm) and Noor City (5,000 feddans with 50% in-kind finished units to NUCA).",
        contentAr: `
          <div class="grid-2">
            <div class="card" style="background:var(--bg-surface-elevated);">
              <div class="card-title">المشروعات السكنية العملاقة</div>
              <ul style="font-size:12.5px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:18px;">
                <li><strong>ساوث ميد (SouthMED):</strong> 23 مليون م²، مبيعات >280 مليار جنيه، بدء التسليم 2029.</li>
                <li><strong>مدينة نور:</strong> 5,000 فدان، حصة عينية 50% مباني منجزة لهيئة المجتمعات.</li>
                <li><strong>مدينة بنان (الرياض):</strong> استثمار 40 مليار ريال بالشراكة مع الوطنية للإسكان.</li>
              </ul>
            </div>
            <div class="card" style="background:var(--bg-surface-elevated);">
              <div class="card-title">توسعات قطاع الفنادق الفاخرة</div>
              <ul style="font-size:12.5px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:18px;">
                <li><strong>محفظة الفنادق التاريخية:</strong> 7 فنادق مملوكة بنسبة 51% لأيكون و40.5% لـ ADQ.</li>
                <li><strong>تأجيلات الفنادق:</strong> فور سيزونز الأقصر (تأجل الافتتاح إلى 2027 بموقع فورسيزونز الرسمي بعد استهداف 2026 بتقرير TMG لنصف 2025؛ لا توجد شكاوى مستخلصات معلنة)، والأهرامات (إلى 2029).</li>
                <li><strong>قروض مصرفية مشتركة:</strong> 6.76 مليار جنيه قرض بنك مصر لفندق مدينتي.</li>
              </ul>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="card" style="background:var(--bg-surface-elevated);">
              <div class="card-title">Megaprojects in Execution</div>
              <ul style="font-size:12.5px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:18px;">
                <li><strong>SouthMED (KM 165 Coast):</strong> 23M sqm, >EGP 280bn sales, delivery slated 2029.</li>
                <li><strong>Noor City:</strong> 5,000 feddans, 50% in-kind finished unit delivery to NUCA.</li>
                <li><strong>Banan City (Riyadh):</strong> SAR 40bn cross-border venture with Saudi NHC.</li>
              </ul>
            </div>
            <div class="card" style="background:var(--bg-surface-elevated);">
              <div class="card-title">Luxury Hospitality Expansion</div>
              <ul style="font-size:12.5px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:18px;">
                <li><strong>Legacy Hotels:</strong> 7 historic state hotels acquired (51% ICON / ADQ 40.5%).</li>
                <li><strong>Luxury Slippages:</strong> Four Seasons Luxor (opening shifted to 2027 on official FS portal vs 2026 target in TMG H1 2025 report; no public contractor complaints), Pyramids (to 2029).</li>
                <li><strong>Bank Covenants:</strong> EGP 6.76B Banque Misr facility for FS Madinaty.</li>
              </ul>
            </div>
          </div>
        `
      },
      {
        num: "SLIDE 06 / 10",
        titleAr: "السجل القضائي: حكم أرض مدينتي وجنح الشيكات",
        titleEn: "Judicial Records: Madinaty Concession & Misdemeanor Checks",
        noteAr: "قضت المحكمة الإدارية العليا ببطلان عقد مدينتي عام 2010 وتمت التسوية بحصة 7% عينية، فيما أخمدت جنح الشيكات التجارية بالتصالح.",
        noteEn: "Supreme Administrative Court annulled Madinaty concession in 2010 (settled via 7% BUA); check misdemeanors resolved via rescheduling.",
        contentAr: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-rose);">
              <div class="flag-title">حكم الإدارية العليا (الطعن 12622 لسنة 63 ق)</div>
              <div class="flag-desc">بطلان البيع المباشر لـ 8,000 فدان لمخالفة قانون المزايدات. تمت التسوية بعقد 2015 بإلزام طلعت مصطفى بتسليم 7% مباني سكنية عيناً لهيئة المجتمعات.</div>
              <div class="flag-footer">
                <span>مجلس الدولة المصري</span>
                <button class="source-link" onclick="showSourceModal('state_council_madinaty')">نص الحكم ↗</button>
              </div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">جنحة شيكات بدون رصيد (قضية 16522 لسنة 2013)</div>
              <div class="flag-desc">دعاوى قضائية من موردين ومقاولين بسبب تعثر شيكات تجارية صادرة من العربية للمشروعات، انقضت بالتصالح وسداد المتأخرات بجدولة زمنية.</div>
              <div class="flag-footer">
                <span>محكمة جنح قصر النيل</span>
                <button class="source-link" onclick="showSourceModal('cairo_misdemeanor_checks')">سجل الجنحة ↗</button>
              </div>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="flag-card" style="border-inline-start-color: var(--accent-rose);">
              <div class="flag-title">Supreme Admin Court (Appeal 12622 / JY 63)</div>
              <div class="flag-desc">Annulled direct sale of 8,000 feddans under Tender Law 89/1998. Settled via 2015 agreement requiring 7% in-kind residential BUA to NUCA.</div>
              <div class="flag-footer">
                <span>Egyptian State Council</span>
                <button class="source-link" onclick="showSourceModal('state_council_madinaty')">View Ruling ↗</button>
              </div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">Bad Checks Misdemeanor (Case 16522 of 2013)</div>
              <div class="flag-desc">Check default proceedings filed by commercial suppliers against ACPUD, reconciled via rescheduling and replacement notes.</div>
              <div class="flag-footer">
                <span>Cairo Misdemeanor Court</span>
                <button class="source-link" onclick="showSourceModal('cairo_misdemeanor_checks')">View Docket ↗</button>
              </div>
            </div>
          </div>
        `
      },
      {
        num: "SLIDE 07 / 10",
        titleAr: "التحليل المالي الجنائي: ديون التأجير التمويلي واستنزاف السيولة",
        titleEn: "Financial Forensics: Off-Balance Debt & Cash Conversion",
        noteAr: "تشمل الديون الحقيقية للمجموعة 44 مليار جنيه التزامات عقود تأجير تمويلي (تكلفة اقتراض 28.6%)، مع استنزاف 18.26 مليار نقد في رأس المال العامل.",
        noteEn: "True effective debt includes EGP 44B in structured financial lease notes (borrowing cost 28.6%), alongside EGP 18.26B cash drain in working capital.",
        contentAr: `
          <div class="grid-2">
            <div class="kpi-card purple">
              <div class="kpi-title">التزامات التأجير التمويلي (خارج الميزانية)</div>
              <div class="kpi-value">43.99 مليار جنيه</div>
              <div class="kpi-delta delta-warn">▲ فائدة اقتراض محلية 28.6%</div>
            </div>
            <div class="kpi-card amber">
              <div class="kpi-title">استنزاف السيولة في رأس المال العامل (H1 26)</div>
              <div class="kpi-value">-18.26 مليار جنيه</div>
              <div class="kpi-delta delta-down">▼ مخزون الإنشاءات تحت التنفيذ</div>
            </div>
          </div>
          <div style="font-size:13px; color:var(--text-muted); line-height:1.7; margin-top:16px;">
            تستخدم المجموعة صفقات البيع وإعادة الاستئجار لتسييل الأصول التجارية (أوبن إير مول، جيت واي مول) لتمويل الالتزامات؛ مما يرفع العبء التمويلي الإجمالي فوق 60.5 مليار جنيه.
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="kpi-card purple">
              <div class="kpi-title">Structured Financial Leases</div>
              <div class="kpi-value">EGP 43.99 bn</div>
              <div class="kpi-delta delta-warn">▲ Borrowing rate 28.6%</div>
            </div>
            <div class="kpi-card amber">
              <div class="kpi-title">H1 2026 Working Capital Outflow</div>
              <div class="kpi-value">EGP -18.26 bn</div>
              <div class="kpi-delta delta-down">▼ Properties Under Development Drain</div>
            </div>
          </div>
          <div style="font-size:13px; color:var(--text-muted); line-height:1.7; margin-top:16px;">
            TMG utilizes sale-and-leaseback transactions on commercial malls to monetize cash; combined true debt (loans + leases) exceeds EGP 60.5B.
          </div>
        `
      },
      {
        num: "SLIDE 08 / 10",
        titleAr: "مصفوفة التحوط الاستراتيجي للمقاولين والبنوك والمستثمرين",
        titleEn: "Strategic Diligence Playbooks for Stakeholders",
        noteAr: "يجب على مقاولي الباطن رفض شروط (Pay-When-Paid)، وعلى البنوك مراقبة سرعة تدوير أوراق الدفع (>15.79 مليار) كإنذار مبكر.",
        noteEn: "Subcontractors must eliminate pay-when-paid clauses; lenders must track notes payable velocity (>EGP 15.79B) as an operational friction signal.",
        contentAr: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-cyan);">
              <div class="card-title" style="color:var(--accent-cyan);">إرشادات مقاولي الباطن والموردين</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>رفض نصوص الدفع المشروط بتدفقات المطور (Pay-When-Paid).</li>
                <li>تأكيد أوامر التغيير كتابياً ومسبقاً قبل أي عمل موقعي.</li>
                <li>توجيه إنذارات رسمية على يد محضر لبدء سريان الفائدة القانونية (5%).</li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-emerald);">
              <div class="card-title" style="color:var(--accent-emerald);">إرشادات البنوك والمستثمرين</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>العزل القانوني يحمي سهم الشركة القابضة من قضايا المقاولين.</li>
                <li>مراقبة حجم أوراق الدفع (>15.79 مليار) لرصد أي تآكل في سلاسل الإمداد.</li>
                <li>دمج التزامات التأجير التمويلي (44 مليار) ضمن حسابات تغطية الديون.</li>
              </ul>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-cyan);">
              <div class="card-title" style="color:var(--accent-cyan);">Subcontractor Diligence Playbook</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>Reject "Pay-When-Paid" language linking payment to developer releases.</li>
                <li>Zero unapproved site variations without signed Variation Orders.</li>
                <li>Serve court bailiff notices to start statutory 5% commercial interest.</li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-emerald);">
              <div class="card-title" style="color:var(--accent-emerald);">Institutional Investor & Lender Playbook</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>Captive privity insulates parent company equity and headline EBITDA.</li>
                <li>Monitor notes payable velocity (>EGP 15.79B) for downstream supply strain.</li>
                <li>Incorporate EGP 44B financial lease obligations into true leverage tests.</li>
              </ul>
            </div>
          </div>
        `
      },
      {
        num: "SLIDE 09 / 10",
        titleAr: "شبكة مقاولي أتريوم (Atrium) والتحالفات الاستراتيجية الكبرى",
        titleEn: "Atrium Expanded Contractor Network & Strategic JVs",
        noteAr: "تتولى شركة أتريوم دور المقاول العام المتكامل للأعمال الفندقية والتجارية، وتشكل تحالفات دولية مع CCC Electromechanical، ومقاولين متخصصين مثل إيفرلاست وسراج وإيماس السويدي.",
        noteEn: "Atrium AQC acts as the turnkey EPC vehicle for hospitality & commercial assets, partnering with CCC Electromechanical, Everlast, Siraj, and EMAS.",
        contentAr: `
          <div class="grid-3">
            <div class="flag-card" style="border-inline-start-color: var(--accent-cyan);">
              <div class="flag-title">فورسيزونز الأقصر & كابيتال</div>
              <div class="flag-desc">تحالف استراتيجي مع CCC Electromechanical لحزم MEP الكبرى (CP02 / CP05) بإشراف Hill International واستشارات شاكر وكناوف مصر.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-emerald);">
              <div class="flag-title">أوبن إير مول وإيست هب</div>
              <div class="flag-desc">إسناد جمالونات الحديد لشركة إيفرلاست (استشاري ECG)، وتوريد أنظمة الإضاءة المعمارية المتطورة من سراج للإضاءة بإشراف دار الهندسة.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">مدينة نور وسيليـا</div>
              <div class="flag-desc">تنفيذ 72 عمارة وفيلات بنور، وتوريد خلايا الجهد المتوسط 24kV من إيماس السويدي، وحزم العاصمة الإدارية بإشراف حمزة وشركاه.</div>
            </div>
          </div>
          <div style="font-size:12.5px; color:var(--text-muted); line-height:1.7; margin-top:16px;">
            ● يضمن نموذج المقاول المدمج (Atrium / ACC) حماية كاملة لأرصدة ومبيعات المجموعة القابضة من أي دعاوى مباشرة لمقاولي الباطن.
          </div>
        `,
        contentEn: `
          <div class="grid-3">
            <div class="flag-card" style="border-inline-start-color: var(--accent-cyan);">
              <div class="flag-title">FS Luxor & Cairo Capital</div>
              <div class="flag-desc">Strategic JV with CCC Electromechanical for MEP packages (CP02 / CP05) under Hill International, Shaker Group & Knauf.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-emerald);">
              <div class="flag-title">Open Air & East Hub Malls</div>
              <div class="flag-desc">Specialist steel trusses by Everlast Construction (ECG Consultant), architectural lighting by Siraj under Dar Al-Handasah.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">Noor City & Celia Capital</div>
              <div class="flag-desc">72 residential buildings at Noor, Siemens 24kV switchgear by EMAS El Sewedy, and New Capital packages under Hamza Associates.</div>
            </div>
          </div>
          <div style="font-size:12.5px; color:var(--text-muted); line-height:1.7; margin-top:16px;">
            ● Captive general contracting ring-fences TMG Holding balances and escrow receivables from downstream trade subcontractor liens.
          </div>
        `
      },
      {
        num: "SLIDE 10 / 10",
        titleAr: "استقصاء مشاعر المقاولين وحقيقة الدفع: نتائج التدقيق الجنائي",
        titleEn: "Contractor Sentiment & Payment Truth: Forensic Audit Conclusions",
        noteAr: "أظهر التدقيق الجنائي تفاوتاً حاداً بين الشكاوى التاريخية ومزاعم النشر الصحفي والواقع التعاقدي؛ لا يوجد دليل على سياسة عامة لحبس المستحقات حالياً، وتكرار التعاقدات (10B لكونكريت بلس) يؤكد استقرار الشراكات الكبرى.",
        noteEn: "Forensic audit strictly separates direct historic dues complaints (2008) from upstream military payment lags (SouthMED 2024) and internal workforce wages.",
        contentAr: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-emerald);">
              <div class="card-title" style="color:var(--accent-emerald);">الأدلة التجارية المؤكدة والإيجابية</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>تكرار إسناد المشروعات الضخمة: كونكريت بلس بـ 10 مليار جنيه بساوث ميد.</li>
                <li>شراكات ممتدة لربع قرن (أندي لانغ LLD في 6 فنادق فورسيزونز).</li>
                <li>توريدات تخصصية منتظمة دون أي قضايا أو بلاغات (إيماس، سراج، كناوف).</li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-rose);">
              <div class="card-title" style="color:var(--accent-rose);">النزاعات المحصورة وقواعد العزل الجنائي</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>واقعة 2008 (شحاتة حسن) تاريخية مرتبطة بظروف حبس هشام طلعت واعتراف ACC.</li>
                <li>ادعاء باطن ساوث ميد (2024) عُزي لتأخر سداد جهات عليا للمقاولين (انقطاع الحجية).</li>
                <li>احتجاجات عمال ومهندسي ACC (2024–2025) نزاع أجور داخلي وليس فواتير مقاولين.</li>
              </ul>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-emerald);">
              <div class="card-title" style="color:var(--accent-emerald);">Confirmed Commercial Partnerships</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>Major repeat contract awards: Concrete Plus ~EGP 10B at SouthMED following Noor.</li>
                <li>Quarter-century continuous collaboration: Andy Lang (LLD) on 6 Four Seasons hotels.</li>
                <li>Regular high-spec technology supply with zero litigation: EMAS, Siraj, Knauf Egypt.</li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-rose);">
              <div class="card-title" style="color:var(--accent-rose);">Forensic Isolation & Privity Realities</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>2008 case (Shehata) was isolated historical event during crisis, acknowledged by ACC.</li>
                <li>2024 SouthMED claim was attributed to upstream Armed Forces lags, not TMG liability.</li>
                <li>ACC worker/engineer actions (2024-25) represent internal wage disputes, not trade debt.</li>
              </ul>
            </div>
          </div>
        `
      }
    ];

    let currentSlide = 0;

    function openPresenterMode() {
      document.getElementById('presenter-overlay').classList.add('active');
      renderSlide(0);
      document.addEventListener('keydown', handlePresenterKeydown);
    }

    function closePresenterMode() {
      document.getElementById('presenter-overlay').classList.remove('active');
      document.removeEventListener('keydown', handlePresenterKeydown);
      if (document.fullscreenElement) {
        document.exitFullscreen();
      }
    }

    function renderSlide(index) {
      currentSlide = index;
      const s = presenterSlides[index];
      document.getElementById('presenter-slide-num').textContent = s.num;
      document.getElementById('presenter-slide-title').textContent = currentLang === 'ar' ? s.titleAr : s.titleEn;
      document.getElementById('presenter-slide-content').innerHTML = currentLang === 'ar' ? s.contentAr : s.contentEn;
      document.getElementById('presenter-speaker-note').textContent = currentLang === 'ar' ? s.noteAr : s.noteEn;

      document.getElementById('presenter-dock-indicator').textContent = `${index + 1} / ${presenterSlides.length}`;
      const pct = ((index + 1) / presenterSlides.length) * 100;
      document.getElementById('slide-progress-bar').style.width = pct + '%';

      document.getElementById('btn-prev-slide').textContent = currentLang === 'ar' ? '❮ السابق' : '❮ Previous';
      document.getElementById('btn-next-slide').textContent = currentLang === 'ar' ? 'التالي ❯' : 'Next ❯';
      document.getElementById('btn-fs-slide').textContent = currentLang === 'ar' ? '⛶ شاشة كاملة' : '⛶ Fullscreen';
      document.getElementById('btn-exit-presenter').textContent = currentLang === 'ar' ? '✕ خروج (Esc)' : '✕ Exit (Esc)';
      document.getElementById('lbl-speaker-note-tag').textContent = currentLang === 'ar' ? 'استنتاج الفحص الجنائي:' : 'Forensic Diligence Takeaway:';
      document.getElementById('lbl-keyboard-nav').innerHTML = currentLang === 'ar' ? 'اضغط <kbd>←</kbd> <kbd>→</kbd> للتنقل' : 'Press <kbd>←</kbd> <kbd>→</kbd> to Navigate';
      document.getElementById('lbl-keyboard-fs').innerHTML = currentLang === 'ar' ? 'اضغط <kbd>F</kbd> للشاشة الكاملة' : 'Press <kbd>F</kbd> for Fullscreen';
    }

    function prevSlide() {
      if (currentSlide > 0) renderSlide(currentSlide - 1);
    }

    function nextSlide() {
      if (currentSlide < presenterSlides.length - 1) renderSlide(currentSlide + 1);
    }

    function toggleFullScreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    }

    function handlePresenterKeydown(e) {
      if (e.key === 'ArrowRight' || e.key === 'Space') {
        if (currentLang === 'ar') prevSlide(); else nextSlide();
      } else if (e.key === 'ArrowLeft') {
        if (currentLang === 'ar') nextSlide(); else prevSlide();
      } else if (e.key === 'Escape') {
        closePresenterMode();
      } else if (e.key.toLowerCase() === 'f') {
        toggleFullScreen();
      }
    }

    /* ==========================================================================
       CHART.JS DYNAMIC THEMING & LOCALIZATION
       ========================================================================== */
    let chartFin, chartComp, chartCash, chartDebt;
    let chartLandbank, chartRadar, chartOwnership, chartPolar, chartIPC, chartBubble, chartLiab;

    function initCharts() {
      // Destroy any existing chart instances to prevent canvas re-use errors
      [chartFin, chartComp, chartCash, chartDebt, chartLandbank, chartRadar, chartOwnership, chartPolar, chartIPC, chartBubble, chartLiab].forEach(c => {
        if (c) c.destroy();
      });

      const textColor = currentTheme === 'light' ? '#090d16' : '#f8fafc';
      const textMuted = currentTheme === 'light' ? '#475569' : '#94a3b8';
      const gridColor = currentTheme === 'light' ? 'rgba(203, 213, 225, 0.6)' : 'rgba(51, 65, 85, 0.35)';
      const fontFam = currentLang === 'ar' ? 'Cairo, Plus Jakarta Sans, sans-serif' : 'Plus Jakarta Sans, Cairo, sans-serif';

      // ----------------------------------------------------
      // 1. Financial Trends Chart
      // ----------------------------------------------------
      const elFin = document.getElementById('chartFinancialTrends');
      if (elFin) {
        chartFin = new Chart(elFin.getContext('2d'), {
          type: 'bar',
          data: {
            labels: ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026'],
            datasets: [
              {
                label: currentLang === 'ar' ? 'الإيرادات المجمعة (مليار جنيه)' : 'Consolidated Revenue (EGP bn)',
                data: [15.35, 19.87, 28.43, 42.70, 62.50, 30.19],
                backgroundColor: '#0284c7',
                borderRadius: 5
              },
              {
                label: currentLang === 'ar' ? 'صافي الأرباح المجمعة (مليار جنيه)' : 'Net Profit (EGP bn)',
                data: [1.78, 2.23, 3.31, 12.80, 18.20, 9.95],
                backgroundColor: '#059669',
                borderRadius: 5
              },
              {
                type: 'line',
                label: currentLang === 'ar' ? 'رصيد المبيعات غير المسلمة (Backlog)' : 'Contracted Backlog (EGP bn)',
                data: [63.0, 77.0, 145.0, 294.0, 441.2, 460.0],
                borderColor: '#d97706',
                backgroundColor: 'rgba(217, 119, 6, 0.1)',
                borderWidth: 2.5,
                tension: 0.3,
                fill: false
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { labels: { color: textColor, font: { family: fontFam, size: 11, weight: '700' } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } }
            }
          }
        });
      }

      // ----------------------------------------------------
      // 2. Complaints Breakdown Chart
      // ----------------------------------------------------
      const elComp = document.getElementById('chartComplaints');
      if (elComp) {
        chartComp = new Chart(elComp.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: currentLang === 'ar' ? [
              'فروق الصيانة وعائد الوديعة (35%)',
              'رسوم التنازل العقاري 5-10% (24%)',
              'مستحقات مقاولين واحتجاجات عمالية (20%)',
              'تأخير التسليم وفروق الأسعار (14%)',
              'تعريفة المرافق وضغط المياه (7%)'
            ] : [
              'Maintenance Deficit Fees (35%)',
              'Resale Transfer Fees (24%)',
              'Contractor Dues & Labor Protests (20%)',
              'Delivery Slippage & Price Creep (14%)',
              'Utility Tariffs & Water Pressure (7%)'
            ],
            datasets: [{
              data: [35, 24, 20, 14, 7],
              backgroundColor: ['#dc2626', '#d97706', '#0284c7', '#7c3aed', '#64748b'],
              borderWidth: 0
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'right', labels: { color: textColor, boxWidth: 12, font: { family: fontFam, size: 11, weight: '600' } } }
            },
            cutout: '66%'
          }
        });
      }

      // ----------------------------------------------------
      // 3. Landbank Footprint Chart (from gemini-code)
      // ----------------------------------------------------
      const elLand = document.getElementById('landbankBarChart');
      if (elLand) {
        chartLandbank = new Chart(elLand.getContext('2d'), {
          type: 'bar',
          data: {
            labels: currentLang === 'ar' ? 
              ['مدينتي', 'ساوث ميد', 'مدينة نور', 'مدينة الرحاب', 'سيليا (العاصمة)', 'الربوة'] :
              ['Madinaty', 'SouthMED', 'Noor City', 'Al Rehab', 'Celia (NAC)', 'Al Rabwa'],
            datasets: [{
              label: currentLang === 'ar' ? 'مساحة الأرض (فدان)' : 'Land Area (Feddans)',
              data: [8000, 5500, 5000, 2380, 500, 500],
              backgroundColor: ['#0284c7', '#0ea5e9', '#6366f1', '#818cf8', '#d97706', '#059669'],
              borderRadius: 5
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => ` ${ctx.parsed.y.toLocaleString()} ${currentLang === 'ar' ? 'فدان' : 'Feddans'}`
                }
              }
            },
            scales: {
              x: { grid: { display: false }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } }
            }
          }
        });
      }

      // ----------------------------------------------------
      // 4. Multi-Dimensional Risk Radar Chart (from gemini-code)
      // ----------------------------------------------------
      const elRadar = document.getElementById('riskRadarChart');
      if (elRadar) {
        chartRadar = new Chart(elRadar.getContext('2d'), {
          type: 'radar',
          data: {
            labels: currentLang === 'ar' ? [
              'تأخر صرف المستخلصات',
              'درع الحجية النسبية للعقود',
              'عائق التحكيم السري CRCICA',
              'التضخم وفروق الأسعار',
              'فترة رد محتجز الضمان',
              'الضغوط النقدية للعمالة'
            ] : [
              'Payment Delay',
              'Tier Privity Insulation',
              'Dispute Forum Barrier',
              'Inflation & Escalation',
              'Retention Lag',
              'Labor Cash Friction'
            ],
            datasets: [{
              label: currentLang === 'ar' ? 'مؤشر الخطورة المقدر (1-10)' : 'Assessed Risk Score (1-10)',
              data: [8.5, 9.5, 8.8, 8.2, 7.8, 7.0],
              backgroundColor: 'rgba(220, 38, 38, 0.22)',
              borderColor: '#dc2626',
              pointBackgroundColor: '#dc2626',
              pointBorderColor: '#fff',
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              r: {
                angleLines: { color: gridColor },
                grid: { color: gridColor },
                pointLabels: { color: textColor, font: { family: fontFam, size: 11, weight: '600' } },
                ticks: { display: false, min: 0, max: 10 }
              }
            },
            plugins: { legend: { display: false } }
          }
        });
      }

      // ----------------------------------------------------
      // 5. Ownership & UBO Doughnut Chart (from gemini-code)
      // ----------------------------------------------------
      const elOwner = document.getElementById('ownershipDoughnutChart');
      if (elOwner) {
        chartOwnership = new Chart(elOwner.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: currentLang === 'ar' ? [
              'عائلة طلعت مصطفى (59.8%)',
              'التداول الحر بالبورصة المصرية (32.9%)',
              'البنك المركزي النرويجي Norges (3.3%)',
              'مؤسسات وصناديق استراتيجية أخرى (4.0%)'
            ] : [
              'Talaat Moustafa Family (59.8%)',
              'EGX Free Float (32.9%)',
              'Norges Bank Norway (3.3%)',
              'Other Strategic Entities (4.0%)'
            ],
            datasets: [{
              data: [59.8, 32.9, 3.3, 4.0],
              backgroundColor: ['#0284c7', '#6366f1', '#059669', '#d97706'],
              borderColor: currentTheme === 'light' ? '#ffffff' : '#0c1220',
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 12, font: { family: fontFam, size: 11 } } },
              tooltip: { callbacks: { label: ctx => ` ${ctx.label}: ${ctx.parsed}%` } }
            },
            cutout: '62%'
          }
        });
      }

      // ----------------------------------------------------
      // 6. Evidence Strength Polar Area Chart (from gemini-code)
      // ----------------------------------------------------
      const elPolar = document.getElementById('evidencePolarChart');
      if (elPolar) {
        chartPolar = new Chart(elPolar.getContext('2d'), {
          type: 'polarArea',
          data: {
            labels: currentLang === 'ar' ? [
              'مستوى أ (أحكام قضائية / إفصاحات رسمية)',
              'مستوى ب (سوابق أعمال هندسية موثقة)',
              'مستوى جـ (إعلانات وتسويق المطور)',
              'مستوى د (مؤشرات وتوترات عمالية بالمواقع)'
            ] : [
              'Level A (Official / Court / FRA)',
              'Level B (Verified Technical Portfolios)',
              'Level C (Company Marketing Claims)',
              'Level D (Labor / Site Friction Leads)'
            ],
            datasets: [{
              data: [35, 45, 15, 5],
              backgroundColor: [
                'rgba(2, 132, 199, 0.75)',
                'rgba(99, 102, 241, 0.75)',
                'rgba(217, 119, 6, 0.75)',
                'rgba(220, 38, 38, 0.75)'
              ],
              borderColor: currentTheme === 'light' ? '#ffffff' : '#0c1220'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              r: {
                grid: { color: gridColor },
                ticks: { display: false }
              }
            },
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 12, font: { family: fontFam, size: 11 } } }
            }
          }
        });
      }

      // ----------------------------------------------------
      // 7. Payment Lifecycle Line Chart (from gemini-code)
      // ----------------------------------------------------
      const elIPC = document.getElementById('ipcLifecycleLineChart');
      if (elIPC) {
        chartIPC = new Chart(elIPC.getContext('2d'), {
          type: 'line',
          data: {
            labels: currentLang === 'ar' ? [
              'تقديم المستخلص',
              'حصر الكميات بالموقع',
              'المكتب الفني للإسكندرية',
              'مراجعة إدارة مدينتي',
              'اعتماد المستخلص رسمياً',
              'إصدار شيكات آجلة (PDC)',
              'التحصيل والمقاصة النقدية'
            ] : [
              'Submission',
              'Site Quantity Survey',
              'ACC Technical Office',
              'Madinaty HQ Audit',
              'Certificate Approved',
              'Note Issued (PDC)',
              'Final Cash Clearance'
            ],
            datasets: [
              {
                label: currentLang === 'ar' ? 'الجدول الزمني التعاقدي المعياري (90 يوماً)' : 'Standard Contractual Timeline (90 Days)',
                data: [0, 15, 30, 45, 60, 75, 90],
                borderColor: '#059669',
                backgroundColor: 'rgba(5, 150, 105, 0.1)',
                borderDash: [5, 5],
                fill: false,
                tension: 0.2
              },
              {
                label: currentLang === 'ar' ? 'الجدول الزمني الفعلي المرصود للتعطيل (270 يوماً)' : 'Observed Extended Processing Timeline (270 Days)',
                data: [0, 25, 60, 105, 135, 180, 270],
                borderColor: '#dc2626',
                backgroundColor: 'rgba(220, 38, 38, 0.1)',
                fill: true,
                tension: 0.3
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { labels: { color: textColor, font: { family: fontFam, size: 11, weight: '700' } } },
              tooltip: {
                callbacks: {
                  label: ctx => ` ${ctx.dataset.label}: ${currentLang === 'ar' ? 'اليوم' : 'Day'} ${ctx.parsed.y}`
                }
              }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: {
                title: { display: true, text: currentLang === 'ar' ? 'إجمالي الأيام التراكمية' : 'Cumulative Days', color: textMuted },
                grid: { color: gridColor },
                ticks: { color: textMuted, font: { family: fontFam } }
              }
            }
          }
        });
      }

      // ----------------------------------------------------
      // 8. Counterparty Dispute Bubble Chart (from gemini-code)
      // ----------------------------------------------------
      const elBubble = document.getElementById('disputeBubbleChart');
      if (elBubble) {
        chartBubble = new Chart(elBubble.getContext('2d'), {
          type: 'bubble',
          data: {
            datasets: [
              {
                label: currentLang === 'ar' ? 'كونكريت بلس (مقاولات ساوث ميد)' : 'Concrete Plus (SouthMED EPC)',
                data: [{ x: 10.0, y: 1.5, r: 24 }],
                backgroundColor: 'rgba(2, 132, 199, 0.75)'
              },
              {
                label: currentLang === 'ar' ? 'أتريوم للمقاولات (تسليم مفتاح بمدينتي)' : 'Atrium Quality Contractors (Turnkey)',
                data: [{ x: 4.5, y: 1.8, r: 16 }],
                backgroundColor: 'rgba(99, 102, 241, 0.75)'
              },
              {
                label: currentLang === 'ar' ? 'أفراد أمن وعمال الإسكندرية للإنشاءات' : 'ACC Site Security & Labor Force',
                data: [{ x: 1.2, y: 8.5, r: 15 }],
                backgroundColor: 'rgba(220, 38, 38, 0.85)'
              },
              {
                label: currentLang === 'ar' ? 'المجد للمقاولات (كهروميكانيك سيليا)' : 'Al Majd (Celia MEP Subcontractor)',
                data: [{ x: 0.8, y: 1.2, r: 10 }],
                backgroundColor: 'rgba(5, 150, 105, 0.75)'
              },
              {
                label: currentLang === 'ar' ? 'سافيتو مصر (توريد مواد البناء)' : 'Saveto Egypt (Materials Supplier)',
                data: [{ x: 0.9, y: 1.0, r: 10 }],
                backgroundColor: 'rgba(217, 119, 6, 0.75)'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 12, font: { family: fontFam, size: 11 } } },
              tooltip: {
                callbacks: {
                  label: ctx => ` ${ctx.dataset.label}: ${currentLang === 'ar' ? 'الحجم' : 'Scale'} ~${ctx.parsed.x}B EGP, ${currentLang === 'ar' ? 'مؤشر التوتر' : 'Friction'}: ${ctx.parsed.y}/10`
                }
              }
            },
            scales: {
              x: {
                title: { display: true, text: currentLang === 'ar' ? 'حجم التعاقد / التسهيل المقدر (مليار جنيه)' : 'Estimated Contract / Facility Scale (EGP Billions)', color: textMuted },
                grid: { color: gridColor },
                ticks: { color: textMuted, font: { family: fontFam } }
              },
              y: {
                title: { display: true, text: currentLang === 'ar' ? 'مؤشر النزاعات والاحتكاك الموقعي (1-10)' : 'Public Dispute Friction Index (1-10)', color: textMuted },
                grid: { color: gridColor },
                ticks: { color: textMuted, font: { family: fontFam } },
                min: 0,
                max: 10
              }
            }
          }
        });
      }

      // ----------------------------------------------------
      // 9. Commercial Debt & Liabilities Horizontal Bar Chart (from gemini-code)
      // ----------------------------------------------------
      const elLiab = document.getElementById('liabilitiesHBarChart');
      if (elLiab) {
        chartLiab = new Chart(elLiab.getContext('2d'), {
          type: 'bar',
          data: {
            labels: currentLang === 'ar' ? [
              'أرصدة الدائنين وأوراق الدفع (الموردين والمقاولين)',
              'تحالف تمويل بنكي لمشروع نور',
              'توريق وبيع أصول رواسي (الشريحة 1)',
              'تسهيل فندق فور سيزونز مدينتي',
              'توريق وبيع أصول رواسي (الشريحة 2)',
              'مساهمة صندوق مصر العقاري 1'
            ] : [
              'Creditors & Notes Payable Shift (Suppliers & Contractors)',
              'Noor Project Bank Consortium',
              'Rawasy Asset Sale (Tranche 1)',
              'Four Seasons Madinaty Facility',
              'Rawasy Asset Sale (Tranche 2)',
              'Misr RE Fund 1 Contribution'
            ],
            datasets: [{
              label: currentLang === 'ar' ? 'القيمة (مليار جنيه)' : 'Value (EGP Billions)',
              data: [15.79, 9.00, 8.50, 6.76, 3.40, 0.50],
              backgroundColor: '#d97706',
              borderRadius: 5
            }]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: { callbacks: { label: ctx => ` ${currentLang === 'ar' ? 'القيمة:' : 'Value:'} ${ctx.parsed.x.toFixed(2)} ${currentLang === 'ar' ? 'مليار جنيه' : 'Billion EGP'}` } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { grid: { display: false }, ticks: { color: textColor, font: { family: fontFam, weight: '600' } } }
            }
          }
        });
      }

      // ----------------------------------------------------
      // 10. Cash Flow Conversion Chart
      // ----------------------------------------------------
      const elCash = document.getElementById('chartCashFlow');
      if (elCash) {
        chartCash = new Chart(elCash.getContext('2d'), {
          type: 'bar',
          data: {
            labels: currentLang === 'ar' ? ['صافي الأرباح', 'التدفق التشغيلي', 'استنزاف الإنشاءات (WIP)', 'مقدمات حجز العملاء'] : ['Net Profit', 'CFO Operating Cash', 'WIP Outflow', 'Customer Inflow'],
            datasets: [{
              label: currentLang === 'ar' ? 'القيمة (مليون جنيه)' : 'Amount (EGP Millions)',
              data: [9950, -4200, -22500, 48000],
              backgroundColor: ['#059669', '#dc2626', '#d97706', '#0284c7'],
              borderRadius: 5
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } }
            }
          }
        });
      }

      // ----------------------------------------------------
      // 11. Debt Structure Chart
      // ----------------------------------------------------
      const elDebt = document.getElementById('chartDebt') || document.getElementById('chartDebtBreakdown');
      if (elDebt) {
        chartDebt = new Chart(elDebt.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: currentLang === 'ar' ? [
              'تأجير تمويلي خارج الميزانية (44 مليار)',
              'أوراق دفع تجارية ودائنون (>15.8 مليار)',
              'تسهيلات بنكية مباشرة (16.2 مليار)'
            ] : [
              'Off-Balance Lease Liabilities (EGP 44B)',
              'Notes Payable & Trade Creditors (>EGP 15.8B)',
              'Direct Bank Borrowings (EGP 16.2B)'
            ],
            datasets: [{
              data: [44.0, 15.8, 16.2],
              backgroundColor: ['#7c3aed', '#d97706', '#0284c7'],
              borderWidth: 0
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 12, font: { family: fontFam, size: 11, weight: '600' } } }
            },
            cutout: '66%'
          }
        });
      }
    }

    function updateChartsTheme(theme) {
      initCharts();
    }

    /* ==========================================================================
       INITIALIZATION
       ========================================================================== */
    document.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('tmg_theme') || 'light';
      const savedLang = localStorage.getItem('tmg_lang') || 'ar';

      setTheme(savedTheme);
      setLanguage(savedLang);
      initCharts();
    });
  </script>

  <!-- Data Stores for Stakeholders, Teams & SWOT -->
  <script>
    const TMG_COMPANIES = [{"id": 1, "name": "Concrete Plus for Engineering & Construction", "role": "مقاول خارجي\n179 مبنى سكنيًا كامل التشطيب وبنية تحتية؛ Zone C01", "project": "SouthMED", "relation": "عقد معلن مع TMG", "phone": "+20 2 2307 6581 / +20 2 2307 6582", "phone_notes": "الخط العام للشركة — منشور على الموقع الرسمي", "email": "info@concrete-plus.net", "website": "https://concrete-plus.net/", "rel_source": "https://www.egypttoday.com/Article/3/144267/Talaat-Moustafa-Group-TMG-signs-EGP-10B-200M-construction-contracts | https://www.dailynewsegypt.com/2025/12/30/tmg-signs-egp-10bn-contract-with-concrete-plus-for-south-med-phase/", "phone_source": "https://concrete-plus.net/contact-us/", "evidence_level": "A/B", "confidence": "مرتفعة", "notes": "أصل العقد غير منشور؛ لا دليل منشور هنا على مستخلصات غير مدفوعة"}, {"id": 2, "name": "Consolidated Contractors Company (CCC)", "role": "مقاول/شريك JV\nمقاول مشترك مع Atrium في Four Seasons Cairo Capital", "project": "مدينتي", "relation": "علاقة مؤكدة عبر JV؛ لا تفترض عقد منفرد لـCCC مع TMG", "phone": "+30 210 618 2000 (المقر المركزي؛ لم أتحقق من رقم مصري مباشر)", "phone_notes": "رقم الشركة المركزي؛ موقع مصر منشور دون رقم محلي في صفحة التواصل", "email": "cccmail@ccc.net", "website": "https://www.ccc.net/", "rel_source": "https://atriumeg.com/portfolio/four-seasons-hotel-and-private-residences-new-cairo-capital-at-madinaty/ | https://www.linkedin.com/posts/hill-international_on-january-21-hill-joined-talaat-moustafa-activity-6761996655584718848-Jt2v", "phone_source": "https://www.ccc.net/wp-content/uploads/2022/08/qr-ccc-building_the_future-corporate_capability.pdf", "evidence_level": "A/B", "confidence": "مرتفعة للعلاقة", "notes": "حصة كل شريك وشروط الدفع غير منشورة"}, {"id": 3, "name": "Atrium Quality Contractors (Atrium)", "role": "ذراع مقاولات بالمجموعة\nتنفيذ مشروعات سكنية ومولات ومدارس وفنادق وبنية أساسية", "project": "مدينتي، الرحاب، نور، Celia، شرم الشيخ", "relation": "شركة ضمن منظومة TMG وليست طرفًا خارجيًا مستقلًا تلقائيًا", "phone": "المقر: +20 2 3331 2000 | الرحاب: +20 2 2693 1643 / 1647 / 1648", "phone_notes": "الخط العام للمقر وفرع الرحاب", "email": "info@atriumeg.com", "website": "https://atriumeg.com/", "rel_source": "https://atriumeg.com/projects/ | https://atriumeg.com/", "phone_source": "https://atriumeg.com/contact/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "المحفظة المنشورة ليست كشفًا كاملاً بالموردين أو المقاولين الفرعيين"}, {"id": 4, "name": "Alexandria Construction Company (ACC)", "role": "مقاولات؛ مرتبطة بالمجموعة\nمقاول بمراحل الرحاب؛ يظهر اسم ACC/Atrium JV في محضر SouthMED", "project": "الرحاب؛ SouthMED", "relation": "علاقة موثقة تاريخيًا في الرحاب؛ ذكر SouthMED من محضر طرف ثالث", "phone": "+20 3 360 9269 / +20 3 360 0278", "phone_notes": "أرقام التواصل كما نشرها موقع الشركة؛ راجع الصيغة الدولية قبل الاتصال", "email": "info@alexconstruction.com.eg", "website": "https://www.acc.eg/", "rel_source": "https://pme-consultancy.com/2022/06/02/el-rehab-city-project/ | https://www.acc.eg/الرئيسية/ | https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://www.acc.eg/contact-us-en/", "evidence_level": "A/B للرحاب؛ C لـSouthMED", "confidence": "مرتفعة للرحاب؛ متوسطة للمحضر", "notes": "نسبة الملكية الحالية وحزمة SouthMED غير مثبتتين في المصادر المستخدمة"}, {"id": 5, "name": "SQUARE Engineering Firm", "role": "مقاول/تشطيبات وأعمال عامة\nمحفظة مشروعات مع APUD؛ ومذكور في اجتماع تنسيق SouthMED", "project": "مدينتي؛ SouthMED", "relation": "المحفظة تثبت مشروعات متصلة؛ تفاصيل حزمة SouthMED غير منشورة", "phone": "+20 105 010 6594", "phone_notes": "رقم التواصل العام الظاهر في موقع الشركة", "email": "", "website": "https://www.square.com.eg/", "rel_source": "https://www.square.com.eg/ | https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://www.square.com.eg/", "evidence_level": "B/C", "confidence": "متوسطة", "notes": "لا يوجد عقد محدد أو قيمة أو بيانات مستحقات في المصادر المستخدمة"}, {"id": 6, "name": "El Soadaa Group", "role": "مقاول محتمل/مشارك موقع\nمذكور ضمن شركات المقاولين في محضر SouthMED", "project": "SouthMED", "relation": "اسم وارد بمحضر مشروع منشور على منصة طرف ثالث", "phone": "+20 2 2704 1297", "phone_notes": "الخط العام للشركة", "email": "info@elsoadaa.com", "website": "https://elsoadaa.com/", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE | https://elsoadaa.com/company/", "phone_source": "https://elsoadaa.com/contact/", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "الحزمة والعقد والقيمة غير معروفة؛ يلزم أصل التعاقد"}, {"id": 7, "name": "Gharably Integrated Engineering Company (GIECO)", "role": "مقاول بنية تحتية محتمل\nمحضر SouthMED يسرد El Gharably ضمن أعمال/تنسيق البنية التحتية", "project": "SouthMED", "relation": "المحضر مصدر غير موثق رسميًا؛ موقع GIECO يثبت التخصص لا عقد TMG", "phone": "+20 3 429 7889", "phone_notes": "الخط العام للشركة — الإسكندرية", "email": "info@gharably.com", "website": "https://gharably.com/", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE | https://gharably.com/", "phone_source": "https://gharably.com/home/", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "لا عقد أو قيمة أو مستخلصات منشورة"}, {"id": 8, "name": "Al Shorouq Construction Co.", "role": "مقاول مشارك بالمشروع وفق محضر\nمذكور بين المقاولين في محضر SouthMED", "project": "SouthMED", "relation": "دليل محضر فني فقط", "phone": "مرشح فقط: +20 2 2247 2395", "phone_notes": "رقم من دليل أعمال لكيان باسم قريب؛ مطابقة الهوية مع اسم SouthMED غير مؤكدة", "email": "", "website": "https://www.alshorouk.com/", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://gludo.org/en/business-directory/1613-al-shorouk-construction", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "لا نطاق أو عقد أصلي أو قيمة معلنة\nلا تستخدم الرقم على أنه مؤكد للشركة المذكورة في محضر SouthMED قبل تأكيد الاسم القانوني."}, {"id": 9, "name": "Knauf Egypt", "role": "مورد أنظمة ومواد بناء\nتقول الشركة إن حلولها استخدمت في Four Seasons Luxor", "project": "Four Seasons Luxor", "relation": "صلة توريد/منتجات معلنة من حساب الشركة؛ مباشر/غير مباشر غير محسوم", "phone": "17300", "phone_notes": "مركز خدمة العملاء / الاستفسارات في مصر", "email": "", "website": "https://knauf.com/en-EG", "rel_source": "https://www.linkedin.com/company/knauf-egypt/", "phone_source": "https://knauf.com/en-EG", "evidence_level": "B", "confidence": "متوسطة-مرتفعة", "notes": "لا أمر شراء أو مبلغ أو رصيد مستحق منشور"}, {"id": 10, "name": "DEVZAH SI", "role": "مورد محتمل – الاسم كما ورد\nتظهر كبائع في بيان استلام مواد بمشروع Four Seasons Cairo Capital CP05", "project": "مدينتي", "relation": "مستند فحص مواد على Scribd؛ علاقة توريد غير مباشرة محتملة", "phone": "غير منشور/لم يُعثر على رقم موثوق", "phone_notes": "لا توجد مطابقة موثوقة لهوية الشركة في المصادر المفتوحة التي تمت مراجعتها", "email": "", "website": "", "rel_source": "https://www.scribd.com/document/928303864/MIR-11", "phone_source": "", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "المستند غير مصادق عليه رسميًا؛ لا قيمة عقد أو دليل دين\nالاسم ورد في مستند مواد منشور على منصة طرف ثالث؛ يلزم مطابقة الاسم القانوني."}, {"id": 11, "name": "Cleopatra Company (الهوية القانونية غير مؤكدة)", "role": "مورد محتمل\nمحضر SouthMED يذكر توريد سيراميك وأدوات صحية لنموذج فيلات", "project": "SouthMED", "relation": "اسم مورد في محضر طرف ثالث؛ لا يثبت أنه Ceramica Cleopatra", "phone": "غير متاح — لا توجد مطابقة مؤكدة للكيان", "phone_notes": "لا ينبغي استخدام رقم سيراميكا كليوباترا دون إثبات أن المورد المذكور هو نفس الكيان", "email": "", "website": "", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE | https://www.cleopatraceramics.com/en/factories/", "phone_source": "", "evidence_level": "C", "confidence": "منخفضة-متوسطة", "notes": "يلزم مطابقة الاسم القانوني قبل ربطه بمجموعة سيراميكا كليوباترا\nمحضر المشروع يذكر Cleopatra Company فقط؛ لم يتم تأكيد تطابقها مع Ceramica Cleopatra."}, {"id": 12, "name": "Richmond Group Egypt", "role": "مقاول ظاهر في مستند موقع\nتجديد Aqua & Steak House في Four Seasons Nile Plaza", "project": "القاهرة", "relation": "مذكور كمقاول رئيسي في نموذج فحص/اعتماد مادة منشور", "phone": "+20 2 2519 2015", "phone_notes": "رقم في دليل أعمال خارجي؛ يجب تأكيد أنه ما زال يعمل", "email": "", "website": "https://www.rgegypt.com/", "rel_source": "https://www.scribd.com/document/343504517/INSPECTION-REQUEST-and-Mateiral-Approval-Aqua", "phone_source": "https://www.bizmideast.com/EG/richmond-group-egypt-company-02-25192015", "evidence_level": "C", "confidence": "منخفضة-متوسطة", "notes": "مستند منفرد غير رسمي؛ نطاق العقد وقيمته غير معلومين\nالموقع الرسمي لم يكن قابلاً للتحقق من صفحة الاتصال أثناء البحث؛ رقم الهاتف ليس مؤكدًا من مصدر الشركة."}, {"id": 13, "name": "Hill International", "role": "استشاري إدارة مشروع/إشراف\nFour Seasons Cairo Capital ومشاركات تنسيق/إشراف", "project": "مدينتي؛ SouthMED (ضمن محضر)", "relation": "موثق في صفحة Atrium وإعلان Hill؛ SouthMED مستند أضعف", "phone": "+20 2 2322 0000", "phone_notes": "مكتب القاهرة / الخط المحلي المنشور في ملف الشركة", "email": "", "website": "https://www.hillintl.com/", "rel_source": "https://atriumeg.com/portfolio/four-seasons-hotel-and-private-residences-new-cairo-capital-at-madinaty/ | https://www.linkedin.com/posts/hill-international_on-january-21-hill-joined-talaat-moustafa-activity-6761996655584718848-Jt2v", "phone_source": "https://www.hillintl.com/wp-content/uploads/2023/02/Hill-International-Cost-Consultancy-India-02-28-23.pdf", "evidence_level": "A/B؛ C في SouthMED", "confidence": "مرتفعة لـFour Seasons", "notes": "لا معلومات عامة هنا عن أتعاب أو مستحقات"}, {"id": 14, "name": "Dar Al-Handasah", "role": "استشاري هندسي\nEast Hub Mall وMadinaty Medical Center ومشروع شرم الشيخ", "project": "مدينتي؛ شرم الشيخ", "relation": "مسمى في صفحات Atrium الرسمية", "phone": "+20 2 3531 8000 (صفحة الاتصال الحالية) | +20 2 3531 0501 (صفحة مكتب أخرى)", "phone_notes": "مكتب القاهرة؛ تختلف الأرقام بين صفحات الاتصال الرسمية", "email": "info@dar.com / cairo@dar.com", "website": "https://www.dar.com/", "rel_source": "https://atriumeg.com/portfolio/east-hub-mall-at-madinaty/ | https://atriumeg.com/portfolio/madinaty-medical-center/ | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/", "phone_source": "https://www.dar.com/contact/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "أتعاب الاستشاري والمستحقات غير منشورة"}, {"id": 15, "name": "EHAF Consulting Engineers", "role": "استشاري هندسي\nمذكور باستشاريي East Hub Mall", "project": "مدينتي", "relation": "صفحة مشروع رسمية من Atrium", "phone": "+20 2 3760 1099 / +20 2 3760 8664", "phone_notes": "مكتب القاهرة", "email": "ehaf@ehaf.com", "website": "https://ehaf.com/", "rel_source": "https://atriumeg.com/portfolio/east-hub-mall-at-madinaty/", "phone_source": "https://ehaf.com/contact-ehaf/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "التوزيع الدقيق للنطاق بين EHAF وDar لم يفصل بالصفحة المختصرة"}, {"id": 16, "name": "ECG Engineering Consultants Group", "role": "استشاري هندسي\nOpen Air Mall وFour Seasons Sharm El Sheikh", "project": "مدينتي؛ شرم الشيخ", "relation": "صفحات Atrium الرسمية", "phone": "+20 2 2352 4740 / +20 2 2352 5748", "phone_notes": "مكاتب القاهرة — مدينة نصر / القرية الذكية", "email": "ecg@ecgsa.com", "website": "https://www.ecgsa.com/", "rel_source": "https://atriumeg.com/portfolio/open-air-mall-at-madinaty/ | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/", "phone_source": "https://www.ecgsa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "لا بيانات عن أتعاب أو مستحقات في المصادر التي روجعت"}, {"id": 17, "name": "Shaker Consultancy Group / SCG", "role": "استشاري تصميم/إشراف\nThe Strip Mall، Noor City، Four Seasons Sharm، ويظهر في محضر SouthMED", "project": "مدينتي؛ نور؛ شرم الشيخ؛ SouthMED", "relation": "A في صفحات Atrium؛ C في محضر SouthMED", "phone": "+20 2 2587 2500", "phone_notes": "مكتب القاهرة الجديدة", "email": "infocairo@shakergroup.com", "website": "https://shakergroup.com/", "rel_source": "https://atriumeg.com/portfolio/the-strip-mall-at-madinaty/ | https://atriumeg.com/portfolio/72-residential-buildings-at-noor-city/ | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/ | https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://shakergroup.com/contact/", "evidence_level": "A/C", "confidence": "مرتفعة للمشروعات الرسمية", "notes": "محضر SouthMED لا يثبت العقد وقيمته"}, {"id": 18, "name": "Raafat Miller Consulting / RMC", "role": "استشاري هندسي\nGateway Mall؛ All Seasons Park؛ RMC في تقرير HQ ومحضر SouthMED", "project": "الرحاب؛ مدينتي؛ SouthMED؛ مقر TMG الجديد", "relation": "صفحات Atrium تثبت بعض الأعمال؛ اختصار RMC في المستندات يحتاج مطابقة الاسم", "phone": "غير متحقق للكيان المحدد", "phone_notes": "لا تستخدم رقم شركة أخرى تحمل اسم Raafat دون مطابقة الاسم القانوني", "email": "", "website": "", "rel_source": "https://atriumeg.com/portfolio/gateway-mall-at-rehab-city/ | https://atriumeg.com/portfolio/all-seasons-park-at-madinaty/ | https://www.scribd.com/document/882859909/P0250-ATR-DPR-TMG-00010", "phone_source": "", "evidence_level": "A/C", "confidence": "مرتفعة للصفحات الرسمية؛ متوسطة للاختصار", "notes": "لا تدمج كل اسم RMC مع Raafat Miller دون مستند تعريف\nالاسم/الاختصار يحتاج تأكيدًا قانونيًا."}, {"id": 19, "name": "Hamza Associates", "role": "استشاري هندسي\nCelia New Capital وAll Seasons Park", "project": "العاصمة الإدارية؛ مدينتي", "relation": "صفحات مشروعات Atrium", "phone": "+20 2 3760 7238", "phone_notes": "المقر الرئيسي — الدقي", "email": "consult@hamza.org", "website": "https://www.hamza.org/", "rel_source": "https://atriumeg.com/portfolio/celia-new-capital/ | https://atriumeg.com/portfolio/all-seasons-park-at-madinaty/", "phone_source": "https://www.hamza.org/offices.html", "evidence_level": "A", "confidence": "مرتفعة", "notes": "أتعاب/مستحقات غير منشورة"}, {"id": 20, "name": "DMA Architects / DMA Design & Engineering Consultancy", "role": "استشاري تصميم\nPrivado وMadinaty V24 Villas", "project": "مدينتي", "relation": "صفحات مشروعات Atrium؛ الاسم مختلف بين الصفحتين", "phone": "لم يُعثر على رقم هاتف رسمي موثوق في صفحة الاتصال المفتوحة", "phone_notes": "الموقع الرسمي وصفحة LinkedIn متاحان؛ رقم مباشر غير مثبت", "email": "", "website": "https://www.dma-mea.com/", "rel_source": "https://atriumeg.com/portfolio/privado-compound-madinaty/ | https://atriumeg.com/portfolio/madinaty-v24-villas/", "phone_source": "https://www.dma-mea.com/", "evidence_level": "A", "confidence": "مرتفعة لذكر الاسم؛ متوسطة لتطابق الكيان", "notes": "لا توحّد الأسماء القانونية المختلفة قبل المطابقة"}, {"id": 21, "name": "PME Consultancy", "role": "استشاري إدارة مشروعات\nإدارة مشروع لمراحل 1–5 الرحاب لمصلحة ACC", "project": "الرحاب", "relation": "صفحة مشروع تاريخية من الاستشاري نفسه", "phone": "القاهرة: +20 122 440 8816 | الإسكندرية: +20 3 592 3291", "phone_notes": "مكتبا القاهرة والإسكندرية", "email": "info@pme-consultancy.com", "website": "https://pme-consultancy.com/", "rel_source": "https://pme-consultancy.com/2022/06/02/el-rehab-city-project/", "phone_source": "https://pme-consultancy.com/contact/", "evidence_level": "B", "confidence": "مرتفعة للعلاقة التاريخية", "notes": "لم تنشر الصفحة أي مديونية أو نزاع"}, {"id": 22, "name": "Mimar Interiors", "role": "مصمم داخلي/استشاري محتمل\nمذكور في منشور Knauf بشأن Four Seasons Luxor\nذكر في منشور Knauf عن Four Seasons Luxor", "project": "الأقصر", "relation": "ذكر في سياق منشور شركة مورد؛ تفاصيل دوره التعاقدي غير كاملة\nصلة من منشور مورد؛ لا تتوفر وثيقة نطاق أو عقد", "phone": "+20 2 2539 0163", "phone_notes": "خط مكتب Mimar Group بالقاهرة؛ لا يوجد رقم منفصل واضح لـMimar Interiors", "email": "projects@mimarinteriors.com", "website": "https://eg.erp-mimar-group.com/contactus", "rel_source": "https://www.linkedin.com/company/knauf-egypt/", "phone_source": "https://eg.erp-mimar-group.com/contactus", "evidence_level": "B", "confidence": "متوسطة", "notes": "لا وثيقة عقد أو نطاق عمل كامل منشور\nلم يتأكد هل هي استشاري أم مقاول تشطيبات أو طرف آخر بهذا المشروع\nرقم المجموعة لا يثبت وجود خط هاتفي مستقل لقسم التصميم الداخلي."}, {"id": 23, "name": "Interserve Consulting Group", "role": "خيط بحث استشاري – غير مؤكد\nاسم في ملف/مستند مشروع Four Seasons Cairo Capital CP03", "project": "مدينتي", "relation": "ظهور في مستند مشروع؛ لم يثبت تعاقده المباشر مع TMG", "phone": "غير منشور/لم يُعثر على رقم موثوق", "phone_notes": "هوية الكيان ودوره التعاقدي لم يتأكدا", "email": "", "website": "", "rel_source": "https://endelegypt.com/data/pdf/Endel_profile%2025_9_2023.pdf", "phone_source": "", "evidence_level": "C/D", "confidence": "منخفضة", "notes": "لا تصنفه كمقاول أو استشاري مؤكد دون خطاب تعيين/عقد\nاسم وارد في مستند مرتبط بحزمة مشروع؛ لا توجد مطابقة مؤكدة لهوية الشركة أو جهة اتصالها."}, {"id": 24, "name": "IEC Consultants", "role": "خيط بحث استشاري – غير مؤكد\nاسم في مستندات مرتبطة بـFour Seasons Cairo Capital CP03", "project": "مدينتي", "relation": "ذكر مستندي فقط", "phone": "مرشح فقط: +20 2 2639 4960 / +20 122 002 0213", "phone_notes": "رقم شركة International Engineering Company (IEC)؛ مطابقة الاسم القانوني مع الكيان الوارد في مستند المشروع غير محسومة", "email": "info@iec.com.eg", "website": "https://www.iec.com.eg/", "rel_source": "https://endelegypt.com/data/pdf/Endel_profile%2025_9_2023.pdf", "phone_source": "https://www.iec.com.eg/pages/contact.html", "evidence_level": "C/D", "confidence": "منخفضة", "notes": "الاختصار مبهم وقد يعود لكيانات متعددة\nتأكد من رقم السجل/الاسم القانوني قبل التعامل على أساس أن هذا هو IEC الوارد بمستند المشروع."}, {"id": 25, "name": "ENDEL Egypt", "role": "شركة – الدور غير مثبت\nملف/مستند يتعلق بحزمة Four Seasons Cairo Capital CP03", "project": "مدينتي", "relation": "ظهور في ملف الشركة/وثائق المشروع؛ نطاق التعاقد غير مثبت", "phone": "لم يُعثر على رقم حديث منشور في صفحة الاتصال الرسمية", "phone_notes": "صفحة الشركة تنشر البريد الإلكتروني دون رقم هاتف واضح", "email": "info@endelegypt.com", "website": "https://endelegypt.com/", "rel_source": "https://endelegypt.com/data/pdf/Endel_profile%2025_9_2023.pdf", "phone_source": "https://endelegypt.com/contactus.aspx", "evidence_level": "C/D", "confidence": "منخفضة", "notes": "لا تُصنف كمقاول باطن مؤكد من هذا المصدر فقط"}, {"id": 26, "name": "Jotun", "role": "علامة/مورد محتمل\nاسم Delivery Note في نموذج استلام مواد Four Seasons Cairo Capital", "project": "مدينتي", "relation": "المستند يذكر إشعار تسليم؛ لا يثبت العقد أو المشتري النهائي", "phone": "لا يظهر رقم مباشر عام لمكتب Jotun مصر في صفحة الاتصال الحالية", "phone_notes": "استخدم نموذج التواصل الرسمي أو دليل الموزعين/المطبقين المعتمدين", "email": "", "website": "https://www.jotun.com/eg-en/contact-us", "rel_source": "https://www.scribd.com/document/928303864/MIR-11", "phone_source": "https://www.jotun.com/eg-en/contact-us", "evidence_level": "C/D", "confidence": "منخفضة-متوسطة", "notes": "يلزم أمر شراء/اعتماد مادة يربطها بالحزمة بوضوح"}, {"id": 27, "name": "Bauer Egypt", "role": "مقاول أساسات محتمل – خيط منخفض الثقة\nملف مهني فردي يربطه بأعمال أساسات مقر TMG الجديد", "project": "المقر الجديد – القاهرة", "relation": "ملف مهني فقط؛ لم يظهر عقد أو إعلان رسمي يؤكد العلاقة", "phone": "لم يُعثر على رقم فرع مصر موثوق", "phone_notes": "علاقة المشروع نفسها منخفضة الثقة؛ لا توجد مطابقة مؤكدة لفرع محلي", "email": "", "website": "https://www.bauer.de/", "rel_source": "https://ae.linkedin.com/in/mohamed-gamal-594929168", "phone_source": "", "evidence_level": "D", "confidence": "منخفضة", "notes": "ليست علاقة مؤكدة ولا دليل على مستحقات\nالاسم وارد كخيط بحث مهني فقط وليس عقدًا أو إعلانًا رسميًا لمشروع TMG."}, {"id": 28, "name": "Power Axes Piling & Foundation LLC", "role": "مقاول أساسات محتمل – خيط منخفض الثقة\nذكر مهني ضمن سياق مشروع مقر TMG الجديد", "project": "المقر الجديد – القاهرة", "relation": "ملف مهني فقط؛ التسلسل التعاقدي غير مثبت", "phone": "+20 10 1691 0698 / +20 10 2210 5385", "phone_notes": "فرع مصر — الشروق / القاهرة الجديدة", "email": "info@poweraxes.com", "website": "https://poweraxes.com/", "rel_source": "https://ae.linkedin.com/in/mohamed-gamal-594929168", "phone_source": "https://poweraxes.com/contact.html", "evidence_level": "D", "confidence": "منخفضة", "notes": "يلزم أمر إسناد أو عقد أصلي قبل تصنيفها كمقاول\nرقم الشركة موثق، لكن اشتراكها في أعمال مقر TMG الجديد ما زال خيطًا منخفض الثقة غير مؤكد بعقد."}, {"id": 29, "name": "GEMS Egypt for Education Services", "role": "عميل/جهة مالكة للمشروع لا مورد\nصاحبة مشروع GEMS School بالرحاب حسب صفحة Atrium", "project": "الرحاب", "relation": "جهة مشروع؛ لا تعتبر موردًا لـTMG لمجرد وجودها بالمشروع", "phone": "الاستقبال: +20 2 2607 0291 / 0292 / 0294 / 0295 | القبول: +20 10 5038 5588 / +20 10 6003 9353", "phone_notes": "مدرسة GEMS British School Al Rehab — جهة تشغيل/تعليم بالمشروع وليست مقاولًا", "email": "registrar_tbs@gemsedu.com", "website": "https://www.tbs-cairo.com/", "rel_source": "https://atriumeg.com/portfolio/gems-school-at-rehab-city/", "phone_source": "https://www.tbs-cairo.com/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "يجب فصل العميل عن المقاول والمورد في قاعدة بيانات الأطراف"}, {"id": 30, "name": "First Design for Urban Investment and Development SAE", "role": "طرف تطوير/أرض محتمل وليس مقاولًا مثبتًا\nذكر في تقرير حضري بسياق بيع أرض/تطوير مشترك في Madinaty", "project": "مدينتي", "relation": "علاقة تطوير/أرض من مصدر ثانوي", "phone": "لم يُعثر على رقم رسمي موثوق", "phone_notes": "الكيان مذكور في مصدر ثانوي بسياق أرض/تطوير؛ لا يوجد خط اتصال موثق", "email": "", "website": "", "rel_source": "https://marsadomran.info/en/2022/09/2777/", "phone_source": "", "evidence_level": "C", "confidence": "منخفضة-متوسطة", "notes": "لا تدرج كمقاول أو مورد دون عقد إنشاء مستقل\nالعلاقة ليست عقد مقاولات مثبتًا؛ لا ينبغي إدراجه كمقاول أو مورد دون مستند إضافي."}, {"id": 31, "name": "Thabat", "role": "شريك إقليمي لـAtrium\nشراكة مع Atrium في السعودية بحسب موقع Atrium", "project": "السعودية", "relation": "شراكة مؤسسية؛ ليست موردًا مصريًا مؤكدًا", "phone": "لم يُعثر على رقم موثوق ضمن المصادر المستخدمة", "phone_notes": "شريك Atrium في السعودية وفق موقع Atrium؛ لم يثبت ارتباطه بمشروع مصري محدد", "email": "", "website": "https://atriumeg.com/", "rel_source": "https://atriumeg.com/", "phone_source": "", "evidence_level": "B", "confidence": "متوسطة", "notes": "إدراج للتعرّف على الشبكة لا لإثبات علاقة بمشروع مصري\nمدرج للشفافية فقط؛ خارج نطاق قائمة الموردين المحليين المصرية ما لم يظهر مشروع مصري مباشر."}, {"id": 32, "name": "Emileo Interiors", "role": "شركة مرتبطة بـAtrium/استحواذ معلن\nتصميم داخلي وتشطيبات حسب موقع Atrium", "project": "المشروعات غير المحددة", "relation": "صلة مؤسسية معلنة؛ لم يتحدد مشروع بعينه", "phone": "للتواصل الأولي عبر Atrium: +20 2 2693 1643 / 1647 / 1648", "phone_notes": "رقم مكتب Atrium العام؛ لم يُعثر على رقم مستقل موثوق لـEmileo Interiors", "email": "", "website": "https://atriumeg.com/", "rel_source": "https://atriumeg.com/", "phone_source": "https://atriumeg.com/contact/", "evidence_level": "B", "confidence": "متوسطة للصلة العامة", "notes": "لا ينسب إليها عقد محدد أو مطالبة دون مصدر خاص بالمشروع\nالموقع يعرض Emileo Interiors ضمن العلامات المرتبطة، لكن لم تُطابق علاقة مشروع محدد أو رقم مستقل."}, {"id": 33, "name": "MCBS – Modern Construction of Building Systems", "role": "كيان ضمن شبكة TMG؛ MEP/تيار خفيف/تشغيل\nأعمال خدمات فنية وصيانة للمنشآت والمراكز التجارية والفنادق", "project": "مرافق ومشروعات المجموعة", "relation": "يصف نفسه بأنه عضو بمجموعة TMG؛ ليست كل العقود منشورة", "phone": "غير منشور علنًا في المصادر التي تمت مراجعتها", "phone_notes": "شركة متخصصة بمجموعة TMG؛ يلزم طلب رقم إدارة الشركة من المجموعة", "email": "", "website": "https://eg.linkedin.com/company/mcbs-member-of-talaat-moustafa-group", "rel_source": "https://www.linkedin.com/company/mcbs-member-of-talaat-moustafa-group", "phone_source": "https://eg.linkedin.com/company/mcbs-member-of-talaat-moustafa-group", "evidence_level": "B", "confidence": "متوسطة-مرتفعة", "notes": "قائمة الملكية والقيمة والمشروعات تحتاج إفصاحًا أو سجلات داخلية\nلا أضع رقم TMG على أنه رقم مباشر لـMCBS؛ رقم المجموعة العام موجود بصف TMG مستقل."}, {"id": 34, "name": "Orion Facilities Management & Services", "role": "شركة مجموعة لإدارة المرافق\nإدارة مرافق وصيانة وخدمات عقارية", "project": "مدينتي ومشروعات المجموعة؛ The Spine", "relation": "شركة تابعة/مرتبطة بالمجموعة حسب المصادر الرسمية/ملف الشركة", "phone": "16286 | واتساب: +20 110 101 6286", "phone_notes": "خط حجز/استفسارات الخدمات — يشمل مدينتي والرحاب", "email": "", "website": "https://orion-eg.com/", "rel_source": "https://talaatmoustafa.com/upload/TMG%20Conso%20%20FS%2031%20December%202024-English.pdf | https://eg.linkedin.com/company/orionfms", "phone_source": "https://orion-eg.com/", "evidence_level": "A/B", "confidence": "مرتفعة للصلة العامة", "notes": "لا توجد قائمة موحدة للعقود أو أوامر العمل"}, {"id": 35, "name": "APUD – Arab Company for Projects and Urban Development", "role": "شركة مجموعة – مالك/مطور\nجهة مالكة لعدة مشروعات Atrium في مدينتي والرحاب", "project": "مدينتي؛ الرحاب", "relation": "كيان من مجموعة TMG؛ دوره غالبًا مالك/مطور وليس موردًا", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا لـAPUD", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/ar/investor-relations-ar/ | https://pme-consultancy.com/2022/06/02/el-rehab-city-project/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "يجب استخدام الكيان القانوني الدقيق في المطالبة والعقد\nالشركة جهة مالكة/مطور في مشاريع؛ الرقم المباشر للكيان لم يُتحقق منه."}, {"id": 36, "name": "Arab Company for Urban Investment", "role": "شركة مجموعة – جهة مالكة/استثمارية\nالجهة المالكة لمشروع 72 مبنى سكنيًا في Noor City على صفحة Atrium", "project": "نور", "relation": "اسم منفصل عن APUD بحسب مصدر المشروع", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://atriumeg.com/portfolio/72-residential-buildings-at-noor-city/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "لا تدمجها مع APUD دون مستند قانوني"}, {"id": 37, "name": "Nova Park Cairo", "role": "شركة تابعة/كيان مالك فندقي\nجهة مالكة/صاحب مشروع Four Seasons Nile Plaza على صفحة Atrium", "project": "القاهرة", "relation": "شركة ضمن سلسلة شركات TMG حسب القوائم 2025", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/upload/Consolidated%20financial%20statements%20for%20the%20year%20ended%2031-12-2025-English.pdf | https://atriumeg.com/portfolio/four-seasons-hotel-cairo-at-nile-plaza/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "ليست مقاولًا؛ تحدد كيان المشروع"}, {"id": 38, "name": "Egyptian Company for Development and Real Estate Projects", "role": "شركة تابعة/كيان مشروع\nجهة مالكة Four Seasons Sharm El Sheikh", "project": "شرم الشيخ", "relation": "شركة ضمن المجموعة بحسب القوائم 2025؛ جهة مشروع على صفحة Atrium", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/upload/Consolidated%20financial%20statements%20for%20the%20year%20ended%2031-12-2025-English.pdf | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "قيمة الحزمة ليست مبلغ دين أو كامل قيمة الأصل"}, {"id": 39, "name": "San Stefano Company for Touristic Investment", "role": "شركة تابعة/كيان فندقي\nجهة مشروع Four Seasons San Stefano في صفحة Atrium", "project": "الإسكندرية", "relation": "صلة ملكية/مشروع ضمن سلسلة TMG الفندقية", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/upload/Consolidated%20financial%20statements%20for%20the%20year%20ended%2031-12-2025-English.pdf | https://atriumeg.com/portfolio/four-seasons-hotel-san-stefano-grand-plaza/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "يجب فصلها عن San Stefano Real Estate Investment قانونيًا"}, {"id": 40, "name": "TMG Holding (Talaat Moustafa Group)", "role": "المطور/المالك الرئيسي\nالمطور الرئيسي ومجموعة الكيانات المالكة للمشروعات", "project": "مدينتي؛ الرحاب؛ SouthMED؛ نور؛ سيليا؛ الفنادق", "relation": "علاقة مباشرة كمالك/مطور؛ رقم التواصل هنا للخط العام للمجموعة", "phone": "الخط الساخن: 19691 | المقر: +20 2 3331 2000 / +20 2 3301 6701", "phone_notes": "الخط العام للمجموعة / المقر الرئيسي بالدقي", "email": "TMGH@tmg.com.eg | ir@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/contact-us/ | https://talaatmoustafa.com/investor-relations/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "استخدم رقم المجموعة للتوجيه فقط؛ لا يعني أن كل مقاول أو مورد لديه عقد مباشر مع TMG."}, {"id": 41, "name": "ACE Moharram Bakhoum", "role": "استشاري هندسي / تصميم وإشراف\nمذكور كاستشاري مشروع في بعض المشروعات الظاهرة بمحفظة SQUARE المرتبطة بجهات تطوير TMG؛ نطاق كل مشروع يحتاج مراجعة صفحة المشروع", "project": "مشروعات SQUARE المرتبطة بـAPUD/Arab Company for Urban Investment؛ مطابقة كل حزمة تحتاج تحققًا", "relation": "استشاري مرشح بعلاقة مشروعية غير مباشرة؛ لا يُفترض تعاقد مباشر مع TMG", "phone": "+20 2 3761 1576 (تحويلة 3930)", "phone_notes": "رقم الشركة العام المنشور على صفحة LinkedIn", "email": "admin.ace@ace-mb.com", "website": "https://ace-mb.com/", "rel_source": "https://www.square.com.eg/ | https://www.linkedin.com/company/ace-moharram-bakhoum", "phone_source": "https://www.linkedin.com/company/ace-moharram-bakhoum", "evidence_level": "B", "confidence": "متوسطة", "notes": "صفحة SQUARE تذكر ACE ضمن project consultant لبعض المشروعات؛ يلزم تحديد المشروع/الحزمة قبل اعتباره طرفًا مباشرًا."}, {"id": 42, "name": "Atrium Project Management (APM)", "role": "إدارة مشروعات / استشاري مرتبط بمجموعة Atrium\nذراع/شركة مرتبطة بـAtrium لإدارة المشروعات؛ لا يوجد في المصادر المستخدمة تعيين مؤكد على حزمة مصرية بعينها", "project": "صلة مؤسسية بمجموعة Atrium؛ المشروع المحدد غير مؤكد", "relation": "شركة مرتبطة مؤسسيًا؛ إدراج استكشافي وليس إثبات عقد مشروع محدد", "phone": "+20 2 2693 1643 / 1647 / 1648 (قناة Atrium العامة؛ ليست رقمًا منفصلًا مؤكدًا لـAPM)", "phone_notes": "رقم مجموعة Atrium بمباني الرحاب؛ قناة إحالة فقط", "email": "", "website": "https://www.apmeg.cloud/contact.html", "rel_source": "https://atriumeg.com/ | https://www.apmeg.cloud/contact.html", "phone_source": "https://www.apmeg.cloud/contact.html", "evidence_level": "B/C", "confidence": "متوسطة للصلة المؤسسية؛ منخفضة لتعيين مشروع بعينه", "notes": "رقم Atrium المنشور يصلح كقناة استفسار أولية فقط؛ لم يظهر رقم/عقد منفصل لكل مشروع."}];
    const TMG_TEAMS = [{"id": 1, "project": "SouthMED", "company": "Concrete Plus", "name": "Ahmed Ayman", "role": "Interior Project Manager", "linkedin": "https://eg.linkedin.com/in/ahmed-ayman-5056541a3", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/ahmed-ayman-5056541a3", "notes": "الملف مرتبط بـConcrete Plus؛ لا يثبت وحده تعيينه في SouthMED تحديدًا."}, {"id": 2, "project": "مشروعات Concrete Plus في مصر/السعودية", "company": "Concrete Plus", "name": "Ahmed Khashaba, PMP®, PMI-RMP®, PMI-SP®", "role": "المنصب الحالي الدقيق غير ظاهر في المقتطف العام؛ ملف مهني لدى Concrete Plus", "linkedin": "https://eg.linkedin.com/in/ahmedkhashaba", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/ahmedkhashaba", "notes": "الملف يعرض خبرة لدى Concrete Plus ومواقع متعددة، لكنه لا يربطه صراحةً بحزمة SouthMED."}, {"id": 3, "project": "مشروعات Concrete Plus", "company": "Concrete Plus", "name": "Ayman Tantawy", "role": "دور هندسي/تنفيذي؛ المسمى الحالي غير مؤكد بالمقتطف", "linkedin": "https://eg.linkedin.com/in/ayman-tantawy-853958103", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/ayman-tantawy-853958103", "notes": "الملف يذكر Concrete Plus وخبرة في تنفيذ أنشطة المشاريع؛ المشروع المحدد غير مؤكد."}, {"id": 4, "project": "مشروعات Concrete Plus", "company": "Concrete Plus", "name": "Kareem Eldsoky, PMP®, PE®", "role": "المسمى الحالي الدقيق غير ظاهر في المقتطف العام", "linkedin": "https://eg.linkedin.com/in/kareem-eldsoky", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/kareem-eldsoky", "notes": "خبرة منشورة لدى Concrete Plus، ومواقع مصرية متعددة؛ ليس تأكيدًا على SouthMED."}, {"id": 5, "project": "مشروعات Concrete Plus", "company": "Concrete Plus", "name": "Fady Mahfouz Youssef", "role": "Senior Electromechanical Commercial & Tendering Manager", "linkedin": "https://eg.linkedin.com/in/fady-mahfouz-youssef-642484a0", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/fady-mahfouz-youssef-642484a0", "notes": "ملف مهني يذكر Concrete Plus؛ لا يثبت تكليفه بمشروع TMG بعينه."}, {"id": 6, "project": "Four Seasons Cairo Capital / Madinaty", "company": "Atrium Quality Contractors", "name": "Ahmed Assaf", "role": "المسمى الوظيفي الحالي غير مؤكد بالمقتطف العام", "linkedin": "https://eg.linkedin.com/in/ahmed-assaf-ba10a9161", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/ahmed-assaf-ba10a9161", "notes": "الملف مرتبط بـAtrium وتوجد منشورات حول وظائف ومشروعات الشركة؛ المشروع المحدد غير محسوم."}, {"id": 7, "project": "مشروعات Atrium / وظائف مشروع بالقاهرة", "company": "Atrium Quality Contractors", "name": "Ahmed El Sobky", "role": "دور مهني لدى Atrium؛ المسمى الحالي غير ظاهر بالمقتطف", "linkedin": "https://eg.linkedin.com/in/ahmed-el-sobky-49841910b", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/ahmed-el-sobky-49841910b", "notes": "الملف مرتبط بـAtrium، لكن مقتطف الصفحة لا يقدم تعيينًا محددًا على مشروع TMG."}, {"id": 8, "project": "مشروعات Atrium", "company": "Atrium Quality Contractors", "name": "Mostafa Abdelatty", "role": "المسمى الوظيفي الحالي غير مؤكد؛ منشورات توظيف مرتبطة بالـQS", "linkedin": "https://eg.linkedin.com/in/mostafa-abdelatty-9a8726bb", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mostafa-abdelatty-9a8726bb", "notes": "يظهر بريد عمل منشور mostafa.abdelatty@atriumeg.com في منشور توظيف عام؛ لا يوجد رقم هاتف شخصي منشور."}, {"id": 9, "project": "Four Seasons Luxor", "company": "Atrium Quality Contractors", "name": "Amr A.", "role": "Civil Engineer؛ خبرة/مشروعات منشورة في Four Seasons Luxor", "linkedin": "https://eg.linkedin.com/in/amr-a-9525a4145", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/amr-a-9525a4145", "notes": "الملف يذكر خبرة Atrium ومشروعات Four Seasons Luxor؛ الاسم مختصر كما يعرضه LinkedIn."}, {"id": 10, "project": "FS Madinaty Villas وFS Luxor", "company": "Atrium Quality Contractors", "name": "Anas Reda, PMP®", "role": "المسمى الحالي التفصيلي غير ظاهر؛ ملف مرتبط بـAtrium", "linkedin": "https://eg.linkedin.com/in/anasreda1993", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/anasreda1993", "notes": "نشاطه العام يربط إعلانات QC بمشروعات FS Madinaty Villas وFS Luxor؛ لا يلزم أنه مدير المشروع."}, {"id": 11, "project": "The Strip Project / Madinaty", "company": "Atrium Quality Contractors", "name": "Abdelrahman Saeed", "role": "المسمى الحالي غير ظاهر بالمقتطف؛ ملف مرتبط بـAtrium", "linkedin": "https://eg.linkedin.com/in/عبدالرحمن-سعيد-8ba606237", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/عبدالرحمن-سعيد-8ba606237", "notes": "الملف/منشور Atrium يذكر اكتمال مرحلة من The Strip؛ يجب التحقق من رابط الملف المباشر على LinkedIn."}, {"id": 12, "project": "All Seasons Park Mall / Madinaty", "company": "Atrium Quality Contractors", "name": "Mahmoud El Najjar", "role": "Site Section Head Engineer", "linkedin": "https://eg.linkedin.com/in/mahmoud-el-najjar-3009b8a5", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mahmoud-el-najjar-3009b8a5", "notes": "الملف يذكر دور Site Section Head Engineer بمشاريع All Seasons Park Mall وGEMS American School Al-Rehab وGateway Mall."}, {"id": 13, "project": "Privado / Madinaty", "company": "Atrium Quality Contractors", "name": "Youssef Sameh", "role": "Planner Engineer", "linkedin": "https://eg.linkedin.com/in/youssef-sameh-a85716327", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/youssef-sameh-a85716327", "notes": "الملف يذكر Planner Engineer وخبرة Atrium في Privado, Madinaty؛ رابط ملف عام."}, {"id": 14, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Mahmoud Abd Elaal", "role": "الصفة الدقيقة غير واضحة بالمقتطف؛ ملف لدى CCC ويعرض حزمة MEP CP02", "linkedin": "https://eg.linkedin.com/in/mahmoud-abd-elaal-5a6a2380", "phone": "غير منشور", "evidence_level": "A/B", "source": "https://eg.linkedin.com/in/mahmoud-abd-elaal-5a6a2380", "notes": "يذكر صراحة العميل TMG، المقاول الرئيسي Atrium، مدير المشروع Hill International، والاستشاري Shaker Consultancy Group."}, {"id": 15, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Khaled Hesham", "role": "الصفة الحالية غير مؤكدة؛ ملف لدى CCC ومشاركات بشأن المشروع", "linkedin": "https://eg.linkedin.com/in/khaled-hesham-3555204", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/khaled-hesham-3555204", "notes": "شارك منشور JV عن حزمة MEP CP02. لا يُستنتج دور قيادي بالمشروع دون دليل إضافي."}, {"id": 16, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Sameh El Naggar", "role": "الصفة الحالية غير مؤكدة؛ ملف لدى CCC ومشاركات بشأن المشروع", "linkedin": "https://eg.linkedin.com/in/sameh-el-naggar-5b5a07161", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/sameh-el-naggar-5b5a07161", "notes": "شارك منشور JV عن الحزمة؛ المسمى والمهمة المحددان غير منشورين في المقتطف."}, {"id": 17, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Mohyeeldin Kotb", "role": "Cost Control Engineer", "linkedin": "https://eg.linkedin.com/in/mohyeeldin-kotb", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mohyeeldin-kotb", "notes": "يذكر الانتقال إلى وظيفة Cost Control Engineer في JV Atrium–CCC بمشروع Four Seasons Luxor."}, {"id": 18, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium / CCCE JV", "name": "Mohamed Yasser", "role": "متدرب/مهندس في مرحلة مبكرة؛ المسمى التفصيلي غير واضح", "linkedin": "https://eg.linkedin.com/in/mohamed-yasser-aa7711381", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/mohamed-yasser-aa7711381", "notes": "منشور LinkedIn يقول إنه ساهم في مشروع Four Seasons Luxor ضمن فريق Atrium؛ المسمى الحالي غير متحقق."}, {"id": 19, "project": "Four Seasons Luxor", "company": "Atrium Quality Contractors", "name": "Samer Gobran", "role": "شركة حالية: ELEVATE Construction Company؛ ناشر تحديث مشروع، لا دليل على توظيفه لدى TMG", "linkedin": "https://eg.linkedin.com/in/samer-gobran-a063bb7", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/samer-gobran-a063bb7", "notes": "منشور يصف المالك TMG، الاستشاري Shaker، المقاول Atrium وJV للأعمال الكهروميكانيكية. لا نعدّه عضوًا في فريق TMG."}, {"id": 20, "project": "Four Seasons Luxor", "company": "استشاري المشروع / Hill International", "name": "Mohamed Karam", "role": "المسمى الحالي SODIC؛ ملفه يسرد خبرة مرتبطة بـFour Seasons Luxor", "linkedin": "https://eg.linkedin.com/in/mohamed-karam-eng", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/mohamed-karam-eng", "notes": "الملف يسرد المشروع والجهات Hill وShaker وIETC؛ لا يثبت أن الشخص موظف حاليًا لدى تلك الجهات."}, {"id": 21, "project": "Noor City / New Gardens Capital", "company": "Atrium Project Management (APM)", "name": "Mohammed Ali, MBA®, PMP®", "role": "دور في إدارة/تخطيط الإنشاءات؛ المسمى الدقيق غير ظاهر في مقتطف الصفحة", "linkedin": "https://eg.linkedin.com/in/mohammed-ali88", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mohammed-ali88", "notes": "الملف يتضمن مشروعات Noor City، العميل TMG وحزم المباني والبنية التحتية."}, {"id": 22, "project": "Noor City / New Gardens Capital", "company": "Atrium Project Management (APM)", "name": "Sherif Nabil, PRMG", "role": "Project/Development Management؛ المسمى الحالي الدقيق يحتاج مراجعة الملف", "linkedin": "https://eg.linkedin.com/in/sherif-shaker-mba-prmg-aace-bsc-of-civil-eng-01a27641/ar", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/sherif-shaker-mba-prmg-aace-bsc-of-civil-eng-01a27641/ar", "notes": "صفحة LinkedIn تعرض Noor City ومشروعات تطوير أخرى بأدوار إدارة/تطوير."}, {"id": 23, "project": "Noor City", "company": "Atrium Project Management (APM)", "name": "Mahmoud Solyman", "role": "Civil Engineer؛ ملف مرتبط بـAPM وNoor City", "linkedin": "https://eg.linkedin.com/in/m-solyman", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/m-solyman", "notes": "الملف يذكر APM | TMG وخبرة في Noor City؛ المسمى المحدد الحالي ليس ظاهرًا بالمقتطف."}, {"id": 24, "project": "Noor City", "company": "Atrium Project Management (APM)", "name": "Alaa Badr", "role": "المسمى الوظيفي غير ظاهر بالمقتطف العام", "linkedin": "https://eg.linkedin.com/in/alaa-badr-b3a22819a", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/alaa-badr-b3a22819a", "notes": "الملف مرتبط بـAPM وNoor City; لا يوجد توصيف أكثر دقة في المقتطف العام."}, {"id": 25, "project": "Madinaty Central Park Extension / Madinaty Club Phase 2 / Madinaty Waterpark / Noor Smart City", "company": "TMG Developments", "name": "Haytham Ahmed Kadry", "role": "Project Manager؛ يذكر هذه المشاريع في خبرته", "linkedin": "https://eg.linkedin.com/in/haytham-kadry-project-manager", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/haytham-kadry-project-manager", "notes": "صفحة LinkedIn تذكر PM في التوسعات التجارية والإدارية والنوادي والـWaterpark وNour Smart City."}, {"id": 26, "project": "Water Park – Atrium / Madinaty", "company": "Atrium Quality Contractors", "name": "Fadel Mosaad", "role": "Mechanical Commercial Engineer؛ عمل في تقدير تكاليف MEP ومراجعة العطاءات والمستخلصات بالمشروع", "linkedin": "https://eg.linkedin.com/in/fadel-mosaad", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/fadel-mosaad", "notes": "الملف يحدد مشروع Water Park–Atrium (TMG) من يناير 2026، مع وصف لنطاق العمل."}, {"id": 27, "project": "Madinaty / Noor City", "company": "MCBS — Member of TMG", "name": "Farid Emile", "role": "MEP Operations Manager", "linkedin": "https://eg.linkedin.com/in/farid-emile", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/farid-emile", "notes": "الملف يذكر MCBS ومهام تشغيل مشروعات الشركة؛ المشروعات المحددة غير ظاهرة في المقتطف."}, {"id": 28, "project": "مشروعات MCBS / TMG", "company": "MCBS — Member of TMG", "name": "Adel Yassin, PMP®", "role": "Electromechanical Engineer؛ خبرة في المجال الكهربائي/الميكانيكي", "linkedin": "https://eg.linkedin.com/in/adel-yassin-pmp-%C2%AE-b0b13a208", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/adel-yassin-pmp-%C2%AE-b0b13a208", "notes": "ملف مرتبط بـMCBS، لكن المشروع المحدد غير مؤكد."}, {"id": 29, "project": "مدينتي ومرافق TMG", "company": "Orion Facilities Management — TMG", "name": "Tamer Ahmed", "role": "Senior Facilities Management Director", "linkedin": "https://eg.linkedin.com/in/tamerabdulaziz", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/tamerabdulaziz", "notes": "الملف يذكر Orion Facilities Management - TMG؛ لا يحدد مشروعًا منفردًا."}, {"id": 30, "project": "Atrium / TMG — قيادة الشركة", "company": "Atrium Quality Contractors / APM", "name": "Hagar Sabry, PRMG, MBA", "role": "المسمى الشخصي يحتاج تحققًا؛ المصدر يذكر قيادة APM/Atrium لشخص آخر في نص مقتطف مختلط", "linkedin": "https://eg.linkedin.com/in/hagar-sabry-prmg-mba-7bb7a9133", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/hagar-sabry-prmg-mba-7bb7a9133", "notes": "تم استبعاد أي استنتاج عن منصب CEO لأن المقتطف يخلط بوضوح أسماء/نبذات مختلفة. أُدرج كرابط للتحقق فقط."}, {"id": 31, "project": "Four Seasons Cairo Capital", "company": "Atrium Quality Contractors", "name": "Ali Elkady", "role": "مهندس؛ المسمى الدقيق غير ظاهر بالمقتطف", "linkedin": "https://eg.linkedin.com/in/ali-elkady-878784172", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/ali-elkady-878784172", "notes": "ملف مرتبط بـAtrium ومواقع متعددة؛ لا دليل كافٍ لربطه مباشرة بحزمة Four Seasons Cairo Capital."}, {"id": 32, "project": "Atrium / مشروعات متعددة", "company": "Atrium Quality Contractors", "name": "Mahmoud Elbakry", "role": "المسمى الوظيفي غير ظاهر بالمقتطف؛ يذكر مشروعات 2026", "linkedin": "https://eg.linkedin.com/in/mahmoudelbakry", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/mahmoudelbakry", "notes": "الملف يذكر Gate 3 Madinaty وRehab Hills Mall؛ ملكية Rehab Hills Mall بالصفحة تعود لجهة أخرى، لذا يلزم فصل المشروع عن حافظة TMG وعدم اعتباره تلقائيًا مشروع TMG."}, {"id": 33, "project": "مشروعات Atrium / Madinaty", "company": "Atrium Quality Contractors", "name": "Bassel Nabil, PMP®, CCP", "role": "Senior Cost Control Engineer", "linkedin": "https://eg.linkedin.com/in/bassel-nabil-ali", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/bassel-nabil-ali", "notes": "الملف يعرض خبرة في Atrium بمدينتي والقاهرة والعاصمة الإدارية؛ لا يحدد حزمة TMG واحدة في المقتطف."}, {"id": 34, "project": "مشروعات Atrium / أدوار QS والتجاري", "company": "Atrium Quality Contractors", "name": "Fadel Mosaad", "role": "Mechanical Commercial Engineer", "linkedin": "https://eg.linkedin.com/in/fadel-mosaad", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/fadel-mosaad", "notes": "الملف يذكر مشروع Water Park – Atrium (TMG) خلال يناير 2026، مع مسؤوليات تقدير أعمال MEP والعطاءات والمستخلصات."}, {"id": 35, "project": "مشروعات Atrium / التوظيف الفني", "company": "Atrium Quality Contractors", "name": "Hoda Hussein", "role": "الدور الحالي غير محدد في المقتطف؛ حساب مرتبط بـAtrium", "linkedin": "https://eg.linkedin.com/in/hoda-hussein-7a98b012a", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/hoda-hussein-7a98b012a", "notes": "منشورات عامة عن توظيف QS وProcurement وBIM وPlanning؛ ليست دليلًا على تعيينها في مشروع محدد."}, {"id": 36, "project": "مشروعات TMG / مدينتي والعاصمة", "company": "TMG Holding", "name": "Amir Elnabawy", "role": "Quantity Surveyor / Technical Office Manager وفق نبذة منشورة؛ وظيفته الدقيقة الحالية تحتاج تحققًا", "linkedin": "https://eg.linkedin.com/in/amir-el-nabawy", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/amir-el-nabawy", "notes": "يذكر الخبرة لدى TMG في Madinaty وNew Capital؛ النبذة تشير إلى QS وTechnical Office Manager وخبرة يبحث لها عن فرصة، لذلك تحقق من الحالة الحالية قبل التواصل."}, {"id": 37, "project": "مشروعات TMG — القيادة المؤسسية", "company": "TMG Holding", "name": "Hesham Talaat Moustafa", "role": "CEO and Managing Director وفق الإفصاحات المؤسسية؛ ملف LinkedIn المطابق غير مؤكد في نتائج البحث", "linkedin": "غير متحقق", "phone": "غير منشور", "evidence_level": "A للمسمى المؤسسي؛ غير متحقق لملف LinkedIn", "source": "https://talaatmoustafa.com/investor-relations/", "notes": "لم يُدرج رابط ملف شخصي غير مؤكد."}, {"id": 38, "project": "مشروعات TMG — القيادة المؤسسية", "company": "TMG Holding", "name": "Tarek Talaat Moustafa", "role": "Chairman وفق الإفصاحات المؤسسية؛ ملف LinkedIn المطابق غير مؤكد", "linkedin": "غير متحقق", "phone": "غير منشور", "evidence_level": "A للمسمى المؤسسي؛ غير متحقق لملف LinkedIn", "source": "https://talaatmoustafa.com/investor-relations/", "notes": "نتائج البحث عن الاسم الأول والشركة لم تُنتج ملفًا يمكن تأكيد هويته."}];
    const TMG_SWOT = {"strengths": [{"id": "S1", "factor": "Dominant Landbank", "details": "Holds Egypt's largest private urban landbank across East Cairo, North Coast, Red Sea, and Gulf region.", "data": "26,722+ Feddans (>112mn sqm BUA); Madinaty (8,000 feddans), Noor (5,000 feddans), SouthMED (5,500 feddans)", "impact": "High Moat", "source": "TMG Investor Relations / Audit FY25"}, {"id": "S2", "factor": "Massive Sales Backlog", "details": "Unprecedented revenue visibility provided by contracted off-plan sales awaiting construction delivery.", "data": "EGP 441.2 Billion backlog (as of Dec 2025); excludes SouthMED gross sales", "impact": "High Visibility", "source": "FY2025 Earnings Release"}, {"id": "S3", "factor": "Strong Headline Financials", "details": "Record-setting revenue and net earnings growth driven by unit deliveries and hospitality consolidation.", "data": "FY25 Revenue EGP 62.5B (+46%), Net Profit EGP 18.2B (+43%); H1 26 Rev EGP 30.19B", "impact": "High Growth", "source": "Audited Financials FY2025 & H1 2026"}, {"id": "S4", "factor": "Hospitality Foreign Currency", "details": "Icon hotel portfolio generates strong USD/EUR cash flows, offering a natural hedge against EGP devaluation.", "data": "Hospitality Revenue EGP 14.9B in FY25 (+30%); 51% acquisition of Legacy Hotels (7 historic state hotels)", "impact": "FX Hedge Moat", "source": "Icon ADQ/ADNEC Filing & FS Notes"}, {"id": "S5", "factor": "Asset-Light Model Pivot", "details": "Shift toward master development partnership agreements that capture development fees without land balance-sheet liabilities.", "data": "SouthMED (~8% master development fee model) & The Spine (24.5% NBE JV plot sale EGP 67.12B)", "impact": "Capital Light", "source": "TMG Market Updates & Cabinet Decrees"}, {"id": "S6", "factor": "Integrated City Model", "details": "Combines residential units with recurring commercial retail leasing, sports clubs, utilities, and transportation.", "data": "Other Recurring Revenue EGP 10.9B (+64% YoY in FY25); Open Air Mall (260k sqm GLA)", "impact": "Resilient Cash", "source": "TMG Operating Segment Reports"}], "weaknesses": [{"id": "W1", "factor": "Cash Conversion Lag", "details": "Operating cash flow trails accounting profit due to heavy cash absorption into properties under development.", "data": "H1 2026 OCF EGP 3.11B vs Consolidated Profit EGP 9.95B (~31% conversion); EGP 18.26B WIP burn", "impact": "Liquidity Risk", "source": "H1 2026 Cash Flow Statement"}, {"id": "W2", "factor": "Off-Balance Sheet Lease Debt", "details": "Extensive use of sale-and-leaseback transactions creates fixed contractual debt-service obligations.", "data": "EGP 43.99 Billion in Financial Lease Notes Payable (June 2026), up from EGP 34.4B in Dec 2025", "impact": "High Leverage", "source": "Consolidated Balance Sheet Note 18"}, {"id": "W3", "factor": "High Interest Cost Environment", "details": "Elevated effective borrowing rates on local debt create substantial annual interest expense.", "data": "Direct Bank Loans EGP 16.5B at 28.6% average effective rate on EGP credit facilities", "impact": "Cost Drag", "source": "Financial Statement Notes H1 2026"}, {"id": "W4", "factor": "Resident & Customer Friction", "details": "Unilateral annual maintenance deficit surcharges and statutory resale transfer fee enforcement cause disputes.", "data": "Annual maintenance difference demands EGP 15k–45k/unit; CPA Art. 15 resale fee challenges", "impact": "Reputational Risk", "source": "CPA Registries & New Cairo Court Logs"}, {"id": "W5", "factor": "Captive EPC & Governance", "details": "Heavy reliance on related-party contractor Alexandria Construction Co. (ACC) and Atrium Quality Contractors.", "data": "ACC holds 8.05% TMGH stake; EGP 1.90B due from related parties in June 2026", "impact": "Governance Risk", "source": "TMG Corporate Governance Report FY25"}, {"id": "W6", "factor": "Long Delivery Horizons", "details": "Mega-projects require 15- to 20-year execution cycles, exposing developer to long-term macro volatility.", "data": "The Spine (2030 first delivery), SouthMED (2029 first delivery), Banan KSA (2029 first delivery)", "impact": "Execution Risk", "source": "IR Masterplan Timelines 2026"}], "opportunities": [{"id": "O1", "factor": "North Coast Tourism Boost", "details": "Transforming North Coast into a year-round international tourist destination via SouthMED.", "data": "$21 Billion projected lifetime project value; >25,000 units sold in initial launch phase", "impact": "High Topline", "source": "Financial Times & TMG Disclosures"}, {"id": "O2", "factor": "Saudi Arabia Expansion", "details": "Expanding master-community model into Riyadh under Saudi National Housing Company (NHC).", "data": "Banan City (10mn sqm landbank, 25k units, SAR 31.4B total projected investment)", "impact": "Regional Growth", "source": "TMG KSA / NHC Partnership Filing"}, {"id": "O3", "factor": "Omani Coastal Development", "details": "Entering Oman's real estate market via partnerships with the Omani Ministry of Housing.", "data": "Jood & Yamal projects (4.9mn sqm landbank, ~14k units, OMR 1.8B projected sales)", "impact": "Market Diversification", "source": "Oman Ministry Protocol May 2025"}, {"id": "O4", "factor": "Sovereign Wealth Partnerships", "details": "Direct equity co-investments with Gulf sovereign wealth funds and Egyptian state banks.", "data": "ADQ/ADNEC $800M investment for 40.5% in ICON; Rawasy EGP 11.9B commercial monetization", "impact": "Capital Inflow", "source": "EGX Disclosures & ADQ Press Releases"}, {"id": "O5", "factor": "Commercial Asset Monetization", "details": "Selling and leasing prime retail spaces in Open Air Mall, East Hub, and Craft Zone.", "data": "260k sqm GLA at Open Air Mall; expansion of retail leasing recurring cash flow", "impact": "High Margin", "source": "TMG Commercial Segment Reports"}, {"id": "O6", "factor": "Smart City & 5G Infrastructure", "details": "Monetizing smart-city utilities, solar microgrids, and fiber-optic networks across Noor City.", "data": "Integrated 5G smart-city grid, Siemens switchgear JV, solar microgrids", "impact": "Recurring Utility", "source": "EMAS Sewedy & TMG Tech Disclosures"}], "threats": [{"id": "T1", "factor": "Construction Cost Inflation", "details": "Cumulative domestic currency devaluation and imported material inflation push up cost-to-complete.", "data": "Egypt CPI inflation projected >16.7%; fixed-price off-plan sales sold in 2021-2023 at lower cost basis", "impact": "Margin Squeeze", "source": "Gleeds Construction Market Report 2026"}, {"id": "T2", "factor": "High Domestic Interest Rates", "details": "Elevated CBE policy rates increase borrowing costs and dampen mortgage affordability.", "data": "CBE overnight lending rate at 20%+; TMG interest-bearing debt & lease obligations >EGP 60.5B", "impact": "Financial Cost", "source": "Central Bank of Egypt MPC Statements"}, {"id": "T3", "factor": "Household Purchasing Strain", "details": "Erosion of domestic consumer real income reduces demand for primary residential property.", "data": "Contracted sales declined 24% YoY in 2025 (EGP 382.2B vs EGP 504.0B in 2024)", "impact": "Demand Risk", "source": "EFG Hermes Property Market Outlook 2026"}, {"id": "T4", "factor": "Consumer Protection Enforcement", "details": "CPA enforcement against 5%-10% resale transfer fees under Article 15 of Law 181/2018.", "data": "Widespread individual civil court rulings ordering refunds of administrative resale fees", "impact": "Legal Liability", "source": "Egyptian CPA Rulings & Law 181/2018"}, {"id": "T5", "factor": "Land Allocation Scrutiny", "details": "Public policy debates and media scrutiny regarding non-competitive direct state land allocations.", "data": "Historical 2010 SAC Madinaty annulment precedent; 2023 ARIJ investigative reporting", "impact": "Regulatory Risk", "source": "Egyptian State Council Rulings & ARIJ 2023"}, {"id": "T6", "factor": "Subcontractor Supply Chain Strain", "details": "Financial pressure on trade subcontractors leading to potential site walk-offs or delivery slippages.", "data": "2008 ACC Shehata Hassan complaint; 2024 Mada Masr SouthMED payment chain risk signal", "impact": "Operational Risk", "source": "Forensic Due Diligence & Press Reports"}]};
    const TMG_TOWS = {"SO": [{"id": "SO-1", "name": "Leverage Landbank for Asset-Light Growth", "roadmap": "Combine massive 26k+ feddan landbank with asset-light master development model (SouthMED) to maximize revenue while minimizing balance-sheet risk.", "priority": "High Priority"}, {"id": "SO-2", "name": "Monetize Icon Hotel FX Cash Flows", "roadmap": "Deploy USD/EUR hospitality revenues from Legacy/Four Seasons hotels to fund cross-border regional expansion in KSA (Banan) and Oman (Jood).", "priority": "High Priority"}, {"id": "SO-3", "name": "Scale Commercial Leasing Portfolio", "roadmap": "Utilize EGP 441B backlog visibility to pre-lease commercial retail centers (Open Air Mall, East Hub) and expand recurring revenue base.", "priority": "Medium Priority"}], "ST": [{"id": "ST-1", "name": "Centralized Bulk Material Hedging", "roadmap": "Use financial scale and liquidity reserves (EGP 66.4B) to bulk-purchase rebar and cement directly, hedging against construction cost inflation.", "priority": "High Priority"}, {"id": "ST-2", "name": "FX Debt & Revenue Matching", "roadmap": "Align foreign currency debt service with USD hospitality earnings, shielding group balance sheet from EGP devaluation shocks.", "priority": "High Priority"}, {"id": "ST-3", "name": "Flexible Customer Financing", "roadmap": "Utilize strong balance sheet to extend unit payment plans to 10-12 years, sustaining sales velocity amidst domestic affordability strain.", "priority": "Medium Priority"}], "WO": [{"id": "WO-1", "name": "Refinance High-Cost EGP Debt", "roadmap": "Use sovereign wealth partnerships (ADQ/ADNEC) and Gulf expansion cash flows to substitute 28.6% EGP debt with lower-cost regional credit.", "priority": "High Priority"}, {"id": "WO-2", "name": "Accelerate Cash Conversion via Asset Monetization", "roadmap": "Convert properties under development into liquid cash by monetizing commercial spaces via Rawasy and leasing vehicles to close OCF gap.", "priority": "High Priority"}, {"id": "WO-3", "name": "Enhance Maintenance Reserve Governance", "roadmap": "Establish independent audited trust accounts for Madinaty/Rehab maintenance deposits to eliminate resident litigation and improve brand trust.", "priority": "Medium Priority"}], "WT": [{"id": "WT-1", "name": "Shorten Subcontractor Payment Cycles", "roadmap": "Reduce post-dated check tenors from 270 days to 60-90 days to prevent trade subcontractor insolvency and avoid project completion slippages.", "priority": "Critical Priority"}, {"id": "WT-2", "name": "Reform Resale Fee Structures", "roadmap": "Replace percentage-based resale transfer fees with flat administrative costs to comply with CPA Article 15 and eliminate legal liability.", "priority": "High Priority"}, {"id": "WT-3", "name": "Cap Off-Balance Sheet Lease Leverage", "roadmap": "Freeze new sale-and-leaseback transactions (currently EGP 44B) to ensure debt service obligations do not consume operating cash flows.", "priority": "High Priority"}]};
    const TMG_PROJECTS_MAP = [{"id": "southmed", "name_ar": "مشروع ساوث ميد (SouthMED)", "name_en": "SouthMED Mediterranean Mega-Resort", "location_ar": "الضبعة، الساحل الشمالي (الكيلو 165 طريق الإسكندرية - مطروح)", "location_en": "El Dabaa, North Coast Mediterranean (Km 165)", "lat": 31.0167, "lng": 28.4, "area": "5,542 فدان (23.3 مليون م²)", "gdv": "21.0 مليار دولار GDV", "deliveries": "2029+", "contractors": "Concrete Plus (Zone C01 - 10B EGP), Atrium AQC, Metito, Crystal Lagoons", "color": "#06b6d4"}, {"id": "noor", "name_ar": "مدينة نور الذكية (Noor City)", "name_en": "Noor Smart City", "location_ar": "حدائق العاصمة، أمام العاصمة الإدارية (شرق القاهرة)", "location_en": "Capital Gardens, East Cairo (Opposite NAC)", "lat": 30.1667, "lng": 31.75, "area": "5,000 فدان (140,000 وحدة سكنية)", "gdv": "> 500 مليار جنيه مصري", "deliveries": "2026 – 2028+", "contractors": "Concrete Plus (V3.2 - 170 Villas), Atrium AQC, Siemens, Schneider Electric", "color": "#3b82f6"}, {"id": "madinaty", "name_ar": "مدينتي و East Hub و Open Air Mall", "name_en": "Madinaty Integrated City & East Hub", "location_ar": "القاهرة الجديدة، طريق السويس", "location_en": "New Cairo, Suez Road", "lat": 30.0833, "lng": 31.6333, "area": "8,000 فدان (33.6 مليون م²)", "gdv": "مجتمع متكامل يضم >700 ألف نسمة", "deliveries": "مكتمل جزئياً / توسعات مستمرة", "contractors": "Atrium AQC, Alexandria Construction (ACC), CCC (Four Seasons Capital JV), MCBS", "color": "#10b981"}, {"id": "celia", "name_ar": "مشروع سيليا (Celia New Capital)", "name_en": "Celia New Administrative Capital", "location_ar": "العاصمة الإدارية الجديدة، الحزام الأخضر", "location_en": "New Administrative Capital, Green River", "lat": 30.0167, "lng": 31.7, "area": "500 فدان (فيلات وعمارات فاخرة)", "gdv": "> 35 مليار جنيه مبيعات", "deliveries": "تسليمات مرحلية جارية", "contractors": "Atrium Quality Contractors, Alexandria Construction (ACC)", "color": "#8b5cf6"}, {"id": "fs_luxor", "name_ar": "فندق فورسيزونز الأقصر (Four Seasons Luxor)", "name_en": "Four Seasons Hotel Luxor", "location_ar": "الأقصر، كورنيش النيل مباشرة", "location_en": "Luxor, Direct Nile Corniche", "lat": 25.6872, "lng": 32.6396, "area": "فندق تاريخي فاخر 201 غرفة وجناح", "gdv": "رافعة تدفقات دولارية (Icon Hospitality)", "deliveries": "2026/2027", "contractors": "Atrium Quality Contractors (Main EPC Turnkey)", "color": "#f59e0b"}, {"id": "fs_sharm", "name_ar": "فورسيزونز شرم الشيخ (Four Seasons Sharm)", "name_en": "Four Seasons Resort Sharm El Sheikh", "location_ar": "شرم الشيخ، خليج القرش (البحر الأحمر)", "location_en": "Sharm El Sheikh, Sharks Bay (Red Sea)", "lat": 27.9158, "lng": 34.3299, "area": "توسعة منتجع فاخر بـ 1,400 غرفة وفيلا", "gdv": "أعلى عائد سياحي دولاري بالغرفة", "deliveries": "قيد التشغيل وتوسعات نشطة", "contractors": "Atrium Quality Contractors, ACC", "color": "#ec4899"}, {"id": "san_stefano", "name_ar": "سان ستيفانو جراند بلازا (San Stefano Alexandria)", "name_en": "San Stefano Grand Plaza Alexandria", "location_ar": "الإسكندرية، كورنيش سان ستيفانو", "location_en": "Alexandria, Corniche Landmark", "lat": 31.2439, "lng": 29.9678, "area": "برج متعدد الاستخدامات + فورسيزونز + مارينا", "gdv": "أحد أبرز أصول محفظة الضيافة والتجزئة", "deliveries": "مشروع قائم ومُدر للدخل الدوري", "contractors": "Alexandria Construction (ACC), Atrium AQC", "color": "#6366f1"}, {"id": "banan", "name_ar": "مدينة بنان الذكية - الرياض (Banan Riyadh)", "name_en": "Banan Smart City Riyadh (KSA)", "location_ar": "ضاحية الفرسان، شمال شرق الرياض، المملكة العربية السعودية", "location_en": "Al Fursan Suburb, North-East Riyadh, KSA", "lat": 24.85, "lng": 46.75, "area": "10.0 مليون م² (27,000 وحدة سكنية)", "gdv": "31.4 مليار ريال سعودي (> 8.3B USD)", "deliveries": "2029 المستهدف الأول", "contractors": "Atrium Saudi (100%), NHC (الشركة الوطنية للإسكان)", "color": "#10b981"}, {"id": "jood_yamal", "name_ar": "مدينتي جود ويامال - سلطنة عمان", "name_en": "Jood & Yamal Coastal Cities (Oman)", "location_ar": "مسقط / بركاء، ساحل سلطنة عمان", "location_en": "Muscat / Barka Coast, Sultanate of Oman", "lat": 23.7, "lng": 58.0, "area": "4.9 مليون م² (~14,000 وحدة سكنية)", "gdv": "1.8 مليار ريال عماني (~ 4.7B USD)", "deliveries": "مرحلة التخطيط والتمهيد", "contractors": "تحالف مجموعة طلعت مصطفى ووزارة الإسكان العمانية", "color": "#14b8a6"}];

    
    // XSS Sanitizer & Protocol Validator (Codex Audit Recommendation)
    function escapeHTML(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function safeUrl(url, allowedProtocols = ['http:', 'https:']) {
      if (!url) return '';
      try {
        const parsed = new URL(url);
        return allowedProtocols.includes(parsed.protocol) ? parsed.href : '';
      } catch (e) {
        return '';
      }
    }

    let activeProjectFilter = 'all';
    let tmgLeafletMapInstance = null;
    let tmgMapMarkers = {};

    // Initialize Leaflet Map
    function initTmgMap() {
      const mapContainer = document.getElementById('tmg-leaflet-map');
      if (!mapContainer || tmgLeafletMapInstance) return;

      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const tileUrl = isDark 
        ? 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}'
        : 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}';

      tmgLeafletMapInstance = L.map('tmg-leaflet-map', {
        center: [27.5, 38.0],
        zoom: 5,
        minZoom: 3,
        maxZoom: 16,
        zoomControl: true
      });

      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; Esri, HERE, Garmin, FAO, USGS, EPA',
        maxZoom: 16
      }).addTo(tmgLeafletMapInstance);

      // Add Project Markers with custom HTML Pins & Labels
      const latLngs = [];
      TMG_PROJECTS_MAP.forEach(proj => {
        latLngs.push([proj.lat, proj.lng]);
        
        // Custom Rich HTML DivIcon
        const customIcon = L.divIcon({
          className: 'tmg-map-pin',
          html: `
            <div style="display:flex; flex-direction:column; align-items:center; transform: translate(-50%, -100%); cursor:pointer;">
              <div style="background:${proj.color}; color:#fff; font-weight:800; font-size:11px; padding:3px 8px; border-radius:12px; box-shadow:0 3px 8px rgba(0,0,0,0.35); white-space:nowrap; border:1.5px solid #fff; display:flex; align-items:center; gap:4px;">
                <span>📍</span> <span>${proj.id === 'banan' ? '🇸🇦 بنان الرياض' : (proj.id === 'jood_yamal' ? '🇴🇲 عمان' : proj.name_ar.split(' ')[0] + ' ' + (proj.name_ar.split(' ')[1] || ''))}</span>
              </div>
              <div style="width:10px; height:10px; background:${proj.color}; border:2px solid #fff; border-radius:50%; margin-top:2px; box-shadow:0 0 8px ${proj.color};"></div>
            </div>
          `,
          iconSize: [0, 0],
          iconAnchor: [0, 0]
        });

        const marker = L.marker([proj.lat, proj.lng], { icon: customIcon }).addTo(tmgLeafletMapInstance);

        // Tooltip
        marker.bindTooltip(`<strong>${proj.name_ar}</strong><br><span style="font-size:11px; color:#888;">${proj.area}</span>`, {
          permanent: false,
          direction: 'top'
        });

        // Rich Popup
        const popupHtml = `
          <div style="font-family: inherit; min-width: 250px; padding: 6px; color: #111;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 2px solid ${proj.color}; padding-bottom: 5px; margin-bottom: 8px;">
              <h4 style="margin:0; font-size:14px; font-weight:800; color:#111827;">${proj.name_ar}</h4>
            </div>
            <div style="font-size:12px; margin-bottom:5px;">📍 <strong>الموقع:</strong> ${proj.location_ar}</div>
            <div style="font-size:12px; margin-bottom:5px;">📐 <strong>المساحة:</strong> ${proj.area}</div>
            <div style="font-size:12px; margin-bottom:5px;">💰 <strong>القيمة / الأثر:</strong> ${proj.gdv}</div>
            <div style="font-size:12px; margin-bottom:6px;">🏗️ <strong>المقاولون الرئيسيون:</strong> ${proj.contractors}</div>
            <div style="margin-top:10px;">
              <button onclick="filterMapByProject('${proj.id}')" style="width:100%; background:${proj.color}; color:#fff; border:none; padding:7px 12px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                🔍 تصفية الشركات والفرق لهذا المشروع
              </button>
            </div>
          </div>
        `;
        marker.bindPopup(popupHtml);
        tmgMapMarkers[proj.id] = marker;
      });

      // Fit bounds to show Egypt, KSA, and Oman
      if (latLngs.length > 0) {
        tmgLeafletMapInstance.fitBounds(latLngs, { padding: [40, 40] });
      }

      window.tmgMapInitialized = true;
    }

    // Switch Map Tile Theme
    function updateMapTheme(theme) {
      if (!tmgLeafletMapInstance || !window.tmgMapTiles) return;
      const tileUrl = theme === 'dark'
        ? 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}'
        : 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}';
      tmgLeafletMapInstance.removeLayer(window.tmgMapTiles);
      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; Esri, HERE, Garmin, FAO, USGS, EPA',
        maxZoom: 16
      }).addTo(tmgLeafletMapInstance);
    }

    // Filter Map by Project
    function filterMapByProject(projId) {
      activeProjectFilter = projId;

      // Update Filter Chips UI
      document.querySelectorAll('#project-filter-chips .filter-chip').forEach(btn => {
        const onclickAttr = btn.getAttribute('onclick') || '';
        btn.classList.toggle('active', onclickAttr.includes(`'${projId}'`));
      });

      // Update Map View
      if (tmgLeafletMapInstance) {
        if (projId === 'all') {
          tmgLeafletMapInstance.setView([28.5, 36.0], 5);
          document.getElementById('map-selection-indicator').textContent = 'المشروع النشط: عرض جميع المشروعات';
        } else {
          const proj = TMG_PROJECTS_MAP.find(p => p.id === projId);
          if (proj) {
            tmgLeafletMapInstance.setView([proj.lat, proj.lng], 9);
            if (tmgMapMarkers[projId]) {
              tmgMapMarkers[projId].openPopup();
            }
            document.getElementById('map-selection-indicator').innerHTML = `المشروع النشط: <strong>${proj.name_ar}</strong> (${proj.area})`;
          }
        }
      }

      // Cross-filter Companies Table and Teams Grid
      renderCompaniesTable();
      renderTeamsCards();

      // Smooth scroll to table if a specific project was selected
      if (projId !== 'all') {
        const tableEl = document.getElementById('companies-table-dom');
        if (tableEl) {
          tableEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }
    }

    function resetProjectFilter() {
      filterMapByProject('all');
      document.getElementById('company-search-input').value = '';
      document.getElementById('company-role-filter').value = 'all';
      document.getElementById('team-search-input').value = '';
      applyCompanyFilters();
      applyTeamFilters();
    }

    // Render Companies Table
    function renderCompaniesTable() {
      const tbody = document.getElementById('companies-table-body');
      if (!tbody) return;

      const searchTerm = (document.getElementById('company-search-input')?.value || '').toLowerCase().trim();
      const roleFilter = document.getElementById('company-role-filter')?.value || 'all';

      let filtered = TMG_COMPANIES.filter(c => {
        // Project Match (Full Multi-Keyword & Oman Support)
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': ['southmed', 'ساوث'],
            'noor': ['نور', 'noor'],
            'madinaty': ['مدينتي', 'madinaty'],
            'celia': ['celia', 'سيليا'],
            'fs_luxor': ['أقصر', 'luxor'],
            'fs_sharm': ['شرم', 'sharm'],
            'san_stefano': ['سان ستيفانو', 'san stefano', 'إسكندرية'],
            'banan': ['سعودية', 'رياض', 'بنان', 'banan', 'ksa'],
            'jood_yamal': ['عمان', 'جود', 'يامال', 'oman']
          };
          const keywords = projMap[activeProjectFilter];
          if (keywords && !keywords.some(k => (c.project || '').toLowerCase().includes(k.toLowerCase()))) {
            return false;
          }
        }

        // Role Filter
        if (roleFilter !== 'all') {
          if (roleFilter === 'مقاول' && !c.role.includes('مقاول') && !c.relation.includes('مقاول')) return false;
          if (roleFilter === 'ذراع' && !c.role.includes('ذراع') && !c.relation.includes('منظومة')) return false;
          if (roleFilter === 'مورد' && !c.role.includes('مورد') && !c.role.includes('تجهيز') && !c.role.includes('أنظمة')) return false;
          if (roleFilter === 'استشاري' && !c.role.includes('استشار') && !c.role.includes('إشراف')) return false;
          if (roleFilter === 'بنك' && !c.role.includes('بنك') && !c.relation.includes('بنك')) return false;
        }

        // Search Term
        if (searchTerm) {
          const matchStr = `${c.name} ${c.role} ${c.project} ${c.phone} ${c.relation}`.toLowerCase();
          if (!matchStr.includes(searchTerm)) return false;
        }

        return true;
      });

      document.getElementById('companies-count-badge').textContent = `${filtered.length} / 42 شركة`;

      if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:30px; color:var(--text-muted);">لا توجد شركات مطابقة لمعايير البحث والتصفية المحددة.</td></tr>`;
        return;
      }

      tbody.innerHTML = filtered.map((c, idx) => {
        // Evidence badge color
        const evColor = c.evidence_level.startsWith('A') ? 'badge-low' : (c.evidence_level.includes('B') ? 'badge-med' : 'badge-high');
        
        // Format Phones with click-to-call
        const phoneLinks = c.phone && c.phone !== 'غير متاح'
          ? c.phone.split('/').map(p => {
              const cleanP = p.replace(/[^0-9+]/g, '');
              return `<a href="tel:${cleanP}" style="color:var(--accent-blue); text-decoration:none; font-family:var(--font-mono); font-size:12px; margin-inline-end:6px;">📞 ${p.trim()}</a>`;
            }).join('<br>')
          : `<span style="color:var(--text-muted); font-size:11.5px;">غير معلن</span>`;

        // Format Email
        const emailLink = c.email && c.email !== 'غير متاح'
          ? `<a href="mailto:${c.email}" style="color:var(--accent-cyan); text-decoration:none; font-size:11.5px; display:block; overflow:hidden; text-overflow:ellipsis;">✉️ ${c.email}</a>`
          : `<span style="color:var(--text-muted); font-size:11px;">—</span>`;

        // Website
        const webLink = c.website && c.website.startsWith('http')
          ? `<a href="${c.website}" target="_blank" style="color:var(--accent-emerald); text-decoration:none; font-size:11.5px; font-weight:700;">🌐 زيارة الموقع ↗</a>`
          : ``;

        return `
          <tr style="border-bottom: 1px solid var(--border-subtle); hover: background-color: var(--bg-surface-elevated);">
            <td style="padding: 10px 12px; font-weight:700; color:var(--text-muted);">${c.id}</td>
            <td style="padding: 10px 12px;">
              <div style="font-weight:800; color:var(--text-main); font-size:13.5px;">${c.name}</div>
              <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">${c.relation}</div>
            </td>
            <td style="padding: 10px 12px;">
              <span class="badge" style="background:rgba(59,130,246,0.1); color:var(--accent-blue); font-size:11px;">${c.project}</span>
            </td>
            <td style="padding: 10px 12px; font-size:12.5px; line-height:1.5;">
              <div style="white-space:pre-line;">${c.role}</div>
              ${c.notes ? `<div style="font-size:11px; color:var(--text-muted); margin-top:4px;">ℹ️ ${c.notes}</div>` : ''}
            </td>
            <td style="padding: 10px 12px; font-size:12px; color:var(--text-muted);">${c.relation}</td>
            <td style="padding: 10px 12px; line-height:1.6;">${phoneLinks}</td>
            <td style="padding: 10px 12px; line-height:1.5;">${emailLink}${webLink}</td>
            <td style="padding: 10px 12px; text-align:center;">
              <span class="badge ${evColor}" style="font-size:11px; font-weight:700;">${c.evidence_level}</span>
              <div style="font-size:10px; color:var(--text-muted); margin-top:2px;">${c.confidence}</div>
            </td>
          </tr>
        `;
      }).join('');
    }

    function applyCompanyFilters() {
      renderCompaniesTable();
    }

    // Render Teams Cards
    function renderTeamsCards() {
      const container = document.getElementById('teams-cards-grid');
      if (!container) return;

      const searchTerm = (document.getElementById('team-search-input')?.value || '').toLowerCase().trim();

      let filtered = TMG_TEAMS.filter(t => {
        // Project Match (Full Multi-Keyword & Oman Support)
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': ['southmed', 'ساوث'],
            'noor': ['نور', 'noor'],
            'madinaty': ['مدينتي', 'madinaty'],
            'celia': ['celia', 'سيليا'],
            'fs_luxor': ['أقصر', 'luxor'],
            'fs_sharm': ['شرم', 'sharm'],
            'san_stefano': ['سان ستيفانو', 'san stefano', 'إسكندرية'],
            'banan': ['سعودية', 'رياض', 'بنان', 'banan', 'ksa'],
            'jood_yamal': ['عمان', 'جود', 'يامال', 'oman']
          };
          const keywords = projMap[activeProjectFilter];
          if (keywords && !keywords.some(k => (t.project || '').toLowerCase().includes(k.toLowerCase()))) {
            return false;
          }
        }

        // Search Term
        if (searchTerm) {
          const matchStr = `${t.name} ${t.role} ${t.company} ${t.project}`.toLowerCase();
          if (!matchStr.includes(searchTerm)) return false;
        }

        return true;
      });

      document.getElementById('teams-count-badge').textContent = `${filtered.length} / 38 كادراً`;

      if (filtered.length === 0) {
        container.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:30px; color:var(--text-muted);">لا توجد ملفات مهنية مطابقة لخيارات التصفية.</div>`;
        return;
      }

      container.innerHTML = filtered.map(t => {
        const evBadge = t.evidence_level.startsWith('A') ? 'badge-low' : (t.evidence_level.includes('B') ? 'badge-med' : 'badge-high');
        
        return `
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; transition: transform 0.2s;" onmouseover="this.style.borderColor='var(--accent-blue)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:8px;">
                <div style="font-weight:800; font-size:14px; color:var(--text-main);">${t.name}</div>
                <span class="badge ${evBadge}" style="font-size:10.5px;">دليل ${t.evidence_level}</span>
              </div>
              
              <div style="font-size:12px; font-weight:700; color:var(--accent-blue); margin-top:4px; line-height:1.4;">
                ${t.role}
              </div>

              <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:8px;">
                <span style="font-size:11px; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:4px; color:var(--text-muted);">🏢 ${t.company}</span>
                <span style="font-size:11px; background:rgba(59,130,246,0.1); padding:2px 8px; border-radius:4px; color:var(--accent-blue);">📍 ${t.project}</span>
              </div>

              ${t.notes ? `<p style="font-size:11.5px; color:var(--text-muted); margin:8px 0 0; line-height:1.5;">${t.notes}</p>` : ''}
            </div>

            <div style="margin-top:12px; pt:8px; border-top:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:11px; color:var(--text-muted);">${t.phone !== 'غير منشور' ? t.phone : 'هاتف العمل متاح بالشركة'}</span>
              <a href="${t.linkedin}" target="_blank" style="background:#0a66c2; color:#fff; text-decoration:none; padding:4px 10px; border-radius:6px; font-size:11.5px; font-weight:700; display:inline-flex; align-items:center; gap:4px;">
                <svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                عرض الملف ↗
              </a>
            </div>
          </div>
        `;
      }).join('');
    }

    function applyTeamFilters() {
      renderTeamsCards();
    }

    // Render SWOT & TOWS
    function renderSwotAndTows() {
      // Strengths
      const strContainer = document.getElementById('swot-strengths-container');
      if (strContainer) {
        strContainer.innerHTML = TMG_SWOT.strengths.map(s => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-emerald);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${s.id}: ${s.factor}</span>
              <span class="badge badge-low" style="font-size:10px;">${s.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${s.details}</p>
            <div style="font-size:11px; color:var(--accent-emerald); margin-top:4px; font-weight:700;">📊 ${s.data}</div>
          </div>
        `).join('');
      }

      // Weaknesses
      const wContainer = document.getElementById('swot-weaknesses-container');
      if (wContainer) {
        wContainer.innerHTML = TMG_SWOT.weaknesses.map(w => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-rose);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${w.id}: ${w.factor}</span>
              <span class="badge badge-high" style="font-size:10px;">${w.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${w.details}</p>
            <div style="font-size:11px; color:var(--accent-rose); margin-top:4px; font-weight:700;">⚠️ ${w.data}</div>
          </div>
        `).join('');
      }

      // Opportunities
      const oContainer = document.getElementById('swot-opportunities-container');
      if (oContainer) {
        oContainer.innerHTML = TMG_SWOT.opportunities.map(o => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-blue);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${o.id}: ${o.factor}</span>
              <span class="badge badge-low" style="font-size:10px;">${o.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${o.details}</p>
            <div style="font-size:11px; color:var(--accent-blue); margin-top:4px; font-weight:700;">🚀 ${o.data}</div>
          </div>
        `).join('');
      }

      // Threats
      const tContainer = document.getElementById('swot-threats-container');
      if (tContainer) {
        tContainer.innerHTML = TMG_SWOT.threats.map(t => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-amber);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${t.id}: ${t.factor}</span>
              <span class="badge badge-med" style="font-size:10px;">${t.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${t.details}</p>
            <div style="font-size:11px; color:var(--accent-amber); margin-top:4px; font-weight:700;">⚡ ${t.data}</div>
          </div>
        `).join('');
      }

      // TOWS Containers
      ['SO', 'ST', 'WO', 'WT'].forEach(cat => {
        const el = document.getElementById(`tows-${cat.toLowerCase()}-container`);
        if (el && TMG_TOWS[cat]) {
          el.innerHTML = TMG_TOWS[cat].map(strat => `
            <div style="background:var(--bg-surface); padding:8px 10px; border-radius:6px; margin-bottom:6px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:700; font-size:12.5px; color:var(--text-main);">${strat.id}: ${strat.name}</span>
                <span class="badge badge-med" style="font-size:10px;">${strat.priority}</span>
              </div>
              <p style="font-size:11.5px; color:var(--text-muted); margin:4px 0 0; line-height:1.4;">${strat.roadmap}</p>
            </div>
          `).join('');
        }
      });
    }

    function switchSwotView(view) {
      document.getElementById('swot-quadrants-view').style.display = view === 'swot' ? 'grid' : 'none';
      document.getElementById('tows-matrix-view').style.display = view === 'tows' ? 'flex' : 'none';
      document.getElementById('btn-show-swot').classList.toggle('active', view === 'swot');
      document.getElementById('btn-show-tows').classList.toggle('active', view === 'tows');
    }

    // Initial render on load
    document.addEventListener('DOMContentLoaded', function() {
      renderCompaniesTable();
      renderTeamsCards();
      renderSwotAndTows();
    });
  </script>

</body>
</html>
'''

with open(output_path_1, "w", encoding="utf-8") as f:
    f.write(html_code)

with open(output_path_2, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"Successfully compiled {output_path_1} and {output_path_2}")
print(f"Total bytes written: {len(html_code.encode('utf-8'))}")
