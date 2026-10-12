# -*- coding: utf-8 -*-
"""
Script to create the complete Tab 11 (Project Map, Stakeholders, LinkedIn Teams, SWOT & TOWS)
and inject it cleanly into scripts/build_perfect_dashboard.py, then rebuild the dashboards.
"""
import openpyxl
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
risk_dir = r"F:\Mr Hesham\TMG\RISK"

# ==============================================================================
# 1. LOAD & CLEAN DATA FROM EXCEL
# ==============================================================================

# Companies
wb_comp = openpyxl.load_workbook(os.path.join(risk_dir, "TMG_Project_Companies_Contacts_One_Sheet.xlsx"), data_only=True)
sheet_comp = wb_comp["دليل الاتصال"]
companies_data = []
for r in range(5, sheet_comp.max_row + 1):
    c_id = sheet_comp.cell(row=r, column=1).value
    if c_id is None:
        continue
    name = sheet_comp.cell(row=r, column=2).value or ""
    role = sheet_comp.cell(row=r, column=3).value or ""
    project = sheet_comp.cell(row=r, column=4).value or ""
    relation = sheet_comp.cell(row=r, column=5).value or ""
    phone = sheet_comp.cell(row=r, column=6).value or ""
    phone_notes = sheet_comp.cell(row=r, column=7).value or ""
    email = sheet_comp.cell(row=r, column=8).value or ""
    website = sheet_comp.cell(row=r, column=9).value or ""
    rel_source = sheet_comp.cell(row=r, column=10).value or ""
    phone_source = sheet_comp.cell(row=r, column=11).value or ""
    evidence_level = sheet_comp.cell(row=r, column=12).value or ""
    confidence = sheet_comp.cell(row=r, column=13).value or ""
    notes = sheet_comp.cell(row=r, column=14).value or ""
    
    companies_data.append({
        "id": int(c_id) if isinstance(c_id, (int, float)) else str(c_id),
        "name": str(name).strip(),
        "role": str(role).strip(),
        "project": str(project).strip(),
        "relation": str(relation).strip(),
        "phone": str(phone).strip(),
        "phone_notes": str(phone_notes).strip(),
        "email": str(email).strip(),
        "website": str(website).strip(),
        "rel_source": str(rel_source).strip(),
        "phone_source": str(phone_source).strip(),
        "evidence_level": str(evidence_level).strip(),
        "confidence": str(confidence).strip(),
        "notes": str(notes).strip()
    })

# Key Personnel
wb_team = openpyxl.load_workbook(os.path.join(risk_dir, "TMG_Project_Teams_LinkedIn_People_AR.xlsx"), data_only=True)
sheet_team = wb_team["فرق المشاريع وLinkedIn"]
teams_data = []
for r in range(4, sheet_team.max_row + 1):
    t_id = sheet_team.cell(row=r, column=1).value
    if t_id is None:
        continue
    project = sheet_team.cell(row=r, column=2).value or ""
    company = sheet_team.cell(row=r, column=3).value or ""
    name = sheet_team.cell(row=r, column=4).value or ""
    role = sheet_team.cell(row=r, column=5).value or ""
    linkedin = sheet_team.cell(row=r, column=6).value or ""
    phone = sheet_team.cell(row=r, column=7).value or ""
    evidence_level = sheet_team.cell(row=r, column=8).value or ""
    source = sheet_team.cell(row=r, column=9).value or ""
    notes = sheet_team.cell(row=r, column=10).value or ""
    
    teams_data.append({
        "id": int(t_id) if isinstance(t_id, (int, float)) else str(t_id),
        "project": str(project).strip(),
        "company": str(company).strip(),
        "name": str(name).strip(),
        "role": str(role).strip(),
        "linkedin": str(linkedin).strip(),
        "phone": str(phone).strip(),
        "evidence_level": str(evidence_level).strip(),
        "source": str(source).strip(),
        "notes": str(notes).strip()
    })

# SWOT & TOWS
wb_swot = openpyxl.load_workbook(os.path.join(risk_dir, "tmg_swot_analysis.xlsx"), data_only=True)
def parse_swot(sheetname):
    sh = wb_swot[sheetname]
    items = []
    for r in range(5, sh.max_row + 1):
        s_id = sh.cell(row=r, column=1).value
        if not s_id:
            continue
        items.append({
            "id": str(s_id).strip(),
            "factor": str(sh.cell(row=r, column=2).value or "").strip(),
            "details": str(sh.cell(row=r, column=3).value or "").strip(),
            "data": str(sh.cell(row=r, column=4).value or "").strip(),
            "impact": str(sh.cell(row=r, column=5).value or "").strip(),
            "source": str(sh.cell(row=r, column=6).value or "").strip()
        })
    return items

swot_data = {
    "strengths": parse_swot("Detailed Strengths"),
    "weaknesses": parse_swot("Detailed Weaknesses"),
    "opportunities": parse_swot("Detailed Opportunities"),
    "threats": parse_swot("Detailed Threats")
}

sh_tows = wb_swot["Strategic TOWS Matrix"]
tows_data = {"SO": [], "ST": [], "WO": [], "WT": []}
current_cat = None
for r in range(4, sh_tows.max_row + 1):
    c1 = sh_tows.cell(row=r, column=1).value
    if c1 and "SO STRATEGIES" in str(c1):
        current_cat = "SO"
        continue
    elif c1 and "ST STRATEGIES" in str(c1):
        current_cat = "ST"
        continue
    elif c1 and "WO STRATEGIES" in str(c1):
        current_cat = "WO"
        continue
    elif c1 and "WT STRATEGIES" in str(c1):
        current_cat = "WT"
        continue
    elif c1 == "Strategy ID" or not c1:
        continue
    
    if current_cat and str(c1).startswith(current_cat):
        tows_data[current_cat].append({
            "id": str(c1).strip(),
            "name": str(sh_tows.cell(row=r, column=2).value or "").strip(),
            "roadmap": str(sh_tows.cell(row=r, column=3).value or "").strip(),
            "priority": str(sh_tows.cell(row=r, column=7).value or "High Priority").strip()
        })

print(f"Data parsed successfully: {len(companies_data)} companies, {len(teams_data)} people, {sum(len(v) for v in swot_data.values())} SWOT items, {sum(len(v) for v in tows_data.values())} TOWS strategies.")

# Map Projects Data
projects_map_data = [
    {
        "id": "southmed",
        "name_ar": "مشروع ساوث ميد (SouthMED)",
        "name_en": "SouthMED Mediterranean Mega-Resort",
        "location_ar": "الضبعة، الساحل الشمالي (الكيلو 165 طريق الإسكندرية - مطروح)",
        "location_en": "El Dabaa, North Coast Mediterranean (Km 165)",
        "lat": 31.0167,
        "lng": 28.4000,
        "area": "5,542 فدان (23.3 مليون م²)",
        "gdv": "21.0 مليار دولار GDV",
        "deliveries": "2029+",
        "contractors": "Concrete Plus (Zone C01 - 10B EGP), Atrium AQC, Metito, Crystal Lagoons",
        "color": "#06b6d4",
        "category": "coastal"
    },
    {
        "id": "noor",
        "name_ar": "مدينة نور الذكية (Noor City)",
        "name_en": "Noor Smart City",
        "location_ar": "حدائق العاصمة، أمام العاصمة الإدارية (شرق القاهرة)",
        "location_en": "Capital Gardens, East Cairo (Opposite NAC)",
        "lat": 30.1667,
        "lng": 31.7500,
        "area": "5,000 فدان (140,000 وحدة سكنية)",
        "gdv": "> 500 مليار جنيه مصري",
        "deliveries": "2026 – 2028+",
        "contractors": "Concrete Plus (V3.2 - 170 Villas), Atrium AQC, Siemens, Schneider Electric",
        "color": "#3b82f6",
        "category": "smart_city"
    },
    {
        "id": "madinaty",
        "name_ar": "مدينتي و East Hub و Open Air Mall",
        "name_en": "Madinaty Integrated City & East Hub",
        "location_ar": "القاهرة الجديدة، طريق السويس",
        "location_en": "New Cairo, Suez Road",
        "lat": 30.0833,
        "lng": 31.6333,
        "area": "8,000 فدان (33.6 مليون م²)",
        "gdv": "مجتمع متكامل يضم >700 ألف نسمة",
        "deliveries": "مكتمل جزئياً / توسعات مستمرة",
        "contractors": "Atrium AQC, Alexandria Construction (ACC), CCC (Four Seasons Capital JV), MCBS",
        "color": "#10b981",
        "category": "urban"
    },
    {
        "id": "celia",
        "name_ar": "مشروع سيليا (Celia New Capital)",
        "name_en": "Celia New Administrative Capital",
        "location_ar": "العاصمة الإدارية الجديدة، الحزام الأخضر",
        "location_en": "New Administrative Capital, Green River",
        "lat": 30.0167,
        "lng": 31.7000,
        "area": "500 فدان (فيلات وعمارات فاخرة)",
        "gdv": "> 35 مليار جنيه مبيعات",
        "deliveries": "تسليمات مرحلية جارية",
        "contractors": "Atrium Quality Contractors, Alexandria Construction (ACC)",
        "color": "#8b5cf6",
        "category": "luxury"
    },
    {
        "id": "fs_luxor",
        "name_ar": "فندق فورسيزونز الأقصر (Four Seasons Luxor)",
        "name_en": "Four Seasons Hotel Luxor",
        "location_ar": "الأقصر، كورنيش النيل مباشرة",
        "location_en": "Luxor, Direct Nile Corniche",
        "lat": 25.6872,
        "lng": 32.6396,
        "area": "فندق تاريخي فاخر 201 غرفة وجناح",
        "gdv": "رافعة تدفقات دولارية (Icon Hospitality)",
        "deliveries": "2026/2027",
        "contractors": "Atrium Quality Contractors (Main EPC Turnkey)",
        "color": "#f59e0b",
        "category": "hospitality"
    },
    {
        "id": "fs_sharm",
        "name_ar": "فورسيزونز شرم الشيخ (Four Seasons Sharm)",
        "name_en": "Four Seasons Resort Sharm El Sheikh",
        "location_ar": "شرم الشيخ، خليج القرش (البحر الأحمر)",
        "location_en": "Sharm El Sheikh, Sharks Bay (Red Sea)",
        "lat": 27.9158,
        "lng": 34.3299,
        "area": "توسعة منتجع فاخر بـ 1,400 غرفة وفيلا",
        "gdv": "أعلى عائد سياحي دولاري بالغرفة",
        "deliveries": "قيد التشغيل وتوسعات نشطة",
        "contractors": "Atrium Quality Contractors, ACC",
        "color": "#ec4899",
        "category": "hospitality"
    },
    {
        "id": "san_stefano",
        "name_ar": "سان ستيفانو جراند بلازا (San Stefano Alexandria)",
        "name_en": "San Stefano Grand Plaza Alexandria",
        "location_ar": "الإسكندرية، كورنيش سان ستيفانو",
        "location_en": "Alexandria, Corniche Landmark",
        "lat": 31.2439,
        "lng": 29.9678,
        "area": "برج متعدد الاستخدامات + فورسيزونز + مارينا",
        "gdv": "أحد أبرز أصول محفظة الضيافة والتجزئة",
        "deliveries": "مشروع قائم ومُدر للدخل الدوري",
        "contractors": "Alexandria Construction (ACC), Atrium AQC",
        "color": "#6366f1",
        "category": "landmark"
    },
    {
        "id": "banan",
        "name_ar": "مدينة بنان الذكية - الرياض (Banan Riyadh)",
        "name_en": "Banan Smart City Riyadh (KSA)",
        "location_ar": "ضاحية الفرسان، شمال شرق الرياض، المملكة العربية السعودية",
        "location_en": "Al Fursan Suburb, North-East Riyadh, KSA",
        "lat": 24.8500,
        "lng": 46.7500,
        "area": "10.0 مليون م² (27,000 وحدة سكنية)",
        "gdv": "31.4 مليار ريال سعودي (> 8.3B USD)",
        "deliveries": "2029 المستهدف الأول",
        "contractors": "Atrium Saudi (100%), NHC (الشركة الوطنية للإسكان - شريك استراتيجي)",
        "color": "#10b981",
        "category": "regional"
    },
    {
        "id": "jood_yamal",
        "name_ar": "مدينتي جود ويامال - سلطنة عمان",
        "name_en": "Jood & Yamal Coastal Cities (Oman)",
        "location_ar": "مسقط / بركاء، ساحل سلطنة عمان",
        "location_en": "Muscat / Barka Coast, Sultanate of Oman",
        "lat": 23.7000,
        "lng": 58.0000,
        "area": "4.9 مليون م² (~14,000 وحدة سكنية)",
        "gdv": "1.8 مليار ريال عماني (~ 4.7B USD)",
        "deliveries": "مرحلة التخطيط والتمهيد",
        "contractors": "تحالف مجموعة طلعت مصطفى ووزارة الإسكان والتخطيط العمراني العمانية",
        "color": "#14b8a6",
        "category": "regional"
    }
]

print("Projects mapped count:", len(projects_map_data))
