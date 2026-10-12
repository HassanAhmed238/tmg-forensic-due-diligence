import sys
sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('function setLanguage(lang)')
print("Inside setLanguage:")
end_setlang = text.find('function setTheme', idx)
print(text[end_setlang-300:end_setlang])
