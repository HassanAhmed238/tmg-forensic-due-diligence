import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\([^\)]*\)\s*\{[^}]*currentLang[^}]*\}', text)
print("Functions mentioning currentLang:", matches)

# Find button that changes language
lang_btn = re.findall(r'<button[^>]*lang[^>]*>.*?</button>', text, re.IGNORECASE)
print("Language buttons in HTML:", lang_btn)
