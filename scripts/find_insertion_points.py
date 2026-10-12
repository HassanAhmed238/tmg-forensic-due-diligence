import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check tab-financials boundary
fin_start = text.find('<div id="tab-financials"')
sent_start = text.find('<div id="tab-sentiment"')
print(f"tab-financials starts at char {fin_start}")
print(f"tab-sentiment starts at char {sent_start}")
print(f"tab-financials current block length: {sent_start - fin_start} chars")

# Check initCharts boundary
idx_init = text.find('function initCharts()')
idx_next_func = text.find('function updateChartsTheme()', idx_init)
print(f"initCharts starts at char {idx_init}, next func starts at {idx_next_func}")

# Check setLanguage boundary
idx_setlang = text.find('function setLanguage(lang)')
idx_next_lang = text.find('function renderProjects()', idx_setlang)
print(f"setLanguage starts at char {idx_setlang}, next func starts at {idx_next_lang}")
