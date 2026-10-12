import sys
sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("document.getElementById('financials-tbody')")
if pos != -1:
    print(text[pos-100:pos+250])
