import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 235595
start = max(0, pos - 800)
end = min(len(text), pos + 1200)
print("=== FINANCIALS RENDER CODE ===")
print(text[start:end])
