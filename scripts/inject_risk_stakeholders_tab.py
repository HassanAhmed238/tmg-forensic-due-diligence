# -*- coding: utf-8 -*-
"""
Script to inject Tab 11: Project Map, Stakeholders, LinkedIn Teams, SWOT & TOWS
into build_perfect_dashboard.py and rebuild the dashboards.
"""
import openpyxl
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
risk_dir = r"F:\Mr Hesham\TMG\RISK"

# ==============================================================================
# 1. PARSE EXCEL DATA
# ==============================================================================

# A. Companies & Contacts (42 entities)
wb_comp = openpyxl.load_workbook(os.path.join(risk_dir, "TMG_Project_Companies_Contacts_One_Sheet.xlsx"), data_only=True)
sheet_comp = wb_comp["دليل الاتصال"]
companies_list = []
for r in range(5, sheet_comp.max_row + 1):
    c_id = sheet_comp.cell(row=r, column=1).value
    if c_id is None:
        continue
    name = str(sheet_comp.cell(row=r, column=2).value or "").strip()
    role = str(sheet_comp.cell(row=r, column=3).value or "").strip()
    project = str(sheet_comp.cell(row=r, column=4).value or "").strip()
    relation = str(sheet_comp.cell(row=r, column=5).value or "").strip()
    phone = str(sheet_comp.cell(row=r, column=6).value or "").strip()
    phone_notes = str(sheet_comp.cell(row=r, column=7).value or "").strip()
    email = str(sheet_comp.cell(row=r, column=8).value or "").strip()
    website = str(sheet_comp.cell(row=r, column=9).value or "").strip()
    rel_source = str(sheet_comp.cell(row=r, column=10).value or "").strip()
    phone_source = str(sheet_comp.cell(row=r, column=11).value or "").strip()
    evidence_level = str(sheet_comp.cell(row=r, column=12).value or "").strip()
    confidence = str(sheet_comp.cell(row=r, column=13).value or "").strip()
    notes = str(sheet_comp.cell(row=r, column=14).value or "").strip()
    
    companies_list.append({
        "id": int(c_id) if isinstance(c_id, (int, float)) else str(c_id),
        "name": name,
        "role": role,
        "project": project,
        "relation": relation,
        "phone": phone,
        "phone_notes": phone_notes,
        "email": email,
        "website": website,
        "rel_source": rel_source,
        "phone_source": phone_source,
        "evidence_level": evidence_level,
        "confidence": confidence,
        "notes": notes
    })

# B. Project Teams & LinkedIn Profiles (38 profiles)
wb_team = openpyxl.load_workbook(os.path.join(risk_dir, "TMG_Project_Teams_LinkedIn_People_AR.xlsx"), data_only=True)
sheet_team = wb_team["فرق المشاريع وLinkedIn"]
teams_list = []
for r in range(4, sheet_team.max_row + 1):
    t_id = sheet_team.cell(row=r, column=1).value
    if t_id is None:
        continue
    project = str(sheet_team.cell(row=r, column=2).value or "").strip()
    company = str(sheet_team.cell(row=r, column=3).value or "").strip()
    name = str(sheet_team.cell(row=r, column=4).value or "").strip()
    role = str(sheet_team.cell(row=r, column=5).value or "").strip()
    linkedin = str(sheet_team.cell(row=r, column=6).value or "").strip()
    phone = str(sheet_team.cell(row=r, column=7).value or "").strip()
    evidence_level = str(sheet_team.cell(row=r, column=8).value or "").strip()
    source = str(sheet_team.cell(row=r, column=9).value or "").strip()
    notes = str(sheet_team.cell(row=r, column=10).value or "").strip()
    
    teams_list.append({
        "id": int(t_id) if isinstance(t_id, (int, float)) else str(t_id),
        "project": project,
        "company": company,
        "name": name,
        "role": role,
        "linkedin": linkedin,
        "phone": phone,
        "evidence_level": evidence_level,
        "source": source,
        "notes": notes
    })

# C. SWOT & TOWS
wb_swot = openpyxl.load_workbook(os.path.join(risk_dir, "tmg_swot_analysis.xlsx"), data_only=True)
def parse_swot_items(sheetname):
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

swot_dict = {
    "strengths": parse_swot_items("Detailed Strengths"),
    "weaknesses": parse_swot_items("Detailed Weaknesses"),
    "opportunities": parse_swot_items("Detailed Opportunities"),
    "threats": parse_swot_items("Detailed Threats")
}

sh_tows = wb_swot["Strategic TOWS Matrix"]
tows_dict = {"SO": [], "ST": [], "WO": [], "WT": []}
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
        tows_dict[current_cat].append({
            "id": str(c1).strip(),
            "name": str(sh_tows.cell(row=r, column=2).value or "").strip(),
            "roadmap": str(sh_tows.cell(row=r, column=3).value or "").strip(),
            "priority": str(sh_tows.cell(row=r, column=7).value or "High Priority").strip()
        })

# D. Map Projects List
projects_map = [
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
        "color": "#06b6d4"
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
        "color": "#3b82f6"
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
        "color": "#10b981"
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
        "color": "#8b5cf6"
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
        "color": "#f59e0b"
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
        "color": "#ec4899"
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
        "color": "#6366f1"
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
        "contractors": "Atrium Saudi (100%), NHC (الشركة الوطنية للإسكان)",
        "color": "#10b981"
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
        "contractors": "تحالف مجموعة طلعت مصطفى ووزارة الإسكان العمانية",
        "color": "#14b8a6"
    }
]

# Serialized JSON representations
companies_json = json.dumps(companies_list, ensure_ascii=False)
teams_json = json.dumps(teams_list, ensure_ascii=False)
swot_json = json.dumps(swot_dict, ensure_ascii=False)
tows_json = json.dumps(tows_dict, ensure_ascii=False)
projects_map_json = json.dumps(projects_map, ensure_ascii=False)

print("Serialized datasets ready for embedding.")

# ==============================================================================
# 2. HTML TAB 11 MARKUP
# ==============================================================================
tab11_html = f'''
      <!-- ================================================================== -->
      <!-- TAB 11: INTERACTIVE PROJECT MAP, STAKEHOLDERS & LINKEDIN DIRECTORY -->
      <!-- ================================================================== -->
      <div id="tab-stakeholders" class="tab-pane">
        
        <!-- Header Banner -->
        <div class="bezel-wrap" style="margin-bottom: 20px;">
          <div class="card" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(16, 185, 129, 0.08)); border-inline-start: 5px solid var(--accent-blue);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
              <div>
                <div style="display:flex; align-items:center; gap:10px;">
                  <span class="badge badge-high" style="background:rgba(59,130,246,0.2); color:var(--accent-blue); border-color:var(--accent-blue);">إشراف تنفيذي جنائي</span>
                  <h3 style="margin:0; font-size:18px; font-weight:800; color:var(--text-main);" id="stakeholders-header-title">خريطة المشروعات وأصحاب المصلحة ودليل الفرق والمقاولين (42 كيان و 38 ملف قيادي)</h3>
                </div>
                <p style="margin:8px 0 0; font-size:13.5px; color:var(--text-muted); line-height:1.6; max-width:1100px;" id="stakeholders-header-desc">
                  خريطة جغرافية تفاعلية شاملة لمشروعات مجموعة طلعت مصطفى (TMGH) في مصر والسعودية وعمان. تتيح استعراض 42 شركة ومقاول ومورد معتمد مع أرقام التواصل العامة، و 38 قيادياً ومهندساً مع روابط LinkedIn موثقة، مصحوبة بمصفوفة SWOT و TOWS الاستراتيجية المدققة.
                </p>
              </div>
              <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <button class="btn-action" onclick="resetProjectFilter()" style="font-weight:700;">
                  <span>🔄 إعادة ضبط التصفية</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- 4 Top KPI Ribbon Cards -->
        <div class="kpi-grid" style="margin-bottom: 24px;">
          <div class="kpi-card blue">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-landbank">إجمالي محفظة الأراضي (Landbank)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064"/></svg>
            </div>
            <div class="kpi-value">> 26,700 فدان</div>
            <div class="kpi-delta delta-up">> 112 مليون م² عبر 3 دول (مصر، KSA، عمان)</div>
          </div>

          <div class="kpi-card emerald">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-backlog">رصيد المبيعات التعاقدية (Backlog)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div class="kpi-value">441.2B ج.م</div>
            <div class="kpi-delta delta-up">يضمن تدفقات إيرادات معترف بها لـ 5-7 سنوات</div>
          </div>

          <div class="kpi-card purple">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-comp-count">الكيانات والشركات المفهرسة</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
            </div>
            <div class="kpi-value">42 جهة موثقة</div>
            <div class="kpi-delta delta-neutral">مقاولون عموميون، ذراع المقاولات، موردو نظم وبنوك</div>
          </div>

          <div class="kpi-card amber">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-lbl-team-count">فرق العمل وقيادات المشاريع</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
            </div>
            <div class="kpi-value">38 ملف مهني</div>
            <div class="kpi-delta delta-up">روابط LinkedIn مباشرة ومصنفة بدرجة الدليل</div>
          </div>
        </div>

        <!-- SECTION 1: INTERACTIVE GEOGRAPHIC MAP -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap: wrap; gap: 12px;">
              <div>
                <div class="card-title" id="map-section-title">🗺️ الخريطة الجغرافية التفاعلية لمشروعات TMG التوسعية</div>
                <div class="card-subtitle" id="map-section-subtitle">انقر على أي علامة مشروع لتكبير الخريطة وتصفية جدول المقاولين ودليل الفرق تلقائياً</div>
              </div>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;" id="project-filter-chips">
                <button class="filter-chip active" onclick="filterMapByProject('all')">الكل (9 مشروعات)</button>
                <button class="filter-chip" onclick="filterMapByProject('southmed')">ساوث ميد (SouthMED)</button>
                <button class="filter-chip" onclick="filterMapByProject('noor')">مدينة نور (Noor)</button>
                <button class="filter-chip" onclick="filterMapByProject('madinaty')">مدينتي (Madinaty)</button>
                <button class="filter-chip" onclick="filterMapByProject('celia')">سيليا (Celia)</button>
                <button class="filter-chip" onclick="filterMapByProject('fs_luxor')">فورسيزونز الأقصر</button>
                <button class="filter-chip" onclick="filterMapByProject('fs_sharm')">فورسيزونز شرم</button>
                <button class="filter-chip" onclick="filterMapByProject('san_stefano')">سان ستيفانو</button>
                <button class="filter-chip" onclick="filterMapByProject('banan')">بنان الرياض 🇸🇦</button>
                <button class="filter-chip" onclick="filterMapByProject('jood_yamal')">جود ويامال عمان 🇴🇲</button>
              </div>
            </div>

            <!-- Map Container -->
            <div id="tmg-leaflet-map" style="width: 100%; height: 500px; border-radius: 10px; border: 1px solid var(--border-subtle); z-index: 1;"></div>
            
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px; font-size:12px; color:var(--text-muted); flex-wrap:wrap; gap:10px;">
              <div>📌 <strong>مفتاح الخريطة:</strong> <span style="color:#06b6d4;">● ساحلي وسياحي</span> | <span style="color:#3b82f6;">● مدن ذكية جديدة</span> | <span style="color:#10b981;">● مجتمعات ناضجة</span> | <span style="color:#f59e0b;">● ضيافة وفنادق</span> | <span style="color:#10b981;">● توسعات إقليمية (KSA/Oman)</span></div>
              <div id="map-selection-indicator" style="font-weight:700; color:var(--accent-blue);">المشروع النشط: عرض جميع المشروعات</div>
            </div>
          </div>
        </div>

        <!-- SECTION 2: VERIFIED COMPANIES & CONTRACTS DIRECTORY -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap: wrap; gap: 14px;">
              <div>
                <div class="card-title" id="companies-table-title">🏢 دليل الشركات والجهات المرتبطة بمشروعات TMG (أرقام التواصل العامة المنشورة)</div>
                <div class="card-subtitle" id="companies-table-subtitle">42 كيان مفهرس مع الصفة، نطاق العمل، أرقام الهاتف العامة، البريد، ومستوى ثقة العلاقة</div>
              </div>
              <div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
                <input type="text" id="company-search-input" placeholder="🔍 بحث باسم الشركة، الدور، أو المشروع..." style="background:var(--bg-surface-elevated); color:var(--text-main); border:1px solid var(--border-subtle); border-radius:8px; padding:8px 14px; font-size:13px; min-width:240px;" oninput="applyCompanyFilters()">
                <select id="company-role-filter" style="background:var(--bg-surface-elevated); color:var(--text-main); border:1px solid var(--border-subtle); border-radius:8px; padding:8px 12px; font-size:13px;" onchange="applyCompanyFilters()">
                  <option value="all">كل الأدوار والصفات</option>
                  <option value="مقاول">مقاولون رئيسيون / JV</option>
                  <option value="ذراع">أذرع مقاولات بالمجموعة (Atrium / ACC)</option>
                  <option value="مورد">موردو أنظمة وبنية أساسية</option>
                  <option value="استشاري">استشاريون وإشراف</option>
                  <option value="بنك">بنوك وشركاء تمويليون</option>
                </select>
                <span id="companies-count-badge" class="badge badge-med" style="font-size:12px;">42 شركة</span>
              </div>
            </div>

            <div style="overflow-x: auto; max-height: 520px; overflow-y: auto;">
              <table style="width: 100%; border-collapse: collapse; font-size: 13px;" id="companies-table-dom">
                <thead style="position: sticky; top: 0; background: var(--bg-surface-elevated); z-index: 2;">
                  <tr style="border-bottom: 2px solid var(--border-subtle); text-align: start;">
                    <th style="padding: 10px 12px; width: 40px;">#</th>
                    <th style="padding: 10px 12px; min-width: 180px;">اسم الشركة / الكيان</th>
                    <th style="padding: 10px 12px; min-width: 150px;">المشروع / الموقع</th>
                    <th style="padding: 10px 12px; min-width: 220px;">الدور ونطاق الأعمال</th>
                    <th style="padding: 10px 12px; min-width: 150px;">طبيعة العلاقة بـ TMG</th>
                    <th style="padding: 10px 12px; min-width: 180px;">أرقام التواصل العامة</th>
                    <th style="padding: 10px 12px; min-width: 140px;">البريد والموقع</th>
                    <th style="padding: 10px 12px; width: 90px; text-align: center;">درجة الدليل</th>
                  </tr>
                </thead>
                <tbody id="companies-table-body">
                  <!-- Dynamically rendered via JS -->
                </tbody>
              </table>
            </div>
            
            <div style="margin-top: 12px; font-size: 11.5px; color: var(--text-muted); line-height: 1.5;">
              ⚠️ <strong>إخلاء مسؤولية جنائي:</strong> الأرقام المدرجة هي أرقام أعمال منشورة علناً وليست أرقاماً خاصة. وجود اسم شركة في مستندات المشروع لا يثبت بالضرورة عقداً مباشراً مع TMG أو وجود مستحقات معلقة ما لم يتم التثبت من أصل التعاقد.
            </div>
          </div>
        </div>

        <!-- SECTION 3: PROJECT TEAMS & LINKEDIN PERSONNEL DIRECTORY -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap: wrap; gap: 14px;">
              <div>
                <div class="card-title" id="teams-section-title">👥 دليل الأشخاص وفرق العمل المرتبطة بالمشروعات (ملفات LinkedIn العامة)</div>
                <div class="card-subtitle" id="teams-section-subtitle">38 كادراً هندسياً وإدارياً مع المسمى المهني المنشور ودرجة التوثيق ورابط الملف المباشر</div>
              </div>
              <div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
                <input type="text" id="team-search-input" placeholder="🔍 بحث باسم الشخص، المنصب، أو الشركة..." style="background:var(--bg-surface-elevated); color:var(--text-main); border:1px solid var(--border-subtle); border-radius:8px; padding:8px 14px; font-size:13px; min-width:240px;" oninput="applyTeamFilters()">
                <span id="teams-count-badge" class="badge badge-med" style="font-size:12px;">38 مهندساً وقيادياً</span>
              </div>
            </div>

            <!-- Personnel Grid -->
            <div id="teams-cards-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 14px; max-height: 550px; overflow-y: auto; padding: 4px;">
              <!-- Dynamically populated via JS -->
            </div>

            <div style="margin-top: 12px; font-size: 11.5px; color: var(--text-muted); line-height: 1.5;">
              📌 <strong>معايير التدقيق:</strong> ملفات الأشخاص مستخرجة من الفهرسة العامة المهنية لـ LinkedIn حتى أكتوبر 2026. الانتماء إلى شركة لا يثبت تعيين الشخص في مشروع محدد إلا إذا ذكر المصدر ذلك صراحة (تصنيف B / C).
            </div>
          </div>
        </div>

        <!-- SECTION 4: STRATEGIC SWOT & TOWS MATRIX -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header" style="flex-wrap:wrap; gap:12px;">
              <div>
                <div class="card-title" id="swot-section-title">⚖️ التحليل الاستراتيجي الرباعي (TMG Deep SWOT Matrix) ومصفوفة TOWS التنفيذية</div>
                <div class="card-subtitle" id="swot-section-subtitle">تقييم جنائي مفصل لنقاط القوة والضعف والفرص والتهديدات مع خطط العمل الاستراتيجية</div>
              </div>
              <div style="display:flex; gap:8px;">
                <button class="filter-chip active" id="btn-show-swot" onclick="switchSwotView('swot')">مصفوفة SWOT الرباعية</button>
                <button class="filter-chip" id="btn-show-tows" onclick="switchSwotView('tows')">مصفوفة TOWS الاستراتيجية (Action Plans)</button>
              </div>
            </div>

            <!-- View 1: 4 SWOT Quadrants -->
            <div id="swot-quadrants-view" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(440px, 1fr)); gap: 16px;">
              
              <!-- STRENGTHS -->
              <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(16,185,129,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-emerald);">💪 نقاط القوة (Strengths)</span>
                  <span class="badge badge-low">6 محاور استراتيجية</span>
                </div>
                <div id="swot-strengths-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

              <!-- WEAKNESSES -->
              <div style="background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(239,68,68,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-rose);">⚠️ نقاط الضعف (Weaknesses)</span>
                  <span class="badge badge-high">6 فجوات هيكلية</span>
                </div>
                <div id="swot-weaknesses-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

              <!-- OPPORTUNITIES -->
              <div style="background: rgba(59, 130, 246, 0.05); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(59,130,246,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-blue);">🚀 الفرص التوسعية (Opportunities)</span>
                  <span class="badge badge-low">6 محفزات نمو</span>
                </div>
                <div id="swot-opportunities-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

              <!-- THREATS -->
              <div style="background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 10px; padding: 16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(245,158,11,0.2); padding-bottom:8px;">
                  <span style="font-weight:800; font-size:15px; color:var(--accent-amber);">⚡ التهديدات والمخاطر (Threats)</span>
                  <span class="badge badge-med">6 متجهات خطر خارجية</span>
                </div>
                <div id="swot-threats-container" style="display:flex; flex-direction:column; gap:10px;">
                  <!-- Rendered via JS -->
                </div>
              </div>

            </div>

            <!-- View 2: Strategic TOWS Actionable Matrix -->
            <div id="tows-matrix-view" style="display: none; flex-direction: column; gap: 16px;">
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(440px, 1fr)); gap:16px;">
                
                <!-- SO STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-emerald);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-emerald); margin-bottom:10px;">🎯 استراتيجيات SO (استغلال القوة لاقتناص الفرص)</div>
                  <div id="tows-so-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

                <!-- ST STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-amber);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-amber); margin-bottom:10px;">🛡️ استراتيجيات ST (توظيف القوة لتحييد التهديدات)</div>
                  <div id="tows-st-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

                <!-- WO STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-blue);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-blue); margin-bottom:10px;">🔄 استراتيجيات WO (معالجة نقاط الضعف باغتنام الفرص)</div>
                  <div id="tows-wo-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

                <!-- WT STRATEGIES -->
                <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-inline-start: 4px solid var(--accent-rose);">
                  <div style="font-weight:800; font-size:14.5px; color:var(--accent-rose); margin-bottom:10px;">⚠️ استراتيجيات WT (تقليص الضعف وتفادي المخاطر)</div>
                  <div id="tows-wt-container" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

              </div>
            </div>

          </div>
        </div>

      </div>
'''

# ==============================================================================
# 3. JAVASCRIPT CONTROLLER FOR TAB 11
# ==============================================================================
tab11_js = f'''
  <!-- Data Stores for Stakeholders, Teams & SWOT -->
  <script>
    const TMG_COMPANIES = {companies_json};
    const TMG_TEAMS = {teams_json};
    const TMG_SWOT = {swot_json};
    const TMG_TOWS = {tows_json};
    const TMG_PROJECTS_MAP = {projects_map_json};

    let activeProjectFilter = 'all';
    let tmgLeafletMapInstance = null;
    let tmgMapMarkers = {{}};

    // Initialize Leaflet Map
    function initTmgMap() {
      const mapContainer = document.getElementById('tmg-leaflet-map');
      if (!mapContainer || tmgLeafletMapInstance) return;

      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const tileUrl = isDark 
        ? 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}'
        : 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}';

      tmgLeafletMapInstance = L.map('tmg-leaflet-map', {
        center: [27.5, 38.0],
        zoom: 5,
        minZoom: 3,
        maxZoom: 16,
        zoomControl: true
      });

      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; Esri, HERE, Garmin, FAO, USGS, EPA',
        maxZoom: 16
      }).addTo(tmgLeafletMapInstance);

      // Add Project Markers with custom HTML Pins & Labels
      const latLngs = [];
      TMG_PROJECTS_MAP.forEach(proj => {
        latLngs.push([proj.lat, proj.lng]);
        
        // Custom Rich HTML DivIcon
        const customIcon = L.divIcon({
          className: 'tmg-map-pin',
          html: `
            <div style="display:flex; flex-direction:column; align-items:center; transform: translate(-50%, -100%); cursor:pointer;">
              <div style="background:${proj.color}; color:#fff; font-weight:800; font-size:11px; padding:3px 8px; border-radius:12px; box-shadow:0 3px 8px rgba(0,0,0,0.35); white-space:nowrap; border:1.5px solid #fff; display:flex; align-items:center; gap:4px;">
                <span>📍</span> <span>${proj.id === 'banan' ? '🇸🇦 بنان الرياض' : (proj.id === 'jood_yamal' ? '🇴🇲 عمان' : proj.name_ar.split(' ')[0] + ' ' + (proj.name_ar.split(' ')[1] || ''))}</span>
              </div>
              <div style="width:10px; height:10px; background:${proj.color}; border:2px solid #fff; border-radius:50%; margin-top:2px; box-shadow:0 0 8px ${proj.color};"></div>
            </div>
          `,
          iconSize: [0, 0],
          iconAnchor: [0, 0]
        });

        const marker = L.marker([proj.lat, proj.lng], { icon: customIcon }).addTo(tmgLeafletMapInstance);

        // Tooltip
        marker.bindTooltip(`<strong>${proj.name_ar}</strong><br><span style="font-size:11px; color:#888;">${proj.area}</span>`, {
          permanent: false,
          direction: 'top'
        });

        // Rich Popup
        const popupHtml = `
          <div style="font-family: inherit; min-width: 250px; padding: 6px; color: #111;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 2px solid ${proj.color}; padding-bottom: 5px; margin-bottom: 8px;">
              <h4 style="margin:0; font-size:14px; font-weight:800; color:#111827;">${proj.name_ar}</h4>
            </div>
            <div style="font-size:12px; margin-bottom:5px;">📍 <strong>الموقع:</strong> ${proj.location_ar}</div>
            <div style="font-size:12px; margin-bottom:5px;">📐 <strong>المساحة:</strong> ${proj.area}</div>
            <div style="font-size:12px; margin-bottom:5px;">💰 <strong>القيمة / الأثر:</strong> ${proj.gdv}</div>
            <div style="font-size:12px; margin-bottom:6px;">🏗️ <strong>المقاولون الرئيسيون:</strong> ${proj.contractors}</div>
            <div style="margin-top:10px;">
              <button onclick="filterMapByProject('${proj.id}')" style="width:100%; background:${proj.color}; color:#fff; border:none; padding:7px 12px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                🔍 تصفية الشركات والفرق لهذا المشروع
              </button>
            </div>
          </div>
        `;
        marker.bindPopup(popupHtml);
        tmgMapMarkers[proj.id] = marker;
      });

      // Fit bounds to show Egypt, KSA, and Oman
      if (latLngs.length > 0) {
        tmgLeafletMapInstance.fitBounds(latLngs, { padding: [40, 40] });
      }

      window.tmgMapInitialized = true;
    }

    // Switch Map Tile Theme
    function updateMapTheme(theme) {
      if (!tmgLeafletMapInstance || !window.tmgMapTiles) return;
      const tileUrl = theme === 'dark'
        ? 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}'
        : 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}';
      tmgLeafletMapInstance.removeLayer(window.tmgMapTiles);
      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; Esri, HERE, Garmin, FAO, USGS, EPA',
        maxZoom: 16
      }).addTo(tmgLeafletMapInstance);
    }

    // Filter Map by Project
    function filterMapByProject(projId) {{
      activeProjectFilter = projId;

      // Update Filter Chips UI
      document.querySelectorAll('#project-filter-chips .filter-chip').forEach(btn => {{
        const onclickAttr = btn.getAttribute('onclick') || '';
        btn.classList.toggle('active', onclickAttr.includes(`'${{projId}}'`));
      }});

      // Update Map View
      if (tmgLeafletMapInstance) {{
        if (projId === 'all') {{
          tmgLeafletMapInstance.setView([28.5, 36.0], 5);
          document.getElementById('map-selection-indicator').textContent = 'المشروع النشط: عرض جميع المشروعات';
        }} else {{
          const proj = TMG_PROJECTS_MAP.find(p => p.id === projId);
          if (proj) {{
            tmgLeafletMapInstance.setView([proj.lat, proj.lng], 9);
            if (tmgMapMarkers[projId]) {{
              tmgMapMarkers[projId].openPopup();
            }}
            document.getElementById('map-selection-indicator').innerHTML = `المشروع النشط: <strong>${{proj.name_ar}}</strong> (${{proj.area}})`;
          }}
        }}
      }}

      // Cross-filter Companies Table and Teams Grid
      renderCompaniesTable();
      renderTeamsCards();
    }}

    function resetProjectFilter() {{
      filterMapByProject('all');
      document.getElementById('company-search-input').value = '';
      document.getElementById('company-role-filter').value = 'all';
      document.getElementById('team-search-input').value = '';
      applyCompanyFilters();
      applyTeamFilters();
    }}

    // Render Companies Table
    function renderCompaniesTable() {{
      const tbody = document.getElementById('companies-table-body');
      if (!tbody) return;

      const searchTerm = (document.getElementById('company-search-input')?.value || '').toLowerCase().trim();
      const roleFilter = document.getElementById('company-role-filter')?.value || 'all';

      let filtered = TMG_COMPANIES.filter(c => {{
        // Project Match
        if (activeProjectFilter !== 'all') {{
          const projMap = {{
            'southmed': 'southmed',
            'noor': 'نور',
            'madinaty': 'مدينتي',
            'celia': 'celia',
            'fs_luxor': 'أقصر',
            'fs_sharm': 'شرم',
            'san_stefano': 'سان ستيفانو',
            'banan': 'سعودية'
          }};
          const keyword = projMap[activeProjectFilter];
          if (keyword && !c.project.toLowerCase().includes(keyword.toLowerCase())) {{
            return false;
          }}
        }}

        // Role Filter
        if (roleFilter !== 'all') {{
          if (roleFilter === 'مقاول' && !c.role.includes('مقاول') && !c.relation.includes('مقاول')) return false;
          if (roleFilter === 'ذراع' && !c.role.includes('ذراع') && !c.relation.includes('منظومة')) return false;
          if (roleFilter === 'مورد' && !c.role.includes('مورد') && !c.role.includes('تجهيز') && !c.role.includes('أنظمة')) return false;
          if (roleFilter === 'استشاري' && !c.role.includes('استشار') && !c.role.includes('إشراف')) return false;
          if (roleFilter === 'بنك' && !c.role.includes('بنك') && !c.relation.includes('بنك')) return false;
        }}

        // Search Term
        if (searchTerm) {{
          const matchStr = `${{c.name}} ${{c.role}} ${{c.project}} ${{c.phone}} ${{c.relation}}`.toLowerCase();
          if (!matchStr.includes(searchTerm)) return false;
        }}

        return true;
      }});

      document.getElementById('companies-count-badge').textContent = `${{filtered.length}} / 42 شركة`;

      if (filtered.length === 0) {{
        tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:30px; color:var(--text-muted);">لا توجد شركات مطابقة لمعايير البحث والتصفية المحددة.</td></tr>`;
        return;
      }}

      tbody.innerHTML = filtered.map((c, idx) => {{
        // Evidence badge color
        const evColor = c.evidence_level.startsWith('A') ? 'badge-low' : (c.evidence_level.includes('B') ? 'badge-med' : 'badge-high');
        
        // Format Phones with click-to-call
        const phoneLinks = c.phone && c.phone !== 'غير متاح'
          ? c.phone.split('/').map(p => {{
              const cleanP = p.replace(/[^0-9+]/g, '');
              return `<a href="tel:${{cleanP}}" style="color:var(--accent-blue); text-decoration:none; font-family:var(--font-mono); font-size:12px; margin-inline-end:6px;">📞 ${{p.trim()}}</a>`;
            }}).join('<br>')
          : `<span style="color:var(--text-muted); font-size:11.5px;">غير معلن</span>`;

        // Format Email
        const emailLink = c.email && c.email !== 'غير متاح'
          ? `<a href="mailto:${{c.email}}" style="color:var(--accent-cyan); text-decoration:none; font-size:11.5px; display:block; overflow:hidden; text-overflow:ellipsis;">✉️ ${{c.email}}</a>`
          : `<span style="color:var(--text-muted); font-size:11px;">—</span>`;

        // Website
        const webLink = c.website && c.website.startsWith('http')
          ? `<a href="${{c.website}}" target="_blank" style="color:var(--accent-emerald); text-decoration:none; font-size:11.5px; font-weight:700;">🌐 زيارة الموقع ↗</a>`
          : ``;

        return `
          <tr style="border-bottom: 1px solid var(--border-subtle); hover: background-color: var(--bg-surface-elevated);">
            <td style="padding: 10px 12px; font-weight:700; color:var(--text-muted);">${{c.id}}</td>
            <td style="padding: 10px 12px;">
              <div style="font-weight:800; color:var(--text-main); font-size:13.5px;">${{c.name}}</div>
              <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">${{c.relation}}</div>
            </td>
            <td style="padding: 10px 12px;">
              <span class="badge" style="background:rgba(59,130,246,0.1); color:var(--accent-blue); font-size:11px;">${{c.project}}</span>
            </td>
            <td style="padding: 10px 12px; font-size:12.5px; line-height:1.5;">
              <div style="white-space:pre-line;">${{c.role}}</div>
              ${{c.notes ? `<div style="font-size:11px; color:var(--text-muted); margin-top:4px;">ℹ️ ${{c.notes}}</div>` : ''}}
            </td>
            <td style="padding: 10px 12px; font-size:12px; color:var(--text-muted);">${{c.relation}}</td>
            <td style="padding: 10px 12px; line-height:1.6;">${{phoneLinks}}</td>
            <td style="padding: 10px 12px; line-height:1.5;">${{emailLink}}${{webLink}}</td>
            <td style="padding: 10px 12px; text-align:center;">
              <span class="badge ${{evColor}}" style="font-size:11px; font-weight:700;">${{c.evidence_level}}</span>
              <div style="font-size:10px; color:var(--text-muted); margin-top:2px;">${{c.confidence}}</div>
            </td>
          </tr>
        `;
      }}).join('');
    }}

    function applyCompanyFilters() {{
      renderCompaniesTable();
    }}

    // Render Teams Cards
    function renderTeamsCards() {{
      const container = document.getElementById('teams-cards-grid');
      if (!container) return;

      const searchTerm = (document.getElementById('team-search-input')?.value || '').toLowerCase().trim();

      let filtered = TMG_TEAMS.filter(t => {{
        // Project Match
        if (activeProjectFilter !== 'all') {{
          const projMap = {{
            'southmed': 'southmed',
            'noor': 'نور',
            'madinaty': 'مدينتي',
            'celia': 'celia',
            'fs_luxor': 'أقصر',
            'fs_sharm': 'شرم',
            'san_stefano': 'سان ستيفانو',
            'banan': 'سعودية'
          }};
          const keyword = projMap[activeProjectFilter];
          if (keyword && !t.project.toLowerCase().includes(keyword.toLowerCase())) {{
            return false;
          }}
        }}

        // Search Term
        if (searchTerm) {{
          const matchStr = `${{t.name}} ${{t.role}} ${{t.company}} ${{t.project}}`.toLowerCase();
          if (!matchStr.includes(searchTerm)) return false;
        }}

        return true;
      }});

      document.getElementById('teams-count-badge').textContent = `${{filtered.length}} / 38 كادراً`;

      if (filtered.length === 0) {{
        container.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:30px; color:var(--text-muted);">لا توجد ملفات مهنية مطابقة لخيارات التصفية.</div>`;
        return;
      }}

      container.innerHTML = filtered.map(t => {{
        const evBadge = t.evidence_level.startsWith('A') ? 'badge-low' : (t.evidence_level.includes('B') ? 'badge-med' : 'badge-high');
        
        return `
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; transition: transform 0.2s;" onmouseover="this.style.borderColor='var(--accent-blue)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:8px;">
                <div style="font-weight:800; font-size:14px; color:var(--text-main);">${{t.name}}</div>
                <span class="badge ${{evBadge}}" style="font-size:10.5px;">دليل ${{t.evidence_level}}</span>
              </div>
              
              <div style="font-size:12px; font-weight:700; color:var(--accent-blue); margin-top:4px; line-height:1.4;">
                ${{t.role}}
              </div>

              <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:8px;">
                <span style="font-size:11px; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:4px; color:var(--text-muted);">🏢 ${{t.company}}</span>
                <span style="font-size:11px; background:rgba(59,130,246,0.1); padding:2px 8px; border-radius:4px; color:var(--accent-blue);">📍 ${{t.project}}</span>
              </div>

              ${{t.notes ? `<p style="font-size:11.5px; color:var(--text-muted); margin:8px 0 0; line-height:1.5;">${{t.notes}}</p>` : ''}}
            </div>

            <div style="margin-top:12px; pt:8px; border-top:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:11px; color:var(--text-muted);">${{t.phone !== 'غير منشور' ? t.phone : 'هاتف العمل متاح بالشركة'}}</span>
              <a href="${{t.linkedin}}" target="_blank" style="background:#0a66c2; color:#fff; text-decoration:none; padding:4px 10px; border-radius:6px; font-size:11.5px; font-weight:700; display:inline-flex; align-items:center; gap:4px;">
                <svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                عرض الملف ↗
              </a>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function applyTeamFilters() {{
      renderTeamsCards();
    }}

    // Render SWOT & TOWS
    function renderSwotAndTows() {{
      // Strengths
      const strContainer = document.getElementById('swot-strengths-container');
      if (strContainer) {{
        strContainer.innerHTML = TMG_SWOT.strengths.map(s => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-emerald);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${{s.id}}: ${{s.factor}}</span>
              <span class="badge badge-low" style="font-size:10px;">${{s.impact}}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${{s.details}}</p>
            <div style="font-size:11px; color:var(--accent-emerald); margin-top:4px; font-weight:700;">📊 ${{s.data}}</div>
          </div>
        `).join('');
      }}

      // Weaknesses
      const wContainer = document.getElementById('swot-weaknesses-container');
      if (wContainer) {{
        wContainer.innerHTML = TMG_SWOT.weaknesses.map(w => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-rose);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${{w.id}}: ${{w.factor}}</span>
              <span class="badge badge-high" style="font-size:10px;">${{w.impact}}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${{w.details}}</p>
            <div style="font-size:11px; color:var(--accent-rose); margin-top:4px; font-weight:700;">⚠️ ${{w.data}}</div>
          </div>
        `).join('');
      }}

      // Opportunities
      const oContainer = document.getElementById('swot-opportunities-container');
      if (oContainer) {{
        oContainer.innerHTML = TMG_SWOT.opportunities.map(o => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-blue);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${{o.id}}: ${{o.factor}}</span>
              <span class="badge badge-low" style="font-size:10px;">${{o.impact}}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${{o.details}}</p>
            <div style="font-size:11px; color:var(--accent-blue); margin-top:4px; font-weight:700;">🚀 ${{o.data}}</div>
          </div>
        `).join('');
      }}

      // Threats
      const tContainer = document.getElementById('swot-threats-container');
      if (tContainer) {{
        tContainer.innerHTML = TMG_SWOT.threats.map(t => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-amber);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${{t.id}}: ${{t.factor}}</span>
              <span class="badge badge-med" style="font-size:10px;">${{t.impact}}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${{t.details}}</p>
            <div style="font-size:11px; color:var(--accent-amber); margin-top:4px; font-weight:700;">⚡ ${{t.data}}</div>
          </div>
        `).join('');
      }}

      // TOWS Containers
      ['SO', 'ST', 'WO', 'WT'].forEach(cat => {{
        const el = document.getElementById(`tows-${{cat.toLowerCase()}}-container`);
        if (el && TMG_TOWS[cat]) {{
          el.innerHTML = TMG_TOWS[cat].map(strat => `
            <div style="background:var(--bg-surface); padding:8px 10px; border-radius:6px; margin-bottom:6px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:700; font-size:12.5px; color:var(--text-main);">${{strat.id}}: ${{strat.name}}</span>
                <span class="badge badge-med" style="font-size:10px;">${{strat.priority}}</span>
              </div>
              <p style="font-size:11.5px; color:var(--text-muted); margin:4px 0 0; line-height:1.4;">${{strat.roadmap}}</p>
            </div>
          `).join('');
        }}
      }});
    }}

    function switchSwotView(view) {{
      document.getElementById('swot-quadrants-view').style.display = view === 'swot' ? 'grid' : 'none';
      document.getElementById('tows-matrix-view').style.display = view === 'tows' ? 'flex' : 'none';
      document.getElementById('btn-show-swot').classList.toggle('active', view === 'swot');
      document.getElementById('btn-show-tows').classList.toggle('active', view === 'tows');
    }}

    // Initial render on load
    document.addEventListener('DOMContentLoaded', function() {{
      renderCompaniesTable();
      renderTeamsCards();
      renderSwotAndTows();
    }});
  </script>
'''

# ==============================================================================
# 4. INJECT INTO build_perfect_dashboard.py
# ==============================================================================
builder_file = r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py"
with open(builder_file, "r", encoding="utf-8") as f:
    dashboard_code = f.read()

# 1. Inject Leaflet CDN into <head>
leaflet_head = """  <!-- Leaflet.js Interactive Geo Map -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
"""
if "leaflet@1.9.4" not in dashboard_code:
    dashboard_code = dashboard_code.replace("</head>", leaflet_head + "\n</head>")
    print("Leaflet head assets injected.")

# 2. Add Tab 11 Nav Button
nav_btn_target = """      <button class="nav-btn" onclick="switchTab('pzone')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
        <span id="nav-pzone">دراسة P.ZONE وحزم المياه</span>
      </button>"""

nav_btn_new = nav_btn_target + """

      <button class="nav-btn" onclick="switchTab('stakeholders')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/></svg>
        <span id="nav-stakeholders">خريطة المشروعات وأصحاب المصلحة</span>
      </button>"""

if nav_btn_target in dashboard_code and 'switchTab(\'stakeholders\')' not in dashboard_code:
    dashboard_code = dashboard_code.replace(nav_btn_target, nav_btn_new)
    print("Nav button 11 injected.")

# 3. Add Tab 11 HTML Markup
tab_pzone_end = """        <!-- The Non-Negotiable Contractual Armor -->
        <div class="bezel-wrap">
          <div class="card" style="background: rgba(16, 185, 129, 0.05); border-inline-start: 5px solid var(--accent-emerald);">
            <div class="card-header">
              <div>
                <div class="card-title" style="color:var(--accent-emerald);">🛡️ الدرع التعاقدي الحتمي لشركة P.ZONE (The Non-Negotiable Term Sheet)</div>
                <div class="card-subtitle">شروط لا تقبل المساومة لضمان سلامة رأس المال والسيولة النقدية</div>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px;">
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">1. دفعة مقدمة نقدية 25%</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  سداد فوري كاش مقابل خطاب ضمان دفعة مقدمة (APG) لتأمين طلبيات المصانع العالمية فوراً دون استنزاف السيولة الذاتية لـ P.ZONE.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">2. بند تحييد سعر الصرف (FX Pass-Through)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  تثبيت أسعار بنود التوريدات الكهروميكانيكية بالعملة الأجنبية أو السداد بالمعادل الرسمي بسعر البنك المركزي يوم التحويل.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">3. حظر أوراق الدفع المؤجلة</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  سداد المستخلصات الشهرية نقداً بحد أقصى 30 يوماً؛ ورفض أي شيكات مؤجلة تفوق 60 يوماً إلا إذا كانت معززة مصرفياً ومحملة بفوائد التمويل التجارية.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-emerald); font-weight:800; font-size:13.5px; margin-bottom:6px;">4. إسقاط شرط التبعية (Pay-When-Paid)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  ربط استحقاق P.ZONE بالمطابقة الفنية للأعمال المنفذة فقط، واستقلاليتها التامة عن حسابات المقاول العام والنزاعات التمويلية مع المطور.
                </p>
              </div>
            </div>
          </div>
        </div>

      </div>"""

if tab_pzone_end in dashboard_code and 'id="tab-stakeholders"' not in dashboard_code:
    dashboard_code = dashboard_code.replace(tab_pzone_end, tab_pzone_end + "\n\n" + tab11_html)
    print("Tab 11 HTML injected.")

# 4. Inject JS Controller before </body>
if 'TMG_PROJECTS_MAP' not in dashboard_code:
    dashboard_code = dashboard_code.replace("</body>", tab11_js + "\n</body>")
    print("Tab 11 JS Controller injected.")

# 5. Hook switchTab for Map Invalidation
switch_hook_target = """      if (tabId === 'procurement') {
        setTimeout(renderD3PrivityTree, 60);
      }"""
switch_hook_replacement = """      if (tabId === 'procurement') {
        setTimeout(renderD3PrivityTree, 60);
      }
      if (tabId === 'stakeholders') {
        setTimeout(function() {
          if (!window.tmgMapInitialized) {
            initTmgMap();
          } else if (tmgLeafletMapInstance) {
            tmgLeafletMapInstance.invalidateSize();
          }
        }, 100);
      }"""

if switch_hook_target in dashboard_code and "tabId === 'stakeholders'" not in dashboard_code:
    dashboard_code = dashboard_code.replace(switch_hook_target, switch_hook_replacement)
    print("switchTab hook injected.")

# 6. Hook setTheme for Leaflet Tiles
theme_hook_target = """      updateChartsTheme(theme);"""
theme_hook_replacement = """      updateChartsTheme(theme);
      if (typeof updateMapTheme === 'function') updateMapTheme(theme);"""
if theme_hook_target in dashboard_code and "updateMapTheme(theme)" not in dashboard_code:
    dashboard_code = dashboard_code.replace(theme_hook_target, theme_hook_replacement)
    print("setTheme hook injected.")

# 7. Add i18n entries
i18n_ar_target = """pzone: "دراسة P.ZONE وحزم المياه","""
i18n_ar_new = """pzone: "دراسة P.ZONE وحزم المياه",
          stakeholders: "خريطة المشروعات وأصحاب المصلحة","""

i18n_en_target = """pzone: "P.ZONE Water MEP Case Study","""
i18n_en_new = """pzone: "P.ZONE Water MEP Case Study",
          stakeholders: "Project Map & Stakeholders","""

if i18n_ar_target in dashboard_code and 'stakeholders:' not in dashboard_code:
    dashboard_code = dashboard_code.replace(i18n_ar_target, i18n_ar_new)
    dashboard_code = dashboard_code.replace(i18n_en_target, i18n_en_new)
    print("i18n entries injected.")

set_lang_target = """if (document.getElementById('nav-pzone')) document.getElementById('nav-pzone').textContent = t.pzone;"""
set_lang_new = """if (document.getElementById('nav-pzone')) document.getElementById('nav-pzone').textContent = t.pzone;
      if (document.getElementById('nav-stakeholders')) document.getElementById('nav-stakeholders').textContent = t.stakeholders;"""
if set_lang_target in dashboard_code and 'nav-stakeholders' not in dashboard_code:
    dashboard_code = dashboard_code.replace(set_lang_target, set_lang_new)
    print("setLanguage handler injected.")

# Write back to build_perfect_dashboard.py
with open(builder_file, "w", encoding="utf-8") as f:
    f.write(dashboard_code)

print("build_perfect_dashboard.py successfully updated with Tab 11!")
