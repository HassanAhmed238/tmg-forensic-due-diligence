import re
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', text, re.DOTALL)
print(f"Found {len(scripts)} script tags in HTML.")

for i, s in enumerate(scripts):
    code = s.strip()
    if not code:
        continue
    # write to temp file
    test_file = f"scripts/test_script_{i}.js"
    # wrap DOM-specific references in mocks so node can parse
    mock_env = """
    const document = {
      documentElement: { setAttribute: () => {}, getAttribute: () => 'ar' },
      getElementById: (id) => ({ innerHTML: '', textContent: '', value: '50000000', style: {}, classList: { toggle: () => {}, add: () => {}, remove: () => {} }, getContext: () => ({}) }),
      querySelectorAll: () => [],
      querySelector: () => null,
      addEventListener: () => {}
    };
    const window = { addEventListener: () => {} };
    const localStorage = { getItem: () => 'ar', setItem: () => {} };
    const Chart = function() { return { destroy: () => {} }; };
    const d3 = { select: () => ({ append: () => ({ attr: () => ({}) }) }) };
    """
    with open(test_file, "w", encoding="utf-8") as tf:
        tf.write(mock_env + "\n" + code)
    
    # Run node --check
    res = subprocess.run(["node", "--check", test_file], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Script {i+1} syntax check: PASSED (OK)!")
    else:
        print(f"Script {i+1} syntax check: FAILED!")
        print(res.stderr[:500])
