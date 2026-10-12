with open(r'f:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

fin_pos = text.find('id="tab-financials"')
sent_pos = text.find('id="tab-sentiment"')

print(f"tab-financials starts at char {fin_pos}, tab-sentiment starts at char {sent_pos}")
print(f"Length of tab-financials section: {sent_pos - fin_pos}")

with open(r'f:\Mr Hesham\TMG\scripts\tab_fin_current.html', 'w', encoding='utf-8') as out:
    out.write(text[fin_pos:sent_pos])

print("Wrote current tab-financials to scripts/tab_fin_current.html")
