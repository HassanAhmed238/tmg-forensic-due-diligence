# -*- coding: utf-8 -*-
"""
Update TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx
Rewrites all explanatory banners and front guide to sound like a Senior Project Controls & Risk Director
explaining the system to a Fresh Graduate Site/Project Controls Engineer:
- Professional, rigorous, practical engineering language (Project Controls, Site Management, Claims, IPCs, Reliability Engineering).
- Clear breakdown of Weibull Analysis (Shape factor alpha, Scale parameter beta, Hazard rate, Quality Action limits).
- Clear engineering context of TMG megaprojects (Madinaty, Noor, SouthMED) and subcontractor dynamics.
"""

import sys, os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"F:\Mr Hesham\TMG\TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx"
print(f"Opening workbook for Senior Engineering rewrite: {file_path}")
wb = openpyxl.load_workbook(file_path, data_only=False)

# Typography & Palette: Professional Corporate Engineering
font_title_ar = Font(name="Cairo", size=13.5, bold=True, color="1E3A8A")
font_sec_title = Font(name="Cairo", size=11, bold=True, color="0284C7")
font_head_box = Font(name="Cairo", size=10, bold=True, color="FFFFFF")
font_text_ar = Font(name="Cairo", size=9.5, color="1E293B")
font_text_bold = Font(name="Cairo", size=9.5, bold=True, color="0F172A")
font_note_ar = Font(name="Cairo", size=9, italic=True, color="475569")
font_alert_title = Font(name="Cairo", size=11, bold=True, color="B91C1C")

fill_navy = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
fill_cyan = PatternFill(start_color="0284C7", end_color="0284C7", fill_type="solid")
fill_light_blue = PatternFill(start_color="F0F9FF", end_color="F0F9FF", fill_type="solid")
fill_light_amber = PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid")
fill_light_rose = PatternFill(start_color="FEF2F2", end_color="FEF2F2", fill_type="solid")
fill_light_green = PatternFill(start_color="F0FDF4", end_color="F0FDF4", fill_type="solid")

thin_side = Side(style='thin', color="CBD5E1")
card_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
thick_border_blue = Border(left=Side(style='medium', color="0284C7"), right=thin_side, top=thin_side, bottom=thin_side)
thick_border_amber = Border(left=Side(style='medium', color="D97706"), right=thin_side, top=thin_side, bottom=thin_side)
thick_border_rose = Border(left=Side(style='medium', color="DC2626"), right=thin_side, top=thin_side, bottom=thin_side)
thick_border_green = Border(left=Side(style='medium', color="16A34A"), right=thin_side, top=thin_side, bottom=thin_side)

align_right_wrap = Alignment(horizontal="right", vertical="center", wrap_text=True)
align_center_wrap = Alignment(horizontal="center", vertical="center", wrap_text=True)

# ==============================================================================
# 1. FRONT SHEET: "دليل إدارة المخاطر للمهندس"
# ==============================================================================
# 1. FRONT SHEET: "دليل إدارة المخاطر للمهندس"
# ==============================================================================
first_name = wb.sheetnames[0]
wb.remove(wb[first_name])

ws_guide = wb.create_sheet(title="دليل إدارة المخاطر للمهندس", index=0)
ws_guide.sheet_view.rightToLeft = True
ws_guide.views.sheetView[0].showGridLines = True

# Header Banner
ws_guide.merge_cells("A1:G1")
b1 = ws_guide.cell(1, 1, "🏗️ دليل مهندس إدارة المشروعات والمكتب الفني (Project Controls & Risk Engineering Guide)")
b1.font = font_title_ar
b1.alignment = align_center_wrap
b1.fill = PatternFill(start_color="E0F2FE", end_color="E0F2FE", fill_type="solid")
ws_guide.row_dimensions[1].height = 36

sections = [
    (
        "📌 أولاً: المفهوم الهندسي لإدارة المخاطر في المشروعات العملاقة (Megaprojects):",
        "يا بشمهندس، بصفتك مهندس في مشروع ضخم (زي مدينتي أو ساوث ميد أو مدينة نور)، إدارة المخاطر (Risk Management) مش مجرد كلام نظري أو جدول بنسلمه في كراسة الشروط.\n"
        "إدارة المخاطر هي 'نظام إنذار مبكر' (Early Warning System) بيجاوبك بالأرقام على 3 أسئلة حاسمة:\n"
        "1. إيه الأعطال والمشاكل التعاقدية والتنفيذية المتكررة في الموقع؟ (Disputes, Late IPCs, Inflation, Labor Strife).\n"
        "2. إيه احتمالية حدوث المشكلة دي إحصائياً؟ ومعدل تكرارها كل أسبوع؟\n"
        "3. مين الخطر الأكبر اللي لو مخدناش بالنا منه فوراً، هيوقف الجداول الزمنية (Baseline Schedule) ويستنزف ميزانية المشروع (Cost Overrun)؟",
        fill_light_blue,
        font_sec_title,
        thick_border_blue
    ),
    (
        "📑 ثانياً: الهيكل الإجرائي لصفحات الملف (Workflow Architecture):",
        "الملف ده مبني على تسلسل هندسي واحترافي مقسم لـ 4 مراحل متتابعة:\n"
        "1. ورقة العصف الذهني (Risk Brainstorming): تحديد المخاطر المرتبطة بكل إدارة (Technical Office, Procurement, Site Ops, Legal) وطرق التحكم الوقائية.\n"
        "2. شيتات التقييم الدوري الأسبوعي (Risk Assesment): رصد وتتبع عدد مرات ظهور المشكلة (Occurrences) أسبوعياً على مدار 12 أسبوعاً (3 أشهر) واستخراج معامل التشتت (Likelihood L عبر AVEDEV).\n"
        "3. شيتات نمذجة وايبول (Weibull Reliability Analysis): تطبيق نموذج توزيع وايبول الرياضي لحساب معدل الإخفاق الزمني (Hazard Rate) واشتقاق الاحتمالية التراكمية (p).\n"
        "4. مصفوفة الأولوية والترتيب النهائي (Risk score): حساب درجة الخطر الإجمالية (Risk Score = p × L) لترتيب الأولويات للمدير التنفيذي ومدير المشروع.",
        fill_light_amber,
        Font(name="Cairo", size=10.5, bold=True, color="D97706"),
        thick_border_amber
    ),
    (
        "📐 ثالثاً: الدليل الرياضي لمعادلات وايبول (Weibull Analysis Explained for Engineers):",
        "توزيع وايبول (Weibull Distribution) هو النموذج الإحصائي الأقوى عالمياً في هندسة الموثوقية (Reliability Engineering) وإدارة مخاطر التشييد:\n"
        "• معامل الشكل (Weibull Slope α): بيعبر عن سلوك الخطر مع الوقت:\n"
        "  - إذا كان α > 1 (زي ما طالع في ملفنا 2.0 إلى 2.7): ده بيثبت هندسياً ظاهرة 'معدل التآكل المتسارع' (Wear-out Phase)؛ يعني المشكلة كل ما الوقت بيعدي عليها من غير حل جذري، بتتراكم وتتفاقم وتضغط على مقاولي الباطن بمعدل أسرع!\n"
        "• معامل القياس (Scale Parameter β): بيعبر عن الزمن المعتاد المميز لتكرار الواقعة (Characteristic Life).\n"
        "• دالة الاحتمال التراكمي (Weibull CDF p): الاحتمالية الفعلية لحدوث الخطر عند وصول المشروع لمتوسط تردد التشغيل المعتاد.\n"
        "• حدود التحكم عند مستوى ثقة 99% (Action Limit): ده السقف الحرج (Threshold). لو عدد المشاكل في أي أسبوع تجاوز هذا الرقم، يبقى النظام خرج عن السيطرة الإحصائية (Out-of-Control) ولازم تتدخل كمهندس فوراً وتصدر تقرير عدم مطابقة أو مذكرة للمدير العام.",
        fill_light_rose,
        Font(name="Cairo", size=10.5, bold=True, color="DC2626"),
        thick_border_rose
    ),
    (
        "🏢 رابعاً: مصفوفة المخاطر الأربعة المدققة لمجموعة طلعت مصطفى (TMG Specific Risks):",
        "🥇 المركز الأول (Rank 1) — تأخير صرف المستخلصات وأوراق الدفع (Payment & Privity Shield):\n"
        "توقيع العقود مع الذراع التنفيذي (شركة الإسكندرية ACC أو أتريوم AQC) وليس القابضة، ومد أجل الاعتماد عبر 7 بوابات حصر، ثم السداد بشيكات آجلة (PDCs) لـ 90-270 يوماً. حجم أوراق الدفع يتجاوز 15.79B جنيه، وهو الخطر الأول لأنه بيهدد السيولة النقدية لمقاولي الباطن.\n"
        "🥈 المركز الثاني (Rank 2) — تضخم الأسعار وفصل التوريد عن المصنعيات (Cost Inflation & Material Decoupling):\n"
        "شراء الخامات الأساسية (حديد وأسمنت) مركزياً وحصر المقاول على المصنعيات، مما يجرده من هوامش أرباح التوريد ويعرضه لزيادات أجور العمالة والمعدات.\n"
        "🥉 المركز الثالث (Rank 3) — مكون الأعمال الكهروميكانيكية ومعدات البحيرات المستوردة (Water & Lagoon MEP):\n"
        "تنفيذ 107 كم بحيرات وشواطئ بمشروعات ساوث ميد ومدينتي يتطلب استيراد محطات ضخ وفلاتر متطورة بالدولار واليورو، مما يعرض التكلفة لفروق سعر الصرف وتأخير التوريد الجمركي.\n"
        "🎖️ المركز الرابع (Rank 4) — علاقات العمل واحتجاجات الموقع (Labor Strife & Workforce Friction):\n"
        "مخاطر توقف العمالة بالمواقع الكبرى حال تعثر المقاول في سداد الأجور، وتستوجب تفعيل حساب وسيط (Escrow) لصرف مستحقات العمالة مباشرة.",
        fill_light_green,
        Font(name="Cairo", size=10.5, bold=True, color="16A34A"),
        thick_border_green
    )
]

r_curr = 3
for title, text, bg_fill, title_font, border_style in sections:
    ws_guide.merge_cells(start_row=r_curr, start_column=1, end_row=r_curr, end_column=7)
    c_t = ws_guide.cell(r_curr, 1, title)
    c_t.font = title_font
    c_t.fill = bg_fill
    c_t.border = border_style
    c_t.alignment = align_right_wrap
    ws_guide.row_dimensions[r_curr].height = 26

    ws_guide.merge_cells(start_row=r_curr+1, start_column=1, end_row=r_curr+1, end_column=7)
    c_b = ws_guide.cell(r_curr+1, 1, text)
    c_b.font = font_text_ar
    c_b.fill = bg_fill
    c_b.border = border_style
    c_b.alignment = align_right_wrap
    
    lines_count = text.count('\n') + (len(text) // 95) + 1
    ws_guide.row_dimensions[r_curr+1].height = max(55, lines_count * 18)
    
    r_curr += 3

ws_guide.column_dimensions["A"].width = 14
ws_guide.column_dimensions["B"].width = 14
ws_guide.column_dimensions["C"].width = 16
ws_guide.column_dimensions["D"].width = 18
ws_guide.column_dimensions["E"].width = 18
ws_guide.column_dimensions["F"].width = 18
ws_guide.column_dimensions["G"].width = 18

print("Updated Sheet: دليل إدارة المخاطر للمهندس")

# ==============================================================================
# 2. IN-SHEET EXPLANATIONS FOR "Risk Brainstorming"
# ==============================================================================
ws_b = wb["Risk Brainstorming"]
ws_b.sheet_view.rightToLeft = True
start_r = 9

ws_b.cell(start_r, 1, "📘 توجيه هندسي: هيكلية العصف الذهني وتبويب المخاطر التعاقدية (Risk Breakdown Structure):").font = font_sec_title
start_r += 1

b_expl_text = (
    "• الهدف الهندسي: قبل إصدار أوامر الإسناد (LOA) وبدء أعمال الموقع، بنعمل فحص شامل لكل إدارة لتحديد مسارات النزاع المحتملة.\n"
    "• الأعمدة 1 و 2 (Department & Key Elements): تحديد الإدارة المعنية ومحور العمليات التخصصي (عقود، مشتريات، إشراف موقع، أو بنية تحتية).\n"
    "• العمود 3 و 4 (Processes & Identified Risks): وصف الآلية التشغيلية التي ينشأ منها الخطر، والتعريف الفني للخطر المترتب عليها (مثل تأخر صرف مستخلصات مقاولي الباطن IPCs أو تآكل هوامش الربح نتيجة التضخم).\n"
    "• العمود 5 و 6 (Current vs Proposed Controls): مقارنة أسلوب إدارة المشروع الحالي بالضوابط التعاقدية الموصى بها لإغلاق ثغرات النزاع والتحوط ضد قضايا التحكيم أو المطالبات الزمنية والمالية (Claims & EOT)."
)
ws_b.merge_cells(start_row=start_r, start_column=1, end_row=start_r+1, end_column=6)
c_expl = ws_b.cell(start_r, 1, b_expl_text)
c_expl.font = font_text_ar
c_expl.fill = fill_light_blue
c_expl.border = thick_border_blue
c_expl.alignment = align_right_wrap
ws_b.row_dimensions[start_r].height = 70
print("Updated in-sheet explanation: Risk Brainstorming")

# ==============================================================================
# 3. IN-SHEET EXPLANATIONS FOR "Risk Assesment" SHEETS
# ==============================================================================
assess_sheets_eng = [
    (
        "Risk Assesment(Payment&Privity)",
        "سجل الرصد الأسبوعي لمستخلصات مقاولي الباطن والعزل التعاقدي (Payment Certification & Privity Audit)",
        "رصد وتوثيق دوري لشكاوى ومطالبات مقاولي الباطن بشأن تأخر اعتماد المستخلصات الجارية (IPCs) والشيكات الآجلة (PDCs) لدى شركة الإسكندرية (ACC) وأتريوم (AQC)."
    ),
    (
        "Risk Assesment(Cost Inflation)",
        "سجل الرصد الأسبوعي لمطالبات فروق الأسعار وتضخم الخامات (Cost Inflation & Price Variations)",
        "رصد أسبوعي لطلبات مقاولي الباطن بتعديل أسعار الفئات (Rate Adjustments) نتيجة تضخم أجور العمالة وتكاليف تشغيل المعدات في ظل عقود المصنعيات محددة السعر."
    ),
    (
        "Risk Assesment(Water & Lagoon)",
        "سجل الرصد الأسبوعي لتوريدات الأعمال الكهروميكانيكية ومعدات البحيرات (Water & Lagoon MEP Infrastructure)",
        "رصد أسبوعي للتأخيرات اللوجستية، واضطرابات فتح الاعتمادات المستندية، وتغيرات أسعار الصرف المرتبطة بمعدات محطات الرفع والفلاتر والبحيرات المستوردة."
    ),
    (
        "Risk Assesment(Labor & Strife)",
        "سجل الرصد الأسبوعي لاحتجاجات واضطرابات العمالة بالموقع (Workforce Strife & Site Grievances)",
        "رصد أسبوعي لمؤشرات التوتر الموقعي، وبلاغات مكاتب العمل، ومذكرات توقف الأعمال الناتجة عن تأخر مقاولي الباطن في صرف رواتب العمالة المباشرة."
    )
]

for s_name, title_box, custom_intro in assess_sheets_eng:
    ws_curr = wb[s_name]
    ws_curr.sheet_view.rightToLeft = True
    r_box = 17
    
    ws_curr.cell(r_box, 1, f"📘 التوجيه الهندسي لقراءة السجل: {title_box}").font = font_sec_title
    
    text_content = (
        f"• السياق الهندسي: {custom_intro}\n"
        "• عمود عدد التكرارات (Column J - Occurrences): عدد وقائع النزاع أو الشكاوى أو مذكرات التأخير المسجلة رسمياً خلال كل أسبوع تعاقدي.\n"
        "• عمود الاحتمالية النسبية (Column K - Relative Likelihood): النسبة المئوية للمشكلة في ذلك الأسبوع مقارنة بإجمالي الوقائع المسجلة خلال الربع السنوي (J/Total).\n"
        "• خلية التشتت الإحصائي (Cell K15 - AVEDEV): حساب متوسط الانحراف المطلق (Average Absolute Deviation). رياضياً: الرقم ده بيقيس مدى تذبذب واستقرار معدل حدوث المشكلة أسبوعياً، وبيشكل مدخل معامل الاحتمالية (Likelihood L) في التقييم النهائي."
    )
    ws_curr.merge_cells(start_row=r_box+1, start_column=1, end_row=r_box+2, end_column=11)
    c_b = ws_curr.cell(r_box+1, 1, text_content)
    c_b.font = font_text_ar
    c_b.fill = fill_light_blue
    c_b.border = thick_border_blue
    c_b.alignment = align_right_wrap
    ws_curr.row_dimensions[r_box+1].height = 70
    print(f"Updated in-sheet explanation: {s_name}")

# ==============================================================================
# 4. IN-SHEET EXPLANATIONS FOR "Weibull" RELIABILITY SHEETS
# ==============================================================================
weibull_sheets_eng = [
    ("Weibull(Payment & Privity)", "النمذجة الرياضية لموثوقية دورة الصرف ومخاطر السيولة لمقاولي الباطن"),
    ("Weibull(Cost Inflation)", "النمذجة الرياضية لموثوقية التكاليف وحساسية المشروعات لتقلبات التضخم"),
    ("Weibull(Water & Lagoon)", "النمذجة الرياضية لاحتمالات تعطل سلاسل إمداد ومعدات البحيرات ومحطات MEP"),
    ("Weibull(Labor & Strife)", "النمذجة الرياضية لمعدل تكرار الاضطرابات العمالية وتوقفات الموقع")
]

for s_name, title_box in weibull_sheets_eng:
    ws_curr = wb[s_name]
    ws_curr.sheet_view.rightToLeft = True
    r_box = 30
    
    ws_curr.cell(r_box, 2, f"📐 دليل المهندس لتحليل نتائج ومؤشرات وايبول الإحصائية ({title_box}):").font = font_sec_title
    
    w_text = (
        "1. التحويل الخطي لمخطط وايبول (Linearized Plot X & Y):\n"
        "   - تم تحويل دالة التوزيع التراكمي إلى معادلة خط مستقيم (Y = ln(C) مقابل X = ln(ln(1/(1-F)))) لتمكين استخراج الميل ونقطة التقاطع عبر دوال SLOPE و INTERCEPT.\n"
        "2. معامل الشكل ومعدل الإخفاق (Weibull Slope α = 1/SLOPE):\n"
        "   - القيمة المحسوبة (α > 1) تؤكد هندسياً أن الخطر يمر بمرحلة 'الإخفاق المتسارع الناتج عن التقادم والضغط المستمر' (Wear-out failure rate). تراكم مستحقات المقاولين أو تأخر التوريد بيزيد من احتمالية توقف الأعمال بمعدل تصاعدي وليس عشوائياً.\n"
        "3. معامل القياس المميز (Scale Parameter β = EXP(INTERCEPT)):\n"
        "   - يمثل التردد المعتاد الذي يصل عنده الخطر لاحتمالية تراكمية تبلغ 63.2%.\n"
        "4. الاحتمالية التراكمية عند متوسط التشغيل (Weibull CDF p):\n"
        "   - النسبة المئوية الدقيقة لاحتمالية تحقق الخطر عند وصول المشروع لمتوسط تردد الحوادث الأسبوعي (Mean M11)، وتستخدم كمدخل أساسي لحساب درجة الخطر الكلية (Probability p).\n"
        "5. حدود الضبط والتحكم الإحصائي (Action Limit @ 99% Confidence):\n"
        "   - محسوبة وفق مبادئ الإحصاء الهندسي (μ + Z * σ / √N). إذا سجل أي أسبوع عدداً من الوقائع يتجاوز حد الإجراء (Action Limit)، فإن النظام يعتبر في حالة 'شذوذ تشغيلي حرج' (Process Out of Control) يفرض رفع تقرير عاجل للإدارة التنفيذية."
    )
    ws_curr.merge_cells(start_row=r_box+1, start_column=2, end_row=r_box+3, end_column=13)
    c_w = ws_curr.cell(r_box+1, 2, w_text)
    c_w.font = font_text_ar
    c_w.fill = fill_light_amber
    c_w.border = thick_border_amber
    c_w.alignment = align_right_wrap
    ws_curr.row_dimensions[r_box+1].height = 115
    print(f"Updated in-sheet explanation: {s_name}")

# ==============================================================================
# 5. IN-SHEET EXPLANATIONS FOR "Risk score" SHEET
# ==============================================================================
ws_sc = wb["Risk score"]
ws_sc.sheet_view.rightToLeft = True
r_sc = 14

ws_sc.cell(r_sc, 2, "🏆 التقرير التنفيذي لمهندس إدارة المشروعات (Executive Project Controls Summary):").font = font_title_ar

sc_text = (
    "• الغرض من المصفوفة التنفيذية:\n"
    "  دمج القياس الإحصائي لموثوقية العمليات (Weibull CDF Probability p) مع درجة التشتت التشغيلي في الموقع (Likelihood L) لإنتاج مؤشر كمي موحد (Risk Score = p × L) يدعم اتخاذ القرار وتوجيه بنود ميزانية الطوارئ (Contingency Reserves) نحو البنود الأشد خطورة.\n\n"
    "• التقييم الهندسي والتعاقدي لنتائج الترتيب (Risk Ranking Analysis):\n"
    "  🥇 الخطر رقم 1 (Rank 1) — تأخير المستخلصات ودورة الصرف (Payment & Privity Shield):\n"
    "  سجل أعلى درجة خطورة مركبة نظراً للجمع بين احتمالية وايبول التراكمية المرتفعة وتذبذب فترات التدقيق عبر 7 بوابات حصر. التوصية الهندسية: إلزام المطور بمهلة اعتماد لا تتجاوز 45 يوماً، وتحديد سقف زمني لأوراق الدفع.\n"
    "  🥈 الخطر رقم 2 (Rank 2) — تضخم الأسعار وفصل التوريد عن المصنعيات (Cost Inflation & Material Decoupling):\n"
    "  يأتي ثانياً نظراً لتعرض مقاولي الباطن لقفزات تضخم الأجور في عقود المصنعيات المقطوعة. التوصية: إدراج معادلات تعديل أسعار تعاقدية مرتبطة بنشرات وزارة الإسكان.\n"
    "  🥉 الخطر رقم 3 (Rank 3) — مكون الأعمال الكهروميكانيكية والبحيرات (Water & Lagoon MEP Infrastructure):\n"
    "  خطر تذبذب العملة والتوريدات المستوردة. التوصية: التحوط ضد تقلبات العملة وزيادة نسبة التجميع والتصنيع المحلي (على غرار شراكة شندلر Schindler JV).\n"
    "  🎖️ الخطر رقم 4 (Rank 4) — علاقات العمل والاضطرابات الموقعية (Labor Strife):\n"
    "  خطر تشغيلي موقعي يُعالج بانتظام تدفقات الرواتب وإنشاء حساب وسيط (Labor Escrow) لحماية استقرار الأعمال بالموقع."
)
ws_sc.merge_cells(start_row=r_sc+1, start_column=2, end_row=r_sc+3, end_column=6)
c_sc = ws_sc.cell(r_sc+1, 2, sc_text)
c_sc.font = font_text_ar
c_sc.fill = fill_light_green
c_sc.border = Border(left=Side(style='medium', color="16A34A"), right=thin_side, top=thin_side, bottom=thin_side)
c_sc.alignment = align_right_wrap
ws_sc.row_dimensions[r_sc+1].height = 145
print("Updated in-sheet explanation: Risk score")

# Save workbook
wb.save(file_path)
print(f"\nWorkbook successfully updated with Senior Engineering Explanations:\n{file_path}")
print(f"File size: {os.path.getsize(file_path)} bytes")
