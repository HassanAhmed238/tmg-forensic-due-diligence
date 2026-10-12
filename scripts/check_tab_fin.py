import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="tab-financials"')
print('tab-financials starts at:', idx)
print(text[idx:idx+400])
