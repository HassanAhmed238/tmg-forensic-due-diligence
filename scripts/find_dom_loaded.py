import sys
sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.rfind("document.addEventListener('DOMContentLoaded'")
if idx != -1:
    print(text[idx:idx+600])
else:
    print("DOMContentLoaded not found")
