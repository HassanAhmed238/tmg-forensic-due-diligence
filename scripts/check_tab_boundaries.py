import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/build_perfect_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

pzone_idx = text.find('id="tab-pzone"')
print("pzone_idx:", pzone_idx)

# Search for the closing tag of tab-pzone
# tab-pzone starts with <div id="tab-pzone" class="tab-pane">
# Let's find where the next major container begins, e.g. main-wrapper end or modals or scripts
script_idx = text.find('<script', pzone_idx)
print("script_idx after pzone:", script_idx)

# Print 300 chars before script_idx
print("Snippet before script_idx:")
print(text[script_idx-300:script_idx])
