import sys
sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('id="swot-section-title"')
card_start = text.rfind('<div class="bezel-wrap"', 0, idx)
print("Card starts at pos:", card_start)
print(text[card_start:idx+300])
