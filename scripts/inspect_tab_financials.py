import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="tab-financials"' in line:
        start_line = i
        print(f"tab-financials starts at line {i+1}")
        for j in range(i, min(i+120, len(lines))):
            print(f"{j+1}: {lines[j][:120]}", end='')
            if 'id="tab-' in lines[j] and j > i:
                print(f"\nNext tab starts at line {j+1}: {lines[j]}")
                break
        break
