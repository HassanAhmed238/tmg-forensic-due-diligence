# -*- coding: utf-8 -*-
"""
Inject Comprehensive Child-Friendly & Plain-Arabic Explanations into:
F:\Mr Hesham\TMG\TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx

Adds:
1. Brand New First Sheet: "دليل المبتدئين والأطفال" (Beginner & Child Guide to Risk Analysis)
   Explaining the entire philosophy like building with LEGO blocks, the purpose of each page, and how to read the numbers.
2. In-Sheet Explanatory Panels at the bottom of EVERY sheet:
   - Risk Brainstorming: "إيه لازمة الصفحة دي؟"
   - Risk Assesment sheets: "إزاي تقرأ كشكول الملاحظات ده ببساطة؟"
   - Weibull sheets: "مين عم وايبول ده وبيعمل إيه بالمعادلات دي؟" (شرح ألفا، بيتا، والخط الأحمر للإنذار)
   - Risk score: "لوحة الشرف للأشرار.. مين أكتر وحش لازم نخاف منه ونحله فوراً؟"
"""

import sys, os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"F:\Mr Hesham\TMG\TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx"
print(f"Opening workbook: {file_path}")
wb = openpyxl.load_workbook(file_path, data_only=False)

# Styling
font_title_ar = Font(name="Cairo", size=14, bold=True, color="1E3A8A")
font_sec_title = Font(name="Cairo", size=11.5, bold=True, color="0284C7")
font_head_box = Font(name="Cairo", size=10.5, bold=True, color="FFFFFF")
font_text_ar = Font(name="Cairo", size=10, color="1E293B")
font_text_bold = Font(name="Cairo", size=10, bold=True, color="0F172A")
font_note_ar = Font(name="Cairo", size=9.5, italic=True, color="475569")
font_highlight_box = Font(name="Cairo", size=10, bold=True, color="D97706")

fill_navy = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
fill_cyan = PatternFill(start_color="0284C7", end_color="0284C7", fill_type="solid")
fill_light_blue = PatternFill(start_color="F0F9FF", end_color="F0F9FF", fill_type="solid")
fill_light_amber = PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid")
fill_light_rose = PatternFill(start_color="FFF1F2", end_color="FFF1F2", fill_type="solid")
fill_light_green = PatternFill(start_color="F0FDF4", end_color="F0FDF4", fill_type="solid")

thin_side = Side(style='thin', color="CBD5E1")
card_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
thick_border_blue = Border(left=Side(style='medium', color="0284C7"), right=thin_side, top=thin_side, bottom=thin_side)
thick_border_amber = Border(left=Side(style='medium', color="D97706"), right=thin_side, top=thin_side, bottom=thin_side)

align_right_wrap = Alignment(horizontal="right", vertical="center", wrap_text=True)
align_center_wrap = Alignment(horizontal="center", vertical="center", wrap_text=True)

# ==============================================================================
# 1. CREATE FRONT SHEET: "دليل المبتدئين (اقرأني أولاً)"
# ==============================================================================
guide_sheet_title = "دليل الشرح المبسط (اقرأني أولاً)"
if guide_sheet_title in wb.sheetnames:
    wb.remove(wb[guide_sheet_title])

ws_guide = wb.create_sheet(title=guide_sheet_title, index=0)
ws_guide.views.sheetView[0].showGridLines = True
ws_guide.sheet_view.rightToLeft = True

# Main Banner
ws_guide.merge_cells("A1:G1")
b1 = ws_guide.cell(1, 1, "🏰 كيف تفهم هذا الملف كأنك تشاهد قصة مصورة لبناء مدينة من المكعبات؟ (دليل المبتدئين والأطفال)")
b1.font = font_title_ar
b1.alignment = align_center_wrap
b1.fill = PatternFill(start_color="E0F2FE", end_color="E0F2FE", fill_type="solid")
ws_guide.row_dimensions[1].height = 40

intro_paragraphs = [
    (
        "💡 الفكرة ببساطة شديدة:",
        "تخيل إننا بنبني مع بعض مدينة ألعاب عملاقة جداً (زي مدينتي، أو مشروع نور، أو ساوث ميد على البحر). وجايبين أصحابنا المقاولين يساعدونا: حد بيجيب الرمل والحديد، وحد بيبني البيوت، وحد بيعمل البحيرات الجميلة. الملف ده اتعمل علشان يجاوب على سؤال واحد بس: (إيه المشاكل اللي ممكن تحصل وتبوظ اللعبة؟ ومين أكبر مشكلة لازم نحلها فوراً قبل ما توقف البنا كله؟).",
        fill_light_blue,
        font_sec_title
    ),
    (
        "📑 خريطة المشي داخل صفحات الملف (4 خطوات سحرية):",
        "1) صفحة العصف الذهني (Risk Brainstorming): ورقة بنقعد نكتب فيها كل الحاجات اللي بتخوفنا قبل ما نبدأ اللعب.\n"
        "2) صفحات التقييم الأسبوعي (Risk Assesment): كشكول درجات بنعد فيه كل أسبوع: حصلت كام خناقة أو مشكلة في الموقع؟\n"
        "3) صفحات عم وايبول (Weibull): آلة حاسبة ذكية جداً بتشوف الأرقام وتقولنا: المشكلة دي هتفرقع تاني إمتى؟ وهل بتكبر ولا بتصغر؟\n"
        "4) لوحة الشرف للأشرار (Risk score): النتيجة النهائية اللي بترتب المشاكل من المركز الأول (أخطر وحش) للمركز الأخير.",
        fill_light_amber,
        font_highlight_box
    ),
    (
        "🧙‍♂️ مين هو 'عم وايبول' (Weibull) وليه الكل بيحبه في الرياضيات؟",
        "وايبول ده عالم رياضيات عبقري، فكر وقال: لو في لعبة أو مكنة بتبوظ كل شوية، يا ترى في طريقة نعرف بيها إمتى هتعطل المرة الجاية قبل ما تعطل فعلاً؟ وعمل معادلة بتطلع لنا 3 أسرار:\n"
        "• معامل ألفا (α - الميل): بيقولنا هل المشكلة بتكبر وتتوحش مع الوقت؟ (لو أكبر من 1 يبقى المشكلة بتزيد وبتتراكم ومش بتتحل لوحدها!).\n"
        "• معامل بيتا (β - القياس): بيقولنا في العادي وبالمتوسط، المشكلة دي بتتكرر كل كام مرة؟\n"
        "• الاحتمال (p - النسبة المئوية): بيقولنا فرصة إن المشكلة تحصل الأسبوع الجاي كام في المية؟ (لو 88% يبقى اجهز المشكلة جاية جاية!).\n"
        "• الخط الأحمر للإنذار (Action Limit 99%): دي صفارة الإنذار، لو عدد المشاكل في أي أسبوع زاد عن الرقم ده، المدير لازم يسيب فنجان القهوة ويجري يحل فوراً!",
        fill_light_rose,
        Font(name="Cairo", size=11, bold=True, color="DC2626")
    ),
    (
        "🏆 مين هم الأشرار الأربعة بتوع طلعت مصطفى في الملف ده؟",
        "🥇 المركز الأول (أخطر مشكلة): تأخير صرف الفلوس للمقاولين والشيكات المؤجلة (أوراق الدفع تتجاوز 15.79 مليار جنيه) لأنها بتعطل شغل الناس وبتوقف الموقع.\n"
        "🥈 المركز الثاني: غلاء الأسعار والدولار (الحديد والأسمنت والمضخات سعرها بيعلى بسرعة).\n"
        "🥉 المركز الثالث: معدات ومضخات البحيرات الصناعية (107 كم بحيرات) لأن قطع غيارها بتيجي من برة بالعملة الصعبة.\n"
        "🎖️ المركز الرابع: مشاكل العمالة وتأخر الأجور بالموقع.",
        fill_light_green,
        Font(name="Cairo", size=11, bold=True, color="16A34A")
    )
]

r_curr = 3
for title, text, bg_fill, title_font in intro_paragraphs:
    ws_guide.merge_cells(start_row=r_curr, start_column=1, end_row=r_curr, end_column=7)
    c_t = ws_guide.cell(r_curr, 1, title)
    c_t.font = title_font
    c_t.fill = bg_fill
    c_t.border = card_border
    c_t.alignment = align_right_wrap
    ws_guide.row_dimensions[r_curr].height = 28

    ws_guide.merge_cells(start_row=r_curr+1, start_column=1, end_row=r_curr+1, end_column=7)
    c_b = ws_guide.cell(r_curr+1, 1, text)
    c_b.font = font_text_ar
    c_b.fill = bg_fill
    c_b.border = card_border
    c_b.alignment = align_right_wrap
    
    # Calculate row height based on text length
    lines_count = text.count('\n') + (len(text) // 90) + 1
    ws_guide.row_dimensions[r_curr+1].height = max(55, lines_count * 20)
    
    r_curr += 3

ws_guide.column_dimensions["A"].width = 14
ws_guide.column_dimensions["B"].width = 14
ws_guide.column_dimensions["C"].width = 16
ws_guide.column_dimensions["D"].width = 18
ws_guide.column_dimensions["E"].width = 18
ws_guide.column_dimensions["F"].width = 18
ws_guide.column_dimensions["G"].width = 18

print("Created Sheet: دليل الشرح المبسط (اقرأني أولاً)")

# ==============================================================================
# 2. IN-SHEET EXPLANATIONS FOR "Risk Brainstorming"
# ==============================================================================
ws_b = wb["Risk Brainstorming"]
ws_b.sheet_view.rightToLeft = True
start_r = 9

ws_b.cell(start_r, 1, "💡 كبسولة الشرح المبسط للأطفال وغير المتخصصين (إيه لازمة الصفحة دي؟):").font = font_title_ar
start_r += 1

b_expl_text = (
    "• الصفحة دي زي ما تقعد مع إخواتك قبل ما تبنوا قصر الرمل على الشاطئ، وتسألهم: (الموجة ممكن تيجي منين وتهده؟).\n"
    "• العمود الأول والتاني: مين الفريق المسؤول عن الحتة دي؟ (فريق الفلوس، فريق الحفر، ولا فريق المهندسين؟).\n"
    "• العمود التالت والرابع: إيه الوحش أو المشكلة اللي ممكن تظهر؟ (مثلاً: الفلوس تتأخر، أو الأسمنت يغلى فجأة، أو العمال يتعبوا ومايجوش).\n"
    "• العمود الخامس والسادس: إحنا كنا بنعمل إيه غلط وبنحل إزاي زمان؟ وإيه الطريقة الذكية الجديدة اللي لازم نتبعها عشان نحمي قصر المكعبات بتاعنا ومايتكسرش أبداً!"
)
ws_b.merge_cells(start_row=start_r, start_column=1, end_row=start_r+1, end_column=6)
c_expl = ws_b.cell(start_r, 1, b_expl_text)
c_expl.font = font_text_ar
c_expl.fill = fill_light_amber
c_expl.border = thick_border_amber
c_expl.alignment = align_right_wrap
ws_b.row_dimensions[start_r].height = 80
print("Added in-sheet explanation to: Risk Brainstorming")

# ==============================================================================
# 3. IN-SHEET EXPLANATIONS FOR "Risk Assesment" SHEETS
# ==============================================================================
assess_sheets = [
    ("Risk Assesment(Payment&Privity)", "كشكول مراقبة تأخير الفلوس والشيكات (Payment & Privity)", "هنا بنسجل كل أسبوع: كام مقاول زعل وقدم شكوى علشان مستحقاته أو شيكاته اتأخرت في طلعت مصطفى؟"),
    ("Risk Assesment(Cost Inflation)", "كشكول مراقبة غلاء الأسعار والحديد والأسمنت (Cost Inflation)", "هنا بنعد كل أسبوع: كام مرة جالنا طلب فرق سعر للحديد أو أجور العمالة بسبب زيادة التضخم؟"),
    ("Risk Assesment(Water & Lagoon)", "كشكول مراقبة بحيرات ومضخات المية (Water & Lagoon MEP)", "هنا بنعد كل أسبوع: كام مرة طلمبة مية أو فلتر بحيرة اتأخر في الاستيراد من برة مصر بالدولار؟"),
    ("Risk Assesment(Labor & Strife)", "كشكول مراقبة العمالة والموقع (Labor Strife)", "هنا بنعد كل أسبوع: كام شكوى عمالية أو توقف عن الشغل حصل في الموقع بسبب الرواتب أو الإقامة؟")
]

for s_name, title_box, custom_intro in assess_sheets:
    ws_curr = wb[s_name]
    ws_curr.sheet_view.rightToLeft = True
    r_box = 17
    
    ws_curr.cell(r_box, 1, f"👶 الشرح المبسط للأطفال: {title_box}").font = font_sec_title
    
    text_content = (
        f"• {custom_intro}\n"
        "• العمود (J - Number of occurrences): ده عدد المرات اللي المشكلة ظهرت فيها في الأسبوع ده (يعني في الأسبوع التاني مثلاً ظهرت 12 مرة!).\n"
        "• العمود (K - Likelihood): ده بيقولنا: المشكلة دي بتمثل كام في المية من إجمالي المشاكل اللي حصلت في التلات شهور؟\n"
        "• المربع الأصفر في الأسفل (Total & Likelihood): بيحسب المجموع، وبيطلع رقم اسمه التشتت المتوسط (AVEDEV) وده معناه: (هل المشاكل بتحصل بانتظام ولا بتنطط وتفاجئنا أسبوع بعد أسبوع؟)."
    )
    ws_curr.merge_cells(start_row=r_box+1, start_column=1, end_row=r_box+2, end_column=11)
    c_b = ws_curr.cell(r_box+1, 1, text_content)
    c_b.font = font_text_ar
    c_b.fill = fill_light_blue
    c_b.border = thick_border_blue
    c_b.alignment = align_right_wrap
    ws_curr.row_dimensions[r_box+1].height = 80
    print(f"Added in-sheet explanation to: {s_name}")

# ==============================================================================
# 4. IN-SHEET EXPLANATIONS FOR "Weibull" RELIABILITY SHEETS
# ==============================================================================
weibull_sheets = [
    ("Weibull(Payment & Privity)", "سر معادلات وايبول لمستخلصات وفلوس المقاولين"),
    ("Weibull(Cost Inflation)", "سر معادلات وايبول لغلاء أسعار الحديد ومواد البناء"),
    ("Weibull(Water & Lagoon)", "سر معادلات وايبول لطلمبات البحيرات والمعدات المستوردة"),
    ("Weibull(Labor & Strife)", "سر معادلات وايبول لإضرابات العمالة ومشاكل المواقع")
]

for s_name, title_box in weibull_sheets:
    ws_curr = wb[s_name]
    ws_curr.sheet_view.rightToLeft = True
    r_box = 30
    
    ws_curr.cell(r_box, 2, f"🔬 إزاي تفهم الصفحة دي كأنك مهندس شاطر بيفك مكعبات اللعبة؟ ({title_box})").font = font_sec_title
    
    w_text = (
        "1) الترتيب (Rank) والأعمدة X و Y: دي خطوات بنرتب بيها الأسابيع من الأصغر للأكبر عشان نحطها على رسم بياني زي خط مستقيم.\n"
        "2) معامل ألفا (α - Weibull Slope): لو الرقم ده أكبر من 1 (مثلاً 2.0 أو 2.6)، ده معناه إن المشكلة (بتكبر وتتوحش مع الوقت) والناس بتزعل أكتر لو ماحلينهاش بدري!\n"
        "3) معامل بيتا (β - Scale Parameter): ده العمر الافتراضي أو الوقت المعتاد اللي كل ما يعدي لازم المشكلة تظهر فيه.\n"
        "4) نسبة وايبول التراكمية (Weibull CDF): دي الإجابة على السؤال الذهبي: (فرصة إن المشكلة دي تحصل الأسبوع الجاي كام في المية؟) وبتطلع نسبة مئوية عالية زي 80% أو 88%.\n"
        "5) حد الإنذار الأحمر (Action Limit 99%): ده الرقم اللي لو تخطيناه في أي أسبوع، يبقى دخلنا في مرحلة الخطر الشديد ولازم الإدارة تتدخل فوراً!"
    )
    ws_curr.merge_cells(start_row=r_box+1, start_column=2, end_row=r_box+3, end_column=13)
    c_w = ws_curr.cell(r_box+1, 2, w_text)
    c_w.font = font_text_ar
    c_w.fill = fill_light_amber
    c_w.border = thick_border_amber
    c_w.alignment = align_right_wrap
    ws_curr.row_dimensions[r_box+1].height = 95
    print(f"Added in-sheet explanation to: {s_name}")

# ==============================================================================
# 5. IN-SHEET EXPLANATIONS FOR "Risk score" SHEET
# ==============================================================================
ws_sc = wb["Risk score"]
ws_sc.sheet_view.rightToLeft = True
r_sc = 14

ws_sc.cell(r_sc, 2, "🏆 لوحة الشرف للأشرار (شرح النتيجة النهائية للأطفال والمديرين):").font = font_title_ar

sc_text = (
    "• الجدول ده بيجمع كل الأرقام اللي في الشيتات التانية عشان يجاوب على أهم سؤال في الشركة:\n"
    "  (لو عندنا مليون جنيه ومجهود واحد بس.. نحطه في حل أنهي مشكلة الأول؟).\n\n"
    "• معادلة التقييم البسيطة: حجم الخطر = (فرصة إن المشكلة تحصل) × (درجة التكرار واللخبطة اللي بتعملها)\n"
    "  Risk Score = Probability (p) × Likelihood (L)\n\n"
    "• ترتيب المشاكل بالأولويات:\n"
    "  🥇 المركز الأول (Rank 1): تأخير صرف الفلوس وأوراق الدفع للمقاولين (Risk Payment & Privity) - لأنها السبب الحقيقي وراء توقف الأعمال ومقاضاة المقاولين.\n"
    "  🥈 المركز الثاني (Rank 2): تضخم أسعار البناء وفرق العملة (Cost Inflation) - لأن الحديد والأسمنت بيشفطوا سيولة ضخمة لو مش متحوطين ليهم.\n"
    "  🥉 المركز الثالث (Rank 3): محطات ومعدات البحيرات الصناعية (Water & Lagoon MEP) - لأن استيرادها بالدولار بيعمل فجوة زمنية.\n"
    "  🎖️ المركز الرابع (Rank 4): علاقات العمل واحتجاجات الموقع (Labor Strife) - وبتتحل بصرف أجور العمالة بانتظام وبحساب وسيط."
)
ws_sc.merge_cells(start_row=r_sc+1, start_column=2, end_row=r_sc+3, end_column=6)
c_sc = ws_sc.cell(r_sc+1, 2, sc_text)
c_sc.font = font_text_ar
c_sc.fill = fill_light_green
c_sc.border = Border(left=Side(style='medium', color="16A34A"), right=thin_side, top=thin_side, bottom=thin_side)
c_sc.alignment = align_right_wrap
ws_sc.row_dimensions[r_sc+1].height = 135
print("Added in-sheet explanation to: Risk score")

# Save workbook
wb.save(file_path)
print(f"\nWorkbook successfully updated with child-friendly & executive explanations:\n{file_path}")
print(f"File size: {os.path.getsize(file_path)} bytes")
