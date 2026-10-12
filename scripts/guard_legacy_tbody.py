import sys

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

target = "document.getElementById('financials-tbody').innerHTML = finRows.map(r => `"
replacement = "const finTb = document.getElementById('financials-tbody'); if (finTb) finTb.innerHTML = finRows.map(r => `"

if target in text:
    text = text.replace(target, replacement, 1)
    print("Safely guarded legacy financials-tbody call!")
    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(text)
else:
    print("Target legacy financials-tbody call not found or already guarded.")
