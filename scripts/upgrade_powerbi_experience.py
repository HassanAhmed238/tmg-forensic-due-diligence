import sys, re

# Set utf-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

# Read original file
with open(r'scripts/generate_powerbi_ceo_dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original script length: {len(content)}")
