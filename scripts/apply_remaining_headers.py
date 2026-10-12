# -*- coding: utf-8 -*-
"""
Upgrade generator script to transform generate_powerbi_ceo_dashboard.py into a full Microsoft Power BI interactive experience.
Transforms the remaining chart containers 2 to 11 into full Power BI visual headers.
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'scripts/generate_powerbi_ceo_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Map of exact chart titles in generate_powerbi_ceo_dashboard.py
charts_to_replace = [
    (
        'chartRevenueBacklogCombo',
        '2. نمو الإيرادات المجمعة ورصيد المبيعات المتعاقد عليها (Backlog Combo)',
        'إيرادات التسليم السكني والفنادق (أعمدة) مقابل رصيد المبيعات غير المسلمة (خط - مليار جنيه)',
        'مؤشر تراكمي',
        'badge-cyan'
    ),
    (
        'chartForensicRiskRadar',
        '3. رادار أبعاد المخاطر الجنائية (6-Axis Risk Radar)',
        'تقييم الصرف، العزل القانوني، التحكيم، والتضخم مقابل السقف الآمن (1-10)',
        'تحليل 6 أبعاد',
        'badge-rose'
    ),
    (
        'chartDebtStructureTreemapDoughnut',
        '4. هيكل الالتزامات والديون الإجمالية (Debt Architecture)',
        'عقود التأجير التمويلي خارج الميزانية، أوراق الدفع، والتسهيلات البنكية (مليار جنيه)',
        '76.0B إجمالي الديون',
        'badge-purple'
    ),
    (
        'chartOwnershipUBODoughnut',
        '5. هيكل الملكية والمساهمين الرئيسيين (UBO Matrix)',
        'توزيع حصص رأس المال المصدر: عائلة طلعت مصطفى والتداول الحر وصناديق السيادة',
        '20.64B رأس المال',
        'badge-cyan'
    ),
    (
        'chartIPCMustakhlasatSCurve',
        '6. منحنى دورة صرف المستخلصات S-Curve (تعاقدي 90 يوماً مقابل فعلي 270 يوماً)',
        'المسار الزمني لمراحل التدقيق حتى التحصيل ومقاصة الشيكات (فجوة احتجاز 180 يوماً)',
        'المستخلصات وأوراق الدفع',
        'badge-amber'
    ),
    (
        'chartContractorDisputeBubble',
        '7. مصفوفة حجم التعاقد مقابل مؤشر النزاعات والتوتر (Dispute Friction)',
        'حجم التعاقد (مليار جنيه) مقابل مؤشر التوتر العلني وقضايا المحاكم والاحتجاجات (1-10)',
        'خريطة الاحتكاك',
        'badge-rose'
    ),
    (
        'chartVulnerabilityGauge',
        '8. مقياس تعرض مقاولي الباطن للمخاطر (Subcontractor Vulnerability Gauge)',
        'مؤشر التعرض التراكمي لسعر الصرف، تأخر الصرف، وشروط العقود (8.8 / 10 - حرج)',
        'مؤشر الحساسية',
        'badge-rose'
    ),
    (
        'chartInflationTornado',
        '9. مخطط إعصار حساسية التضخم والعملة الأجنبية (FX Tornado Chart)',
        'مستوى الانكشاف على العملة الصعبة ومخاطر استيراد معدات المياه والمضخات (P.Zone / MEP)',
        'حساسية الصدمات',
        'badge-amber'
    ),
    (
        'landbankBarChart',
        '10. توزيع محفظة الأراضي (Landbank Footprint)',
        'المساحات الإجمالية لأبرز المدن والمشاريع التابعة للمجموعة (فدان)',
        '26,722 فدان',
        'badge-cyan'
    ),
    (
        'chartEvidenceHierarchyPolar',
        '11. هرمية قوة الأدلة والموثوقية (Evidence Hierarchy)',
        'أحكام قضائية وإفصاحات رسمية مقابل سوابق هندسية وتسويق',
        'حجية الإثبات',
        'badge-emerald'
    )
]

for canvas_id, title, sub, badge_text, badge_class in charts_to_replace:
    old_block = f'''<div class="pbi-card-header">
                <div>
                  <div class="pbi-card-title">{title}</div>
                  <div class="pbi-card-subtitle">{sub}</div>
                </div>
                <span class="pbi-pill-badge {badge_class}">{badge_text}</span>
              </div>'''

    new_block = f'''<div class="pbi-visual-header">
                <div class="pbi-visual-title-box">
                  <div class="pbi-card-title" style="font-size:13px;">{title}</div>
                  <div class="pbi-card-subtitle">{sub}</div>
                </div>
                <div class="pbi-visual-actions">
                  <span class="pbi-pill-badge {badge_class}" style="margin-inline-end:4px;">{badge_text}</span>
                  <button class="pbi-visual-btn" onclick="openFocusMode('{canvas_id}', '{title}')" title="Focus Mode / Show as Table">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>⛶ تفكيك</span>
                  </button>
                  <button class="pbi-visual-btn" onclick="exportChartDataCSV('{canvas_id}')" title="Export CSV Data">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  </button>
                </div>
              </div>'''

    if old_block in code:
        code = code.replace(old_block, new_block, 1)
        print(f"Successfully upgraded header for {canvas_id}")
    else:
        print(f"Could not find exact block for {canvas_id}")

with open(r'scripts/generate_powerbi_ceo_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated all remaining visual headers in scripts/generate_powerbi_ceo_dashboard.py!")
