with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="tab-pzone"' in l:
        print('tab-pzone starts at line', i+1)
    if 'id="tab-stakeholders"' in l:
        print('tab-stakeholders starts at line', i+1)
