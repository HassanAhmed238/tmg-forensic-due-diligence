import sys

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update switchTab to initialize financial module
target_switch = "if (tabId === 'stakeholders') {"
replacement_switch = """if (tabId === 'financials') {
        setTimeout(function() {
          if (typeof setFinView === 'function') setFinView(finCurrentView);
          if (typeof initDynamicFinancialCharts === 'function') initDynamicFinancialCharts();
          if (typeof updateFinancialKPIs === 'function') updateFinancialKPIs();
        }, 50);
      }
      if (tabId === 'stakeholders') {"""

if "if (tabId === 'financials') {" not in text:
    text = text.replace(target_switch, replacement_switch, 1)
    print("Hooked financial triggers into switchTab!")
else:
    print("switchTab already contains financial trigger.")

# 2. Update DOMContentLoaded
target_dom = "renderSwotAndTows();"
replacement_dom = """renderSwotAndTows();
      if (typeof setFinView === 'function') setFinView('is-bs');
      if (typeof updateSimCalculations === 'function') updateSimCalculations();
      if (typeof initDynamicFinancialCharts === 'function') initDynamicFinancialCharts();"""

if "if (typeof setFinView === 'function') setFinView('is-bs');" not in text:
    text = text.replace(target_dom, replacement_dom, 1)
    print("Hooked financial triggers into DOMContentLoaded!")
else:
    print("DOMContentLoaded already hooked.")

with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("All hooks saved successfully.")
