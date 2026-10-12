with open(r'f:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('financials-tbody')
if idx != -1:
    with open(r'f:\Mr Hesham\TMG\scripts\fin_js_snippet.txt', 'w', encoding='utf-8') as out:
        out.write(text[idx-100:idx+2500])
    print("Found JS snippet")
else:
    print("Not found")
