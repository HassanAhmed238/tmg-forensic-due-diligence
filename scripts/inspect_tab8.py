import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/generate_powerbi_ceo_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = list(re.finditer(r'id=["\']tab-sentiment["\']', text))
print('Count:', len(m))
for item in m:
    pos = item.start()
    print('POS:', pos)
    print(text[pos:pos+300])
