with open(r"F:\Mr Hesham\TMG\scripts\generate_powerbi_ceo_dashboard.py", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if 'id="tab-' in line:
            print(f"{i+1}: {line.strip()[:60]}")
