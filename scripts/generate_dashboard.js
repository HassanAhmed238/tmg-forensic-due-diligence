const fs = require('fs');
const path = require('path');

const htmlContent = `<!DOCTYPE html>
<html lang="en" data-theme="dark" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TMG Holding — Forensic Due Diligence & Supply-Chain Risk Intelligence Dashboard</title>
  
  <!-- Google Fonts: Plus Jakarta Sans, JetBrains Mono, Cairo -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- CDN Libraries: Chart.js & D3.js v7 -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://d3js.org/d3.v7.min.js"></script>

  <style>
    /* ==========================================================================
       THEME VARIABLES & HIGH-END DESIGN SYSTEM (Double-Bezel & Haptic Depth)
       ========================================================================== */
    :root {
      /* Dark Theme (Default OLED Luxury) */
      --bg-base: #060911;
      --bg-surface: #0c1220;
      --bg-surface-elevated: #131c31;
      --bg-card: rgba(18, 27, 46, 0.75);
      --bg-card-hover: rgba(25, 38, 64, 0.85);
      --outer-bezel: rgba(255, 255, 255, 0.05);
      --outer-bezel-hover: rgba(6, 182, 212, 0.25);
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
      --table-hover: rgba(6, 182, 212, 0.06);
    }

    [data-theme="light"] {
      /* White Theme (Executive Crisp Paper Luxury) */
      --bg-base: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #f1f5f9;
      --bg-card: #ffffff;
      --bg-card-hover: #f8fafc;
      --outer-bezel: rgba(15, 23, 42, 0.06);
      --outer-bezel-hover: rgba(6, 182, 212, 0.35);
      --border-subtle: #e2e8f0;
      --border-highlight: #cbd5e1;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #64748b;
      
      --accent-cyan: #0284c7;
      --accent-blue: #2563eb;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-rose: #e11d48;
      --accent-purple: #7c3aed;

      --card-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05), inset 0 1px 0 rgba(255, 255, 255, 0.9);
      --kpi-shadow: 0 4px 15px -3px rgba(15, 23, 42, 0.06);

      --diagram-bg: #f8fafc;
      --diagram-border: #cbd5e1;
      --diagram-text: #0284c7;
      --table-stripe: rgba(15, 23, 42, 0.015);
      --table-hover: rgba(2, 132, 199, 0.06);
    }

    /* RTL Layout overrides for Arabic */
    [dir="rtl"] {
      font-family: var(--font-ar);
    }
    [dir="rtl"] .sidebar {
      border-right: none;
      border-left: 1px solid var(--border-subtle);
    }
    [dir="rtl"] .search-box svg {
      left: auto;
      right: 12px;
    }
    [dir="rtl"] .search-box input {
      padding: 7px 34px 7px 14px;
    }
    [dir="rtl"] .nav-btn {
      text-align: right;
    }
    [dir="rtl"] .flag-card {
      border-left: 1px solid var(--border-subtle);
      border-right: 4px solid var(--accent-cyan);
    }
    [dir="rtl"] .step-num {
      left: auto;
      right: 16px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-base);
      color: var(--text-main);
      font-family: var(--font-sans);
      font-size: 13.5px;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      overflow-x: hidden;
      transition: background-color 0.25s cubic-bezier(0.16, 1, 0.3, 1), color 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-base); }
    ::-webkit-scrollbar-thumb { background: var(--border-subtle); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--border-highlight); }

    /* ==========================================================================
       SIDEBAR & NAVIGATION
       ========================================================================== */
    .sidebar {
      width: 280px;
      background: var(--bg-surface);
      border-right: 1px solid var(--border-subtle);
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
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      color: #fff;
      font-size: 18px;
      box-shadow: 0 4px 15px rgba(6, 182, 212, 0.35);
    }

    .brand-title { font-weight: 700; font-size: 14.5px; letter-spacing: -0.02em; }
    .brand-subtitle { font-size: 10.5px; color: var(--text-dim); font-family: var(--font-mono); text-transform: uppercase; letter-spacing: 0.06em; }

    .nav-menu {
      padding: 16px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex: 1;
      overflow-y: auto;
    }

    .nav-label {
      font-size: 10.5px;
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
      padding: 10px 14px;
      border-radius: 9px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      background: transparent;
      border: 1px solid transparent;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      width: 100%;
      text-align: left;
    }

    .nav-btn:hover {
      background: var(--bg-surface-elevated);
      color: var(--text-main);
      border-color: var(--border-subtle);
    }

    .nav-btn.active {
      background: rgba(6, 182, 212, 0.12);
      color: var(--accent-cyan);
      border-color: rgba(6, 182, 212, 0.28);
      font-weight: 600;
    }

    .nav-btn svg { width: 17px; height: 17px; flex-shrink: 0; }

    .sidebar-footer {
      padding: 16px 20px;
      border-top: 1px solid var(--border-subtle);
      background: var(--bg-surface-elevated);
      font-size: 11px;
      color: var(--text-dim);
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    /* ==========================================================================
       TOPBAR & TOOL CONTROLS (Theme Switch, AR/EN, Presenter Mode)
       ========================================================================== */
    .topbar {
      height: 64px;
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
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .badge-status {
      font-size: 11px;
      font-family: var(--font-mono);
      background: rgba(16, 185, 129, 0.12);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.28);
      padding: 2px 9px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 600;
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
      padding: 7px 14px 7px 34px;
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
      width: 270px;
    }
    .search-box svg {
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      width: 14px;
      height: 14px;
      color: var(--text-dim);
    }

    /* Nested Island Controls */
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
      padding: 5px 10px;
      border-radius: 7px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .ctrl-pill:hover {
      color: var(--text-main);
    }

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
      font-weight: 600;
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
       CONTENT AREA & DOUBLE-BEZEL CARDS
       ========================================================================== */
    .content-area {
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 24px;
      max-width: 1680px;
      width: 100%;
      margin: 0 auto;
    }

    .tab-pane { display: none; animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1); }
    .tab-pane.active { display: block; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Double Bezel Card Wrapper */
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
      font-size: 15px;
      font-weight: 700;
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
    .kpi-card:hover {
      transform: translateY(-2px);
    }

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
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .kpi-icon {
      width: 20px;
      height: 20px;
      color: var(--text-dim);
    }

    .kpi-value {
      font-size: 23px;
      font-weight: 800;
      font-family: var(--font-mono);
      letter-spacing: -0.03em;
    }

    .kpi-delta {
      font-size: 11px;
      display: flex;
      align-items: center;
      gap: 5px;
      font-weight: 600;
      flex-wrap: wrap;
    }

    .delta-up { color: var(--accent-emerald); }
    .delta-down { color: var(--accent-rose); }
    .delta-warn { color: var(--accent-amber); }
    .delta-sub { color: var(--text-dim); font-weight: normal; margin-left: 4px; }

    /* Grids */
    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
    .grid-2-1 { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }

    @media (max-width: 1080px) {
      .grid-2, .grid-3, .grid-2-1 { grid-template-columns: 1fr; }
      .sidebar { position: fixed; transform: translateX(-100%); }
      [dir="rtl"] .sidebar { transform: translateX(100%); }
    }

    /* Charts */
    .chart-box {
      position: relative;
      height: 310px;
      width: 100%;
    }

    /* Tables */
    .table-container {
      overflow-x: auto;
      border: 1px solid var(--border-subtle);
      border-radius: 11px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 12.5px;
    }

    [dir="rtl"] table { text-align: right; }

    thead {
      background: var(--bg-surface-elevated);
      border-bottom: 1px solid var(--border-subtle);
    }

    th {
      padding: 12px 14px;
      font-size: 11px;
      text-transform: uppercase;
      color: var(--text-muted);
      font-weight: 700;
      letter-spacing: 0.05em;
    }

    td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-main);
      vertical-align: middle;
    }

    tbody tr:nth-child(even) { background: var(--table-stripe); }
    tbody tr:hover { background: var(--table-hover); }

    .cell-mono { font-family: var(--font-mono); font-size: 12px; }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
    }

    .badge-low { background: rgba(16, 185, 129, 0.12); color: var(--accent-emerald); border: 1px solid rgba(16, 185, 129, 0.25); }
    .badge-med { background: rgba(59, 130, 246, 0.12); color: var(--accent-blue); border: 1px solid rgba(59, 130, 246, 0.25); }
    .badge-medhigh { background: rgba(245, 158, 11, 0.12); color: var(--accent-amber); border: 1px solid rgba(245, 158, 11, 0.25); }
    .badge-high { background: rgba(244, 63, 94, 0.12); color: var(--accent-rose); border: 1px solid rgba(244, 63, 94, 0.25); }

    /* Flags & Steps */
    .flag-card {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-left: 4px solid var(--accent-cyan);
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: var(--kpi-shadow);
    }
    .flag-header { display: flex; align-items: center; justify-content: space-between; }
    .flag-title { font-weight: 700; font-size: 13.5px; }
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
      left: 16px;
      background: var(--accent-cyan);
      color: #fff;
      font-weight: 700;
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
      padding: 5px 12px;
      border-radius: 7px;
      font-size: 12px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .filter-btn:hover { color: var(--text-main); }
    .filter-btn.active {
      background: var(--accent-cyan);
      color: #fff;
      border-color: var(--accent-cyan);
    }

    /* D3 Interactive Graph Container */
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
      right: 14px;
      display: flex;
      gap: 6px;
      z-index: 10;
    }
    [dir="rtl"] .d3-controls {
      right: auto;
      left: 14px;
    }

    /* Node Inspector Drawer */
    #node-inspector {
      position: absolute;
      top: 14px;
      right: 14px;
      width: 320px;
      background: var(--bg-surface);
      border: 1px solid var(--border-highlight);
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
      display: none;
      z-index: 20;
    }
    [dir="rtl"] #node-inspector {
      right: auto;
      left: 14px;
    }
    #node-inspector.active { display: block; animation: fadeIn 0.2s ease; }

    /* ==========================================================================
       PRESENTER MODE (HTML PPT Reveal Deck)
       ========================================================================== */
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
      padding: 40px;
      overflow-y: auto;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .slide-canvas {
      width: 100%;
      max-width: 1280px;
      background: var(--bg-surface);
      border: 1px solid var(--border-highlight);
      border-radius: 20px;
      padding: 40px 48px;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      gap: 24px;
      min-height: 580px;
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
      gap: 20px;
    }

    .speaker-notes-banner {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-left: 4px solid var(--accent-amber);
      border-radius: 10px;
      padding: 14px 18px;
      font-size: 12.5px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 12px;
    }
    [dir="rtl"] .speaker-notes-banner {
      border-left: 1px solid var(--border-subtle);
      border-right: 4px solid var(--accent-amber);
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

    /* Print styles */
    @media print {
      body { background: #fff !important; color: #000 !important; }
      .sidebar, .topbar, #presenter-overlay, .topbar-actions, .filter-group { display: none !important; }
      .main-wrapper { height: auto !important; overflow: visible !important; }
      .tab-pane { display: block !important; margin-bottom: 40px; page-break-after: always; }
      .card { border: 1px solid #ccc !important; background: #fff !important; color: #000 !important; box-shadow: none !important; }
    }
  </style>
</head>
<body>

  <!-- ==========================================================================
       SIDEBAR NAVIGATION
       ========================================================================== -->
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-icon">T</div>
      <div>
        <div class="brand-title" data-i18n="brandTitle">TMG Forensic Intel</div>
        <div class="brand-subtitle" data-i18n="brandSubtitle">Due Diligence Harness</div>
      </div>
    </div>

    <nav class="nav-menu">
      <div class="nav-label" data-i18n="navLabel">Investigation Modules</div>
      
      <button class="nav-btn active" onclick="switchTab('overview')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        <span data-i18n="tabOverview">Executive Dashboard</span>
      </button>

      <button class="nav-btn" onclick="switchTab('procurement')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
        <span data-i18n="tabProcurement">Captive Procurement & Privity</span>
      </button>

      <button class="nav-btn" onclick="switchTab('mustakhlasat')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        <span data-i18n="tabMustakhlasat">المستخلصات & Payment Gate</span>
      </button>

      <button class="nav-btn" onclick="switchTab('projects')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
        <span data-i18n="tabProjects">Project Portfolio & Assets</span>
      </button>

      <button class="nav-btn" onclick="switchTab('contractors')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        <span data-i18n="tabContractors">Master Contractor Roster</span>
      </button>

      <button class="nav-btn" onclick="switchTab('disputes')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>
        <span data-i18n="tabDisputes">Legal, Arbitration & Courts</span>
      </button>

      <button class="nav-btn" onclick="switchTab('financials')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
        <span data-i18n="tabFinancials">Financial Forensics</span>
      </button>

      <button class="nav-btn" onclick="switchTab('sentiment')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"/></svg>
        <span data-i18n="tabSentiment">Resident Sentiment & Grievances</span>
      </button>

      <button class="nav-btn" onclick="switchTab('risks')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
        <span data-i18n="tabRisks">Risk Matrix & Playbooks</span>
      </button>
    </nav>

    <div class="sidebar-footer">
      <div><span data-i18n="cutoffDate">Cut-Off</span>: <strong>11 Oct 2026</strong></div>
      <div><span data-i18n="issuedCapital">Issued Capital</span>: <strong>EGP 20.64 bn</strong></div>
      <div style="color: var(--accent-cyan); margin-top: 4px; font-weight:600;">Hassan Soliman Mode • v3.0</div>
    </div>
  </aside>

  <!-- ==========================================================================
       MAIN VIEWPORT
       ========================================================================== -->
  <div class="main-wrapper">
    <!-- TOP BAR -->
    <header class="topbar">
      <div class="page-title">
        <span id="current-tab-name" data-i18n="headerTitle">Executive Dashboard</span>
        <span class="badge-status" data-i18n="badgeAudited">Audited Primary Verified</span>
      </div>

      <div class="topbar-actions">
        <!-- Search -->
        <div class="search-box">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="global-search" placeholder="Search entity, contractor, case..." data-i18n-ph="searchPlaceholder" onkeyup="handleGlobalSearch(this.value)">
        </div>

        <!-- Language Switcher -->
        <div class="ctrl-group">
          <button id="lang-en" class="ctrl-pill active" onclick="setLanguage('en')">EN</button>
          <button id="lang-ar" class="ctrl-pill" onclick="setLanguage('ar')">عربي</button>
        </div>

        <!-- Theme Toggle -->
        <div class="ctrl-group">
          <button id="theme-dark" class="ctrl-pill active" onclick="setTheme('dark')" title="Dark Mode">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
          </button>
          <button id="theme-light" class="ctrl-pill" onclick="setTheme('light')" title="Light Mode">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
          </button>
        </div>

        <!-- Presenter Mode Button -->
        <button class="btn-action highlight" onclick="openPresenterMode()">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/></svg>
          <span data-i18n="btnPresenter">Presenter Mode</span>
        </button>

        <!-- Export / Print -->
        <button class="btn-action" onclick="window.print()">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
          <span data-i18n="btnPrint">Export / Print</span>
        </button>
      </div>
    </header>

    <div class="content-area">

      <!-- ========================================== -->
      <!-- TAB 1: EXECUTIVE DASHBOARD -->
      <!-- ========================================== -->
      <div id="tab-overview" class="tab-pane active">
        <!-- Top KPIs -->
        <div class="kpi-grid">
          <div class="kpi-card cyan">
            <div class="kpi-header">
              <span class="kpi-title" data-i18n="kpi1Title">Issued & Paid Capital</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
            </div>
            <div class="kpi-value">EGP 20.64 bn</div>
            <div class="kpi-delta delta-up"><span data-i18n="kpi1Delta">● Listed EGX: TMGH</span> <span class="delta-sub">2,063,562,286 shares</span></div>
          </div>

          <div class="kpi-card emerald">
            <div class="kpi-header">
              <span class="kpi-title" data-i18n="kpi2Title">FY2025 Revenue / Net Profit</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
            </div>
            <div class="kpi-value">62.5B / 18.2B</div>
            <div class="kpi-delta delta-up"><span data-i18n="kpi2Delta">▲ +46% Rev / +43% Profit</span> <span class="delta-sub">EGP 7.5bn H1 26</span></div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title" data-i18n="kpi3Title">Creditors & Notes (أوراق دفع)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
            </div>
            <div class="kpi-value">> EGP 15.79 bn</div>
            <div class="kpi-delta delta-down"><span data-i18n="kpi3Delta">▲ Deferred Commercial Notes</span> <span class="delta-sub">90–270 day deferral</span></div>
          </div>

          <div class="kpi-card purple">
            <div class="kpi-header">
              <span class="kpi-title" data-i18n="kpi4Title">Lease Debt Equivalent</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div class="kpi-value">EGP 43.99 bn</div>
            <div class="kpi-delta delta-warn"><span data-i18n="kpi4Delta">▲ Financial Lease Notes</span> <span class="delta-sub">28.6% borrowing cost</span></div>
          </div>

          <div class="kpi-card amber">
            <div class="kpi-header">
              <span class="kpi-title" data-i18n="kpi5Title">Cash Conversion Ratio</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
            </div>
            <div class="kpi-value">31.2%</div>
            <div class="kpi-delta delta-warn"><span data-i18n="kpi5Delta">▼ CFO EGP 3.1bn</span> <span class="delta-sub">vs 9.95bn profit H1 26</span></div>
          </div>
        </div>

        <!-- Charts Grid 1 -->
        <div class="grid-2-1" style="margin-top: 20px;">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" data-i18n="chartFinTitle">Multi-Year Financial Trends (2021 – 2025 + H1 26)</div>
                  <div class="card-subtitle" data-i18n="chartFinSub">Revenue, Net Profit, and Real Estate Contracted Backlog (EGP Billions)</div>
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
                  <div class="card-title" data-i18n="chartCompTitle">Customer Grievance Distribution</div>
                  <div class="card-subtitle" data-i18n="chartCompSub">Indexed resident complaint breakdown (Sample: n=42)</div>
                </div>
              </div>
              <div class="chart-box">
                <canvas id="chartComplaints"></canvas>
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
                  <span data-i18n="coreFindingsTitle">Core Material Verified Conclusions</span>
                </div>
                <div class="card-subtitle" data-i18n="coreFindingsSub">Grounded in corporate filings, court dockets, bank syndications & engineering portfolios</div>
              </div>
            </div>

            <div class="grid-3">
              <div class="flag-card" style="border-left-color: var(--accent-cyan);">
                <div class="flag-header">
                  <span class="flag-title" data-i18n="finding1Title">1. Vertically Integrated Privity Shield</span>
                  <span class="badge badge-med">Structural</span>
                </div>
                <div class="flag-desc" data-i18n="finding1Desc">
                  TMG operates through captive contractor <strong>Alexandria Construction Co. (ACC)</strong> and general package contractors (Atrium). Trade subcontractors contract strictly with ACC/Atrium, denying them legal privity (*نسبية أثر العقود*) to place liens on listed TMG Holding assets or customer receivables.
                </div>
                <div class="flag-footer">
                  <span>Privity: Clean Holding</span>
                  <span>Captive: ACC (8.03% Stake)</span>
                </div>
              </div>

              <div class="flag-card" style="border-left-color: var(--accent-rose);">
                <div class="flag-header">
                  <span class="flag-title" data-i18n="finding2Title">2. Payment Certificate Gatekeeping (المستخلصات)</span>
                  <span class="badge badge-high">Cash-Flow Bottleneck</span>
                </div>
                <div class="flag-desc" data-i18n="finding2Desc">
                  Dedicated quantity surveying and administrative audit layers at Madinaty/Dokki inspect progress claims. Under Egyptian Civil Law, an uncertified progress claim is not an executable due debt (*دين غير حالّ الأداء*), allowing cash preservation during macroeconomic crunches without formal default.
                </div>
                <div class="flag-footer">
                  <span>Impact: Downstream SME Drag</span>
                  <span>Notes Payable: >EGP 15.79B</span>
                </div>
              </div>

              <div class="flag-card" style="border-left-color: var(--accent-amber);">
                <div class="flag-header">
                  <span class="flag-title" data-i18n="finding3Title">3. Institutional Arbitration Shield</span>
                  <span class="badge badge-medhigh">Legal Shield</span>
                </div>
                <div class="flag-desc" data-i18n="finding3Desc">
                  Mandatory confidential CRCICA arbitration clauses remove contractor disputes from public economic courts. Substantial tribunal fees render arbitrating claims under EGP 20M uneconomic for trade SMEs, driving forced commercial discounts on replacement commercial notes.
                </div>
                <div class="flag-footer">
                  <span>Forum: CRCICA (Cairo)</span>
                  <span>Public Records: Suppressed</span>
                </div>
              </div>
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
                <div class="card-title" data-i18n="procurementTitle">Corporate Procurement & Interactive Contractual Privity Network</div>
                <div class="card-subtitle" data-i18n="procurementSub">Interactive D3.js Privity Tree — Click any node to inspect ownership, legal privity shield, and exposure</div>
              </div>
              <div class="filter-group">
                <button class="filter-btn" onclick="resetD3View()" data-i18n="btnResetView">Reset View</button>
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
                  <strong id="inspector-name" style="font-size:13px; color:var(--accent-cyan);">Entity</strong>
                  <button onclick="closeInspector()" style="background:none; border:none; color:var(--text-dim); cursor:pointer; font-size:14px;">✕</button>
                </div>
                <div id="inspector-type" style="font-size:11px; color:var(--text-dim); text-transform:uppercase; margin-bottom:10px;">Type</div>
                <div style="font-size:12px; line-height:1.5; color:var(--text-muted); margin-bottom:8px;" id="inspector-desc">Description</div>
                <div style="border-top:1px solid var(--border-subtle); padding-top:8px; font-size:11px; display:flex; flex-direction:column; gap:4px;">
                  <div><strong>Legal Privity Shield:</strong> <span id="inspector-shield">High</span></div>
                  <div><strong>Downstream Risk:</strong> <span id="inspector-risk">Low</span></div>
                </div>
              </div>
            </div>

            <!-- Explanatory cards -->
            <div class="grid-2" style="margin-top: 20px;">
              <div class="card" style="background: var(--bg-surface-elevated);">
                <div class="card-title" style="color: var(--accent-cyan); margin-bottom: 8px;" data-i18n="privityCard1Title">Why Contractual Privity Matters</div>
                <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.6;" data-i18n="privityCard1Desc">
                  TMG Holding never executes trade-level subcontracts directly. Subcontractors sign with <strong>Alexandria Construction Company (ACC)</strong> or package general contractors (e.g. <strong>Atrium</strong>). If payment delays occur, trade contractors cannot place liens on TMG bank accounts or seize customer installment revenues under Egyptian Civil Code rules (*حجز ما للمدين لدى الغير*).
                </p>
              </div>

              <div class="card" style="background: var(--bg-surface-elevated);">
                <div class="card-title" style="color: var(--accent-amber); margin-bottom: 8px;" data-i18n="privityCard2Title">Decoupling Labor from Materials</div>
                <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.6;" data-i18n="privityCard2Desc">
                  TMG centralized the bulk procurement of rebar steel (Ezz/Beshay) and cement through direct corporate supply agreements. Subcontractors are strictly retained for labor, formwork, and installation. This removes material price speculation but eliminates contractor margin buffers, exposing trade SMEs to acute labor wage inflation.
                </p>
              </div>
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
                <div class="card-title" data-i18n="mustakhlasatTitle">The "Payment Certificate" Gatekeeping Bottleneck (المستخلصات)</div>
                <div class="card-subtitle" data-i18n="mustakhlasatSub">Procedural walkthrough of how progress payments are verified, audited, and deferred</div>
              </div>
            </div>

            <!-- Workflow Graph -->
            <div class="grid-3" style="margin-top: 10px;">
              <div class="step-card">
                <span class="step-num" data-i18n="step1Badge">Step 1: Technical Measurement</span>
                <h4 style="margin-top: 8px; margin-bottom: 6px;" data-i18n="step1Title">حصر هندسي ومطابقة الكميات</h4>
                <p style="color: var(--text-muted); font-size: 12px; line-height:1.6;" data-i18n="step1Desc">
                  ACC site engineering teams review measured work against Bill of Quantities (BOQ). Variations without formal advance written orders are routinely excluded or marked down.
                </p>
              </div>

              <div class="step-card">
                <span class="step-num" data-i18n="step2Badge">Step 2: Central Document Audit</span>
                <h4 style="margin-top: 8px; margin-bottom: 6px;" data-i18n="step2Title">مراجعة الإدارة والتوثيق المالي</h4>
                <p style="color: var(--text-muted); font-size: 12px; line-height:1.6;" data-i18n="step2Desc">
                  Central data entry and document control units at Madinaty / Dokki cross-check submittals. Deficiencies in delivery slips (*أذون استلام موقع*) trigger administrative withholding.
                </p>
              </div>

              <div class="step-card">
                <span class="step-num" data-i18n="step3Badge">Step 3: Deferred Commercial Paper</span>
                <h4 style="margin-top: 8px; margin-bottom: 6px;" data-i18n="step3Title">إصدار أوراق الدفع المؤجلة</h4>
                <p style="color: var(--text-muted); font-size: 12px; line-height:1.6;" data-i18n="step3Desc">
                  Approved *مستخلصات* are disbursed via post-dated checks (90 to 270 days). Operating creditors & notes payable (*الدائنون وأوراق الدفع*) routinely exceed EGP 15.79 billion.
                </p>
              </div>
            </div>

            <div class="flag-card" style="margin-top: 20px; border-left-color: var(--accent-rose);">
              <div class="flag-header">
                <span class="flag-title" data-i18n="defenseTitle">The "Non-Due Debt" Legal Defense (*الدين غير حالّ الأداء*)</span>
                <span class="badge badge-high">Civil Law Shield</span>
              </div>
              <div class="flag-desc" data-i18n="defenseDesc">
                Under Egyptian Civil Law, an uncertified payment certificate does not constitute an enforceable liquid debt (*دين محقق الوجود وحالّ الأداء*). By indefinitely prolonging technical re-surveys and QA/QC document reviews, TMG entities legally conserve cash flow during macro currency crunches without triggering formal contract default on corporate balance sheets.
              </div>
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
                <div class="card-title" data-i18n="projectsTitle">Comprehensive Project Database & Asset Ledger</div>
                <div class="card-subtitle" data-i18n="projectsSub">Verified ownership structures, delivery baselines, and land allocation models</div>
              </div>
              <div class="filter-group" id="project-filters">
                <button class="filter-btn active" onclick="filterProjects('all')" data-i18n="filterAll">All (14)</button>
                <button class="filter-btn" onclick="filterProjects('east-cairo')" data-i18n="filterEastCairo">East Cairo</button>
                <button class="filter-btn" onclick="filterProjects('coastal')" data-i18n="filterCoastal">Coastal / Red Sea</button>
                <button class="filter-btn" onclick="filterProjects('cross-border')" data-i18n="filterCrossBorder">Cross-Border</button>
                <button class="filter-btn" onclick="filterProjects('hospitality')" data-i18n="filterHospitality">Hospitality SPVs</button>
              </div>
            </div>

            <div class="table-container">
              <table id="projects-table">
                <thead>
                  <tr>
                    <th data-i18n="thProjName">Project Name (EN / AR)</th>
                    <th data-i18n="thProjLoc">Location & Land Size</th>
                    <th data-i18n="thProjSPV">Owning SPV & TMG Stake</th>
                    <th data-i18n="thProjLand">Land / Partner Model</th>
                    <th data-i18n="thProjStatus">Delivery Status</th>
                    <th data-i18n="thProjComponents">Key Components & Pipeline</th>
                    <th data-i18n="thProjRisk">Risk Level</th>
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
                <div class="card-title" data-i18n="contractorsTitle">Master Documented Contractor, Supplier & Consultant Registry</div>
                <div class="card-subtitle" data-i18n="contractorsSub">Verified commercial roles, contracted scopes, evidence ratings, and risk levels</div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th data-i18n="thConProj">Project</th>
                    <th data-i18n="thConEntity">TMG Legal Entity</th>
                    <th data-i18n="thConMain">Main Contractor</th>
                    <th data-i18n="thConSub">Subcontractor / Supplier</th>
                    <th data-i18n="thConScope">Scope of Works</th>
                    <th data-i18n="thConEvid">Contract Evidence & Dates</th>
                    <th data-i18n="thConIssue">Documented Issue</th>
                    <th data-i18n="thConRating">Evidence Rating</th>
                    <th data-i18n="thConRisk">Risk</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Madinaty</strong></td>
                    <td>Arab Co. for Projects & Urban Dev.</td>
                    <td>Alexandria Construction Co. (ACC)</td>
                    <td>In-House Trade Teams & SMEs</td>
                    <td>Civil superstructures, infrastructure, 120k units</td>
                    <td>ACC Corporate Filings (Multi-Billion EGP)</td>
                    <td>Delayed *مستخلصات* signoff, commercial paper deferral</td>
                    <td><span class="badge badge-low">Level A</span></td>
                    <td><span class="badge badge-med">Medium</span></td>
                  </tr>
                  <tr>
                    <td><strong>Celia (NAC)</strong></td>
                    <td>Arab Co. for Projects & Urban Dev.</td>
                    <td>Atrium Quality Contractors</td>
                    <td>Al Majd for General Contracting</td>
                    <td>Full Electromechanical (MEP) installations</td>
                    <td>Contractor Portfolios (2017–2023)</td>
                    <td>Back-to-back payment terms, certification delays</td>
                    <td><span class="badge badge-low">Level B</span></td>
                    <td><span class="badge badge-med">Medium</span></td>
                  </tr>
                  <tr>
                    <td><strong>External Infra.</strong></td>
                    <td>Talaat Moustafa Group / ACC</td>
                    <td>Alexandria Construction Co. (ACC)</td>
                    <td>Gemka Group</td>
                    <td>Wastewater MEP: sedimentation bridges, screens</td>
                    <td>Gemka Client Portfolio (2018–2022)</td>
                    <td>Routine retention withholding (5–10%), guarantee periods</td>
                    <td><span class="badge badge-low">Level B</span></td>
                    <td><span class="badge badge-low">Low</span></td>
                  </tr>
                  <tr>
                    <td><strong>Noor City</strong></td>
                    <td>Arab Co. for Urban Investment SAE</td>
                    <td>Alexandria Construction Co. (ACC)</td>
                    <td>Saveto Egypt</td>
                    <td>Supply of dry-mix mortars, wall putties, coatings</td>
                    <td>Manufacturer Portfolio (2021–Present)</td>
                    <td>Exposure to delayed receivables and supply credit cycles</td>
                    <td><span class="badge badge-low">Level B</span></td>
                    <td><span class="badge badge-low">Low</span></td>
                  </tr>
                  <tr>
                    <td><strong>Madinaty Site</strong></td>
                    <td>Arab Co. for Projects & Urban Dev.</td>
                    <td>Alexandria Construction Co. (ACC)</td>
                    <td>In-House Site Security & Labor Force</td>
                    <td>Site security, workforce logistics, perimeter control</td>
                    <td>Labor Reports / Committee for Justice (Aug 2024–2025)</td>
                    <td>Unpaid wage allowances, 14-hr shifts, unpaid overtime</td>
                    <td><span class="badge badge-low">Level B</span></td>
                    <td><span class="badge badge-high">High</span></td>
                  </tr>
                  <tr>
                    <td><strong>Madinaty Hospital</strong></td>
                    <td>Arab Co. for Projects & Urban Dev.</td>
                    <td>TMG Healthcare Arm</td>
                    <td>Alameda Healthcare</td>
                    <td>Hospital operation & medical equipment fit-out</td>
                    <td>USD 100M Venture Agreement Disclosures</td>
                    <td>Institutional co-investment framework</td>
                    <td><span class="badge badge-low">Level A</span></td>
                    <td><span class="badge badge-low">Low</span></td>
                  </tr>
                  <tr>
                    <td><strong>Madinaty / Noor</strong></td>
                    <td>Arab Co. for Projects & Urban Dev.</td>
                    <td>Lead Planners</td>
                    <td>SWA Group / HHCP / Sasaki</td>
                    <td>Master planning, urban zoning, landscape guidelines</td>
                    <td>International Master Planning Archives</td>
                    <td>Completed master design phases</td>
                    <td><span class="badge badge-low">Level A</span></td>
                    <td><span class="badge badge-low">Low</span></td>
                  </tr>
                  <tr>
                    <td><strong>ACC Site Fleet</strong></td>
                    <td>Alexandria Construction Co.</td>
                    <td>ACC Procurement</td>
                    <td>Laser Tech Print / MetroTec</td>
                    <td>Wide-format plotters & electromechanical parts</td>
                    <td>Vendor Portfolios (2019–Present)</td>
                    <td>Standard commercial credit terms (90–120 days)</td>
                    <td><span class="badge badge-low">Level B</span></td>
                    <td><span class="badge badge-low">Low</span></td>
                  </tr>
                  <tr>
                    <td><strong>SouthMed (C01)</strong></td>
                    <td>Arab Co. for Projects & Urban Dev.</td>
                    <td>Concrete Plus for Contracting</td>
                    <td>Direct General Contracting Package</td>
                    <td>Package C01: 179 finished buildings + infra (~EGP 10bn)</td>
                    <td>Joint Corporate Announcement (Jan 2026)</td>
                    <td>Execution pacing for 2029 coastal delivery</td>
                    <td><span class="badge badge-low">Level A</span></td>
                    <td><span class="badge badge-med">Medium</span></td>
                  </tr>
                  <tr>
                    <td><strong>Four Seasons Madinaty</strong></td>
                    <td>Madinaty Co. for Tourism & Urban</td>
                    <td>Alexandria Construction Co. (ACC)</td>
                    <td>Turnkey Hospitality Contractors</td>
                    <td>Luxury hotel superstructures, MEP, finishing</td>
                    <td>EGP 6.76B Banque Misr Syndication</td>
                    <td>Strict lender drawdown engineering certifications</td>
                    <td><span class="badge badge-low">Level A</span></td>
                    <td><span class="badge badge-med">Medium</span></td>
                  </tr>
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
                <div class="card-title" data-i18n="disputesTitle">Judicial Decisions, Commercial Misdemeanors & Arbitration Dockets</div>
                <div class="card-subtitle" data-i18n="disputesSub">Verified court cases across the Egyptian State Council, Cairo Courts & International Tribunals</div>
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 16px;">
              <div class="flag-card" style="border-left-color: var(--accent-rose);">
                <div class="flag-header">
                  <span class="flag-title">Case 12622 / JY 63 — Supreme Administrative Court (Madinaty Concession)</span>
                  <span class="badge badge-high">Level A Judicial</span>
                </div>
                <div class="flag-desc">
                  Public interest lawsuit (Hamdy El-Fakharany et al.) challenging the 2006 direct allocation of 8,000 feddans to Arab Company for Projects & Urban Development without open bidding under Law 89/1998. The court annulled the contract in Sept 2010. <strong>Settlement:</strong> Preserved via 2010/2011 Cabinet decrees and 2015 revised contract requiring TMG to deliver 7% of total residential built-up area to NUCA as in-kind consideration (worth tens of billions of EGP).
                </div>
                <div class="flag-footer">
                  <span>Parties: El-Fakharany vs NUCA / TMG</span>
                  <span>Outcome: Annulled & Settled via 7% In-Kind Delivery</span>
                </div>
              </div>

              <div class="flag-card" style="border-left-color: var(--accent-amber);">
                <div class="flag-header">
                  <span class="flag-title">Case 16522 of 2013 — Cairo Misdemeanor Court (Bad Checks / شيكات بدون رصيد)</span>
                  <span class="badge badge-medhigh">Level A Judicial</span>
                </div>
                <div class="flag-desc">
                  Criminal misdemeanor filings arising from commercial check defaults issued by Arab Company for Projects and Urban Development SAE to commercial counterparties and suppliers during historical liquidity adjustments. Resulted in initial misdemeanor verdicts against authorized signatories, later resolved through financial restructuring and post-dated replacement notes.
                </div>
                <div class="flag-footer">
                  <span>Parties: Commercial Creditors vs ACPUD</span>
                  <span>Outcome: Settled via Rescheduling & Cash Replacement</span>
                </div>
              </div>

              <div class="flag-card" style="border-left-color: var(--accent-blue);">
                <div class="flag-header">
                  <span class="flag-title">CRCICA Mandatory Arbitration Architecture</span>
                  <span class="badge badge-med">Level A / Institutional</span>
                </div>
                <div class="flag-desc">
                  All EPC, package, and commercial supply agreements mandate confidential institutional arbitration under Cairo Regional Centre for International Commercial Arbitration (CRCICA) rules. Major disputes involving liquidated damages (*غرامات التأخير*) or scope terminations are kept out of public courts. High filing fees suppress claims under EGP 20 million from SME subcontractors.
                </div>
                <div class="flag-footer">
                  <span>Counsel: Sarie Eldin & Partners / Matouk Bassiouny</span>
                  <span>Shield: Confidential Private Arbitral Tribunals</span>
                </div>
              </div>

              <div class="flag-card" style="border-left-color: var(--accent-purple);">
                <div class="flag-header">
                  <span class="flag-title">London High Court (Queen's Bench Division) — Al-Azzawi vs. Hisham Talaat Moustafa</span>
                  <span class="badge badge-low">Level A Foreign Court</span>
                </div>
                <div class="flag-desc">
                  Tort damages and psychological injury claim filed in the United Kingdom against TMG's CEO. In July 2025, the London High Court dismissed the claim in its entirety on jurisdictional grounds (*forum non conveniens*), holding that Egyptian courts were the appropriate forum.
                </div>
                <div class="flag-footer">
                  <span>Date: July 2025</span>
                  <span>Outcome: Dismissed on Jurisdictional Grounds</span>
                </div>
              </div>
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
                  <div class="card-title" data-i18n="finCashFlowTitle">Cash Flow Conversion Analysis (H1 2026)</div>
                  <div class="card-subtitle" data-i18n="finCashFlowSub">Net Profit vs Operating Cash Flow vs Working Capital Drain (EGP Millions)</div>
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
                  <div class="card-title" data-i18n="finDebtTitle">Total Debt & Obligation Architecture (30 June 2026)</div>
                  <div class="card-subtitle" data-i18n="finDebtSub">Bank Loans vs Structured Financial Leases vs Customer Advances (EGP bn)</div>
                </div>
              </div>
              <div class="chart-box">
                <canvas id="chartDebtBreakdown"></canvas>
              </div>
            </div>
          </div>
        </div>

        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" data-i18n="finTableTitle">Multi-Year Audited Balance Sheet & P&L Forensic Matrix</div>
                <div class="card-subtitle" data-i18n="finTableSub">All figures in EGP Millions, cross-checked against audited primary statements</div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th data-i18n="thIndicator">Financial Indicator (EGP Millions)</th>
                    <th>FY2021</th>
                    <th>FY2022</th>
                    <th>FY2023</th>
                    <th>FY2024</th>
                    <th>FY2025</th>
                    <th>H1 2026</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Consolidated Revenue</strong></td>
                    <td class="cell-mono">15,357</td>
                    <td class="cell-mono">19,873</td>
                    <td class="cell-mono">28,432</td>
                    <td class="cell-mono">42,700</td>
                    <td class="cell-mono" style="color: var(--accent-cyan); font-weight:700;">62,500</td>
                    <td class="cell-mono">30,190</td>
                  </tr>
                  <tr>
                    <td>— <em>Real Estate Deliveries</em></td>
                    <td class="cell-mono">10,214</td>
                    <td class="cell-mono">14,715</td>
                    <td class="cell-mono">21,630</td>
                    <td class="cell-mono">28,800</td>
                    <td class="cell-mono">36,700</td>
                    <td class="cell-mono">17,000</td>
                  </tr>
                  <tr>
                    <td>— <em>Hospitality & Tourism</em></td>
                    <td class="cell-mono">1,268</td>
                    <td class="cell-mono">2,564</td>
                    <td class="cell-mono">3,545</td>
                    <td class="cell-mono">11,400</td>
                    <td class="cell-mono">14,900</td>
                    <td class="cell-mono">7,500</td>
                  </tr>
                  <tr>
                    <td><strong>Consolidated Net Profit</strong></td>
                    <td class="cell-mono">1,780</td>
                    <td class="cell-mono">2,230</td>
                    <td class="cell-mono">3,310</td>
                    <td class="cell-mono">12,800</td>
                    <td class="cell-mono" style="color: var(--accent-emerald); font-weight:700;">18,200</td>
                    <td class="cell-mono">9,950</td>
                  </tr>
                  <tr>
                    <td>— <em>Attributable to Parent Equity</em></td>
                    <td class="cell-mono">1,780</td>
                    <td class="cell-mono">2,230</td>
                    <td class="cell-mono">3,310</td>
                    <td class="cell-mono">9,800</td>
                    <td class="cell-mono">14,500</td>
                    <td class="cell-mono">7,477</td>
                  </tr>
                  <tr>
                    <td><strong>New Contracted Sales</strong></td>
                    <td class="cell-mono">32,360</td>
                    <td class="cell-mono">33,200</td>
                    <td class="cell-mono">142,700</td>
                    <td class="cell-mono">504,000</td>
                    <td class="cell-mono" style="color: var(--accent-amber);">382,200</td>
                    <td class="cell-mono">219,100</td>
                  </tr>
                  <tr>
                    <td><strong>Contracted Backlog (Unearned)</strong></td>
                    <td class="cell-mono">63,000</td>
                    <td class="cell-mono">77,000</td>
                    <td class="cell-mono">145,000</td>
                    <td class="cell-mono">294,000</td>
                    <td class="cell-mono" style="font-weight:700;">441,200</td>
                    <td class="cell-mono">>460,000</td>
                  </tr>
                  <tr>
                    <td><strong>Operating Creditors & Notes (*أوراق دفع*)</strong></td>
                    <td class="cell-mono">3,400</td>
                    <td class="cell-mono">4,900</td>
                    <td class="cell-mono">8,200</td>
                    <td class="cell-mono">12,400</td>
                    <td class="cell-mono" style="color: var(--accent-rose); font-weight:700;">>15,790</td>
                    <td class="cell-mono">>16,200</td>
                  </tr>
                  <tr>
                    <td><strong>Financial Lease Notes Payable (Off-Bal)</strong></td>
                    <td class="cell-mono">1,200</td>
                    <td class="cell-mono">2,100</td>
                    <td class="cell-mono">4,800</td>
                    <td class="cell-mono">22,100</td>
                    <td class="cell-mono">34,400</td>
                    <td class="cell-mono" style="color: var(--accent-rose); font-weight:700;">43,990</td>
                  </tr>
                  <tr>
                    <td><strong>Customer Advance Payments</strong></td>
                    <td class="cell-mono">38,500</td>
                    <td class="cell-mono">48,200</td>
                    <td class="cell-mono">72,000</td>
                    <td class="cell-mono">95,000</td>
                    <td class="cell-mono">117,680</td>
                    <td class="cell-mono">133,990</td>
                  </tr>
                  <tr>
                    <td><strong>Cash & Liquid Financial Assets</strong></td>
                    <td class="cell-mono">4,210</td>
                    <td class="cell-mono">4,780</td>
                    <td class="cell-mono">11,500</td>
                    <td class="cell-mono">32,000</td>
                    <td class="cell-mono">41,200</td>
                    <td class="cell-mono" style="color: var(--accent-emerald);">66,400</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 8: CUSTOMER SENTIMENT & GRIEVANCES -->
      <!-- ========================================== -->
      <div id="tab-sentiment" class="tab-pane">
        <div class="grid-3">
          <div class="card" style="border-top: 3px solid var(--accent-rose);">
            <div class="card-title" style="margin-bottom: 8px;">1. Maintenance Surcharges (38%)</div>
            <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.6;">
              Systematic demands for annual "maintenance deficit differences" (فروق الصيانة) between EGP 15,000 and 45,000 per unit. Residents complain that HOA trust accounting balances and earned deposit interest are not disclosed in certified reports.
            </p>
          </div>

          <div class="card" style="border-top: 3px solid var(--accent-amber);">
            <div class="card-title" style="margin-bottom: 8px;">2. Resale Transfer Fees (26%)</div>
            <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.6;">
              Charging 5%–10% of resale value or flat administrative fees (EGP 50k–100k) upon unit transfer. Direct contradiction with Article 15 of Egyptian Consumer Protection Law No. 181/2018 which declares all resale commission clauses null and void.
            </p>
          </div>

          <div class="card" style="border-top: 3px solid var(--accent-blue);">
            <div class="card-title" style="margin-bottom: 8px;">3. Handover Delays (18%)</div>
            <p style="color: var(--text-muted); font-size: 12.5px; line-height: 1.6;">
              Documented 12 to 18-month delivery slippages in secondary phases of Celia (New Capital) and luxury hotel pipeline (Four Seasons Luxor delayed to 2026, Marsa Alam to 2027). TMG shields itself via force majeure and utility readiness clauses.
            </p>
          </div>
        </div>

        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" data-i18n="complaintTableTitle">Granular Resident Experience & Complaint Log</div>
                <div class="card-subtitle" data-i18n="complaintTableSub">Documented across community forums, judicial petitions, and consumer authority logs</div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Project</th>
                    <th>Issue Category</th>
                    <th>Documented Claim / Experience</th>
                    <th>Date Recorded</th>
                    <th>Source / Platform</th>
                    <th>Legal & Analytical Classification</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Madinaty</strong></td>
                    <td>Maintenance Surcharge</td>
                    <td>Issuance of annual invoices for maintenance differences (EGP 15k–40k); residents demand certified bank account disclosure of the original deposit yield.</td>
                    <td>Jan 2025</td>
                    <td>TMG Life App / Community Action</td>
                    <td><span class="badge badge-medhigh">Verified Fact (Accounting Lawsuits Pending)</span></td>
                  </tr>
                  <tr>
                    <td><strong>Madinaty</strong></td>
                    <td>Resale Transfer Fee</td>
                    <td>Sellers forced to pay administrative fees upon resale; CPA disputes cite Article 15 of Law 181/2018 banning developer resale percentages.</td>
                    <td>2024–2026</td>
                    <td>Consumer Protection Agency Filings</td>
                    <td><span class="badge badge-high">Verified Legal Dispute</span></td>
                  </tr>
                  <tr>
                    <td><strong>Celia (NAC)</strong></td>
                    <td>Delivery Slippage</td>
                    <td>Phases 3 and 4 apartment handovers delayed 14–18 months; developer cited municipal power and water connection delays by ACUD.</td>
                    <td>Mid 2024</td>
                    <td>Buyer Association Notices</td>
                    <td><span class="badge badge-med">Verified Operational Delay</span></td>
                  </tr>
                  <tr>
                    <td><strong>Madinaty</strong></td>
                    <td>Security & Labor</td>
                    <td>Security personnel employed via Alexandria Construction petitioned Ministry of Labor over 12-hour shifts, overtime pay, and contract terms.</td>
                    <td>29 Oct 2025</td>
                    <td>Al Manassa Investigative Report</td>
                    <td><span class="badge badge-med">Documented Labor Grievance</span></td>
                  </tr>
                  <tr>
                    <td><strong>Madinaty & Rehab</strong></td>
                    <td>Asset Appreciation</td>
                    <td>Exceptional secondary market capital appreciation (>400% in EGP from 2022 to 2026); top-tier landscaping, integrated sports clubs, and private transit.</td>
                    <td>Continuous</td>
                    <td>Aqarmap / Nawy Resale Indexes</td>
                    <td><span class="badge badge-low">Verified Highly Positive Driver</span></td>
                  </tr>
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
                <div class="card-title" data-i18n="riskTableTitle">Forensic Risk Register & Severity Matrix</div>
                <div class="card-subtitle" data-i18n="riskTableSub">Evaluating likelihood, potential impact, observable triggers, and suggested diligence controls</div>
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Risk Category</th>
                    <th>Severity</th>
                    <th>Likelihood</th>
                    <th>Mechanisms & Operational Indicators</th>
                    <th>Actionable Diligence Control</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Contractual Privity Insulation</strong></td>
                    <td><span class="badge badge-high">Critical</span></td>
                    <td>High</td>
                    <td>TMG Holding off contract books; contracts signed with ACC or Atrium, removing legal recourse against parent.</td>
                    <td>Verify corporate registration (*سجل تجاري*) of signing counterparty; do not rely on TMG tender branding.</td>
                  </tr>
                  <tr>
                    <td><strong>Payment Deferral (*أوراق دفع*)</strong></td>
                    <td><span class="badge badge-high">High</span></td>
                    <td>High</td>
                    <td>Use of quantity surveying layers to delay *مستخلصات*; deferred notes payable exceeding EGP 15.79B (90–270 days).</td>
                    <td>Track engineer measurement signoff delays; monitor requests for post-dated checks in lieu of bank wires.</td>
                  </tr>
                  <tr>
                    <td><strong>CRCICA Dispute Barrier</strong></td>
                    <td><span class="badge badge-high">High</span></td>
                    <td>High</td>
                    <td>Mandatory arbitration clauses make legal recovery uneconomic for claims below EGP 20M due to filing fees.</td>
                    <td>Negotiate expedited local summary court jurisdiction for claims under defined monetary thresholds.</td>
                  </tr>
                  <tr>
                    <td><strong>Inflation & Price Escalation</strong></td>
                    <td><span class="badge badge-high">High</span></td>
                    <td>Med-High</td>
                    <td>Reluctance by ACC to grant price indexation (*فروق أسعار*) absent formal back-to-back developer signoffs.</td>
                    <td>Insist on explicit material indexation tied to Egyptian Ministry of Housing monthly cost bulletins (*نشرة الأسعار*).</td>
                  </tr>
                  <tr>
                    <td><strong>Working Capital / Retention</strong></td>
                    <td><span class="badge badge-medhigh">Medium</span></td>
                    <td>High</td>
                    <td>Extended retention release cycles (5–10%) tied to master city handover rather than package completion.</td>
                    <td>Insist on package-specific acceptance certificates (*محضر استلام ابتدائي للعملية*) triggering bond release.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Stakeholder Playbooks -->
        <div class="grid-2" style="margin-top: 20px;">
          <div class="card" style="border-top: 3px solid var(--accent-cyan);">
            <div class="card-title" style="margin-bottom: 12px; color: var(--accent-cyan);" data-i18n="playbookSubTitle">Playbook for Subcontractors & Suppliers</div>
            <ul style="color: var(--text-muted); font-size: 12.5px; line-height: 1.7; padding-left: 18px;">
              <li><strong>Reject "Pay-When-Paid" Clauses:</strong> Eliminate terms making your *مستخلص* contingent upon developer releases to ACC.</li>
              <li><strong>Zero Verbal Variations:</strong> Never execute works without a written Variation Order (*أمر تغيير*) signed by authorized executives.</li>
              <li><strong>Establish Commercial Default:</strong> Serve formal court bailiff notices (*إنذار رسمي على يد محضر*) to establish statutory 5% commercial interest.</li>
              <li><strong>Retention of Title:</strong> Retain legal title (*شرط الاحتفاظ بالملكية*) on delivered equipment until full check clearance.</li>
            </ul>
          </div>

          <div class="card" style="border-top: 3px solid var(--accent-emerald);">
            <div class="card-title" style="margin-bottom: 12px; color: var(--accent-emerald);" data-i18n="playbookInvTitle">Playbook for Institutional Investors & Banks</div>
            <ul style="color: var(--text-muted); font-size: 12.5px; line-height: 1.7; padding-left: 18px;">
              <li><strong>Holding-Level Balance Sheet Strength:</strong> Captive contracting insulates TMG Holding from subcontractor claims, maintaining high headline liquidity.</li>
              <li><strong>Monitor Creditors Velocity:</strong> Track trade payables and notes (*الدائنون وأوراق الدفع*) relative to WIP inventory to spot site-level friction.</li>
              <li><strong>Downstream Re-Tendering Risk:</strong> Severe inflation passed to SME contractors can trigger site walk-offs, threatening delivery targets on Noor and Celia.</li>
              <li><strong>Verify DSCR Headroom:</strong> Factor in EGP 44bn financial lease liabilities alongside bank borrowings when calculating true debt service coverage.</li>
            </ul>
          </div>
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
            <div class="slide-number" id="presenter-slide-num">SLIDE 01 / 08</div>
            <h2 id="presenter-slide-title" style="font-size: 22px; font-weight: 800; margin-top: 4px;">Executive Dashboard & Macro Overview</h2>
          </div>
          <button class="btn-action" onclick="closePresenterMode()">✕ Exit (Esc)</button>
        </div>

        <div class="slide-body" id="presenter-slide-content">
          <!-- Dynamically populated via JS -->
        </div>

        <div class="speaker-notes-banner">
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="flex-shrink:0; color:var(--accent-amber);"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          <div>
            <strong>Forensic Due Diligence Takeaway:</strong>
            <span id="presenter-speaker-note">TMG Holding operates a captive contractor model that insulates parent balance sheets while accumulating deferred contractor notes (>EGP 15.79B).</span>
          </div>
        </div>
      </div>
    </div>

    <div class="presenter-dock">
      <div style="font-size: 12px; color: var(--text-dim); display:flex; gap:16px;">
        <span>Press <kbd>←</kbd> <kbd>→</kbd> or <kbd>Space</kbd> to Navigate</span>
        <span>Press <kbd>F</kbd> for Fullscreen</span>
      </div>

      <div style="display: flex; gap: 8px; align-items: center;">
        <button class="btn-action" onclick="prevSlide()">❮ Previous</button>
        <span id="presenter-dock-indicator" style="font-family: var(--font-mono); font-size: 13px; font-weight: 600; padding: 0 8px;">1 / 8</span>
        <button class="btn-action" onclick="nextSlide()">Next ❯</button>
        <button class="btn-action" onclick="toggleFullScreen()">⛶ Fullscreen</button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       CORE JAVASCRIPT & DATA CONTROLLER
       ========================================================================== -->
  <script>
    /* ==========================================================================
       I18N DICTIONARY (ARABIC / ENGLISH BILINGUAL HARNESS)
       ========================================================================== */
    const i18n = {
      en: {
        brandTitle: "TMG Forensic Intel",
        brandSubtitle: "Due Diligence Harness",
        navLabel: "Investigation Modules",
        tabOverview: "Executive Dashboard",
        tabProcurement: "Captive Procurement & Privity",
        tabMustakhlasat: "المستخلصات & Payment Gate",
        tabProjects: "Project Portfolio & Assets",
        tabContractors: "Master Contractor Roster",
        tabDisputes: "Legal, Arbitration & Courts",
        tabFinancials: "Financial Forensics",
        tabSentiment: "Resident Sentiment & Grievances",
        tabRisks: "Risk Matrix & Playbooks",
        cutoffDate: "Cut-Off",
        issuedCapital: "Issued Capital",
        headerTitle: "Executive Dashboard",
        badgeAudited: "Audited Primary Verified",
        searchPlaceholder: "Search entity, contractor, case...",
        btnPresenter: "Presenter Mode",
        btnPrint: "Export / Print",
        kpi1Title: "Issued & Paid Capital",
        kpi1Delta: "● Listed EGX: TMGH",
        kpi2Title: "FY2025 Revenue / Net Profit",
        kpi2Delta: "▲ +46% Rev / +43% Profit",
        kpi3Title: "Creditors & Notes (أوراق دفع)",
        kpi3Delta: "▲ Deferred Commercial Notes",
        kpi4Title: "Lease Debt Equivalent",
        kpi4Delta: "▲ Financial Lease Notes",
        kpi5Title: "Cash Conversion Ratio",
        kpi5Delta: "▼ CFO EGP 3.1bn",
        chartFinTitle: "Multi-Year Financial Trends (2021 – 2025 + H1 26)",
        chartFinSub: "Revenue, Net Profit, and Real Estate Contracted Backlog (EGP Billions)",
        chartCompTitle: "Customer Grievance Distribution",
        chartCompSub: "Indexed resident complaint breakdown (Sample: n=42)",
        coreFindingsTitle: "Core Material Verified Conclusions",
        coreFindingsSub: "Grounded in corporate filings, court dockets, bank syndications & engineering portfolios",
        finding1Title: "1. Vertically Integrated Privity Shield",
        finding1Desc: "TMG operates through captive contractor Alexandria Construction Co. (ACC) and general package contractors (Atrium). Trade subcontractors contract strictly with ACC/Atrium, denying them legal privity to place liens on listed TMG Holding assets or customer receivables.",
        finding2Title: "2. Payment Certificate Gatekeeping (المستخلصات)",
        finding2Desc: "Dedicated quantity surveying and administrative audit layers at Madinaty/Dokki inspect progress claims. Under Egyptian Civil Law, an uncertified progress claim is not an executable due debt, allowing cash preservation during macroeconomic crunches without formal default.",
        finding3Title: "3. Institutional Arbitration Shield",
        finding3Desc: "Mandatory confidential CRCICA arbitration clauses remove contractor disputes from public economic courts. Substantial tribunal fees render arbitrating claims under EGP 20M uneconomic for trade SMEs, driving forced commercial discounts on replacement commercial notes.",
        procurementTitle: "Corporate Procurement & Interactive Contractual Privity Network",
        procurementSub: "Interactive D3.js Privity Tree — Click any node to inspect ownership, legal privity shield, and exposure",
        btnResetView: "Reset View",
        privityCard1Title: "Why Contractual Privity Matters",
        privityCard1Desc: "TMG Holding never executes trade-level subcontracts directly. Subcontractors sign with Alexandria Construction Company (ACC) or package general contractors (e.g. Atrium). If payment delays occur, trade contractors cannot place liens on TMG bank accounts or seize customer installment revenues under Egyptian Civil Code rules.",
        privityCard2Title: "Decoupling Labor from Materials",
        privityCard2Desc: "TMG centralized the bulk procurement of rebar steel (Ezz/Beshay) and cement through direct corporate supply agreements. Subcontractors are strictly retained for labor, formwork, and installation. This removes material price speculation but eliminates contractor margin buffers, exposing trade SMEs to acute labor wage inflation.",
        mustakhlasatTitle: "The \"Payment Certificate\" Gatekeeping Bottleneck (المستخلصات)",
        mustakhlasatSub: "Procedural walkthrough of how progress payments are verified, audited, and deferred",
        step1Badge: "Step 1: Technical Measurement",
        step1Title: "حصر هندسي ومطابقة الكميات",
        step1Desc: "ACC site engineering teams review measured work against Bill of Quantities (BOQ). Variations without formal advance written orders are routinely excluded or marked down.",
        step2Badge: "Step 2: Central Document Audit",
        step2Title: "مراجعة الإدارة والتوثيق المالي",
        step2Desc: "Central data entry and document control units at Madinaty / Dokki cross-check submittals. Deficiencies in delivery slips trigger administrative withholding.",
        step3Badge: "Step 3: Deferred Commercial Paper",
        step3Title: "إصدار أوراق الدفع المؤجلة",
        step3Desc: "Approved مستخلصات are disbursed via post-dated checks (90 to 270 days). Operating creditors & notes payable routinely exceed EGP 15.79 billion.",
        defenseTitle: "The \"Non-Due Debt\" Legal Defense (الدين غير حالّ الأداء)",
        defenseDesc: "Under Egyptian Civil Law, an uncertified payment certificate does not constitute an enforceable liquid debt. By indefinitely prolonging technical re-surveys and QA/QC document reviews, TMG entities legally conserve cash flow during macro currency crunches without triggering formal contract default on corporate balance sheets.",
        projectsTitle: "Comprehensive Project Database & Asset Ledger",
        projectsSub: "Verified ownership structures, delivery baselines, and land allocation models",
        filterAll: "All (14)",
        filterEastCairo: "East Cairo",
        filterCoastal: "Coastal / Red Sea",
        filterCrossBorder: "Cross-Border",
        filterHospitality: "Hospitality SPVs",
        thProjName: "Project Name (EN / AR)",
        thProjLoc: "Location & Land Size",
        thProjSPV: "Owning SPV & TMG Stake",
        thProjLand: "Land / Partner Model",
        thProjStatus: "Delivery Status",
        thProjComponents: "Key Components & Pipeline",
        thProjRisk: "Risk Level",
        contractorsTitle: "Master Documented Contractor, Supplier & Consultant Registry",
        contractorsSub: "Verified commercial roles, contracted scopes, evidence ratings, and risk levels",
        thConProj: "Project",
        thConEntity: "TMG Legal Entity",
        thConMain: "Main Contractor",
        thConSub: "Subcontractor / Supplier",
        thConScope: "Scope of Works",
        thConEvid: "Contract Evidence & Dates",
        thConIssue: "Documented Issue",
        thConRating: "Evidence Rating",
        thConRisk: "Risk",
        disputesTitle: "Judicial Decisions, Commercial Misdemeanors & Arbitration Dockets",
        disputesSub: "Verified court cases across the Egyptian State Council, Cairo Courts & International Tribunals",
        finCashFlowTitle: "Cash Flow Conversion Analysis (H1 2026)",
        finCashFlowSub: "Net Profit vs Operating Cash Flow vs Working Capital Drain (EGP Millions)",
        finDebtTitle: "Total Debt & Obligation Architecture (30 June 2026)",
        finDebtSub: "Bank Loans vs Structured Financial Leases vs Customer Advances (EGP bn)",
        finTableTitle: "Multi-Year Audited Balance Sheet & P&L Forensic Matrix",
        finTableSub: "All figures in EGP Millions, cross-checked against audited primary statements",
        thIndicator: "Financial Indicator (EGP Millions)",
        complaintTableTitle: "Granular Resident Experience & Complaint Log",
        complaintTableSub: "Documented across community forums, judicial petitions, and consumer authority logs",
        riskTableTitle: "Forensic Risk Register & Severity Matrix",
        riskTableSub: "Evaluating likelihood, potential impact, observable triggers, and suggested diligence controls",
        playbookSubTitle: "Playbook for Subcontractors & Suppliers",
        playbookInvTitle: "Playbook for Institutional Investors & Banks"
      },
      ar: {
        brandTitle: "استخبارات طلعت مصطفى الجنائية",
        brandSubtitle: "درع الفحص النافي للجهالة",
        navLabel: "وحدات التحقيق الجنائي",
        tabOverview: "لوحة القيادة التنفيذية",
        tabProcurement: "المشتريات المدمجة والدرع القانوني",
        tabMustakhlasat: "المستخلصات وعقبة دورة المدفوعات",
        tabProjects: "محفظة المشاريع والأصول العقارية",
        tabContractors: "سجل المقاولين والموردين والاستشاريين",
        tabDisputes: "الأحكام القضائية والتحكيم والنزاعات",
        tabFinancials: "التحليل المالي الجنائي والسيولة",
        tabSentiment: "شكاوى السكان ومؤشر رضا العملاء",
        tabRisks: "مصفوفة المخاطر ودليل التحوط",
        cutoffDate: "تاريخ التحديث",
        issuedCapital: "رأس المال المصدر",
        headerTitle: "لوحة القيادة التنفيذية",
        badgeAudited: "مدقق رسمياً من الإفصاحات",
        searchPlaceholder: "ابحث عن كيان، مقاول، قضية...",
        btnPresenter: "وضع العرض التنفيذي",
        btnPrint: "طباعة / تصدير PDF",
        kpi1Title: "رأس المال المصدر والمدفوع",
        kpi1Delta: "● مدرج بالبورصة المصرية: TMGH",
        kpi2Title: "إيرادات / أرباح 2025 المجمعة",
        kpi2Delta: "▲ +46% إيرادات / +43% أرباح",
        kpi3Title: "الدائنون وأوراق الدفع التجارية",
        kpi3Delta: "▲ أوراق دفع وشيكات مؤجلة",
        kpi4Title: "التزامات عقود التأجير التمويلي",
        kpi4Delta: "▲ تمويلات هيكلية خارج الميزانية",
        kpi5Title: "معدل تحويل السيولة النقدية",
        kpi5Delta: "▼ تدفق تشغيلي 3.1 مليار",
        chartFinTitle: "المؤشرات المالية التاريخية (2021 – 2025 + النصف الأول 2026)",
        chartFinSub: "الإيرادات، صافي الأرباح، والمبيعات المتعاقد عليها غير المسلمة (مليار جنيه)",
        chartCompTitle: "توزيع شكاوى السكان والعملاء",
        chartCompSub: "تحليل إحصائي لمطالبات الملاك (عينة موثقة: 42 شكوى)",
        coreFindingsTitle: "النتائج الجوهرية المدققة للفحص النافي للجهالة",
        coreFindingsSub: "مستندة للإفصاحات الرسمية، الأحكام القضائية، عقود القروض المشتركة وسجلات التنفيذ",
        finding1Title: "1. الدرع القانوني للمشتريات المدمجة",
        finding1Desc: "تنفذ المجموعة مشروعاتها عبر شركة الإسكندرية للإنشاءات (ACC) ومقاولي حزم مستقلين (أتريوم). مقاولو الباطن يتعاقدون حصرياً مع شركة المقاولات، مما يحرمهم من الحجية النسبية للعقد ضد الشركة القابضة أو الحجز على حساباتها.",
        finding2Title: "2. عقبة اعتماد المستخلصات الجارية",
        finding2Desc: "تعمل مكاتب الحصر والتوثيق بمدينتي والدقي على التدقيق المطول للكميات. طبقاً للقانون المدني المصري، لا يُعد المستخلص غير المعتمد ديناً محقق الوجود وحالّ الأداء، مما يسمح بحفظ السيولة دون إعلان تعثر مالي.",
        finding3Title: "3. درع التحكيم الإجباري (CRCICA)",
        finding3Desc: "تنص كافة العقود على التحكيم السري بمركز القاهرة الدولي للتحكيم (CRCICA). رسوم قيد التحكيم المرتفعة تجعل مقاضاة المطالبات دون 20 مليون جنيه غير مجدية اقتصادياً لصغار المقاولين، مما يفرض عليهم خصومات تجارية إجبارية.",
        procurementTitle: "هيكل المشتريات المدمجة والشبكة التفاعلية للحجية النسبية للعقود",
        procurementSub: "شجرة D3.js التفاعلية — انقر فوق أي عقدة لفحص نسبة الملكية والدرع القانوني ومستوى المخاطر",
        btnResetView: "إعادة ضبط العرض",
        privityCard1Title: "أهمية مبدأ نسبية أثر العقود",
        privityCard1Desc: "لا توقع طلعت مصطفى القابضة أي عقود مباشرة مع مقاولي الباطن، بل تقتصر التعاقدات على شركة الإسكندرية للإنشاءات أو المقاولين العموميين. يمنع ذلك مقاولي الباطن من الحجز الإداري أو القضائي على التدفقات المالية للملاك.",
        privityCard2Title: "فصل توريد الخامات عن المصنعيات",
        privityCard2Desc: "تتولى طلعت مصطفى التوريد المركزي للحديد (عز/بشاي) والأسمنت. يتعاقد مقاولو الباطن على المصنعيات والمعدات فقط، مما يجرد المقاول من هوامش أرباح التوريد ويعرضه للتآكل المالي جراء تضخم أجور العمالة.",
        mustakhlasatTitle: "عقبة دورة اعتماد مستخلصات المقاولين",
        mustakhlasatSub: "التسلسل الإجرائي لتدقيق واعتماد وصرف دفعات الإنجاز التجاري",
        step1Badge: "المرحلة الأولى: الحصر الفني",
        step1Title: "حصر هندسي ومطابقة الكميات",
        step1Desc: "تقوم أطقم مهندسي الموقع بشركة الإسكندرية بمطابقة الأعمال المنفذة مع جداول الكميات. يتم استبعاد أو خصم بنود التغييرات غير المعتمدة مسبقاً بأمر كتابي.",
        step2Badge: "المرحلة الثانية: التدقيق المركزي",
        step2Title: "مراجعة الإدارة والتوثيق المالي",
        step2Desc: "تتولى وحدات إدخال البيانات والتوثيق بمدينتي والدقي فحص أذون الاستلام. أي نقص في أذون التشوين أو الاستلام يوقف صرف المستخلص إدارياً.",
        step3Badge: "المرحلة الثالثة: إصدار أوراق الدفع",
        step3Title: "إصدار أوراق الدفع والشيكات المؤجلة",
        step3Desc: "يتم صرف المستخلصات المعتمدة بشيكات آجلة (من 90 إلى 270 يوماً). تتجاوز أوراق الدفع والدائنون التجاريون حاجز 15.79 مليار جنيه بالمجموعة.",
        defenseTitle: "الدفاع القانوني بعدم حلول أجل الدين (*الدين غير حالّ الأداء*)",
        defenseDesc: "طبقاً لأحكام القانون المدني المصري، لا يشكل المستخلص غير المعتمد نهائياً سنداً تنفيذياً لدين محقق الوجود وحالّ الأداء. تستغل المجموعة هذا التكييف لإطالة أمد الحصر دون اعتبارها متعثرة قانوناً أمام البنوك.",
        projectsTitle: "قاعدة البيانات الشاملة لمحفظة المشاريع والأصول",
        projectsSub: "هياكل الملكية الموثقة، تواريخ التسليم التعاقدية، ونماذج الشراكة على الأراضي",
        filterAll: "الكل (14)",
        filterEastCairo: "شرق القاهرة",
        filterCoastal: "الساحل والبحر الأحمر",
        filterCrossBorder: "خارج الحدود (السعودية)",
        filterHospitality: "شركات الفنادق التابعة",
        thProjName: "اسم المشروع",
        thProjLoc: "الموقع والمساحة",
        thProjSPV: "الشركة المالكة وحصة طلعت",
        thProjLand: "نموذج الشراكة والأرض",
        thProjStatus: "موقف التسليم الفعلي",
        thProjComponents: "المكونات الأساسية والوحدات",
        thProjRisk: "مستوى المخاطرة",
        contractorsTitle: "السجل الحصري للمقاولين والموردين والاستشاريين المعتمدين",
        contractorsSub: "الأدوار التعاقدية الموثقة، نطاقات الأعمال، ودرجات قوة الإثبات",
        thConProj: "المشروع",
        thConEntity: "كيان طلعت مصطفى المتعاقد",
        thConMain: "المقاول الرئيسي",
        thConSub: "مقاول الباطن / المورد",
        thConScope: "نطاق الأعمال المنفذة",
        thConEvid: "مستند العلاقة والتواريخ",
        thConIssue: "الملاحظة التوثيقية",
        thConRating: "درجة الإثبات",
        thConRisk: "المخاطرة",
        disputesTitle: "الأحكام القضائية، الجنح التجارية وسجلات التحكيم المؤسسي",
        disputesSub: "القضايا الموثقة بمجلس الدولة، المحاكم الاقتصادية ومحاكم الجنح والتحكيم الدولي",
        finCashFlowTitle: "تحليل كفاءة تحويل السيولة النقدية (النصف الأول 2026)",
        finCashFlowSub: "صافي الأرباح مقابل التدفق النقدي التشغيلي واستنزاف رأس المال العامل (مليون جنيه)",
        finDebtTitle: "هيكل الالتزامات والديون الإجمالية (30 يونيو 2026)",
        finDebtSub: "القروض البنكية مقابل التأجير التمويلي ودفعات العملاء المقدمة (مليار جنيه)",
        finTableTitle: "المصفوفة المالية الجنائية للقوائم المدققة وميزانيات المجموعة",
        finTableSub: "كافة الأرقام بملايين الجنيهات المصرية، مدققة من تقارير مراقبي الحسابات",
        thIndicator: "المؤشر المالي (مليون جنيه)",
        complaintTableTitle: "سجل الشكاوى ونزاعات الملاك التفصيلي",
        complaintTableSub: "مرصود من اتحادات الشاغلين، بلاغات حماية المستهلك والدعاوى القضائية",
        riskTableTitle: "مصفوفة المخاطر الجنائية ومؤشرات الإنذار المبكر",
        riskTableSub: "تقييم الأثر، احتمالية الحدوث، آليات الرصد، وخطط التحوط النافية للجهالة",
        playbookSubTitle: "دليل التحوط لمقاولي الباطن والموردين",
        playbookInvTitle: "دليل الفحص للبنوك والمستثمرين المؤسسيين"
      }
    };

    let currentLang = 'en';
    let currentTheme = 'dark';

    function setLanguage(lang) {
      currentLang = lang;
      document.documentElement.setAttribute('lang', lang);
      document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

      document.getElementById('lang-en').classList.toggle('active', lang === 'en');
      document.getElementById('lang-ar').classList.toggle('active', lang === 'ar');

      // Update text nodes with data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (i18n[lang][key]) {
          el.textContent = i18n[lang][key];
        }
      });

      // Update placeholders
      document.querySelectorAll('[data-i18n-ph]').forEach(el => {
        const key = el.getAttribute('data-i18n-ph');
        if (i18n[lang][key]) {
          el.setAttribute('placeholder', i18n[lang][key]);
        }
      });

      // Re-render projects table
      renderProjects(currentFilteredProjects);

      // Re-render D3 text if available
      renderD3PrivityTree();

      // Update active tab title in topbar
      const currentTab = document.querySelector('.nav-btn.active').getAttribute('onclick').match(/'([^']+)'/)[1];
      const tabTitleKeys = {
        'overview': 'tabOverview',
        'procurement': 'tabProcurement',
        'mustakhlasat': 'tabMustakhlasat',
        'projects': 'tabProjects',
        'contractors': 'tabContractors',
        'disputes': 'tabDisputes',
        'financials': 'tabFinancials',
        'sentiment': 'tabSentiment',
        'risks': 'tabRisks'
      };
      document.getElementById('current-tab-name').textContent = i18n[lang][tabTitleKeys[currentTab]] || 'Dashboard';
      localStorage.setItem('tmg_lang', lang);
    }

    function setTheme(theme) {
      currentTheme = theme;
      document.documentElement.setAttribute('data-theme', theme);
      document.getElementById('theme-dark').classList.toggle('active', theme === 'dark');
      document.getElementById('theme-light').classList.toggle('active', theme === 'light');
      localStorage.setItem('tmg_theme', theme);

      // Re-render charts with proper grid/tick colors
      updateChartsTheme(theme);
    }

    /* ==========================================================================
       TAB SWITCHING
       ========================================================================== */
    function switchTab(tabId) {
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
      
      const targetPane = document.getElementById('tab-' + tabId);
      if (targetPane) targetPane.classList.add('active');

      const activeBtn = Array.from(document.querySelectorAll('.nav-btn')).find(b => b.getAttribute('onclick').includes(tabId));
      if (activeBtn) activeBtn.classList.add('active');

      const tabTitleKeys = {
        'overview': 'tabOverview',
        'procurement': 'tabProcurement',
        'mustakhlasat': 'tabMustakhlasat',
        'projects': 'tabProjects',
        'contractors': 'tabContractors',
        'disputes': 'tabDisputes',
        'financials': 'tabFinancials',
        'sentiment': 'tabSentiment',
        'risks': 'tabRisks'
      };
      document.getElementById('current-tab-name').textContent = i18n[currentLang][tabTitleKeys[tabId]] || 'Investigation';
      
      if (tabId === 'procurement') {
        setTimeout(renderD3PrivityTree, 50);
      }
    }

    /* ==========================================================================
       PROJECT DATABASE & FILTERING
       ========================================================================== */
    const projectsData = [
      {
        nameEn: "Madinaty",
        nameAr: "مدينتي",
        category: "east-cairo",
        location: "New Cairo (~33.4M sqm / 8,000 feddans)",
        spv: "ACPUD (99.99%)",
        landModel: "NUCA in-kind BUA (7% of total) & cash (re-contracted 2011)",
        status: "Delivering (c116.5k units planned, >49.5k delivered)",
        components: "Open Air Mall (260k sqm GLA), Arabesque Mall, Golf, Medical Centre",
        risk: "Medium",
        riskBadge: "badge-med"
      },
      {
        nameEn: "The Spine (Central Park)",
        nameAr: "ذا سباين (سنترال بارك مدينتي)",
        category: "east-cairo",
        location: "Inside Madinaty (4.3 mn sqm / 1,000 feddans)",
        spv: "ACPUD (99.99%)",
        landModel: "Carved from Madinaty master concession",
        status: "Under Construction (Delayed 2026/27)",
        components: "Administrative towers, commercial plazas, lakes, business district",
        risk: "Med-High",
        riskBadge: "badge-medhigh"
      },
      {
        nameEn: "Al Rehab City",
        nameAr: "مدينة الرحاب",
        category: "east-cairo",
        location: "New Cairo (~9.9 mn sqm / 2,360 feddans)",
        spv: "ACPUD (99.99%)",
        landModel: "Direct purchase from NUCA (Historical 1996)",
        status: "Fully Delivered (~33.5k units, ~160k residents)",
        components: "Rehab Mall 1 & 2, City Square, Avenue Mall, Gateway Mall",
        risk: "Low",
        riskBadge: "badge-low"
      },
      {
        nameEn: "Celia",
        nameAr: "سيليا (العاصمة الإدارية)",
        category: "east-cairo",
        location: "New Administrative Capital (~2.1 mn sqm / 500 feddans)",
        spv: "ACPUD (99.99%)",
        landModel: "Direct allocation from ACUD (EGP 6.5bn land liability)",
        status: "Phased Delivery (Phases 1-2 delivered, 3-4 late)",
        components: "Village & Park districts, Central Park, commercial strip",
        risk: "Medium",
        riskBadge: "badge-med"
      },
      {
        nameEn: "Noor City",
        nameAr: "مدينة نور (حدائق العاصمة)",
        category: "east-cairo",
        location: "Capital Gardens, East Cairo (~21.0 mn sqm / 5,000 feddans)",
        spv: "Arab Co. for Urban Investment (100%)",
        landModel: "NUCA partnership: 50% in-kind finished units delivery",
        status: "Under Construction (First handovers expected 2026)",
        components: "Smart city, 140k units, light rail connectivity, green infrastructure",
        risk: "High",
        riskBadge: "badge-high"
      },
      {
        nameEn: "SouthMED",
        nameAr: "ساوث ميد (الضبعة - الساحل الشمالي)",
        category: "coastal",
        location: "KM 165–170 Alex-Matrouh Rd (~23 mn sqm)",
        spv: "Arab Co. for Projects & Urban Dev. (99.99%)",
        landModel: "NUCA partnership (Cabinet approval June 2024)",
        status: "Site Preparation / Earthworks (Contracted Sales >EGP 280bn)",
        components: "International marina, 6 hotels, golf, lagoons, retail promenade",
        risk: "High",
        riskBadge: "badge-high"
      },
      {
        nameEn: "Banan City",
        nameAr: "مدينة بنان (الرياض - السعودية)",
        category: "cross-border",
        location: "Al-Fursan Suburb, Riyadh (~3.1 mn sqm)",
        spv: "TMG Saudi LLC / Saudi NHC (JV)",
        landModel: "NHC Land Allocation (SAR 40bn projected investment)",
        status: "Site Works & Sales (First handovers slated 2027)",
        components: "27,745 apartments & villas, commercial spines, health centers",
        risk: "Medium",
        riskBadge: "badge-med"
      },
      {
        nameEn: "Four Seasons San Stefano",
        nameAr: "فور سيزونز سان ستيفانو (الإسكندرية)",
        category: "hospitality",
        location: "Corniche, Alexandria",
        spv: "San Stefano Co. for Tourism & Real Estate (Direct & Indirect)",
        landModel: "State hotel privatization auction (1998)",
        status: "Operating Asset (118 hotel keys, branded residences)",
        components: "Luxury hotel, Grand Shopping Plaza, marina, residential tower",
        risk: "Low",
        riskBadge: "badge-low"
      },
      {
        nameEn: "Four Seasons Nile Plaza",
        nameAr: "فور سيزونز نايل بلازا (القاهرة)",
        category: "hospitality",
        location: "Garden City, Cairo",
        spv: "Nova Park Co. for Tourism Dev. (Direct & Indirect)",
        landModel: "Direct private freehold parcel acquisition",
        status: "Operating Asset (365 hotel keys, 127 luxury apartments)",
        components: "Premier luxury hotel, conference facilities, ballroom",
        risk: "Low",
        riskBadge: "badge-low"
      },
      {
        nameEn: "Four Seasons Sharm El Sheikh",
        nameAr: "فور سيزونز شرم الشيخ",
        category: "hospitality",
        location: "Ras Nasrani, Sharm El Sheikh",
        spv: "Alexandria Saudi Co. for Tourism Projects (Direct & Indirect)",
        landModel: "Red Sea Tourism Development Authority allocation",
        status: "Operating & Expanded (547 keys after 2022 expansion)",
        components: "Palatial dive resort, private beach, convention facilities",
        risk: "Low",
        riskBadge: "badge-low"
      },
      {
        nameEn: "Four Seasons The Pyramids",
        nameAr: "فور سيزونز الأهرامات (الجيزة)",
        category: "hospitality",
        location: "Giza, overlooking Grand Egyptian Museum (42.4 feddans)",
        spv: "Icon Pyramids Co. (100% via Alex RE)",
        landModel: "Developed with NUCA (Disclosed Nov 2025)",
        status: "Under Construction (Delayed: 2028 → 2029)",
        components: "415 keys luxury hotel & branded residences (USD 788mn investment)",
        risk: "Med-High",
        riskBadge: "badge-medhigh"
      },
      {
        nameEn: "Four Seasons Luxor",
        nameAr: "فور سيزونز الأقصر",
        category: "hospitality",
        location: "Luxor Nile Front",
        spv: "Luxor Co. for Urban & Tourism Dev (99.72%)",
        landModel: "Tourism development land allocation",
        status: "Under Construction (Delayed: 2025 → 2026)",
        components: "200 keys luxury palace hotel (Debt EGP 2.1bn, AUC EGP 2.04bn)",
        risk: "Med-High",
        riskBadge: "badge-medhigh"
      },
      {
        nameEn: "Four Seasons Madinaty",
        nameAr: "فور سيزونز مدينتي",
        category: "hospitality",
        location: "Inside Madinaty",
        spv: "Madinaty for Tourism & Urban Projects (96.84%)",
        landModel: "Carved from Madinaty masterplan",
        status: "Under Construction (Delayed: 2026 → 2027)",
        components: "346 keys, convention center, golf villas (Debt EGP 9.2bn, AUC EGP 11.15bn)",
        risk: "High",
        riskBadge: "badge-high"
      },
      {
        nameEn: "Legacy Hotels Portfolio (7 Historic Hotels)",
        nameAr: "محفظة الفنادق التاريخية (7 فنادق)",
        category: "hospitality",
        location: "Cairo, Giza, Alexandria, Aswan, Luxor",
        spv: "Legacy for Hotels (51% ICON / ADQ 40.5%)",
        landModel: "Acquisition from state EGOTH (USD 100mn instalments)",
        status: "Operating & Renovating (Old Cataract & Winter Palace → Mandarin Oriental)",
        components: "Mena House, Cairo Marriott, Cecil, Old Cataract, Winter Palace",
        risk: "Medium",
        riskBadge: "badge-med"
      }
    ];

    let currentFilteredProjects = projectsData;

    function renderProjects(data) {
      const tbody = document.getElementById('projects-tbody');
      tbody.innerHTML = '';
      data.forEach(p => {
        const tr = document.createElement('tr');
        const displayName = currentLang === 'ar' ? p.nameAr : p.nameEn;
        tr.innerHTML = \`
          <td><strong>\${displayName}</strong></td>
          <td>\${p.location}</td>
          <td><span class="cell-mono">\${p.spv}</span></td>
          <td>\${p.landModel}</td>
          <td>\${p.status}</td>
          <td style="max-width:240px; font-size:12px; color:var(--text-muted);">\${p.components}</td>
          <td><span class="badge \${p.riskBadge}">\${p.risk}</span></td>
        \`;
        tbody.appendChild(tr);
      });
    }

    function filterProjects(cat) {
      document.querySelectorAll('#project-filters .filter-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
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
        return;
      }
      currentFilteredProjects = projectsData.filter(p => 
        p.nameEn.toLowerCase().includes(query) ||
        p.nameAr.toLowerCase().includes(query) ||
        p.location.toLowerCase().includes(query) ||
        p.spv.toLowerCase().includes(query) ||
        p.components.toLowerCase().includes(query)
      );
      renderProjects(currentFilteredProjects);
    }

    /* ==========================================================================
       D3.JS INTERACTIVE PRIVITY TREE & NODE INSPECTOR
       ========================================================================== */
    const privityTreeData = {
      name: "TMG Holding (TMGH)",
      type: "Listed Parent Holding",
      desc: "EGX Listed holding vehicle. Issued capital EGP 20.64B. Contractually insulated from trade subcontractors.",
      shield: "Complete Privity Shield",
      risk: "Low Legal Privity Exposure",
      color: "#06b6d4",
      children: [
        {
          name: "Alexandria Construction (ACC)",
          type: "Captive General Contractor",
          desc: "100% TM Family owned, 8.03% cross-shareholding in TMGH. Executes bulk civil packages & absorbs trade liabilities.",
          shield: "Direct Contractual Privity",
          risk: "High Operational & Labor Exposure",
          color: "#f43f5e",
          children: [
            {
              name: "Madinaty Infrastructure & Civil",
              type: "Megaproject Execution",
              desc: "120,000 units civil works, utility conduits, road networks.",
              shield: "ACC Package Privity",
              risk: "Moderate",
              color: "#3b82f6"
            },
            {
              name: "Gemka Group",
              type: "Trade Subcontractor (MEP)",
              desc: "Wastewater treatment equipment, sedimentation bridges, pumps.",
              shield: "Privity with ACC Only",
              risk: "Low (Subcontractor)",
              color: "#10b981"
            },
            {
              name: "Saveto Egypt",
              type: "Material Supplier",
              desc: "Dry-mix mortars, wall putties, architectural coatings for Noor City.",
              shield: "Supply Credit Terms",
              risk: "Low (Supply Terms)",
              color: "#10b981"
            },
            {
              name: "Site Security & Labor Force",
              type: "Internal Workforce",
              desc: "Perimeter security, transport logistics. Documented grievances over shifts and allowances.",
              shield: "Labor Law Exposure",
              risk: "High Labor Friction",
              color: "#f59e0b"
            }
          ]
        },
        {
          name: "Arab Co. (ACPUD)",
          type: "Megaproject Developer SPV",
          desc: "99.99% owned by TMG Holding. Legal concession holder for Madinaty, Celia, and SouthMED.",
          shield: "Intermediate Developer Shield",
          risk: "Medium Concession Risk",
          color: "#06b6d4",
          children: [
            {
              name: "Atrium Quality Contractors",
              type: "Turnkey General Contractor",
              desc: "Wholly owned general contractor executing commercial and New Capital packages.",
              shield: "Contractor Privity Shield",
              risk: "Medium",
              color: "#f43f5e",
              children: [
                {
                  name: "Al Majd Contracting",
                  type: "MEP Subcontractor",
                  desc: "Electromechanical works for Celia (New Capital). Subject to back-to-back payment terms.",
                  shield: "Privity with Atrium Only",
                  risk: "Moderate",
                  color: "#10b981"
                },
                {
                  name: "Schindler Egypt (JV)",
                  type: "Specialist Subcontractor",
                  desc: "Elevator assembly and maintenance joint venture with Atrium.",
                  shield: "JV Direct Agreement",
                  risk: "Low",
                  color: "#10b981"
                }
              ]
            },
            {
              name: "Concrete Plus for Contracting",
              type: "Independent Tier-1 Contractor",
              desc: "Package C01 SouthMed (179 buildings) and Noor V3.2 villas (~EGP 10B total contract).",
              shield: "Direct Privity with ACPUD",
              risk: "Medium Delivery Pacing",
              color: "#f59e0b"
            }
          ]
        },
        {
          name: "ICON Luxury Hotels",
          type: "Hospitality Arm (59.5% TMG / 40.5% ADQ)",
          desc: "Owns Four Seasons properties and 7 Historic Hotels (Legacy Hotels). Foreign currency revenue hedge.",
          shield: "Joint Venture Shield",
          risk: "Low Operational Risk",
          color: "#8b5cf6",
          children: [
            {
              name: "Legacy Hotels Portfolio",
              type: "State Asset Acquisition",
              desc: "Mena House, Cairo Marriott, Cecil, Old Cataract, Winter Palace.",
              shield: "Institutional SPV",
              risk: "Low",
              color: "#3b82f6"
            },
            {
              name: "Banque Misr Syndication (FS Madinaty)",
              type: "Lender Consortium",
              desc: "EGP 6.76B bank syndication requiring strict engineer drawdown certifications.",
              shield: "Banking Escrow Privity",
              risk: "Lender Covenant Monitoring",
              color: "#f59e0b"
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

      d3G = d3Svg.append('g').attr('transform', 'translate(80, 40)');

      d3Zoom = d3.zoom().scaleExtent([0.5, 2.5]).on('zoom', (e) => {
        d3G.attr('transform', e.transform);
      });
      d3Svg.call(d3Zoom);

      const treeLayout = d3.tree().size([height - 80, width - 260]);
      const root = d3.hierarchy(privityTreeData);
      treeLayout(root);

      // Links
      d3G.selectAll('.d3-link')
        .data(root.links())
        .enter()
        .append('path')
        .attr('class', 'd3-link')
        .attr('d', d3.linkHorizontal().x(d => d.y).y(d => d.x));

      // Nodes
      const node = d3G.selectAll('.d3-node')
        .data(root.descendants())
        .enter()
        .append('g')
        .attr('class', 'd3-node')
        .attr('transform', d => \`translate(\${d.y}, \${d.x})\`)
        .on('click', (event, d) => inspectNode(d.data));

      node.append('circle')
        .attr('r', d => d.children ? 8 : 6)
        .attr('fill', d => d.data.color || '#06b6d4')
        .attr('stroke', '#fff');

      node.append('text')
        .attr('dy', 4)
        .attr('x', d => d.children ? -12 : 12)
        .style('text-anchor', d => d.children ? 'end' : 'start')
        .text(d => d.data.name)
        .style('font-size', '11px')
        .style('font-weight', d => d.depth <= 1 ? '700' : '500')
        .style('fill', currentTheme === 'light' ? '#0f172a' : '#f8fafc');
    }

    function inspectNode(data) {
      const panel = document.getElementById('node-inspector');
      document.getElementById('inspector-name').textContent = data.name;
      document.getElementById('inspector-type').textContent = data.type;
      document.getElementById('inspector-desc').textContent = data.desc;
      document.getElementById('inspector-shield').textContent = data.shield;
      document.getElementById('inspector-risk').textContent = data.risk;
      panel.classList.add('active');
    }

    function closeInspector() {
      document.getElementById('node-inspector').classList.remove('active');
    }

    function resetD3View() {
      if (d3Svg && d3Zoom) {
        d3Svg.transition().duration(500).call(d3Zoom.transform, d3.zoomIdentity.translate(80, 40).scale(1));
      }
    }

    function zoomD3(factor) {
      if (d3Svg && d3Zoom) {
        d3Svg.transition().duration(300).call(d3Zoom.scaleBy, factor);
      }
    }

    /* ==========================================================================
       PRESENTER MODE ENGINE (SLIDES & KEYBOARD SHORTCUTS)
       ========================================================================== */
    const presenterSlides = [
      {
        num: "SLIDE 01 / 08",
        title: "Executive Overview & Corporate Positioning",
        note: "TMG Holding boasts EGP 20.64B issued capital and >EGP 441B backlog, but operates with aggressive working capital deferral (>EGP 15.79B commercial notes).",
        content: \`
          <div class="kpi-grid">
            <div class="kpi-card cyan">
              <div class="kpi-title">Issued & Paid Capital</div>
              <div class="kpi-value">EGP 20.64 bn</div>
              <div class="kpi-delta delta-up">● EGX Listed (TMGH)</div>
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
          <div style="font-size:14px; color:var(--text-muted); line-height:1.7; margin-top:20px;">
            This forensic investigation examines the contractual reality of Talaat Moustafa Group Holding. Despite astronomical contracted sales (EGP 504B in 2024, EGP 382B in 2025), cash flow conversion is severely strained by construction inflation and working capital drain.
          </div>
        \`
      },
      {
        num: "SLIDE 02 / 08",
        title: "Captive Procurement & Contractual Privity Shield",
        note: "Contractual privity shields the parent entity. Trade contractors have zero direct claim on TMG Holding bank accounts or project revenues.",
        content: \`
          <div class="grid-2">
            <div class="flag-card" style="border-left-color: var(--accent-cyan);">
              <div class="flag-title">The Alexandria Construction Co. (ACC) Insulator</div>
              <div class="flag-desc">ACC (100% TM Family owned, 8.03% cross-shareholding) executes all major superstructures. Subcontractors sign with ACC, removing legal recourse against listed TMG Holding.</div>
            </div>
            <div class="flag-card" style="border-left-color: var(--accent-amber);">
              <div class="flag-title">Labor & Materials Decoupling</div>
              <div class="flag-desc">TMG buys rebar and cement directly. Trade subcontractors execute labor-only packages, eliminating contractor margin buffers against severe wage inflation.</div>
            </div>
          </div>
        \`
      },
      {
        num: "SLIDE 03 / 08",
        title: "The Payment Certificate Gatekeeping Bottleneck (المستخلصات)",
        note: "Under Egyptian Civil Law, an uncertified progress certificate is not an executable debt. Delays in technical measurement conserve developer cash without formal default.",
        content: \`
          <div class="grid-3">
            <div class="step-card">
              <span class="step-num">Stage 1</span>
              <h4>1. Technical Site Measurement</h4>
              <p style="font-size:12px; color:var(--text-muted); margin-top:6px;">Site quantities audited strictly. Variations without advance written approvals are rejected.</p>
            </div>
            <div class="step-card">
              <span class="step-num">Stage 2</span>
              <h4>2. Central Document Gatekeeping</h4>
              <p style="font-size:12px; color:var(--text-muted); margin-top:6px;">Madinaty central data entry cross-references site delivery slips. Defects halt payment approval.</p>
            </div>
            <div class="step-card">
              <span class="step-num">Stage 3</span>
              <h4>3. Deferred Commercial Paper</h4>
              <p style="font-size:12px; color:var(--text-muted); margin-top:6px;">Approved dues paid via post-dated checks (90 to 270 days), swelling notes payable past EGP 15.79B.</p>
            </div>
          </div>
        \`
      },
      {
        num: "SLIDE 04 / 08",
        title: "Project Portfolio: Scale vs Pacing Risk",
        note: "Flagship projects like Madinaty and Rehab are mature; however, SouthMed (23M sqm) and Noor (5,000 feddans) create enormous long-term execution obligations.",
        content: \`
          <div class="grid-2">
            <div class="card" style="background:var(--bg-surface-elevated);">
              <div class="card-title">Mega Developments in Pipeline</div>
              <ul style="font-size:13px; color:var(--text-muted); line-height:1.8; margin-top:10px; padding-left:20px;">
                <li><strong>SouthMED (KM 165 Coast):</strong> 23M sqm, >EGP 280bn sales, delivery slated 2029.</li>
                <li><strong>Noor City (Capital Gardens):</strong> 5,000 feddans, 50% in-kind finished unit delivery to NUCA.</li>
                <li><strong>Banan City (Riyadh):</strong> SAR 40bn cross-border venture with Saudi NHC.</li>
              </ul>
            </div>
            <div class="card" style="background:var(--bg-surface-elevated);">
              <div class="card-title">Hospitality Expansion Pacing</div>
              <ul style="font-size:13px; color:var(--text-muted); line-height:1.8; margin-top:10px; padding-left:20px;">
                <li><strong>Legacy Hotels:</strong> 7 historic state hotels acquired (51% ICON / ADQ 40.5%).</li>
                <li><strong>Luxury Slippages:</strong> Four Seasons Luxor (delayed to 2026), Pyramids (to 2029).</li>
                <li><strong>Syndicated Covenants:</strong> EGP 6.76B Banque Misr facility for FS Madinaty.</li>
              </ul>
            </div>
          </div>
        \`
      },
      {
        num: "SLIDE 05 / 08",
        title: "Master Contractor & Subcontractor Roster",
        note: "While Alexandria Construction Co. remains the captive core, Tier-1 contractor Concrete Plus was awarded ~EGP 10B in packages to meet coastal 2029 milestones.",
        content: \`
          <div style="font-size:13px; color:var(--text-muted); line-height:1.7;">
            <p><strong>Primary Contracting Entities Identified:</strong></p>
            <ul style="margin-top:10px; margin-bottom:15px; padding-left:20px;">
              <li><strong>Alexandria Construction Co. (ACC):</strong> Captive civil/EPC contractor across Madinaty, Rehab, and hospitality.</li>
              <li><strong>Concrete Plus for Contracting:</strong> Independent Tier-1 general contractor awarded SouthMed Package C01 (179 buildings) & Noor V3.2 villas.</li>
              <li><strong>Atrium Quality Contractors:</strong> Captive turnkey contractor for Celia (New Capital) and luxury fit-outs.</li>
              <li><strong>Specialist Subcontractors:</strong> Al Majd (MEP), Gemka Group (Wastewater), Metito (Water treatment), Saveto Egypt (Mortars).</li>
            </ul>
          </div>
        \`
      },
      {
        num: "SLIDE 06 / 08",
        title: "Judicial Rulings & The CRCICA Arbitration Barrier",
        note: "Mandatory institutional arbitration suppresses public contractor litigation, while historic Supreme Administrative Court rulings imposed a 7% in-kind land settlement.",
        content: \`
          <div class="grid-2">
            <div class="flag-card" style="border-left-color: var(--accent-rose);">
              <div class="flag-title">Case 12622 / JY 63 — Madinaty Concession</div>
              <div class="flag-desc">Supreme Administrative Court annulled direct allocation in 2010. Settled via 7% in-kind residential BUA delivered to NUCA (worth tens of billions of EGP).</div>
            </div>
            <div class="flag-card" style="border-left-color: var(--accent-blue);">
              <div class="flag-title">CRCICA Mandatory Arbitration Shield</div>
              <div class="flag-desc">All supply and subcontract agreements mandate CRCICA rules. High tribunal costs make arbitrating claims under EGP 20M economically unviable for SMEs.</div>
            </div>
          </div>
        \`
      },
      {
        num: "SLIDE 07 / 08",
        title: "Financial Forensics: Debt Equivalent & Cash Burn",
        note: "Effective debt includes EGP 43.99B in structured financial lease notes. H1 2026 cash conversion stood at only 31.2% due to EGP 18.26B working capital drain.",
        content: \`
          <div class="grid-2">
            <div class="kpi-card purple">
              <div class="kpi-title">Structured Financial Leases</div>
              <div class="kpi-value">EGP 43.99 bn</div>
              <div class="kpi-delta delta-warn">▲ Effective debt (borrowing cost 28.6%)</div>
            </div>
            <div class="kpi-card amber">
              <div class="kpi-title">H1 2026 Cash Velocity Drain</div>
              <div class="kpi-value">EGP -18.26 bn</div>
              <div class="kpi-delta delta-down">▼ WIP Inventory & Construction Outflow</div>
            </div>
          </div>
          <div style="font-size:13px; color:var(--text-muted); line-height:1.7; margin-top:20px;">
            TMG uses sale-and-leaseback transactions to monetize commercial assets (Open Air Mall, Gateway Mall) while deferring balance sheet debt. Combined true debt exceeds EGP 60.5B.
          </div>
        \`
      },
      {
        num: "SLIDE 08 / 08",
        title: "Forensic Risk Matrix & Diligence Playbooks",
        note: "Subcontractors must reject pay-when-paid clauses and insist on written variation orders. Banks must monitor trade payables velocity alongside headline cash.",
        content: \`
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-cyan);">
              <div class="card-title" style="color:var(--accent-cyan);">Subcontractor Diligence Playbook</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.7; margin-top:8px; padding-left:16px;">
                <li>Reject "Pay-When-Paid" language linking payment to developer releases.</li>
                <li>Zero unapproved site variations without signed Variation Orders.</li>
                <li>Serve court bailiff notices to start statutory 5% commercial default interest.</li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-emerald);">
              <div class="card-title" style="color:var(--accent-emerald);">Institutional Investor & Lender Playbook</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.7; margin-top:8px; padding-left:16px;">
                <li>Captive privity insulates parent company equity and headline EBITDA.</li>
                <li>Monitor notes payable velocity (>EGP 15.79B) for downstream subcontractor strain.</li>
                <li>Incorporate EGP 44B financial lease obligations into true leverage tests.</li>
              </ul>
            </div>
          </div>
        \`
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
      document.getElementById('presenter-slide-title').textContent = s.title;
      document.getElementById('presenter-slide-content').innerHTML = s.content;
      document.getElementById('presenter-speaker-note').textContent = s.note;

      document.getElementById('presenter-dock-indicator').textContent = \`\${index + 1} / \${presenterSlides.length}\`;
      const pct = ((index + 1) / presenterSlides.length) * 100;
      document.getElementById('slide-progress-bar').style.width = pct + '%';
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
        nextSlide();
      } else if (e.key === 'ArrowLeft') {
        prevSlide();
      } else if (e.key === 'Escape') {
        closePresenterMode();
      } else if (e.key.toLowerCase() === 'f') {
        toggleFullScreen();
      }
    }

    /* ==========================================================================
       CHART.JS CONFIGURATION & THEME UPDATER
       ========================================================================== */
    let chartFin, chartComp, chartCash, chartDebt;

    function initCharts() {
      const textColor = currentTheme === 'light' ? '#475569' : '#94a3b8';
      const gridColor = currentTheme === 'light' ? 'rgba(203, 213, 225, 0.4)' : 'rgba(51, 65, 85, 0.3)';

      // Chart 1: Financial Trends
      const ctxFin = document.getElementById('chartFinancialTrends').getContext('2d');
      chartFin = new Chart(ctxFin, {
        type: 'bar',
        data: {
          labels: ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026'],
          datasets: [
            {
              label: 'Consolidated Revenue (EGP bn)',
              data: [15.35, 19.87, 28.43, 42.70, 62.50, 30.19],
              backgroundColor: '#06b6d4',
              borderRadius: 5
            },
            {
              label: 'Consolidated Net Profit (EGP bn)',
              data: [1.78, 2.23, 3.31, 12.80, 18.20, 9.95],
              backgroundColor: '#10b981',
              borderRadius: 5
            },
            {
              type: 'line',
              label: 'Contracted Backlog (EGP bn)',
              data: [63.0, 77.0, 145.0, 294.0, 441.2, 460.0],
              borderColor: '#f59e0b',
              backgroundColor: 'rgba(245, 158, 11, 0.1)',
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
            legend: { labels: { color: textColor, font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' } } }
          },
          scales: {
            x: { grid: { color: gridColor }, ticks: { color: textColor, font: { family: 'Plus Jakarta Sans' } } },
            y: { grid: { color: gridColor }, ticks: { color: textColor, font: { family: 'Plus Jakarta Sans' } } }
          }
        }
      });

      // Chart 2: Complaints
      const ctxComp = document.getElementById('chartComplaints').getContext('2d');
      chartComp = new Chart(ctxComp, {
        type: 'doughnut',
        data: {
          labels: [
            'Maintenance Deficit Fees (فروق صيانة)',
            'Resale Transfer Fees (رسوم تنازل)',
            'Phased Delivery Slippage',
            'Finishing & Physical Defects',
            'Utility Tariffs & Water Pressure'
          ],
          datasets: [{
            data: [38, 26, 18, 11, 7],
            backgroundColor: ['#f43f5e', '#f59e0b', '#3b82f6', '#8b5cf6', '#64748b'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'right', labels: { color: textColor, boxWidth: 12, font: { family: 'Plus Jakarta Sans', size: 10.5 } } }
          },
          cutout: '68%'
        }
      });

      // Chart 3: Cash Flow
      const ctxCash = document.getElementById('chartCashFlow').getContext('2d');
      chartCash = new Chart(ctxCash, {
        type: 'bar',
        data: {
          labels: ['Consolidated Profit', 'Net Operating Cash', 'WIP Outflow', 'Customer Inflow'],
          datasets: [{
            label: 'H1 2026 Cash Velocity (EGP Millions)',
            data: [9950, 3110, -18260, 16320],
            backgroundColor: ['#10b981', '#06b6d4', '#f43f5e', '#3b82f6'],
            borderRadius: 5
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { grid: { color: gridColor }, ticks: { color: textColor } },
            y: { grid: { color: gridColor }, ticks: { color: textColor } }
          }
        }
      });

      // Chart 4: Debt
      const ctxDebt = document.getElementById('chartDebtBreakdown').getContext('2d');
      chartDebt = new Chart(ctxDebt, {
        type: 'doughnut',
        data: {
          labels: [
            'Financial Lease Notes (EGP 44.0bn)',
            'Bank Borrowings (EGP 16.5bn)',
            'Customer Advances (EGP 134.0bn)'
          ],
          datasets: [{
            data: [43.99, 16.50, 133.99],
            backgroundColor: ['#f43f5e', '#f59e0b', '#3b82f6'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { color: textColor, boxWidth: 12, font: { family: 'Plus Jakarta Sans', size: 10.5 } } }
          },
          cutout: '65%'
        }
      });
    }

    function updateChartsTheme(theme) {
      const textColor = theme === 'light' ? '#475569' : '#94a3b8';
      const gridColor = theme === 'light' ? 'rgba(203, 213, 225, 0.4)' : 'rgba(51, 65, 85, 0.3)';

      [chartFin, chartCash].forEach(chart => {
        if (!chart) return;
        chart.options.scales.x.grid.color = gridColor;
        chart.options.scales.x.ticks.color = textColor;
        chart.options.scales.y.grid.color = gridColor;
        chart.options.scales.y.ticks.color = textColor;
        if (chart.options.plugins.legend) {
          chart.options.plugins.legend.labels.color = textColor;
        }
        chart.update();
      });

      [chartComp, chartDebt].forEach(chart => {
        if (!chart) return;
        if (chart.options.plugins.legend) {
          chart.options.plugins.legend.labels.color = textColor;
        }
        chart.update();
      });

      // Also refresh D3 tree text colors
      if (d3G) {
        d3G.selectAll('.d3-node text')
          .style('fill', theme === 'light' ? '#0f172a' : '#f8fafc');
      }
    }

    /* ==========================================================================
       INITIALIZATION
       ========================================================================== */
    document.addEventListener('DOMContentLoaded', () => {
      // Restore persisted theme & lang
      const savedTheme = localStorage.getItem('tmg_theme') || 'dark';
      const savedLang = localStorage.getItem('tmg_lang') || 'en';

      setTheme(savedTheme);
      setLanguage(savedLang);

      renderProjects(projectsData);
      initCharts();
    });
  </script>
</body>
</html>
\`;

fs.writeFileSync(path.join(__dirname, '..', 'TMG_Forensic_Due_Diligence_Dashboard.html'), htmlContent, 'utf8');
fs.writeFileSync(path.join(__dirname, '..', 'index.html'), htmlContent, 'utf8');
console.log('Successfully generated upgraded TMG Forensic Due Diligence Dashboard (HTML + index.html)');
