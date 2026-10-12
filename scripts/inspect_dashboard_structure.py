import re

with open("scripts/build_perfect_dashboard.py", "r", encoding="utf-8") as f:
    text = f.read()

tabs = re.findall(r'id=["\']tab-([^"\']+)["\']', text)
nav = re.findall(r'data-tab=["\']([^"\']+)["\']', text)
print("Tabs found:", list(dict.fromkeys(tabs)))
print("Nav found:", list(dict.fromkeys(nav)))
