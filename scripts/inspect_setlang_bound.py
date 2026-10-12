import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_setlang = text.find('function setLanguage(lang)')
idx_next = text.find('function ', idx_setlang + 50)
print(f"setLanguage starts at char {idx_setlang}, next function starts at {idx_next}")
print("Next function line:", text[idx_next:idx_next+100])
