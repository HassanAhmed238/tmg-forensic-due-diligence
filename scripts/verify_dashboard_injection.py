# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

print("Verifying Dashboard HTML elements...")

required_ids = [
    # Subviews
    'subview-is-bs', 'subview-sources-uses', 'subview-common-size', 
    'subview-cfo-ratios', 'subview-pzone-deep', 'subview-guide',
    # Tables
    'fin-fs-th-row', 'fin-fs-tbody',
    'fin-su-th-row', 'fin-su-tbody',
    'fin-cs-th-row', 'fin-cs-tbody',
    'fin-rt-th-row', 'fin-rt-tbody',
    # Charts
    'chartFinancialTrendsDynamic', 'chartBalanceSheetDynamic',
    'chartDpoDynamic', 'chartSourcesUsesDynamic',
    # Simulator
    'sim-input-val', 'sim-input-mep', 'sim-input-days', 'sim-input-fx',
    'disp-sim-val', 'disp-sim-mep', 'disp-sim-days', 'disp-sim-fx',
    'res-sim-frozen', 'res-sim-interest', 'res-sim-fxloss', 'res-sim-advpay',
    # KPIs
    'kpi-fin-rev-v', 'kpi-fin-ni-v', 'kpi-fin-adv-v',
    'kpi-fin-notes-v', 'kpi-fin-lease-v', 'kpi-fin-dpo-v',
    # Slicer Buttons
    'btn-v-isbs', 'btn-v-sources', 'btn-v-common', 'btn-v-ratios', 'btn-v-pzone', 'btn-v-guide',
    'btn-y-all', 'btn-u-b', 'btn-u-k', 'btn-u-usd', 'finSearchInput'
]

missing = []
for el_id in required_ids:
    if f'id="{el_id}"' not in text:
        missing.append(el_id)

if missing:
    print(f"FAILED: Missing IDs: {missing}")
else:
    print(f"SUCCESS: All {len(required_ids)} required DOM IDs are present!")

# Check JS functions
required_funcs = [
    'setFinView', 'setFinYear', 'setFinUnit', 'handleFinSearch',
    'renderFinancialStatementsTable', 'renderSourcesUsesTable',
    'renderCommonSizeTable', 'renderCfoRatiosTable',
    'updateSimCalculations', 'initDynamicFinancialCharts',
    'updateFinancialKPIs', 'updateFinancialLanguage'
]

missing_funcs = []
for f_name in required_funcs:
    if f"function {f_name}" not in text:
        missing_funcs.append(f_name)

if missing_funcs:
    print(f"FAILED: Missing JS functions: {missing_funcs}")
else:
    print(f"SUCCESS: All {len(required_funcs)} required JS functions are defined!")
