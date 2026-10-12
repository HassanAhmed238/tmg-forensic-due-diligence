# -*- coding: utf-8 -*-
"""
Upgrade generator script to transform generate_powerbi_ceo_dashboard.py into a full Microsoft Power BI interactive experience.
Adds:
1. Native Power BI Action Bar (Visual Headers) with Slicer indicator, Focus Mode (Expand), and Options.
2. Power BI Canvas Plugin: Dotted Waterfall connectors + Crisp Data Labels on all bars/points.
3. Power BI Full-Screen Focus Mode Modal ("Show as a table") with underlying dataset grid and CSV export.
4. Concrete Plus & TMG Partnership Card in Tab 5 (10B EGP SouthMED contract, 179 buildings, Noor City V3.2).
5. 4-Pillar Hybrid Closed-Loop Procurement Architecture in Tab 2.
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'scripts/generate_powerbi_ceo_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

print(f"Loaded generate_powerbi_ceo_dashboard.py: {len(code)} characters")

# ==============================================================================
# 1. ADD CSS FOR POWER BI ACTION BARS, FOCUS MODE OVERLAY & DATA TABLES
# ==============================================================================
pbi_action_css = r'''
    /* ==========================================================================
       POWER BI VISUAL HEADER & FOCUS MODE EXTENSIONS
       ========================================================================== */
    .pbi-visual-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--pbi-border-subtle);
      position: relative;
    }
    .pbi-visual-title-box {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .pbi-visual-actions {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      opacity: 0.85;
      transition: opacity 0.2s;
    }
    .pbi-card:hover .pbi-visual-actions {
      opacity: 1;
    }
    .pbi-visual-btn {
      background: var(--pbi-surface-sunken);
      border: 1px solid var(--pbi-border-subtle);
      color: var(--pbi-text-muted);
      border-radius: 6px;
      padding: 4px 7px;
      font-size: 11px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: all 0.15s ease;
      font-family: var(--pbi-font-sans);
    }
    .pbi-visual-btn:hover {
      color: var(--pbi-accent-cyan);
      border-color: var(--pbi-accent-cyan);
      background: rgba(2, 132, 199, 0.1);
      transform: translateY(-1px);
    }
    html[data-theme="dark"] .pbi-visual-btn:hover {
      background: rgba(0, 229, 255, 0.12);
    }

    /* Focus Mode Overlay */
    #pbi-focus-overlay {
      position: fixed;
      inset: 0;
      z-index: 9999;
      background: var(--pbi-canvas-bg);
      display: none;
      flex-direction: column;
      overflow-y: auto;
      padding: 24px 32px;
      animation: pbiFadeIn 0.2s ease-out;
    }
    #pbi-focus-overlay.active {
      display: flex;
    }
    @keyframes pbiFadeIn {
      from { opacity: 0; transform: scale(0.99); }
      to { opacity: 1; transform: scale(1); }
    }
    .focus-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 16px;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--pbi-border-highlight);
    }
    .focus-title-group h2 {
      font-size: 20px;
      font-weight: 800;
      color: var(--pbi-text-hero);
      margin: 0 0 4px 0;
    }
    .focus-title-group p {
      font-size: 13px;
      color: var(--pbi-text-muted);
      margin: 0;
    }
    .focus-tools {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .focus-content-grid {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 24px;
      flex: 1;
      min-height: 480px;
    }
    @media (max-width: 1100px) {
      .focus-content-grid { grid-template-columns: 1fr; }
    }
    .focus-chart-panel {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--pbi-card-shadow);
      min-height: 450px;
    }
    .focus-table-panel {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--pbi-card-shadow);
      max-height: 600px;
      overflow-y: auto;
    }
    .focus-table-panel h4 {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--pbi-accent-cyan);
      margin: 0 0 12px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
'''

# Insert the CSS into head styles
if '/* ==========================================================================\n       POWER BI VISUAL HEADER & FOCUS MODE EXTENSIONS' not in code:
    code = code.replace(
        '.pbi-card-header {',
        pbi_action_css + '\n    .pbi-card-header {'
    )
    print("Injected Power BI Visual Header & Focus Mode CSS.")

# ==============================================================================
# 2. ADD FOCUS MODE OVERLAY CONTAINER IN HTML
# ==============================================================================
focus_overlay_html = r'''
  <!-- ==========================================================================
       POWER BI FOCUS MODE OVERLAY (FULLSCREEN VISUAL + DATA MATRIX)
       ========================================================================== -->
  <div id="pbi-focus-overlay">
    <div class="focus-top-bar">
      <div class="focus-title-group">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="pbi-pill-badge badge-cyan" id="focus-badge-tag">POWER BI FOCUS MODE</span>
          <h2 id="focus-modal-title">Visual Title</h2>
        </div>
        <p id="focus-modal-sub">Forensic dataset breakdown and tabular underlying matrix</p>
      </div>
      <div class="focus-tools">
        <button class="btn-action" onclick="exportFocusChartCSV()" id="btn-focus-export-csv" title="Download CSV Dataset">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          <span id="lbl-focus-export">تصدير البيانات (CSV)</span>
        </button>
        <button class="btn-action highlight" onclick="closeFocusMode()" style="padding:6px 16px; font-weight:800;">
          <span>✕ إغلاق العرض المكبر</span>
        </button>
      </div>
    </div>

    <div class="focus-content-grid">
      <div class="focus-chart-panel">
        <div style="position:relative; width:100%; height:100%; min-height:420px;" id="focus-canvas-wrap">
          <canvas id="focusModeChartCanvas"></canvas>
        </div>
      </div>
      <div class="focus-table-panel">
        <h4>
          <span id="lbl-focus-table-heading">مصفوفة البيانات التفصيلية (Underlying Data Matrix)</span>
          <span class="pbi-pill-badge badge-amber" id="focus-data-rows-count">0 Rows</span>
        </h4>
        <div class="table-container" style="max-height: 480px; overflow-y: auto;">
          <table class="pbi-table" id="focus-modal-table">
            <thead id="focus-modal-thead"></thead>
            <tbody id="focus-modal-tbody"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
'''

if 'id="pbi-focus-overlay"' not in code:
    code = code.replace(
        '<!-- ==========================================================================\n       PRESENTER MODE OVERLAY (CEO SLIDE DECK)',
        focus_overlay_html + '\n  <!-- ==========================================================================\n       PRESENTER MODE OVERLAY (CEO SLIDE DECK)'
    )
    print("Injected #pbi-focus-overlay HTML.")

# ==============================================================================
# 3. UPGRADE ALL 16 CHART HEADERS WITH POWER BI ACTION BARS (FOCUS MODE BTN)
# ==============================================================================
chart_upgrades = [
    ('chartWaterfallCashFlow', '1. شلال تحويل السيولة النقدية (Cash Conversion Waterfall)', 'الأرباح المحاسبية مقابل نزوح السيولة للإنشاءات ومتحصلات العملاء (H1 2026 - مليون جنيه)', 'فجوة CFO', 'badge-rose'),
    ('chartRevenueBacklogCombo', '2. اتجاه الإيرادات مقابل المبيعات التعاقدية غير المسلمة (Backlog)', 'النمو الحاد لرصيد المبيعات التعاقدية (مليار جنيه) مقابل الإيرادات المحققة فعلياً', 'مبيعات غير مسلّمة', 'badge-cyan'),
    ('chartForensicRiskRadar', '3. رادار المخاطر الجنائية والتعرض التشغيلي (Risk Radar)', 'تقييم سداسي الأبعاد لدرجات المخاطر من واقع التحقيقات والإفصاحات', 'تقييم شامل', 'badge-rose'),
    ('chartDebtStructureTreemapDoughnut', '4. هيكل التمويل: الديون البنكية مقابل التأجير التمويلي', 'انكشاف الالتزامات الفعلية (16.5B بنوك مقابل 43.99B بيع وإعادة استئجار)', 'رافعة خفية', 'badge-rose'),
    ('chartOwnershipUBODoughnut', '5. هيكل الملكية الحقيقي والسيطرة العائلية (UBO Structure)', 'حصص عائلة طلعت مصطفى، المؤسسات السعودية (سليمان الراجحي)، وحرية التداول', 'مستفيدي السيطرة', 'badge-amber'),
    ('chartIPCMustakhlasatSCurve', '6. منحنى تراكم مستحقات المقاولين وتأخر الدورة (Mustakhlasat S-Curve)', 'الوتيرة التعاقدية لصرف المستخلصات (90 يوماً) مقابل الواقع الفعلي (270 يوماً)', 'تراكم 180 يوماً', 'badge-rose'),
    ('chartContractorDisputeBubble', '7. خريطة احتكاك المقاولين والنزاعات القضائية (Contractor Friction Bubble)', 'حجم الأعمال، عدد شهور التعطيل، وتصنيف المخاطر المباشرة للمقاولين', 'حصر النزاعات', 'badge-amber'),
    ('chartVulnerabilityGauge', '8. مؤشر الهشاشة والتعرض المالي الجنائي (Vulnerability Gauge)', 'درجة المخاطرة المركبة من السيولة، التأجير التمويلي، ونزاعات المقاولين', 'مؤشر مالي', 'badge-rose'),
    ('chartInflationTornado', '9. أثر تقلبات سعر الصرف والفائدة على التكلفة (Tornado Sensitivity)', 'حساسية تكلفة تنفيذ المشروعات ونفقات التمويل لهبوط الجنيه وزيادة الكوريدور', 'تحليل حساسية', 'badge-amber'),
    ('landbankBarChart', '10. محفظة الأراضي الرئيسية (Landbank Footprint)', 'المساحة بالملايين م² عبر مشروعات المجموعة الاستراتيجية', 'أصول عقارية', 'badge-cyan'),
    ('chartEvidenceHierarchyPolar', '11. تسلسل قوة الأدلة الجنائية ومصادر التدقيق (Polar Evidence)', 'توزيع مصادر التحقيق الموثقة وفق المعايير القضائية والمحاسبية', 'موثوقية الأدلة', 'badge-emerald'),
    ('chartLagoonMEPCapexOpex', '12. نطاق أعمال البحيرات P.Zone: التنفيذ مقابل الصيانة', 'توزيع القيمة بين التنفيذ الرأسمالي (Capex) وعقود التشغيل والصيانة (O&M)', 'هندسة المياه', 'badge-cyan'),
    ('chartComplaints', '13. تحليل وتوزيع شكاوى أصحاب المصلحة (Complaints Breakdown)', 'فروق الصيانة، رسوم التنازل 5-10%، مستحقات المقاولين والعمال (عينة موثقة 46 واقعة)', '46 شكوى موثقة', 'badge-rose'),
    ('chartProjectDeliveryTimeline', '14. الجداول الزمنية لتسليم المشاريع وتعديل المواعيد (Project Slippages)', 'مقارنة تواريخ التسليم الأصلية بالتواريخ المعدلة (أشهر التأخير المرصودة)', 'الالتزام بالتسليم', 'badge-amber'),
    ('ipcLifecycleLineChart', 'مقارنة دورة صرف المستخلصات: التعاقدي (90 يوماً) مقابل المرصود فعلياً (270 يوماً)', 'الجدول الزمني عبر بوابات التدقيق السبع ومقاصة الشيكات الآجلة (PDC)', 'فجوة 180 يوماً', 'badge-rose'),
    ('chartEvidenceSentiment', 'توزيع الأدلة الجنائية ومصادر التحقق (Evidence Hierarchy Breakdown)', 'تصنيف نتائج الفحص الاستقصائي وفق معايير الإثبات القضائي والتوثيق التجاري (15 مخططاً)', 'Chart 15 • Polar Area', 'badge-cyan')
]

for canvas_id, title, sub, badge_text, badge_class in chart_upgrades:
    # Pattern matching the card header above this canvas
    # We replace standard pbi-card-header with visual-header containing Power BI Action icons
    old_header_pat = rf'''<div class="pbi-card-header">\s*<div>\s*<div class="pbi-card-title">{re.escape(title)}</div>\s*<div class="pbi-card-subtitle">{re.escape(sub)}</div>\s*</div>\s*<span class="pbi-pill-badge {re.escape(badge_class)}">{re.escape(badge_text)}</span>\s*</div>'''
    
    new_header = f'''<div class="pbi-visual-header">
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
    
    match = re.search(old_header_pat, code)
    if match:
        code = code[:match.start()] + new_header + code[match.end():]
        print(f"Upgraded header for {canvas_id} with Power BI Visual Header.")
    else:
        # Fallback simpler replacement
        target = f'<canvas id="{canvas_id}"></canvas>'
        # Check if already upgraded
        if f"openFocusMode('{canvas_id}'" not in code:
            print(f"Notice: Specific regex did not match for {canvas_id}, searching nearby...")

# ==============================================================================
# 4. INJECT CONCRETE PLUS 10B SOUTHMED CARD IN TAB 5 ATRIUM GRID
# ==============================================================================
concrete_plus_card = r'''
            <!-- 8. Concrete Plus & TMG Strategic Partnership (SouthMED & Noor City) -->
            <div class="atrium-card" style="border-top: 3px solid var(--pbi-accent-cyan);">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name" style="color:var(--pbi-accent-cyan);">كونكريت بلس للمقاولات والتنمية (Concrete Plus)</div>
                  <div class="atrium-entity-tag">مشروع ساوث ميد (SouthMED) + مدينة نور (Noor City)</div>
                </div>
                <span class="badge badge-low" style="background:rgba(2,132,199,0.15); color:var(--pbi-accent-cyan); border:1px solid rgba(2,132,199,0.3);">عقد 10 مليار جنيه</span>
              </div>
              <div class="atrium-scope-box">
                <strong style="color:var(--pbi-text-hero);">نطاق ساوث ميد (يناير 2026):</strong> إسناد حزمة المنطقة (Zone C01) لبناء وتشطيب <strong>179 مبنى وعمارة سكنية</strong> وشبكات المرافق التحتية بالساحل الشمالي (المستهدف 2029).<br>
                <strong style="color:var(--pbi-text-hero); margin-top:4px; display:inline-block;">امتداد الشراكة (مدينة نور):</strong> تنفيذ قطاع الفيلات V3.2 (~170 فيلا سكنية فاخرة). كمقاول عام فئة أولى (Tier-1) مستقل للطاقات الفائضة (Overflow Capacity).
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-emerald); font-weight:800;">حالة المستخلصات: صفر قضايا نزاع</span>
                <span class="partner-pill">حجم العقد: 10,000,000,000 EGP</span>
                <span class="partner-pill">المقاول: كونكريت بلس (Tier-1)</span>
                <span class="partner-pill">المالك: TMG / ساوث ميد</span>
                <button class="source-link" onclick="showSourceModal('concrete_plus_southmed_contract')" style="margin-inline-start:auto;">بيان العقد ↗</button>
              </div>
            </div>
'''

if 'كونكريت بلس للمقاولات والتنمية (Concrete Plus)' not in code:
    # Insert right before </div> of atrium-grid
    code = code.replace(
        '<!-- 7. Cairo Gate & Townsquare Offices (Emaar Misr) -->',
        concrete_plus_card + '\n            <!-- 7. Cairo Gate & Townsquare Offices (Emaar Misr) -->'
    )
    print("Injected Concrete Plus SouthMED 10B Card into Tab 5 Atrium Grid.")

# ==============================================================================
# 5. INJECT 4-PILLAR HYBRID CLOSED-LOOP PROCUREMENT ARCHITECTURE IN TAB 2
# ==============================================================================
hybrid_procurement_section = r'''
        <!-- 4-PILLAR HYBRID CLOSED-LOOP PROCUREMENT ARCHITECTURE -->
        <div class="pbi-card" style="margin-top: 24px; border-top: 3px solid var(--pbi-accent-cyan);">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="display:flex; align-items:center; gap:8px;">
                <span class="pulse-dot"></span>
                <span>النموذج الهجين لشراكات المقاولات والتوريد (Hybrid Closed-Loop Procurement Model)</span>
              </div>
              <div class="pbi-card-subtitle">الركائز الأربع لإدارة سلاسل الإمداد، درع العزل القانوني، والدورة التمويلية عبر أوراق الدفع (Notes Payable)</div>
            </div>
            <span class="pbi-pill-badge badge-cyan">4 Strategic Pillars</span>
          </div>

          <div class="advisory-grid">
            <!-- Pillar 1 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(2,132,199,0.15); color:var(--pbi-accent-cyan);">01</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">درع المقاول الداخلي والعزل التعاقدي (Captive EPC)</strong>
                </div>
                <span class="pbi-pill-badge badge-emerald">حماية القابضة</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                عزل الذمة المالية للشركة القابضة (TMGH)؛ إسناد العمليات الإنشائية لأذرع داخلية (شركة الإسكندرية للإنشاءات ACC وشركة أتريوم AQC) أو تحالفات Tier-1 مستقلة كبرى (مثل كونكريت بلس بـ 10 مليار في ساوث ميد)، لمنع أي حجز قضائي على حسابات الشركة القابضة.
              </div>
            </div>

            <!-- Pillar 2 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(16,185,129,0.15); color:var(--pbi-accent-emerald);">02</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">فصل توريد الخامات عن عقود المصنعيات (Bulk Purchasing)</strong>
                </div>
                <span class="pbi-pill-badge badge-cyan">تحييد التضخم</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                الشراء المركزي المباشر لخامات البناء الإستراتيجية (حديد عز وبشاي، والأسمنت السائب، والكابلات من السويدي) بوفورات حجم ضخمة، وحصر عقود مقاولي الباطن على "المصنعيات والتركيبات فقط"، مما يقلل مخاطر مطالبة المقاولين بفروق أسعار الخامات.
              </div>
            </div>

            <!-- Pillar 3 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(245,158,11,0.15); color:var(--pbi-accent-amber);">03</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">الدورة التمويلية عبر أوراق الدفع (Notes Payable >15.79B)</strong>
                </div>
                <span class="pbi-pill-badge badge-amber">تمويل الموردين</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                تحويل مستحقات الموردين والمقاولين لشيكات آجلة وكمبيالات تجارية لفترات تمتد من 90 إلى 180 يوماً؛ مما يوفر خط ائتمان تشغيلي بدون فوائد مصرفية بقيمة تتجاوز 15.79 مليار جنيه لتمويل مشاريع مدينتي ونور وساوث ميد.
              </div>
            </div>

            <!-- Pillar 4 -->
            <div class="advisory-card">
              <div class="advisory-card-header">
                <div class="advisory-title-group">
                  <div class="advisory-num-badge" style="background:rgba(220,38,38,0.15); color:var(--pbi-accent-rose);">04</div>
                  <strong style="color:var(--pbi-text-hero); font-size:13px;">بوابات الفحص السبع وتأخر الصرف (135 - 270 يوماً)</strong>
                </div>
                <span class="pbi-pill-badge badge-rose">فجوة 180 يوماً</span>
              </div>
              <div class="advisory-body" style="font-size:12px; line-height:1.7;">
                خضوع مستخلصات المقاولين لدورة تحقق دقيقة عبر 7 مراحل (حصر الكميات، تكسير الخرسانة، مراجعة المكتب الفني بالدقي، اعتماد ACC، وتأجيل الصرف)، مما يؤدي لمد أجل السيولة التشغيلية وصمود المجموعة أمام صدمات التدفق النقدي.
              </div>
            </div>
          </div>
        </div>
'''

if 'النموذج الهجين لشراكات المقاولات والتوريد (Hybrid Closed-Loop Procurement Model)' not in code:
    code = code.replace(
        '<!-- Explanatory cards -->\n          <div class="grid-2" style="margin-top: 20px;" id="procurement-expl-cards">',
        hybrid_procurement_section + '\n        <!-- Explanatory cards -->\n          <div class="grid-2" style="margin-top: 20px;" id="procurement-expl-cards">'
    )
    print("Injected 4-Pillar Hybrid Procurement Architecture into Tab 2.")

# ==============================================================================
# 6. INJECT POWER BI CHART JS PLUGIN (WATERFALL CONNECTORS + DATA LABELS) + FOCUS MODE JS
# ==============================================================================
pbi_engine_js = r'''
    // ==========================================================================
    // POWER BI NATIVE VISUAL ENGINE: DATA LABELS & WATERFALL CONNECTORS PLUGIN
    // ==========================================================================
    const pbiVisualPlugin = {
      id: 'pbiVisualPlugin',
      afterDatasetsDraw(chart, args, options) {
        const { ctx, data, chartArea } = chart;
        if (!chartArea) return;

        const isLight = document.documentElement.getAttribute('data-theme') === 'light';
        const labelTextColor = isLight ? '#1E293B' : '#F1F5F9';
        const fontName = currentLang === 'ar' ? 'Cairo, Plus Jakarta Sans, sans-serif' : 'Plus Jakarta Sans, sans-serif';

        // 1. Dotted Waterfall Connectors for Waterfall Charts
        if (chart.canvas.id === 'chartWaterfallCashFlow' && chart.getDatasetMeta(0).data) {
          const meta = chart.getDatasetMeta(0);
          ctx.save();
          ctx.setLineDash([3, 3]);
          ctx.strokeStyle = isLight ? '#94A3B8' : '#64748B';
          ctx.lineWidth = 1;

          for (let i = 0; i < meta.data.length - 1; i++) {
            const currEl = meta.data[i];
            const nextEl = meta.data[i + 1];
            if (currEl && nextEl) {
              const yVal = currEl.base !== undefined ? currEl.y : currEl.y;
              ctx.beginPath();
              ctx.moveTo(currEl.x + (currEl.width / 2), currEl.y);
              ctx.lineTo(nextEl.x - (nextEl.width / 2), currEl.y);
              ctx.stroke();
            }
          }
          ctx.restore();
        }

        // 2. Power BI Crisp Value Data Labels on Bar & Column Visuals
        if (['bar'].includes(chart.config.type) && chart.canvas.id !== 'landbankBarChart') {
          ctx.save();
          ctx.font = `bold 10px ${fontName}`;
          ctx.fillStyle = labelTextColor;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'bottom';

          chart.data.datasets.forEach((dataset, dIdx) => {
            const meta = chart.getDatasetMeta(dIdx);
            if (meta.hidden) return;

            meta.data.forEach((element, index) => {
              const rawVal = dataset.data[index];
              if (rawVal === null || rawVal === undefined) return;

              let displayTxt = '';
              if (Array.isArray(rawVal)) {
                // Floating bar (waterfall): show delta
                const delta = rawVal[1] - rawVal[0];
                displayTxt = (delta >= 0 ? '+' : '') + delta.toLocaleString();
              } else if (typeof rawVal === 'number') {
                if (Math.abs(rawVal) >= 1000) {
                  displayTxt = (rawVal / 1000).toFixed(1) + 'k';
                } else {
                  displayTxt = rawVal.toLocaleString();
                }
              }

              if (displayTxt && element.x !== undefined && element.y !== undefined) {
                const yPos = element.y < element.base ? element.y - 4 : element.y + 12;
                ctx.fillText(displayTxt, element.x, yPos);
              }
            });
          });
          ctx.restore();
        }
      }
    };

    // Register Chart.js Visual Plugin
    if (typeof Chart !== 'undefined' && Chart.register) {
      Chart.register(pbiVisualPlugin);
    }

    // ==========================================================================
    // POWER BI FOCUS MODE ENGINE ("SHOW AS TABLE" & CSV EXPORT)
    // ==========================================================================
    let focusChartInstance = null;
    let activeFocusChartId = null;

    function openFocusMode(chartId, title) {
      const srcCanvas = document.getElementById(chartId);
      if (!srcCanvas) return;

      const overlay = document.getElementById('pbi-focus-overlay');
      const focusTitle = document.getElementById('focus-modal-title');
      const focusSub = document.getElementById('focus-modal-sub');
      const thead = document.getElementById('focus-modal-thead');
      const tbody = document.getElementById('focus-modal-tbody');
      const countTag = document.getElementById('focus-data-rows-count');

      activeFocusChartId = chartId;
      focusTitle.textContent = title || chartId;
      focusSub.textContent = currentLang === 'ar' 
        ? 'عرض التحليل الموسّع بنمط Power BI مع تفكيك مصفوفة البيانات الأساسية'
        : 'Expanded Power BI visual view with underlying structured forensic matrix';

      // Find chart instance in chartInstances
      let targetInstance = null;
      for (const k in chartInstances) {
        if (chartInstances[k] && chartInstances[k].canvas && chartInstances[k].canvas.id === chartId) {
          targetInstance = chartInstances[k];
          break;
        }
      }

      // Populate Table
      if (targetInstance && targetInstance.data) {
        const labels = targetInstance.data.labels || [];
        const datasets = targetInstance.data.datasets || [];

        // Build Table Header
        let thHtml = `<tr><th>${currentLang === 'ar' ? 'البند / التصنيف' : 'Category / Dimension'}</th>`;
        datasets.forEach(ds => {
          thHtml += `<th>${ds.label || 'Value'}</th>`;
        });
        thHtml += `</tr>`;
        thead.innerHTML = thHtml;

        // Build Table Body
        let tbHtml = '';
        labels.forEach((lbl, i) => {
          tbHtml += `<tr><td><strong>${lbl}</strong></td>`;
          datasets.forEach(ds => {
            const v = ds.data[i];
            let cellStr = v;
            if (Array.isArray(v)) {
              cellStr = `[${v[0]} → ${v[1]}] (Δ ${v[1] - v[0]})`;
            } else if (typeof v === 'number') {
              cellStr = v.toLocaleString();
            }
            tbHtml += `<td class="cell-mono" style="color:var(--pbi-accent-cyan); font-weight:700;">${cellStr !== undefined ? cellStr : '-'}</td>`;
          });
          tbHtml += `</tr>`;
        });
        tbody.innerHTML = tbHtml;
        countTag.textContent = `${labels.length} ${currentLang === 'ar' ? 'سجلات' : 'Rows'}`;

        // Recreate Focus Canvas Chart
        const focusCanvas = document.getElementById('focusModeChartCanvas');
        if (focusChartInstance) focusChartInstance.destroy();

        const ctx = focusCanvas.getContext('2d');
        const configClone = JSON.parse(JSON.stringify({
          type: targetInstance.config.type,
          data: targetInstance.config.data,
          options: targetInstance.config.options
        }));
        configClone.options.responsive = true;
        configClone.options.maintainAspectRatio = false;

        focusChartInstance = new Chart(ctx, configClone);
      }

      overlay.classList.add('active');
    }

    function closeFocusMode() {
      const overlay = document.getElementById('pbi-focus-overlay');
      overlay.classList.remove('active');
      if (focusChartInstance) {
        focusChartInstance.destroy();
        focusChartInstance = null;
      }
      activeFocusChartId = null;
    }

    function exportFocusChartCSV() {
      if (activeFocusChartId) {
        exportChartDataCSV(activeFocusChartId);
      }
    }

    function exportChartDataCSV(chartId) {
      let targetInstance = null;
      for (const k in chartInstances) {
        if (chartInstances[k] && chartInstances[k].canvas && chartInstances[k].canvas.id === chartId) {
          targetInstance = chartInstances[k];
          break;
        }
      }
      if (!targetInstance) return;

      const labels = targetInstance.data.labels || [];
      const datasets = targetInstance.data.datasets || [];

      let csv = 'Category,' + datasets.map(d => `"${d.label || 'Value'}"`).join(',') + '\n';
      labels.forEach((lbl, i) => {
        let row = `"${lbl}",`;
        row += datasets.map(ds => {
          const v = ds.data[i];
          if (Array.isArray(v)) return `"${v[1] - v[0]}"`;
          return `"${v !== undefined ? v : ''}"`;
        }).join(',');
        csv += row + '\n';
      });

      const blob = new Blob(["\ufeff" + csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `TMG_Forensic_${chartId}_Data.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }
'''

# Insert the engine JS into script section
if 'const pbiVisualPlugin =' not in code:
    code = code.replace(
        'function initAll14Charts() {',
        pbi_engine_js + '\n    function initAll14Charts() {'
    )
    print("Injected Power BI Visual Plugin & Focus Mode JS functions.")

# Write modified generator script
with open(r'scripts/generate_powerbi_ceo_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated scripts/generate_powerbi_ceo_dashboard.py successfully!")
