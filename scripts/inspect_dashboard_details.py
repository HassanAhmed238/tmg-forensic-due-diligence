import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where tabs are defined and what JS exists
script_tags = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', text, re.DOTALL)
print(f"Number of script tags: {len(script_tags)}")
for i, s in enumerate(script_tags):
    if len(s.strip()) > 0:
        print(f"Script {i+1} length: {len(s)} chars")
        # Print first few lines of main script
        lines = [line for line in s.strip().split('\n') if line.strip()]
        print(f"  First 5 lines: {lines[:5]}")
        print(f"  Last 5 lines: {lines[-5:]}")

# Check tab-financials content size and keywords
fin_match = re.search(r'<div[^>]*id=["\']tab-financials["\'][^>]*>(.*?)</div>\s*<!--\s*/?tab', text, re.DOTALL)
if fin_match:
    print(f"\nTab-financials found, length: {len(fin_match.group(1))} chars")
else:
    # try finding by next tab
    idx1 = text.find('id="tab-financials"')
    if idx1 != -1:
        idx2 = text.find('id="tab-', idx1 + 25)
        print(f"\nTab-financials slice length: {idx2 - idx1 if idx2 != -1 else 'to end'}")

# Check tab-pzone
idx_pz = text.find('id="tab-pzone"')
if idx_pz != -1:
    idx_next = text.find('id="tab-', idx_pz + 25)
    print(f"Tab-pzone slice length: {idx_next - idx_pz if idx_next != -1 else 'to end'}")
