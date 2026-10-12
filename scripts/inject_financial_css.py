# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

extra_css = """
    /* ==========================================================================
       FINANCIAL COMMAND CENTER & INTERACTIVE SLICER SUITE
       ========================================================================== */
    .fin-slicer-deck {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 16px 20px;
      margin-bottom: 24px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .fin-slicer-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }
    .fin-slicer-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .fin-slicer-label {
      font-size: 11px;
      font-weight: 800;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .fin-pills-wrap {
      display: inline-flex;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 9px;
      padding: 3px;
      gap: 3px;
      flex-wrap: wrap;
    }
    .fin-pill {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 12px;
      border-radius: 7px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: inherit;
    }
    .fin-pill:hover {
      color: var(--text-main);
      background: rgba(6, 182, 212, 0.08);
    }
    .fin-pill.active {
      background: var(--accent-cyan);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(6, 182, 212, 0.35);
    }
    [data-theme="light"] .fin-pill.active {
      background: var(--accent-blue);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
    }
    .fin-search-box {
      position: relative;
      min-width: 220px;
    }
    .fin-search-box input {
      width: 100%;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 7px 12px 7px 32px;
      border-radius: 8px;
      font-size: 12px;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s ease;
    }
    html[dir="rtl"] .fin-search-box input {
      padding: 7px 32px 7px 12px;
    }
    .fin-search-box svg {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      left: 10px;
      width: 14px;
      height: 14px;
      color: var(--text-muted);
      pointer-events: none;
    }
    html[dir="rtl"] .fin-search-box svg {
      left: auto;
      right: 10px;
    }
    .fin-search-box input:focus {
      border-color: var(--accent-cyan);
    }

    /* Sub-view containers */
    .fin-subview {
      display: none;
      animation: finFadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .fin-subview.active {
      display: block;
    }
    @keyframes finFadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Financial Tables */
    .fin-data-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 12.5px;
    }
    .fin-data-table th {
      background: var(--th-bg);
      color: var(--th-color);
      padding: 10px 14px;
      font-weight: 800;
      text-align: right;
      border-bottom: 2px solid var(--border-highlight);
      white-space: nowrap;
      position: sticky;
      top: 0;
      z-index: 10;
    }
    html[dir="ltr"] .fin-data-table th {
      text-align: left;
    }
    .fin-data-table th.num-col, .fin-data-table td.num-col {
      text-align: right;
      direction: ltr;
      font-family: var(--font-mono);
      font-variant-numeric: tabular-nums;
    }
    .fin-data-table td {
      padding: 8px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-main);
      transition: background 0.15s ease;
    }
    .fin-data-table tr:hover td {
      background: var(--table-hover);
    }
    .fin-data-table tr.row-subhead td {
      background: rgba(6, 182, 212, 0.06);
      font-weight: 800;
      color: var(--accent-cyan);
      font-size: 13px;
      border-top: 1px solid var(--border-highlight);
    }
    .fin-data-table tr.row-total td {
      background: rgba(59, 130, 246, 0.08);
      font-weight: 800;
      color: var(--text-main);
      border-top: 2px solid var(--border-highlight);
      border-bottom: 2px solid var(--border-highlight);
    }
    .fin-data-table tr.row-check td {
      background: rgba(16, 185, 129, 0.1);
      font-weight: 800;
      color: var(--accent-emerald);
      border-top: 1px solid var(--accent-emerald);
    }

    /* Risk Badges & Highlights */
    .val-pos { color: var(--accent-emerald); font-weight: 700; }
    .val-neg { color: var(--accent-rose); font-weight: 700; }
    .val-warn { color: var(--accent-amber); font-weight: 700; }
    .val-cyan { color: var(--accent-cyan); font-weight: 700; }

    /* Interactive Simulator */
    .sim-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    @media (max-width: 900px) {
      .sim-grid { grid-template-columns: 1fr; }
    }
    .sim-slider-row {
      margin-bottom: 16px;
    }
    .sim-slider-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      font-size: 12.5px;
      font-weight: 700;
    }
    .sim-slider {
      width: 100%;
      height: 6px;
      border-radius: 4px;
      background: var(--border-highlight);
      outline: none;
      -webkit-appearance: none;
      accent-color: var(--accent-cyan);
    }
    .sim-stat-box {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .sim-stat-num {
      font-size: 22px;
      font-weight: 900;
      font-family: var(--font-mono);
      letter-spacing: -0.5px;
    }
    .sim-verdict-box {
      border-radius: 12px;
      padding: 18px;
      margin-top: 16px;
      border-inline-start: 5px solid;
    }

    /* Beginner Guide Cards */
    .guide-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }
    @media (max-width: 1024px) {
      .guide-grid-3 { grid-template-columns: 1fr; }
    }
    .guide-step-card {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 18px;
      position: relative;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .guide-step-num {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--accent-cyan);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 13px;
    }
    .tl-radar-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-top: 16px;
    }
    @media (max-width: 900px) {
      .tl-radar-grid { grid-template-columns: 1fr; }
    }
    .tl-card {
      border-radius: 12px;
      padding: 18px;
      border: 1px solid var(--border-subtle);
    }
    .tl-card.green { background: rgba(16, 185, 129, 0.06); border-inline-start: 4px solid var(--accent-emerald); }
    .tl-card.amber { background: rgba(245, 158, 11, 0.06); border-inline-start: 4px solid var(--accent-amber); }
    .tl-card.red { background: rgba(244, 63, 94, 0.06); border-inline-start: 4px solid var(--accent-rose); }
"""

pos_style_end = text.find('</style>')
if pos_style_end != -1:
    text = text[:pos_style_end] + extra_css + "\n  " + text[pos_style_end:]
    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully injected Financial CSS into <style> block!")
else:
    print("Could not find </style> tag!")
