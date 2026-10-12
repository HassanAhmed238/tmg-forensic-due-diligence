import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'financials-tbody|chartCashFlow|liabilitiesHBarChart', text)]
print(f"Occurrences found: {len(matches)}")

for pos in matches:
    start = max(0, pos - 100)
    end = min(len(text), pos + 250)
    print("--- MATCH AT POS", pos, "---")
    print(text[start:end])
