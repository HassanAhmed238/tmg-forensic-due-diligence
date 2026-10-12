import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect 1000 chars after initCharts starts
idx_init = text.find('function initCharts()')
print("=== initCharts snippet (first 1000 chars) ===")
print(text[idx_init:idx_init+1000])

# Let's find the closing brace of initCharts
# We can find 'updateChartsTheme' or similar
idx_close = text.find('function ', idx_init + 50)
print(f"\nNext function after initCharts starts at char {idx_close}")
if idx_close != -1:
    print("Next function line:", text[idx_close:idx_close+100])
