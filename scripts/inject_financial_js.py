# -*- coding: utf-8 -*-
"""
Inject the full JavaScript engine for TMG Interactive Financial Module into TMG_Forensic_Due_Diligence_Dashboard.html
"""

import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Define the complete Financial JS engine
financial_js = """
    /* ==========================================================================
       TMG FORENSIC FINANCIAL INTELLIGENCE & SLICER ENGINE
       Audited Multi-Year Datasets (FY2021 – FY2025 + H1 2026)
       ========================================================================== */
    const tmgFinData = {
      years: ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026'],
      yearsKeys: ['fy21', 'fy22', 'fy23', 'fy24', 'fy25', 'h126'],

      // Income Statement Line Items (in Thousands EGP)
      incomeStatement: [
        { id: "rev_re", cat: "rev", nameAr: "إيرادات النشاط العقاري", nameEn: "Real Estate Development Revenue", vals: [12137400, 15650000, 21600000, 32800000, 42200000, 20120000], bold: false },
        { id: "rev_hotel", cat: "rev", nameAr: "إيرادات قطاع الفنادق والضيافة (ICON)", nameEn: "Hotels & Hospitality Revenue (ICON)", vals: [1270000, 2560000, 3550000, 9800000, 14100000, 7150000], bold: false },
        { id: "rev_serv", cat: "rev", nameAr: "إيرادات الأنشطة والخدمات والمرافق", nameEn: "Services, Utilities & Facility Revenue", vals: [1950000, 1660000, 3280000, 4300000, 6200000, 2920000], bold: false },
        { id: "rev_tot", cat: "rev_tot", nameAr: "إجمالي الإيرادات المجمعة", nameEn: "Total Consolidated Revenues", vals: [15357400, 19870000, 28430000, 46900000, 62500000, 30190000], bold: true, color: "var(--accent-cyan)" },
        { id: "cogs", cat: "cost", nameAr: "تكلفة الإيرادات والإنشاءات", nameEn: "Cost of Goods Sold (COGS)", vals: [-10287400, -13270000, -18960000, -31330000, -41620000, -20050000], bold: false },
        { id: "gross_profit", cat: "gp", nameAr: "مجمل الربح (Gross Profit)", nameEn: "Gross Profit", vals: [5070000, 6600000, 9470000, 15570000, 20880000, 10140000], bold: true, color: "var(--accent-emerald)" },
        { id: "sga", cat: "exp", nameAr: "المصروفات البيعية والعمومية والإدارية", nameEn: "Selling, General & Admin (SG&A)", vals: [-1380000, -1790000, -2560000, -4220000, -5620000, -2720000], bold: false },
        { id: "deprec", cat: "exp", nameAr: "الإهلاك والاستهلاك", nameEn: "Depreciation & Amortization", vals: [-285000, -368000, -526000, -868000, -1160000, -610000], bold: false },
        { id: "ebit", cat: "op", nameAr: "أرباح التشغيل (EBIT)", nameEn: "Operating Profit (EBIT)", vals: [3405000, 4442000, 6384000, 10482000, 14100000, 6810000], bold: true, color: "var(--accent-blue)" },
        { id: "fin_cost", cat: "fin", nameAr: "الأعباء التمويلية وفوائد القروض", nameEn: "Finance Costs & Borrowing Interest", vals: [-845000, -1190000, -1710000, -3280000, -4560000, -2410000], bold: false, color: "var(--accent-rose)" },
        { id: "inv_inc", cat: "fin", nameAr: "عوائد استثمارات وأذون خزانة", nameEn: "Investment & Treasury Income", vals: [210000, 320000, 480000, 2450000, 5200000, 3120000], bold: false },
        { id: "fx_gains", cat: "fin", nameAr: "أرباح فروق العملة ومكاسب أخرى", nameEn: "FX Gains & Other Income", vals: [15000, -25000, 85000, 3128000, 9150000, 4800000], bold: false },
        { id: "ebt", cat: "pretax", nameAr: "الأرباح قبل ضرائب الدخل (EBT)", nameEn: "Earnings Before Tax (EBT)", vals: [2785000, 3547000, 5239000, 12780000, 23890000, 12320000], bold: true },
        { id: "tax", cat: "tax", nameAr: "ضريبة الدخل المستحقة", nameEn: "Income Tax Expense", vals: [-1005000, -1317000, -1929000, -3660000, -5690000, -2370000], bold: false },
        { id: "net_profit", cat: "ni_tot", nameAr: "صافي أرباح الفترة المجمعة", nameEn: "Consolidated Net Profit", vals: [1780000, 2230000, 3310000, 9120000, 18200000, 9950000], bold: true, color: "var(--accent-emerald)" },
        { id: "parent_share", cat: "ni", nameAr: "نصيب مساهمي الشركة الأم", nameEn: "Attributable to Parent Equity Holders", vals: [1780000, 2230000, 3310000, 7300000, 14500000, 7920000], bold: false },
        { id: "nci_share", cat: "ni", nameAr: "نصيب الحصص غير المسيطرة (ADQ / ICON)", nameEn: "Non-Controlling Interests Share", vals: [0, 0, 0, 1820000, 3700000, 2030000], bold: false }
      ],

      // Balance Sheet Assets (in Thousands EGP)
      assets: [
        { id: "cash", cat: "cur", nameAr: "النقدية وما في حكمها لدى البنوك", nameEn: "Cash & Cash Equivalents", vals: [4210000, 4780000, 11500000, 32000000, 41200000, 66400000], bold: true, color: "var(--accent-emerald)" },
        { id: "rec", cat: "cur", nameAr: "العملاء، المدينون، وأوراق القبض", nameEn: "Accounts & Notes Receivable", vals: [24500000, 28600000, 36400000, 48200000, 62800000, 71200000], bold: false },
        { id: "wip", cat: "cur", nameAr: "مشروعات عقارية قيد التنفيذ (WIP المخزون)", nameEn: "Real Estate Work-In-Progress (Inventory)", vals: [46800000, 54200000, 71300000, 102500000, 138500000, 154000000], bold: true, color: "var(--accent-amber)" },
        { id: "fin_inv", cat: "noncur", nameAr: "استثمارات مالية بالقيمة العادلة وأذون", nameEn: "Financial Investments & Treasury", vals: [1520500, 2100200, 4200000, 8500000, 14200000, 18500000], bold: false },
        { id: "fixed_cwip", cat: "noncur", nameAr: "أصول ثابتة ومشروعات تحت التنفيذ (فنادق)", nameEn: "Fixed Assets & Hotel Projects (CWIP)", vals: [31200000, 36800000, 51200000, 81400000, 107500000, 118200000], bold: false },
        { id: "other_ast", cat: "other", nameAr: "أصول متداولة وغير متداولة أخرى", nameEn: "Other Current & Non-Current Assets", vals: [3470000, 3920000, 4620000, 6200000, 8000000, 9100000], bold: false },
        { id: "tot_assets", cat: "tot_ast", nameAr: "إجمالي الأصول المجمعة (Total Assets)", nameEn: "Total Assets", vals: [111700500, 130400200, 179220000, 278800000, 372200000, 437400000], bold: true, color: "var(--accent-cyan)" }
      ],

      // Balance Sheet Liabilities & Equity (in Thousands EGP)
      liabilitiesEquity: [
        { id: "st_debt", cat: "cur_liab", nameAr: "سحب على المكشوف وتسهيلات بنكية قصيرة الأجل", nameEn: "Bank Overdrafts & Short-term Loans", vals: [3800000, 4500000, 6200000, 8900000, 11200000, 13800000], bold: false },
        { id: "notes_pay", cat: "cur_liab", nameAr: "أرصدة الدائنين وأوراق الدفع (الموردين والمقاولين)", nameEn: "Trade & Notes Payable (Contractors)", vals: [5120000, 7300000, 9800000, 13500000, 15790000, 18200000], bold: true, color: "var(--accent-rose)" },
        { id: "cust_adv", cat: "cur_liab", nameAr: "دفعات مقدمة من العملاء (التزامات تسليم وحدات)", nameEn: "Customer Advances & Deferred Float", vals: [38500000, 48200000, 72000000, 95000000, 117680000, 133990000], bold: true, color: "var(--accent-amber)" },
        { id: "lt_debt", cat: "noncur_liab", nameAr: "قروض بنكية وتسهيلات طويلة الأجل", nameEn: "Long-Term Bank Borrowings", vals: [8200000, 9800000, 14500000, 19800000, 26500000, 31200000], bold: false },
        { id: "lease_debts", cat: "noncur_liab", nameAr: "التزامات عقود التأجير التمويلي (فنادق ICON)", nameEn: "Financial Lease Obligations (Off-Bal)", vals: [1200000, 2100000, 4800000, 22100000, 34400000, 43990000], bold: true, color: "var(--accent-rose)" },
        { id: "other_liab", cat: "other_liab", nameAr: "التزامات ومخصصات أخرى", nameEn: "Other Liabilities & Provisions", vals: [2140000, 2600000, 3630000, 4730000, 6830000, 8100000], bold: false },
        { id: "tot_liab", cat: "tot_liab", nameAr: "إجمالي الالتزامات (Total Liabilities)", nameEn: "Total Liabilities", vals: [58960000, 74500000, 110930000, 164030000, 212400000, 249280000], bold: true },
        
        // Equity
        { id: "cap", cat: "eq", nameAr: "رأس المال المصدر والمدفوع", nameEn: "Paid-in Share Capital", vals: [20635600, 20635600, 20635600, 20635600, 20635600, 20635600], bold: false },
        { id: "res", cat: "eq", nameAr: "احتياطيات قانونية ونظامية وفروق ترجمة", nameEn: "Legal, Statutory Reserves & FX", vals: [3450000, 4100000, 5200000, 7800000, 11500000, 13200000], bold: false },
        { id: "ret_earn", cat: "eq", nameAr: "أرباح مرحلة ومحتجزة", nameEn: "Retained Earnings", vals: [28654900, 31164600, 42454400, 52834400, 68164400, 74284400], bold: false },
        { id: "nci", cat: "eq", nameAr: "حقوق الحصص غير المسيطرة (شراكة ADQ في ICON)", nameEn: "Non-Controlling Interests (ADQ / ICON)", vals: [0, 0, 0, 33500000, 59500000, 80000000], bold: true, color: "var(--accent-blue)" },
        { id: "tot_equity", cat: "tot_eq", nameAr: "إجمالي حقوق الملكية (Total Equity)", nameEn: "Total Shareholders' Equity", vals: [52740500, 55900200, 68290000, 114770000, 159800000, 188120000], bold: true, color: "var(--accent-blue)" },
        
        // Total
        { id: "tot_liab_eq", cat: "grand_tot", nameAr: "إجمالي الالتزامات وحقوق الملكية", nameEn: "Total Liabilities & Equity", vals: [111700500, 130400200, 179220000, 278800000, 372200000, 437400000], bold: true, color: "var(--accent-cyan)" },
        { id: "balance_check", cat: "check", nameAr: "فحص التوازن الحسابي (الأصول - الالتزامات والملكية)", nameEn: "Balance Check (Assets - Liab & Equity)", vals: [0, 0, 0, 0, 0, 0], bold: true, color: "var(--accent-emerald)" }
      ],

      // Sources & Uses Data (2024 vs 2025 in Thousands EGP)
      sourcesUses: [
        { nameAr: "النقدية وما في حكمها", nameEn: "Cash & Cash Equivalents", v24: 32000000, v25: 41200000, change: 9200000, source: 0, use: 9200000, type: "use" },
        { nameAr: "العملاء والمدينون وأوراق القبض", nameEn: "Receivables & Notes", v24: 48200000, v25: 62800000, change: 14600000, source: 0, use: 14600000, type: "use" },
        { nameAr: "مشروعات عقارية قيد التنفيذ (WIP)", nameEn: "Real Estate Work-In-Progress", v24: 102500000, v25: 138500000, change: 36000000, source: 0, use: 36000000, type: "use" },
        { nameAr: "استثمارات مالية بالقيمة العادلة", nameEn: "Financial Investments", v24: 8500000, v25: 14200000, change: 5700000, source: 0, use: 5700000, type: "use" },
        { nameAr: "أصول ثابتة ومشروعات فنادق (CWIP)", nameEn: "Fixed Assets & Hotel Capex", v24: 81400000, v25: 107500000, change: 26100000, source: 0, use: 26100000, type: "use" },
        { nameAr: "أصول أخرى متداولة وغير متداولة", nameEn: "Other Assets", v24: 6200000, v25: 8000000, change: 1800000, source: 0, use: 1800000, type: "use" },
        { nameAr: "سحب على المكشوف وتسهيلات بنكية", nameEn: "Bank Overdrafts & Credit Lines", v24: 8900000, v25: 11200000, change: 2300000, source: 2300000, use: 0, type: "source" },
        { nameAr: "أرصدة الدائنين وأوراق الدفع (المقاولين)", nameEn: "Trade & Notes Payable (Contractors)", v24: 13500000, v25: 15790000, change: 2290000, source: 2290000, use: 0, type: "source" },
        { nameAr: "دفعات مقدمة من العملاء (Float)", nameEn: "Customer Advances (Float)", v24: 95000000, v25: 117680000, change: 22680000, source: 22680000, use: 0, type: "source" },
        { nameAr: "قروض بنكية وتسهيلات طويلة الأجل", nameEn: "Long-Term Bank Loans", v24: 19800000, v25: 26500000, change: 6700000, source: 6700000, use: 0, type: "source" },
        { nameAr: "التزامات التأجير التمويلي (ICON)", nameEn: "Financial Lease Obligations", v24: 22100000, v25: 34400000, change: 12300000, source: 12300000, use: 0, type: "source" },
        { nameAr: "التزامات ومخصصات أخرى", nameEn: "Other Liabilities & Provisions", v24: 4730000, v25: 6830000, change: 2100000, source: 2100000, use: 0, type: "source" },
        { nameAr: "احتياطيات وفروق ترجمة العملة", nameEn: "Reserves & Translation FX", v24: 7800000, v25: 11500000, change: 3700000, source: 3700000, use: 0, type: "source" },
        { nameAr: "أرباح مرحلة ومحتجزة", nameEn: "Retained Earnings (Profits)", v24: 52834400, v25: 68164400, change: 15330000, source: 15330000, use: 0, type: "source" },
        { nameAr: "الحصص غير المسيطرة (ADQ في ICON)", nameEn: "Non-Controlling Interests (ADQ)", v24: 33500000, v25: 59500000, change: 26000000, source: 26000000, use: 0, type: "source" }
      ],

      // Common Size Data (% of Sales and % of Total Assets)
      commonSizeIS: [
        { nameAr: "إجمالي الإيرادات (Sales Revenue)", nameEn: "Total Consolidated Revenue", p23: "100.0%", p24: "100.0%", p25: "100.0%", noteAr: "سنة الأساس", noteEn: "Base 100%" },
        { nameAr: "تكلفة الإيرادات (COGS)", nameEn: "Cost of Goods Sold (COGS)", p23: "66.7%", p24: "66.8%", p25: "66.6%", noteAr: "ثبات نسبي في هامش التكلفة", noteEn: "Stable production cost margin" },
        { nameAr: "مجمل الربح (Gross Profit)", nameEn: "Gross Profit", p23: "33.3%", p24: "33.2%", p25: "33.4%", noteAr: "هامش ربح إجمالي قوي وثابت", noteEn: "Healthy gross margin (~33.4%)" },
        { nameAr: "المصروفات البيعية والعمومية (SG&A)", nameEn: "Selling, General & Admin (SG&A)", p23: "9.0%", p24: "9.0%", p25: "9.0%", noteAr: "كفاءة وانضباط مصاريف التشغيل", noteEn: "Disciplined operational ratio" },
        { nameAr: "أرباح التشغيل (EBIT)", nameEn: "Operating Profit (EBIT)", p23: "22.5%", p24: "22.3%", p25: "22.5%", noteAr: "هامش تشغيلي ممتاز", noteEn: "Strong EBIT efficiency" },
        { nameAr: "الأعباء التمويلية وفوائد القروض", nameEn: "Finance Costs & Borrowing Interest", p23: "6.0%", p24: "7.0%", p25: "7.3%", noteAr: "⚠️ صعود حاد بسبب الفائدة والتأجير", noteEn: "⚠️ Spiking interest burn (7.3%)" },
        { nameAr: "صافي الربح المجمع (Net Profit)", nameEn: "Consolidated Net Profit", p23: "11.6%", p24: "19.4%", p25: "29.1%", noteAr: "قفزة بأثر استثمارات وفنادق ICON", noteEn: "Boosted by ICON hotels & FX" }
      ],

      commonSizeBS: [
        { nameAr: "النقدية وما في حكمها", nameEn: "Cash & Cash Equivalents", p23: "6.4%", p24: "11.5%", p25: "11.1%", noteAr: "بناء سيولة وقائية لمواجهة الصدمات", noteEn: "Defensive cash buffer" },
        { nameAr: "مشروعات عقارية قيد التنفيذ (WIP)", nameEn: "Real Estate WIP (Inventory)", p23: "39.8%", p24: "36.8%", p25: "37.2%", noteAr: "أكبر مكون في الأصول (138.5 مليار)", noteEn: "Primary asset driver (138.5B)" },
        { nameAr: "أصول ثابتة وفنادق (CWIP)", nameEn: "Fixed Assets & Hotel Projects", p23: "28.6%", p24: "29.2%", p25: "28.9%", noteAr: "أصول فندقية تاريخية تدر عملة أجنبية", noteEn: "Historic hospitality assets" },
        { nameAr: "دفعات مقدمة من العملاء (Customer Float)", nameEn: "Customer Advances (Float)", p23: "40.2%", p24: "34.1%", p25: "31.6%", noteAr: "ثلث الميزانية تمويل بدون فوائد من العملاء", noteEn: "31.6% interest-free customer float" },
        { nameAr: "أوراق دفع الموردين والمقاولين", nameEn: "Trade & Notes Payable (Contractors)", p23: "5.5%", p24: "4.8%", p25: "4.2%", noteAr: "15.8 مليار جنيه تمويل عبر شيكات المقاولين", noteEn: "15.8B contractor credit line" },
        { nameAr: "التزامات عقود التأجير التمويلي", nameEn: "Financial Lease Obligations (Off-Bal)", p23: "2.7%", p24: "7.9%", p25: "9.2%", noteAr: "⚠️ رافعة ديون غير معلنة قفزت لـ 34.4 مليار", noteEn: "⚠️ Surging off-balance lease debt" },
        { nameAr: "إجمالي حقوق الملكية (Shareholders' Equity)", nameEn: "Total Shareholders' Equity", p23: "38.1%", p24: "41.2%", p25: "42.9%", noteAr: "تعزز الملكية بدخول ADQ كشريك", noteEn: "Strengthened by ADQ entry" }
      ],

      // CFO Ratios Scorecard (2021 – 2025)
      cfoRatios: [
        { cat: "liquidity", nameAr: "النسبة الجارية (Current Ratio)", nameEn: "Current Ratio", norm: "1.2x – 1.5x", r21: "1.54", r22: "1.58", r23: "1.49", r24: "1.54", r25: "1.63", status: "green", impactAr: "تغطية جيدة ظاهرياً ولكن ثلث الأصول مخزون بطيء", impactEn: "Adequate coverage but high WIP weight" },
        { cat: "liquidity", nameAr: "النسبة السريعة (Quick Ratio - بدون مخزون)", nameEn: "Quick Ratio (Excl. WIP)", norm: "> 0.8x", r21: "0.60", r22: "0.54", r23: "0.57", r24: "0.67", r25: "0.73", status: "amber", impactAr: "تحت المعيار المستهدف؛ ضغط حال تراجع المبيعات", impactEn: "Below benchmark; vulnerable if sales slow" },
        { cat: "liquidity", nameAr: "نسبة النقدية الفورية (Cash Ratio)", nameEn: "Cash Ratio", norm: "> 0.2x", r21: "0.09", r22: "0.08", r23: "0.13", r24: "0.27", r25: "0.28", status: "green", impactAr: "ارتفعت بقوة بفضل تحصيل مقدمات الحجز", impactEn: "Solid cash buffer from customer float" },
        
        { cat: "working_cap", nameAr: "فترة سداد الموردين والمقاولين (DPO)", nameEn: "Days Payable Outstanding (DPO)", norm: "60 – 90 يوماً", r21: "—", r22: "134 يوماً", r23: "141 يوماً", r24: "138 يوماً", r25: "160 يوماً", status: "red", impactAr: "⚠️ مؤشر خطر حرج لمقاولي الباطن؛ احتجاز سيولة قسري", impactEn: "⚠️ Critical subcontractor risk; cash stretched" },
        { cat: "working_cap", nameAr: "فترة دوران المخزون (DSI)", nameEn: "Days Sales of Inventory (DSI)", norm: "360 – 720 يوماً", r21: "1,659 يوماً", r22: "1,490 يوماً", r23: "1,372 يوماً", r24: "1,194 يوماً", r25: "1,214 يوماً", status: "amber", impactAr: "دورة إنشائية طويلة تمتد لـ 3-4 سنوات للتسليم", impactEn: "3-4 year execution lifecycle" },
        { cat: "working_cap", nameAr: "فترة تحصيل المدينين (DSO)", nameEn: "Days Sales Outstanding (DSO)", norm: "90 – 180 يوماً", r21: "582 يوماً", r22: "525 يوماً", r23: "467 يوماً", r24: "375 يوماً", r25: "367 يوماً", status: "amber", impactAr: "تحسن ملحوظ ولكن ما تزال أقساط العملاء ممتدة", impactEn: "Improving but long customer installment profile" },
        { cat: "working_cap", nameAr: "دورة التحويل النقدي (Cash Conversion Cycle)", nameEn: "Cash Conversion Cycle (CCC)", norm: "—", r21: "—", r22: "1,881 يوماً", r23: "1,698 يوماً", r24: "1,431 يوماً", r25: "1,421 يوماً", status: "amber", impactAr: "دورة نقدية ممتدة تمولها دفعات حجز العملاء", impactEn: "Extended cash cycle funded by customer float" },

        { cat: "leverage", nameAr: "نسبة إجمالي الدين إلى الملكية (Debt/Equity)", nameEn: "Total Debt to Equity", norm: "< 1.5x", r21: "1.12", r22: "1.33", r23: "1.62", r24: "1.43", r25: "1.33", status: "green", impactAr: "انخفضت بفضل دخول رأسمال ADQ في الفنادق", impactEn: "Diluted by ADQ equity injection" },
        { cat: "leverage", nameAr: "معدل تغطية الفوائد (Interest Coverage ICR)", nameEn: "Interest Coverage Ratio (ICR)", norm: "> 3.0x", r21: "4.02x", r22: "3.73x", r23: "3.74x", r24: "3.20x", r25: "3.09x", status: "amber", impactAr: "انخفاض تدريجي بسبب ارتفاع الفوائد لـ 4.56 مليار", impactEn: "Compressed by 4.56B interest expense" },
        { cat: "leverage", nameAr: "التزامات التأجير التمويلي خارج الميزانية", nameEn: "Off-Balance Lease Obligations", norm: "Minimal", r21: "1.20 B", r22: "2.10 B", r23: "4.80 B", r24: "22.10 B", r25: "34.40 B", status: "red", impactAr: "⚠️ رافعة ديون خفية تتطلب خدمة دين تفوق 4.5B سنوياً", impactEn: "⚠️ Massive debt service priority over contractors" },

        { cat: "profitability", nameAr: "هامش مجمل الربح (Gross Margin)", nameEn: "Gross Profit Margin", norm: "> 30%", r21: "33.0%", r22: "33.2%", r23: "33.3%", r24: "33.2%", r25: "33.4%", status: "green", impactAr: "استقرار استثنائي في تسعير الوحدات وهوامش التنفيذ", impactEn: "Remarkable stability in unit margins" },
        { cat: "profitability", nameAr: "هامش صافي الربح (Net Profit Margin)", nameEn: "Net Profit Margin", norm: "> 15%", r21: "11.6%", r22: "11.2%", r23: "11.6%", r24: "19.4%", r25: "29.1%", status: "green", impactAr: "قفزة قياسية في 2025 مدعومة بقطاع الفنادق بالدولار", impactEn: "Surge driven by FX & hotel ADRs" },
        { cat: "profitability", nameAr: "العائد على حقوق الملكية (ROE)", nameEn: "Return on Equity (ROE)", norm: "> 10%", r21: "3.37%", r22: "3.99%", r23: "4.85%", r24: "7.95%", r25: "11.39%", status: "green", impactAr: "تجاوز 11% لأول مرة بفضل أرباح صفقة الفنادق", impactEn: "Crossed 11% milestone on hotel turnaround" },
        { cat: "profitability", nameAr: "العائد على الأصول (ROA)", nameEn: "Return on Assets (ROA)", norm: "> 3%", r21: "1.59%", r22: "1.71%", r23: "1.85%", r24: "3.27%", r25: "4.89%", status: "green", impactAr: "كفاءة ربحية متصاعدة لأصول المجموعة", impactEn: "Rising asset turnover & profitability" }
      ]
    };

    // State Variables
    let finCurrentView = 'is-bs';
    let finCurrentYear = 'all';
    let finCurrentUnit = 'billions';
    let finCurrentSearch = '';
    let finStatementType = 'all'; // 'all', 'is', 'bs'

    // Chart Instances
    let chartFinTrendsDyn = null;
    let chartBSDyn = null;
    let chartDpoDyn = null;
    let chartSourcesUsesDyn = null;

    /* ==========================================================================
       VALUE FORMATTING HELPER
       ========================================================================== */
    function formatFinVal(valK, unit, isRatio=false) {
      if (isRatio) return valK;
      if (valK === 0 || valK === '0') return '0.00';
      if (typeof valK === 'string') return valK;

      if (unit === 'billions') {
        const valB = valK / 1000000;
        return (valB >= 0 ? '' : '') + valB.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' B';
      } else if (unit === 'thousands') {
        return valK.toLocaleString('en-US') + ' k';
      } else if (unit === 'usd') {
        const valUsdM = (valK / 1000) / 49.5;
        return '$' + valUsdM.toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + ' M';
      }
      return valK.toLocaleString('en-US');
    }

    /* ==========================================================================
       SLICER HANDLERS
       ========================================================================== */
    function setFinView(viewId) {
      finCurrentView = viewId;
      document.querySelectorAll('.fin-pill[data-view]').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-view') === viewId);
      });
      document.querySelectorAll('.fin-subview').forEach(p => {
        p.classList.remove('active');
      });
      const targetPane = document.getElementById('subview-' + viewId);
      if (targetPane) targetPane.classList.add('active');

      // Refresh appropriate table
      if (viewId === 'is-bs') renderFinancialStatementsTable();
      else if (viewId === 'sources-uses') renderSourcesUsesTable();
      else if (viewId === 'common-size') renderCommonSizeTable();
      else if (viewId === 'cfo-ratios') renderCfoRatiosTable();
      else if (viewId === 'guide') updateSimCalculations();
    }

    function setFinYear(yearId) {
      finCurrentYear = yearId;
      document.querySelectorAll('.fin-pill[data-year]').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-year') === yearId);
      });
      renderFinancialStatementsTable();
      updateFinancialKPIs();
    }

    function setFinUnit(unitId) {
      finCurrentUnit = unitId;
      document.querySelectorAll('.fin-pill[data-unit]').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-unit') === unitId);
      });
      renderFinancialStatementsTable();
      renderSourcesUsesTable();
      updateFinancialKPIs();
    }

    function handleFinSearch(query) {
      finCurrentSearch = query.trim().toLowerCase();
      renderFinancialStatementsTable();
      renderSourcesUsesTable();
      renderCommonSizeTable();
      renderCfoRatiosTable();
    }

    function toggleStatementType(type) {
      finStatementType = type;
      ['all', 'is', 'bs'].forEach(t => {
        const btn = document.getElementById('btn-st-' + t);
        if (btn) btn.classList.toggle('active', t === type);
      });
      renderFinancialStatementsTable();
    }

    /* ==========================================================================
       RENDER: FINANCIAL STATEMENTS TABLE (IS & BS)
       ========================================================================== */
    function renderFinancialStatementsTable() {
      const thRow = document.getElementById('fin-fs-th-row');
      const tbody = document.getElementById('fin-fs-tbody');
      if (!thRow || !tbody) return;

      const isAr = currentLang === 'ar';
      
      // Determine visible columns
      let visibleIndices = [0, 1, 2, 3, 4, 5];
      if (finCurrentYear === '2021') visibleIndices = [0];
      else if (finCurrentYear === '2022') visibleIndices = [1];
      else if (finCurrentYear === '2023') visibleIndices = [2];
      else if (finCurrentYear === '2024') visibleIndices = [3];
      else if (finCurrentYear === '2025') visibleIndices = [4];
      else if (finCurrentYear === 'h126') visibleIndices = [5];

      // Build Headers
      let headersHtml = `<th>${isAr ? 'البند المالي / البيان المحاسبي' : 'Financial Statement Line Item'}</th>`;
      visibleIndices.forEach(idx => {
        headersHtml += `<th class="num-col">${tmgFinData.years[idx]}</th>`;
      });
      headersHtml += `<th style="text-align:center;">${isAr ? 'المصدر' : 'Source'}</th>`;
      thRow.innerHTML = headersHtml;

      // Filter rows by statement type and search query
      let rowsToRender = [];

      if (finStatementType === 'all' || finStatementType === 'is') {
        rowsToRender.push({ isHeader: true, titleAr: "— قائمة الدخل المجمعة (Consolidated Income Statement) —", titleEn: "— Consolidated Income Statement —" });
        rowsToRender = rowsToRender.concat(tmgFinData.incomeStatement);
      }

      if (finStatementType === 'all' || finStatementType === 'bs') {
        rowsToRender.push({ isHeader: true, titleAr: "— قائمة المركز المالي: الأصول المجمعة (Consolidated Assets) —", titleEn: "— Consolidated Assets —" });
        rowsToRender = rowsToRender.concat(tmgFinData.assets);
        rowsToRender.push({ isHeader: true, titleAr: "— قائمة المركز المالي: الالتزامات وحقوق الملكية (Liabilities & Equity) —", titleEn: "— Consolidated Liabilities & Equity —" });
        rowsToRender = rowsToRender.concat(tmgFinData.liabilitiesEquity);
      }

      // Filter by search query
      if (finCurrentSearch) {
        rowsToRender = rowsToRender.filter(r => {
          if (r.isHeader) return true;
          const name = (isAr ? r.nameAr : r.nameEn).toLowerCase();
          return name.includes(finCurrentSearch);
        });
      }

      // Build tbody rows
      let bodyHtml = '';
      rowsToRender.forEach(r => {
        if (r.isHeader) {
          bodyHtml += `
            <tr class="row-subhead">
              <td colspan="${visibleIndices.length + 2}">${isAr ? r.titleAr : r.titleEn}</td>
            </tr>
          `;
          return;
        }

        const isTotal = r.cat.includes('tot') || r.cat === 'grand_tot' || r.cat === 'check';
        const isCheck = r.cat === 'check';
        let rowClass = isCheck ? 'row-check' : (isTotal ? 'row-total' : '');

        bodyHtml += `<tr class="${rowClass}">`;
        bodyHtml += `<td><strong style="${r.bold ? 'font-weight:800;' : 'font-weight:normal;'} color:${r.color || 'inherit'}">${isAr ? r.nameAr : r.nameEn}</strong></td>`;

        visibleIndices.forEach(idx => {
          const val = r.vals[idx];
          let formatted = isCheck ? (val === 0 ? '0.00 (Balanced ✓)' : val.toLocaleString()) : formatFinVal(val, finCurrentUnit);
          let cellStyle = r.color ? `color:${r.color}; font-weight:700;` : '';
          bodyHtml += `<td class="num-col" style="${cellStyle}">${formatted}</td>`;
        });

        bodyHtml += `<td style="text-align:center;"><button class="source-link" onclick="showSourceModal('egx_filings_fy25_h126')">${isAr ? 'إفصاح رسمي ↗' : 'EGX Filing ↗'}</button></td>`;
        bodyHtml += `</tr>`;
      });

      tbody.innerHTML = bodyHtml;
    }

    /* ==========================================================================
       RENDER: SOURCES & USES TABLE
       ========================================================================== */
    function renderSourcesUsesTable() {
      const thRow = document.getElementById('fin-su-th-row');
      const tbody = document.getElementById('fin-su-tbody');
      if (!thRow || !tbody) return;

      const isAr = currentLang === 'ar';
      thRow.innerHTML = `
        <th>${isAr ? 'بند المركز المالي' : 'Balance Sheet Line Item'}</th>
        <th class="num-col">${isAr ? 'ديسمبر 2024' : 'Dec 31, 2024'}</th>
        <th class="num-col">${isAr ? 'ديسمبر 2025' : 'Dec 31, 2025'}</th>
        <th class="num-col">${isAr ? 'التغير (Change)' : 'Net Change'}</th>
        <th class="num-col">${isAr ? 'مصدر نقد (Source +)' : 'Source (+)'}</th>
        <th class="num-col">${isAr ? 'استخدام نقد (Use -)' : 'Use (-)'}</th>
        <th style="text-align:center;">${isAr ? 'التصنيف' : 'Classification'}</th>
      `;

      let totalSources = 0;
      let totalUses = 0;

      let filteredItems = tmgFinData.sourcesUses;
      if (finCurrentSearch) {
        filteredItems = filteredItems.filter(r => (isAr ? r.nameAr : r.nameEn).toLowerCase().includes(finCurrentSearch));
      }

      let rowsHtml = filteredItems.map(r => {
        totalSources += r.source;
        totalUses += r.use;

        const isSource = r.type === 'source';
        const badge = isSource ? 
          `<span class="badge badge-low" style="background:rgba(16,185,129,0.15); color:var(--accent-emerald);">${isAr ? 'مصدر نقد' : 'Cash Source'}</span>` :
          `<span class="badge badge-high" style="background:rgba(244,63,94,0.15); color:var(--accent-rose);">${isAr ? 'استخدام سيولة' : 'Cash Deployment'}</span>`;

        return `
          <tr>
            <td><strong>${isAr ? r.nameAr : r.nameEn}</strong></td>
            <td class="num-col">${formatFinVal(r.v24, finCurrentUnit)}</td>
            <td class="num-col">${formatFinVal(r.v25, finCurrentUnit)}</td>
            <td class="num-col" style="${r.change >= 0 ? 'color:var(--accent-emerald); font-weight:700;' : 'color:var(--accent-rose); font-weight:700;'}">${(r.change >= 0 ? '+' : '') + formatFinVal(r.change, finCurrentUnit)}</td>
            <td class="num-col" style="${r.source > 0 ? 'color:var(--accent-emerald); font-weight:700;' : 'color:var(--text-dim);'}">${r.source > 0 ? formatFinVal(r.source, finCurrentUnit) : '—'}</td>
            <td class="num-col" style="${r.use > 0 ? 'color:var(--accent-rose); font-weight:700;' : 'color:var(--text-dim);'}">${r.use > 0 ? formatFinVal(r.use, finCurrentUnit) : '—'}</td>
            <td style="text-align:center;">${badge}</td>
          </tr>
        `;
      }).join('');

      // Add Total Row
      rowsHtml += `
        <tr class="row-total">
          <td><strong>${isAr ? 'إجمالي مصادر واستخدامات الأموال لعام 2025' : 'Total Sources & Uses of Funds (FY25)'}</strong></td>
          <td class="num-col">—</td>
          <td class="num-col">—</td>
          <td class="num-col">—</td>
          <td class="num-col" style="color:var(--accent-emerald); font-weight:800;">${formatFinVal(totalSources, finCurrentUnit)}</td>
          <td class="num-col" style="color:var(--accent-rose); font-weight:800;">${formatFinVal(totalUses, finCurrentUnit)}</td>
          <td style="text-align:center;"><span class="badge badge-high" style="background:rgba(16,185,129,0.2); color:var(--accent-emerald);">${isAr ? 'توازن تام 100%' : 'Balanced ✓'}</span></td>
        </tr>
      `;

      tbody.innerHTML = rowsHtml;
    }

    /* ==========================================================================
       RENDER: COMMON SIZE TABLE
       ========================================================================== */
    function renderCommonSizeTable() {
      const thRow = document.getElementById('fin-cs-th-row');
      const tbody = document.getElementById('fin-cs-tbody');
      if (!thRow || !tbody) return;

      const isAr = currentLang === 'ar';
      thRow.innerHTML = `
        <th>${isAr ? 'البند وقاعدة التحليل' : 'Statement Item / Base'}</th>
        <th class="num-col">2023 %</th>
        <th class="num-col">2024 %</th>
        <th class="num-col">2025 %</th>
        <th>${isAr ? 'التحليل الجنائي والدلالة' : 'Forensic Commentary'}</th>
      `;

      let bodyHtml = '';

      // 1. Income Statement Section
      bodyHtml += `
        <tr class="row-subhead">
          <td colspan="5">${isAr ? '— التحليل الرأسي لقائمة الدخل (% من إجمالي الإيرادات) —' : '— Income Statement Vertical Analysis (% of Revenue) —'}</td>
        </tr>
      `;

      tmgFinData.commonSizeIS.forEach(r => {
        if (finCurrentSearch && !(isAr ? r.nameAr : r.nameEn).toLowerCase().includes(finCurrentSearch)) return;
        bodyHtml += `
          <tr>
            <td><strong>${isAr ? r.nameAr : r.nameEn}</strong></td>
            <td class="num-col">${r.p23}</td>
            <td class="num-col">${r.p24}</td>
            <td class="num-col" style="font-weight:700; color:var(--accent-cyan);">${r.p25}</td>
            <td style="color:var(--text-muted); font-size:12px;">${isAr ? r.noteAr : r.noteEn}</td>
          </tr>
        `;
      });

      // 2. Balance Sheet Section
      bodyHtml += `
        <tr class="row-subhead">
          <td colspan="5">${isAr ? '— التحليل الرأسي لقائمة المركز المالي (% من إجمالي الأصول) —' : '— Balance Sheet Vertical Analysis (% of Assets) —'}</td>
        </tr>
      `;

      tmgFinData.commonSizeBS.forEach(r => {
        if (finCurrentSearch && !(isAr ? r.nameAr : r.nameEn).toLowerCase().includes(finCurrentSearch)) return;
        bodyHtml += `
          <tr>
            <td><strong>${isAr ? r.nameAr : r.nameEn}</strong></td>
            <td class="num-col">${r.p23}</td>
            <td class="num-col">${r.p24}</td>
            <td class="num-col" style="font-weight:700; color:var(--accent-blue);">${r.p25}</td>
            <td style="color:var(--text-muted); font-size:12px;">${isAr ? r.noteAr : r.noteEn}</td>
          </tr>
        `;
      });

      tbody.innerHTML = bodyHtml;
    }

    /* ==========================================================================
       RENDER: CFO RATIOS TABLE
       ========================================================================== */
    function renderCfoRatiosTable() {
      const thRow = document.getElementById('fin-rt-th-row');
      const tbody = document.getElementById('fin-rt-tbody');
      if (!thRow || !tbody) return;

      const isAr = currentLang === 'ar';
      thRow.innerHTML = `
        <th>${isAr ? 'المؤشر المالي ونوع التحليل' : 'Financial Ratio & Analysis'}</th>
        <th style="text-align:center;">${isAr ? 'المعيار المستهدف' : 'Target / Benchmark'}</th>
        <th class="num-col">2021</th>
        <th class="num-col">2022</th>
        <th class="num-col">2023</th>
        <th class="num-col">2024</th>
        <th class="num-col">2025</th>
        <th>${isAr ? 'الأثر على مقاولي الباطن وسلاسل الإمداد' : 'Subcontractor / Supply Chain Impact'}</th>
      `;

      let bodyHtml = '';
      let currentCategory = '';

      tmgFinData.cfoRatios.forEach(r => {
        if (finCurrentSearch && !(isAr ? r.nameAr : r.nameEn).toLowerCase().includes(finCurrentSearch)) return;

        if (r.cat !== currentCategory) {
          currentCategory = r.cat;
          let catTitles = {
            liquidity: { ar: "— مؤشرات السيولة قصيرة الأجل (Liquidity Ratios) —", en: "— Short-Term Liquidity Ratios —" },
            working_cap: { ar: "— مؤشرات رأس المال العامل والتشغيل (Working Capital & DPO) —", en: "— Working Capital & Operating Cycles —" },
            leverage: { ar: "— مؤشرات الملاءة والرافعة المالية والديون (Solvency & Leverage) —", en: "— Solvency & Debt Leverage Ratios —" },
            profitability: { ar: "— مؤشرات الربحية والعائد على الاستثمار (Profitability & Returns) —", en: "— Profitability & Return Ratios —" }
          };
          bodyHtml += `
            <tr class="row-subhead">
              <td colspan="8">${isAr ? catTitles[currentCategory].ar : catTitles[currentCategory].en}</td>
            </tr>
          `;
        }

        let badgeClass = r.status === 'green' ? 'badge-low' : (r.status === 'amber' ? 'badge-med' : 'badge-high');
        let statusColor = r.status === 'green' ? 'var(--accent-emerald)' : (r.status === 'amber' ? 'var(--accent-amber)' : 'var(--accent-rose)');

        bodyHtml += `
          <tr>
            <td><strong style="color:${statusColor};">${isAr ? r.nameAr : r.nameEn}</strong></td>
            <td style="text-align:center; font-size:11.5px; color:var(--text-dim);">${r.norm}</td>
            <td class="num-col">${r.r21}</td>
            <td class="num-col">${r.r22}</td>
            <td class="num-col">${r.r23}</td>
            <td class="num-col">${r.r24}</td>
            <td class="num-col" style="font-weight:800; color:${statusColor};">${r.r25}</td>
            <td style="font-size:12px; color:var(--text-muted);">${isAr ? r.impactAr : r.impactEn}</td>
          </tr>
        `;
      });

      tbody.innerHTML = bodyHtml;
    }

    /* ==========================================================================
       DYNAMIC KPI STRIP UPDATER
       ========================================================================== */
    function updateFinancialKPIs() {
      let idx = 4; // default FY25
      if (finCurrentYear === '2021') idx = 0;
      else if (finCurrentYear === '2022') idx = 1;
      else if (finCurrentYear === '2023') idx = 2;
      else if (finCurrentYear === '2024') idx = 3;
      else if (finCurrentYear === '2025') idx = 4;
      else if (finCurrentYear === 'h126') idx = 5;

      const revVal = tmgFinData.incomeStatement.find(x => x.id === 'rev_tot').vals[idx];
      const niVal = tmgFinData.incomeStatement.find(x => x.id === 'net_profit').vals[idx];
      const advVal = tmgFinData.liabilitiesEquity.find(x => x.id === 'cust_adv').vals[idx];
      const notesVal = tmgFinData.liabilitiesEquity.find(x => x.id === 'notes_pay').vals[idx];
      const leaseVal = tmgFinData.liabilitiesEquity.find(x => x.id === 'lease_debts').vals[idx];
      const dpoVal = (idx === 4) ? "160 يوماً" : (idx === 3 ? "138 يوماً" : (idx === 2 ? "141 يوماً" : (idx === 1 ? "134 يوماً" : "—")));

      document.getElementById('kpi-fin-rev-v').textContent = formatFinVal(revVal, finCurrentUnit);
      document.getElementById('kpi-fin-ni-v').textContent = formatFinVal(niVal, finCurrentUnit);
      document.getElementById('kpi-fin-adv-v').textContent = formatFinVal(advVal, finCurrentUnit);
      document.getElementById('kpi-fin-notes-v').textContent = formatFinVal(notesVal, finCurrentUnit);
      document.getElementById('kpi-fin-lease-v').textContent = formatFinVal(leaseVal, finCurrentUnit);
      document.getElementById('kpi-fin-dpo-v').textContent = dpoVal;
    }

    /* ==========================================================================
       SUBCONTRACTOR RISK SIMULATOR
       ========================================================================== */
    function updateSimCalculations() {
      const contractVal = parseFloat(document.getElementById('sim-input-val').value);
      const mepPct = parseFloat(document.getElementById('sim-input-mep').value) / 100;
      const delayDays = parseFloat(document.getElementById('sim-input-days').value);
      const fxPct = parseFloat(document.getElementById('sim-input-fx').value) / 100;

      const isAr = currentLang === 'ar';

      // Update Slider Displays
      document.getElementById('disp-sim-val').textContent = (contractVal / 1000000).toFixed(1) + (isAr ? ' مليون ج.م' : ' M EGP');
      document.getElementById('disp-sim-mep').textContent = (mepPct * 100).toFixed(0) + '%';
      document.getElementById('disp-sim-days').textContent = delayDays.toFixed(0) + (isAr ? ' يوماً' : ' Days');
      document.getElementById('disp-sim-fx').textContent = (fxPct * 100).toFixed(0) + '%';

      // Core Calculations
      // 1. Frozen Working Capital = (Contract Value * (Delay Days / 365) * 0.80)
      const frozenCapital = contractVal * (delayDays / 365) * 0.80;
      
      // 2. Bank Financing Interest Cost @ 28% APR
      const interestCost = frozenCapital * 0.28 * (delayDays / 365);

      // 3. Unhedged FX Loss = (Contract Value * MEP % * FX Devaluation %)
      const fxLoss = (contractVal * mepPct) * fxPct;

      // 4. Minimum Required Mobilization Advance = (MEP % * Contract Value * 0.65)
      const minAdvance = contractVal * Math.max(0.35, mepPct * 0.60);
      const minAdvancePct = ((minAdvance / contractVal) * 100).toFixed(0);

      // Render Outputs
      document.getElementById('res-sim-frozen').textContent = (frozenCapital / 1000000).toFixed(2) + ' M';
      document.getElementById('res-sim-interest').textContent = (interestCost / 1000000).toFixed(2) + ' M';
      document.getElementById('res-sim-fxloss').textContent = (fxLoss / 1000000).toFixed(2) + ' M';
      document.getElementById('res-sim-advpay').textContent = (minAdvance / 1000000).toFixed(2) + ` M (${minAdvancePct}%)`;

      // Verdict Logic
      const totalExposure = interestCost + fxLoss;
      const exposurePct = (totalExposure / contractVal) * 100;

      const verdictBox = document.getElementById('res-sim-verdict');
      const verdictTitle = document.getElementById('res-sim-verdict-title');
      const verdictDesc = document.getElementById('res-sim-verdict-desc');

      if (delayDays > 120 && mepPct > 0.50 && fxPct > 0.10) {
        verdictBox.style.background = 'rgba(244,63,94,0.1)';
        verdictBox.style.borderColor = 'var(--accent-rose)';
        verdictTitle.style.color = 'var(--accent-rose)';
        verdictTitle.textContent = isAr ? '⚠️ تقييم العقد: عالي المخاطرة النقدية (High Liquidity Exposure)' : '⚠️ Verdict: High Liquidity & Margin Exposure';
        verdictDesc.textContent = isAr ? 
          `تكلفة التمويل وفروق العملة تلتهم ${exposurePct.toFixed(1)}% من قيمة العقد. لا يجوز توقيع هذا العقد إلا بعد اشتراط دفعة مقدمة نقدية بنسبة ${minAdvancePct}% وإلغاء شرط الباك تو باك.` :
          `Financing cost and currency risk erode ${exposurePct.toFixed(1)}% of contract value. Do NOT sign without minimum ${minAdvancePct}% cash advance and elimination of back-to-back clause.`;
      } else {
        verdictBox.style.background = 'rgba(16,185,129,0.1)';
        verdictBox.style.borderColor = 'var(--accent-emerald)';
        verdictTitle.style.color = 'var(--accent-emerald)';
        verdictTitle.textContent = isAr ? '✓ تقييم العقد: مخاطرة متوازنة وقابلة للتحوط' : '✓ Verdict: Manageable & Hedged Contract Profile';
        verdictDesc.textContent = isAr ? 
          `مستوى المخاطرة تحت السيطرة. تأكد من إيداع شيكات الدفعة المقدمة والربط بجدول تسليم معتمد.` :
          `Risk profile is balanced. Ensure advance payment clearance and milestone certification schedule.`;
      }
    }

    /* ==========================================================================
       DYNAMIC FINANCIAL CHARTS INITIALIZATION (Chart.js)
       ========================================================================== */
    function initDynamicFinancialCharts() {
      const textColor = currentTheme === 'light' ? '#090d16' : '#f8fafc';
      const textMuted = currentTheme === 'light' ? '#475569' : '#94a3b8';
      const gridColor = currentTheme === 'light' ? 'rgba(203, 213, 225, 0.6)' : 'rgba(51, 65, 85, 0.35)';
      const fontFam = currentLang === 'ar' ? 'Cairo, Plus Jakarta Sans, sans-serif' : 'Plus Jakarta Sans, Cairo, sans-serif';
      const isAr = currentLang === 'ar';

      // Destroy previous dynamic charts if exist
      [chartFinTrendsDyn, chartBSDyn, chartDpoDyn, chartSourcesUsesDyn].forEach(c => {
        if (c) c.destroy();
      });

      // 1. Multi-Year Trends Dynamic Chart
      const elFinDyn = document.getElementById('chartFinancialTrendsDynamic');
      if (elFinDyn) {
        chartFinTrendsDyn = new Chart(elFinDyn.getContext('2d'), {
          type: 'bar',
          data: {
            labels: ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026'],
            datasets: [
              {
                label: isAr ? 'الإيرادات المجمعة (مليار جنيه)' : 'Consolidated Revenue (EGP bn)',
                data: [15.36, 19.87, 28.43, 46.90, 62.50, 30.19],
                backgroundColor: '#0284c7',
                borderRadius: 5
              },
              {
                label: isAr ? 'صافي الأرباح المجمعة (مليار جنيه)' : 'Net Profit (EGP bn)',
                data: [1.78, 2.23, 3.31, 9.12, 18.20, 9.95],
                backgroundColor: '#059669',
                borderRadius: 5
              },
              {
                type: 'line',
                label: isAr ? 'رصيد المبيعات المتعاقد عليها (Backlog)' : 'Contracted Backlog (EGP bn)',
                data: [63.0, 77.0, 145.0, 294.0, 441.2, 460.0],
                borderColor: '#d97706',
                backgroundColor: 'rgba(217, 119, 6, 0.1)',
                borderWidth: 2.5,
                tension: 0.3,
                fill: false
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { labels: { color: textColor, font: { family: fontFam, size: 11, weight: '700' } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } }
            }
          }
        });
      }

      // 2. Balance Sheet Composition Stacked Dynamic Chart
      const elBSDyn = document.getElementById('chartBalanceSheetDynamic');
      if (elBSDyn) {
        chartBSDyn = new Chart(elBSDyn.getContext('2d'), {
          type: 'bar',
          data: {
            labels: ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026'],
            datasets: [
              {
                label: isAr ? 'مشروعات قيد التنفيذ WIP (مليار)' : 'Real Estate WIP (bn)',
                data: [46.8, 54.2, 71.3, 102.5, 138.5, 154.0],
                backgroundColor: '#f59e0b'
              },
              {
                label: isAr ? 'الأصول الثابتة والفنادق CWIP (مليار)' : 'Hotels & Fixed Assets (bn)',
                data: [31.2, 36.8, 51.2, 81.4, 107.5, 118.2],
                backgroundColor: '#3b82f6'
              },
              {
                label: isAr ? 'مقدمات العملاء Float (مليار)' : 'Customer Advances (bn)',
                data: [38.5, 48.2, 72.0, 95.0, 117.7, 134.0],
                backgroundColor: '#dc2626'
              },
              {
                label: isAr ? 'التزامات التأجير التمويلي (مليار)' : 'Lease Debt (bn)',
                data: [1.2, 2.1, 4.8, 22.1, 34.4, 44.0],
                backgroundColor: '#8b5cf6'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { labels: { color: textColor, font: { family: fontFam, size: 10, weight: '700' } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } }
            }
          }
        });
      }

      // 3. DPO vs Contractor Stretch Dynamic Chart
      const elDpoDyn = document.getElementById('chartDpoDynamic');
      if (elDpoDyn) {
        chartDpoDyn = new Chart(elDpoDyn.getContext('2d'), {
          type: 'line',
          data: {
            labels: ['FY2022', 'FY2023', 'FY2024', 'FY2025'],
            datasets: [
              {
                label: isAr ? 'فترة سداد الموردين والمقاولين (DPO يوماً)' : 'Days Payable Outstanding (DPO)',
                data: [134, 141, 138, 160],
                borderColor: '#f43f5e',
                backgroundColor: 'rgba(244, 63, 94, 0.1)',
                borderWidth: 3,
                tension: 0.3,
                fill: true,
                pointRadius: 6,
                pointHoverRadius: 8
              },
              {
                label: isAr ? 'معيار المقاولات الآمن (90 يوماً)' : 'Safe Industry Norm (90d)',
                data: [90, 90, 90, 90],
                borderColor: '#10b981',
                borderDash: [5, 5],
                borderWidth: 2,
                fill: false,
                pointRadius: 0
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { labels: { color: textColor, font: { family: fontFam, size: 11, weight: '700' } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } }, min: 60, max: 200 }
            }
          }
        });
      }

      // 4. Sources & Uses Waterfall Bar Dynamic Chart
      const elSUDyn = document.getElementById('chartSourcesUsesDynamic');
      if (elSUDyn) {
        chartSourcesUsesDyn = new Chart(elSUDyn.getContext('2d'), {
          type: 'bar',
          data: {
            labels: isAr ? 
              ['شراكة ADQ', 'مقدمات حجز', 'أرباح محتجزة', 'تأجير تمويلي', 'توسع WIP', 'تطوير فنادق', 'مدينون'] :
              ['ADQ Equity', 'Cust. Advances', 'Retained Earnings', 'Lease Debt', 'WIP Expansion', 'Hotel Capex', 'Receivables'],
            datasets: [
              {
                label: isAr ? 'مصادر الأموال + (مليار)' : 'Sources of Funds + (bn)',
                data: [26.0, 22.7, 15.3, 12.3, 0, 0, 0],
                backgroundColor: '#059669',
                borderRadius: 4
              },
              {
                label: isAr ? 'استخدامات الأموال - (مليار)' : 'Uses of Funds - (bn)',
                data: [0, 0, 0, 0, -36.0, -26.1, -14.6],
                backgroundColor: '#dc2626',
                borderRadius: 4
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { labels: { color: textColor, font: { family: fontFam, size: 10, weight: '700' } } }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam, size: 10 } } },
              y: { grid: { color: gridColor }, ticks: { color: textMuted, font: { family: fontFam } } }
            }
          }
        });
      }
    }

    /* ==========================================================================
       FINANCIAL LANGUAGE & TEXT SYNCHRONIZATION
       ========================================================================== */
    function updateFinancialLanguage() {
      const isAr = currentLang === 'ar';

      const trans = {
        badgeHero: { ar: "مدقق جنائياً — البورصة المصرية", en: "Forensically Audited — EGX Disclosures" },
        heroTitle: { ar: "مركز التحليل المالي والتدقيق الجنائي المتقدم (2021 – 2025 + H1 2026)", en: "Forensic Financial Intelligence & Multi-Year Audit Center (FY2021 – FY2025 + H1 2026)" },
        heroSub: { 
          ar: "تحليل تفاعلي ديناميكي كامل لقوائم الدخل والمركز المالي لمجموعة طلعت مصطفى القابضة (TMGH.CA). يتضمن تحليل مصادر واستخدامات الأموال، التحليل الرأسي النسبي، مؤشرات Construction CFO، وتقييم أثر السيولة والائتمان على مقاولي الباطن (P.ZONE).",
          en: "Comprehensive dynamic forensic audit of TMG Holding (TMGH.CA) income statements and balance sheets. Includes cash sources & uses, common size %, Construction CFO metrics, and subcontractor risk protections (P.ZONE)."
        },
        slicerView: { ar: "نافذة التحليل:", en: "Analysis Module:" },
        slicerYear: { ar: "النطاق الزمني:", en: "Time Horizon:" },
        slicerUnit: { ar: "وحدة العرض:", en: "Reporting Unit:" },
        searchPh: { ar: "بحث فوري في البنود...", en: "Instant line item filter..." },
        btnVIsbs: { ar: "📑 القوائم المالية الكاملة", en: "📑 Financial Statements" },
        btnVSources: { ar: "🔄 مصادر واستخدامات النقدية", en: "🔄 Sources & Uses" },
        btnVCommon: { ar: "⚖️ التحليل الرأسي %", en: "⚖️ Common Size %" },
        btnVRatios: { ar: "📈 نسب Construction CFO", en: "📈 CFO Ratios" },
        btnVPzone: { ar: "🛡️ تقييم P.ZONE وحزم المياه", en: "🛡️ P.Zone Water Risk" },
        btnVGuide: { ar: "💡 دليل المبتدئين والحاسبة", en: "💡 Plain Guide & Calculator" }
      };

      const setT = (id, obj) => {
        const el = document.getElementById(id);
        if (el) el.textContent = isAr ? obj.ar : obj.en;
      };

      setT('badge-fin-hero', trans.badgeHero);
      setT('t-fin-hero-title', trans.heroTitle);
      setT('t-fin-hero-sub', trans.heroSub);
      setT('btn-v-isbs', trans.btnVIsbs);
      setT('btn-v-sources', trans.btnVSources);
      setT('btn-v-common', trans.btnVCommon);
      setT('btn-v-ratios', trans.btnVRatios);
      setT('btn-v-pzone', trans.btnVPzone);
      setT('btn-v-guide', trans.btnVGuide);

      const searchEl = document.getElementById('finSearchInput');
      if (searchEl) searchEl.placeholder = isAr ? trans.searchPh.ar : trans.searchPh.en;

      // Re-render active subview
      if (finCurrentView === 'is-bs') renderFinancialStatementsTable();
      else if (finCurrentView === 'sources-uses') renderSourcesUsesTable();
      else if (finCurrentView === 'common-size') renderCommonSizeTable();
      else if (finCurrentView === 'cfo-ratios') renderCfoRatiosTable();
      else if (finCurrentView === 'guide') updateSimCalculations();

      updateFinancialKPIs();
      initDynamicFinancialCharts();
    }
"""

# Let's insert financial_js into the main <script> tag before initCharts()
if "const tmgFinData = {" not in text:
    target_pos = text.find('function initCharts()')
    if target_pos == -1:
        print("ERROR: Could not find function initCharts() in HTML!")
        sys.exit(1)

    print(f"Injecting Financial JS engine before initCharts() at pos {target_pos}...")
    new_text = text[:target_pos] + financial_js + "\n\n    " + text[target_pos:]

    # Also hook into initCharts() body so it calls initDynamicFinancialCharts()
    needle = "function initCharts() {"
    replace_needle = "function initCharts() {\n      initDynamicFinancialCharts();"
    new_text = new_text.replace(needle, replace_needle, 1)

    # Also hook into setLanguage() so it calls updateFinancialLanguage()
    needle_lang = "localStorage.setItem('tmg_lang', lang);"
    replace_needle_lang = "localStorage.setItem('tmg_lang', lang);\n      if (typeof updateFinancialLanguage === 'function') updateFinancialLanguage();"
    new_text = new_text.replace(needle_lang, replace_needle_lang, 1)

    # Also hook into DOMContentLoaded
    needle_load = "renderSwotAndTows();"
    replace_needle_load = "renderSwotAndTows();\n      if (typeof setFinView === 'function') setFinView('is-bs');\n      if (typeof updateSimCalculations === 'function') updateSimCalculations();"
    new_text = new_text.replace(needle_load, replace_needle_load, 1)

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(new_text)

    print("Successfully injected Financial JS engine and lifecycle hooks! New length:", len(new_text))
else:
    print("Financial JS engine already injected.")
