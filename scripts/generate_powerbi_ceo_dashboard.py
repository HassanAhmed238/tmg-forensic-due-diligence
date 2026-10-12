# -*- coding: utf-8 -*-
"""
Generate the Definitive PowerBI-Grade Executive Forensic Dashboard for TMG Holding & Subcontractors
Designed for CEO & Board Executive Presentations.
Strict Pure Dark Canvas (Zero White Mode), 14 Interactive Charts, PowerBI Slicers, Multi-Metric KPI Ribbon, D3.js Tree.
"""

output_path_1 = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"
output_path_2 = r"F:\Mr Hesham\TMG\index.html"

# We read the existing build_perfect_dashboard.py to preserve all verified datasets
with open(r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py", "r", encoding="utf-8") as f:
    orig_code = f.read()

# Extract datasets from the original code
def extract_section(start_str, end_str):
    pos1 = orig_code.find(start_str)
    if pos1 == -1:
        raise ValueError(f"Start string not found: {start_str}")
    pos2 = orig_code.find(end_str, pos1)
    if pos2 == -1:
        raise ValueError(f"End string not found: {end_str}")
    return orig_code[pos1:pos2]

projects_data_str = extract_section("const projectsData = [", "const contractorsData = [")
contractors_data_str = extract_section("const contractorsData = [", "const complaintsData = [")
complaints_data_str = extract_section("const complaintsData = [", "const risksData = [")
risks_data_str = extract_section("const risksData = [", "function renderDynamicCards() {")
privity_tree_data_str = extract_section("const privityTreeData = {", "let d3Svg, d3G, d3Zoom;")
sources_data_str = extract_section("const sourcesDB = {", "const projectsData = [") + "\n    const sourcesData = sourcesDB;\n"
slides_data_str = extract_section("const presenterSlides = [", "let currentSlide = 0;")

# Append Slide 11: Investor & Homeowner Dual Advisory to slides_data_str
slide_11_code = r'''
      ,
      {
        num: "SLIDE 11 / 11",
        titleAr: "التوجيهات المزدوجة لمستثمري البورصة (EGX: TMGH) والمشترين والملاك مع السندات الرسمية",
        titleEn: "Dual Advisory: EGX Stock Investors (TMGH) & Homeowners / Buyers with Grounded Evidence",
        noteAr: "فصل كامل بين جاذبية السهم الدفترية ومخاطر السيولة والتأجير التمويلي (60.5B @ 28.6%)، مع تحذير الملاك والمشترين من مخالفة رسوم التنازل للمادة 15 من قانون حماية المستهلك 181/2018 وسندات التخصيص.",
        noteEn: "Clear demarcation between accounting backlog and cash conversion (~31% CFO) vs consumer protection rights under Law 181/2018 Article 15 and verified land decrees.",
        contentAr: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-cyan);">
              <div class="card-title" style="color:var(--accent-cyan); display:flex; align-items:center; justify-content:space-between;">
                <span>مستثمرو البورصة (EGX: TMGH)</span>
                <span class="badge badge-med">أولويات التدقيق المالي</span>
              </div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.9; margin-top:8px; padding-inline-start:16px;">
                <li style="margin-bottom:8px;">
                  <strong>جودة التحويل النقدي (CFO):</strong> تدفق تشغيلي 3.11B فقط في H1 2026 مقابل أرباح 9.95B (تحويل 31%) لاستيعاب WIP بـ 18.26B.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('egx_filings_fy25_h126')">السند: إفصاح البورصة إيضاح 9، 102 ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>الديون والهيكل التمويلي:</strong> قروض مباشرة 16.5B + تأجير تمويلي 43.99B = إجمالي 60.5B بفائدة 28.6%.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('egx_leaseback_debt_2026')">السند: إيضاح التأجير التمويلي 10، 25 ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>طبيعة الـ Backlog:</strong> رصيد 441.2B ليس نقداً فورياً، بل التزام تشييد معرض لتضخم التكلفة.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('tmg_backlog_statutory_2025')">السند: إفصاح المبيعات التعاقدية 24 ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>حوكمة العائلة والأطراف المرتبطة:</strong> سيطرة 43.2% وأرصدة مدينة 1.90B تتطلب رقابة صارمة لحماية مساهمي الأقلية.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('fra_related_parties_2026')">السند: إفصاح الرقابة المالية 11، 120 ↗</button></div>
                </li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-amber);">
              <div class="card-title" style="color:var(--accent-amber); display:flex; align-items:center; justify-content:space-between;">
                <span>المشترون والملاك في المشروعات</span>
                <span class="badge badge-high">حماية المستهلك والقانون</span>
              </div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.9; margin-top:8px; padding-inline-start:16px;">
                <li style="margin-bottom:8px;">
                  <strong>المشترون الجدد:</strong> ملاءة الشركة القابضة ليست ضماناً للوحدة؛ تدقيق تراخيص وتخصيصات NUCA / ACUD إلزامي.
                  <div style="margin-top:4px; display:flex; gap:6px; flex-wrap:wrap;">
                    <button class="source-link" onclick="showSourceModal('nuca_acud_land_decrees')">قرارات تخصيص الأراضي ↗</button>
                    <button class="source-link" onclick="showSourceModal('state_council_madinaty')">حكم الإدارية العليا 12622 ↗</button>
                  </div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>بنود التعاقد والتأخير:</strong> فحص بنود إعفاء تأخر المرافق الحكومية، وحساب التكلفة الشاملة للوديعة والمرافق.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('tmg_standard_contract_terms')">السند: الشروط التعاقدية النموذجية ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>فروق وديعة الصيانة:</strong> مطالبات متكررة بـ 15k-45k ج.م سنوياً تستوجب طلب ميزانيات مدققة وعوائد الفوائد البنكية.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('madinaty_maintenance_audit')">السند: شكاوى فروق الصيانة المدققة ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>رسوم التنازل (Resale):</strong> فرض 5-10% يخالف صراحة المادة 15 من قانون حماية المستهلك رقم 181 لسنة 2018.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('cpa_article15_resale')">السند: نص المادة 15 (منشورات) ↗</button></div>
                </li>
              </ul>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-cyan);">
              <div class="card-title" style="color:var(--accent-cyan); display:flex; align-items:center; justify-content:space-between;">
                <span>Stock Investors (EGX: TMGH)</span>
                <span class="badge badge-med">Audit Priorities</span>
              </div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.9; margin-top:8px; padding-inline-start:16px;">
                <li style="margin-bottom:8px;">
                  <strong>Cash Conversion Gap:</strong> H1 2026 CFO was only EGP 3.11B vs EGP 9.95B net profit (31% conversion) as WIP absorbed EGP 18.26B.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('egx_filings_fy25_h126')">Evidence: EGX Filing Note 9, 102 ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>Debt & Financial Leases:</strong> Direct bank debt EGP 16.5B + leaseback EGP 43.99B = EGP 60.5B total obligations @ 28.6% interest.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('egx_leaseback_debt_2026')">Evidence: Leaseback Disclosures 10, 25 ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>Backlog Reality:</strong> EGP 441.2B unearned sales backlog is future delivery liability, not cash in hand, exposed to inflation.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('tmg_backlog_statutory_2025')">Evidence: Sales Backlog Note 24, 104 ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>Governance & Related Parties:</strong> TM Family controls 43.2% equity; EGP 1.90B related party dues require rigorous minority scrutiny.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('fra_related_parties_2026')">Evidence: FRA Governance Note 11, 120 ↗</button></div>
                </li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-amber);">
              <div class="card-title" style="color:var(--accent-amber); display:flex; align-items:center; justify-content:space-between;">
                <span>Homeowners & Prospective Buyers</span>
                <span class="badge badge-high">Consumer Protection</span>
              </div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.9; margin-top:8px; padding-inline-start:16px;">
                <li style="margin-bottom:8px;">
                  <strong>Prospective Buyers:</strong> Corporate solvency is no guarantee for unit deeds; independent NUCA / ACUD title search required.
                  <div style="margin-top:4px; display:flex; gap:6px; flex-wrap:wrap;">
                    <button class="source-link" onclick="showSourceModal('nuca_acud_land_decrees')">Land Concession Decrees ↗</button>
                    <button class="source-link" onclick="showSourceModal('state_council_madinaty')">Supreme Court Ruling 12622 ↗</button>
                  </div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>Contractual Slippage:</strong> Audit government utility delay exemption clauses and compute total lifecycle costs.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('tmg_standard_contract_terms')">Evidence: Standard Unit Sales Contract ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>Maintenance Deficit Demands:</strong> Annual EGP 15k-45k claims require independent audited statements and deposit interest accounting.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('madinaty_maintenance_audit')">Evidence: Maintenance Deficit Docket ↗</button></div>
                </li>
                <li style="margin-bottom:8px;">
                  <strong>Resale Fees:</strong> Charging 5-10% transfer fee explicitly violates Article 15 of Consumer Protection Law 181/2018.
                  <div style="margin-top:4px;"><button class="source-link" onclick="showSourceModal('cpa_article15_resale')">Evidence: Article 15 Law 181/2018 ↗</button></div>
                </li>
              </ul>
            </div>
          </div>
        `
      }
'''

# Insert slide 11 right before the closing bracket of presenterSlides array
slides_data_str = slides_data_str.rstrip()
if slides_data_str.endswith("];"):
    slides_data_str = slides_data_str[:-2] + slide_11_code + "\n  ];"
elif slides_data_str.endswith("]"):
    slides_data_str = slides_data_str[:-1] + slide_11_code + "\n  ];"

print("Successfully extracted all core datasets with Slide 11 appended.")

# Build the complete PowerBI Executive HTML
html_content = r'''<!DOCTYPE html>
<html lang="ar" data-theme="light" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TMG Holding & Subcontractors | Executive PowerBI Forensic Intelligence Dashboard</title>
  
  <!-- Fonts: Cairo, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- CDN Libraries: Chart.js & D3.js v7 -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://d3js.org/d3.v7.min.js"></script>

  <style>
    /* ==========================================================================
       POWERBI ENTERPRISE EXECUTIVE THEME (Light Mode Default + Dark Mode)
       ========================================================================== */
    :root, html[data-theme="light"] {
      --pbi-canvas-bg: #F0F2F5;
      --pbi-surface-card: #FFFFFF;
      --pbi-surface-elevated: #F8FAFC;
      --pbi-surface-sunken: #E2E8F0;
      
      --pbi-border-subtle: #E2E8F0;
      --pbi-border-highlight: #CBD5E1;
      --pbi-border-glow: rgba(2, 132, 199, 0.35);

      --pbi-accent-cyan: #0284C7;
      --pbi-accent-blue: #2563EB;
      --pbi-accent-emerald: #059669;
      --pbi-accent-amber: #D97706;
      --pbi-accent-rose: #DC2626;
      --pbi-accent-purple: #7C3AED;
      --pbi-accent-teal: #0D9488;

      --pbi-text-hero: #0F172A;
      --pbi-text-main: #1E293B;
      --pbi-text-muted: #475569;
      --pbi-text-dim: #64748B;

      --pbi-font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --pbi-font-mono: 'JetBrains Mono', monospace;
      --pbi-font-ar: 'Cairo', 'Plus Jakarta Sans', sans-serif;

      --pbi-card-shadow: 0 4px 14px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.04);
      --pbi-kpi-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);

      --diagram-bg: #FFFFFF;
      --diagram-border: #E2E8F0;
      --table-stripe: #F8FAFC;
      --table-hover: rgba(37, 99, 235, 0.06);
      --th-bg: #F1F5F9;
      --th-color: #1E293B;
    }

    html[data-theme="dark"] {
      --pbi-canvas-bg: #090D16;
      --pbi-surface-card: #111726;
      --pbi-surface-elevated: #161E31;
      --pbi-surface-sunken: #060910;
      
      --pbi-border-subtle: #1E293B;
      --pbi-border-highlight: #334155;
      --pbi-border-glow: rgba(0, 229, 255, 0.4);

      --pbi-accent-cyan: #00E5FF;
      --pbi-accent-blue: #3B82F6;
      --pbi-accent-emerald: #10B981;
      --pbi-accent-amber: #F59E0B;
      --pbi-accent-rose: #F43F5E;
      --pbi-accent-purple: #A855F7;
      --pbi-accent-teal: #14B8A6;

      --pbi-text-hero: #FFFFFF;
      --pbi-text-main: #F8FAFC;
      --pbi-text-muted: #94A3B8;
      --pbi-text-dim: #64748B;

      --pbi-card-shadow: 0 10px 30px -8px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.06);
      --pbi-kpi-shadow: 0 4px 18px -2px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.08);

      --diagram-bg: #060910;
      --diagram-border: #1E293B;
      --table-stripe: rgba(255, 255, 255, 0.015);
      --table-hover: rgba(0, 229, 255, 0.08);
      --th-bg: #161E31;
      --th-color: #CBD5E1;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html, body {
      background-color: var(--pbi-canvas-bg) !important;
      color: var(--pbi-text-main) !important;
      font-size: 13px;
      line-height: 1.55;
      min-height: 100vh;
      display: flex;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    html[data-theme="light"] { color-scheme: light !important; }
    html[data-theme="dark"] { color-scheme: dark !important; }

    html[dir="rtl"] body { font-family: var(--pbi-font-ar); }
    html[dir="ltr"] body { font-family: var(--pbi-font-sans); }

    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--pbi-canvas-bg); }
    ::-webkit-scrollbar-thumb { background: var(--pbi-border-highlight); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--pbi-accent-cyan); }

    /* Layout Structure */
    .sidebar {
      width: 280px;
      background: var(--pbi-surface-card);
      border-inline-end: 1px solid var(--pbi-border-subtle);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      position: sticky;
      top: 0;
      height: 100vh;
      z-index: 40;
    }

    .main-wrapper {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      height: 100vh;
      background: var(--pbi-canvas-bg);
    }

    /* Brand Header */
    .brand {
      padding: 18px 20px;
      border-bottom: 1px solid var(--pbi-border-subtle);
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(255,255,255,0.01);
    }

    .brand-icon {
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, var(--pbi-accent-cyan), var(--pbi-accent-blue));
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      color: #060910;
      font-size: 19px;
      box-shadow: 0 4px 15px rgba(0, 229, 255, 0.35);
      flex-shrink: 0;
    }

    .brand-title { font-weight: 800; font-size: 15px; letter-spacing: -0.01em; color: var(--pbi-text-hero); }
    .brand-subtitle { font-size: 10.5px; color: var(--pbi-accent-cyan); font-family: var(--pbi-font-mono); text-transform: uppercase; font-weight: 700; }

    /* Nav Menu */
    .nav-menu {
      padding: 14px 10px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex: 1;
      overflow-y: auto;
    }

    .nav-label {
      font-size: 10.5px;
      text-transform: uppercase;
      color: var(--pbi-text-dim);
      padding: 6px 12px 3px;
      font-weight: 800;
      letter-spacing: 0.05em;
    }

    .nav-btn {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      border-radius: 8px;
      color: var(--pbi-text-muted);
      text-decoration: none;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      background: transparent;
      border: 1px solid transparent;
      transition: all 0.15s ease;
      width: 100%;
      text-align: inherit;
    }

    .nav-btn:hover {
      background: var(--pbi-surface-elevated);
      color: var(--pbi-text-main);
      border-color: var(--pbi-border-subtle);
    }

    .nav-btn.active {
      background: rgba(0, 229, 255, 0.12);
      color: var(--pbi-accent-cyan);
      border-color: rgba(0, 229, 255, 0.3);
      font-weight: 800;
    }

    .nav-btn svg { width: 17px; height: 17px; flex-shrink: 0; }

    .sidebar-footer {
      padding: 14px 18px;
      border-top: 1px solid var(--pbi-border-subtle);
      background: var(--pbi-surface-sunken);
      font-size: 11px;
      color: var(--pbi-text-dim);
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    /* Topbar */
    .topbar {
      height: 62px;
      border-bottom: 1px solid var(--pbi-border-subtle);
      background: rgba(17, 23, 38, 0.85);
      backdrop-filter: blur(16px);
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 30;
    }

    .page-title {
      font-size: 15px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .badge-status {
      font-size: 10.5px;
      font-family: var(--pbi-font-mono);
      background: rgba(16, 185, 129, 0.12);
      color: var(--pbi-accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 2px 9px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-weight: 700;
    }

    .badge-status::before {
      content: '';
      width: 6px;
      height: 6px;
      background: var(--pbi-accent-emerald);
      border-radius: 50%;
      box-shadow: 0 0 6px var(--pbi-accent-emerald);
    }

    .topbar-actions { display: flex; align-items: center; gap: 8px; }

    .search-box { position: relative; }
    .search-box input {
      background: var(--pbi-surface-sunken);
      border: 1px solid var(--pbi-border-subtle);
      color: var(--pbi-text-main);
      border-radius: 8px;
      font-size: 12px;
      width: 240px;
      outline: none;
      transition: all 0.2s ease;
      font-family: inherit;
      padding: 6px 30px 6px 12px;
    }
    html[dir="ltr"] .search-box input { padding: 6px 12px 6px 30px; }
    .search-box input:focus {
      border-color: var(--pbi-accent-cyan);
      box-shadow: 0 0 0 2px rgba(0, 229, 255, 0.2);
      width: 290px;
    }
    .search-box svg {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 14px;
      height: 14px;
      color: var(--pbi-text-dim);
      right: 10px;
    }
    html[dir="ltr"] .search-box svg { right: auto; left: 10px; }

    .ctrl-group {
      display: inline-flex;
      align-items: center;
      background: var(--pbi-surface-sunken);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 8px;
      padding: 2px;
      gap: 2px;
    }

    .ctrl-pill {
      background: transparent;
      border: none;
      color: var(--pbi-text-muted);
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      font-family: inherit;
    }
    .ctrl-pill.active {
      background: var(--pbi-surface-elevated);
      color: var(--pbi-accent-cyan);
      box-shadow: 0 1px 4px rgba(0,0,0,0.4);
    }

    .btn-action {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      color: var(--pbi-text-muted);
      padding: 6px 13px;
      border-radius: 8px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .btn-action:hover {
      color: var(--pbi-text-hero);
      border-color: var(--pbi-border-highlight);
    }
    .btn-action.highlight {
      background: rgba(0, 229, 255, 0.12);
      border-color: rgba(0, 229, 255, 0.35);
      color: var(--pbi-accent-cyan);
    }

    /* Content Area */
    .content-area {
      padding: 22px 26px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      max-width: 1780px;
      width: 100%;
      margin: 0 auto;
    }

    .tab-pane { display: none; animation: fadeIn 0.2s ease; }
    .tab-pane.active { display: block; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ==========================================================================
       POWERBI SLICER BAR
       ========================================================================== */
    .pbi-slicer-bar {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 12px 18px;
      box-shadow: var(--pbi-card-shadow);
      margin-bottom: 20px;
    }
    .slicer-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .slicer-label {
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--pbi-accent-cyan);
      display: flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 0.04em;
    }
    .slicer-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .slicer-active-count {
      font-size: 11px;
      color: var(--pbi-text-dim);
      font-family: var(--pbi-font-mono);
    }
    .slicer-reset-btn {
      background: var(--pbi-surface-elevated);
      border: 1px solid var(--pbi-border-subtle);
      color: var(--pbi-text-muted);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }
    .slicer-reset-btn:hover {
      color: var(--pbi-text-hero);
      border-color: var(--pbi-accent-cyan);
      background: rgba(0, 229, 255, 0.1);
    }
    .slicer-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }
    @media (max-width: 1200px) {
      .slicer-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
      .slicer-grid { grid-template-columns: 1fr; }
    }
    .slicer-box {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .slicer-box-title {
      font-size: 11px;
      font-weight: 700;
      color: var(--pbi-text-muted);
    }
    .slicer-pills {
      display: flex;
      align-items: center;
      gap: 5px;
      flex-wrap: wrap;
    }
    .slicer-pill {
      background: var(--pbi-surface-elevated);
      border: 1px solid var(--pbi-border-subtle);
      color: var(--pbi-text-muted);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 9px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .slicer-pill:hover {
      border-color: var(--pbi-border-highlight);
      color: var(--pbi-text-main);
    }
    .slicer-pill.active {
      background: rgba(0, 229, 255, 0.15);
      border-color: var(--pbi-accent-cyan);
      color: var(--pbi-accent-cyan);
      box-shadow: 0 0 10px rgba(0, 229, 255, 0.2);
    }
    .slicer-pill.danger.active {
      background: rgba(244, 63, 94, 0.2);
      border-color: var(--pbi-accent-rose);
      color: var(--pbi-accent-rose);
    }
    .slicer-pill.warning.active {
      background: rgba(245, 158, 11, 0.2);
      border-color: var(--pbi-accent-amber);
      color: var(--pbi-accent-amber);
    }
    .slicer-pill.medium.active {
      background: rgba(59, 130, 246, 0.2);
      border-color: var(--pbi-accent-blue);
      color: var(--pbi-accent-blue);
    }

    /* ==========================================================================
       EXECUTIVE KPI RIBBON (6-Card Target vs Actual + SVG Sparklines)
       ========================================================================== */
    .pbi-kpi-ribbon {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 12px;
      margin-bottom: 24px;
    }
    @media (max-width: 1440px) {
      .pbi-kpi-ribbon { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 900px) {
      .pbi-kpi-ribbon { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .pbi-kpi-ribbon { grid-template-columns: 1fr; }
    }

    .pbi-kpi-card {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 14px 16px;
      box-shadow: var(--pbi-kpi-shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s ease, border-color 0.2s;
    }
    .pbi-kpi-card:hover {
      transform: translateY(-2px);
      border-color: var(--pbi-border-highlight);
    }
    .pbi-kpi-card.card-alert::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, var(--pbi-accent-rose), var(--pbi-accent-amber));
    }

    .kpi-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }
    .kpi-name {
      font-size: 11px;
      font-weight: 700;
      color: var(--pbi-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
    .kpi-status-tag {
      font-size: 9.5px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      letter-spacing: 0.02em;
    }
    .tag-cyan { background: rgba(0, 229, 255, 0.12); color: var(--pbi-accent-cyan); border: 1px solid rgba(0, 229, 255, 0.3); }
    .tag-emerald { background: rgba(16, 185, 129, 0.12); color: var(--pbi-accent-emerald); border: 1px solid rgba(16, 185, 129, 0.3); }
    .tag-rose { background: rgba(244, 63, 94, 0.12); color: var(--pbi-accent-rose); border: 1px solid rgba(244, 63, 94, 0.3); }
    .tag-amber { background: rgba(245, 158, 11, 0.12); color: var(--pbi-accent-amber); border: 1px solid rgba(245, 158, 11, 0.3); }
    .tag-purple { background: rgba(168, 85, 247, 0.12); color: var(--pbi-accent-purple); border: 1px solid rgba(168, 85, 247, 0.3); }

    .kpi-metric-row {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 8px;
    }
    .kpi-value {
      font-size: 21px;
      font-weight: 900;
      font-family: var(--pbi-font-mono);
      color: var(--pbi-text-hero);
      letter-spacing: -0.02em;
    }
    .kpi-unit {
      font-size: 12px;
      color: var(--pbi-text-dim);
      font-weight: 700;
    }
    .kpi-sparkline {
      width: 78px;
      height: 22px;
      overflow: visible;
      flex-shrink: 0;
    }

    .kpi-variance-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 10.5px;
      border-top: 1px solid rgba(255, 255, 255, 0.04);
      padding-top: 6px;
      gap: 4px;
    }
    .var-tag { font-weight: 800; font-family: var(--pbi-font-mono); }
    .var-up { color: var(--pbi-accent-emerald); }
    .var-down { color: var(--pbi-accent-rose); }
    .var-warn { color: var(--pbi-accent-amber); }
    .var-target { color: var(--pbi-text-dim); }

    /* ==========================================================================
       POWERBI 12-COLUMN MASTER ANALYTICS CANVAS
       ========================================================================== */
    .pbi-chart-grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }
    .pbi-grid-col-12 { grid-column: span 12; }
    .pbi-grid-col-6  { grid-column: span 6; }
    .pbi-grid-col-4  { grid-column: span 4; }
    .pbi-grid-col-8  { grid-column: span 8; }

    @media (max-width: 1280px) {
      .pbi-grid-col-6, .pbi-grid-col-4, .pbi-grid-col-8 {
        grid-column: span 12;
      }
    }

    .pbi-card {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 18px;
      box-shadow: var(--pbi-card-shadow);
      position: relative;
    }
    .pbi-card:hover {
      border-color: var(--pbi-border-highlight);
    }
    
    /* ==========================================================================
       POWER BI VISUAL HEADER & FOCUS MODE EXTENSIONS
       ========================================================================== */
    .pbi-visual-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--pbi-border-subtle);
      position: relative;
    }
    .pbi-visual-title-box {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .pbi-visual-actions {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      opacity: 0.85;
      transition: opacity 0.2s;
    }
    .pbi-card:hover .pbi-visual-actions {
      opacity: 1;
    }
    .pbi-visual-btn {
      background: var(--pbi-surface-sunken);
      border: 1px solid var(--pbi-border-subtle);
      color: var(--pbi-text-muted);
      border-radius: 6px;
      padding: 4px 7px;
      font-size: 11px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: all 0.15s ease;
      font-family: var(--pbi-font-sans);
    }
    .pbi-visual-btn:hover {
      color: var(--pbi-accent-cyan);
      border-color: var(--pbi-accent-cyan);
      background: rgba(2, 132, 199, 0.1);
      transform: translateY(-1px);
    }
    html[data-theme="dark"] .pbi-visual-btn:hover {
      background: rgba(0, 229, 255, 0.12);
    }

    /* Focus Mode Overlay */
    #pbi-focus-overlay {
      position: fixed;
      inset: 0;
      z-index: 9999;
      background: var(--pbi-canvas-bg);
      display: none;
      flex-direction: column;
      overflow-y: auto;
      padding: 24px 32px;
      animation: pbiFadeIn 0.2s ease-out;
    }
    #pbi-focus-overlay.active {
      display: flex;
    }
    @keyframes pbiFadeIn {
      from { opacity: 0; transform: scale(0.99); }
      to { opacity: 1; transform: scale(1); }
    }
    .focus-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 16px;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--pbi-border-highlight);
    }
    .focus-title-group h2 {
      font-size: 20px;
      font-weight: 800;
      color: var(--pbi-text-hero);
      margin: 0 0 4px 0;
    }
    .focus-title-group p {
      font-size: 13px;
      color: var(--pbi-text-muted);
      margin: 0;
    }
    .focus-tools {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .focus-content-grid {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 24px;
      flex: 1;
      min-height: 480px;
    }
    @media (max-width: 1100px) {
      .focus-content-grid { grid-template-columns: 1fr; }
    }
    .focus-chart-panel {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--pbi-card-shadow);
      min-height: 450px;
    }
    .focus-table-panel {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--pbi-card-shadow);
      max-height: 600px;
      overflow-y: auto;
    }
    .focus-table-panel h4 {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--pbi-accent-cyan);
      margin: 0 0 12px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .pbi-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    }
    .pbi-card-title {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--pbi-text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .pbi-card-subtitle {
      font-size: 11px;
      color: var(--pbi-text-dim);
      margin-top: 2px;
    }
    .pbi-chart-box {
      position: relative;
      width: 100%;
    }

    .pbi-pill-badge {
      font-size: 10.5px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      font-family: var(--pbi-font-mono);
    }
    .badge-cyan { background: rgba(0, 229, 255, 0.12); color: var(--pbi-accent-cyan); border: 1px solid rgba(0, 229, 255, 0.3); }
    .badge-emerald { background: rgba(16, 185, 129, 0.12); color: var(--pbi-accent-emerald); border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-rose { background: rgba(244, 63, 94, 0.12); color: var(--pbi-accent-rose); border: 1px solid rgba(244, 63, 94, 0.3); }
    .badge-amber { background: rgba(245, 158, 11, 0.12); color: var(--pbi-accent-amber); border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-purple { background: rgba(168, 85, 247, 0.12); color: var(--pbi-accent-purple); border: 1px solid rgba(168, 85, 247, 0.3); }

    /* Tables */
    .table-container {
      overflow-x: auto;
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 10px;
      background: var(--pbi-surface-sunken);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
    }
    thead {
      background: var(--th-bg);
      border-bottom: 1px solid var(--pbi-border-subtle);
    }
    th {
      padding: 12px 14px;
      font-size: 11px;
      text-transform: uppercase;
      color: var(--th-color);
      font-weight: 800;
      letter-spacing: 0.04em;
    }
    td {
      padding: 11px 14px;
      border-bottom: 1px solid var(--pbi-border-subtle);
      color: var(--pbi-text-main);
    }
    tbody tr:nth-child(even) { background: var(--table-stripe); }
    tbody tr:hover { background: var(--table-hover); }
    .cell-mono { font-family: var(--pbi-font-mono); font-size: 12px; }

    .source-link {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: var(--pbi-surface-elevated);
      color: var(--pbi-accent-cyan);
      border: 1px solid var(--pbi-border-subtle);
      padding: 2px 7px;
      border-radius: 5px;
      font-size: 10.5px;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
    }
    .source-link:hover {
      background: var(--pbi-accent-cyan);
      color: #060910;
      border-color: var(--pbi-accent-cyan);
    }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 2px 8px;
      border-radius: 5px;
      font-size: 10.5px;
      font-weight: 700;
    }
    .badge-low { background: rgba(16, 185, 129, 0.12); color: var(--pbi-accent-emerald); border: 1px solid rgba(16, 185, 129, 0.25); }
    .badge-med { background: rgba(59, 130, 246, 0.12); color: var(--pbi-accent-blue); border: 1px solid rgba(59, 130, 246, 0.25); }
    .badge-high { background: rgba(244, 63, 94, 0.12); color: var(--pbi-accent-rose); border: 1px solid rgba(244, 63, 94, 0.25); }

    /* D3 Interactive Graph */
    #d3-privity-tree {
      width: 100%;
      height: 480px;
      background: var(--diagram-bg);
      border: 1px solid var(--diagram-border);
      border-radius: 12px;
      position: relative;
      overflow: hidden;
    }
    .d3-node circle { stroke-width: 2px; cursor: pointer; transition: all 0.2s ease; }
    .d3-node circle:hover { r: 12px; filter: drop-shadow(0 0 8px var(--pbi-accent-cyan)); }
    .d3-node text { font-family: var(--pbi-font-sans); font-size: 11px; fill: var(--pbi-text-main); pointer-events: none; }
    .d3-link { fill: none; stroke: var(--pbi-border-highlight); stroke-width: 1.5px; stroke-opacity: 0.7; }
    .d3-controls { position: absolute; bottom: 14px; inset-inline-end: 14px; display: flex; gap: 6px; z-index: 10; }

    #node-inspector {
      position: absolute; top: 14px; inset-inline-end: 14px; width: 320px;
      background: var(--pbi-surface-card); border: 1px solid var(--pbi-border-highlight);
      border-radius: 12px; padding: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); display: none; z-index: 20;
    }
    #node-inspector.active { display: block; }

    /* Modal */
    #source-modal {
      display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.75);
      backdrop-filter: blur(8px); z-index: 999; align-items: center; justify-content: center;
    }
    #source-modal.active { display: flex; }
    .modal-box {
      width: 90%; max-width: 700px; max-height: 85vh; overflow-y: auto;
      background: var(--pbi-surface-card); border: 1px solid var(--pbi-border-highlight);
      border-radius: 14px; padding: 24px; box-shadow: 0 25px 60px rgba(0,0,0,0.6);
      display: flex; flex-direction: column; gap: 14px;
    }

    /* Presenter Overlay */
    #presenter-overlay {
      display: none; position: fixed; inset: 0; background: var(--pbi-canvas-bg);
      z-index: 100; flex-direction: column;
    }
    #presenter-overlay.active { display: flex; }
    .slide-progress { height: 4px; background: var(--pbi-border-subtle); width: 100%; }
    .slide-progress-bar { height: 100%; background: linear-gradient(90deg, var(--pbi-accent-cyan), var(--pbi-accent-blue)); width: 12.5%; }
    .presenter-viewport { flex: 1; padding: 30px; overflow-y: auto; display: flex; align-items: center; justify-content: center; }
    .slide-canvas {
      width: 100%; max-width: 1200px; background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-highlight); border-radius: 18px; padding: 36px 40px;
      box-shadow: 0 25px 60px -15px rgba(0,0,0,0.8); display: flex; flex-direction: column; gap: 18px; min-height: 540px;
    }
    .slide-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--pbi-border-subtle); padding-bottom: 14px; }
    .slide-number { font-family: var(--pbi-font-mono); font-size: 11.5px; color: var(--pbi-accent-cyan); font-weight: 700; }
    .speaker-notes-banner {
      background: var(--pbi-surface-elevated); border: 1px solid var(--pbi-border-subtle);
      border-inline-start: 4px solid var(--pbi-accent-amber); border-radius: 8px; padding: 12px 16px;
      font-size: 12px; color: var(--pbi-text-muted); display: flex; align-items: center; gap: 10px;
    }
    .presenter-dock {
      height: 60px; background: var(--pbi-surface-card); border-top: 1px solid var(--pbi-border-subtle);
      display: flex; align-items: center; justify-content: space-between; padding: 0 36px;
    }

    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    @media (max-width: 1080px) {
      .grid-2, .grid-3 { grid-template-columns: 1fr; }
    }
    .flag-card {
      background: var(--pbi-surface-elevated); border: 1px solid var(--pbi-border-subtle);
      border-radius: 10px; padding: 14px; display: flex; flex-direction: column; gap: 6px;
      border-inline-start: 4px solid var(--pbi-accent-cyan);
    }

    /* UI MOTION & UI-UX-PRO-MAX STYLING EXTENSIONS */
    .atrium-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }
    @media (max-width: 1200px) {
      .atrium-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
      .atrium-grid { grid-template-columns: 1fr; }
    }
    .atrium-card {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 12px;
      box-shadow: var(--pbi-card-shadow);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }
    .atrium-card:hover {
      transform: translateY(-3px);
      border-color: var(--pbi-accent-cyan);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }
    .atrium-card::before {
      content: '';
      position: absolute;
      top: 0;
      inset-inline: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--pbi-accent-cyan), var(--pbi-accent-blue));
    }
    .atrium-card-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
    }
    .atrium-proj-name {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--pbi-text-hero);
    }
    .atrium-entity-tag {
      font-size: 10.5px;
      font-weight: 700;
      color: var(--pbi-accent-cyan);
      font-family: var(--pbi-font-mono);
    }
    .atrium-scope-box {
      background: var(--pbi-surface-elevated);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 11.5px;
      color: var(--pbi-text-main);
      line-height: 1.6;
    }
    .atrium-partners-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }
    .partner-pill {
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      background: var(--pbi-surface-sunken);
      border: 1px solid var(--pbi-border-highlight);
      color: var(--pbi-text-main);
    }

    /* Sentiment 4-Pillar Grid */
    .sentiment-pillars-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-bottom: 24px;
    }
    @media (max-width: 1200px) {
      .sentiment-pillars-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
      .sentiment-pillars-grid { grid-template-columns: 1fr; }
    }
    .sentiment-pillar-card {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: var(--pbi-card-shadow);
      position: relative;
      overflow: hidden;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .sentiment-pillar-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }
    .pillar-card-emerald { border-inline-start: 4px solid var(--pbi-accent-emerald); }
    .pillar-card-amber { border-inline-start: 4px solid var(--pbi-accent-amber); }
    .pillar-card-purple { border-inline-start: 4px solid var(--pbi-accent-purple); }
    .pillar-card-rose { border-inline-start: 4px solid var(--pbi-accent-rose); }

    .pillar-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .pillar-title {
      font-size: 12px;
      font-weight: 800;
      color: var(--pbi-text-hero);
    }
    .pillar-badge {
      font-size: 10px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
    }
    .pillar-desc {
      font-size: 11.5px;
      color: var(--pbi-text-muted);
      line-height: 1.6;
    }
    .pillar-examples {
      font-size: 11px;
      font-weight: 700;
      color: var(--pbi-text-main);
      border-top: 1px dashed var(--pbi-border-subtle);
      padding-top: 8px;
    }

    /* Tab 10 Advisory Grid & Cards */
    .advisory-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin-bottom: 20px;
    }
    @media (max-width: 1024px) {
      .advisory-grid { grid-template-columns: 1fr; }
    }
    .advisory-card {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 18px 20px;
      box-shadow: var(--pbi-card-shadow);
      position: relative;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .advisory-card:hover {
      border-color: var(--pbi-border-highlight);
    }
    .advisory-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      border-bottom: 1px solid var(--pbi-border-subtle);
      padding-bottom: 12px;
    }
    .advisory-title-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .advisory-num-badge {
      width: 28px;
      height: 28px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 13px;
      font-family: var(--pbi-font-mono);
      flex-shrink: 0;
    }
    .advisory-body {
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 12px;
      line-height: 1.7;
      color: var(--pbi-text-main);
    }
    .advisory-callout {
      background: var(--pbi-surface-elevated);
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 11.5px;
      border-inline-start: 4px solid var(--pbi-accent-cyan);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .advisory-law-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 800;
      color: var(--pbi-accent-rose);
      background: rgba(244, 63, 94, 0.12);
      border: 1px solid rgba(244, 63, 94, 0.3);
      padding: 4px 10px;
      border-radius: 6px;
      width: fit-content;
    }
    .advisory-evidence-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px dashed var(--pbi-border-subtle);
      font-size: 11px;
      flex-wrap: wrap;
    }

    /* 8-Point Checklist Styling */
    .checklist-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-top: 14px;
    }
    @media (max-width: 1200px) {
      .checklist-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .checklist-grid { grid-template-columns: 1fr; }
    }
    .checklist-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 12px 14px;
      background: var(--pbi-surface-elevated);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 10px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .checklist-item:hover {
      border-color: var(--pbi-accent-cyan);
      transform: translateX(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .checklist-icon {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(16, 185, 129, 0.15);
      color: var(--pbi-accent-emerald);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 900;
      flex-shrink: 0;
      margin-top: 2px;
    }
    .checklist-text {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .checklist-title {
      font-size: 11.5px;
      font-weight: 800;
      color: var(--pbi-text-hero);
    }
    .checklist-sub {
      font-size: 10.5px;
      color: var(--pbi-text-muted);
      line-height: 1.45;
    }

    /* Pulse Glow Animation */
    @keyframes pulse-glow {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.6; }
      100% { transform: scale(1); opacity: 1; }
    }
    .pulse-dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--pbi-accent-emerald);
      animation: pulse-glow 2s infinite ease-in-out;
      margin-inline-end: 6px;
    }

  </style>
</head>
<body>

  <!-- ==========================================================================
       SIDEBAR NAVIGATION
       ========================================================================== -->
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-icon">T</div>
      <div>
        <div class="brand-title" id="lbl-brand-title">استخبارات طلعت مصطفى</div>
        <div class="brand-subtitle" id="lbl-brand-sub">PowerBI Executive Portal v5.0</div>
      </div>
    </div>

    <nav class="nav-menu">
      <div class="nav-label" id="lbl-nav-label">وحدات التحقيق الجنائي</div>
      
      <button class="nav-btn active" onclick="switchTab('overview')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        <span id="nav-overview">لوحة القيادة التنفيذية (Overview)</span>
      </button>

      <button class="nav-btn" onclick="switchTab('procurement')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
        <span id="nav-procurement">المشتريات المدمجة والدرع القانوني</span>
      </button>

      <button class="nav-btn" onclick="switchTab('mustakhlasat')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        <span id="nav-mustakhlasat">المستخلصات وعقبة الصرف (270d)</span>
      </button>

      <button class="nav-btn" onclick="switchTab('projects')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
        <span id="nav-projects">محفظة المشاريع والأراضي (Landbank)</span>
      </button>

      <button class="nav-btn" onclick="switchTab('contractors')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        <span id="nav-contractors">سجل المقاولين وسلاسل الإمداد</span>
      </button>

      <button class="nav-btn" onclick="switchTab('disputes')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>
        <span id="nav-disputes">الأحكام القضائية وسجلات النزاع</span>
      </button>

      <button class="nav-btn" onclick="switchTab('financials')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
        <span id="nav-financials">التحليل المالي الجنائي والسيولة</span>
      </button>

      <button class="nav-btn" onclick="switchTab('sentiment')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"/></svg>
        <span id="nav-sentiment">شكاوى المقاولين والعمال والملاك</span>
      </button>

      <button class="nav-btn" onclick="switchTab('risks')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
        <span id="nav-risks">مصفوفة المخاطر ودليل التحوط</span>
      </button>

      <button class="nav-btn" onclick="switchTab('advisory')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
        <span id="nav-advisory">توجيهات المستثمرين والملاك</span>
      </button>
    </nav>

    <div class="sidebar-footer">
      <div><span id="lbl-cutoff">تاريخ التدقيق</span>: <strong>12 أكتوبر 2026</strong></div>
      <div><span id="lbl-cap">رأس المال</span>: <strong>20.64 مليار جنيه</strong></div>
      <div style="color: var(--pbi-accent-cyan); margin-top: 4px; font-weight:800;">PowerBI Executive • v5.0</div>
    </div>
  </aside>

  <!-- ==========================================================================
       MAIN VIEWPORT
       ========================================================================== -->
  <div class="main-wrapper">
    <!-- TOP BAR -->
    <header class="topbar">
      <div class="page-title">
        <span id="current-tab-name">لوحة القيادة التنفيذية</span>
        <span class="badge-status" id="lbl-badge-audited">مدقق رسمياً من الإفصاحات ومحاضر المحاكم</span>
      </div>

      <div class="topbar-actions">
        <!-- Search Box -->
        <div class="search-box">
          <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="global-search" placeholder="ابحث عن كيان، مقاول، قضية، رقم..." onkeyup="handleGlobalSearch(this.value)">
        </div>

        <!-- Language Switcher -->
        <div class="ctrl-group">
          <button id="lang-ar" class="ctrl-pill active" onclick="setLanguage('ar')">عربي</button>
          <button id="lang-en" class="ctrl-pill" onclick="setLanguage('en')">EN</button>
        </div>

        <!-- Theme Switcher -->
        <button class="btn-action" onclick="toggleTheme()" id="btn-theme-toggle" title="تبديل الوضع (فاتح / داكن)">
          <span id="theme-toggle-icon">🌙</span>
          <span id="theme-toggle-lbl">الوضع الداكن</span>
        </button>

        <!-- Presenter Mode Button -->
        <button class="btn-action highlight" onclick="openPresenterMode()">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/></svg>
          <span id="btn-presenter-lbl">وضع العرض التنفيذي (CEO Deck)</span>
        </button>

        <!-- Export CSV / Print -->
        <button class="btn-action" onclick="window.print()">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
          <span id="btn-print-lbl">تصدير PDF / طباعة</span>
        </button>
      </div>
    </header>

    <div class="content-area">

      <!-- ==========================================================================
           POWERBI SLICER BAR (Multi-Select Interactive Filter Ribbon)
           ========================================================================== -->
      <div class="pbi-slicer-bar" id="pbi-slicer-container">
        <div class="slicer-header">
          <div class="slicer-label">
            <svg width="15" height="15" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/>
            </svg>
            <span id="lbl-slicer-title">محددات وفلاتر التحليل (POWERBI SLICERS)</span>
          </div>
          <div class="slicer-actions">
            <span class="slicer-active-count" id="slicer-filter-count">الفلاتر النشطة: كافة المشاريع (DirectQuery)</span>
            <button class="slicer-reset-btn" onclick="resetAllSlicers()">
              <svg width="12" height="12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
              </svg>
              <span id="lbl-reset-slicer">إعادة ضبط الفلاتر</span>
            </button>
          </div>
        </div>

        <div class="slicer-grid">
          <!-- SLICER 1: Project Filter -->
          <div class="slicer-box" id="slicer-project">
            <span class="slicer-box-title" id="slicer-title-proj">المشروع / الأصل المستهدف:</span>
            <div class="slicer-pills">
              <button class="slicer-pill active" data-slicer="project" data-val="all" onclick="toggleSlicer(this)">الكل (8 أصول)</button>
              <button class="slicer-pill" data-slicer="project" data-val="southmed" onclick="toggleSlicer(this)">ساوث ميد (SouthMED)</button>
              <button class="slicer-pill" data-slicer="project" data-val="noor" onclick="toggleSlicer(this)">مدينة نور (Noor City)</button>
              <button class="slicer-pill" data-slicer="project" data-val="madinaty" onclick="toggleSlicer(this)">مدينتي (Madinaty)</button>
              <button class="slicer-pill" data-slicer="project" data-val="celia" onclick="toggleSlicer(this)">سيليا (Celia)</button>
              <button class="slicer-pill" data-slicer="project" data-val="banan" onclick="toggleSlicer(this)">بنان الرياض (Banan)</button>
            </div>
          </div>

          <!-- SLICER 2: Risk Severity -->
          <div class="slicer-box" id="slicer-severity">
            <span class="slicer-box-title" id="slicer-title-sev">مستوى الحساسية الجنائية:</span>
            <div class="slicer-pills">
              <button class="slicer-pill active" data-slicer="severity" data-val="all" onclick="toggleSlicer(this)">كافة المستويات</button>
              <button class="slicer-pill danger" data-slicer="severity" data-val="critical" onclick="toggleSlicer(this)">حرج (Critical)</button>
              <button class="slicer-pill warning" data-slicer="severity" data-val="high" onclick="toggleSlicer(this)">مرتفع (High)</button>
              <button class="slicer-pill medium" data-slicer="severity" data-val="med" onclick="toggleSlicer(this)">متوسط (Medium)</button>
            </div>
          </div>

          <!-- SLICER 3: Year / Financial Period -->
          <div class="slicer-box" id="slicer-year">
            <span class="slicer-box-title" id="slicer-title-yr">الأفق الزمني للتقييم:</span>
            <div class="slicer-pills">
              <button class="slicer-pill active" data-slicer="year" data-val="all" onclick="toggleSlicer(this)">2021 – 2026</button>
              <button class="slicer-pill" data-slicer="year" data-val="h126" onclick="toggleSlicer(this)">H1 2026</button>
              <button class="slicer-pill" data-slicer="year" data-val="fy25" onclick="toggleSlicer(this)">FY2025</button>
              <button class="slicer-pill" data-slicer="year" data-val="historical" onclick="toggleSlicer(this)">2021–2024</button>
            </div>
          </div>

          <!-- SLICER 4: Contractual Entity -->
          <div class="slicer-box" id="slicer-entity">
            <span class="slicer-box-title" id="slicer-title-ent">كيان التعاقد والدرع القانوني:</span>
            <div class="slicer-pills">
              <button class="slicer-pill active" data-slicer="entity" data-val="all" onclick="toggleSlicer(this)">كافة الأطراف</button>
              <button class="slicer-pill" data-slicer="entity" data-val="acc" onclick="toggleSlicer(this)">الإسكندرية للإنشاءات (ACC)</button>
              <button class="slicer-pill" data-slicer="entity" data-val="atrium" onclick="toggleSlicer(this)">أتريوم (Atrium AQC)</button>
              <button class="slicer-pill" data-slicer="entity" data-val="subcontractor" onclick="toggleSlicer(this)">مقاول باطن (P.Zone / MEP)</button>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           EXECUTIVE KPI RIBBON (6-Card Target vs Actual + SVG Sparklines)
           ========================================================================== -->
      <div class="pbi-kpi-ribbon">
        
        <!-- KPI 1: Contracted Backlog -->
        <div class="pbi-kpi-card">
          <div class="kpi-top">
            <span class="kpi-name">المبيعات المتعاقد عليها (Backlog)</span>
            <span class="kpi-status-tag tag-cyan">حاجز تسليمات ضخم</span>
          </div>
          <div class="kpi-metric-row">
            <div class="kpi-value">> 460B <span class="kpi-unit">EGP</span></div>
            <svg class="kpi-sparkline" viewBox="0 0 100 24" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g-bkl" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.4"/>
                  <stop offset="100%" stop-color="#00E5FF" stop-opacity="0.0"/>
                </linearGradient>
              </defs>
              <path d="M0,22 L20,20 L40,15 L60,9 L80,4 L100,1 L100,24 L0,24 Z" fill="url(#g-bkl)"/>
              <path d="M0,22 L20,20 L40,15 L60,9 L80,4 L100,1" fill="none" stroke="#00E5FF" stroke-width="2"/>
              <circle cx="100" cy="1" r="2.5" fill="#00E5FF"/>
            </svg>
          </div>
          <div class="kpi-variance-row">
            <span class="var-tag var-up">▲ 441.2B نهاية 2025</span>
            <span class="var-target">يشمل ساوث ميد (280B+) ونور</span>
          </div>
        </div>

        <!-- KPI 2: Total Liquid Buffer vs Cash Conversion -->
        <div class="pbi-kpi-card card-alert">
          <div class="kpi-top">
            <span class="kpi-name">السيولة النقدية ومعدل التحويل</span>
            <span class="kpi-status-tag tag-amber">عجز تدفق تشغيلي</span>
          </div>
          <div class="kpi-metric-row">
            <div class="kpi-value">66.4B <span class="kpi-unit">/ 31.2%</span></div>
            <svg class="kpi-sparkline" viewBox="0 0 100 24" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g-cfo" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.4"/>
                  <stop offset="100%" stop-color="#F59E0B" stop-opacity="0.0"/>
                </linearGradient>
              </defs>
              <path d="M0,6 L20,9 L40,11 L60,15 L80,18 L100,20 L100,24 L0,24 Z" fill="url(#g-cfo)"/>
              <path d="M0,6 L20,9 L40,11 L60,15 L80,18 L100,20" fill="none" stroke="#F59E0B" stroke-width="2"/>
              <circle cx="100" cy="20" r="2.5" fill="#F59E0B"/>
            </svg>
          </div>
          <div class="kpi-variance-row">
            <span class="var-tag var-down">▼ CFO 3.11B فقط</span>
            <span class="var-target">احتجاز 18.26B بأعمال الإنشاء</span>
          </div>
        </div>

        <!-- KPI 3: Off-Balance Lease Liabilities -->
        <div class="pbi-kpi-card">
          <div class="kpi-top">
            <span class="kpi-name">التزامات التأجير التمويلي (ديون)</span>
            <span class="kpi-status-tag tag-purple">تمويل خارج الميزانية</span>
          </div>
          <div class="kpi-metric-row">
            <div class="kpi-value">43.99B <span class="kpi-unit">EGP</span></div>
            <svg class="kpi-sparkline" viewBox="0 0 100 24" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g-lease" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#A855F7" stop-opacity="0.4"/>
                  <stop offset="100%" stop-color="#A855F7" stop-opacity="0.0"/>
                </linearGradient>
              </defs>
              <path d="M0,22 L20,20 L40,16 L60,8 L80,4 L100,2 L100,24 L0,24 Z" fill="url(#g-lease)"/>
              <path d="M0,22 L20,20 L40,16 L60,8 L80,4 L100,2" fill="none" stroke="#A855F7" stroke-width="2"/>
              <circle cx="100" cy="2" r="2.5" fill="#A855F7"/>
            </svg>
          </div>
          <div class="kpi-variance-row">
            <span class="var-tag var-warn">▲ فائدة محلية 28.6%</span>
            <span class="var-target">تسييل رواسي والأهلي ومصر</span>
          </div>
        </div>

        <!-- KPI 4: Commercial Notes Payable -->
        <div class="pbi-kpi-card card-alert">
          <div class="kpi-top">
            <span class="kpi-name">أوراق الدفع والدائنون التجاريون</span>
            <span class="kpi-status-tag tag-rose">شيكات آجلة للمقاولين</span>
          </div>
          <div class="kpi-metric-row">
            <div class="kpi-value">> 15.79B <span class="kpi-unit">EGP</span></div>
            <svg class="kpi-sparkline" viewBox="0 0 100 24" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g-pay" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#F43F5E" stop-opacity="0.4"/>
                  <stop offset="100%" stop-color="#F43F5E" stop-opacity="0.0"/>
                </linearGradient>
              </defs>
              <path d="M0,21 L20,17 L40,14 L60,9 L80,5 L100,2 L100,24 L0,24 Z" fill="url(#g-pay)"/>
              <path d="M0,21 L20,17 L40,14 L60,9 L80,5 L100,2" fill="none" stroke="#F43F5E" stroke-width="2"/>
              <circle cx="100" cy="2" r="2.5" fill="#F43F5E"/>
            </svg>
          </div>
          <div class="kpi-variance-row">
            <span class="var-tag var-down">▲ +57.9% توسع ائتماني</span>
            <span class="var-target">دورة صرف: 90 إلى 270 يوماً</span>
          </div>
        </div>

        <!-- KPI 5: SouthMed Swimmable Lagoons & Marine Waterfront -->
        <div class="pbi-kpi-card">
          <div class="kpi-top">
            <span class="kpi-name">بحيرات ساوث ميد والواجهات</span>
            <span class="kpi-status-tag tag-cyan">مكون كهروميكانيكي</span>
          </div>
          <div class="kpi-metric-row">
            <div class="kpi-value">107 <span class="kpi-unit">KM Lagoons</span></div>
            <svg class="kpi-sparkline" viewBox="0 0 100 24" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g-water" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.4"/>
                  <stop offset="100%" stop-color="#00E5FF" stop-opacity="0.0"/>
                </linearGradient>
              </defs>
              <path d="M0,15 L25,12 L50,16 L75,8 L100,4 L100,24 L0,24 Z" fill="url(#g-water)"/>
              <path d="M0,15 L25,12 L50,16 L75,8 L100,4" fill="none" stroke="#00E5FF" stroke-width="2"/>
              <circle cx="100" cy="4" r="2.5" fill="#00E5FF"/>
            </svg>
          </div>
          <div class="kpi-variance-row">
            <span class="var-tag var-up">▲ 8 كم شاطئ رملي</span>
            <span class="var-target">مارينا دولية + 6 فنادق عالمية</span>
          </div>
        </div>

        <!-- KPI 6: Total Landbank Area -->
        <div class="pbi-kpi-card">
          <div class="kpi-top">
            <span class="kpi-name">إجمالي محفظة الأراضي (Landbank)</span>
            <span class="kpi-status-tag tag-emerald">أكبر بنك أراضٍ</span>
          </div>
          <div class="kpi-metric-row">
            <div class="kpi-value">26,722 <span class="kpi-unit">فدان</span></div>
            <svg class="kpi-sparkline" viewBox="0 0 100 24" preserveAspectRatio="none">
              <defs>
                <linearGradient id="g-land" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#10B981" stop-opacity="0.4"/>
                  <stop offset="100%" stop-color="#10B981" stop-opacity="0.0"/>
                </linearGradient>
              </defs>
              <path d="M0,18 L20,16 L40,14 L60,11 L80,7 L100,3 L100,24 L0,24 Z" fill="url(#g-land)"/>
              <path d="M0,18 L20,16 L40,14 L60,11 L80,7 L100,3" fill="none" stroke="#10B981" stroke-width="2"/>
              <circle cx="100" cy="3" r="2.5" fill="#10B981"/>
            </svg>
          </div>
          <div class="kpi-variance-row">
            <span class="var-tag var-up">~ 112 مليون م² مساحة</span>
            <span class="var-target">مدينتي، ساوث ميد، نور، بنان</span>
          </div>
        </div>

      </div>

      <!-- ==========================================================================
           TAB 1: EXECUTIVE DASHBOARD CANVAS (14 MASTER CHARTS)
           ========================================================================== -->
      <div id="tab-overview" class="tab-pane active">

        <div class="pbi-chart-grid">

          <!-- ROW 1 (6-col / 6-col): Cash Waterfall & Backlog Combo -->
          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">1. شلال تحويل السيولة النقدية (Cash Conversion Waterfall)</div>
                  <div class="pbi-card-subtitle">الأرباح المحاسبية مقابل نزوح السيولة للإنشاءات ومتحصلات العملاء (H1 2026 - مليون جنيه)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-rose" style="margin-inline-end:4px;">فجوة CFO</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartWaterfallCashFlow', '1. شلال تحويل السيولة النقدية (Cash Conversion Waterfall)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartWaterfallCashFlow')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 310px;">
                <canvas id="chartWaterfallCashFlow"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">2. نمو الإيرادات المجمعة ورصيد المبيعات المتعاقد عليها (Backlog Combo)</div>
                  <div class="pbi-card-subtitle">إيرادات التسليم السكني والفنادق (أعمدة) مقابل رصيد المبيعات غير المسلمة (خط - مليار جنيه)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-cyan" style="margin-inline-end:4px;">مؤشر تراكمي</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartRevenueBacklogCombo', '2. نمو الإيرادات المجمعة ورصيد المبيعات المتعاقد عليها (Backlog Combo)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartRevenueBacklogCombo')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 310px;">
                <canvas id="chartRevenueBacklogCombo"></canvas>
              </div>
            </div>
          </div>

          <!-- ROW 2 (4-col / 4-col / 4-col): Risk Radar, Debt Doughnut, UBO Doughnut -->
          <div class="pbi-grid-col-4">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">3. رادار أبعاد المخاطر الجنائية (6-Axis Risk Radar)</div>
                  <div class="pbi-card-subtitle">تقييم الصرف، العزل القانوني، التحكيم، والتضخم مقابل السقف الآمن (1-10)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-rose" style="margin-inline-end:4px;">تحليل 6 أبعاد</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartForensicRiskRadar', '3. رادار أبعاد المخاطر الجنائية (6-Axis Risk Radar)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartForensicRiskRadar')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 290px;">
                <canvas id="chartForensicRiskRadar"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-4">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">4. هيكل الالتزامات والديون الإجمالية (Debt Architecture)</div>
                  <div class="pbi-card-subtitle">عقود التأجير التمويلي خارج الميزانية، أوراق الدفع، والتسهيلات البنكية (مليار جنيه)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-purple" style="margin-inline-end:4px;">76.0B إجمالي الديون</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartDebtStructureTreemapDoughnut', '4. هيكل الالتزامات والديون الإجمالية (Debt Architecture)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartDebtStructureTreemapDoughnut')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 290px;">
                <canvas id="chartDebtStructureTreemapDoughnut"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-4">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">5. هيكل الملكية والمساهمين الرئيسيين (UBO Matrix)</div>
                  <div class="pbi-card-subtitle">توزيع حصص رأس المال المصدر: عائلة طلعت مصطفى والتداول الحر وصناديق السيادة</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-cyan" style="margin-inline-end:4px;">20.64B رأس المال</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartOwnershipUBODoughnut', '5. هيكل الملكية والمساهمين الرئيسيين (UBO Matrix)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartOwnershipUBODoughnut')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 290px;">
                <canvas id="chartOwnershipUBODoughnut"></canvas>
              </div>
            </div>
          </div>

          <!-- ROW 3 (6-col / 6-col): IPC Mustakhlasat S-Curve & Dispute Bubble -->
          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">6. منحنى دورة صرف المستخلصات S-Curve (تعاقدي 90 يوماً مقابل فعلي 270 يوماً)</div>
                  <div class="pbi-card-subtitle">المسار الزمني لمراحل التدقيق حتى التحصيل ومقاصة الشيكات (فجوة احتجاز 180 يوماً)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-amber" style="margin-inline-end:4px;">المستخلصات وأوراق الدفع</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartIPCMustakhlasatSCurve', '6. منحنى دورة صرف المستخلصات S-Curve (تعاقدي 90 يوماً مقابل فعلي 270 يوماً)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartIPCMustakhlasatSCurve')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 310px;">
                <canvas id="chartIPCMustakhlasatSCurve"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">7. مصفوفة حجم التعاقد مقابل مؤشر النزاعات والتوتر (Dispute Friction)</div>
                  <div class="pbi-card-subtitle">حجم التعاقد (مليار جنيه) مقابل مؤشر التوتر العلني وقضايا المحاكم والاحتجاجات (1-10)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-rose" style="margin-inline-end:4px;">خريطة الاحتكاك</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartContractorDisputeBubble', '7. مصفوفة حجم التعاقد مقابل مؤشر النزاعات والتوتر (Dispute Friction)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartContractorDisputeBubble')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 310px;">
                <canvas id="chartContractorDisputeBubble"></canvas>
              </div>
            </div>
          </div>

          <!-- ROW 4 (6-col / 6-col): Risk Heatmap & FX Escalation Tornado -->
          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">8. مقياس تعرض مقاولي الباطن للمخاطر (Subcontractor Vulnerability Gauge)</div>
                  <div class="pbi-card-subtitle">مؤشر التعرض التراكمي لسعر الصرف، تأخر الصرف، وشروط العقود (8.8 / 10 - حرج)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-rose" style="margin-inline-end:4px;">مؤشر الحساسية</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartVulnerabilityGauge', '8. مقياس تعرض مقاولي الباطن للمخاطر (Subcontractor Vulnerability Gauge)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartVulnerabilityGauge')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 310px;">
                <canvas id="chartVulnerabilityGauge"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">9. مخطط إعصار حساسية التضخم والعملة الأجنبية (FX Tornado Chart)</div>
                  <div class="pbi-card-subtitle">مستوى الانكشاف على العملة الصعبة ومخاطر استيراد معدات المياه والمضخات (P.Zone / MEP)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-amber" style="margin-inline-end:4px;">حساسية الصدمات</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartInflationTornado', '9. مخطط إعصار حساسية التضخم والعملة الأجنبية (FX Tornado Chart)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartInflationTornado')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 310px;">
                <canvas id="chartInflationTornado"></canvas>
              </div>
            </div>
          </div>

          <!-- ROW 5 (4-col / 4-col / 4-col): Landbank, Evidence Polar, P.Zone Lagoon Scope -->
          <div class="pbi-grid-col-4">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">10. توزيع محفظة الأراضي (Landbank Footprint)</div>
                  <div class="pbi-card-subtitle">المساحات الإجمالية لأبرز المدن والمشاريع التابعة للمجموعة (فدان)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-cyan" style="margin-inline-end:4px;">26,722 فدان</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('landbankBarChart', '10. توزيع محفظة الأراضي (Landbank Footprint)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('landbankBarChart')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 290px;">
                <canvas id="landbankBarChart"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-4">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">11. هرمية قوة الأدلة والموثوقية (Evidence Hierarchy)</div>
                  <div class="pbi-card-subtitle">أحكام قضائية وإفصاحات رسمية مقابل سوابق هندسية وتسويق</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-emerald" style="margin-inline-end:4px;">حجية الإثبات</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartEvidenceHierarchyPolar', '11. هرمية قوة الأدلة والموثوقية (Evidence Hierarchy)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartEvidenceHierarchyPolar')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 290px;">
                <canvas id="chartEvidenceHierarchyPolar"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-4">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">12. نطاق أعمال البحيرات P.Zone: التنفيذ مقابل الصيانة</div>
                  <div class="pbi-card-subtitle">توزيع القيمة بين التنفيذ الرأسمالي (Capex) وعقود التشغيل والصيانة (O&M)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-cyan" style="margin-inline-end:4px;">هندسة المياه</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartLagoonMEPCapexOpex', '12. نطاق أعمال البحيرات P.Zone: التنفيذ مقابل الصيانة')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartLagoonMEPCapexOpex')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 290px;">
                <canvas id="chartLagoonMEPCapexOpex"></canvas>
              </div>
            </div>
          </div>

          <!-- ROW 6 (6-col / 6-col): Complaints Breakdown & Project Slippages -->
          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">13. تحليل وتوزيع شكاوى أصحاب المصلحة (Complaints Breakdown)</div>
                  <div class="pbi-card-subtitle">فروق الصيانة، رسوم التنازل 5-10%، مستحقات المقاولين والعمال (عينة موثقة 46 واقعة)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-rose" style="margin-inline-end:4px;">46 شكوى موثقة</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartComplaints', '13. تحليل وتوزيع شكاوى أصحاب المصلحة (Complaints Breakdown)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartComplaints')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 300px;">
                <canvas id="chartComplaints"></canvas>
              </div>
            </div>
          </div>

          <div class="pbi-grid-col-6">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">14. الجداول الزمنية لتسليم المشاريع وتعديل المواعيد (Project Slippages)</div>
                  <div class="pbi-card-subtitle">مقارنة تواريخ التسليم الأصلية بالتواريخ المعدلة (أشهر التأخير المرصودة)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-amber" style="margin-inline-end:4px;">الالتزام بالتسليم</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartProjectDeliveryTimeline', '14. الجداول الزمنية لتسليم المشاريع وتعديل المواعيد (Project Slippages)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartProjectDeliveryTimeline')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 300px;">
                <canvas id="chartProjectDeliveryTimeline"></canvas>
              </div>
            </div>
          </div>

        </div>

        <!-- Verified Strategic Conclusions Cards -->
        <div class="pbi-card" style="margin-top: 10px;">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="color: var(--pbi-accent-cyan);">
                <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                <span id="t-conclusions-title">النتائج الجوهرية المدققة للفحص النافي للجهالة (Executive Findings)</span>
              </div>
              <div class="pbi-card-subtitle" id="t-conclusions-sub">مستندة للإفصاحات الرسمية، الأحكام القضائية، التحقيقات الصحفية وسجلات التنفيذ المباشرة</div>
            </div>
          </div>
          <div class="grid-3" id="conclusions-cards-container">
            <!-- Dynamically populated via JS -->
          </div>
        </div>

      </div>

      <!-- ==========================================================================
           TAB 2: CAPTIVE PROCUREMENT & D3.JS NETWORK
           ========================================================================== -->
      <div id="tab-procurement" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-proc-title">هيكل المشتريات المدمجة والشبكة التفاعلية للحجية النسبية للعقود</div>
              <div class="pbi-card-subtitle" id="t-proc-sub">شجرة D3.js التفاعلية — انقر فوق أي كيان أو شركة لفحص سند الملكية، درع الحجية القانونية، ومصدر الإثبات</div>
            </div>
            <div style="display:flex; gap:6px;">
              <button class="btn-action" onclick="resetD3View()" id="btn-reset-d3">إعادة ضبط المشهد</button>
            </div>
          </div>

          <!-- D3 Interactive Tree -->
          <div id="d3-privity-tree">
            <div class="d3-controls">
              <button class="btn-action" onclick="zoomD3(1.2)">+</button>
              <button class="btn-action" onclick="zoomD3(0.8)">-</button>
            </div>

            <!-- Node Inspector Panel -->
            <div id="node-inspector">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <strong id="inspector-name" style="font-size:13.5px; color:var(--pbi-accent-cyan);">Entity</strong>
                <button onclick="closeInspector()" style="background:none; border:none; color:var(--pbi-text-dim); cursor:pointer; font-size:14px;">✕</button>
              </div>
              <div id="inspector-type" style="font-size:11px; color:var(--pbi-text-dim); text-transform:uppercase; margin-bottom:10px; font-weight:700;">Type</div>
              <div style="font-size:12px; line-height:1.6; color:var(--pbi-text-muted); margin-bottom:10px;" id="inspector-desc">Description</div>
              <div style="border-top:1px solid var(--pbi-border-subtle); padding-top:8px; font-size:11.5px; display:flex; flex-direction:column; gap:4px;">
                <div><strong>الدرع القانوني (الحجية):</strong> <span id="inspector-shield">High</span></div>
                <div><strong>مستوى التعرض المباشر:</strong> <span id="inspector-risk">Low</span></div>
                <div style="margin-top:6px;"><span id="inspector-source-box"></span></div>
              </div>
            </div>
          </div>

          
        <!-- 4-PILLAR HYBRID CLOSED-LOOP PROCUREMENT ARCHITECTURE -->
        <div class="pbi-card" style="margin-top: 24px; border-top: 3px solid var(--pbi-accent-cyan);">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="display:flex; align-items:center; gap:8px;">
                <span class="pulse-dot"></span>
                <span>النموذج الهجين لشراكات المقاولات والتوريد (Hybrid Closed-Loop Procurement Model)</span>
              </div>
              <div class="pbi-card-subtitle">الركائز الأربع لإدارة سلاسل الإمداد، درع العزل القانوني، والدورة التمويلية عبر أوراق الدفع (Notes Payable)</div>
            </div>
            <span class="pbi-pill-badge badge-cyan">4 Strategic Pillars</span>
          </div>

          <div class="advisory-grid">
            <!-- Pillar 1 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(2,132,199,0.15); color:var(--pbi-accent-cyan);">01</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">درع المقاول الداخلي والعزل التعاقدي (Captive EPC)</strong>
                </div>
                <span class="pbi-pill-badge badge-emerald">حماية القابضة</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                عزل الذمة المالية للشركة القابضة (TMGH)؛ إسناد العمليات الإنشائية لأذرع داخلية (شركة الإسكندرية للإنشاءات ACC وشركة أتريوم AQC) أو تحالفات Tier-1 مستقلة كبرى (مثل كونكريت بلس بـ 10 مليار في ساوث ميد)، لمنع أي حجز قضائي على حسابات الشركة القابضة.
              </div>
            </div>

            <!-- Pillar 2 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(16,185,129,0.15); color:var(--pbi-accent-emerald);">02</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">فصل توريد الخامات عن عقود المصنعيات (Bulk Purchasing)</strong>
                </div>
                <span class="pbi-pill-badge badge-cyan">تحييد التضخم</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                الشراء المركزي المباشر لخامات البناء الإستراتيجية (حديد عز وبشاي، والأسمنت السائب، والكابلات من السويدي) بوفورات حجم ضخمة، وحصر عقود مقاولي الباطن على "المصنعيات والتركيبات فقط"، مما يقلل مخاطر مطالبة المقاولين بفروق أسعار الخامات.
              </div>
            </div>

            <!-- Pillar 3 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(245,158,11,0.15); color:var(--pbi-accent-amber);">03</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">الدورة التمويلية عبر أوراق الدفع (Notes Payable >15.79B)</strong>
                </div>
                <span class="pbi-pill-badge badge-amber">تمويل الموردين</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                تحويل مستحقات الموردين والمقاولين لشيكات آجلة وكمبيالات تجارية لفترات تمتد من 90 إلى 180 يوماً؛ مما يوفر خط ائتمان تشغيلي بدون فوائد مصرفية بقيمة تتجاوز 15.79 مليار جنيه لتمويل مشاريع مدينتي ونور وساوث ميد.
              </div>
            </div>

            <!-- Pillar 4 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(220,38,38,0.15); color:var(--pbi-accent-rose);">04</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">بوابات الفحص السبع وتأخر الصرف (135 - 270 يوماً)</strong>
                </div>
                <span class="pbi-pill-badge badge-rose">فجوة 180 يوماً</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                خضوع مستخلصات المقاولين لدورة تحقق دقيقة عبر 7 مراحل (حصر الكميات، تكسير الخرسانة، مراجعة المكتب الفني بالدقي، اعتماد ACC، وتأجيل الصرف)، مما يؤدي لمد أجل السيولة التشغيلية وصمود المجموعة أمام صدمات التدفق النقدي.
              </div>
            </div>
          </div>
        </div>

        <!-- Explanatory cards -->
          <div class="grid-2" style="margin-top: 20px;" id="procurement-expl-cards">
            <!-- Dynamically populated via JS -->
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 3: MUSTAKHLASAT (PAYMENT BOTTLENECK)
           ========================================================================== -->
      <div id="tab-mustakhlasat" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-must-title">عقبة دورة اعتماد مستخلصات المقاولين (المستخلصات)</div>
              <div class="pbi-card-subtitle" id="t-must-sub">التسلسل الإجرائي لتدقيق واعتماد وصرف دفعات الإنجاز التجاري وأثرها على المقاولين</div>
            </div>
          </div>

          <div style="margin-top: 14px; margin-bottom: 20px;">
            <div class="pbi-card">
              <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">مقارنة دورة صرف المستخلصات: التعاقدي (90 يوماً) مقابل المرصود فعلياً (270 يوماً)</div>
                  <div class="pbi-card-subtitle">الجدول الزمني عبر بوابات التدقيق السبع ومقاصة الشيكات الآجلة (PDC)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-rose" style="margin-inline-end:4px;">فجوة 180 يوماً</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('ipcLifecycleLineChart', 'مقارنة دورة صرف المستخلصات: التعاقدي (90 يوماً) مقابل المرصود فعلياً (270 يوماً)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('ipcLifecycleLineChart')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
              <div class="pbi-chart-box" style="height: 290px;">
                <canvas id="ipcLifecycleLineChart"></canvas>
              </div>
            </div>
          </div>

          <!-- Steps Timeline Grid -->
          <div class="grid-3" id="mustakhlasat-steps-container">
            <!-- Dynamically populated via JS -->
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 4: PROJECTS TABLE & PORTFOLIO
           ========================================================================== -->
      <div id="tab-projects" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-proj-title">سجل محفظة المشاريع الكبرى والأراضي</div>
              <div class="pbi-card-subtitle" id="t-proj-sub">يشمل تفاصيل المساحات، حصص الملكية، الشركات المالكة، وموقف الإنجاز</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="projects-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="projects-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 5: CONTRACTORS ROSTER & ATRIUM EXPANDED NETWORK
           ========================================================================== -->
      <div id="tab-contractors" class="tab-pane">
        <!-- Section A: Atrium Quality Contractors (AQC) Multi-Tier JV Network Matrix -->
        <div class="pbi-card" style="margin-bottom:20px;">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="display:flex; align-items:center;">
                <span class="pulse-dot"></span>
                <span id="lbl-atrium-matrix-title">شبكة شركة أتريوم للمقاولات (Atrium AQC) والتحالفات المشتركة</span>
              </div>
              <div class="pbi-card-subtitle" id="lbl-atrium-matrix-sub">تحليل حزم المقاول العام المتكامل، تحالفات MEP، مقاولي الباطن المتخصصين، وكبرى مكاتب الإشراف الهندسي</div>
            </div>
            <span class="pbi-pill-badge badge-cyan" id="lbl-atrium-badge">40 مشروعاً معتمداً • تحالفات دولية</span>
          </div>

          <div class="atrium-grid">
            <!-- 1. Four Seasons Luxor -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">فندق فورسيزونز الأقصر (Four Seasons Luxor)</div>
                  <div class="atrium-entity-tag">آيكون (ICON) / إيجوث (EGOTH) / TMG</div>
                </div>
                <span class="badge badge-low">EPC Turnkey</span>
              </div>
              <div class="atrium-scope-box">
                المقاول العام المتكامل للمشروع الفندقي الفاخر؛ تشكيل تحالف استراتيجي مع CCC Electromechanical لتنفيذ الحزمة الكهروميكانيكية الرئيسية (CP02).
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-blue); font-weight:800;">JV: CCC Electromechanical (CP02)</span>
                <span class="partner-pill">إدارة: Hill International</span>
                <span class="partner-pill">استشاري: مجموعة شاكر</span>
                <span class="partner-pill">مورد: كناوف مصر (Knauf)</span>
                <span class="partner-pill">تصميم: معمار إنتريرز (Mimar)</span>
                <span class="partner-pill" style="color:var(--pbi-accent-cyan);">إشراف: محمود عبد العال</span>
              </div>
            </div>

            <!-- 2. Four Seasons Cairo Capital -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">فورسيزونز نيو كايرو كابيتال (مدينتي)</div>
                  <div class="atrium-entity-tag">العربية للمشروعات (المالك) / آيكون / مدينتي</div>
                </div>
                <span class="badge badge-low">Package CP05</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ حزمة الفندق الرئيسية CP05 عبر تحالف أتريوم وCCC المشترك؛ اعتماد واستلام المواد (MIR-11) وتصميمات الإضاءة عبر شراكة ممتدة 25 عاماً.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-blue); font-weight:800;">JV: Atrium-CCC Consortium</span>
                <span class="partner-pill">باطن: Devzah SI</span>
                <span class="partner-pill">إشراف: Hill International</span>
                <span class="partner-pill">إضاءة: Andy Lang (LLD)</span>
              </div>
            </div>

            <!-- 3. Open Air Mall Madinaty -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">أوبن إير مول مدينتي (Open Air Mall)</div>
                  <div class="atrium-entity-tag">الشركة العربية للمشروعات (ACPUD)</div>
                </div>
                <span class="badge badge-low">Commercial EPC</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ المركز التجاري الأكبر؛ إسناد تصنيع وتوريد وتركيب الجمالونات والهياكل الإنشائية الحديدية لشركة إيفرلاست للمقاولات كباطن متخصص.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-cyan); font-weight:800;">باطن: Everlast Construction</span>
                <span class="partner-pill">استشاري: جماعة المهندسين (ECG)</span>
                <span class="partner-pill">المقاول العام: Atrium AQC</span>
              </div>
            </div>

            <!-- 4. East Hub Madinaty -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">إيست هب مول مدينتي (East Hub Mall)</div>
                  <div class="atrium-entity-tag">الشركة العربية للمشروعات (ACPUD)</div>
                </div>
                <span class="badge badge-low">Fit-out & MEP</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ أعمال التشطيبات المتكاملة، الواجهات المعمارية، شبكات MEP، وتوريد أنظمة الإضاءة المعمارية المتطورة من شركة سراج للإضاءة.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill">إدارة: دار الهندسة (EHAF)</span>
                <span class="partner-pill">إضاءة: Siraj Lighting</span>
                <span class="partner-pill">شراكة: سكوير (SQUARE)</span>
                <span class="partner-pill">تنفيذ: MCBS</span>
              </div>
            </div>

            <!-- 5. Celia New Capital -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">مشروع سيليا (العاصمة الإدارية الجديدة)</div>
                  <div class="atrium-entity-tag">الشركة العربية للمشروعات (ACPUD)</div>
                </div>
                <span class="badge badge-med">Villages & Services</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ حزم الفيلات وقرى سيليا السكنية ومراكز الخدمات والبنية التحتية واللاندسكيب بإشراف استشاري حمزة وشركاه، مع عزل تعاقدي يحمي القابضة.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill">استشاري: حمزة وشركاه (Hamza)</span>
                <span class="partner-pill">المقاول العام: Atrium AQC</span>
                <span class="partner-pill">المالك: العربية للمشروعات</span>
              </div>
            </div>

            <!-- 6. Noor Smart City -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">مدينة نور الذكية (حدائق العاصمة)</div>
                  <div class="atrium-entity-tag">الشركة العربية للاستثمار العمراني</div>
                </div>
                <span class="badge badge-low">Smart Superstructures</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ حزمة 72 عمارة سكنية وفيلات فاخرة؛ توريد خلايا الجهد المتوسط الذكية Simoprime 24 kV من إيماس السويدي بإشراف مجموعة شاكر.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill">مورد: إيماس السويدي (EMAS)</span>
                <span class="partner-pill">استشاري: مجموعة شاكر (Shaker)</span>
                <span class="partner-pill">حزم الفيلات: كونكريت بلس</span>
              </div>
            </div>

            
            <!-- 8. Concrete Plus & TMG Strategic Partnership (SouthMED & Noor City) -->
            <div class="atrium-card" style="border-top: 3px solid var(--pbi-accent-cyan);">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name" style="color:var(--pbi-accent-cyan);">كونكريت بلس للمقاولات والتنمية (Concrete Plus)</div>
                  <div class="atrium-entity-tag">مشروع ساوث ميد (SouthMED) + مدينة نور (Noor City)</div>
                </div>
                <span class="badge badge-low" style="background:rgba(2,132,199,0.15); color:var(--pbi-accent-cyan); border:1px solid rgba(2,132,199,0.3);">عقد 10 مليار جنيه</span>
              </div>
              <div class="atrium-scope-box">
                <strong style="color:var(--pbi-text-hero);">نطاق ساوث ميد (يناير 2026):</strong> إسناد حزمة المنطقة (Zone C01) لبناء وتشطيب <strong>179 مبنى وعمارة سكنية</strong> وشبكات المرافق التحتية بالساحل الشمالي (المستهدف 2029).<br>
                <strong style="color:var(--pbi-text-hero); margin-top:4px; display:inline-block;">امتداد الشراكة (مدينة نور):</strong> تنفيذ قطاع الفيلات V3.2 (~170 فيلا سكنية فاخرة). كمقاول عام فئة أولى (Tier-1) مستقل للطاقات الفائضة (Overflow Capacity).
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-emerald); font-weight:800;">حالة المستخلصات: صفر قضايا نزاع</span>
                <span class="partner-pill">حجم العقد: 10,000,000,000 EGP</span>
                <span class="partner-pill">المقاول: كونكريت بلس (Tier-1)</span>
                <span class="partner-pill">المالك: TMG / ساوث ميد</span>
                <button class="source-link" onclick="showSourceModal('concrete_plus_southmed_contract')" style="margin-inline-start:auto;">بيان العقد ↗</button>
              </div>
            </div>

            <!-- 7. Cairo Gate & Townsquare Offices (Emaar Misr) -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">كايرو جيت - تاون سكوير (Cairo Gate)</div>
                  <div class="atrium-entity-tag">شركة إعمار مصر للتنمية (Emaar Misr)</div>
                </div>
                <span class="badge badge-low">Delivered Turnkey</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ الأعمال الإنشائية والتشطيبات المتكاملة لمباني مكاتب تاون سكوير بوتيك المتطورة كأحد مشاريع المقاولات لصالح عميل إقليمي مرموق (إعمار مصر).
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-emerald); font-weight:800;">العميل: إعمار مصر (Emaar)</span>
                <span class="partner-pill">المقاول العام: Atrium AQC</span>
                <span class="partner-pill">تسليم تجاري ناجح</span>
                <span class="partner-pill">صفر نزاعات مستحقات</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Section B: Primary Contractors & Subcontractors Searchable Table -->
        <div class="pbi-card" style="margin-bottom:20px;">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-cont-title">سجل المقاولين الرئيسيين ومقاولي الباطن وسلاسل الإمداد</div>
              <div class="pbi-card-subtitle" id="t-cont-sub">خريطة التعاقدات المنفذة عبر شركة الإسكندرية وأتريوم والمقاولين المستقلين والموردين</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="contractors-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="contractors-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section C: 8-Point Documentary Diligence Checklist for CEO -->
        <div class="pbi-card" style="background:var(--pbi-surface-sunken); border:1px solid var(--pbi-border-highlight);">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="color:var(--pbi-accent-cyan);">قائمة التحقق المستندي الثمانية لعقود المقاولات (8-Point Forensic Checklist)</div>
              <div class="pbi-card-subtitle">المستندات الإلزامية المطلوب فحصها قبل توقيع أي صفقة أو تسوية مستحقات لفصل النزاعات التاريخية عن الالتزامات النافذة</div>
            </div>
            <span class="pbi-pill-badge badge-emerald">معايير فحص العناية الواجبة (Due Diligence)</span>
          </div>

          <div class="checklist-grid">
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">1. العقد الموقع وأمر الإسناد</div>
                <div class="checklist-sub">فحص الكيان القانوني الموقع وتحديد بنود الدفع وغرامات التأخير.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">2. تقويم ومدد الاعتماد</div>
                <div class="checklist-sub">تدقيق المدى الزمني لحصر الكميات بالموقع وتوقيع مهندسي الإشراف.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">3. سجل المستخلصات الجارية (IPC)</div>
                <div class="checklist-sub">تتبع تواريخ التقديم، الاعتماد الهندسي، تاريخ الاستحقاق الفعلي، وتاريخ التحصيل.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">4. سجل مبالغ الضمان (Retention)</div>
                <div class="checklist-sub">بيان نسبة الـ 5-10% المحتجزة وتاريخ استحقاق الإفراج الابتدائي والنهائي.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">5. سجل الأوامر التغييرية (VOs)</div>
                <div class="checklist-sub">فصل الأعمال الإضافية المعتمدة رسمياً عن المطالبات الشفهية غير المسندة.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">6. سجل الاستقطاعات والجزاءات</div>
                <div class="checklist-sub">حصر الخصومات المطبقة على مقاولي الباطن وأسبابها الهندسية المعتمدة.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">7. مخالصة الحساب الختامي</div>
                <div class="checklist-sub">تسوية الحسابات الختامية الموقعة بين المقاول العام والكيان التابع.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">8. شهادة إبراء الذمة (Close-Out)</div>
                <div class="checklist-sub">استلام شهادة إخلاء الطرف النهائية وانقضاء مدة الضمان العشري أو الصيانة.</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 6: JUDICIAL & ARBITRATION RECORDS
           ========================================================================== -->
      <div id="tab-disputes" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-disp-title">سجل النزاعات القضائية، التحكيم، وقرارات حماية المستهلك</div>
              <div class="pbi-card-subtitle" id="t-disp-sub">حكم بطلان عقد مدينتي التاريخي (2010)، النزاعات العمالية، وقضايا رسوم التنازل</div>
            </div>
          </div>

          <div class="grid-2" id="disputes-cards-container">
            <!-- Dynamically populated via JS -->
          </div>

          <!-- 5-Point Verification Gap Protocol Card from Corporate Risk Report -->
          <div class="pbi-card" style="margin-top:20px; background:var(--pbi-surface-sunken); border:1px solid rgba(0, 229, 255, 0.25);">
            <div class="pbi-card-header">
              <div>
                <div class="pbi-card-title" style="color:var(--pbi-accent-cyan);" id="lbl-gap-protocol-title">بروتوكول إغلاق فجوة التحقق لمقاولي الباطن والمستخلصات (Verification Gap Protocol)</div>
                <div class="pbi-card-subtitle" id="lbl-gap-protocol-sub">المستندات الخمسة الإلزامية للفصل بين الشكاوى التاريخية والالتزامات القانونية النافذة وفق تقرير العناية الواجبة (مدينتي وسقالات 2012)</div>
              </div>
              <span class="pbi-pill-badge badge-cyan">5 محاور فحص</span>
            </div>
            <div class="grid-3" style="margin-top:10px;" id="verification-gap-grid">
              <!-- Rendered via JS -->
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 7: FINANCIAL FORENSICS MATRIX
           ========================================================================== -->
      <div id="tab-financials" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-fin-table-title">المصفوفة المالية الجنائية للقوائم المدققة وميزانيات المجموعة (2021 – 2026)</div>
              <div class="pbi-card-subtitle" id="t-fin-table-sub">كافة الأرقام بملايين الجنيهات، مدققة من تقارير مراقبي الحسابات المودعة بالبورصة المصرية</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="financials-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="financials-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 8: CUSTOMER & LABOR SENTIMENT & CONTRACTOR INTELLIGENCE
           ========================================================================== -->
      <div id="tab-sentiment" class="tab-pane">
        <!-- 4-Pillar Sentiment & Attribution Hierarchy Cards -->
        <div class="sentiment-pillars-grid">
          <!-- Pillar 1 -->
          <div class="sentiment-pillar-card pillar-card-emerald">
            <div class="pillar-header">
              <div class="pillar-title">1. شراكات مستمرة وتكرار أعمال</div>
              <span class="pillar-badge badge-emerald">Level A/B</span>
            </div>
            <div class="pillar-desc">
              عقود رسمية وشراكات ممتدة تعكس استمرارية تجارية ونجاح تسليم الحزم الكبرى؛ لا تتضمن بيانات علنية عن مدد سداد المستخلصات.
            </div>
            <div class="pillar-examples">
              ● كونكريت بلس (10B ساوث ميد بعد نور)<br>
              ● تحالف CCC وأتريوم (الأقصر والقاهرة)<br>
              ● أندي لانغ LLD (شراكة 25 عاماً في 6 فنادق)
            </div>
          </div>

          <!-- Pillar 2 -->
          <div class="sentiment-pillar-card pillar-card-amber">
            <div class="pillar-header">
              <div class="pillar-title">2. أجور وظروف العمالة الداخلية</div>
              <span class="pillar-badge badge-amber">Level A/B</span>
            </div>
            <div class="pillar-desc">
              احتجاجات ومذكرات للعاملين والمهندسين وحرس الأمن بشركة الإسكندرية للإنشاءات تخص الرواتب والتأمين؛ سياق عمالي منفصل عن فواتير المقاولين.
            </div>
            <div class="pillar-examples">
              ● 100+ عامل بالإسكندرية (مارس 2024)<br>
              ● 400 مهندس بشركة الإسكندرية (مارس 2024)<br>
              ● حرس أمن مدينتي (المنصة - أكتوبر 2025)
            </div>
          </div>

          <!-- Pillar 3 -->
          <div class="sentiment-pillar-card pillar-card-purple">
            <div class="pillar-header">
              <div class="pillar-title">3. مخاطر سلاسل الدفع العليا</div>
              <span class="pillar-badge badge-purple">Level D</span>
            </div>
            <div class="pillar-desc">
              ادعاءات أهالي ومقاولي باطن محليين بعدم سداد مستحقات؛ نسبت التقارير التأخير لسداد جهات عليا للمقاولين، دون ثبوت مديونية مباشرة على طلعت مصطفى.
            </div>
            <div class="pillar-examples">
              ● مقاولو باطن ساوث ميد (مدى مصر نوفمبر 2024)<br>
              ● مصدر محلي غير محدد بالاسم أو المستند<br>
              ● انقطاع الحجية المباشرة مع المطور القابض
            </div>
          </div>

          <!-- Pillar 4 -->
          <div class="sentiment-pillar-card pillar-card-rose">
            <div class="pillar-header">
              <div class="pillar-title">4. مطالبات المستحقات المباشرة</div>
              <span class="pillar-badge badge-rose">Level A/B</span>
            </div>
            <div class="pillar-desc">
              نزاعات موثقة بمحاضر نيابة وقضايا محاكم تخص مستحقات مقاولي باطن مدنيين تجاه المقاول العام المدمج (شركة الإسكندرية للإنشاءات).
            </div>
            <div class="pillar-examples">
              ● شحاتة حسن وبلاغ النيابة (أكتوبر 2008)<br>
              ● اعتراف إبراهيم حسبو بتعمد التعطيل آنذاك<br>
              ● دعوى 2923/2012 سقالات (609 ألف ج.م)
            </div>
          </div>
        </div>

        <!-- Evidence Classification Chart & Attribution Rules Grid -->
        <div class="grid-2" style="margin-bottom:20px;">
          <div class="pbi-card">
            <div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">توزيع الأدلة الجنائية ومصادر التحقق (Evidence Hierarchy Breakdown)</div>
                  <div class="pbi-card-subtitle">تصنيف نتائج الفحص الاستقصائي وفق معايير الإثبات القضائي والتوثيق التجاري (15 مخططاً)</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge badge-cyan" style="margin-inline-end:4px;">Chart 15 • Polar Area</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('chartEvidenceSentiment', 'توزيع الأدلة الجنائية ومصادر التحقق (Evidence Hierarchy Breakdown)')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('chartEvidenceSentiment')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>
            <div style="height:320px; position:relative;">
              <canvas id="chartEvidenceSentiment"></canvas>
            </div>
          </div>

          <div class="pbi-card">
            <div class="pbi-card-header">
              <div>
                <div class="pbi-card-title">مستويات الإثبات الجنائي وقواعد العزل التعاقدي (Attribution Rules)</div>
                <div class="pbi-card-subtitle">الضوابط القانونية للفصل بين ادعاءات النشر وحقيقة الالتزام المالي على المجموعة</div>
              </div>
            </div>
            <div style="display:flex; flex-direction:column; gap:10px; font-size:11.5px; line-height:1.65;">
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-emerald);">
                <strong style="color:var(--pbi-text-hero);">Level A — علاقة تجارية موثقة بمستندات مستقلة:</strong><br>
                تحديد أطراف العقد بدقة (المشروع، النطاق، القيمة)، مثل إفصاحات البورصة، محاضر المحاكم، وعقود التمويل المشترك.
              </div>
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-cyan);">
                <strong style="color:var(--pbi-text-hero);">Level B — بيانات رسمية صادرة عن الشركات:</strong><br>
                منشورات الشركاء والموردين والمصممين حول إنجاز الأعمال أو توريد المهمات، وهي أدلة استمرارية ولا تثبت تواريخ السداد.
              </div>
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-amber);">
                <strong style="color:var(--pbi-text-hero);">Level C — تحليلات فنية عامة لصناعة المقاولات:</strong><br>
                دراسات استشارية تشرح أثر تأخر المستخلصات على مقاولي الباطن دون توجيه اتهام مباشر لمجموعة طلعت مصطفى.
              </div>
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-rose);">
                <strong style="color:var(--pbi-text-hero);">Level D — ادعاءات مجهولة المصدر أو غير مؤيدة:</strong><br>
                أخبار صحفية تنقل عن مصادر مجهولة تأخر دفعات، مع انقطاع السند التعاقدي المباشر مع الشركة القابضة.
              </div>
            </div>
          </div>
        </div>

        <!-- Complaints and Sentiment Table -->
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-sent-table-title">سجل الشكاوى التفصيلي: المقاولون، عمال المقاولات، واتحادات السكان</div>
              <div class="pbi-card-subtitle" id="t-sent-table-sub">يتضمن واقعة مقاول مدينتي التاريخية، احتجاجات عمال الإسكندرية للإنشاءات، وبلاغات الملاك</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="complaints-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="complaints-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 9: RISK MATRIX & DILIGENCE HEDGING
           ========================================================================== -->
      <div id="tab-risks" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-risk-table-title">مصفوفة المخاطر الجنائية المتكاملة وإجراءات التحوط المقترحة للمقاولين</div>
              <div class="pbi-card-subtitle" id="t-risk-table-sub">دليل شامل لحماية التدفقات النقدية وتفادي شرط الحجية النسبية وأوراق الدفع الآجلة</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="risks-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="risks-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- ==========================================================================
           TAB 10: INVESTOR & HOMEOWNER DUAL ADVISORY (EGX: TMGH & BUYERS)
           ========================================================================== -->
      <div id="tab-advisory" class="tab-pane">
        
        <!-- SECTION 1: EGX STOCK INVESTORS (TMGH) -->
        <div class="pbi-card" style="margin-bottom: 24px;">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="display:flex; align-items:center; gap:8px;">
                <span class="pulse-dot"></span>
                <span id="t-adv-investor-title">أولاً: توجيهات وتحليل لمستثمري البورصة المصرية (EGX: TMGH)</span>
              </div>
              <div class="pbi-card-subtitle" id="t-adv-investor-sub">فحص جودة الأرباح، تحويل التدفقات النقدية (CFO)، هيكل الديون المباشرة والتأجير التمويلي، وحوكمة العائلة</div>
            </div>
            <div style="display:flex; gap:8px;">
              <span class="pbi-pill-badge badge-cyan">EGX: TMGH</span>
              <span class="pbi-pill-badge badge-amber">Capital Markets</span>
            </div>
          </div>

          <div class="advisory-grid">
            
            <!-- Pillar 1: Cash Conversion -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(0, 229, 255, 0.15); color:var(--pbi-accent-cyan);">01</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-inv1-title">قوة الزخم المالي مقابل جودة التحويل النقدي (Cash Conversion)</strong>
                </div>
                <span class="pbi-pill-badge badge-rose" id="lbl-adv-inv1-badge">نسبة تحويل ~31%</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">الأداء الربحي المعترف به:</strong>
                  حققت المجموعة إيرادات قياسية بلغت <strong style="color:var(--pbi-accent-cyan);">62.5 مليار جنيه</strong> (+46%) وصافي ربح <strong style="color:var(--pbi-accent-emerald);">18.2 مليار جنيه</strong> (+43%) في FY2025، وواصلت النمو في النصف الأول من H1 2026 بـ <strong>30.19 مليار جنيه</strong> إيرادات و <strong>9.95 مليار جنيه</strong> أرباحاً موحدة.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-rose);">
                  <strong style="color:var(--pbi-accent-rose);">فجوة التدفق النقدي التشغيلي (CFO Gap):</strong>
                  بلغت التدفقات النقدية التشغيلية الفعلية <strong style="color:var(--pbi-accent-rose);">3.11 مليار جنيه فقط</strong> في H1 2026 مقارنة بالأرباح الدفترية المجمعة (9.95B)، بنسبة تحويل نقدي متدنية بلغت نحو <strong>31%</strong>.
                </div>
                <div style="font-size:11.5px; color:var(--pbi-text-muted);">
                  <strong>السبب الجنائي والتشغيلي:</strong> امتصاص مشروعات التطوير العقاري الجارية والأعمال تحت التنفيذ (WIP) ورأس المال العامل لسيولة نقدية ضخمة بلغت <strong style="color:var(--pbi-accent-amber);">18.26 مليار جنيه</strong> خلال النصف الأول من عام 2026.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-cyan);">
                  <strong>المعيار الاستثماري للتقييم:</strong> ينبغي لمستثمر البورصة عدم الاكتفاء بالأرباح المحاسبية المقيدة دفترياً بنسبة الإنجاز ومراقبة تحولها الفعلي لسيولة حرة (Free Cash Flow) موزعة عبر الفترات القادمة.
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                  <span>إفصاح البورصة المصرية: إيضاح 9، 102 (H1 2026)</span>
                </span>
                <button class="source-link" onclick="showSourceModal('egx_filings_fy25_h126')">فحص السند الرسمي ↗</button>
              </div>
            </div>

            <!-- Pillar 2: Debt & Leasing -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(244, 63, 94, 0.15); color:var(--pbi-accent-rose);">02</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-inv2-title">هيكل التمويل والديون المباشرة وغير المباشرة (Leaseback)</strong>
                </div>
                <span class="pbi-pill-badge badge-rose" id="lbl-adv-inv2-badge">التزامات 60.5B @ 28.6%</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">الديون المصرفية المباشرة:</strong>
                  سجلت التسهيلات الائتمانية والقروض البنكية المباشرة نحو <strong style="color:var(--pbi-accent-amber);">16.5 مليار جنيه</strong> حتى إقفال يونيو 2026.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-purple);">
                  <strong style="color:var(--pbi-accent-purple);">التزامات التأجير التمويلي غير المقيدة كقروض (Off-Balance Debt):</strong>
                  ترتبط المجموعة بعقود إيجار تمويلي عن بيع وإعادة استئجار أصول تجارية وفندقية بقيمة <strong style="color:var(--pbi-accent-purple);">43.99 مليار جنيه</strong> (مع شركات تابعة كـ "رواسي" التابعة للبنك الأهلي وبنك مصر).
                </div>
                <div>
                  <strong style="color:var(--pbi-text-hero);">إجمالي الالتزامات الفعلية وتكلفة الفائدة:</strong>
                  يصل إجمالي التزامات التمويل والرافعة المالية الحقيقية إلى <strong style="color:var(--pbi-accent-rose);">60.5 مليار جنيه</strong>، مع متوسط فائدة فعلي قياسي على الجنيه المصري يبلغ <strong style="color:var(--pbi-accent-rose);">28.6%</strong>، مما يضع أعباء وتكاليف تمويل سنوية باهظة تمتص عوائد التشغيل.
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                  <span>إيضاح مالي 10، 25، 101: التأجير التمويلي ورواسي</span>
                </span>
                <button class="source-link" onclick="showSourceModal('egx_leaseback_debt_2026')">فحص السند الرسمي ↗</button>
              </div>
            </div>

            <!-- Pillar 3: Backlog Reality -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(245, 158, 11, 0.15); color:var(--pbi-accent-amber);">03</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-inv3-title">طبيعة رصيد المبيعات التعاقدية غير المسلمة (Backlog Reality)</strong>
                </div>
                <span class="pbi-pill-badge badge-amber" id="lbl-adv-inv3-badge">رصيد 441.2B جنيه</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">ضخامة الرصيد التعاقدي:</strong>
                  تمتلك المجموعة رصيد مبيعات تعاقدية مؤجلة قياسياً يتجاوز <strong style="color:var(--pbi-accent-amber);">441.2 مليار جنيه</strong> بنهاية عام 2025 ونحو 460 مليار جنيه في منتصف 2026.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-cyan);">
                  <strong>رؤية الإيرادات المستقبلية:</strong> يضمن هذا الرصيد تدفقات إيرادية مسجلة محاسبياً لعدة سنوات قادمة عند تسليم الوحدات السكنية في مشروعات مدينتي، نور، وسيليا.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-rose);">
                  <strong style="color:var(--pbi-accent-rose);">المخاطر التضخمية والتنفيذية:</strong>
                  هذا الرصيد <strong style="color:var(--pbi-accent-rose);">ليس نقداً فورياً في الخزينة</strong>، بل التزام تشييد مستقبلي يضع الشركة تحت مخاطر تضخم تكلفة مواد البناء (حديد، أسمنت، إلكتروميكانيكال) حال تأخر الجداول الزمنية أو تعثر سلاسل الإمداد.
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                  <span>إفصاح المبيعات التعاقدية: إيضاح 24، 104</span>
                </span>
                <button class="source-link" onclick="showSourceModal('tmg_backlog_statutory_2025')">فحص السند الرسمي ↗</button>
              </div>
            </div>

            <!-- Pillar 4: Corporate Governance -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(16, 185, 129, 0.15); color:var(--pbi-accent-emerald);">04</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-inv4-title">الحوكمة وهيكل الملكية والأطراف ذات الصلة (Related Parties)</strong>
                </div>
                <span class="pbi-pill-badge badge-cyan" id="lbl-adv-inv4-badge">سيطرة العائلة 43.2%</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">هيكل السيطرة العائلية:</strong>
                  تسيطر عائلة طلعت مصطفى عبر شركاتها الاستثمارية الخاصة والمباشرة على <strong style="color:var(--pbi-accent-cyan);">43.2%</strong> من إجمالي أسهم الشركة القابضة المدرجة بالبورصة.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-amber);">
                  <strong style="color:var(--pbi-accent-amber);">أرصدة الأطراف ذات الصلة (Related-Party Balances):</strong>
                  بلغت الأرصدة المدينة المستحقة من أطراف ذات صلة <strong style="color:var(--pbi-accent-amber);">1.90 مليار جنيه</strong> في يونيو 2026 (مقارنة بـ 2.45 مليار جنيه في نهاية عام 2025).
                </div>
                <div style="font-size:11.5px; color:var(--pbi-text-muted);">
                  <strong>توصية الحوكمة لمساهمي الأقلية (Minority Protection):</strong> ضرورة التدقيق المستمر من قبل لجنة المراجعة ومراقبي الحسابات والأعضاء المستقلين في مجلس الإدارة لضمان أن كافة المعاملات البينية تتم وفق مبدأ السعر المحايد (Arm's Length) وبما يحمي حقوق حملة الأسهم الأقلية.
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                  <span>الهيئة العامة للرقابة المالية: إيضاح 11، 120</span>
                </span>
                <button class="source-link" onclick="showSourceModal('fra_related_parties_2026')">فحص السند الرسمي ↗</button>
              </div>
            </div>

          </div>
        </div>

        <!-- SECTION 2: PROSPECTIVE BUYERS & EXISTING PROPERTY OWNERS -->
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="display:flex; align-items:center; gap:8px;">
                <span class="pulse-dot" style="background:var(--pbi-accent-amber);"></span>
                <span id="t-adv-buyers-title">ثانياً: توجيهات للمشترين والملاك في مشروعات المجموعة (Buyers & Owners Advisory)</span>
              </div>
              <div class="pbi-card-subtitle" id="t-adv-buyers-sub">الفحص النافي للجهالة قبل التعاقد، تدقيق وديعة الصيانة، والمخالفة الصريحة لقانون حماية المستهلك رقم 181 لسنة 2018</div>
            </div>
            <div style="display:flex; gap:8px;">
              <span class="pbi-pill-badge badge-amber">Consumer Protection</span>
              <span class="pbi-pill-badge badge-rose">Law 181/2018 Art.15</span>
            </div>
          </div>

          <div class="advisory-grid">

            <!-- Card 1: Prospective Buyers - Solvency vs Legal Deed -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(2, 132, 199, 0.15); color:var(--pbi-accent-cyan);">A</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-buy1-title">المشترون الجدد: الملاءة المؤسسية ليست ضماناً فردياً للوحدة</strong>
                </div>
                <span class="pbi-pill-badge badge-cyan">Due Diligence</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">قاعدة الفصل التعاقدي:</strong>
                  الملاءة المالية الضخمة للشركة القابضة وشهرتها التسويقية تمثل خلفية إيجابية، لكنها <strong style="color:var(--pbi-accent-rose);">لا تُغني إطلاقاً</strong> عن الفحص الفردي والمستقل للموقف القانوني والتنفيذي للوحدة والمشروع محل التعاقد.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-cyan);">
                  <strong>الفحص المستندي لسندات الأرض:</strong> التحقق عبر مستشار قانوني عقاري متخصص من تراخيص المشروع، والقرارات الوزارية المعتمدة، وسندات تخصيص الأرض من هيئة المجتمعات العمرانية (NUCA) أو شركة العاصمة الإدارية (ACUD) للتأكد من سداد أقساط الأرض وعدم وجود رهون تجارية للبنوك على المرحلة.
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                  <span>قرارات مجلس الوزراء وهيئة المجتمعات (NUCA)</span>
                </span>
                <div style="display:flex; gap:6px; flex-wrap:wrap;">
                  <button class="source-link" onclick="showSourceModal('nuca_acud_land_decrees')">سند التخصيص ↗</button>
                  <button class="source-link" onclick="showSourceModal('state_council_madinaty')">حكم 12622 ↗</button>
                </div>
              </div>
            </div>

            <!-- Card 2: Contractual Clauses & Delivery Delay -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(245, 158, 11, 0.15); color:var(--pbi-accent-amber);">B</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-buy2-title">مراجعة بنود العقد وشروط التأخير والتكاليف الإضافية</strong>
                </div>
                <span class="pbi-pill-badge badge-amber">Contract Risk</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">اشتراطات غرامات التأخير:</strong>
                  فحص مواعيد التسليم المحددة بدقة، والتحقق من بنود التعويضات، مع الانتباه للبنود النموذجية التي تعفي المطور من المسؤولية عند "تأخر المرافق الحكومية السيادية" كذريعة للقوة القاهرة.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-amber);">
                  <strong>حساب دورة التكلفة الإجمالية (Total Cost of Ownership):</strong> حساب إجمالي الأعباء قبل التوقيع: أقساط الوحدة + دفعة الاستلام + نسبة وديعة الصيانة (5% إلى 8%) + رسوم مقايسات عدادات المياه والكهرباء والغاز وشروط ورسوم التنازل أو الإلغاء.
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                  <span>العقد النموذجي وإعفاءات المرافق</span>
                </span>
                <button class="source-link" onclick="showSourceModal('tmg_standard_contract_terms')">فحص العقد ↗</button>
              </div>
            </div>

            <!-- Card 3: Existing Owners - Maintenance Deficit -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(244, 63, 94, 0.15); color:var(--pbi-accent-rose);">C</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-buy3-title">الملاك الحاليون: مطالبات "فروق وديعة الصيانة" السنوية</strong>
                </div>
                <span class="pbi-pill-badge badge-rose">15k - 45k ج.م / سنة</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">ظاهرة المطالبات الإضافية:</strong>
                  يواجه سكان مدينتي والرحاب مطالبات سنوية متكررة بدفع "فروق صيانة" تتراوح في بعض المجموعات بين <strong style="color:var(--pbi-accent-rose);">15,000 و 45,000 جنيه مصري</strong> بحجة التضخم وتآكل عائد الوديعة الأصلية.
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-rose);">
                  <strong>التوصية القانونية للملاك:</strong> الامتناع عن السداد الجزافي والمطالبة عبر اتحاد الشاغلين بقوائم مالية وميزانيات تشغيلية مدققة ومعتمدة من مراقب حسابات مستقل توضح:
                  <ul style="padding-inline-start: 18px; margin-top: 4px;">
                    <li>أوجه الصرف والمصروفات الفعلية على الصيانة والنظافة والأمن.</li>
                    <li>عوائد الفوائد البنكية وأذون الخزانة المحققة على الوديعة التأسيسية للمشروع وتجنيبها لصالح الصيانة.</li>
                  </ul>
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                  <span>شكاوى ومذكرات اتحاد شاغلي مدينتي</span>
                </span>
                <button class="source-link" onclick="showSourceModal('madinaty_maintenance_audit')">ملف التدقيق ↗</button>
              </div>
            </div>

            <!-- Card 4: Resale Fees & Article 15 Law 181/2018 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(220, 38, 38, 0.15); color:var(--pbi-accent-rose);">D</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13.5px;" id="lbl-adv-buy4-title">رسوم التنازل العقاري وإعادة البيع (مخالفة القانون 181/2018)</strong>
                </div>
                <span class="advisory-law-badge">مخالفة المادة 15 صراحة</span>
              </div>
              <div class="advisory-body">
                <div>
                  <strong style="color:var(--pbi-text-hero);">فرض رسوم التنازل (5% إلى 10%):</strong>
                  تفرض إدارة المجموعة رسوماً تتراوح بين 5% و10% من قيمة العقار أو مبالغ مقطوعة لإصدار خطابات عدم الممانعة وتعديل بيانات المشتري في التنازلات بالأسواق الثانوية (Resale).
                </div>
                <div class="advisory-callout" style="border-inline-start-color: var(--pbi-accent-rose); background:rgba(244, 63, 94, 0.06);">
                  <strong style="color:var(--pbi-accent-rose);">النص القاطع للمادة 15 من قانون حماية المستهلك رقم 181 لسنة 2018:</strong>
                  <em>"يقع باطلاً كل شرط تعاقدي أو إجراء يفرضه المطور يوجب على المشتري دفع نسبة مئوية أو مقابل مالي عند إعادة بيع الوحدة أو التنازل عنها لأي طرف آخر."</em>
                  وقد أصدر جهاز حماية المستهلك ومحاكم الجنح الاقتصادية أحكاماً قاطعة ببطلان هذه الرسوم وإلزام المطورين بردها وتغريم المخالفين.
                </div>
                <div style="font-size:11.5px; color:var(--pbi-text-muted);">
                  <strong>تسعير إعادة البيع (Market Realities):</strong> عند اتخاذ قرار التخارج أو البيع، يجب الاعتماد على أسعار التنفيذ الفعلي في السوق الموازي والصفقات المنفذة (Cash-in-Hand)، بدلاً من أسعار الطرح الإعلانية للمطور الممتدة على 10-12 سنة تقسيط.
                </div>
              </div>
              <div class="advisory-evidence-bar">
                <span style="color:var(--pbi-text-dim); display:flex; align-items:center; gap:6px;">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                  <span>المادة 15 قانون 181/2018 (منشورات)</span>
                </span>
                <button class="source-link" onclick="showSourceModal('cpa_article15_resale')">السند القانوني الآمر ↗</button>
              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </div>

  <!-- ==========================================================================
       MODAL FOR SOURCE CITATIONS
       ========================================================================== -->
  <div id="source-modal">
    <div class="modal-box">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--pbi-border-subtle); padding-bottom:12px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:var(--pbi-accent-cyan);"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          <strong id="modal-source-title" style="font-size:14.5px; color:var(--pbi-text-hero);">Document Title</strong>
        </div>
        <button onclick="closeSourceModal()" style="background:none; border:none; color:var(--pbi-text-dim); cursor:pointer; font-size:16px;">✕</button>
      </div>

      <div style="font-size:12.5px; line-height:1.7; color:var(--pbi-text-main);" id="modal-source-desc">
        Document content goes here...
      </div>

      <div style="background:var(--pbi-surface-elevated); border:1px solid var(--pbi-border-subtle); border-radius:8px; padding:12px; font-size:11.5px; display:flex; flex-direction:column; gap:6px;">
        <div><strong>الناشر / الجهة المصدرة:</strong> <span id="modal-source-publisher" style="color:var(--pbi-accent-cyan);">Authority</span></div>
        <div><strong>التاريخ:</strong> <span id="modal-source-date" class="cell-mono">Date</span></div>
        <div style="margin-top:6px;">
          <a id="modal-source-url" href="#" target="_blank" rel="noopener noreferrer" class="btn-action highlight" style="display:inline-flex; font-size:12px;">زيارة الرابط الأصلي المباشر ↗</a>
        </div>
      </div>
    </div>
  </div>

  
  <!-- ==========================================================================
       POWER BI FOCUS MODE OVERLAY (FULLSCREEN VISUAL + DATA MATRIX)
       ========================================================================== -->
  <div id="pbi-focus-overlay">
    <div class="focus-top-bar">
      <div class="focus-title-group">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="pbi-pill-badge badge-cyan" id="focus-badge-tag">POWER BI FOCUS MODE</span>
          <h2 id="focus-modal-title">Visual Title</h2>
        </div>
        <p id="focus-modal-sub">Forensic dataset breakdown and tabular underlying matrix</p>
      </div>
      <div class="focus-tools">
        <button class="btn-action" onclick="exportFocusChartCSV()" id="btn-focus-export-csv" title="Download CSV Dataset">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          <span id="lbl-focus-export">تصدير البيانات (CSV)</span>
        </button>
        <button class="btn-action highlight" onclick="closeFocusMode()" style="padding:6px 16px; font-weight:800;">
          <span>✕ إغلاق العرض المكبر</span>
        </button>
      </div>
    </div>

    <div class="focus-content-grid">
      <div class="focus-chart-panel">
        <div style="position:relative; width:100%; height:100%; min-height:420px;" id="focus-canvas-wrap">
          <canvas id="focusModeChartCanvas"></canvas>
        </div>
      </div>
      <div class="focus-table-panel">
        <h4>
          <span id="lbl-focus-table-heading">مصفوفة البيانات التفصيلية (Underlying Data Matrix)</span>
          <span class="pbi-pill-badge badge-amber" id="focus-data-rows-count">0 Rows</span>
        </h4>
        <div class="table-container" style="max-height: 480px; overflow-y: auto;">
          <table class="pbi-table" id="focus-modal-table">
            <thead id="focus-modal-thead"></thead>
            <tbody id="focus-modal-tbody"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       PRESENTER MODE OVERLAY (CEO SLIDE DECK)
       ========================================================================== -->
  <div id="presenter-overlay">
    <div class="slide-progress">
      <div class="slide-progress-bar" id="slide-progress-bar"></div>
    </div>

    <div class="presenter-viewport">
      <div class="slide-canvas">
        <div class="slide-header">
          <div class="slide-number" id="presenter-slide-num">SLIDE 01 / 11</div>
          <h2 id="presenter-slide-title" style="font-size:18px; font-weight:800; color:var(--pbi-text-hero);">Slide Title</h2>
          <button onclick="closePresenterMode()" style="background:none; border:none; color:var(--pbi-text-dim); cursor:pointer; font-size:18px;">✕</button>
        </div>

        <div class="slide-body" id="presenter-slide-content">
          <!-- Slide Content -->
        </div>

        <div class="speaker-notes-banner">
          <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:var(--pbi-accent-amber); flex-shrink:0;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          <div>
            <strong id="lbl-speaker-note-tag">استنتاج الفحص الجنائي التنفيذي:</strong>
            <span id="presenter-speaker-note">Note...</span>
          </div>
        </div>
      </div>
    </div>

    <div class="presenter-dock">
      <button class="btn-action" onclick="prevSlide()" id="btn-prev-slide">❮ السابق</button>
      <div style="font-family:var(--pbi-font-mono); font-size:12px; color:var(--pbi-text-muted);" id="presenter-dock-indicator">1 / 11</div>
      <button class="btn-action highlight" onclick="nextSlide()" id="btn-next-slide">التالي ❯</button>
    </div>
  </div>

  <!-- ==========================================================================
       DATASETS & JAVASCRIPT ENGINE
       ========================================================================== -->
  <script>
    let currentLang = 'ar';
    let currentTab = 'overview';

    // Core Data Collections
    __REPLACE_SOURCES_DATA__

    __REPLACE_PROJECTS_DATA__

    __REPLACE_CONTRACTORS_DATA__

    __REPLACE_COMPLAINTS_DATA__

    __REPLACE_RISKS_DATA__

    __REPLACE_PRIVITY_TREE_DATA__

    __REPLACE_SLIDES_DATA__

    // Financial Table Rows
    const finRows = [
      { nameAr: "إجمالي الإيرادات المجمعة", nameEn: "Consolidated Revenue", fy21: "15,350", fy22: "19,870", fy23: "28,430", fy24: "42,700", fy25: "62,500", h126: "30,190", color: "var(--pbi-accent-cyan)", bold: true },
      { nameAr: "إيرادات النشاط العقاري السكني", nameEn: "Real Estate Deliveries", fy21: "10,210", fy22: "14,710", fy23: "21,630", fy24: "28,800", fy25: "36,700", h126: "17,000", color: "", bold: false },
      { nameAr: "إيرادات قطاع الفنادق والسياحة (دولارية)", nameEn: "Hospitality Revenue (USD-linked)", fy21: "1,270", fy22: "2,560", fy23: "3,550", fy24: "11,400", fy25: "14,900", h126: "7,500", color: "var(--pbi-accent-emerald)", bold: true },
      { nameAr: "مجمل الربح الإجمالي (Gross Profit)", nameEn: "Gross Profit", fy21: "5,180", fy22: "6,680", fy23: "9,600", fy24: "18,200", fy25: "24,800", h126: "12,100", color: "", bold: false },
      { nameAr: "صافي الأرباح المجمعة بعد الضرائب", nameEn: "Consolidated Net Profit", fy21: "1,780", fy22: "2,230", fy23: "3,310", fy24: "12,800", fy25: "18,200", h126: "9,950", color: "var(--pbi-accent-emerald)", bold: true },
      { nameAr: "صافي التدفق النقدي التشغيلي (NOCF)", nameEn: "Net Operating Cash Flow (CFO)", fy21: "2,100", fy22: "-1,800", fy23: "-3,400", fy24: "4,200", fy25: "6,100", h126: "3,110", color: "var(--pbi-accent-rose)", bold: true },
      { nameAr: "أوراق الدفع والدائنون التجاريون (المقاولون)", nameEn: "Notes Payable & Trade Creditors", fy21: "5,400", fy22: "6,800", fy23: "9,200", fy24: "12,400", fy25: ">15,790", h126: ">16,200", color: "var(--pbi-accent-rose)", bold: true },
      { nameAr: "التزامات عقود التأجير التمويلي (ديون هيكلية)", nameEn: "Financial Lease Notes Payable (Off-Bal)", fy21: "1,200", fy22: "2,100", fy23: "4,800", fy24: "22,100", fy25: "34,400", h126: "43,990", color: "var(--pbi-accent-purple)", bold: true },
      { nameAr: "دفعات العملاء المقدمة (التزامات تسليم)", nameEn: "Customer Advance Payments", fy21: "38,500", fy22: "48,200", fy23: "72,000", fy24: "95,000", fy25: "117,680", h126: "133,990", color: "", bold: false },
      { nameAr: "النقدية والأرصدة لدى البنوك واستثمارات سائلة", nameEn: "Cash & Liquid Financial Assets", fy21: "4,210", fy22: "4,780", fy23: "11,500", fy24: "32,000", fy25: "41,200", h126: "66,400", color: "var(--pbi-accent-emerald)", bold: true }
    ];

    // Slicer Filtering State
    let activeSlicers = {
      project: 'all',
      severity: 'all',
      year: 'all',
      entity: 'all'
    };

    function toggleSlicer(btn) {
      const slicerGroup = btn.getAttribute('data-slicer');
      const slicerVal = btn.getAttribute('data-val');
      
      const parent = btn.parentElement;
      parent.querySelectorAll('.slicer-pill').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      
      activeSlicers[slicerGroup] = slicerVal;
      applySlicers();
    }

    function resetAllSlicers() {
      activeSlicers = { project: 'all', severity: 'all', year: 'all', entity: 'all' };
      document.querySelectorAll('.slicer-pill').forEach(p => {
        if (p.getAttribute('data-val') === 'all') p.classList.add('active');
        else p.classList.remove('active');
      });
      applySlicers();
    }

    function applySlicers() {
      // Update label
      const activeKeys = Object.entries(activeSlicers).filter(([k,v]) => v !== 'all');
      const countEl = document.getElementById('slicer-filter-count');
      if (activeKeys.length === 0) {
        countEl.textContent = currentLang === 'ar' ? 'الفلاتر النشطة: كافة المشاريع (افتراضي)' : 'Active Filters: All Projects (Default)';
      } else {
        countEl.textContent = (currentLang === 'ar' ? 'فلاتر نشطة: ' : 'Active Filters: ') + activeKeys.map(([k,v]) => `${k}:${v}`).join(' | ');
      }

      // Filter Projects Table
      const filteredProjects = projectsData.filter(p => {
        if (activeSlicers.project === 'southmed' && !p.nameEn.toLowerCase().includes('southmed')) return false;
        if (activeSlicers.project === 'noor' && !p.nameEn.toLowerCase().includes('noor')) return false;
        if (activeSlicers.project === 'madinaty' && !p.nameEn.toLowerCase().includes('madinaty')) return false;
        if (activeSlicers.project === 'celia' && !p.nameEn.toLowerCase().includes('celia')) return false;
        if (activeSlicers.project === 'banan' && !p.nameEn.toLowerCase().includes('banan')) return false;
        return true;
      });
      renderProjectsTable(filteredProjects);

      // Filter Contractors Table
      const filteredContractors = contractorsData.filter(c => {
        if (activeSlicers.entity === 'acc' && !c.clientEn.toLowerCase().includes('alexandria')) return false;
        if (activeSlicers.entity === 'atrium' && !c.mainContractorEn.toLowerCase().includes('atrium')) return false;
        if (activeSlicers.project === 'southmed' && !c.projectEn.toLowerCase().includes('southmed')) return false;
        if (activeSlicers.project === 'noor' && !c.projectEn.toLowerCase().includes('noor')) return false;
        return true;
      });
      renderContractorsTable(filteredContractors);

      // Filter Risks Table
      const filteredRisks = risksData.filter(r => {
        if (activeSlicers.severity === 'critical' && r.sevBadge !== 'badge-high') return false;
        if (activeSlicers.severity === 'high' && r.sevBadge !== 'badge-high') return false;
        if (activeSlicers.severity === 'med' && r.sevBadge !== 'badge-med') return false;
        return true;
      });
      renderRisksTable(filteredRisks);
    }

    // Chart Controller & Instance Registry
    let chartInstances = {};

    
    // ==========================================================================
    // POWER BI NATIVE VISUAL ENGINE: DATA LABELS & WATERFALL CONNECTORS PLUGIN
    // ==========================================================================
    const pbiVisualPlugin = {
      id: 'pbiVisualPlugin',
      afterDatasetsDraw(chart, args, options) {
        const { ctx, data, chartArea } = chart;
        if (!chartArea) return;

        const isLight = document.documentElement.getAttribute('data-theme') === 'light';
        const labelTextColor = isLight ? '#1E293B' : '#F1F5F9';
        const fontName = currentLang === 'ar' ? 'Cairo, Plus Jakarta Sans, sans-serif' : 'Plus Jakarta Sans, sans-serif';

        // 1. Dotted Waterfall Connectors for Waterfall Charts
        if (chart.canvas.id === 'chartWaterfallCashFlow' && chart.getDatasetMeta(0).data) {
          const meta = chart.getDatasetMeta(0);
          ctx.save();
          ctx.setLineDash([3, 3]);
          ctx.strokeStyle = isLight ? '#94A3B8' : '#64748B';
          ctx.lineWidth = 1;

          for (let i = 0; i < meta.data.length - 1; i++) {
            const currEl = meta.data[i];
            const nextEl = meta.data[i + 1];
            if (currEl && nextEl) {
              const yVal = currEl.base !== undefined ? currEl.y : currEl.y;
              ctx.beginPath();
              ctx.moveTo(currEl.x + (currEl.width / 2), currEl.y);
              ctx.lineTo(nextEl.x - (nextEl.width / 2), currEl.y);
              ctx.stroke();
            }
          }
          ctx.restore();
        }

        // 2. Power BI Crisp Value Data Labels on Bar & Column Visuals
        if (['bar'].includes(chart.config.type) && chart.canvas.id !== 'landbankBarChart') {
          ctx.save();
          ctx.font = `bold 10px ${fontName}`;
          ctx.fillStyle = labelTextColor;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'bottom';

          chart.data.datasets.forEach((dataset, dIdx) => {
            const meta = chart.getDatasetMeta(dIdx);
            if (meta.hidden) return;

            meta.data.forEach((element, index) => {
              const rawVal = dataset.data[index];
              if (rawVal === null || rawVal === undefined) return;

              let displayTxt = '';
              if (Array.isArray(rawVal)) {
                // Floating bar (waterfall): show delta
                const delta = rawVal[1] - rawVal[0];
                displayTxt = (delta >= 0 ? '+' : '') + delta.toLocaleString();
              } else if (typeof rawVal === 'number') {
                if (Math.abs(rawVal) >= 1000) {
                  displayTxt = (rawVal / 1000).toFixed(1) + 'k';
                } else {
                  displayTxt = rawVal.toLocaleString();
                }
              }

              if (displayTxt && element.x !== undefined && element.y !== undefined) {
                const yPos = element.y < element.base ? element.y - 4 : element.y + 12;
                ctx.fillText(displayTxt, element.x, yPos);
              }
            });
          });
          ctx.restore();
        }
      }
    };

    // Register Chart.js Visual Plugin
    if (typeof Chart !== 'undefined' && Chart.register) {
      Chart.register(pbiVisualPlugin);
    }

    // ==========================================================================
    // POWER BI FOCUS MODE ENGINE ("SHOW AS TABLE" & CSV EXPORT)
    // ==========================================================================
    let focusChartInstance = null;
    let activeFocusChartId = null;

    function openFocusMode(chartId, title) {
      const srcCanvas = document.getElementById(chartId);
      if (!srcCanvas) return;

      const overlay = document.getElementById('pbi-focus-overlay');
      const focusTitle = document.getElementById('focus-modal-title');
      const focusSub = document.getElementById('focus-modal-sub');
      const thead = document.getElementById('focus-modal-thead');
      const tbody = document.getElementById('focus-modal-tbody');
      const countTag = document.getElementById('focus-data-rows-count');

      activeFocusChartId = chartId;
      focusTitle.textContent = title || chartId;
      focusSub.textContent = currentLang === 'ar' 
        ? 'عرض التحليل الموسّع بنمط Power BI مع تفكيك مصفوفة البيانات الأساسية'
        : 'Expanded Power BI visual view with underlying structured forensic matrix';

      // Find chart instance in chartInstances
      let targetInstance = null;
      for (const k in chartInstances) {
        if (chartInstances[k] && chartInstances[k].canvas && chartInstances[k].canvas.id === chartId) {
          targetInstance = chartInstances[k];
          break;
        }
      }

      // Populate Table
      if (targetInstance && targetInstance.data) {
        const labels = targetInstance.data.labels || [];
        const datasets = targetInstance.data.datasets || [];

        // Build Table Header
        let thHtml = `<tr><th>${currentLang === 'ar' ? 'البند / التصنيف' : 'Category / Dimension'}</th>`;
        datasets.forEach(ds => {
          thHtml += `<th>${ds.label || 'Value'}</th>`;
        });
        thHtml += `</tr>`;
        thead.innerHTML = thHtml;

        // Build Table Body
        let tbHtml = '';
        labels.forEach((lbl, i) => {
          tbHtml += `<tr><td><strong>${lbl}</strong></td>`;
          datasets.forEach(ds => {
            const v = ds.data[i];
            let cellStr = v;
            if (Array.isArray(v)) {
              cellStr = `[${v[0]} → ${v[1]}] (Δ ${v[1] - v[0]})`;
            } else if (typeof v === 'number') {
              cellStr = v.toLocaleString();
            }
            tbHtml += `<td class="cell-mono" style="color:var(--pbi-accent-cyan); font-weight:700;">${cellStr !== undefined ? cellStr : '-'}</td>`;
          });
          tbHtml += `</tr>`;
        });
        tbody.innerHTML = tbHtml;
        countTag.textContent = `${labels.length} ${currentLang === 'ar' ? 'سجلات' : 'Rows'}`;

        // Recreate Focus Canvas Chart
        const focusCanvas = document.getElementById('focusModeChartCanvas');
        if (focusChartInstance) focusChartInstance.destroy();

        const ctx = focusCanvas.getContext('2d');
        const configClone = JSON.parse(JSON.stringify({
          type: targetInstance.config.type,
          data: targetInstance.config.data,
          options: targetInstance.config.options
        }));
        configClone.options.responsive = true;
        configClone.options.maintainAspectRatio = false;

        focusChartInstance = new Chart(ctx, configClone);
      }

      overlay.classList.add('active');
    }

    function closeFocusMode() {
      const overlay = document.getElementById('pbi-focus-overlay');
      overlay.classList.remove('active');
      if (focusChartInstance) {
        focusChartInstance.destroy();
        focusChartInstance = null;
      }
      activeFocusChartId = null;
    }

    function exportFocusChartCSV() {
      if (activeFocusChartId) {
        exportChartDataCSV(activeFocusChartId);
      }
    }

    function exportChartDataCSV(chartId) {
      let targetInstance = null;
      for (const k in chartInstances) {
        if (chartInstances[k] && chartInstances[k].canvas && chartInstances[k].canvas.id === chartId) {
          targetInstance = chartInstances[k];
          break;
        }
      }
      if (!targetInstance) return;

      const labels = targetInstance.data.labels || [];
      const datasets = targetInstance.data.datasets || [];

      let csv = 'Category,' + datasets.map(d => `"${d.label || 'Value'}"`).join(',') + '\n';
      labels.forEach((lbl, i) => {
        let row = `"${lbl}",`;
        row += datasets.map(ds => {
          const v = ds.data[i];
          if (Array.isArray(v)) return `"${v[1] - v[0]}"`;
          return `"${v !== undefined ? v : ''}"`;
        }).join(',');
        csv += row + '\n';
      });

      const blob = new Blob(["\ufeff" + csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `TMG_Forensic_${chartId}_Data.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    function initAll14Charts() {
      // Destroy existing
      Object.keys(chartInstances).forEach(k => {
        if (chartInstances[k]) chartInstances[k].destroy();
      });

      const isLight = document.documentElement.getAttribute('data-theme') === 'light';
      const fontFam = currentLang === 'ar' ? 'Cairo, Plus Jakarta Sans, sans-serif' : 'Plus Jakarta Sans, Cairo, sans-serif';
      const textColor = isLight ? '#0F172A' : '#F8FAFC';
      const textMuted = isLight ? '#475569' : '#94A3B8';
      const gridColor = isLight ? 'rgba(0, 0, 0, 0.08)' : 'rgba(51, 65, 85, 0.35)';

      // 1. Cash Conversion Waterfall
      const ctxWf = document.getElementById('chartWaterfallCashFlow');
      if (ctxWf) {
        chartInstances.wf = new Chart(ctxWf.getContext('2d'), {
          type: 'bar',
          data: {
            labels: currentLang === 'ar' ? 
              ['صافي أرباح H1', 'استنزاف الإنشاءات (WIP)', 'متحصلات العملاء', 'سداد تأجير وتمويل', 'فوائد وضرائب', 'التدفق التشغيلي (CFO)'] :
              ['H1 Net Profit', 'WIP Inventory Drain', 'Customer Inflows', 'Lease & Debt Outflow', 'Tax & Finance Cost', 'Ending CFO Cash'],
            datasets: [{
              label: 'EGP Millions',
              data: [
                [0, 9950],
                [9950, -8310],
                [-8310, 15800],
                [15800, 7100],
                [7100, 3110],
                [0, 3110]
              ],
              backgroundColor: ['#10B981', '#F43F5E', '#00E5FF', '#F43F5E', '#F59E0B', '#3B82F6'],
              borderRadius: 4
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                callbacks: {
                  label: ctx => {
                    const raw = ctx.raw;
                    const delta = raw[1] - raw[0];
                    return ` ${delta > 0 ? '+' : ''}${delta.toLocaleString()}M EGP (الرصيد: ${raw[1].toLocaleString()}M)`;
                  }
                }
              }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam, size: 10 } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, callback: v => v + 'M' } }
            }
          }
        });
      }

      // 2. Revenue & Backlog Combo (Bar + Line)
      const ctxCombo = document.getElementById('chartRevenueBacklogCombo');
      if (ctxCombo) {
        chartInstances.combo = new Chart(ctxCombo.getContext('2d'), {
          data: {
            labels: ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026'],
            datasets: [
              {
                type: 'bar',
                label: currentLang === 'ar' ? 'إيرادات التسليم السكني' : 'Residential Sales (EGP bn)',
                data: [10.21, 14.71, 21.63, 28.80, 36.70, 17.00],
                backgroundColor: '#00E5FF',
                borderRadius: 4,
                yAxisID: 'y'
              },
              {
                type: 'bar',
                label: currentLang === 'ar' ? 'إيرادات الفنادق والسياحة (دولارية)' : 'Hospitality Revenue (EGP bn)',
                data: [1.27, 2.56, 3.55, 11.40, 14.90, 7.50],
                backgroundColor: '#3B82F6',
                borderRadius: 4,
                yAxisID: 'y'
              },
              {
                type: 'line',
                label: currentLang === 'ar' ? 'المبيعات التعاقدية غير المسلمة (Backlog)' : 'Unearned Backlog (EGP bn)',
                data: [63.0, 77.0, 145.0, 294.0, 441.2, 460.0],
                borderColor: '#F59E0B',
                backgroundColor: 'rgba(245, 158, 11, 0.15)',
                borderWidth: 2.5,
                fill: true,
                tension: 0.3,
                yAxisID: 'y1'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top', labels: { color: textColor, font: { family: fontFam, size: 10.5, weight: '700' } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { 
                type: 'linear', position: 'left', grid: { color: gridColor }, 
                ticks: { color: textMuted, callback: v => v + 'B' },
                title: { display: true, text: 'الإيرادات السنوية', color: textMuted }
              },
              y1: { 
                type: 'linear', position: 'right', grid: { drawOnChartArea: false }, 
                ticks: { color: '#F59E0B', callback: v => v + 'B' },
                title: { display: true, text: 'رصيد المبيعات', color: '#F59E0B' }
              }
            }
          }
        });
      }

      // 3. 6-Axis Forensic Risk Radar
      const ctxRadar = document.getElementById('chartForensicRiskRadar');
      if (ctxRadar) {
        chartInstances.radar = new Chart(ctxRadar.getContext('2d'), {
          type: 'radar',
          data: {
            labels: currentLang === 'ar' ? [
              'تأخير صرف المستخلصات (PDC)', 'درع العزل القانوني (ACC)', 'عائق التحكيم السري CRCICA',
              'تضخم التكاليف وفصل التوريد', 'احتجاز مبالغ الضمان (5-10%)', 'الاحتكاك العمالي والورديات'
            ] : [
              'Payment Deferral (PDC)', 'Privity Insulation (ACC)', 'CRCICA Arbitration Barrier',
              'Cost Inflation & Decoupling', 'Retention Withholding Lag', 'Labor Shift & Friction'
            ],
            datasets: [
              {
                label: currentLang === 'ar' ? 'التقييم الجنائي المرصود (1-10)' : 'Forensic Score (1-10)',
                data: [8.5, 9.5, 8.8, 8.2, 7.8, 7.0],
                backgroundColor: 'rgba(244, 63, 94, 0.25)',
                borderColor: '#F43F5E',
                pointBackgroundColor: '#F43F5E',
                borderWidth: 2
              },
              {
                label: currentLang === 'ar' ? 'السقف الآمن المعياري' : 'Safe Benchmark',
                data: [4.0, 4.0, 4.0, 4.0, 4.0, 4.0],
                borderColor: '#00E5FF',
                borderDash: [4, 4],
                fill: false,
                borderWidth: 1.5,
                pointRadius: 0
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              r: {
                angleLines: { color: gridColor },
                grid: { color: gridColor },
                pointLabels: { color: textColor, font: { family: fontFam, size: 9.5, weight: '700' } },
                ticks: { display: false, min: 0, max: 10 }
              }
            },
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 10, font: { family: fontFam, size: 10 } } }
            }
          }
        });
      }

      // 4. Debt Structure Doughnut
      const ctxDebt = document.getElementById('chartDebtStructureTreemapDoughnut');
      if (ctxDebt) {
        chartInstances.debt = new Chart(ctxDebt.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: currentLang === 'ar' ? [
              'عقود تأجير تمويلي خارج الميزانية (43.99B @ 28.6%)',
              'قروض وتسهيلات بنكية مباشرة (16.20B)',
              'أوراق دفع تجارية ودائنون (>15.79B PDC)'
            ] : [
              'Off-Balance Financial Leases (43.99B @ 28.6%)',
              'Direct Bank Facilities (16.20B)',
              'Operating Notes Payable (>15.79B PDC)'
            ],
            datasets: [{
              data: [43.99, 16.20, 15.79],
              backgroundColor: ['#A855F7', '#3B82F6', '#F59E0B'],
              borderColor: '#111726',
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '66%',
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 10, font: { family: fontFam, size: 9.5 } } }
            }
          }
        });
      }

      // 5. Ownership & UBO Doughnut
      const ctxUbo = document.getElementById('chartOwnershipUBODoughnut');
      if (ctxUbo) {
        chartInstances.ubo = new Chart(ctxUbo.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: currentLang === 'ar' ? [
              'عائلة طلعت مصطفى (59.8%)', 'التداول الحر بالبورصة (32.9%)',
              'صندوق الثروة النرويجي Norges (3.3%)', 'مؤسسات وصناديق أخرى (4.0%)'
            ] : [
              'Talaat Moustafa Family (59.8%)', 'EGX Free Float (32.9%)',
              'Norges Bank Sovereign (3.3%)', 'Strategic Institutions (4.0%)'
            ],
            datasets: [{
              data: [59.8, 32.9, 3.3, 4.0],
              backgroundColor: ['#00E5FF', '#3B82F6', '#10B981', '#A855F7'],
              borderColor: '#111726',
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '66%',
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 10, font: { family: fontFam, size: 9.5 } } }
            }
          }
        });
      }

      // 6. IPC Mustakhlasat S-Curve
      const ctxIpc = document.getElementById('chartIPCMustakhlasatSCurve');
      if (ctxIpc) {
        chartInstances.ipc = new Chart(ctxIpc.getContext('2d'), {
          type: 'line',
          data: {
            labels: currentLang === 'ar' ? [
              'تقديم المستخلص', 'الحصر بالموقع', 'المكتب الفني ACC', 'مراجعة مدينتي', 'الاعتماد المالي', 'إصدار الشيك الآجل', 'التحصيل والمقاصة'
            ] : [
              'Submittal', 'Site Survey', 'ACC Tech Office', 'HQ Audit', 'Approval', 'PDC Issuance', 'Cash Liquidity'
            ],
            datasets: [
              {
                label: currentLang === 'ar' ? 'الجدول التعاقدي المعياري (90 يوماً)' : 'Standard Contract (90d)',
                data: [0, 15, 30, 45, 60, 75, 90],
                borderColor: '#10B981',
                borderDash: [5, 5],
                fill: false,
                borderWidth: 2
              },
              {
                label: currentLang === 'ar' ? 'المسار الزمني الفعلي المرصود (270 يوماً)' : 'Observed Timeline (270d)',
                data: [0, 25, 60, 105, 135, 180, 270],
                borderColor: '#F43F5E',
                backgroundColor: 'rgba(244, 63, 94, 0.12)',
                fill: true,
                borderWidth: 2.5,
                tension: 0.3
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top', labels: { color: textColor, font: { family: fontFam, size: 10.5, weight: '700' } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam, size: 10 } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, callback: v => v + 'd' } }
            }
          }
        });
      }

      // 7. Contractor Dispute Friction Bubble Chart
      const ctxBubble = document.getElementById('chartContractorDisputeBubble');
      if (ctxBubble) {
        chartInstances.bubble = new Chart(ctxBubble.getContext('2d'), {
          type: 'bubble',
          data: {
            datasets: [
              {
                label: currentLang === 'ar' ? 'كونكريت بلس (ساوث ميد ~10B)' : 'Concrete Plus (~10B)',
                data: [{ x: 10.0, y: 2.0, r: 22 }],
                backgroundColor: 'rgba(0, 229, 255, 0.75)'
              },
              {
                label: currentLang === 'ar' ? 'أتريوم للمقاولات (AQC ~18B)' : 'Atrium Turnkey (~18B)',
                data: [{ x: 18.0, y: 1.5, r: 26 }],
                backgroundColor: 'rgba(59, 130, 246, 0.75)'
              },
              {
                label: currentLang === 'ar' ? 'عمال ومقاولو باطن الإسكندرية (ACC)' : 'ACC Labor & Subs',
                data: [{ x: 4.5, y: 8.5, r: 18 }],
                backgroundColor: 'rgba(244, 63, 94, 0.85)'
              },
              {
                label: currentLang === 'ar' ? 'حسن علام (بحيرات مدينتي)' : 'Hassan Allam Utilities',
                data: [{ x: 4.5, y: 1.2, r: 14 }],
                backgroundColor: 'rgba(16, 185, 129, 0.75)'
              },
              {
                label: currentLang === 'ar' ? 'P.Zone (البحيرات والنوافير)' : 'P.Zone International',
                data: [{ x: 2.5, y: 1.0, r: 12 }],
                backgroundColor: 'rgba(0, 229, 255, 0.85)'
              },
              {
                label: currentLang === 'ar' ? 'ماتيتو أوفرسيز (محطات المعالجة TSE)' : 'Metito Overseas (WWTP & TSE)',
                data: [{ x: 3.2, y: 1.1, r: 15 }],
                backgroundColor: 'rgba(16, 185, 129, 0.85)'
              },
              {
                label: currentLang === 'ar' ? 'خالد هنداوي (سقالات مدينتي - دعوى 2923/2012)' : 'Khaled Hendawi (Scaffolding 609K)',
                data: [{ x: 0.61, y: 7.8, r: 13 }],
                backgroundColor: 'rgba(239, 68, 68, 0.85)'
              },
              {
                label: currentLang === 'ar' ? 'شحاتة حسن (مدينتي 2008 - حجز المستخلصات)' : 'Shehata Hassan (2008 Dues Withheld)',
                data: [{ x: 0.85, y: 8.8, r: 15 }],
                backgroundColor: 'rgba(225, 29, 72, 0.85)'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 10, font: { family: fontFam, size: 9.5 } } }
            },
            scales: {
              x: { title: { display: true, text: 'حجم التعاقد المقدر (مليار جنيه)', color: textMuted }, grid: { color: gridColor }, ticks: { color: textMuted } },
              y: { title: { display: true, text: 'مؤشر التوتر والنزاع (1-10)', color: textMuted }, min: 0, max: 10, grid: { color: gridColor }, ticks: { color: textMuted } }
            }
          }
        });
      }

      // 8. Subcontractor Vulnerability Gauge (Doughnut as Half-Gauge)
      const ctxGauge = document.getElementById('chartVulnerabilityGauge');
      if (ctxGauge) {
        chartInstances.gauge = new Chart(ctxGauge.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: ['مستوى الخطورة المرصود (8.8/10)', 'النطاق الآمن المتبقي'],
            datasets: [{
              data: [88, 12],
              backgroundColor: ['#F43F5E', 'rgba(255, 255, 255, 0.05)'],
              borderWidth: 0,
              circumference: 180,
              rotation: 270
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '78%',
            plugins: {
              legend: { display: false },
              tooltip: { enabled: false }
            }
          }
        });
      }

      // 9. FX & Material Inflation Escalation Tornado Chart
      const ctxTornado = document.getElementById('chartInflationTornado');
      if (ctxTornado) {
        chartInstances.tornado = new Chart(ctxTornado.getContext('2d'), {
          type: 'bar',
          data: {
            labels: currentLang === 'ar' ? [
              'مضخات وفلاتر البحيرات (MEP المستورد)', 'أنظمة النوافير والتحكم (Ghesa/acis)',
              'عزل البولي إيثيلين والأغشية (HDPE)', 'الخرسانة وحديد التسليح المدني', 'العمالة وسكن المواقع الساحلية'
            ] : [
              'Imported Lagoon Pumps & Filters', 'Dancing Fountain Control Systems',
              'HDPE Geo-membrane Liners', 'Civil Structural Concrete & Rebar', 'Site Labor & Coastal Lodging'
            ],
            datasets: [
              {
                label: currentLang === 'ar' ? 'حساسية صدمة العملة (FX Exposure %)' : 'FX Exposure (%)',
                data: [70, 75, 65, 45, 15],
                backgroundColor: '#F43F5E',
                borderRadius: 4
              },
              {
                label: currentLang === 'ar' ? 'التضخم التراكمي المقدر (Inflation %)' : 'Cumulative Inflation (%)',
                data: [55, 60, 50, 65, 40],
                backgroundColor: '#F59E0B',
                borderRadius: 4
              }
            ]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top', labels: { color: textColor, font: { family: fontFam, size: 10 } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, callback: v => v + '%' } },
              y: { grid: { display: false }, ticks: { color: textColor, font: { family: fontFam, size: 9.5 } } }
            }
          }
        });
      }

      // 10. Landbank Bar Chart
      const ctxLand = document.getElementById('landbankBarChart');
      if (ctxLand) {
        chartInstances.land = new Chart(ctxLand.getContext('2d'), {
          type: 'bar',
          data: {
            labels: currentLang === 'ar' ? 
              ['مدينتي', 'ساوث ميد', 'مدينة نور', 'بنان (الرياض)', 'الرحاب', 'ذا سباين', 'سيليا'] :
              ['Madinaty', 'SouthMed', 'Noor City', 'Banan (Riyadh)', 'Al Rehab', 'The Spine', 'Celia'],
            datasets: [{
              label: currentLang === 'ar' ? 'المساحة (فدان)' : 'Area (Feddans)',
              data: [8000, 5542, 5000, 2380, 2360, 1000, 500],
              backgroundColor: ['#00E5FF', '#3B82F6', '#10B981', '#A855F7', '#00E5FF', '#F59E0B', '#F43F5E'],
              borderRadius: 4
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
              x: { grid: { display: false }, ticks: { color: textColor, font: { family: fontFam, size: 9.5 } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, callback: v => v.toLocaleString() } }
            }
          }
        });
      }

      // 11. Evidence Hierarchy Polar Area
      const ctxPolar = document.getElementById('chartEvidenceHierarchyPolar');
      if (ctxPolar) {
        chartInstances.polar = new Chart(ctxPolar.getContext('2d'), {
          type: 'polarArea',
          data: {
            labels: currentLang === 'ar' ? [
              'مستوى أ: أحكام وإفصاحات رسمية (35%)', 'مستوى ب: سوابق هندسية موثقة (45%)',
              'مستوى جـ: بيانات وتسويق المطور (15%)', 'مستوى د: بلاغات وتوترات مواقع (5%)'
            ] : [
              'Level A: Official / Court (35%)', 'Level B: Verified Portfolios (45%)',
              'Level C: Marketing Claims (15%)', 'Level D: Site Friction Leads (5%)'
            ],
            datasets: [{
              data: [35, 45, 15, 5],
              backgroundColor: ['rgba(0, 229, 255, 0.75)', 'rgba(59, 130, 246, 0.75)', 'rgba(245, 158, 11, 0.75)', 'rgba(244, 63, 94, 0.75)'],
              borderColor: '#111726'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: { r: { grid: { color: gridColor }, ticks: { display: false } } },
            plugins: { legend: { position: 'bottom', labels: { color: textColor, boxWidth: 10, font: { family: fontFam, size: 9.5 } } } }
          }
        });
      }

      // 12. P.Zone Lagoon Scope Capex vs O&M
      const ctxLagoon = document.getElementById('chartLagoonMEPCapexOpex');
      if (ctxLagoon) {
        chartInstances.lagoon = new Chart(ctxLagoon.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: currentLang === 'ar' ? [
              'تنفيذ كهروميكانيكي وبحيرات (Capex 75%)', 'تشغيل وصيانة مستدامة (O&M 25%)'
            ] : [
              'MEP & Turnkey Execution (Capex 75%)', 'Recurring Maintenance (O&M 25%)'
            ],
            datasets: [{
              data: [75, 25],
              backgroundColor: ['#00E5FF', '#10B981'],
              borderColor: '#111726',
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '66%',
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 10, font: { family: fontFam, size: 9.5 } } }
            }
          }
        });
      }

      // 13. Complaints Breakdown
      const ctxComp = document.getElementById('chartComplaints');
      if (ctxComp) {
        chartInstances.comp = new Chart(ctxComp.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: currentLang === 'ar' ? [
              'فروق الصيانة وعائد الوديعة (35%)', 'رسوم التنازل العقاري 5-10% (24%)',
              'مستحقات مقاولين واحتجاجات (20%)', 'تأخير التسليم وفروق الأسعار (14%)', 'تعريفة المرافق وضغط المياه (7%)'
            ] : [
              'Maintenance Deficits (35%)', 'Resale Fees (24%)',
              'Contractor Dues & Labor (20%)', 'Delivery Slippage (14%)', 'Utility Tariffs (7%)'
            ],
            datasets: [{
              data: [35, 24, 20, 14, 7],
              backgroundColor: ['#F43F5E', '#F59E0B', '#00E5FF', '#A855F7', '#64748B'],
              borderWidth: 0
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '60%',
            plugins: {
              legend: { position: 'bottom', labels: { color: textColor, boxWidth: 10, font: { family: fontFam, size: 9.5 } } }
            }
          }
        });
      }

      // 14. Project Slippage Timeline Bar Chart
      const ctxSlip = document.getElementById('chartProjectDeliveryTimeline');
      if (ctxSlip) {
        chartInstances.slip = new Chart(ctxSlip.getContext('2d'), {
          type: 'bar',
          data: {
            labels: currentLang === 'ar' ? [
              'فورسيزونز الأقصر (EGOTH)', 'فورسيزونز مدينتي', 'راديسون مرسى علم',
              'فورسيزونز الأهرامات (GEM)', 'سيليا المراحل الثانوية', 'مدينة نور المرحلة 1', 'ساوث ميد المرحلة 1'
            ] : [
              'FS Luxor (EGOTH)', 'FS Madinaty', 'Radisson Marsa Alam',
              'FS Pyramids (GEM)', 'Celia Secondary', 'Noor City Phase 1', 'SouthMed Phase 1'
            ],
            datasets: [{
              label: currentLang === 'ar' ? 'فترة التعديل / التأخير الإضافي (أشهر)' : 'Delivery Shift (Months)',
              data: [24, 12, 24, 12, 18, 0, 0],
              backgroundColor: ['#F43F5E', '#F59E0B', '#F43F5E', '#F59E0B', '#F43F5E', '#10B981', '#00E5FF'],
              borderRadius: 4
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
              x: { grid: { display: false }, ticks: { color: textColor, font: { family: fontFam, size: 9 } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, callback: v => v + 'm' } }
            }
          }
        });
      }

      
      // 15. Evidence Hierarchy & Contractor Sentiment Breakdown (Polar Area)
      const ctxEvSent = document.getElementById('chartEvidenceSentiment');
      if (ctxEvSent) {
        chartInstances.evSent = new Chart(ctxEvSent.getContext('2d'), {
          type: 'polarArea',
          data: {
            labels: currentLang === 'ar' ? [
              'علاقات تعاقدية وتكرار أعمال (Level A)',
              'إفصاحات توريد وشراكة معلنة (Level B)',
              'احتجاجات أجور وظروف عمل داخلية (Level A/B)',
              'ادعاءات سلاسل إمداد عليا جهات حكومية (Level D)',
              'شكاوى مستحقات تاريخية مباشرة (Level A/B)',
              'معايير ونزاعات قطاع المقاولات العام (Level C)'
            ] : [
              'Documented Commercial Repeat (Level A)',
              'Public Supplier Statement (Level B)',
              'Internal Labor Wage Actions (Level A/B)',
              'Upstream Payer Claims - Armed Forces (Level D)',
              'Direct Historic Contractor Dues (Level A/B)',
              'General Industry Claims Benchmark (Level C)'
            ],
            datasets: [{
              data: [8, 6, 4, 2, 2, 2],
              backgroundColor: [
                'rgba(16, 185, 129, 0.75)',
                'rgba(2, 132, 199, 0.75)',
                'rgba(245, 158, 11, 0.75)',
                'rgba(168, 85, 247, 0.75)',
                'rgba(225, 29, 72, 0.75)',
                'rgba(100, 116, 139, 0.75)'
              ],
              borderWidth: 1,
              borderColor: isLight ? '#FFFFFF' : '#111726'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'right',
                labels: { color: textColor, font: { family: fontFam, size: 9.5 }, boxWidth: 12 }
              },
              tooltip: {
                callbacks: {
                  label: ctx => ` ${ctx.label}: ${ctx.raw} حالات توثيق`
                }
              }
            },
            scales: {
              r: {
                grid: { color: gridColor },
                ticks: { display: false }
              }
            }
          }
        });
      }

      // Re-render Tab 3 Line Chart if visible
      const elIPC = document.getElementById('ipcLifecycleLineChart');
      if (elIPC && !chartInstances.ipcTab3) {
        chartInstances.ipcTab3 = new Chart(elIPC.getContext('2d'), {
          type: 'line',
          data: {
            labels: currentLang === 'ar' ? [
              'تقديم المستخلص', 'حصر الكميات بالموقع', 'المكتب الفني ACC', 'مراجعة مدينتي', 'اعتماد المستخلص', 'إصدار الشيكات الآجلة (PDC)', 'التحصيل والمقاصة'
            ] : [
              'Submission', 'Site Survey', 'ACC Tech Office', 'HQ Audit', 'Certified', 'PDC Issued', 'Cash Clearance'
            ],
            datasets: [
              {
                label: currentLang === 'ar' ? 'الجدول التعاقدي (90 يوماً)' : 'Contractual (90d)',
                data: [0, 15, 30, 45, 60, 75, 90],
                borderColor: '#10B981',
                borderDash: [5, 5],
                fill: false
              },
              {
                label: currentLang === 'ar' ? 'الجدول الفعلي المرصود (270 يوماً)' : 'Observed Route (270d)',
                data: [0, 25, 60, 105, 135, 180, 270],
                borderColor: '#F43F5E',
                backgroundColor: 'rgba(244, 63, 94, 0.1)',
                fill: true
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, callback: v => v + 'd' } }
            }
          }
        });
      }
    }

    // Tab Switching
    function switchTab(tabId) {
      currentTab = tabId;
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      const activePane = document.getElementById(`tab-${tabId}`);
      if (activePane) activePane.classList.add('active');

      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.querySelector(`.nav-btn[onclick="switchTab('${tabId}')"]`);
      if (activeBtn) activeBtn.classList.add('active');

      const tabNames = {
        overview: currentLang === 'ar' ? 'لوحة القيادة التنفيذية (Overview)' : 'Executive Overview',
        procurement: currentLang === 'ar' ? 'المشتريات المدمجة والدرع القانوني' : 'Captive Procurement & Privity',
        mustakhlasat: currentLang === 'ar' ? 'المستخلصات وعقبة الصرف' : 'Payment Bottlenecks (270d)',
        projects: currentLang === 'ar' ? 'محفظة المشاريع والأراضي' : 'Project Portfolio & Landbank',
        contractors: currentLang === 'ar' ? 'سجل المقاولين وسلاسل الإمداد' : 'Contractors & Supply Chains',
        disputes: currentLang === 'ar' ? 'الأحكام القضائية وسجلات التحكيم' : 'Judicial Rulings & Disputes',
        financials: currentLang === 'ar' ? 'التحليل المالي الجنائي والسيولة' : 'Forensic Financials & Debt',
        sentiment: currentLang === 'ar' ? 'شكاوى المقاولين والعمال والملاك' : 'Stakeholder Complaints',
        risks: currentLang === 'ar' ? 'مصفوفة المخاطر ودليل التحوط' : 'Forensic Risk Matrix',
        advisory: currentLang === 'ar' ? 'توجيهات المستثمرين والملاك (Advisory)' : 'Investor & Buyer Advisory'
      };
      document.getElementById('current-tab-name').textContent = tabNames[tabId] || tabId;

      if (tabId === 'procurement') {
        setTimeout(renderD3PrivityTree, 50);
      }
    }

    // Tables Rendering
    function renderProjectsTable(data) {
      const tbody = document.getElementById('projects-tbody');
      tbody.innerHTML = data.map(p => `
        <tr>
          <td><strong style="color:var(--pbi-text-hero);">${currentLang === 'ar' ? p.nameAr : p.nameEn}</strong></td>
          <td>${currentLang === 'ar' ? p.locAr : p.locEn}</td>
          <td><span class="cell-mono" style="color:var(--pbi-accent-cyan); font-weight:700;">${p.spv}</span></td>
          <td>${currentLang === 'ar' ? p.landAr : p.landEn}</td>
          <td><span class="badge ${p.riskBadge}">${currentLang === 'ar' ? p.statusAr : p.statusEn}</span></td>
          <td style="max-width:280px; font-size:11.5px;">${currentLang === 'ar' ? p.compAr : p.compEn}</td>
          <td><span class="badge ${p.riskBadge}">${currentLang === 'ar' ? p.riskAr : p.riskEn}</span></td>
          <td><button class="source-link" onclick="showSourceModal('${p.sourceKey}')">${currentLang === 'ar' ? 'التدقيق ↗' : 'Verify ↗'}</button></td>
        </tr>
      `).join('');
    }

    function renderContractorsTable(data) {
      const tbody = document.getElementById('contractors-tbody');
      tbody.innerHTML = data.map(c => `
        <tr>
          <td><strong style="color:var(--pbi-text-hero);">${currentLang === 'ar' ? c.projectAr : c.projectEn}</strong></td>
          <td class="cell-mono" style="color:var(--pbi-accent-amber);">${currentLang === 'ar' ? c.clientAr : c.clientEn}</td>
          <td><strong style="color:var(--pbi-accent-cyan);">${currentLang === 'ar' ? c.mainContractorAr : c.mainContractorEn}</strong></td>
          <td>${currentLang === 'ar' ? c.subcontractorAr : c.subcontractorEn}</td>
          <td style="max-width:260px; font-size:11.5px;">${currentLang === 'ar' ? c.scopeAr : c.scopeEn}</td>
          <td class="cell-mono" style="font-size:11px;">${currentLang === 'ar' ? c.docAr : c.docEn}</td>
          <td style="max-width:240px; font-size:11.5px; color:var(--pbi-text-muted);">${currentLang === 'ar' ? c.noteAr : c.noteEn}</td>
          <td><span class="badge ${c.badge}">${currentLang === 'ar' ? c.flagAr : c.flagEn}</span></td>
          <td><button class="source-link" onclick="showSourceModal('${c.sourceKey}')">${currentLang === 'ar' ? 'المستند ↗' : 'Doc ↗'}</button></td>
        </tr>
      `).join('');
    }

    function renderComplaintsTable(data) {
      const tbody = document.getElementById('complaints-tbody');
      tbody.innerHTML = data.map(c => `
        <tr>
          <td><strong style="color:var(--pbi-text-hero);">${currentLang === 'ar' ? c.projectAr : c.projectEn}</strong></td>
          <td><span class="badge ${c.badge}">${currentLang === 'ar' ? c.categoryAr : c.categoryEn}</span></td>
          <td style="max-width:380px; font-size:12px; line-height:1.6;">${currentLang === 'ar' ? c.claimAr : c.claimEn}</td>
          <td class="cell-mono" style="font-size:11.5px;">${c.date}</td>
          <td><span class="cell-mono" style="color:var(--pbi-accent-cyan); font-weight:700;">${c.sourceName}</span></td>
          <td style="font-size:11.5px; color:var(--pbi-text-muted);">${currentLang === 'ar' ? c.classAr : c.classEn}</td>
          <td><button class="source-link" onclick="showSourceModal('${c.sourceKey}')">${currentLang === 'ar' ? 'التوثيق ↗' : 'Evidence ↗'}</button></td>
        </tr>
      `).join('');
    }

    function renderRisksTable(data) {
      const tbody = document.getElementById('risks-tbody');
      tbody.innerHTML = data.map(r => `
        <tr>
          <td><strong style="color:var(--pbi-text-hero);">${currentLang === 'ar' ? r.catAr : r.catEn}</strong></td>
          <td><span class="badge ${r.sevBadge}">${currentLang === 'ar' ? r.sevAr : r.sevEn}</span></td>
          <td><span class="badge badge-med">${currentLang === 'ar' ? r.likAr : r.likEn}</span></td>
          <td style="max-width:340px; font-size:11.5px; line-height:1.6;">${currentLang === 'ar' ? r.mechAr : r.mechEn}</td>
          <td style="max-width:340px; font-size:11.5px; line-height:1.6; color:var(--pbi-accent-emerald);">${currentLang === 'ar' ? r.ctrlAr : r.ctrlEn}</td>
          <td><button class="source-link" onclick="showSourceModal('${r.sourceKey}')">${currentLang === 'ar' ? 'السند ↗' : 'Legal ↗'}</button></td>
        </tr>
      `).join('');
    }

    function renderFinancialsTable() {
      const tbody = document.getElementById('financials-tbody');
      tbody.innerHTML = finRows.map(r => `
        <tr>
          <td><strong style="${r.bold ? 'font-weight:800;' : ''} color:${r.color || 'inherit'}">${currentLang === 'ar' ? r.nameAr : r.nameEn}</strong></td>
          <td class="cell-mono">${r.fy21}</td>
          <td class="cell-mono">${r.fy22}</td>
          <td class="cell-mono">${r.fy23}</td>
          <td class="cell-mono">${r.fy24}</td>
          <td class="cell-mono" style="${r.color ? 'color:' + r.color + '; font-weight:700;' : ''}">${r.fy25}</td>
          <td class="cell-mono" style="font-weight:800; color:var(--pbi-accent-cyan);">${r.h126}</td>
          <td><button class="source-link" onclick="showSourceModal('egx_filings_fy25_h126')">${currentLang === 'ar' ? 'البورصة ↗' : 'EGX ↗'}</button></td>
        </tr>
      `).join('');
    }

    function renderDynamicCards() {
      // Conclusions Cards
      const concCards = [
        {
          title: currentLang === 'ar' ? "فجوة السيولة النقدية مقابل أرباح الدفاتر" : "Earnings vs Cash Conversion Gap",
          desc: currentLang === 'ar' ? "تحقق المجموعة أرباحاً قياسية (9.95 مليار في H1 2026)، إلا أن التدفق التشغيلي بلغ 3.11 مليار فقط (31.2% تحويل)، نظراً لامتصاص 18.26 مليار في الإنشاءات ومخزون قيد التطوير." : "Consolidated net profit reached EGP 9.95B in H1 2026, but CFO was only EGP 3.11B (31.2% conversion), with EGP 18.26B absorbed in construction works-in-progress.",
          badge: currentLang === 'ar' ? "حرج: استنزاف رأسمالي" : "Critical: Capital Drain",
          badgeClass: "badge-high"
        },
        {
          title: currentLang === 'ar' ? "الرافعة المالية غير المرئية (43.99B تأجير تمويلي)" : "Off-Balance Structured Leverage",
          desc: currentLang === 'ar' ? "الديون المصرفية المباشرة تبلغ 16.5 مليار فقط، لكن الالتزامات الفعلية تتضمن 43.99 مليار جنيه عقود تأجير تمويلي لأصول رواسي ومصر والأهلي بفائدة 28.6%." : "Direct bank debt is EGP 16.5B, but off-balance lease liabilities reach EGP 43.99B through sale-and-leaseback of commercial assets with NBE/Banque Misr at 28.6% blended cost.",
          badge: currentLang === 'ar' ? "هيكلي: 43.99 مليار" : "Structural: EGP 44B",
          badgeClass: "badge-high"
        },
        {
          title: currentLang === 'ar' ? "درع العزل القانوني لشركة الإسكندرية (ACC)" : "Contractual Privity Shield (ACC)",
          desc: currentLang === 'ar' ? "توقيع عقود مقاولي الباطن والعمال حصرياً مع شركة الإسكندرية للإنشاءات أو المقاولين المستقلين يحرمهم من الحجز على حسابات أو تدفقات شركة طلعت مصطفى القابضة." : "Subcontracts executed strictly with Alexandria Construction Co. or turnkey EPCs legally isolate listed TMGH holding assets from subcontractor liens.",
          badge: currentLang === 'ar' ? "قانوني: حماية القابضة" : "Legal: Privity Shield",
          badgeClass: "badge-high"
        }
      ];

      document.getElementById('conclusions-cards-container').innerHTML = concCards.map(c => `
        <div class="flag-card" style="border-inline-start-color: var(--pbi-accent-cyan);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:13.5px; color:var(--pbi-text-hero);">${c.title}</strong>
            <span class="badge ${c.badgeClass}">${c.badge}</span>
          </div>
          <div style="font-size:12px; color:var(--pbi-text-muted); line-height:1.6; margin-top:4px;">${c.desc}</div>
        </div>
      `).join('');

      // Disputes Cards
      const dispCards = [
        {
          title: currentLang === 'ar' ? "حكم المحكمة الإدارية العليا ببطلان عقد مدينتي (2010)" : "Supreme Administrative Court: Madinaty Contract Annulment (2010)",
          desc: currentLang === 'ar' ? "قضت المحكمة الإدارية العليا ببطلان عقد تخصيص أرض مدينتي المباشر لمخالفته قانون المناقصات. تمت تسوية النزاع بقرار وزاري عام 2010/2015 باشتراط 7% حصة عينية مباني منجزة لهيئة المجتمعات." : "Egyptian Supreme Administrative Court annulled direct Madinaty land allocation for violating Tenders Law No. 89/1998, restructured via Cabinet settlements requiring 7% finished unit delivery to NUCA.",
          badge: "Level A (Court)",
          sourceKey: "sac_madinaty_2010"
        },
        {
          title: currentLang === 'ar' ? "نزاع أعمال السقالات والأسعار بمدينتي - الدعوى 2923 لسنة 2012 مدني (مطالبة 609,625 ج.م)" : "Madinaty Scaffolding Dispute: Case 2923/2012 North Cairo Civil Court (EGP 609,625)",
          desc: currentLang === 'ar' ? "نزاع مقاول السقالات (شركة خالد هنداوي) ضد شركة الإسكندرية للإنشاءات حول عدم مطابقة أسعار المستخلصات للأسعار المتفق عليها في 3 مواقع بمدينتي (المدرسة البريطانية، بوابة 2011، السوق والمسجد)، ومطالبة بفروق أسعار 609,625 ج.م وطلب إلزام الشركة بتقديم أصول العقود." : "Scaffolding subcontractor Khaled Hendawi filed Case 2923/2012 against ACC over disparity between subcontract and approved IPC rates across 3 Madinaty zones, claiming EGP 609,625 and demanding original subcontracts.",
          badge: "Level B (Defense Memo)",
          sourceKey: "khatib_scaffolding_2012"
        },
        {
          title: currentLang === 'ar' ? "واقعة احتجاز مستحقات مقاول مدينتي شحاتة حسن وإقرار التعطيل (2008)" : "Madinaty Subcontractor Withholding Admission (2008)",
          desc: currentLang === 'ar' ? "تقدم المقاول ببلاغ للنائب العام ضد إدارة المشروع بعد احتجاز مستحقاته؛ وصرح مدير شركة الإسكندرية للإنشاءات (إبراهيم حسبو) لجريدة المصري اليوم باحتجاز المستخلصات عمداً لمنع العمال من مغادرة الموقع بعد القبض على هشام طلعت." : "Subcontractor filed formal complaint with Prosecutor General over withheld payments; ACC Director (Ibrahim Hasabo) admitted on record that dues were held intentionally to prevent workers abandoning site.",
          badge: "Level B (Press)",
          sourceKey: "masry_shehata_2008"
        },
        {
          title: currentLang === 'ar' ? "نزاع مقاول ارتبط بعلاقة عمل 20 عاماً وقضية التهديد الجنائية (2023 - 2026)" : "20-Year Contractor Relationship Payment Dispute & Threat Proceeding",
          desc: currentLang === 'ar' ? "ادعى مقاول وجود مستحقات مالية متأخرة بعد 20 عاماً من العمل مع هشام طلعت مصطفى؛ وانتهى النزاع بحكم جنائي بالحبس سنة في واقعة تهديد، دون أن تفصل المحكمة الجنائية في أصل المديونية المدنية أو تحدد المشروع." : "Contractor with ~20 years working relationship claimed unpaid dues against HTM; resulted in 1-year threat conviction without judicial resolution of underlying civil debt.",
          badge: "Level C (Judicial Press)",
          sourceKey: "haditha_contractor_2023"
        },
        {
          title: currentLang === 'ar' ? "احتجاجات عمال وأمن مدينتي والإسكندرية للإنشاءات (2024-2025)" : "ACC Labor Strife & Madinaty Security Petitions (2024-2025)",
          desc: currentLang === 'ar' ? "وثقت المنصة ومدى مصر احتجاجات لأكثر من 100 موظف بالإسكندرية للإنشاءات على تجميد الرواتب، ومذكرات رسمية لأفراد الأمن بمدينتي للمطالبة ببدلات الإعاشة والأجر الإضافي عن ورديات 12 ساعة." : "Documented sit-ins by >100 ACC staff over wage freezes, and formal petitions by Madinaty security force over grueling 12-hour shifts and meal allowances.",
          badge: "Level D (Labor)",
          sourceKey: "manassa_security_oct2025"
        },
        {
          title: currentLang === 'ar' ? "بطلان رسوم التنازل العقاري - حماية المستهلك (المادة 15)" : "Consumer Protection Agency: Invalidation of Resale Fees",
          desc: currentLang === 'ar' ? "حظر القانون 181 لسنة 2018 تقاضي المطورين أي نسبة (5-10%) من إعادة بيع الوحدات، وهو ما يشكل بؤرة نزاعات قضائية ومحاسبية مستمرة مع ملاك مدينتي والرحاب." : "Article 15 Law 181/2018 explicitly voids all developer resale transfer fees (5-10%), underpinning recurrent litigation by Madinaty and Rehab homeowners.",
          badge: "Statutory Law",
          sourceKey: "cpa_article15_resale"
        },
        {
          title: currentLang === 'ar' ? "تحقيق شبكة أريج الاستقصائي: تخصيص الأراضي والشفافية (2023)" : "ARIJ Investigation: Land Allocation & Developer Transparency (2023)",
          desc: currentLang === 'ar' ? "تحقيق استقصائي حول آليات تخصيص أراضي الدولة لكبار المطورين ومنها مشروعات طلعت مصطفى (نور وسيليا)، مشيراً إلى أن تعديلات الإجراءات قللت الشفافية دون إثبات بطلان المشروعات الحالية." : "Investigative report on state land allocation to major developers including TMG (Noor, Celia), noting reduced procedural transparency while projects operate under regularized decrees.",
          badge: "Level B (ARIJ)",
          sourceKey: "arij_land_allocation_2023"
        },
        {
          title: currentLang === 'ar' ? "توجيهات الرقابة المالية (FRA) حول عقود التطوير والتنازل عن الحقوق (2026)" : "FRA Directives: Real Estate Developer Contracts & Assignment of Rights (2026)",
          desc: currentLang === 'ar' ? "توجيهات رقابية رسمية تحث المقاولين والمشترين على فحص بنود العقود وتوزيع المخاطر وبنود التنازل عن الحقوق وأثر أوراق الدفع المؤجلة لضمان الانضباط التعاقدي." : "Official regulatory directives from the FRA advising buyers and subcontractors to scrutinize contract clauses, assignment of rights, and deferred commercial paper terms.",
          badge: "Regulatory Code",
          sourceKey: "fra_assignment_guidance_2026"
        }
      ];

      document.getElementById('disputes-cards-container').innerHTML = dispCards.map(d => `
        <div class="flag-card" style="border-inline-start-color: var(--pbi-accent-rose);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:13.5px; color:var(--pbi-text-hero);">${d.title}</strong>
            <span class="badge badge-high">${d.badge}</span>
          </div>
          <div style="font-size:12px; color:var(--pbi-text-muted); line-height:1.6; margin-top:4px;">${d.desc}</div>
          <div style="margin-top:8px;">
            <button class="source-link" onclick="showSourceModal('${d.sourceKey}')">${currentLang === 'ar' ? 'فحص السند الرسمي ↗' : 'View Citation ↗'}</button>
          </div>
        </div>
      `).join('');

      // 5-Point Verification Gap Protocol
      const gapCards = [
        {
          num: "01",
          title: currentLang === 'ar' ? "ملف القضية القضائية الرسمية" : "Official Court Case Docket",
          desc: currentLang === 'ar' ? "استخراج صورة رسمية من ملف الدعوى رقم 2923 لسنة 2012 مدني شمال القاهرة تشمل صحيفة الدعوى، محاضر الجلسات، تقرير الخبرة الحسابية، ومنطوق الحكم وشهادة بجدول الاستئناف." : "Certified docket for Case 2923/2012 North Cairo Court: pleadings, minutes, expert quantum report, judgment, and appellate certificate.",
          badge: "Judicial Record"
        },
        {
          num: "02",
          title: currentLang === 'ar' ? "أصول العقود وأوامر التغيير" : "Certified Contracts & Variations",
          desc: currentLang === 'ar' ? "مطابقة النسخ الأصلية المعتمدة لعقود مقاولة الباطن، وجداول الفئات والكميات، وأوامر التغيير الموقعة مسبقاً، ونماذج المستخلصات الجارية وإشعارات الخصم من الاستشاري." : "Original signed subcontracts, BOQs, rate schedules, pre-approved variation orders, and consultant IPC deduction notices.",
          badge: "Technical Audit"
        },
        {
          num: "03",
          title: currentLang === 'ar' ? "كشف حساب متبادل وإثباتات السداد" : "Mutual Ledgers & Wire Proofs",
          desc: currentLang === 'ar' ? "كشف حساب ختامي متبادل يوضح قيمة الأعمال المنفذة والمعتمدة، والمسدد فعلياً عبر شيكات أو تحويلات بنكية، ونسب ضمان الأعمال المحتجزة، والتسويات أو المخالصات النهائية." : "Final mutual account statement showing certified works, verified wire transfers/PDCs, retention releases, and signed waivers.",
          badge: "Financial Proof"
        },
        {
          num: "04",
          title: currentLang === 'ar' ? "التحقق من الشخصية الاعتبارية" : "Entity Privity & Registry Check",
          desc: currentLang === 'ar' ? "تحديد الاسم القانوني ورقم السجل التجاري للطرف المصدر للعقد (مثل ACC)؛ وفحص أي حوالات حقوق أو سندات تثبت مسؤولية الشركة القابضة TMGH مباشرة." : "Commercial registry check of the contracting party (e.g. ACC); audit of assignment of rights to verify privity ring-fencing against TMGH.",
          badge: "Privity Shield"
        },
        {
          num: "05",
          title: currentLang === 'ar' ? "الرد الرسمي الموثق لإدارة المجموعة" : "Formal Documented Developer Response",
          desc: currentLang === 'ar' ? "الحصول على إفادة كتابية مدققة من إدارة طلعت مصطفى أو المقاول العام، مع الالتزام القانوني بأن غياب الرد لا يُعد قرينة على صحة الادعاءات الفردية." : "Documented statement from TMG/EPC management, adhering to the legal standard that non-reply does not prove individual claims.",
          badge: "Due Diligence Gate"
        }
      ];

      const gapContainer = document.getElementById('verification-gap-grid');
      if (gapContainer) {
        gapContainer.innerHTML = gapCards.map(g => `
          <div class="card" style="background:var(--pbi-surface-card); border-top:3px solid var(--pbi-accent-cyan);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-family:var(--pbi-font-mono); font-size:14px; font-weight:900; color:var(--pbi-accent-cyan);">${g.num}</span>
              <span class="pbi-pill-badge badge-cyan">${g.badge}</span>
            </div>
            <div style="font-size:13px; font-weight:800; color:var(--pbi-text-hero); margin-bottom:6px;">${g.title}</div>
            <div style="font-size:11.5px; color:var(--pbi-text-muted); line-height:1.6;">${g.desc}</div>
          </div>
        `).join('');
      }

      // Mustakhlasat 7 Gates Cards
      const gates = [
        { num: "01", name: currentLang === 'ar' ? "حصر الكميات بالموقع" : "Site Quantity Survey", days: "0 - 25d", desc: currentLang === 'ar' ? "مطابقة الأعمال المنفذة واستبعاد أوامر التغيير الشفهية غير المعتمدة." : "Physical measurement; exclusions of verbal variations." },
        { num: "02", name: currentLang === 'ar' ? "مطابقة الجودة والمعامل" : "Quality & Lab Approval", days: "25 - 60d", desc: currentLang === 'ar' ? "خصم بنود الملاحظات (Snagging) واختبارات تكسير الخرسانة." : "Snagging deductions and mandatory concrete test holds." },
        { num: "03", name: currentLang === 'ar' ? "التوثيق والمكتب الفني" : "Document Audit", days: "60 - 105d", desc: currentLang === 'ar' ? "مطابقة أذون التوريد بملفات إدارة مدينتي والدقي المركزية." : "Cross-referencing site delivery slips with central files." },
        { num: "04", name: currentLang === 'ar' ? "تدقيق شركة الإسكندرية (ACC)" : "ACC Technical Audit", days: "105 - 135d", desc: currentLang === 'ar' ? "إعادة تسعير البنود ومراجعة نسبة الإنجاز التعاقدي." : "Unit rate verification against contract BOQ baseline." },
        { num: "05", name: currentLang === 'ar' ? "الاعتماد المالي وإصدار المستخلص" : "Executive IPC Sign-off", days: "135 - 180d", desc: currentLang === 'ar' ? "توقيع المدير المالي وإصدار شهادة الدفع المعتمدة (IPC)." : "Formal signing of certified Interim Payment Certificate." },
        { num: "06", name: currentLang === 'ar' ? "إصدار الشيكات الآجلة (PDC)" : "Deferred PDC Issuance", days: "180 - 225d", desc: currentLang === 'ar' ? "استبدال السداد النقدي بشيكات تجارية آجلة لـ 90-180 يوماً." : "Disbursal of post-dated checks (90 to 180 day terms)." },
        { num: "07", name: currentLang === 'ar' ? "التحصيل والمقاصة البنكية" : "Bank Cash Clearance", days: "225 - 270d", desc: currentLang === 'ar' ? "صرف الشيكات فعلياً في تاريخ الاستحقاق وتسييل السيولة." : "Final bank settlement and cash liquidation for contractor." }
      ];

      document.getElementById('mustakhlasat-steps-container').innerHTML = gates.map(g => `
        <div class="flag-card" style="border-inline-start-color: var(--pbi-accent-amber);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="color:var(--pbi-accent-cyan); font-family:var(--pbi-font-mono); font-size:13px;">GATE ${g.num}</strong>
            <span class="badge badge-med">${g.days}</span>
          </div>
          <div style="font-weight:800; font-size:13px; color:var(--pbi-text-hero); margin-top:2px;">${g.name}</div>
          <div style="font-size:11.5px; color:var(--pbi-text-muted); line-height:1.5; margin-top:4px;">${g.desc}</div>
        </div>
      `).join('');
    }

    function renderTableHeaders() {
      // Projects headers
      document.getElementById('projects-th-row').innerHTML = currentLang === 'ar' ? `
        <th>اسم المشروع</th>
        <th>الموقع والمساحة</th>
        <th>الشركة المالكة وحصة طلعت</th>
        <th>نموذج الأرض والشراكة</th>
        <th>موقف التسليم الفعلي</th>
        <th>المكونات الأساسية والوحدات</th>
        <th>مستوى المخاطرة</th>
        <th>المصدر</th>
      ` : `
        <th>Project Name</th>
        <th>Location & Size</th>
        <th>Owning SPV & Stake</th>
        <th>Land / Partner Model</th>
        <th>Delivery Status</th>
        <th>Key Components</th>
        <th>Risk Level</th>
        <th>Source</th>
      `;

      // Contractors headers
      document.getElementById('contractors-th-row').innerHTML = currentLang === 'ar' ? `
        <th>المشروع</th>
        <th>كيان طلعت مصطفى المتعاقد</th>
        <th>المقاول الرئيسي</th>
        <th>مقاول الباطن / المورد</th>
        <th>نطاق الأعمال المنفذة</th>
        <th>مستند العلاقة والتواريخ</th>
        <th>الملاحظة التوثيقية والنزاع</th>
        <th>مستوى الخطر</th>
        <th>المصدر</th>
      ` : `
        <th>Project</th>
        <th>TMG Counterparty</th>
        <th>Main EPC Contractor</th>
        <th>Subcontractor / Supplier</th>
        <th>Executed Scope</th>
        <th>Contract Document</th>
        <th>Forensic Note / Friction</th>
        <th>Risk Flag</th>
        <th>Source</th>
      `;

      // Complaints headers
      document.getElementById('complaints-th-row').innerHTML = currentLang === 'ar' ? `
        <th>المشروع / الواقعة</th>
        <th>تصنيف النزاع</th>
        <th>تفاصيل الشكوى والوقائع الموثقة</th>
        <th>تاريخ الواقعة</th>
        <th>المنصة / المصدر الصحفي</th>
        <th>التصنيف الجنائي</th>
        <th>المصدر</th>
      ` : `
        <th>Project / Incident</th>
        <th>Category</th>
        <th>Documented Claim / Incident</th>
        <th>Date</th>
        <th>Source Platform</th>
        <th>Classification</th>
        <th>Source</th>
      `;

      // Risks headers
      document.getElementById('risks-th-row').innerHTML = currentLang === 'ar' ? `
        <th>تصنيف الخطر الجنائي</th>
        <th>مستوى الأثر</th>
        <th>الاحتمالية</th>
        <th>الآليات التشغيلية ومؤشرات الإنذار</th>
        <th>إجراءات الفحص والتحوط المقترحة</th>
        <th>المصدر والسند</th>
      ` : `
        <th>Risk Category</th>
        <th>Severity</th>
        <th>Likelihood</th>
        <th>Operational Mechanism</th>
        <th>Actionable Diligence Controls</th>
        <th>Source</th>
      `;

      // Financials headers
      document.getElementById('financials-th-row').innerHTML = currentLang === 'ar' ? `
        <th>المؤشر المالي (مليون جنيه مصري)</th>
        <th>FY2021</th>
        <th>FY2022</th>
        <th>FY2023</th>
        <th>FY2024</th>
        <th>FY2025</th>
        <th>H1 2026</th>
        <th>الإفصاح</th>
      ` : `
        <th>Financial Metric (EGP Millions)</th>
        <th>FY2021</th>
        <th>FY2022</th>
        <th>FY2023</th>
        <th>FY2024</th>
        <th>FY2025</th>
        <th>H1 2026</th>
        <th>Filing</th>
      `;
    }

    function setLanguage(lang) {
      currentLang = lang;
      document.documentElement.setAttribute('lang', lang);
      document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

      document.getElementById('lang-ar').classList.toggle('active', lang === 'ar');
      document.getElementById('lang-en').classList.toggle('active', lang === 'en');

      // Update Nav labels
      const navTexts = {
        ar: {
          brandTitle: "استخبارات طلعت مصطفى",
          brandSub: "PowerBI Executive Portal v5.0",
          navLabel: "وحدات التحقيق الجنائي",
          overview: "لوحة القيادة التنفيذية (Overview)",
          procurement: "المشتريات المدمجة والدرع القانوني",
          mustakhlasat: "المستخلصات وعقبة الصرف (270d)",
          projects: "محفظة المشاريع والأراضي (Landbank)",
          contractors: "سجل المقاولين وسلاسل الإمداد",
          disputes: "الأحكام القضائية وسجلات النزاع",
          financials: "التحليل المالي الجنائي والسيولة",
          sentiment: "شكاوى المقاولين والعمال والملاك",
          risks: "مصفوفة المخاطر ودليل التحوط",
          advisory: "توجيهات المستثمرين والملاك",
          cutoff: "تاريخ التدقيق",
          cap: "رأس المال",
          audited: "مدقق رسمياً من الإفصاحات ومحاضر المحاكم",
          search: "ابحث عن كيان، مقاول، قضية، رقم...",
          presenter: "وضع العرض التنفيذي (CEO Deck)",
          print: "تصدير PDF / طباعة",
          slicerTitle: "محددات وفلاتر التحليل (POWERBI SLICERS)",
          resetSlicer: "إعادة ضبط الفلاتر",
          slicerProj: "المشروع / الأصل المستهدف:",
          slicerSev: "مستوى الحساسية الجنائية:",
          slicerYr: "الأفق الزمني للتقييم:",
          slicerEnt: "كيان التعاقد والدرع القانوني:"
        },
        en: {
          brandTitle: "TMG Intelligence",
          brandSub: "PowerBI Executive Portal v5.0",
          navLabel: "Investigation Modules",
          overview: "Executive Dashboard (Overview)",
          procurement: "Captive Procurement & Privity",
          mustakhlasat: "Payment Gatekeeping (270d)",
          projects: "Master Projects & Landbank",
          contractors: "Contractors & Supply Chains",
          disputes: "Judicial Records & Disputes",
          financials: "Forensic Financials & Debt",
          sentiment: "Stakeholder Complaints & Labor",
          risks: "Risk Matrix & Counterparty Guide",
          advisory: "Investor & Buyer Advisory",
          cutoff: "Audit Date",
          cap: "Issued Capital",
          audited: "Audited from Statutory Filings & Court Rulings",
          search: "Search entities, contractors, lawsuits, metrics...",
          presenter: "Executive CEO Deck",
          print: "Export PDF / Print",
          slicerTitle: "ANALYSIS FILTERS & SLICERS",
          resetSlicer: "Reset All Slicers",
          slicerProj: "Target Asset / Project:",
          slicerSev: "Forensic Risk Severity:",
          slicerYr: "Assessment Horizon:",
          slicerEnt: "Contractual Entity / Shield:"
        }
      };

      const t = navTexts[lang];
      document.getElementById('lbl-brand-title').textContent = t.brandTitle;
      document.getElementById('lbl-brand-sub').textContent = t.brandSub;
      document.getElementById('lbl-nav-label').textContent = t.navLabel;
      document.getElementById('nav-overview').textContent = t.overview;
      document.getElementById('nav-procurement').textContent = t.procurement;
      document.getElementById('nav-mustakhlasat').textContent = t.mustakhlasat;
      document.getElementById('nav-projects').textContent = t.projects;
      document.getElementById('nav-contractors').textContent = t.contractors;
      document.getElementById('nav-disputes').textContent = t.disputes;
      document.getElementById('nav-financials').textContent = t.financials;
      document.getElementById('nav-sentiment').textContent = t.sentiment;
      document.getElementById('nav-risks').textContent = t.risks;
      if (document.getElementById('nav-advisory')) document.getElementById('nav-advisory').textContent = t.advisory;
      document.getElementById('lbl-cutoff').textContent = t.cutoff;
      document.getElementById('lbl-cap').textContent = t.cap;
      document.getElementById('lbl-badge-audited').textContent = t.audited;
      document.getElementById('global-search').placeholder = t.search;
      document.getElementById('btn-presenter-lbl').textContent = t.presenter;
      document.getElementById('btn-print-lbl').textContent = t.print;
      document.getElementById('lbl-slicer-title').textContent = t.slicerTitle;
      document.getElementById('lbl-reset-slicer').textContent = t.resetSlicer;
      document.getElementById('slicer-title-proj').textContent = t.slicerProj;
      document.getElementById('slicer-title-sev').textContent = t.slicerSev;
      document.getElementById('slicer-title-yr').textContent = t.slicerYr;
      document.getElementById('slicer-title-ent').textContent = t.slicerEnt;

      if (document.getElementById('lbl-gap-protocol-title')) {
        document.getElementById('lbl-gap-protocol-title').textContent = currentLang === 'ar' ? 'بروتوكول إغلاق فجوة التحقق لمقاولي الباطن والمستخلصات (Verification Gap Protocol)' : 'Subcontractor Verification Gap Closure Protocol';
        document.getElementById('lbl-gap-protocol-sub').textContent = currentLang === 'ar' ? 'المستندات الخمسة الإلزامية للفصل بين الشكاوى التاريخية والالتزامات القانونية النافذة وفق تقرير العناية الواجبة (مدينتي وسقالات 2012)' : 'The 5 mandatory document checks required to substantiate trade claims and judicial dues from open filings';
      }

      if (document.getElementById('t-adv-investor-title')) {
        const isAr = currentLang === 'ar';
        document.getElementById('t-adv-investor-title').textContent = isAr 
          ? 'أولاً: توجيهات وتحليل لمستثمري البورصة المصرية (EGX: TMGH)' 
          : 'Section I: Strategic Guidance for Capital Market Investors (EGX: TMGH)';
        document.getElementById('t-adv-investor-sub').textContent = isAr 
          ? 'فحص جودة الأرباح، تحويل التدفقات النقدية (CFO)، هيكل الديون المباشرة والتأجير التمويلي، وحوكمة العائلة' 
          : 'Cash conversion quality (CFO Gap), direct & off-balance leaseback debt, and family ownership governance';
        
        document.getElementById('lbl-adv-inv1-title').textContent = isAr 
          ? 'قوة الزخم المالي مقابل جودة التحويل النقدي (Cash Conversion)' 
          : 'Revenue Momentum vs Operating Cash Conversion (CFO)';
        document.getElementById('lbl-adv-inv1-badge').textContent = isAr ? 'نسبة تحويل ~31%' : 'Conversion ~31%';

        document.getElementById('lbl-adv-inv2-title').textContent = isAr 
          ? 'هيكل التمويل والديون المباشرة وغير المباشرة (Leaseback)' 
          : 'Capital Structure: Direct Borrowings & Financial Leases';
        document.getElementById('lbl-adv-inv2-badge').textContent = isAr ? 'التزامات 60.5B @ 28.6%' : 'Debt 60.5B @ 28.6%';

        document.getElementById('lbl-adv-inv3-title').textContent = isAr 
          ? 'طبيعة رصيد المبيعات التعاقدية غير المسلمة (Backlog Reality)' 
          : 'Backlog Reality: Contractual Unearned Liabilities';
        document.getElementById('lbl-adv-inv3-badge').textContent = isAr ? 'رصيد 441.2B جنيه' : 'Backlog 441.2B EGP';

        document.getElementById('lbl-adv-inv4-title').textContent = isAr 
          ? 'الحوكمة وهيكل الملكية والأطراف ذات الصلة (Related Parties)' 
          : 'Governance, UBO Family Equity & Related Parties';
        document.getElementById('lbl-adv-inv4-badge').textContent = isAr ? 'سيطرة العائلة 43.2%' : 'Family Equity 43.2%';

        document.getElementById('t-adv-buyers-title').textContent = isAr 
          ? 'ثانياً: توجيهات للمشترين والملاك في مشروعات المجموعة (Buyers & Owners Advisory)' 
          : 'Section II: Prospective Buyers & Existing Homeowners Advisory';
        document.getElementById('t-adv-buyers-sub').textContent = isAr 
          ? 'الفحص النافي للجهالة قبل التعاقد، تدقيق وديعة الصيانة، والمخالفة الصريحة لقانون حماية المستهلك رقم 181 لسنة 2018' 
          : 'Pre-purchase legal diligence, maintenance deficit auditing, and statutory consumer protection rights';

        document.getElementById('lbl-adv-buy1-title').textContent = isAr 
          ? 'المشترون الجدد: الملاءة المؤسسية ليست ضماناً فردياً للوحدة' 
          : 'Prospective Buyers: Corporate Solvency is Not Unit Title Guarantee';
        document.getElementById('lbl-adv-buy2-title').textContent = isAr 
          ? 'مراجعة بنود العقد وشروط التأخير والتكاليف الإضافية' 
          : 'Purchase Agreement Clauses, Delay Waivers & Total Lifecycle Cost';
        document.getElementById('lbl-adv-buy3-title').textContent = isAr 
          ? 'الملاك الحاليون: مطالبات "فروق وديعة الصيانة" السنوية' 
          : 'Existing Owners: Recurring Maintenance Surcharges (15k-45k EGP)';
        document.getElementById('lbl-adv-buy4-title').textContent = isAr 
          ? 'رسوم التنازل العقاري وإعادة البيع (مخالفة القانون 181/2018)' 
          : 'Resale Transfer Percentage Fees (Law 181/2018 Art.15 Violation)';
      }

      updateThemeButton();
      renderTableHeaders();
      renderProjectsTable(projectsData);
      renderContractorsTable(contractorsData);
      renderComplaintsTable(complaintsData);
      renderRisksTable(risksData);
      renderFinancialsTable();
      renderDynamicCards();
      initAll14Charts();
    }

    // Modal Handling
    function showSourceModal(key) {
      const src = sourcesData[key];
      if (!src) return;
      document.getElementById('modal-source-title').textContent = currentLang === 'ar' ? src.titleAr : src.titleEn;
      document.getElementById('modal-source-desc').textContent = currentLang === 'ar' ? src.descAr : src.descEn;
      document.getElementById('modal-source-publisher').textContent = currentLang === 'ar' ? src.publisherAr : src.publisherEn;
      document.getElementById('modal-source-date').textContent = src.date;
      document.getElementById('modal-source-url').href = src.url;
      document.getElementById('source-modal').classList.add('active');
    }

    function closeSourceModal() {
      document.getElementById('source-modal').classList.remove('active');
    }

    // D3 Privity Tree Implementation
    let d3Svg, d3G, d3Zoom;

    function renderD3PrivityTree() {
      const container = document.getElementById('d3-privity-tree');
      if (!container) return;
      const width = container.clientWidth || 900;
      const height = container.clientHeight || 480;

      d3.select('#d3-privity-tree svg').remove();

      d3Svg = d3.select('#d3-privity-tree')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      d3G = d3Svg.append('g').attr('transform', currentLang === 'ar' ? `translate(${width - 120}, 40)` : 'translate(100, 40)');

      d3Zoom = d3.zoom().scaleExtent([0.5, 2.5]).on('zoom', (e) => {
        d3G.attr('transform', e.transform);
      });
      d3Svg.call(d3Zoom);

      const treeLayout = d3.tree().size([height - 80, width - 280]);
      const root = d3.hierarchy(privityTreeData);
      treeLayout(root);

      d3G.selectAll('.d3-link')
        .data(root.links())
        .enter()
        .append('path')
        .attr('class', 'd3-link')
        .attr('d', d3.linkHorizontal().x(d => currentLang === 'ar' ? -d.y : d.y).y(d => d.x));

      const node = d3G.selectAll('.d3-node')
        .data(root.descendants())
        .enter()
        .append('g')
        .attr('class', 'd3-node')
        .attr('transform', d => `translate(${currentLang === 'ar' ? -d.y : d.y},${d.x})`)
        .on('click', (event, d) => showInspector(d.data));

      node.append('circle')
        .attr('r', 8)
        .style('fill', d => d.data.color || 'var(--pbi-accent-cyan)')
        .style('stroke', 'var(--pbi-surface-card)');

      node.append('text')
        .attr('dy', 4)
        .attr('x', d => currentLang === 'ar' ? (d.children ? 14 : -14) : (d.children ? -14 : 14))
        .style('text-anchor', d => currentLang === 'ar' ? (d.children ? 'start' : 'end') : (d.children ? 'end' : 'start'))
        .text(d => currentLang === 'ar' ? d.data.nameAr : d.data.nameEn)
        .style('fill', 'var(--pbi-text-hero)');
    }

    function showInspector(data) {
      document.getElementById('inspector-name').textContent = currentLang === 'ar' ? data.nameAr : data.nameEn;
      document.getElementById('inspector-type').textContent = currentLang === 'ar' ? data.typeAr : data.typeEn;
      document.getElementById('inspector-desc').textContent = currentLang === 'ar' ? data.descAr : data.descEn;
      document.getElementById('inspector-shield').textContent = currentLang === 'ar' ? data.shieldAr : data.shieldEn;
      document.getElementById('inspector-risk').textContent = currentLang === 'ar' ? data.riskAr : data.riskEn;
      
      const srcBox = document.getElementById('inspector-source-box');
      if (data.sourceKey) {
        srcBox.innerHTML = `<button class="source-link" onclick="showSourceModal('${data.sourceKey}')">${currentLang === 'ar' ? 'فحص السند الرسمي ↗' : 'View Source ↗'}</button>`;
      } else {
        srcBox.innerHTML = '';
      }
      document.getElementById('node-inspector').classList.add('active');
    }

    function closeInspector() {
      document.getElementById('node-inspector').classList.remove('active');
    }

    function zoomD3(scaleFactor) {
      if (d3Svg && d3Zoom) {
        d3Svg.transition().duration(250).call(d3Zoom.scaleBy, scaleFactor);
      }
    }

    function resetD3View() {
      renderD3PrivityTree();
    }

    // Global Text Search
    function handleGlobalSearch(term) {
      const q = term.toLowerCase().trim();
      if (!q) {
        applySlicers();
        return;
      }
      const matchText = (val) => val && val.toLowerCase().includes(q);

      const fProjects = projectsData.filter(p => matchText(p.nameAr) || matchText(p.nameEn) || matchText(p.locAr) || matchText(p.locEn) || matchText(p.spv));
      renderProjectsTable(fProjects);

      const fContractors = contractorsData.filter(c => matchText(c.projectAr) || matchText(c.projectEn) || matchText(c.mainContractorAr) || matchText(c.mainContractorEn) || matchText(c.subcontractorAr) || matchText(c.subcontractorEn) || matchText(c.scopeAr));
      renderContractorsTable(fContractors);

      const fComplaints = complaintsData.filter(c => matchText(c.projectAr) || matchText(c.projectEn) || matchText(c.claimAr) || matchText(c.sourceName));
      renderComplaintsTable(fComplaints);

      const fRisks = risksData.filter(r => matchText(r.catAr) || matchText(r.catEn) || matchText(r.mechAr) || matchText(r.ctrlAr));
      renderRisksTable(fRisks);
    }

    // Presenter Mode Engine
    let currentSlide = 0;

    function openPresenterMode() {
      document.getElementById('presenter-overlay').classList.add('active');
      renderSlide(0);
      document.addEventListener('keydown', handlePresenterKeydown);
    }

    function closePresenterMode() {
      document.getElementById('presenter-overlay').classList.remove('active');
      document.removeEventListener('keydown', handlePresenterKeydown);
    }

    function renderSlide(index) {
      currentSlide = index;
      const s = presenterSlides[index];
      document.getElementById('presenter-slide-num').textContent = s.num;
      document.getElementById('presenter-slide-title').textContent = currentLang === 'ar' ? s.titleAr : s.titleEn;
      document.getElementById('presenter-slide-content').innerHTML = currentLang === 'ar' ? s.contentAr : s.contentEn;
      document.getElementById('presenter-speaker-note').textContent = currentLang === 'ar' ? s.noteAr : s.noteEn;

      document.getElementById('presenter-dock-indicator').textContent = `${index + 1} / ${presenterSlides.length}`;
      const pct = ((index + 1) / presenterSlides.length) * 100;
      document.getElementById('slide-progress-bar').style.width = pct + '%';

      document.getElementById('btn-prev-slide').textContent = currentLang === 'ar' ? '❮ السابق' : '❮ Previous';
      document.getElementById('btn-next-slide').textContent = currentLang === 'ar' ? 'التالي ❯' : 'Next ❯';
    }

    function prevSlide() {
      if (currentSlide > 0) renderSlide(currentSlide - 1);
    }

    function nextSlide() {
      if (currentSlide < presenterSlides.length - 1) renderSlide(currentSlide + 1);
    }

    function handlePresenterKeydown(e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        if (currentLang === 'ar') {
          if (e.key === 'ArrowLeft') nextSlide();
          if (e.key === 'ArrowRight') prevSlide();
        } else {
          if (e.key === 'ArrowRight') nextSlide();
          if (e.key === 'ArrowLeft') prevSlide();
        }
      } else if (e.key === 'Escape') {
        closePresenterMode();
      }
    }

    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('tmg_theme', next);
      updateThemeButton();
      initAll14Charts();
      if (typeof renderD3PrivityTree === 'function') {
        renderD3PrivityTree();
      }
    }

    function updateThemeButton() {
      const isLight = document.documentElement.getAttribute('data-theme') === 'light';
      const icon = document.getElementById('theme-toggle-icon');
      const lbl = document.getElementById('theme-toggle-lbl');
      if (icon && lbl) {
        if (isLight) {
          icon.textContent = '🌙';
          lbl.textContent = currentLang === 'ar' ? 'الوضع الداكن' : 'Dark Mode';
        } else {
          icon.textContent = '☀️';
          lbl.textContent = currentLang === 'ar' ? 'الوضع الفاتح' : 'Light Mode';
        }
      }
    }

    // Initialization
    document.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('tmg_theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeButton();
      setLanguage('ar');
    });
  </script>
</body>
</html>
'''

# Replace the data placeholders in html_content
html_content = html_content.replace("__REPLACE_SOURCES_DATA__", sources_data_str)
html_content = html_content.replace("__REPLACE_PROJECTS_DATA__", projects_data_str)
html_content = html_content.replace("__REPLACE_CONTRACTORS_DATA__", contractors_data_str)
html_content = html_content.replace("__REPLACE_COMPLAINTS_DATA__", complaints_data_str)
html_content = html_content.replace("__REPLACE_RISKS_DATA__", risks_data_str)
html_content = html_content.replace("__REPLACE_PRIVITY_TREE_DATA__", privity_tree_data_str)
html_content = html_content.replace("__REPLACE_SLIDES_DATA__", slides_data_str)

# Write to outputs
with open(output_path_1, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(output_path_2, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"PowerBI Executive Dashboard successfully generated at: {output_path_1} and {output_path_2}")
print(f"Total HTML size: {len(html_content.encode('utf-8'))} bytes")
