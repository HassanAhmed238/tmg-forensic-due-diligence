import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for toggleLanguage function
match = re.search(r'function\s+toggleLanguage\s*\([^\)]*\)\s*\{.*?\}(?=\s*function|\s*const|\s*let|\s*var|\s*document|\s*window)', text, re.DOTALL)
if match:
    print("toggleLanguage definition:\n", match.group(0)[:1500])
else:
    idx = text.find('toggleLanguage')
    if idx != -1:
        print(text[idx-50:idx+600])
