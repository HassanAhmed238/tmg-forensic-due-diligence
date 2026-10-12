import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_pz = text.find('id="tab-pzone"')
if idx_pz != -1:
    idx_next = text.find('id="tab-', idx_pz + 25)
    print(f"Tab-pzone content (first 2500 chars):\n")
    print(text[idx_pz:idx_pz+2500])
