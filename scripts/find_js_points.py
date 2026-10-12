import sys

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

idx_init = text.find('function initCharts()')
idx_setlang = text.find('function setLanguage(lang)')

print("initCharts found at char:", idx_init)
print("setLanguage found at char:", idx_setlang)

# Find where </script> is located
idx_script_end = text.rfind('</script>')
print("Last </script> found at char:", idx_script_end)
