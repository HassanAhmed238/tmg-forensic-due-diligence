import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect TMG_SWOT data object definition
idx_obj = text.find('const TMG_SWOT = {')
if idx_obj != -1:
    print("=== TMG_SWOT DATA OBJECT ===")
    print(text[idx_obj:idx_obj+3000])
else:
    print("TMG_SWOT object not found!")

# Let's inspect TOWS rendering
idx_tows = text.find('tows-so-container')
if idx_tows != -1:
    print("\n=== TOWS CONTAINERS & LOGIC ===")
    print(text[idx_tows-200:idx_tows+1500])
