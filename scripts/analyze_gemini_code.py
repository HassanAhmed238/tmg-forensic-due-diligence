import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if 'function updatechartstheme(' in l.lower():
        print(f"updateChartsTheme starts at line {i+1}")
        for j in range(i, min(i+50, len(lines))):
            print(f"L{j+1}: {lines[j]}")
        break
