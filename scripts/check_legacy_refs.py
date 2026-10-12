import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

old_refs = ['chartCashFlow', 'chartDebtBreakdown', 'liabilitiesHBarChart', 'financials-tbody']

for ref in old_refs:
    matches = [m.start() for m in re.finditer(ref, text)]
    print(f"'{ref}' found {len(matches)} times at positions: {matches}")
    for pos in matches:
        print(f"  Snippet around {pos}: {text[max(0, pos-40):min(len(text), pos+60)]!r}")
