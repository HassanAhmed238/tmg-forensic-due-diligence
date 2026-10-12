with open(r'f:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('financials-tbody')
if idx != -1:
    with open(r'f:\Mr Hesham\TMG\scripts\fin_snippet.txt', 'w', encoding='utf-8') as out:
        out.write(text[idx-200:idx+1500])
    print("Wrote snippet")
else:
    print("Not found")
