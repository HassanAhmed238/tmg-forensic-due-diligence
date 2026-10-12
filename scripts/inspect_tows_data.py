import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_tows_data = text.find('const TMG_TOWS = {')
if idx_tows_data != -1:
    print("=== TMG_TOWS DATA OBJECT ===")
    print(text[idx_tows_data:idx_tows_data+3500])
else:
    # check where tows data is defined
    idx_tows_func = text.find('// TOWS Actions')
    if idx_tows_func != -1:
        print(text[idx_tows_func:idx_tows_func+2000])
