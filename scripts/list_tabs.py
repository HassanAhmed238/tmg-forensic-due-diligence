import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

tabs = re.findall(r'<div[^>]*id=["\'](tab-[^"\']+)["\'][^>]*class=["\'][^"\']*tab-pane[^"\']*["\']', text)
print("Found tab IDs:")
for t in tabs:
    # find where it ends
    idx = text.find(f'id="{t}"')
    title_match = re.search(r'<div[^>]*class=["\']card-title["\'][^>]*>(.*?)</div>', text[idx:idx+2000])
    title = title_match.group(1) if title_match else "No title"
    print(f"  {t} -> {title[:60]}")
