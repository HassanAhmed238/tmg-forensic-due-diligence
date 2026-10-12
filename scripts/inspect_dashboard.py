import re

with open(r'f:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'tab-financials' in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
