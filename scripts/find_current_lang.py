import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'currentLang', text)]
print("currentLang found occurrences:", len(matches))
if matches:
    idx = matches[0]
    print(text[max(0, idx-100):min(len(text), idx+500)])
