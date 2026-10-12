import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find("document.getElementById('financials-tbody')")
func_pos = text.rfind('function ', 0, pos)
print("Function header:", text[func_pos:func_pos+80])

# Let's see the whole function
func_end = text.find('function ', pos)
print("Full function:\n", text[func_pos:func_end])
