import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', html, re.DOTALL)
print(f'Found {len(scripts)} inline script blocks')

for idx, script in enumerate(scripts):
    temp_path = f'F:\\Mr Hesham\\TMG\\temp_script_{idx}.js'
    with open(temp_path, 'w', encoding='utf-8') as sf:
        sf.write(script)
    res = subprocess.run(['node', '-c', temp_path], capture_output=True, text=True)
    if res.returncode != 0:
        print(f'Error in script {idx}:', res.stderr)
    else:
        print(f'Script {idx} passed node syntax check cleanly!')
