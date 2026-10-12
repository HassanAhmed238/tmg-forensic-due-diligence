import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text), "bytes")

# Find nav buttons
nav_btns = re.findall(r'<button[^>]*class=["\'][^"\']*nav-btn[^"\']*["\'][^>]*>(.*?)</button>', text, re.DOTALL)
print(f"\nNav buttons found: {len(nav_btns)}")
for i, btn in enumerate(nav_btns):
    clean = re.sub(r'<[^>]+>', ' ', btn)
    clean = re.sub(r'\s+', ' ', clean).strip()
    print(f"  {i+1}: {clean[:100]}")

# Find section IDs or tab contents
sections = re.findall(r'<(?:section|div)[^>]*id=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*(?:tab-pane|section|view)[^"\']*["\']', text)
print(f"\nTab panes / views found: {len(sections)}")
for s in sections:
    print(f"  ID: {s}")

# Check any existing scripts or data structures
charts = re.findall(r'new\s+Chart\s*\(\s*document\.getElementById\(["\']([^"\']+)["\']\)', text)
print(f"\nCharts initialized: {len(charts)}")
for c in charts:
    print(f"  Chart Canvas ID: {c}")
