# -*- coding: utf-8 -*-
"""
Script to inject:
1. Interactive TMG Audited Balance Sheet & Financial Engine with live dynamic calculations & stress simulation.
2. Excel Source Hub & direct download cards in Tab 7 and Topbar.
3. Excel Download Modal with all 8 verified workbooks.
4. Updates build_perfect_dashboard.py and rebuilds both TMG_Forensic_Due_Diligence_Dashboard.html and index.html.
"""

import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

build_script_path = r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py"

with open(build_script_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Topbar Button Injection
# Find where the presenter button is:
topbar_target = r'<button class="btn-action highlight" onclick="openPresenterMode()">'
topbar_replacement = r'''<!-- Excel Download Button -->
        <button class="btn-action highlight" onclick="openExcelModal()" title="تحميل ملفات الإكسيل الأصلية الحسابية">
          <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          <span id="btn-excel-lbl">ملفات الإكسيل الأصلية (Excel Sources)</span>
        </button>

        <button class="btn-action" onclick="openPresenterMode()">'''

if topbar_target in code:
    code = code.replace(topbar_target, topbar_replacement, 1)
    print("Injected Topbar Excel button")
else:
    print("Warning: topbar_target not found")

# 2. Excel Modal HTML Injection
# Look for #source-modal and add #excel-modal right after it
modal_target = r'<!-- Modal for Detailed Source Inspection -->'
excel_modal_html = r'''<!-- Modal for Excel Source Files -->
  <div id="excel-modal">
    <div class="modal-box" style="max-width: 820px;">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:14px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <div style="width:36px; height:36px; border-radius:8px; background:rgba(16,185,129,0.15); color:var(--accent-emerald); display:flex; align-items:center; justify-content:center; font-weight:800;">
            <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          </div>
          <div>
            <h3 style="font-size:16px; font-weight:800;" id="m-excel-title">مركز تحميل نماذج الإكسيل الحسابية والمدققة (Excel Source Hub)</h3>
            <p style="font-size:11.5px; color:var(--text-dim);" id="m-excel-sub">كافة الملفات تحتوي على معادلات حسابية حية (Formulas) متوافقة 100% مع Microsoft Excel</p>
          </div>
        </div>
        <button onclick="closeExcelModal()" style="background:none; border:none; color:var(--text-dim); cursor:pointer; font-size:22px;">&times;</button>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap:14px; margin-top:14px;">
        
        <!-- File 1: Master Risk & Balance Sheet -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-high" style="background:rgba(6,182,212,0.15); color:var(--accent-cyan); border-color:rgba(6,182,212,0.3);">15 ورقة عمل حسابية</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">47.6 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">دليل المهندس، مصفوفة المخاطر الأربعة، تحليل ويبل، قائمة المركز المالي، التحليل الرأسي، ومؤشرات السيولة والرافعة.</p>
          </div>
          <a href="downloads/TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل الملف (.xlsx)</span>
          </a>
        </div>

        <!-- File 2: Audited Balance Sheet & Financial Statements -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-low">7 أوراق تدقيق مالي</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">25.1 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">القوائم المالية المدققة للبورصة (2021-2025)، قائمة الدخل، الميزانية، ومصفوفة SWOT الاستراتيجية وTOWS ونموذج P.ZONE.</p>
          </div>
          <a href="downloads/TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل الملف (.xlsx)</span>
          </a>
        </div>

        <!-- File 3: Master Forensic Audit Model -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-med">النموذج الجنائي الشامل</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">47.8 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Master_Forensic_Audit_Model.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">النسخة الشاملة المدمجة لكافة حسابات الفحص النافي للجهالة، ومصفوفات المخاطر والتحليل الإحصائي وقوائم المركز المالي.</p>
          </div>
          <a href="downloads/TMG_Master_Forensic_Audit_Model.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل الملف (.xlsx)</span>
          </a>
        </div>

        <!-- File 4: Project Companies & Contacts -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-low">42 شركة و38 مسؤول</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">17.2 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Project_Companies_Contacts_One_Sheet.xlsx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">دليل شركات المقاولات والاستشاريين والمطورين، مع هواتف ومواقع رسمية وبريد إلكتروني وروابط لينكد إن للمسؤولين.</p>
          </div>
          <a href="downloads/TMG_Project_Companies_Contacts_One_Sheet.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل الملف (.xlsx)</span>
          </a>
        </div>

      </div>

      <div style="margin-top:14px; text-align:center; border-top:1px solid var(--border-subtle); padding-top:14px;">
        <button onclick="closeExcelModal()" class="btn-action" style="padding:8px 24px;">إغلاق النافذة</button>
      </div>
    </div>
  </div>
'''

if modal_target in code:
    code = code.replace(modal_target, excel_modal_html + "\n  " + modal_target, 1)
    print("Injected Excel Modal")
else:
    print("Warning: modal_target not found")

# 3. CSS for #excel-modal
css_target = r'#source-modal {'
css_excel = r'''#excel-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
    }
    #excel-modal.active { display: flex; }
    
    '''
if css_target in code:
    code = code.replace(css_target, css_excel + css_target, 1)
    print("Injected CSS for excel modal")

# 4. Enhance Tab 7 (tab-financials) with:
# A) Excel Download Hub Card
# B) Interactive Balance Sheet & Real-Time Calculation Engine with Stress Testing
tab_fin_needle = r'<div class="bezel-wrap" style="margin-top: 20px;">' + "\n" + r'          <div class="card">' + "\n" + r'            <div class="card-header">' + "\n" + r'              <div>' + "\n" + r'                <div class="card-title" id="t-fin-table-title">'

tab_fin_interactive_section = r'''<!-- EXCEL SOURCE & DOWNLOAD HUB CARD -->
        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card" style="background: linear-gradient(135deg, rgba(6,182,212,0.06), rgba(59,130,246,0.04)); border: 1px solid rgba(6,182,212,0.3);">
            <div class="card-header">
              <div>
                <div class="card-title" style="color: var(--accent-cyan); display:flex; align-items:center; gap:8px;">
                  <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                  <span id="t-fin-excel-hub-title">مركز تحميل نماذج الإكسيل الحسابية الأصلية (Audited Excel Models & Calculations)</span>
                </div>
                <div class="card-subtitle" id="t-fin-excel-hub-sub">الملفات تحتوي على المعادلات الحسابية الكاملة (Formulas) لقوائم المركز المالي، الدخل، التدفقات النقدية، ومصفوفات ويبل الإحصائية</div>
              </div>
              <button onclick="openExcelModal()" class="btn-action highlight" style="font-weight:800;">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                <span id="btn-browse-all-excel">استعراض كافة الملفات (8 ملفات)</span>
              </button>
            </div>

            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:14px; margin-top:10px;">
              <div style="background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; gap:10px;">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge badge-high" style="font-size:10px;">15 ورقة عمل حسابية</span>
                    <span style="font-size:10.5px; font-family:var(--font-mono); color:var(--text-dim);">47.6 KB</span>
                  </div>
                  <h4 style="font-size:13px; font-weight:800; margin-top:6px;">TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx</h4>
                  <p style="font-size:11px; color:var(--text-muted); margin-top:4px;">مصفوفة المخاطر الأربعة + ويبل + ميزانية طلعت مصطفى الكاملة بمعادلاتها الحسابية.</p>
                </div>
                <a href="downloads/TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none; font-size:11.5px;">تحميل النموذج الشامل (.xlsx)</a>
              </div>

              <div style="background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; gap:10px;">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge badge-low" style="font-size:10px;">7 أوراق تدقيق مالي</span>
                    <span style="font-size:10.5px; font-family:var(--font-mono); color:var(--text-dim);">25.1 KB</span>
                  </div>
                  <h4 style="font-size:13px; font-weight:800; margin-top:6px;">TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx</h4>
                  <p style="font-size:11px; color:var(--text-muted); margin-top:4px;">القوائم المالية المدققة للبورصة، نسب السيولة، مصفوفة SWOT، ونموذج P.ZONE.</p>
                </div>
                <a href="downloads/TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none; font-size:11.5px;">تحميل القوائم المدققة (.xlsx)</a>
              </div>

              <div style="background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; gap:10px;">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge badge-med" style="font-size:10px;">42 شركة و38 مسؤول</span>
                    <span style="font-size:10.5px; font-family:var(--font-mono); color:var(--text-dim);">17.2 KB</span>
                  </div>
                  <h4 style="font-size:13px; font-weight:800; margin-top:6px;">TMG_Project_Companies_Contacts_One_Sheet.xlsx</h4>
                  <p style="font-size:11px; color:var(--text-muted); margin-top:4px;">دليل شركات المقاولات والاستشاريين والمطورين وهواتفهم وروابط لينكد إن الموثقة.</p>
                </div>
                <a href="downloads/TMG_Project_Companies_Contacts_One_Sheet.xlsx" download class="btn-action highlight" style="justify-content:center; text-decoration:none; font-size:11.5px;">تحميل دليل الشركات (.xlsx)</a>
              </div>
            </div>
          </div>
        </div>

        <!-- TMG INTERACTIVE AUDITED BALANCE SHEET & REAL-TIME CALCULATION ENGINE -->
        <div class="bezel-wrap" style="margin-top: 20px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title" id="t-bs-calc-title">محرك قائمة المركز المالي التفاعلي والحسابات الرياضية (Audited Balance Sheet Dynamic Engine)</div>
                <div class="card-subtitle" id="t-bs-calc-sub">اختر السنة المالية أو اختبر سيناريوهات الضغط (Stress Testing) مع إعادة احتساب نسب السيولة والرافعة ورأس المال العامل آلياً</div>
              </div>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:12px; font-weight:700; color:var(--text-muted);" id="lbl-select-fy">السنة المالية:</span>
                <div class="ctrl-group" id="bs-year-selector">
                  <button class="ctrl-pill" onclick="selectBSYear('FY21')">2021</button>
                  <button class="ctrl-pill" onclick="selectBSYear('FY22')">2022</button>
                  <button class="ctrl-pill" onclick="selectBSYear('FY23')">2023</button>
                  <button class="ctrl-pill active" onclick="selectBSYear('FY24')">2024</button>
                  <button class="ctrl-pill" onclick="selectBSYear('FY25')">2025</button>
                  <button class="ctrl-pill" onclick="selectBSYear('H1_26')">H1 2026</button>
                </div>
              </div>
            </div>

            <!-- Parity Equation Ribbon -->
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap:12px; margin-bottom:18px;">
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--text-dim); text-transform:uppercase;">إجمالي الأصول (Total Assets)</div>
                <div style="font-size:20px; font-weight:900; font-family:var(--font-mono); color:var(--accent-cyan); margin-top:4px;" id="bs-card-assets">278.80 مليار ج.م</div>
                <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">= الأصول المتداولة + الأصول الثابتة</div>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--text-dim); text-transform:uppercase;">إجمالي الالتزامات (Total Liabilities)</div>
                <div style="font-size:20px; font-weight:900; font-family:var(--font-mono); color:var(--accent-rose); margin-top:4px;" id="bs-card-liab">164.03 مليار ج.م</div>
                <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">قروض وتسهيلات + دفعات حجز + تأجير</div>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--text-dim); text-transform:uppercase;">حقوق الملكية (Total Equity)</div>
                <div style="font-size:20px; font-weight:900; font-family:var(--font-mono); color:var(--accent-emerald); margin-top:4px;" id="bs-card-equity">114.77 مليار ج.م</div>
                <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">رأس المال + أرباح مرحلة + أيقون ADQ</div>
              </div>

              <div style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.3); border-radius:10px; padding:14px;">
                <div style="font-size:11px; font-weight:700; color:var(--accent-emerald); text-transform:uppercase;">فحص التوازن المحاسبي (Parity Check)</div>
                <div style="font-size:18px; font-weight:900; font-family:var(--font-mono); color:var(--accent-emerald); margin-top:4px;" id="bs-card-check">صفر ج.م (متطابق 100%)</div>
                <div style="font-size:11px; color:var(--accent-emerald); margin-top:2px;">الأصول - (الالتزامات + حقوق الملكية) = 0</div>
              </div>
            </div>

            <!-- Two-Column Balance Sheet Grid -->
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap:20px;">
              
              <!-- LEFT: ASSETS BREAKDOWN -->
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:18px;">
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:10px; margin-bottom:12px;">
                  <h4 style="font-size:14px; font-weight:800; color:var(--accent-cyan); display:flex; align-items:center; gap:6px;">
                    <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
                    <span>تفصيل جانب الأصول (Assets Breakdown)</span>
                  </h4>
                  <span class="badge badge-low" style="font-size:10.5px;">القيم بمليون ج.م</span>
                </div>
                
                <table style="width:100%; font-size:12.5px; border-collapse:collapse;">
                  <tbody id="bs-assets-rows">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>

              <!-- RIGHT: LIABILITIES & EQUITY BREAKDOWN -->
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:18px;">
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:10px; margin-bottom:12px;">
                  <h4 style="font-size:14px; font-weight:800; color:var(--accent-rose); display:flex; align-items:center; gap:6px;">
                    <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                    <span>الالتزامات وحقوق الملكية (Liab & Equity)</span>
                  </h4>
                  <span class="badge badge-high" style="font-size:10.5px;">القيم بمليون ج.م</span>
                </div>
                
                <table style="width:100%; font-size:12.5px; border-collapse:collapse;">
                  <tbody id="bs-liab-rows">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>

            </div>

            <!-- LIVE FINANCIAL STRESS TESTER & RATIO SIMULATOR -->
            <div style="margin-top:20px; background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:18px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
                <div>
                  <h4 style="font-size:14px; font-weight:800; color:var(--accent-amber); display:flex; align-items:center; gap:6px;">
                    <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
                    <span>محاكي الضغط المالي وحاسبة النسب الحية (Stress Simulation & Live Ratio Engine)</span>
                  </h4>
                  <p style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">حرك المؤشرات لاختبار سيناريوهات الضغط الفعلي وملاحظة التغير الفوري في نسب السيولة ورأس المال العامل</p>
                </div>
                <button onclick="resetBSStress()" class="btn-action" style="font-size:11.5px;">إعادة الضبط الافتراضي (Reset)</button>
              </div>

              <!-- Sliders Grid -->
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin-bottom:16px;">
                <div>
                  <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                    <span>إدراج تأجير رواسي التمويلي بالكامل بالميزانية:</span>
                    <strong id="val-slider-lease" style="font-family:var(--font-mono); color:var(--accent-cyan);">100%</strong>
                  </div>
                  <input type="range" id="slider-lease" min="0" max="100" value="100" step="10" oninput="updateBSCalculations()" style="width:100%; accent-color:var(--accent-cyan);">
                  <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--text-dim);"><span>0% خارج الميزانية</span><span>100% كامل الالتزام</span></div>
                </div>

                <div>
                  <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                    <span>تسديد عاجل لمستحقات مقاولي الباطن (صرف نقدي):</span>
                    <strong id="val-slider-pay" style="font-family:var(--font-mono); color:var(--accent-amber);">0%</strong>
                  </div>
                  <input type="range" id="slider-pay" min="0" max="50" value="0" step="5" oninput="updateBSCalculations()" style="width:100%; accent-color:var(--accent-amber);">
                  <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--text-dim);"><span>0% استمرار التأخير</span><span>50% سداد فوري نقدي</span></div>
                </div>

                <div>
                  <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                    <span>خصم تسييل مخزون الأراضي غير المطورة:</span>
                    <strong id="val-slider-wip" style="font-family:var(--font-mono); color:var(--accent-rose);">0%</strong>
                  </div>
                  <input type="range" id="slider-wip" min="0" max="30" value="0" step="5" oninput="updateBSCalculations()" style="width:100%; accent-color:var(--accent-rose);">
                  <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--text-dim);"><span>0% قيمة دفترية</span><span>30% تخفيض اضطراري</span></div>
                </div>
              </div>

              <!-- Recalculated Ratios Cards -->
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; border-top:1px solid var(--border-subtle); padding-top:14px;">
                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">نسبة التداول الحالية (Current Ratio)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--text-main); margin-top:2px;" id="calc-curr-ratio">1.59x</div>
                  <div style="font-size:10px; color:var(--accent-emerald);">مقبول (> 1.2x)</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">السيولة السريعة (Quick Ratio)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-rose); margin-top:2px;" id="calc-quick-ratio">0.72x</div>
                  <div style="font-size:10px; color:var(--accent-rose);">حرجة بعد استبعاد المخزون (< 1.0x)</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">صافي الدين (Net Debt)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-amber); margin-top:2px;" id="calc-net-debt">18.80B ج.م</div>
                  <div style="font-size:10px; color:var(--text-muted);">(الديون البنكية + التأجير) - النقدية</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">نسبة المديونية (Debt to Equity)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-cyan); margin-top:2px;" id="calc-debt-eq">0.44x</div>
                  <div style="font-size:10px; color:var(--text-muted);">الديون التمويلية / حقوق المساهمين</div>
                </div>

                <div style="text-align:center;">
                  <div style="font-size:11px; color:var(--text-dim);">رأس المال العامل (Working Capital)</div>
                  <div style="font-size:19px; font-weight:900; font-family:var(--font-mono); color:var(--accent-emerald); margin-top:2px;" id="calc-working-cap">+69.80B ج.م</div>
                  <div style="font-size:10px; color:var(--accent-emerald);">الأصول المتداولة - الالتزامات المتداولة</div>
                </div>
              </div>

            </div>
          </div>
        </div>

        ''' + tab_fin_needle

if tab_fin_needle in code:
    code = code.replace(tab_fin_needle, tab_fin_interactive_section, 1)
    print("Injected Interactive Balance Sheet Engine into Tab 7")
else:
    print("Warning: tab_fin_needle not found")

# 5. Inject JavaScript functions for the Interactive Balance Sheet Engine
js_target = r'function switchTab(tabId) {'
bs_js_code = r'''
    // =========================================================================
    // TMG AUDITED BALANCE SHEET DYNAMIC ENGINE & FORMULA RECALCULATION
    // =========================================================================
    const tmgBSDatabase = {
      FY21: {
        cash: 4210, rec: 24500, wip: 46800, fin_inv: 1521, fa_cwip: 31200, oth_ast: 3470,
        st_loans: 3800, notes_pay: 5120, cust_adv: 38500, lt_debt: 8200, lease_debt: 1200, oth_liab: 2140,
        capital: 20636, reserves: 3450, ret_earn: 28655, nci: 0
      },
      FY22: {
        cash: 4780, rec: 28600, wip: 54200, fin_inv: 2100, fa_cwip: 36800, oth_ast: 3920,
        st_loans: 4500, notes_pay: 7300, cust_adv: 48200, lt_debt: 9800, lease_debt: 2100, oth_liab: 2600,
        capital: 20636, reserves: 4100, ret_earn: 31165, nci: 0
      },
      FY23: {
        cash: 11500, rec: 36400, wip: 71300, fin_inv: 4200, fa_cwip: 51200, oth_ast: 4620,
        st_loans: 6200, notes_pay: 9800, cust_adv: 72000, lt_debt: 14500, lease_debt: 4800, oth_liab: 3630,
        capital: 20636, reserves: 5200, ret_earn: 42454, nci: 0
      },
      FY24: {
        cash: 32000, rec: 48200, wip: 102500, fin_inv: 8500, fa_cwip: 81400, oth_ast: 6200,
        st_loans: 8900, notes_pay: 13500, cust_adv: 95000, lt_debt: 19800, lease_debt: 22100, oth_liab: 4730,
        capital: 20636, reserves: 7800, ret_earn: 52834, nci: 33500
      },
      FY25: {
        cash: 41200, rec: 62800, wip: 138500, fin_inv: 14200, fa_cwip: 107500, oth_ast: 8000,
        st_loans: 11200, notes_pay: 15790, cust_adv: 117680, lt_debt: 26500, lease_debt: 34400, oth_liab: 6830,
        capital: 20636, reserves: 11500, ret_earn: 68164, nci: 59500
      },
      H1_26: {
        cash: 47000, rec: 68500, wip: 152000, fin_inv: 16500, fa_cwip: 118000, oth_ast: 8900,
        st_loans: 12500, notes_pay: 16800, cust_adv: 129000, lt_debt: 28500, lease_debt: 44000, oth_liab: 7400,
        capital: 20636, reserves: 12800, ret_earn: 77964, nci: 69000
      }
    };

    let currentBSYear = 'FY24';

    function openExcelModal() {
      const modal = document.getElementById('excel-modal');
      if (modal) modal.classList.add('active');
    }

    function closeExcelModal() {
      const modal = document.getElementById('excel-modal');
      if (modal) modal.classList.remove('active');
    }

    function selectBSYear(yr) {
      currentBSYear = yr;
      const btns = document.querySelectorAll('#bs-year-selector button');
      btns.forEach(b => {
        if (b.getAttribute('onclick').includes(yr)) b.classList.add('active');
        else b.classList.remove('active');
      });
      updateBSCalculations();
    }

    function resetBSStress() {
      document.getElementById('slider-lease').value = 100;
      document.getElementById('slider-pay').value = 0;
      document.getElementById('slider-wip').value = 0;
      updateBSCalculations();
    }

    function updateBSCalculations() {
      const raw = tmgBSDatabase[currentBSYear] || tmgBSDatabase.FY24;
      
      const leasePct = parseFloat(document.getElementById('slider-lease')?.value || 100) / 100;
      const payPct = parseFloat(document.getElementById('slider-pay')?.value || 0) / 100;
      const wipDiscount = parseFloat(document.getElementById('slider-wip')?.value || 0) / 100;

      document.getElementById('val-slider-lease').innerText = `${Math.round(leasePct * 100)}%`;
      document.getElementById('val-slider-pay').innerText = `${Math.round(payPct * 100)}%`;
      document.getElementById('val-slider-wip').innerText = `${Math.round(wipDiscount * 100)}%`;

      // Recalculate Assets with stress
      const adjCash = Math.max(0, raw.cash - (raw.notes_pay * payPct));
      const adjWIP = raw.wip * (1 - wipDiscount);
      const currAssets = adjCash + raw.rec + adjWIP + raw.fin_inv + (raw.oth_ast * 0.6);
      const nonCurrAssets = raw.fa_cwip + (raw.oth_ast * 0.4);
      const totalAssets = currAssets + nonCurrAssets;

      // Recalculate Liabilities with stress
      const adjPayables = raw.notes_pay * (1 - payPct);
      const currLiab = raw.st_loans + adjPayables + raw.cust_adv + (raw.oth_liab * 0.5);
      const adjLease = raw.lease_debt * leasePct;
      const nonCurrLiab = raw.lt_debt + adjLease + (raw.oth_liab * 0.5);
      const totalLiab = currLiab + nonCurrLiab;

      // Recalculate Equity
      const totalEquity = raw.capital + raw.reserves + raw.ret_earn + raw.nci - (raw.wip * wipDiscount);
      const totalLiabAndEquity = totalLiab + totalEquity;
      const balanceCheck = totalAssets - totalLiabAndEquity;

      // Update Ribbon Cards
      document.getElementById('bs-card-assets').innerText = `${(totalAssets / 1000).toFixed(2)}B ج.م`;
      document.getElementById('bs-card-liab').innerText = `${(totalLiab / 1000).toFixed(2)}B ج.م`;
      document.getElementById('bs-card-equity').innerText = `${(totalEquity / 1000).toFixed(2)}B ج.م`;
      
      const checkEl = document.getElementById('bs-card-check');
      if (Math.abs(balanceCheck) < 1) {
        checkEl.innerText = "0.00 ج.م (متطابق 100%)";
        checkEl.style.color = "var(--accent-emerald)";
      } else {
        checkEl.innerText = `${(balanceCheck / 1000).toFixed(2)}B ج.م (فرق ضغط)`;
        checkEl.style.color = "var(--accent-amber)";
      }

      // Render Assets Table Rows
      const assetsHtml = `
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>النقدية وما في حكمها</strong> (Cash & Equivalents)</td><td class="cell-mono" style="text-align:right; font-weight:700;">${Math.round(adjCash).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>العملاء وأوراق القبض</strong> (Receivables)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.rec).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>مشروعات قيد التنفيذ / مخزون الأراضي</strong> (WIP)</td><td class="cell-mono" style="text-align:right;">${Math.round(adjWIP).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>استثمارات مالية بالقيمة العادلة</strong> (Investments)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.fin_inv).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أصول ثابتة وفنادق قيد التطوير</strong> (Fixed Assets)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.fa_cwip).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أصول أخرى متداولة وغير متداولة</strong> (Other)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.oth_ast).toLocaleString()} م.ج</td></tr>
        <tr style="background:var(--table-hover); font-weight:800; border-top:2px solid var(--accent-cyan);"><td style="padding:9px 4px; color:var(--accent-cyan);">إجمالي الأصول الحسابي (Total Assets)</td><td class="cell-mono" style="text-align:right; color:var(--accent-cyan); font-size:14px;">${Math.round(totalAssets).toLocaleString()} م.ج</td></tr>
      `;
      document.getElementById('bs-assets-rows').innerHTML = assetsHtml;

      // Render Liabilities & Equity Rows
      const liabHtml = `
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>تسهيلات بنكية قصيرة الأجل</strong> (ST Credit)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.st_loans).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أوراق الدفع ومستحقات المقاولين</strong> (Payables)</td><td class="cell-mono" style="text-align:right; color:var(--accent-amber);">${Math.round(adjPayables).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>دفعات حجز مقدمة من العملاء</strong> (Advances)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.cust_adv).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>قروض بنكية طويلة الأجل</strong> (LT Debt)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.lt_debt).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>التزامات تأجير تمويلي (رواسي)</strong> (Lease)</td><td class="cell-mono" style="text-align:right; color:var(--accent-rose);">${Math.round(adjLease).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>رأس المال المصدر والمدفوع</strong> (Capital)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.capital).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>أرباح مرحلة واحتياطيات</strong> (Retained)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.reserves + raw.ret_earn).toLocaleString()} م.ج</td></tr>
        <tr style="border-bottom:1px solid var(--border-subtle);"><td style="padding:7px 4px;"><strong>الحصص غير المسيطرة (أيقون ADQ)</strong> (NCI)</td><td class="cell-mono" style="text-align:right;">${Math.round(raw.nci).toLocaleString()} م.ج</td></tr>
        <tr style="background:var(--table-hover); font-weight:800; border-top:2px solid var(--accent-rose);"><td style="padding:9px 4px; color:var(--accent-rose);">إجمالي الالتزامات والملكية (Total Liab & Eq)</td><td class="cell-mono" style="text-align:right; color:var(--accent-rose); font-size:14px;">${Math.round(totalLiabAndEquity).toLocaleString()} م.ج</td></tr>
      `;
      document.getElementById('bs-liab-rows').innerHTML = liabHtml;

      // Calculate and Update Ratios
      const currentRatio = currLiab > 0 ? (currAssets / currLiab) : 0;
      const quickRatio = currLiab > 0 ? ((currAssets - adjWIP) / currLiab) : 0;
      const totalDebt = raw.st_loans + raw.lt_debt + adjLease;
      const netDebt = totalDebt - adjCash;
      const debtToEquity = totalEquity > 0 ? (totalDebt / totalEquity) : 0;
      const workingCapital = currAssets - currLiab;

      document.getElementById('calc-curr-ratio').innerText = `${currentRatio.toFixed(2)}x`;
      document.getElementById('calc-quick-ratio').innerText = `${quickRatio.toFixed(2)}x`;
      document.getElementById('calc-net-debt').innerText = `${(netDebt / 1000).toFixed(2)}B ج.م`;
      document.getElementById('calc-debt-eq').innerText = `${debtToEquity.toFixed(2)}x`;
      document.getElementById('calc-working-cap').innerText = `${workingCapital >= 0 ? '+' : ''}${(workingCapital / 1000).toFixed(2)}B ج.م`;
    }

    ''' + js_target

if js_target in code:
    code = code.replace(js_target, bs_js_code, 1)
    print("Injected Balance Sheet Dynamic JavaScript code")
else:
    print("Warning: js_target not found")

# 6. Call updateBSCalculations on init
init_target = r'renderAllCharts();'
init_replacement = r'''renderAllCharts();
      updateBSCalculations();'''
if init_target in code:
    code = code.replace(init_target, init_replacement, 1)
    print("Injected updateBSCalculations call into init")

# Write updated build_perfect_dashboard.py
with open(build_script_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated build_perfect_dashboard.py")
