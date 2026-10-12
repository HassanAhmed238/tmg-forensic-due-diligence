# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

build_script_path = r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py"

with open(build_script_path, 'r', encoding='utf-8') as f:
    code = f.read()

target = '<div id="source-modal"'
excel_modal_html = r'''<!-- Modal for Excel Source Files -->
  <div id="excel-modal">
    <div class="modal-box" style="max-width: 840px;">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:14px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <div style="width:38px; height:38px; border-radius:10px; background:rgba(16,185,129,0.15); color:var(--accent-emerald); display:flex; align-items:center; justify-content:center; font-weight:800;">
            <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          </div>
          <div>
            <h3 style="font-size:16px; font-weight:800;" id="m-excel-title">مركز تحميل نماذج الإكسيل الحسابية والمدققة (Excel Source Hub)</h3>
            <p style="font-size:11.5px; color:var(--text-dim);" id="m-excel-sub">كافة الملفات تحتوي على معادلات حسابية حية (Formulas) متوافقة 100% مع Microsoft Excel</p>
          </div>
        </div>
        <button onclick="closeExcelModal()" style="background:none; border:none; color:var(--text-dim); cursor:pointer; font-size:24px; line-height:1;">&times;</button>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap:14px; margin-top:16px;">
        
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
            <span>تحميل النموذج الشامل (.xlsx)</span>
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
            <span>تحميل القوائم المدققة (.xlsx)</span>
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
            <span>تحميل النموذج الجنائي (.xlsx)</span>
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
            <span>تحميل دليل الشركات (.xlsx)</span>
          </a>
        </div>

      </div>

      <div style="margin-top:16px; text-align:center; border-top:1px solid var(--border-subtle); padding-top:14px;">
        <button onclick="closeExcelModal()" class="btn-action" style="padding:8px 24px;">إغلاق النافذة</button>
      </div>
    </div>
  </div>

  '''

if target in code:
    code = code.replace(target, excel_modal_html + target, 1)
    print("Injected Excel modal before source-modal")
    with open(build_script_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Saved build_perfect_dashboard.py")
else:
    print("Target not found")
