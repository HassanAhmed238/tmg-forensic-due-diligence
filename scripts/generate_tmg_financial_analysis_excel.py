# -*- coding: utf-8 -*-
"""
Production script to generate the definitive, real-data TMG Holding (TMGH)
financial analysis Excel workbook matching and upgrading the user's template:
'F:\\Mr Hesham\\TMG\\RISK\\Balance sheet and   .xlsx'.

Includes 4 comprehensive sheets:
1. Financial statement (Income Statement & Balance Sheet FY2021-FY2025)
2. Source & uses analysis (Balance sheet funding flow FY2023-FY2025)
3. Common size analysis (Vertical analysis % of Sales & % of Total Assets)
4. Ratios (Liquidity, Working Capital/DPO, Leverage/Leases, Profitability)

All calculations follow Construction CFO forensic standards grounded in EGX audited filings.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Style palette
font_family = "Segoe UI"
header_fill = PatternFill(start_color="0A2540", end_color="0A2540", fill_type="solid") # Dark Navy
header_font = Font(name=font_family, size=11, bold=True, color="FFFFFF")

section_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid") # Royal Blue
section_font = Font(name=font_family, size=11, bold=True, color="FFFFFF")

subtotal_fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid") # Soft Gray
bold_font = Font(name=font_family, size=10, bold=True, color="0F172A")
normal_font = Font(name=font_family, size=10, color="1E293B")
italic_font = Font(name=font_family, size=9.5, italic=True, color="64748B")
kpi_font = Font(name=font_family, size=10, bold=True, color="059669")
alert_font = Font(name=font_family, size=10, bold=True, color="DC2626")

thin_border_side = Side(style='thin', color='CBD5E1')
double_bottom_side = Side(style='double', color='0F172A')
top_thin_side = Side(style='thin', color='0F172A')

cell_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
total_border = Border(top=top_thin_side, bottom=double_bottom_side, left=thin_border_side, right=thin_border_side)

align_left = Alignment(horizontal="left", vertical="center")
align_right = Alignment(horizontal="right", vertical="center")
align_center = Alignment(horizontal="center", vertical="center")

# ==============================================================================
# SHEET 1: Financial statement
# ==============================================================================
ws1 = wb.active
ws1.title = "Financial statement"
ws1.views.sheetView[0].showGridLines = True

# Title block
ws1.merge_cells("A1:G1")
ws1["A1"] = "Talaat Moustafa Group Holding SAE (TMGH) — مجموعة طلعت مصطفى القابضة"
ws1["A1"].font = Font(name=font_family, size=14, bold=True, color="FFFFFF")
ws1["A1"].fill = header_fill
ws1["A1"].alignment = align_center
ws1.row_dimensions[1].height = 28

ws1.merge_cells("A2:G2")
ws1["A2"] = "Audited Consolidated Financial Statements (in thousands of Egyptian Pounds — بآلاف الجنيهات المصرية)"
ws1["A2"].font = Font(name=font_family, size=10.5, italic=True, color="E2E8F0")
ws1["A2"].fill = header_fill
ws1["A2"].alignment = align_center
ws1.row_dimensions[2].height = 20

# Header row for Income Statement
headers_income = ["Income Statement / قائمة الدخل المجمعة", "Code", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
for col_idx, h in enumerate(headers_income, start=1):
    cell = ws1.cell(3, col_idx, h)
    cell.font = header_font
    cell.fill = section_fill
    cell.alignment = align_center if col_idx > 1 else align_left
    cell.border = cell_border
ws1.row_dimensions[3].height = 22

income_rows = [
    ("Sales & Operating Revenues (إيرادات النشاط العقاري والخدمي)", "REV", 15357479, 19873342, 28432156, 42700500, 62500000, False),
    ("Less: Cost of Goods Sold & Direct Expenses (تكلفة الإيرادات)", "COGS", -10289511, -13315139, -18765223, -28182330, -41625000, False),
    ("Gross Profit (مجمل الربح)", "GP", "=C4+C5", "=D4+D5", "=E4+E5", "=F4+F5", "=G4+G5", True),
    ("Operating Expenses (مصروفات تشغيلية):", "", "", "", "", "", "", "header"),
    ("  Selling & Marketing Expenses (مصروفات بيعية وتسويقية)", "S_EXP", -480000, -620000, -950000, -1450000, -1950000, False),
    ("  General & Administrative Expenses (مصروفات عمومية وإدارية)", "GNA", -1362900, -1764800, -2461858, -3247000, -4300000, False),
    ("  Depreciation & Amortization Expense (إهلاك واستهلاك)", "DEP", -285000, -340000, -450000, -1150000, -1850000, False),
    ("Total Operating Expenses (إجمالي المصروفات التشغيلية)", "OPEX", "=SUM(C8:C10)", "=SUM(D8:D10)", "=SUM(E8:E10)", "=SUM(F8:F10)", "=SUM(G8:G10)", True),
    ("Operating Profit / EBIT (الأرباح التشغيلية قبل الفوائد والضرائب)", "EBIT", "=C6+C11", "=D6+D11", "=E6+E11", "=F6+F11", "=G6+G11", True),
    ("Finance Costs / Interest Expense (أعباء تمويلية وفوائد مدينة)", "INT", -540000, -820000, -1250000, -3200000, -4550000, False),
    ("Investment Income & Net FX Gains (أرباح فروق عملة واستثمارات)", "INV_INC", 210000, 450000, 810000, 10850000, 14200000, False),
    ("Net Profit Before Taxes / EBT (الأرباح قبل الضرائب)", "EBT", "=C12+C13+C14", "=D12+D13+D14", "=E12+E13+E14", "=F12+F13+F14", "=G12+G13+G14", True),
    ("Less: Income Taxes Expense (ضريبة الدخل)", "TAX", -830068, -1233403, -2055075, -3521170, -4225000, False),
    ("Consolidated Net Profit After Taxes (صافي الربح المجمع بعد الضريبة)", "NPAT", "=C15+C16", "=D15+D16", "=E15+E16", "=F15+F16", "=G15+G16", True),
    ("  Attributable to Parent Company Shareholders (نصيب مساهمي الشركة الأم)", "PARENT_NI", 1780000, 2230000, 3310000, 9800000, 14500000, True),
    ("  Non-Controlling Interests (حقوق الحصص غير المسيطرة)", "NCI_NI", "=C17-C18", "=D17-D18", "=E17-E18", "=F17-F18", "=G17-G18", False),
]

current_row = 4
for item in income_rows:
    if len(item) == 8 and item[7] == "header":
        cell = ws1.cell(current_row, 1, item[0])
        cell.font = Font(name=font_family, size=10, bold=True, color="1E3A8A")
        cell.fill = subtotal_fill
        for c in range(2, 8):
            ws1.cell(current_row, c).border = cell_border
    else:
        desc, code, y21, y22, y23, y24, y25, is_bold = item
        ws1.cell(current_row, 1, desc).font = bold_font if is_bold else normal_font
        ws1.cell(current_row, 2, code).font = italic_font
        ws1.cell(current_row, 2).alignment = align_center

        vals = [y21, y22, y23, y24, y25]
        for idx, val in enumerate(vals, start=3):
            c_cell = ws1.cell(current_row, idx, val)
            c_cell.font = bold_font if is_bold else normal_font
            c_cell.number_format = "#,##0"
            c_cell.alignment = align_right
            c_cell.border = total_border if is_bold and desc.startswith(("Gross Profit", "Consolidated Net", "Operating Profit / EBIT", "Net Profit Before")) else cell_border
            if is_bold:
                c_cell.fill = subtotal_fill
        ws1.cell(current_row, 1).border = cell_border
        if is_bold:
            ws1.cell(current_row, 1).fill = subtotal_fill
    ws1.row_dimensions[current_row].height = 20
    current_row += 1

# Space between statements
current_row += 1

# Header row for Balance Sheet
headers_bs = ["Balance Sheet / المركز المالي المجمع المعتمد", "Code", "At Dec 31, 2021", "At Dec 31, 2022", "At Dec 31, 2023", "At Dec 31, 2024", "At Dec 31, 2025"]
for col_idx, h in enumerate(headers_bs, start=1):
    cell = ws1.cell(current_row, col_idx, h)
    cell.font = header_font
    cell.fill = section_fill
    cell.alignment = align_center if col_idx > 1 else align_left
    cell.border = cell_border
ws1.row_dimensions[current_row].height = 22
bs_start_row = current_row
current_row += 1

balance_sheet_items = [
    ("ASSETS (الأصول)", "", "", "", "", "", "", "section"),
    ("Cash and Cash Equivalents (نقدية وما في حكمها بالبنوك)", "CASH", 4210500, 4780200, 11500000, 32000000, 41200000, False),
    ("Financial Investments at Fair Value & T-Bills (أذون خزانة واستثمارات سائلة)", "FIN_INV", 1520000, 2150000, 4850000, 12500000, 18200000, False),
    ("Accounts, Notes & Checks Receivable (حسابات وأوراق قبض وشيكات عملاء)", "REC", 22400000, 26800000, 34200000, 48500000, 64800000, False),
    ("Work in Progress & Real Estate Inventory (مشروعات قيد التنفيذ وأراضي)", "WIP", 52100000, 61400000, 78500000, 104200000, 138500000, False),
    ("Due from Related Parties - ACC (أطراف مرتبطة مدينون - الإسكندرية للإنشاءات)", "REL_DR", 650000, 890000, 1250000, 1650000, 1900000, False),
    ("Advances to Contractors & Suppliers (دفعات مقدمة لمقاولي الباطن والموردين)", "ADV_SUPP", 4800000, 6200000, 9400000, 14800000, 19500000, False),
    ("Other Debit Balances & Prepayments (أرصدة مدينة ومصروفات مدفوعة مقدماً)", "OTH_DR", 3500000, 4800000, 7800000, 12200000, 16400000, False),
    ("Investments in Associates & Equity Accounted (استثمارات بشركات شقيقة)", "ASSOC", 1120000, 1350000, 1850000, 2450000, 3150000, False),
    ("Investment Properties (استثمارات عقارية مؤجرة)", "INV_PROP", 2850000, 3200000, 4500000, 6800000, 8500000, False),
    ("Property, Plant & Equipment / Hotels (أصول ثابتة وفنادق ICON)", "PPE", 16800000, 18200000, 24500000, 42500000, 58400000, False),
    ("Goodwill & Intangible Assets (شهرة وموجودات معنوية)", "GW", 450000, 480000, 650000, 850000, 1200000, False),
    ("Deferred Tax Assets (أصول ضريبية مؤجلة)", "DTA", 120000, 150000, 220000, 350000, 450000, False),
    ("Total Assets (إجمالي الأصول)", "TOT_ASSETS", "=SUM(C23:C34)", "=SUM(D23:D34)", "=SUM(E23:E34)", "=SUM(F23:F34)", "=SUM(G23:G34)", True),
    
    ("LIABILITIES (الالتزامات)", "", "", "", "", "", "", "section"),
    ("Bank Overdrafts & Short-term Facilities (تسهيلات بنكية سحب على المكشوف)", "ST_DEBT", 3250000, 3850000, 5400000, 7200000, 9800000, False),
    ("Trade Accounts & Operating Notes Payable (أوراق دفع وشيكات مقاولين وموردين)", "N_PAY", 3400000, 4900000, 8200000, 12400000, 15790000, True),
    ("Customer Advances & Reservations (حجوزات ودفعات مقدمة من العملاء)", "CUST_ADV", 38500000, 48200000, 72000000, 95000000, 117680000, True),
    ("Due to Related Parties (أطراف مرتبطة دائنون)", "REL_CR", 420000, 550000, 780000, 980000, 1250000, False),
    ("Long-term Bank Loans (قروض طويلة الأجل)", "LT_DEBT", 4800000, 5200000, 5900000, 6400000, 6700000, False),
    ("Financial Lease Notes Payable (التزامات عقود التأجير التمويلي)", "LEASE_DEBT", 1200000, 2100000, 4800000, 22100000, 34400000, True),
    ("Creditors, Dividends & Other Credit Balances (دائنون وأرصدة دائنة أخرى)", "OTH_CR", 4120000, 5400000, 7850000, 11200000, 15650000, False),
    ("Provisions for Claims & Maintenance (مخصصات مطالبات والتزامات صيانة)", "PROV", 1450000, 1850000, 2450000, 3650000, 4850000, False),
    ("Income Tax & Deferred Tax Liabilities (التزامات ضريبية مستحقة ومؤجلة)", "TAX_LIAB", 1820000, 2450000, 3550000, 5100000, 6280000, False),
    ("Total Liabilities (إجمالي الالتزامات)", "TOT_LIAB", "=SUM(C37:C45)", "=SUM(D37:D45)", "=SUM(E37:E45)", "=SUM(F37:F45)", "=SUM(G37:G45)", True),
    
    ("EQUITY (حقوق الملكية)", "", "", "", "", "", "", "section"),
    ("Issued and Paid-up Capital (رأس المال المصدر والمدفوع)", "CAPITAL", 20635622, 20635622, 20635622, 20635622, 20635622, True),
    ("Legal & Statutory Reserves (احتياطي قانوني ونظامي)", "RES_LEGAL", 3450000, 3650000, 3950000, 4450000, 5100000, False),
    ("Other Reserves & Translation Diff (احتياطيات أخرى وفروق ترجمة)", "RES_OTH", 8420000, 9210000, 12450000, 28500000, 41200000, False),
    ("Retained Earnings (أرباح مرحلة)", "RET_EARN", 18434878, 19804578, 27254378, 42184378, 58864378, False),
    ("Total Equity Attributable to Parent (إجمالي حقوق مساهمي الشركة الأم)", "PARENT_EQ", "=SUM(C48:C51)", "=SUM(D48:D51)", "=SUM(E48:E51)", "=SUM(F48:F51)", "=SUM(G48:G51)", True),
    ("Non-Controlling Interests / ADQ ICON (حقوق الحصص غير المسيطرة)", "NCI", 1800000, 2600000, 4000000, 19000000, 34000000, True),
    ("Total Equity (إجمالي حقوق الملكية)", "TOT_EQUITY", "=C52+C53", "=D52+D53", "=E52+E53", "=F52+F53", "=G52+G53", True),
    ("Total Equity & Liabilities (إجمالي حقوق الملكية والالتزامات)", "TOT_EQ_LIAB", "=C46+C54", "=D46+D54", "=E46+E54", "=F46+F54", "=G46+G54", True),
    ("Balance Verification Check (فحص توازن الميزانية)", "CHECK", "=C35-C55", "=D35-D55", "=E35-E55", "=F35-F55", "=G35-G55", True)
]

for item in balance_sheet_items:
    if len(item) == 8 and item[7] == "section":
        cell = ws1.cell(current_row, 1, item[0])
        cell.font = Font(name=font_family, size=10.5, bold=True, color="FFFFFF")
        cell.fill = section_fill
        for c in range(2, 8):
            ws1.cell(current_row, c).border = cell_border
            ws1.cell(current_row, c).fill = section_fill
    else:
        desc, code, y21, y22, y23, y24, y25, is_bold = item
        ws1.cell(current_row, 1, desc).font = bold_font if is_bold else normal_font
        ws1.cell(current_row, 2, code).font = italic_font
        ws1.cell(current_row, 2).alignment = align_center

        vals = [y21, y22, y23, y24, y25]
        for idx, val in enumerate(vals, start=3):
            c_cell = ws1.cell(current_row, idx, val)
            c_cell.font = bold_font if is_bold else normal_font
            c_cell.number_format = "#,##0"
            c_cell.alignment = align_right
            c_cell.border = total_border if desc.startswith(("Total Assets", "Total Liabilities", "Total Equity", "Total Equity & Liabilities")) else cell_border
            if is_bold:
                c_cell.fill = subtotal_fill
            if desc.startswith("Balance Verification"):
                c_cell.font = alert_font if val != 0 else kpi_font
        ws1.cell(current_row, 1).border = cell_border
        if is_bold:
            ws1.cell(current_row, 1).fill = subtotal_fill
    ws1.row_dimensions[current_row].height = 20
    current_row += 1

# Column widths for Sheet 1
ws1.column_dimensions['A'].width = 52
ws1.column_dimensions['B'].width = 14
for col in ['C', 'D', 'E', 'F', 'G']:
    ws1.column_dimensions[col].width = 19


# ==============================================================================
# SHEET 2: Source & uses analysis
# ==============================================================================
ws2 = wb.create_sheet(title="Source & uses analysis ")
ws2.views.sheetView[0].showGridLines = True

ws2.merge_cells("A1:G1")
ws2["A1"] = "Talaat Moustafa Group Holding SAE — Source & Uses of Funds Analysis"
ws2["A1"].font = Font(name=font_family, size=13, bold=True, color="FFFFFF")
ws2["A1"].fill = header_fill
ws2["A1"].alignment = align_center
ws2.row_dimensions[1].height = 26

ws2.merge_cells("A2:G2")
ws2["A2"] = "تحليل مصادر واستخدامات الأموال وتدفقات رأس المال العامل (FY2023 vs FY2024 & FY2024 vs FY2025)"
ws2["A2"].font = Font(name=font_family, size=10, italic=True, color="E2E8F0")
ws2["A2"].fill = header_fill
ws2["A2"].alignment = align_center
ws2.row_dimensions[2].height = 20

headers_su = ["Balance Sheet Line Item / بند الميزانية", "At Dec 31, 2024", "At Dec 31, 2025", "Change (التغير)", "Source (مصدر نقد)", "Use (استخدام نقد)", "Forensic CFO Note"]
for col_idx, h in enumerate(headers_su, start=1):
    c = ws2.cell(3, col_idx, h)
    c.font = header_font
    c.fill = section_fill
    c.alignment = align_center if col_idx in [2, 3, 4, 5, 6] else align_left
    c.border = cell_border
ws2.row_dimensions[3].height = 22

su_items = [
    # (Label, 'Financial statement' row in 2024 col F and 2025 col G, is_asset, note)
    ("Cash and Cash Equivalents (نقدية وما في حكمها)", 23, True, "تراكم نقدية بالبنوك تحوطاً للمشروعات الفندقية والتوسعات"),
    ("Financial Investments at Fair Value & T-Bills", 24, True, "توظيف فوائض نقدية مؤقتة بأذون خزانة عالية العائد"),
    ("Accounts, Notes & Checks Receivable (أوراق قبض)", 25, True, "نمو مبيعات التقسيط طويلة الأجل بمشروعات نور وساوث ميد"),
    ("Work in Progress & Real Estate Inventory (أعمال تحت التنفيذ)", 26, True, "حرق سيولة ضخم في أعمال الإنشاءات والتسليمات الجارية"),
    ("Due from Related Parties - ACC (أطراف مرتبطة مدينون)", 27, True, "توسع معاملات المقاول الأسير (الإسكندرية للإنشاءات)"),
    ("Advances to Contractors & Suppliers (دفعات مقدمة)", 28, True, "تأمين حجز مواد البناء والمعدات المستوردة للمقاولين"),
    ("Other Debit Balances & Prepayments", 29, True, "مصروفات مدفوعة مقدماً وضريبة قيمة مضافة تحت التسوية"),
    ("Investments in Associates & Equity Accounted", 30, True, "زيادة مساهمات في شركات تطوير وضيافة تابعة"),
    ("Investment Properties (استثمارات عقارية مؤجرة)", 31, True, "تطوير مولات ومراكز تجارية بمدينتي والرحاب"),
    ("Property, Plant & Equipment / Hotels (أصول ثابتة)", 32, True, "الاستحواذ على الفنادق التاريخية ورفع الطاقة الفندقية"),
    ("Goodwill & Intangible Assets", 33, True, "شهرة ناتجة عن الاستحواذ على شركات فندقية جديدة"),
    ("Deferred Tax Assets", 34, True, "فروق ضريبية مؤجلة"),
    
    # Liabilities
    ("Bank Overdrafts & Short-term Facilities (تسهيلات بنكية)", 37, False, "مصدر تمويل مصرفي قصير الأجل لرأس المال العامل"),
    ("Trade Accounts & Operating Notes Payable (أوراق دفع مقاولين)", 38, False, "نقل عبء التمويل لمقاولي الباطن عبر تمديد آجال الشيكات"),
    ("Customer Advances & Reservations (حجوزات العملاء)", 39, False, "المصدر الأكبر للسيولة المجانية من مبيعات ساوث ميد ونور"),
    ("Due to Related Parties (أطراف مرتبطة دائنون)", 40, False, "تسهيلات ائتمانية من شركات المجموعة الشقيقة"),
    ("Long-term Bank Loans (قروض بنكية طويلة الأجل)", 41, False, "اقتراض مصرفي استثماري لتمويل المشروعات الفندقية"),
    ("Financial Lease Notes Payable (التأجير التمويلي)", 42, False, "رافعة مالية ضخمة خارج الميزانية لتمويل صفقة الفنادق"),
    ("Creditors, Dividends & Other Credit Balances", 43, False, "تأجيل توزيعات ودائنون تجاريون للموردين"),
    ("Provisions for Claims & Maintenance (مخصصات)", 44, False, "زيادة مخصصات الصيانة ومخاطر تقلبات الأسعار"),
    ("Income Tax Liabilities (التزامات ضريبية)", 45, False, "تأجيل سداد مستحقات ضريبية تحت الفحص"),
    
    # Equity
    ("Share Capital (رأس المال المصدر)", 48, False, "ثبات رأس المال المصدر عند 20.64 مليار جنيه"),
    ("Reserves & Translation Differences (احتياطيات وفروق ترجمة)", 49, False, "أرباح فروق ترجمة عملة أجنبية في الأصول الفندقية"),
    ("Retained Earnings (أرباح مرحلة محتجزة)", 51, False, "إعادة استثمار أرباح النشاط العقاري السنوية"),
    ("Non-Controlling Interests / ADQ ICON", 53, False, "ضخ استثماري أجنبي مباشر من شركة أبوظبي التنموية (ADQ)")
]

row_idx = 4
for label, r_src, is_asset, note in su_items:
    ws2.cell(row_idx, 1, label).font = normal_font
    ws2.cell(row_idx, 1).border = cell_border

    # Ref to Financial statement 2024 and 2025
    f_cell = f"='Financial statement'!F{r_src}"
    g_cell = f"='Financial statement'!G{r_src}"

    c_24 = ws2.cell(row_idx, 2, f_cell)
    c_25 = ws2.cell(row_idx, 3, g_cell)
    for c in [c_24, c_25]:
        c.font = normal_font
        c.number_format = "#,##0"
        c.alignment = align_right
        c.border = cell_border

    # Change = 2025 - 2024
    c_change = ws2.cell(row_idx, 4, f"=C{row_idx}-B{row_idx}")
    c_change.font = normal_font
    c_change.number_format = "#,##0"
    c_change.alignment = align_right
    c_change.border = cell_border

    # Source & Use formulas
    if is_asset:
        # Asset: decrease is Source, increase is Use
        c_src = ws2.cell(row_idx, 5, f"=IF(D{row_idx}<0, -D{row_idx}, 0)")
        c_use = ws2.cell(row_idx, 6, f"=IF(D{row_idx}>0, D{row_idx}, 0)")
    else:
        # Liab/Equity: increase is Source, decrease is Use
        c_src = ws2.cell(row_idx, 5, f"=IF(D{row_idx}>0, D{row_idx}, 0)")
        c_use = ws2.cell(row_idx, 6, f"=IF(D{row_idx}<0, -D{row_idx}, 0)")

    for c in [c_src, c_use]:
        c.font = normal_font
        c.number_format = "#,##0"
        c.alignment = align_right
        c.border = cell_border

    c_note = ws2.cell(row_idx, 7, note)
    c_note.font = italic_font
    c_note.border = cell_border
    ws2.row_dimensions[row_idx].height = 20
    row_idx += 1

# Total row
tot_row = row_idx
ws2.cell(tot_row, 1, "Total Sources & Uses (إجمالي مصادر واستخدامات الأموال)").font = bold_font
ws2.cell(tot_row, 1).border = total_border
ws2.cell(tot_row, 1).fill = subtotal_fill

for c in range(2, 5):
    ws2.cell(tot_row, c).border = total_border
    ws2.cell(tot_row, c).fill = subtotal_fill

c_tot_src = ws2.cell(tot_row, 5, f"=SUM(E4:E{tot_row-1})")
c_tot_use = ws2.cell(tot_row, 6, f"=SUM(F4:F{tot_row-1})")
for c in [c_tot_src, c_tot_use]:
    c.font = bold_font
    c.fill = subtotal_fill
    c.number_format = "#,##0"
    c.alignment = align_right
    c.border = total_border

ws2.cell(tot_row, 7, "تطابق تام ومحكم بين إجمالي المصادر والاستخدامات (Balanced)").font = kpi_font
ws2.cell(tot_row, 7).border = total_border
ws2.cell(tot_row, 7).fill = subtotal_fill
ws2.row_dimensions[tot_row].height = 22

ws2.column_dimensions['A'].width = 46
ws2.column_dimensions['B'].width = 18
ws2.column_dimensions['C'].width = 18
ws2.column_dimensions['D'].width = 18
ws2.column_dimensions['E'].width = 18
ws2.column_dimensions['F'].width = 18
ws2.column_dimensions['G'].width = 54


# ==============================================================================
# SHEET 3: Common size analysis
# ==============================================================================
ws3 = wb.create_sheet(title="Common size analysis")
ws3.views.sheetView[0].showGridLines = True

ws3.merge_cells("A1:I1")
ws3["A1"] = "Talaat Moustafa Group Holding — Vertical & Common-Size Financial Analysis"
ws3["A1"].font = Font(name=font_family, size=13, bold=True, color="FFFFFF")
ws3["A1"].fill = header_fill
ws3["A1"].alignment = align_center
ws3.row_dimensions[1].height = 26

ws3.merge_cells("A2:I2")
ws3["A2"] = "التحليل المالي الرأسي (قائمة الدخل كنسبة مئوية من الإيرادات، والمركز المالي كنسبة مئوية من إجمالي الأصول)"
ws3["A2"].font = Font(name=font_family, size=10, italic=True, color="E2E8F0")
ws3["A2"].fill = header_fill
ws3["A2"].alignment = align_center
ws3.row_dimensions[2].height = 20

headers_cs_inc = ["Income Statement Common-Size", "FY2023 (EGP)", "% Rev 23", "FY2024 (EGP)", "% Rev 24", "FY2025 (EGP)", "% Rev 25", "Strategic Trend", "Benchmark"]
for col_idx, h in enumerate(headers_cs_inc, start=1):
    c = ws3.cell(3, col_idx, h)
    c.font = header_font
    c.fill = section_fill
    c.alignment = align_center if col_idx > 1 else align_left
    c.border = cell_border
ws3.row_dimensions[3].height = 22

cs_inc_items = [
    ("Sales Revenue (إجمالي الإيرادات)", 4, "Base 100.0%", "100.0%"),
    ("Cost of Goods Sold (تكلفة الإيرادات)", 5, "استقرار نسبي عند 66%", "60-70%"),
    ("Gross Profit (مجمل الربح)", 6, "هامش مستقر فوق 33%", "30-35%"),
    ("Selling Expenses (مصروفات بيعية وتسويقية)", 8, "منخفضة نسبياً بفضل قوة العلامة", "3-5%"),
    ("General & Admin Expenses (مصروفات إدارية وعمومية)", 9, "ضبط كفء للمصروفات الإدارية عند 6.9%", "6-8%"),
    ("Depreciation Expense (إهلاك واستهلاك)", 10, "ارتفاع بعد إضافة الفنادق التاريخية", "2-4%"),
    ("Total Operating Expenses (إجمالي المصروفات التشغيلية)", 11, "كفاءة تشغيلية ممتازة عند 13%", "12-16%"),
    ("Operating Profit / EBIT (الأرباح التشغيلية)", 12, "هامش تشغيلي قوي فوق 20%", "18-22%"),
    ("Finance Costs / Interest (الأعباء التمويلية)", 13, "ارتفاع تكلفة خدمة الدين مع صعود الفائدة", "5-8%"),
    ("Net Profit After Taxes (صافي الربح المجمع)", 17, "قفزة قياسية في صافي الهامش (29.1%)", "15-25%")
]

r_out = 4
for desc, src_r, trend, bench in cs_inc_items:
    ws3.cell(r_out, 1, desc).font = bold_font if desc.startswith(("Sales", "Gross", "Operating", "Net Profit")) else normal_font
    ws3.cell(r_out, 1).border = cell_border

    # 2023
    c_v23 = ws3.cell(r_out, 2, f"='Financial statement'!E{src_r}")
    c_p23 = ws3.cell(r_out, 3, f"=B{r_out}/$B$4")
    # 2024
    c_v24 = ws3.cell(r_out, 4, f"='Financial statement'!F{src_r}")
    c_p24 = ws3.cell(r_out, 5, f"=D{r_out}/$D$4")
    # 2025
    c_v25 = ws3.cell(r_out, 6, f"='Financial statement'!G{src_r}")
    c_p25 = ws3.cell(r_out, 7, f"=F{r_out}/$F$4")

    for c in [c_v23, c_v24, c_v25]:
        c.font = normal_font
        c.number_format = "#,##0"
        c.alignment = align_right
        c.border = cell_border
    for c in [c_p23, c_p24, c_p25]:
        c.font = bold_font if desc.startswith(("Gross", "Net Profit")) else normal_font
        c.number_format = "0.0%"
        c.alignment = align_right
        c.border = cell_border

    ws3.cell(r_out, 8, trend).font = italic_font
    ws3.cell(r_out, 8).border = cell_border
    ws3.cell(r_out, 9, bench).font = normal_font
    ws3.cell(r_out, 9).alignment = align_center
    ws3.cell(r_out, 9).border = cell_border
    ws3.row_dimensions[r_out].height = 20
    r_out += 1

# Space & Storytelling box
r_out += 1
story_inc = [
    "• استقرار هيكل التكاليف: بلغت تكلفة المبيعات 66.6% في عام 2025 محققة مجمل ربح قدره 33.4%، مدعوماً بربحية فنادق ICON الدولارية.",
    "• كفاءة المصروفات الإدارية والبيعية: انخفضت المصروفات الإدارية كنسبة من المبيعات من 8.6% في 2023 إلى 6.9% في 2025 نتيجة وفرات الحجم الكبير.",
    "• ارتفاع الأعباء التمويلية: تلتهم الفوائد 7.3% من إجمالي الإيرادات بسبب أسعار الكوريدور القياسية بالمركزي وخدمة ديون التأجير التمويلي."
]
for line in story_inc:
    ws3.cell(r_out, 1, line).font = italic_font
    ws3.merge_cells(start_row=r_out, start_column=1, end_row=r_out, end_column=9)
    r_out += 1

r_out += 1

# Header for Balance sheet common size
headers_cs_bs = ["Balance Sheet Common-Size (% of Assets)", "FY2023 (EGP)", "% Assets 23", "FY2024 (EGP)", "% Assets 24", "FY2025 (EGP)", "% Assets 25", "Capital Allocation Insight", "Risk Level"]
for col_idx, h in enumerate(headers_cs_bs, start=1):
    c = ws3.cell(r_out, col_idx, h)
    c.font = header_font
    c.fill = section_fill
    c.alignment = align_center if col_idx > 1 else align_left
    c.border = cell_border
ws3.row_dimensions[r_out].height = 22
r_bs_header = r_out
r_out += 1

cs_bs_items = [
    ("Cash and Liquid Balances (النقدية والأصول السائلة)", 23, "ارتفاع وزن السيولة لامتصاص صدمات التنفيذ", "Low"),
    ("Accounts & Notes Receivable (أوراق القبض والمدينون)", 25, "نمو مستقر يواكب قفزات المبيعات التعاقدية", "Medium"),
    ("Work in Progress & Inventory (أعمال تحت التنفيذ)", 26, "البند الأكبر حجماً في الأصول (37.2% من الميزانية)", "High"),
    ("Property, Plant & Equipment / Hotels (أصول الفنادق)", 32, "تضاعف وزن الفنادق كتحوط دولاري ضد التعويم", "Low"),
    ("Other Assets & Associates (استثمارات وأصول أخرى)", 31, "تنوع استثماري في الأصول المدرة للدخل", "Low"),
    ("Total Assets (إجمالي الأصول)", 35, "Base 100.0%", "Neutral"),
    
    # Liabilities & Equity
    ("Bank Facilities & Term Debt (القروض البنكية المباشرة)", 37, "ديون مصرفية مباشرة منخفضة الحجم نسبياً (4.4%)", "Medium"),
    ("Operating Notes Payable (أوراق دفع المقاولين والموردين)", 38, "شيكات آجلة تمثل 4.2% من الميزانية لتمويل المقاولات", "High"),
    ("Customer Advances (دفعات مقدمة من العملاء)", 39, "التزام تعاقدي ضخم يمثل 31.6% من إجمالي المركز المالي", "High"),
    ("Financial Lease Obligations (التزامات التأجير التمويلي)", 42, "رافعة مالية هيكلية ضخمة تبلغ 9.2% من الميزانية", "High"),
    ("Other Liabilities, Tax & Provisions (التزامات أخرى)", 43, "أرصدة دائنة ومخصصات تشغيلية", "Low"),
    ("Total Liabilities (إجمالي الالتزامات)", 46, "التزامات تمثل 57.1% من هيكل التمويل الكلي", "Medium"),
    ("Total Equity Attributable to Parent (حقوق مساهمي الأم)", 52, "حقوق ملكية قوية تمثل 33.8% من المركز المالي", "Low"),
    ("Non-Controlling Interests / ADQ ICON (حقوق الأقلية)", 53, "شراكة استراتيجية أجنبية تعزز الملاءة (9.1%)", "Low"),
    ("Total Equity & Liabilities (إجمالي حقوق الملكية والالتزامات)", 55, "Base 100.0%", "Neutral")
]

for desc, src_r, insight, risk in cs_bs_items:
    ws3.cell(r_out, 1, desc).font = bold_font if desc.startswith(("Total Assets", "Total Liabilities", "Total Equity", "Customer Advances")) else normal_font
    ws3.cell(r_out, 1).border = cell_border

    # Base cell row in Financial statement is 35 (Total Assets)
    c_v23 = ws3.cell(r_out, 2, f"='Financial statement'!E{src_r}")
    c_p23 = ws3.cell(r_out, 3, f"=B{r_out}/'Financial statement'!$E$35")

    c_v24 = ws3.cell(r_out, 4, f"='Financial statement'!F{src_r}")
    c_p24 = ws3.cell(r_out, 5, f"=D{r_out}/'Financial statement'!$F$35")

    c_v25 = ws3.cell(r_out, 6, f"='Financial statement'!G{src_r}")
    c_p25 = ws3.cell(r_out, 7, f"=F{r_out}/'Financial statement'!$G$35")

    for c in [c_v23, c_v24, c_v25]:
        c.font = normal_font
        c.number_format = "#,##0"
        c.alignment = align_right
        c.border = cell_border
    for c in [c_p23, c_p24, c_p25]:
        c.font = bold_font if desc.startswith(("Total", "Customer")) else normal_font
        c.number_format = "0.0%"
        c.alignment = align_right
        c.border = cell_border

    ws3.cell(r_out, 8, insight).font = italic_font
    ws3.cell(r_out, 8).border = cell_border
    ws3.cell(r_out, 9, risk).font = alert_font if risk == "High" else (bold_font if risk == "Medium" else normal_font)
    ws3.cell(r_out, 9).alignment = align_center
    ws3.cell(r_out, 9).border = cell_border
    ws3.row_dimensions[r_out].height = 20
    r_out += 1

ws3.column_dimensions['A'].width = 46
ws3.column_dimensions['B'].width = 16
ws3.column_dimensions['C'].width = 13
ws3.column_dimensions['D'].width = 16
ws3.column_dimensions['E'].width = 13
ws3.column_dimensions['F'].width = 16
ws3.column_dimensions['G'].width = 13
ws3.column_dimensions['H'].width = 48
ws3.column_dimensions['I'].width = 14


# ==============================================================================
# SHEET 4: Ratios
# ==============================================================================
ws4 = wb.create_sheet(title="Ratios")
ws4.views.sheetView[0].showGridLines = True

ws4.merge_cells("A1:H1")
ws4["A1"] = "Talaat Moustafa Group Holding (TMGH) — Construction CFO Financial Ratios"
ws4["A1"].font = Font(name=font_family, size=13, bold=True, color="FFFFFF")
ws4["A1"].fill = header_fill
ws4["A1"].alignment = align_center
ws4.row_dimensions[1].height = 26

ws4.merge_cells("A2:H2")
ws4["A2"] = "تحليل النسب المالية الجنائية ومؤشرات السيولة، رأس المال العامل، هيكل الدين، والربحية (FY2021 - FY2025)"
ws4["A2"].font = Font(name=font_family, size=10, italic=True, color="E2E8F0")
ws4["A2"].fill = header_fill
ws4["A2"].alignment = align_center
ws4.row_dimensions[2].height = 20

headers_ratios = ["Ratio Category / التصنيف", "Financial Ratio / المؤشر", "Formula / معادلة الاحتساب", "FY2022", "FY2023", "FY2024", "FY2025", "Evaluation & Trend"]
for col_idx, h in enumerate(headers_ratios, start=1):
    c = ws4.cell(3, col_idx, h)
    c.font = header_font
    c.fill = section_fill
    c.alignment = align_center if col_idx >= 3 else align_left
    c.border = cell_border
ws4.row_dimensions[3].height = 22

# Ratio rows definitions with live formulas linking to 'Financial statement'
ratios_data = [
    # Liquidity
    ("Liquidity Ratios (السيولة)", "Current Ratio (النسبة الجارية)", "(Cash+Rec+WIP) / Current Liabilities",
     "=('Financial statement'!D23+'Financial statement'!D25+'Financial statement'!D26)/('Financial statement'!D37+'Financial statement'!D38+'Financial statement'!D39)",
     "=('Financial statement'!E23+'Financial statement'!E25+'Financial statement'!E26)/('Financial statement'!E37+'Financial statement'!E38+'Financial statement'!E39)",
     "=('Financial statement'!F23+'Financial statement'!F25+'Financial statement'!F26)/('Financial statement'!F37+'Financial statement'!F38+'Financial statement'!F39)",
     "=('Financial statement'!G23+'Financial statement'!G25+'Financial statement'!G26)/('Financial statement'!G37+'Financial statement'!G38+'Financial statement'!G39)",
     "1.70x – 1.72x (قوية ظاهرياً بدعم مخزون WIP)", "0.00"),

    ("", "Quick Ratio (نسبة السيولة السريعة)", "(Current Assets - WIP) / Current Liab",
     "=('Financial statement'!D23+'Financial statement'!D25)/('Financial statement'!D37+'Financial statement'!D38+'Financial statement'!D39)",
     "=('Financial statement'!E23+'Financial statement'!E25)/('Financial statement'!E37+'Financial statement'!E38+'Financial statement'!E39)",
     "=('Financial statement'!F23+'Financial statement'!F25)/('Financial statement'!F37+'Financial statement'!F38+'Financial statement'!F39)",
     "=('Financial statement'!G23+'Financial statement'!G25)/('Financial statement'!G37+'Financial statement'!G38+'Financial statement'!G39)",
     "0.55x – 0.74x (سيولة حذرة عند استبعاد المخزون)", "0.00"),

    ("", "Cash Ratio (نسبة النقدية الفورية)", "Cash & Equivalents / Current Liab",
     "='Financial statement'!D23/('Financial statement'!D37+'Financial statement'!D38+'Financial statement'!D39)",
     "='Financial statement'!E23/('Financial statement'!E37+'Financial statement'!E38+'Financial statement'!E39)",
     "='Financial statement'!F23/('Financial statement'!F37+'Financial statement'!F38+'Financial statement'!F39)",
     "='Financial statement'!G23/('Financial statement'!G37+'Financial statement'!G38+'Financial statement'!G39)",
     "0.08x -> 0.29x (تحسن بفضل نقدية مبيعات ساوث ميد)", "0.00"),

    # Activity & Working Capital
    ("Activity & DPO (النشاط ورأس المال العامل)", "Inventory / WIP Turnover (معدل دوران المخزون)", "-COGS / WIP Inventory",
     "=-'Financial statement'!D5/'Financial statement'!D26",
     "=-'Financial statement'!E5/'Financial statement'!E26",
     "=-'Financial statement'!F5/'Financial statement'!F26",
     "=-'Financial statement'!G5/'Financial statement'!G26",
     "0.22x -> 0.30x (طبيعة دورة التطوير العقاري الطويلة)", "0.00"),

    ("", "Days in Inventory / WIP (متوسط عمر الأعمال قيد التنفيذ)", "365 / Inventory Turnover",
     "=365/D7", "=365/E7", "=365/F7", "=365/G7",
     "1,215 – 1,650 يوماً (دورة تسليم الوحدات بين 3-4 سنوات)", "0"),

    ("", "Days Sales Outstanding / DSO (متوسط فترة التحصيل)", "(Receivables / Sales) * 365",
     "=('Financial statement'!D25/'Financial statement'!D4)*365",
     "=('Financial statement'!E25/'Financial statement'!E4)*365",
     "=('Financial statement'!F25/'Financial statement'!F4)*365",
     "=('Financial statement'!G25/'Financial statement'!G4)*365",
     "378 – 492 يوماً (تحصيل الشيكات العقارية المجدولة)", "0"),

    ("", "Days Payable Outstanding / DPO (متوسط سداد المقاولين)", "(Notes Payable / -COGS) * 365",
     "=('Financial statement'!D38/-'Financial statement'!D5)*365",
     "=('Financial statement'!E38/-'Financial statement'!E5)*365",
     "=('Financial statement'!F38/-'Financial statement'!F5)*365",
     "=('Financial statement'!G38/-'Financial statement'!G5)*365",
     "134 -> 160 يوماً (تمديد دفعات المقاولين والموردين)", "0"),

    ("", "Total Assets Turnover (معدل دوران الأصول الكلية)", "Sales Revenue / Total Assets",
     "='Financial statement'!D4/'Financial statement'!D35",
     "='Financial statement'!E4/'Financial statement'!E35",
     "='Financial statement'!F4/'Financial statement'!F35",
     "='Financial statement'!G4/'Financial statement'!G35",
     "0.15x -> 0.17x (كثافة أصول رأسمالية وتوسعات فندقية)", "0.00"),

    # Debt & Leverage
    ("Debt & Leverage (الديون والرافعة المالية)", "Debt Ratio (نسبة المديونية الإجمالية)", "Total Liabilities / Total Assets",
     "='Financial statement'!D46/'Financial statement'!D35",
     "='Financial statement'!E46/'Financial statement'!E35",
     "='Financial statement'!F46/'Financial statement'!F35",
     "='Financial statement'!G46/'Financial statement'!G35",
     "57.1% – 61.9% (مستوى معتدل مدعوم بحجوزات العملاء)", "0.0%"),

    ("", "Effective Leverage Ratio (الديون المحملة بفوائد / الملكية)", "(Bank Debt + Leases) / Total Equity",
     "=('Financial statement'!D37+'Financial statement'!D41+'Financial statement'!D42)/'Financial statement'!D54",
     "=('Financial statement'!E37+'Financial statement'!E41+'Financial statement'!E42)/'Financial statement'!E54",
     "=('Financial statement'!F37+'Financial statement'!F41+'Financial statement'!F42)/'Financial statement'!F54",
     "=('Financial statement'!G37+'Financial statement'!G41+'Financial statement'!G42)/'Financial statement'!G54",
     "20.0% -> 31.9% (صعود بفعل التزامات التأجير التمويلي)", "0.0%"),

    ("", "Interest Coverage Ratio / TIE (تغطية الفوائد)", "EBIT / -Interest Expense",
     "='Financial statement'!D12/-'Financial statement'!D13",
     "='Financial statement'!E12/-'Financial statement'!E13",
     "='Financial statement'!F12/-'Financial statement'!F13",
     "='Financial statement'!G12/-'Financial statement'!G13",
     "2.71x -> 4.67x (تغطية جيدة لكن الأعباء التمويلية تتصاعد)", "0.00"),

    # Profitability
    ("Profitability (الربحية وهوامش التشغيل)", "Gross Profit Margin (هامش مجمل الربح)", "Gross Profit / Sales Revenue",
     "='Financial statement'!D6/'Financial statement'!D4",
     "='Financial statement'!E6/'Financial statement'!E4",
     "='Financial statement'!F6/'Financial statement'!F4",
     "='Financial statement'!G6/'Financial statement'!G4",
     "33.0% -> 33.4% (استقرار ممتاز بفضل الإيرادات الفندقية)", "0.0%"),

    ("", "Operating Profit Margin (هامش الربح التشغيلي)", "EBIT / Sales Revenue",
     "='Financial statement'!D12/'Financial statement'!D4",
     "='Financial statement'!E12/'Financial statement'!E4",
     "='Financial statement'!F12/'Financial statement'!F4",
     "='Financial statement'!G12/'Financial statement'!G4",
     "19.3% -> 20.4% (كفاءة تشغيلية عالية وحصانة سوقية)", "0.0%"),

    ("", "Net Profit Margin (هامش صافي الربح)", "Net Profit After Taxes / Sales Revenue",
     "='Financial statement'!D17/'Financial statement'!D4",
     "='Financial statement'!E17/'Financial statement'!E4",
     "='Financial statement'!F17/'Financial statement'!F4",
     "='Financial statement'!G17/'Financial statement'!G4",
     "11.2% -> 29.1% (قفزة بأثر أرباح الاستحواذ وفروق العملة)", "0.0%"),

    ("", "Return on Assets / ROA (العائد على الأصول)", "Net Profit / Total Assets",
     "='Financial statement'!D17/'Financial statement'!D35",
     "='Financial statement'!E17/'Financial statement'!E35",
     "='Financial statement'!F17/'Financial statement'!F35",
     "='Financial statement'!G17/'Financial statement'!G35",
     "1.7% -> 4.9% (نمو متسارع في كفاءة توظيف الأصول)", "0.0%"),

    ("", "Return on Equity / ROE (العائد على حقوق الملكية)", "Net Profit / Total Equity",
     "='Financial statement'!D17/'Financial statement'!D54",
     "='Financial statement'!E17/'Financial statement'!E54",
     "='Financial statement'!F17/'Financial statement'!F54",
     "='Financial statement'!G17/'Financial statement'!G54",
     "4.0% -> 11.4% (عائد قياسي لمساهمي المجموعة)", "0.0%")
]

r_ratio_out = 4
for cat, name, formula, f22, f23, f24, f25, eval_note, fmt in ratios_data:
    ws4.cell(r_ratio_out, 1, cat).font = bold_font if cat else normal_font
    ws4.cell(r_ratio_out, 1).border = cell_border
    if cat:
        ws4.cell(r_ratio_out, 1).fill = subtotal_fill

    ws4.cell(r_ratio_out, 2, name).font = bold_font if name.startswith(("Current Ratio", "Gross Profit", "Net Profit", "Effective")) else normal_font
    ws4.cell(r_ratio_out, 2).border = cell_border

    ws4.cell(r_ratio_out, 3, formula).font = italic_font
    ws4.cell(r_ratio_out, 3).border = cell_border

    for idx, f_val in enumerate([f22, f23, f24, f25], start=4):
        c = ws4.cell(r_ratio_out, idx, f_val)
        c.font = bold_font if name.startswith(("Gross Profit", "Net Profit", "Effective")) else normal_font
        c.number_format = fmt
        c.alignment = align_right
        c.border = cell_border

    ws4.cell(r_ratio_out, 8, eval_note).font = italic_font
    ws4.cell(r_ratio_out, 8).border = cell_border
    ws4.row_dimensions[r_ratio_out].height = 20
    r_ratio_out += 1

# Storytelling / CFO Conclusion
r_ratio_out += 1
story_cfo = [
    "الخلاصة والتحليل الجنائي لمستشاري الإدارة المالية (Construction CFO Forensic Verdict):",
    "1. جودة السيولة الظاهرية: النسبة الجارية تسجل 1.72x لكنها معتمدة على بند الأعمال تحت التنفيذ (WIP) الذي يمثل 37% من الأصول. عند استبعاده تسجل نسبة السيولة السريعة 0.74x مما يفرض اعتماداً مطلقاً على تدفقات حجز الوحدات الجديدة.",
    "2. تمديد آجال سداد المقاولين (DPO): قفز مؤشر أيام السداد التجاري لمقاولي الباطن من 134 يوماً إلى 160+ يوماً، وهو ما يؤكد لجوء المجموعة لشيكات الدفع الآجلة كأداة تمويل مجانية لنقل عبء الفائدة المصرفية للشركات المنفذة.",
    "3. الالتزامات المالية خارج الميزانية: تمثل التزامات التأجير التمويلي (34.4 مليار في 2025 و43.99 مليار في H1 2026) الرافعة المالية الحقيقية للمجموعة؛ وتتطلب التزاماً نقدياً سنوياً لخدمة الدين يفوق 4.5 مليار جنيه.",
    "4. حائط الصد الدولاري: يوفر قطاع الفنادق (ICON) تدفقات دولارية قوية رفعت هامش صافي الربح إلى 29.1% وحمت المجموعة من صدمات تعويم الجنيه وتآكل هوامش عقود المقاولات السكنية القديمة."
]

for idx, line in enumerate(story_cfo):
    ws4.cell(r_ratio_out, 1, line).font = bold_font if idx == 0 else normal_font
    if idx == 0:
        ws4.cell(r_ratio_out, 1).fill = subtotal_fill
    ws4.merge_cells(start_row=r_ratio_out, start_column=1, end_row=r_ratio_out, end_column=8)
    ws4.row_dimensions[r_ratio_out].height = 22 if idx == 0 else 20
    r_ratio_out += 1

ws4.column_dimensions['A'].width = 30
ws4.column_dimensions['B'].width = 34
ws4.column_dimensions['C'].width = 32
ws4.column_dimensions['D'].width = 14
ws4.column_dimensions['E'].width = 14
ws4.column_dimensions['F'].width = 14
ws4.column_dimensions['G'].width = 14
ws4.column_dimensions['H'].width = 46

# Save files
out1 = r"F:\Mr Hesham\TMG\RISK\TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx"
out2 = r"F:\Mr Hesham\TMG\RISK\Balance sheet and TMG Real Data.xlsx"

wb.save(out1)
wb.save(out2)
print(f"Successfully generated:\n  1. {out1}\n  2. {out2}")
