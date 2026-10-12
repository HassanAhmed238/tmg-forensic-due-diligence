import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_swot_start = text.find('id="swot-section-title"')
idx_swot_end = text.find('<!-- ========================================== -->', idx_swot_start)

print("SWOT section HTML slice:")
print(text[idx_swot_start-200:idx_swot_start+2500])
