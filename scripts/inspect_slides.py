import re

with open('scripts/build_perfect_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

slides = re.findall(r'class=["\']slide["\']', text)
print('Total slides in presenter mode:', len(slides))

# Find slide titles
slide_titles = re.findall(r'<div class=["\']slide-title["\']>([^<]+)</div>', text)
print("Slide titles:", slide_titles)
