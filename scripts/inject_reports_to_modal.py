# -*- coding: utf-8 -*-
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

build_script_path = r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py"

with open(build_script_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Look for the modal box and add the 4 report download cards
needle = r'<!-- File 4: Project Companies & Contacts -->'
report_cards_html = r'''<!-- File 5: Master Forensic Audit Report (Official PDF) -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-high" style="background:rgba(239,68,68,0.15); color:var(--accent-rose); border-color:rgba(239,68,68,0.3);">Official Report (PDF)</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">396.4 KB (16 Pages)</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Forensic_Due_Diligence_Report.pdf</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">التقرير الجنائي الشامل باللغة الإنجليزية، بصيغة PDF قابلة للطباعة بتنسيق LaTeX وجداول تدقيق محاسبي دقيقة.</p>
          </div>
          <a href="downloads/TMG_Forensic_Due_Diligence_Report.pdf" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل التقرير (Official PDF)</span>
          </a>
        </div>

        <!-- File 6: Master Forensic Audit Report (Word DOCX) -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-med">Executive Word (.docx)</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">38.7 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Forensic_Due_Diligence_Report.docx</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">نسخة مايكروسوفت وورد التنفيذية بتنسيق Minimax-DOCX الفاخر وجداول منسقة وقابلة للتعديل والطباعة.</p>
          </div>
          <a href="downloads/TMG_Forensic_Due_Diligence_Report.docx" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل التقرير (Word .docx)</span>
          </a>
        </div>

        <!-- File 7: LaTeX Source Code (.tex) -->
        <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span class="badge badge-low">LaTeX Source (.tex)</span>
              <span style="font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">7.3 KB</span>
            </div>
            <h4 style="font-size:13.5px; font-weight:800; color:var(--text-main);">TMG_Forensic_Due_Diligence_Report.tex</h4>
            <p style="font-size:11.5px; color:var(--text-muted); margin-top:4px;">الكود المصدري الأكاديمي الكامل بلغة LaTeX متوافق مع TeXLive وOverleaf مع كافة المعادلات الرياضية.</p>
          </div>
          <a href="downloads/TMG_Forensic_Due_Diligence_Report.tex" download class="btn-action highlight" style="justify-content:center; text-decoration:none;">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            <span>تحميل الكود المصدري (LaTeX .tex)</span>
          </a>
        </div>

        '''

if needle in code and "TMG_Forensic_Due_Diligence_Report.pdf" not in code:
    code = code.replace(needle, report_cards_html + needle, 1)
    print("Injected Report deliverables into modal")
    with open(build_script_path, "w", encoding="utf-8") as f:
        f.write(code)
    print("Saved updated build_perfect_dashboard.py")
else:
    print("Needle not found or already injected")
