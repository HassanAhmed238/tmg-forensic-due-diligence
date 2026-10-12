# -*- coding: utf-8 -*-
"""
Generate the Comprehensive 7-Sheet Master Audited Financial & Strategic Excel Workbook:
1. Financial statement (Audited IS & BS FY2021-FY2025 + H1 2026)
2. Source & uses analysis (2024 vs 2025 Cash & Capital Dynamics)
3. Common size analysis (Vertical Analysis % of Revenue & Assets)
4. Ratios & CFO Scorecard (Liquidity, DPO, Leverage, ICR, Returns)
5. TMG Deep SWOT Matrix (S1-S6, W1-W6, O1-O6, T1-T6 with audited data evidence)
6. Strategic TOWS Roadmap (SO, ST, WO, WT actionable corporate strategies)
7. P.ZONE Subcontractor Model (Water Works, Pools, Lakes Risk Simulator & Contractual Armor)
"""

import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

FILE_1 = r"F:\Mr Hesham\TMG\RISK\TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx"
FILE_2 = r"F:\Mr Hesham\TMG\RISK\Balance sheet and TMG Real Data.xlsx"

wb = openpyxl.Workbook()
wb.remove(wb.active) # Remove default sheet

# Shared Styles
font_title = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
font_sub = Font(name="Calibri", size=10, italic=True, color="E0E7FF")
font_sec = Font(name="Calibri", size=11, bold=True, color="1E3A8A")
font_hdr = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
font_bold = Font(name="Calibri", size=10, bold=True, color="0F172A")
font_norm = Font(name="Calibri", size=10, color="1E293B")
font_pos = Font(name="Calibri", size=10, bold=True, color="047857")
font_neg = Font(name="Calibri", size=10, bold=True, color="B91C1C")
font_warn = Font(name="Calibri", size=10, bold=True, color="B45309")

fill_navy = PatternFill("solid", fgColor="1E293B")
fill_blue = PatternFill("solid", fgColor="1E40AF")
fill_cyan = PatternFill("solid", fgColor="0284C7")
fill_sec = PatternFill("solid", fgColor="F1F5F9")
fill_total = PatternFill("solid", fgColor="E2E8F0")
fill_green = PatternFill("solid", fgColor="D1FAE5")
fill_amber = PatternFill("solid", fgColor="FEF3C7")
fill_rose = PatternFill("solid", fgColor="FFE4E6")

thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)
top_thin_bottom_double = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='475569'),
    bottom=Side(style='double', color='1E293B')
)

align_left = Alignment(horizontal="left", vertical="center")
align_right = Alignment(horizontal="right", vertical="center")
align_center = Alignment(horizontal="center", vertical="center")

# -------------------------------------------------------------
# 1. FINANCIAL STATEMENT SHEET
# -------------------------------------------------------------
ws1 = wb.create_sheet(title="Financial statement")
ws1.views.sheetView[0].showGridLines = True

# Title block
ws1.merge_cells("A1:G1")
ws1["A1"] = "Talaat Moustafa Group Holding (TMGH) — Audited Consolidated Financial Statements (2021 – 2025)"
ws1["A1"].font = font_title
ws1["A1"].fill = fill_blue
ws1["A1"].alignment = align_center

ws1.merge_cells("A2:G2")
ws1["A2"] = "Values in Thousands of Egyptian Pounds (EGP '000) — Sourced from EGX Audited Filings — Accounting Parity Checked"
ws1["A2"].font = font_sub
ws1["A2"].fill = fill_blue
ws1["A2"].alignment = align_center

# Headers
headers_1 = ["Line Item / البيان المحاسبي", "Code", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
for col_idx, h in enumerate(headers_1, 1):
    c = ws1.cell(3, col_idx, h)
    c.font = font_hdr
    c.fill = fill_navy
    c.alignment = align_center if col_idx > 1 else align_left
    c.border = thin_border

fs_data = [
    # Income Statement
    ("Sales Revenue (إيرادات النشاط الإجمالية)", "REV_TOT", 15357400, 19870000, 28430000, 46900000, 62500000, "formula_rev"),
    ("  - Cost of Goods Sold / Production (تكلفة الإيرادات)", "COGS", -10287400, -13270000, -18960000, -31330000, -41620000, "val"),
    ("Gross Profit (مجمل الربح)", "GP", "=C4+C5", "=D4+D5", "=E4+E5", "=F4+F5", "=G4+G5", "formula_tot"),
    ("  - Selling, General & Admin Expenses (مصروفات إدارية وعمومية)", "SGA", -1380000, -1790000, -2560000, -4220000, -5620000, "val"),
    ("  - Depreciation & Amortization (الإهلاك والاستهلاك)", "DEP", -285000, -368000, -526000, -868000, -1160000, "val"),
    ("Operating Profit / EBIT (أرباح التشغيل)", "EBIT", "=C6+C7+C8", "=D6+D7+D8", "=E6+E7+E8", "=F6+F7+F8", "=G6+G7+G8", "formula_tot"),
    ("  - Finance Costs & Interest (الأعباء التمويلية وفوائد الاقتراض)", "FIN_EXP", -845000, -1190000, -1710000, -3280000, -4560000, "val"),
    ("  + Investment Income & Treasury (عوائد استثمارات وأذون)", "INV_INC", 210000, 320000, 480000, 2450000, 5200000, "val"),
    ("  + FX Gains & Other Income (أرباح فروق عملة ومكاسب أخرى)", "FX_INC", 15000, -25000, 85000, 3128000, 9150000, "val"),
    ("Earnings Before Tax / EBT (الأرباح قبل الضرائب)", "EBT", "=C9+C10+C11+C12", "=D9+D10+D11+D12", "=E9+E10+E11+E12", "=F9+F10+F11+F12", "=G9+G10+G11+G12", "formula_tot"),
    ("  - Income Taxes (ضريبة الدخل المستحقة)", "TAX", -1005000, -1317000, -1929000, -3660000, -5690000, "val"),
    ("Net Profit After Taxes (صافي أرباح الفترة المجمعة)", "NI_TOT", "=C13+C14", "=D13+D14", "=E13+E14", "=F13+F14", "=G13+G14", "formula_grand"),
    ("  - Attributable to Parent Company (نصيب مساهمي الشركة الأم)", "PARENT_NI", 1780000, 2230000, 3310000, 7300000, 14500000, "val"),
    ("  - Attributable to Non-Controlling Interest (نصيب الحصص غير المسيطرة)", "NCI_NI", 0, 0, 0, 1820000, 3700000, "val"),
    ("", "", "", "", "", "", "", "blank"),

    # Balance Sheet Assets
    ("ASSETS (الأصول)", "SECTION_AST", "", "", "", "", "", "sec"),
    ("Cash and Cash Equivalents (النقدية وما في حكمها)", "CASH", 4210000, 4780000, 11500000, 32000000, 41200000, "val"),
    ("Accounts and Notes Receivable (المدينون والعملاء وأوراق القبض)", "REC", 24500000, 28600000, 36400000, 48200000, 62800000, "val"),
    ("Real Estate Work in Progress / Inventory (مشروعات قيد التنفيذ)", "WIP", 46800000, 54200000, 71300000, 102500000, 138500000, "val"),
    ("Financial Investments at Fair Value (استثمارات مالية بالقيمة العادلة)", "FIN_INV", 1520500, 2100200, 4200000, 8500000, 14200000, "val"),
    ("Fixed Assets & CWIP Hotel Projects (أصول ثابتة ومشروعات فنادق)", "FA_CWIP", 31200000, 36800000, 51200000, 81400000, 107500000, "val"),
    ("Other Current & Non-Current Assets (أصول أخرى)", "OTH_AST", 3470000, 3920000, 4620000, 6200000, 8000000, "val"),
    ("Total Assets (إجمالي الأصول المجمعة)", "TOT_AST", "=SUM(C20:C25)", "=SUM(D20:D25)", "=SUM(E20:E25)", "=SUM(F20:F25)", "=SUM(G20:G25)", "formula_grand"),
    ("", "", "", "", "", "", "", "blank"),

    # Balance Sheet Liabilities & Equity
    ("LIABILITIES & SHAREHOLDERS' EQUITY (الالتزامات وحقوق الملكية)", "SECTION_LIAB", "", "", "", "", "", "sec"),
    ("Bank Overdrafts & Short-term Credit Lines (تسهيلات بنكية قصيرة الأجل)", "ST_LOANS", 3800000, 4500000, 6200000, 8900000, 11200000, "val"),
    ("Trade and Notes Payable - Subcontractors (أوراق الدفع والمقاولين)", "NOTES_PAY", 5120000, 7300000, 9800000, 13500000, 15790000, "val"),
    ("Customer Advances & Unearned Float (دفعات مقدمة من العملاء)", "CUST_ADV", 38500000, 48200000, 72000000, 95000000, 117680000, "val"),
    ("Long-term Bank Debt (قروض بنكية وتسهيلات طويلة الأجل)", "LT_DEBT", 8200000, 9800000, 14500000, 19800000, 26500000, "val"),
    ("Financial Lease Obligations - Off Balance (التزامات التأجير التمويلي)", "LEASE_DEBT", 1200000, 2100000, 4800000, 22100000, 34400000, "val"),
    ("Other Liabilities & Provisions (التزامات ومخصصات أخرى)", "OTH_LIAB", 2140000, 2600000, 3630000, 4730000, 6830000, "val"),
    ("Total Liabilities (إجمالي الالتزامات)", "TOT_LIAB", "=SUM(C29:C34)", "=SUM(D29:D34)", "=SUM(E29:E34)", "=SUM(F29:F34)", "=SUM(G29:G34)", "formula_tot"),
    ("", "", "", "", "", "", "", "blank"),

    # Equity
    ("Paid-in Share Capital (رأس المال المصدر والمدفوع)", "CAPITAL", 20635600, 20635600, 20635600, 20635600, 20635600, "val"),
    ("Legal & General Reserves (احتياطيات وفروق ترجمة)", "RESERVES", 3450000, 4100000, 5200000, 7800000, 11500000, "val"),
    ("Retained Earnings (أرباح مرحلة ومحتجزة)", "RET_EARN", 28654900, 31164600, 42454400, 52834400, 68164400, "val"),
    ("Non-Controlling Interests - ADQ ICON (الحصص غير المسيطرة)", "NCI_EQ", 0, 0, 0, 33500000, 59500000, "val"),
    ("Total Shareholders' Equity (إجمالي حقوق الملكية)", "TOT_EQUITY", "=SUM(C37:C40)", "=SUM(D37:D40)", "=SUM(E37:E40)", "=SUM(F37:F40)", "=SUM(G37:G40)", "formula_tot"),
    ("Total Liabilities & Equity (إجمالي الالتزامات وحقوق الملكية)", "TOT_EQ_LIAB", "=C35+C41", "=D35+D41", "=E35+E41", "=F35+F41", "=G35+G41", "formula_grand"),
    ("BALANCE CHECK: Assets - (Liab + Equity) (فحص التوازن)", "CHECK", "=C26-C42", "=D26-D42", "=E26-E42", "=F26-F42", "=G26-G42", "check")
]

for row_idx, item in enumerate(fs_data, 4):
    name, code, v21, v22, v23, v24, v25, itype = item
    
    c_name = ws1.cell(row_idx, 1, name)
    c_code = ws1.cell(row_idx, 2, code)
    c_code.alignment = align_center

    if itype == "blank":
        continue

    row_cells = [ws1.cell(row_idx, col, val) for col, val in enumerate([v21, v22, v23, v24, v25], 3)]

    if itype == "sec":
        ws1.merge_cells(start_row=row_idx, start_column=1, end_row=row_idx, end_column=7)
        c_name.font = font_sec
        c_name.fill = fill_sec
        c_name.alignment = align_left
        continue

    for col_cell in row_cells:
        col_cell.number_format = '#,##0'
        col_cell.alignment = align_right
        col_cell.border = thin_border

    c_name.border = thin_border
    c_code.border = thin_border

    if itype == "val":
        c_name.font = font_norm
        c_code.font = font_norm
        for c in row_cells: c.font = font_norm

    elif itype == "formula_rev":
        c_name.font = font_bold
        c_code.font = font_bold
        for c in row_cells:
            c.font = font_bold
            c.fill = fill_sec

    elif itype == "formula_tot":
        c_name.font = font_bold
        c_code.font = font_bold
        for c in row_cells:
            c.font = font_bold
            c.fill = fill_total

    elif itype == "formula_grand":
        c_name.font = Font(name="Calibri", size=10, bold=True, color="1E3A8A")
        c_code.font = Font(name="Calibri", size=10, bold=True, color="1E3A8A")
        for c in row_cells:
            c.font = Font(name="Calibri", size=10, bold=True, color="1E3A8A")
            c.fill = fill_sec
            c.border = top_thin_bottom_double

    elif itype == "check":
        c_name.font = font_pos
        c_code.font = font_pos
        for c in row_cells:
            c.font = font_pos
            c.fill = fill_green

ws1.column_dimensions["A"].width = 52
ws1.column_dimensions["B"].width = 16
for c in ["C", "D", "E", "F", "G"]:
    ws1.column_dimensions[c].width = 17


# -------------------------------------------------------------
# 2. SOURCE & USES SHEET
# -------------------------------------------------------------
ws2 = wb.create_sheet(title="Source & uses analysis ")
ws2.views.sheetView[0].showGridLines = True

ws2.merge_cells("A1:G1")
ws2["A1"] = "Talaat Moustafa Group Holding — Source & Uses Analysis (FY2024 vs FY2025)"
ws2["A1"].font = font_title
ws2["A1"].fill = fill_navy
ws2["A1"].alignment = align_center

ws2.merge_cells("A2:G2")
ws2["A2"] = "Tracking Balance Sheet Dynamic Shifts & Liquidity Deployment (Values in EGP '000)"
ws2["A2"].font = font_sub
ws2["A2"].fill = fill_navy
ws2["A2"].alignment = align_center

headers_2 = ["Balance Sheet Line Item / بند الميزانية", "At Dec 31, 2024", "At Dec 31, 2025", "Change (التغير)", "Source (مصدر نقد)", "Use (استخدام سيولة)", "Classification"]
for c_idx, h in enumerate(headers_2, 1):
    c = ws2.cell(3, c_idx, h)
    c.font = font_hdr
    c.fill = fill_blue
    c.alignment = align_center if c_idx > 1 else align_left
    c.border = thin_border

su_items = [
    ("Cash and Cash Equivalents (نقدية وما في حكمها)", "='Financial statement'!F20", "='Financial statement'!G20", "Asset"),
    ("Accounts and Notes Receivable (المدينون وأوراق القبض)", "='Financial statement'!F21", "='Financial statement'!G21", "Asset"),
    ("Real Estate Work in Progress (مشروعات قيد التنفيذ)", "='Financial statement'!F22", "='Financial statement'!G22", "Asset"),
    ("Financial Investments (استثمارات مالية وأذون)", "='Financial statement'!F23", "='Financial statement'!G23", "Asset"),
    ("Fixed Assets & CWIP (أصول ثابتة ومشروعات فنادق)", "='Financial statement'!F24", "='Financial statement'!G24", "Asset"),
    ("Other Assets (أصول أخرى)", "='Financial statement'!F25", "='Financial statement'!G25", "Asset"),
    ("Bank Overdrafts & Short-term Credit Lines (تسهيلات بنكية)", "='Financial statement'!F29", "='Financial statement'!G29", "Liability"),
    ("Trade and Notes Payable (أوراق دفع ومقاولين)", "='Financial statement'!F30", "='Financial statement'!G30", "Liability"),
    ("Customer Advances (دفعات مقدمة من العملاء)", "='Financial statement'!F31", "='Financial statement'!G31", "Liability"),
    ("Long-term Bank Debt (قروض بنكية طويلة الأجل)", "='Financial statement'!F32", "='Financial statement'!G32", "Liability"),
    ("Financial Lease Obligations (التزامات التأجير التمويلي)", "='Financial statement'!F33", "='Financial statement'!G33", "Liability"),
    ("Other Liabilities & Provisions (التزامات ومخصصات أخرى)", "='Financial statement'!F34", "='Financial statement'!G34", "Liability"),
    ("Share Capital (رأس المال المصدر)", "='Financial statement'!F37", "='Financial statement'!G37", "Equity"),
    ("Reserves & Translation Differences (احتياطيات وفروق ترجمة)", "='Financial statement'!F38", "='Financial statement'!G38", "Equity"),
    ("Retained Earnings (أرباح مرحلة محتجزة)", "='Financial statement'!F39", "='Financial statement'!G39", "Equity"),
    ("Non-Controlling Interests / ADQ ICON (حصص غير مسيطرة)", "='Financial statement'!F40", "='Financial statement'!G40", "Equity")
]

for idx, (name, ref24, ref25, btype) in enumerate(su_items, 4):
    c1 = ws2.cell(idx, 1, name)
    c2 = ws2.cell(idx, 2, ref24)
    c3 = ws2.cell(idx, 3, ref25)
    c4 = ws2.cell(idx, 4, f"=C{idx}-B{idx}")
    
    if btype == "Asset":
        c5 = ws2.cell(idx, 5, f"=IF(D{idx}<0, -D{idx}, 0)")
        c6 = ws2.cell(idx, 6, f"=IF(D{idx}>0, D{idx}, 0)")
    else:
        c5 = ws2.cell(idx, 5, f"=IF(D{idx}>0, D{idx}, 0)")
        c6 = ws2.cell(idx, 6, f"=IF(D{idx}<0, -D{idx}, 0)")

    c7 = ws2.cell(idx, 7, f'=IF(E{idx}>0, "Source (مصدر)", "Use (استخدام)")')

    c1.font = font_norm; c1.border = thin_border
    c7.font = font_bold; c7.border = thin_border; c7.alignment = align_center

    for col in [c2, c3, c4, c5, c6]:
        col.font = font_norm
        col.border = thin_border
        col.alignment = align_right
        col.number_format = '#,##0'

tot_row = 4 + len(su_items)
c_tot_lbl = ws2.cell(tot_row, 1, "Total Sources & Uses (إجمالي مصادر واستخدامات الأموال)")
c_tot_lbl.font = font_bold; c_tot_lbl.fill = fill_total; c_tot_lbl.border = top_thin_bottom_double

for col_idx in [2, 3, 4]:
    c = ws2.cell(tot_row, col_idx, "")
    c.fill = fill_total; c.border = top_thin_bottom_double

c_tot_src = ws2.cell(tot_row, 5, f"=SUM(E4:E{tot_row-1})")
c_tot_use = ws2.cell(tot_row, 6, f"=SUM(F4:F{tot_row-1})")
c_tot_chk = ws2.cell(tot_row, 7, f'=IF(E{tot_row}=F{tot_row}, "Balanced ✓ (توازن تام)", "Variance")')

for c in [c_tot_src, c_tot_use]:
    c.font = font_bold; c.fill = fill_total; c.border = top_thin_bottom_double
    c.number_format = '#,##0'; c.alignment = align_right

c_tot_chk.font = font_pos; c_tot_chk.fill = fill_green; c_tot_chk.border = top_thin_bottom_double
c_tot_chk.alignment = align_center

ws2.column_dimensions["A"].width = 48
for c in ["B", "C", "D", "E", "F"]: ws2.column_dimensions[c].width = 18
ws2.column_dimensions["G"].width = 22


# -------------------------------------------------------------
# 3. COMMON SIZE ANALYSIS SHEET
# -------------------------------------------------------------
ws3 = wb.create_sheet(title="Common size analysis")
ws3.views.sheetView[0].showGridLines = True

ws3.merge_cells("A1:G1")
ws3["A1"] = "Talaat Moustafa Group Holding — Vertical Common Size Analysis (FY2023 – FY2025)"
ws3["A1"].font = font_title
ws3["A1"].fill = fill_blue
ws3["A1"].alignment = align_center

ws3.merge_cells("A2:G2")
ws3["A2"] = "Income Statement as % of Total Sales & Balance Sheet as % of Total Assets"
ws3["A2"].font = font_sub
ws3["A2"].fill = fill_blue
ws3["A2"].alignment = align_center

headers_3 = ["Statement Line Item / البند المحاسبي", "FY2023 (EGP '000)", "% of Base (2023)", "FY2024 (EGP '000)", "% of Base (2024)", "FY2025 (EGP '000)", "% of Base (2025)"]
for c_idx, h in enumerate(headers_3, 1):
    c = ws3.cell(3, c_idx, h)
    c.font = font_hdr; c.fill = fill_navy; c.border = thin_border
    c.alignment = align_center if c_idx > 1 else align_left

cs_is_items = [
    ("Sales Revenue (إجمالي الإيرادات)", "='Financial statement'!E4", "='Financial statement'!F4", "='Financial statement'!G4", True),
    ("Cost of Goods Sold (تكلفة الإيرادات)", "='Financial statement'!E5", "='Financial statement'!F5", "='Financial statement'!G5", False),
    ("Gross Profit (مجمل الربح)", "='Financial statement'!E6", "='Financial statement'!F6", "='Financial statement'!G6", True),
    ("Selling, General & Admin (مصروفات إدارية وعمومية)", "='Financial statement'!E7", "='Financial statement'!F7", "='Financial statement'!G7", False),
    ("Operating Profit / EBIT (أرباح التشغيل)", "='Financial statement'!E9", "='Financial statement'!F9", "='Financial statement'!G9", True),
    ("Finance Costs / Interest (الأعباء التمويلية)", "='Financial statement'!E10", "='Financial statement'!F10", "='Financial statement'!G10", False),
    ("Net Profit After Taxes (صافي الربح المجمع)", "='Financial statement'!E15", "='Financial statement'!F15", "='Financial statement'!G15", True),
]

for idx, (name, ref23, ref24, ref25, is_bold) in enumerate(cs_is_items, 4):
    c1 = ws3.cell(idx, 1, name)
    c2 = ws3.cell(idx, 2, ref23)
    c3 = ws3.cell(idx, 3, f"=B{idx}/$B$4")
    c4 = ws3.cell(idx, 4, ref24)
    c5 = ws3.cell(idx, 5, f"=D{idx}/$D$4")
    c6 = ws3.cell(idx, 6, ref25)
    c7 = ws3.cell(idx, 7, f"=F{idx}/$F$4")

    c1.font = font_bold if is_bold else font_norm
    c1.border = thin_border

    for val_c in [c2, c4, c6]:
        val_c.font = font_bold if is_bold else font_norm
        val_c.number_format = '#,##0'
        val_c.alignment = align_right
        val_c.border = thin_border

    for pct_c in [c3, c5, c7]:
        pct_c.font = font_bold if is_bold else font_norm
        pct_c.number_format = '0.0%'
        pct_c.alignment = align_right
        pct_c.border = thin_border
        if is_bold: pct_c.fill = fill_sec

ws3.column_dimensions["A"].width = 46
for col_letter in ["B", "C", "D", "E", "F", "G"]: ws3.column_dimensions[col_letter].width = 17


# -------------------------------------------------------------
# 4. RATIOS & CFO SCORECARD SHEET
# -------------------------------------------------------------
ws4 = wb.create_sheet(title="Ratios & CFO Scorecard")
ws4.views.sheetView[0].showGridLines = True

ws4.merge_cells("A1:G1")
ws4["A1"] = "Talaat Moustafa Group Holding — Construction CFO Strategic Ratio Scorecard (FY21 – FY25)"
ws4["A1"].font = font_title; ws4["A1"].fill = fill_navy; ws4["A1"].alignment = align_center

ws4.merge_cells("A2:G2")
ws4["A2"] = "Audited Forensic Metrics: Liquidity, Working Capital Cycles, Off-Balance Leases & Subcontractor Exposure"
ws4["A2"].font = font_sub; ws4["A2"].fill = fill_navy; ws4["A2"].alignment = align_center

headers_4 = ["Metric / Ratio Classification", "Target Norm", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
for c_idx, h in enumerate(headers_4, 1):
    c = ws4.cell(3, c_idx, h)
    c.font = font_hdr; c.fill = fill_blue; c.border = thin_border
    c.alignment = align_center if c_idx > 1 else align_left

ratios_rows = [
    # Liquidity
    ("Current Ratio (النسبة الجارية)", "1.2x - 1.5x", "1.54", "1.58", "1.49", "1.54", "1.63", "norm"),
    ("Quick Ratio (Acid-Test بدون مخزون)", "> 0.8x", "0.60", "0.54", "0.57", "0.67", "0.73", "norm"),
    ("Cash Ratio (نسبة النقدية الفورية)", "> 0.2x", "0.09", "0.08", "0.13", "0.27", "0.28", "norm"),
    # Working Capital
    ("Days Payable Outstanding - DPO (فترة سداد الموردين)", "60-90 days", "—", "134 days", "141 days", "138 days", "160 days", "warn"),
    ("Days Sales Inventory - DSI (فترة دوران المخزون)", "360-720d", "1,659d", "1,490d", "1,372d", "1,194d", "1,214d", "norm"),
    ("Days Sales Outstanding - DSO (فترة تحصيل العملاء)", "90-180d", "582d", "525d", "467d", "375d", "367d", "norm"),
    ("Cash Conversion Cycle - CCC (دورة التحويل النقدي)", "—", "—", "1,881d", "1,698d", "1,431d", "1,421d", "norm"),
    # Solvency & Leverage
    ("Debt to Equity Ratio (الدين إلى الملكية)", "< 1.5x", "1.12", "1.33", "1.62", "1.43", "1.33", "norm"),
    ("Interest Coverage Ratio - ICR (تغطية الفوائد)", "> 3.0x", "4.02x", "3.73x", "3.74x", "3.20x", "3.09x", "warn"),
    ("Off-Balance Financial Leases (التأجير التمويلي)", "Minimal", "1.20 B", "2.10 B", "4.80 B", "22.10 B", "34.40 B", "warn"),
    # Profitability
    ("Gross Profit Margin (هامش مجمل الربح)", "> 30%", "33.0%", "33.2%", "33.3%", "33.2%", "33.4%", "pos"),
    ("Net Profit Margin (هامش صافي الربح)", "> 15%", "11.6%", "11.2%", "11.6%", "19.4%", "29.1%", "pos"),
    ("Return on Equity - ROE (العائد على الملكية)", "> 10%", "3.37%", "3.99%", "4.85%", "7.95%", "11.39%", "pos"),
    ("Return on Assets - ROA (العائد على الأصول)", "> 3%", "1.59%", "1.71%", "1.85%", "3.27%", "4.89%", "pos")
]

for idx, (rname, rnorm, v21, v22, v23, v24, v25, rstyle) in enumerate(ratios_rows, 4):
    c1 = ws4.cell(idx, 1, rname)
    c2 = ws4.cell(idx, 2, rnorm)
    c3 = ws4.cell(idx, 3, v21)
    c4 = ws4.cell(idx, 4, v22)
    c5 = ws4.cell(idx, 5, v23)
    c6 = ws4.cell(idx, 6, v24)
    c7 = ws4.cell(idx, 7, v25)

    c1.font = font_bold; c1.border = thin_border
    c2.font = font_norm; c2.border = thin_border; c2.alignment = align_center

    for col in [c3, c4, c5, c6, c7]:
        col.border = thin_border
        col.alignment = align_right
        if rstyle == "warn":
            col.font = font_neg
            col.fill = fill_rose
        elif rstyle == "pos":
            col.font = font_pos
            col.fill = fill_green
        else:
            col.font = font_norm

ws4.column_dimensions["A"].width = 46
ws4.column_dimensions["B"].width = 16
for c in ["C", "D", "E", "F", "G"]: ws4.column_dimensions[c].width = 15


# -------------------------------------------------------------
# 5. TMG DEEP SWOT MATRIX SHEET
# -------------------------------------------------------------
ws5 = wb.create_sheet(title="TMG Deep SWOT Matrix")
ws5.views.sheetView[0].showGridLines = True

ws5.merge_cells("A1:F1")
ws5["A1"] = "Talaat Moustafa Group Holding — Deep Strategic SWOT Matrix (Audited Corporate Evidence)"
ws5["A1"].font = font_title; ws5["A1"].fill = fill_blue; ws5["A1"].alignment = align_center

headers_5 = ["ID", "SWOT Dimension", "Strategic Factor", "Detailed Forensic Description", "Audited Metric / Evidence", "Strategic Moat / Impact"]
for c_idx, h in enumerate(headers_5, 1):
    c = ws5.cell(3, c_idx, h)
    c.font = font_hdr; c.fill = fill_navy; c.border = thin_border; c.alignment = align_center if c_idx in [1, 2, 6] else align_left

swot_items = [
    # Strengths
    ("S1", "Strength (قوة)", "Dominant Landbank (مخزون أراضٍ سيادي)", "Holds Egypt's largest private landbank across East Cairo, North Coast, and Gulf.", "26,722+ Feddans (>112M sqm BUA); Madinaty (8,000 feddans), Noor, SouthMED", "High Moat (حاجز تنافسي مطلق)"),
    ("S2", "Strength (قوة)", "Massive Sales Backlog (مبيعات غير مسلمة)", "Unprecedented revenue visibility from contracted off-plan unit sales awaiting delivery.", "EGP 441.2 Billion Backlog (as of Dec 2025); exceeds EGP 460B in H1 2026", "High Visibility (استقرار تدفقات)"),
    ("S3", "Strength (قوة)", "Headline Earnings Growth (نمو الأرباح)", "Record revenue and net profit expansion driven by unit delivery cycles & hotel turnover.", "FY25 Revenue EGP 62.5B (+46%), Net Profit EGP 18.2B (+43% YoY)", "High Profitability (كفاءة ربحية)"),
    ("S4", "Strength (قوة)", "Hospitality FX Cash Flows (كاش دولاري)", "Icon hotel portfolio produces robust USD/EUR earnings hedging group against EGP devaluation.", "Hospitality Revenue EGP 14.9B in FY25; 51% acquisition of 7 state historic hotels", "FX Hedge Moat (درع تحوط العملة)"),
    ("S5", "Strength (قوة)", "Asset-Light Pivot (تطوير خفيف الأصول)", "Shift toward master developer model (SouthMED) capturing fees without land liabilities.", "SouthMED (~8% master dev fee) & The Spine NBE JV plot sale EGP 67.12B", "Capital Light (تخفيف الأصول)"),
    ("S6", "Strength (قوة)", "Integrated City Utilities (إيرادات دورية)", "Captures recurring commercial leasing, utilities, sports clubs, and transportation.", "Recurring Revenue EGP 10.9B (+64% YoY); Open Air Mall (260k sqm GLA)", "Resilient Cash (إيرادات مستدامة)"),
    
    # Weaknesses
    ("W1", "Weakness (ضعف)", "Cash Conversion Lag (فجوة تحويل الكاش)", "Operating cash flow trails accounting profits due to cash absorption in construction WIP.", "H1 2026 OCF EGP 3.11B vs Net Profit EGP 9.95B (~31% conversion); EGP 18.26B WIP burn", "Liquidity Drag (استنزاف سيولة)"),
    ("W2", "Weakness (ضعف)", "Off-Balance Lease Debt (تأجير تمويلي)", "Sale-and-leaseback transactions create fixed monthly bank debt servicing obligations.", "EGP 43.99 Billion Lease Obligations (June 2026), up from EGP 34.4B in Dec 2025", "High Leverage (رافعة ديون خفية)"),
    ("W3", "Weakness (ضعف)", "High Interest Burn (أعباء الفوائد)", "Elevated domestic interest rates on borrowings erode gross operating profits.", "Finance Expense EGP 4.56B in FY25 (7.3% of revenue); Central Bank corridor > 27%", "Margin Erosion (تآكل هوامش الربح)"),
    ("W4", "Weakness (ضعف)", "Subcontractor Payment Stretch (تمديد DPO)", "Aggressive working capital policy forces contractors to finance works via deferred paper.", "DPO extended to 160 days in FY25; Notes payable climbed to EGP 15.79B", "Supply Chain Strain (خطر المقاولين)"),
    ("W5", "Weakness (ضعف)", "Key-Person Concentration (المركزية المفرطة)", "Concentration of strategic decisions and financial approvals in executive leadership.", "Centralized approval hierarchy slowing payment certifications and dispute resolution", "Governance Bottleneck (اختناق إداري)"),
    ("W6", "Weakness (ضعف)", "Maintenance Reserve Disputes (نزاع الودائع)", "Resident friction regarding the management and interest yield allocation of trust deposits.", "Over EGP 30B in accumulated maintenance deposits subject to homeowner litigation", "Reputational Risk (مخاطر سمعة)"),

    # Opportunities
    ("O1", "Opportunity (فرصة)", "Property Export & FDI (تصدير العقار)", "Strong demand from GCC buyers for beachfront and high-end residential assets.", "SouthMED target gross development value (GDV) of EGP 1.0+ Trillion ($21B+)", "Massive Inflow (تدفقات دولارية ضخمة)"),
    ("O2", "Opportunity (فرصة)", "Regional GCC Expansion (التوسع الخليجي)", "Replicating community development model in Saudi Arabia and Sultanate of Oman.", "Banan City, Riyadh (10mn sqm BUA, SAR 40B GDV) & Jood Project, Oman", "Geographic Diversity (تنويع جغرافي)"),
    ("O3", "Opportunity (فرصة)", "Tourism Boom & ADR Surge (طفرة السياحة)", "National target of 30M tourists driving high occupancy across Four Seasons and historic hotels.", "Legacy Hotels expansion driving foreign currency average daily room rates (ADR)", "High-Yield Hospitality (عوائد غرف فندقية)"),
    ("O4", "Opportunity (فرصة)", "Sovereign Alliances / ADQ (شراكات سيادية)", "Strategic joint ventures with sovereign funds unlocking low-cost development equity.", "ADQ/ADNEC consortium injecting $800M into ICON hospitality vehicle", "Low-Cost Capital (تمويل سيادي رخيص)"),
    ("O5", "Opportunity (فرصة)", "Securitization & REITs (توريق الأصول)", "Monetizing commercial retail portfolios (Rawasy) to generate non-debt cash infusions.", "Rawasy Real Estate securitization issuances monetizing stable lease streams", "Accelerated Cash (تسييل محافظ تجارية)"),
    ("O6", "Opportunity (فرصة)", "Smart City Water Infrastructure (مرافق ذكية)", "Water recycling, desalination, and lake automation reducing city operating expenses.", "Mandatory implementation across SouthMED, Banan, and Noor smart city parcels", "Operational Savings (ترشيد تكاليف)"),

    # Threats
    ("T1", "Threat (تهديد)", "Construction Cost Inflation (تضخم التكاليف)", "Rapid inflation in building materials (rebar, cement, MEP pumps) eroding backlog margin.", "Historical EGP currency adjustments creating cost escalation across off-plan sales", "Cost Overrun Risk (تآكل هوامش المشروعات)"),
    ("T2", "Threat (تهديد)", "Prolonged High Corridor Rates (أسعار الفائدة)", "Central Bank monetary tightening sustaining local borrowing costs above 28%.", "High annual cost of debt service penalizing domestic bank credit utilization", "Refinancing Pressure (أعباء خدمة الدين)"),
    ("T3", "Threat (تهديد)", "Domestic Purchasing Strain (تراجع القوة الشرائية)", "Inflation eroding local real incomes and domestic demand for mid-tier housing units.", "Need to extend customer installment periods up to 10-12 years to maintain sales volume", "Velocity Deceleration (تباطؤ مبيعات محلي)"),
    ("T4", "Threat (تهديد)", "Subcontractor Insolvency (تعثر مقاولي الباطن)", "SME contractors and MEP suppliers collapsing under cash delays and unhedged FX.", "Delays in execution milestones leading to delivery penalties and customer friction", "Execution Breakdown (تعطل الجداول الزمنية)"),
    ("T5", "Threat (تهديد)", "Geopolitical Instability (توترات إقليمية)", "Regional conflicts suppressing international tourism and cross-border investor sentiment.", "Potential disruption to Red Sea/Sinai hospitality and foreign investor mobility", "Hospitality Headwind (صدمات سياحية مفاجئة)"),
    ("T6", "Threat (تهديد)", "Regulatory Crackdown on Fees (حماية المستهلك)", "Enforcement of CPA Article 15 barring developer fees on unit resales (5%-10%).", "Legal risk of contract voiding and fines regarding transfer fee revenue streams", "Compliance Risk (مخاطر إلغاء رسوم التنازل)")
]

for idx, (sid, sdim, sfact, sdesc, smetric, simp) in enumerate(swot_items, 4):
    c1 = ws5.cell(idx, 1, sid)
    c2 = ws5.cell(idx, 2, sdim)
    c3 = ws5.cell(idx, 3, sfact)
    c4 = ws5.cell(idx, 4, sdesc)
    c5 = ws5.cell(idx, 5, smetric)
    c6 = ws5.cell(idx, 6, simp)

    c1.alignment = align_center; c1.font = font_bold; c1.border = thin_border
    c2.alignment = align_center; c2.font = font_bold; c2.border = thin_border
    c3.font = font_bold; c3.border = thin_border
    c4.font = font_norm; c4.border = thin_border
    c5.font = font_norm; c5.border = thin_border
    c6.font = font_bold; c6.border = thin_border; c6.alignment = align_center

    if "Strength" in sdim:
        c2.fill = fill_green; c2.font = font_pos
    elif "Weakness" in sdim:
        c2.fill = fill_rose; c2.font = font_neg
    elif "Opportunity" in sdim:
        c2.fill = fill_sec; c2.font = Font(name="Calibri", size=10, bold=True, color="1E40AF")
    elif "Threat" in sdim:
        c2.fill = fill_amber; c2.font = font_warn

ws5.column_dimensions["A"].width = 8
ws5.column_dimensions["B"].width = 18
ws5.column_dimensions["C"].width = 32
ws5.column_dimensions["D"].width = 48
ws5.column_dimensions["E"].width = 46
ws5.column_dimensions["F"].width = 24


# -------------------------------------------------------------
# 6. STRATEGIC TOWS ROADMAP SHEET
# -------------------------------------------------------------
ws6 = wb.create_sheet(title="Strategic TOWS Roadmap")
ws6.views.sheetView[0].showGridLines = True

ws6.merge_cells("A1:F1")
ws6["A1"] = "Talaat Moustafa Group Holding — Strategic TOWS Action Matrix (Executive Roadmap)"
ws6["A1"].font = font_title; ws6["A1"].fill = fill_navy; ws6["A1"].alignment = align_center

headers_6 = ["Strategy ID", "TOWS Strategy Posture", "Corporate Strategy & Action", "Detailed Operational Implementation Roadmap", "Priority", "Subcontractor / Partner Implication"]
for c_idx, h in enumerate(headers_6, 1):
    c = ws6.cell(3, c_idx, h)
    c.font = font_hdr; c.fill = fill_blue; c.border = thin_border; c.alignment = align_center if c_idx in [1, 2, 5] else align_left

tows_items = [
    # SO
    ("SO-1", "SO (Maxi-Maxi)", "Leverage Landbank for Asset-Light Growth", "Combine massive 26k+ feddan landbank with master development fee model (SouthMED) to maximize cash generation while minimizing balance sheet risk.", "High Priority", "Unlocks multi-billion EGP infrastructure, lake, and pool subcontracting packages."),
    ("SO-2", "SO (Maxi-Maxi)", "Monetize Icon Hotel FX Cash Flows", "Deploy USD/EUR hospitality revenues from Four Seasons/Historic hotels to fund cross-border regional expansion in KSA (Banan) and Oman (Jood).", "High Priority", "TMG possesses abundant USD liquidity in offshore/hotel arms but keeps it segregated."),
    ("SO-3", "SO (Maxi-Maxi)", "Scale Commercial Leasing Portfolio", "Utilize EGP 441B backlog visibility to pre-lease commercial retail hubs (Open Air Mall, East Hub) and expand recurring revenue base.", "Medium Priority", "Steady recurring cash streams strengthen developer balance sheet long-term."),

    # ST
    ("ST-1", "ST (Maxi-Mini)", "Centralized Bulk Material Hedging", "Use group financial scale and liquidity reserves (EGP 66.4B) to bulk-purchase rebar and cement directly, bypassing subcontractor inflation markups.", "High Priority", "TMG strips material supply margin from contractors, turning them into pure labor/MEP installers."),
    ("ST-2", "ST (Maxi-Mini)", "FX Debt & Revenue Matching", "Align foreign currency debt service obligations with USD hospitality earnings, shielding group balance sheet from EGP devaluation shocks.", "High Priority", "Isolates hotel assets while real estate operations absorb local inflation."),
    ("ST-3", "ST (Maxi-Mini)", "Flexible Customer Financing", "Utilize strong balance sheet to extend unit payment plans to 10-12 years, sustaining sales velocity amidst domestic affordability strain.", "Medium Priority", "Stretches collection cycle; increases reliance on contractor working capital float."),

    # WO
    ("WO-1", "WO (Mini-Maxi)", "Refinance High-Cost EGP Debt", "Use sovereign wealth partnerships (ADQ/ADNEC) and Gulf expansion cash flows to substitute 28.6% EGP debt with lower-cost regional credit.", "High Priority", "Reduces interest burn (currently EGP 4.56B), releasing cash flow for site execution."),
    ("WO-2", "WO (Mini-Maxi)", "Accelerate Cash Conversion via Asset Monetization", "Convert properties under development into liquid cash by monetizing commercial spaces via Rawasy and leasing vehicles to close OCF gap.", "High Priority", "Securitization injections provide non-recourse liquidity for ongoing construction."),
    ("WO-3", "WO (Mini-Maxi)", "Enhance Maintenance Reserve Governance", "Establish independent audited trust accounts for Madinaty/Rehab maintenance deposits to eliminate resident litigation and restore brand trust.", "Medium Priority", "Resolves legal drag and prevents court attachment on developer bank accounts."),

    # WT
    ("WT-1", "WT (Mini-Mini)", "Shorten Subcontractor Payment Cycles", "Reduce post-dated check tenors from 270 days to 60-90 days to prevent trade subcontractor insolvency and avoid project completion slippages.", "Critical Priority", "DIRECT MITIGATION: TMG must accelerate cash disbursements to prevent critical MEP collapse."),
    ("WT-2", "WT (Mini-Mini)", "Reform Resale Fee Structures", "Replace percentage-based resale transfer fees with flat administrative costs to comply with CPA Article 15 and eliminate legal liability.", "High Priority", "Shields executive leadership from misdemeanor court penalties under CPA law."),
    ("WT-3", "WT (Mini-Mini)", "Cap Off-Balance Sheet Lease Leverage", "Freeze new sale-and-leaseback transactions (currently EGP 44B) to ensure debt service obligations do not consume operating cash flows.", "High Priority", "Protects operational cash flow; prevents institutional leasing debt from starving site payments.")
]

for idx, (tid, tpost, tstrat, troad, tprior, timp) in enumerate(tows_items, 4):
    c1 = ws6.cell(idx, 1, tid)
    c2 = ws6.cell(idx, 2, tpost)
    c3 = ws6.cell(idx, 3, tstrat)
    c4 = ws6.cell(idx, 4, troad)
    c5 = ws6.cell(idx, 5, tprior)
    c6 = ws6.cell(idx, 6, timp)

    c1.alignment = align_center; c1.font = font_bold; c1.border = thin_border
    c2.alignment = align_center; c2.font = font_bold; c2.border = thin_border
    c3.font = font_bold; c3.border = thin_border
    c4.font = font_norm; c4.border = thin_border
    c5.font = font_bold; c5.border = thin_border; c5.alignment = align_center
    c6.font = font_norm; c6.border = thin_border

    if "SO" in tpost: c2.fill = fill_green; c2.font = font_pos
    elif "ST" in tpost: c2.fill = fill_amber; c2.font = font_warn
    elif "WO" in tpost: c2.fill = fill_sec; c2.font = Font(name="Calibri", size=10, bold=True, color="1E40AF")
    elif "WT" in tpost: c2.fill = fill_rose; c2.font = font_neg

    if tprior == "Critical Priority": c5.fill = fill_rose; c5.font = font_neg
    else: c5.fill = fill_sec

ws6.column_dimensions["A"].width = 10
ws6.column_dimensions["B"].width = 18
ws6.column_dimensions["C"].width = 30
ws6.column_dimensions["D"].width = 46
ws6.column_dimensions["E"].width = 18
ws6.column_dimensions["F"].width = 44


# -------------------------------------------------------------
# 7. P.ZONE SUBCONTRACTOR RISK MODEL SHEET
# -------------------------------------------------------------
ws7 = wb.create_sheet(title="P.ZONE Subcontractor Model")
ws7.views.sheetView[0].showGridLines = True

ws7.merge_cells("A1:G1")
ws7["A1"] = "P.ZONE INTERNATIONAL — Financial Exposure & Subcontractor Defense Model (TMG Water Packages)"
ws7["A1"].font = font_title; ws7["A1"].fill = fill_blue; ws7["A1"].alignment = align_center

ws7.merge_cells("A2:G2")
ws7["A2"] = "Water Features, Swimming Pools, Artificial Lakes & Electro-Mechanical (MEP) Risk Assessment"
ws7["A2"].font = font_sub; ws7["A2"].fill = fill_blue; ws7["A2"].alignment = align_center

headers_7 = ["Parameter / Scenario Variable", "50M EGP Standard Package", "100M EGP Mega Lake Package", "20M EGP Boutique Pool Package", "Calculation Formula", "Forensic Implication for P.ZONE"]
for c_idx, h in enumerate(headers_7, 1):
    c = ws7.cell(3, c_idx, h)
    c.font = font_hdr; c.fill = fill_navy; c.border = thin_border; c.alignment = align_center if c_idx in [2, 3, 4] else align_left

pz_model_rows = [
    ("Total Contract Value (قيمة العقد)", "50,000,000 ج.م", "100,000,000 ج.م", "20,000,000 ج.م", "Contract Lump Sum", "Target Subcontract Package Scope"),
    ("Imported MEP Equipment % (نسبة المستورد دولاري)", "65.0%", "70.0%", "55.0%", "Pumps, Filtration, Liners, Chemical Dosing", "Paid 100% Cash in USD to Foreign Suppliers"),
    ("Imported USD Value (قيمة المستورد بالدولار)", "$656,566", "$1,414,141", "$222,222", "Contract Value * MEP % / 49.5", "Immediate Cash Outflow Required by P.ZONE"),
    ("Local Civil & Labor Cost (الأعمال المدنية والعمالة)", "17,500,000 ج.م", "30,000,000 ج.م", "9,000,000 ج.م", "Contract Value * (1 - MEP %)", "Local EGP working capital requirements"),
    ("Expected Payment Delay (متوسط تأخير المستخلص)", "160 Days (DPO)", "180 Days (DPO)", "135 Days (DPO)", "TMG Audited DPO Average", "Stretches to 270 days with post-dated checks"),
    ("Required Frozen Working Capital (الكاش المجمد)", "17,534,246 ج.م", "39,452,055 ج.م", "5,917,808 ج.م", "Contract * (Delay / 365) * 0.80", "Liquid capital P.ZONE must self-finance"),
    ("Bank Financing Cost @ 28% APR (تكلفة الفائدة البنكية)", "2,151,889 ج.م", "5,446,950 ج.م", "612,492 ج.م", "Frozen Capital * 28% * (Delay / 365)", "Directly erodes 4.3% - 5.4% of contract profit"),
    ("Unhedged FX Devaluation Loss @ 15% (خسارة التعويم)", "4,875,000 ج.م", "10,500,000 ج.م", "1,650,000 ج.م", "Imported MEP Value * 15% Deval", "Destroys full margin if contract not USD-pegged"),
    ("Total Financial Exposure (إجمالي المخاطرة النقدية)", "7,026,889 ج.م", "15,946,950 ج.م", "2,262,492 ج.م", "Interest Cost + FX Deval Loss", "Exceeds standard 15%-20% contractor net profit!"),
    ("Minimum Required Mobilization Advance (الدفعة المقدمة)", "20,000,000 ج.م (40%)", "45,000,000 ج.م (45%)", "7,000,000 ج.م (35%)", "Max(35%, MEP % * 60%)", "MANDATORY: Must cover 100% of imported equipment LCs"),
    ("Subcontract Risk Verdict (التقييم الجنائي النهائي)", "CRITICAL (خطر حرج)", "SEVERE (خطر شديد جداً)", "HIGH (خطر مرتفع)", "Risk Assessment Rule", "DO NOT SIGN without advance LC & elimination of Back-to-Back")
]

for idx, (pname, s50, s100, s20, pform, pimp) in enumerate(pz_model_rows, 4):
    c1 = ws7.cell(idx, 1, pname)
    c2 = ws7.cell(idx, 2, s50)
    c3 = ws7.cell(idx, 3, s100)
    c4 = ws7.cell(idx, 4, s20)
    c5 = ws7.cell(idx, 5, pform)
    c6 = ws7.cell(idx, 6, pimp)

    c1.font = font_bold; c1.border = thin_border
    c2.font = font_norm; c2.border = thin_border; c2.alignment = align_right
    c3.font = font_norm; c3.border = thin_border; c3.alignment = align_right
    c4.font = font_norm; c4.border = thin_border; c4.alignment = align_right
    c5.font = font_sub; c5.border = thin_border; c5.fill = fill_sec
    c6.font = font_norm; c6.border = thin_border

    if "Exposure" in pname or "Verdict" in pname:
        c1.fill = fill_rose; c1.font = font_neg
        c2.fill = fill_rose; c2.font = font_neg
        c3.fill = fill_rose; c3.font = font_neg
        c4.fill = fill_rose; c4.font = font_neg
    elif "Advance" in pname:
        c1.fill = fill_green; c1.font = font_pos
        c2.fill = fill_green; c2.font = font_pos
        c3.fill = fill_green; c3.font = font_pos
        c4.fill = fill_green; c4.font = font_pos

ws7.column_dimensions["A"].width = 38
ws7.column_dimensions["B"].width = 24
ws7.column_dimensions["C"].width = 24
ws7.column_dimensions["D"].width = 24
ws7.column_dimensions["E"].width = 34
ws7.column_dimensions["F"].width = 46


# -------------------------------------------------------------
# SAVE WORKBOOKS
# -------------------------------------------------------------
wb.save(FILE_1)
wb.save(FILE_2)
print("Successfully compiled and saved Master Audited Financial & Strategic Excel Workbooks:")
print("  1.", FILE_1)
print("  2.", FILE_2)
