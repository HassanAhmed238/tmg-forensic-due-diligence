import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for switchTab function
match = re.search(r'function\s+switchTab\s*\([^\)]*\)\s*\{.*?\}(?=\s*function|\s*const|\s*let|\s*var|\s*document|\s*window)', text, re.DOTALL)
if match:
    print("switchTab definition:\n", match.group(0))
else:
    print("switchTab not found by regex, searching raw:")
    idx = text.find('switchTab')
    if idx != -1:
        print(text[idx-50:idx+350])
