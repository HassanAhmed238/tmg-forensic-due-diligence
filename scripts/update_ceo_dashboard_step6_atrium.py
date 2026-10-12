# -*- coding: utf-8 -*-
"""
Update generate_powerbi_ceo_dashboard.py to incorporate:
1. TMG_Contractor_Sentiment_Step6 (2).md
2. TMG_Atrium_Expanded_Contractor_Network_Review.md
With PowerBI Executive Light Canvas, UI-Motion, UI-UX-Pro-Max polish, and Chart 15.
"""

with open(r"F:\Mr Hesham\TMG\scripts\generate_powerbi_ceo_dashboard.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add CSS for Atrium Network, Sentiment Pillars, and 8-point Checklist
css_addition = '''
    /* UI MOTION & UI-UX-PRO-MAX STYLING EXTENSIONS */
    .atrium-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }
    @media (max-width: 1200px) {
      .atrium-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
      .atrium-grid { grid-template-columns: 1fr; }
    }
    .atrium-card {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 12px;
      box-shadow: var(--pbi-card-shadow);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }
    .atrium-card:hover {
      transform: translateY(-3px);
      border-color: var(--pbi-accent-cyan);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }
    .atrium-card::before {
      content: '';
      position: absolute;
      top: 0;
      inset-inline: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--pbi-accent-cyan), var(--pbi-accent-blue));
    }
    .atrium-card-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
    }
    .atrium-proj-name {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--pbi-text-hero);
    }
    .atrium-entity-tag {
      font-size: 10.5px;
      font-weight: 700;
      color: var(--pbi-accent-cyan);
      font-family: var(--pbi-font-mono);
    }
    .atrium-scope-box {
      background: var(--pbi-surface-elevated);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 11.5px;
      color: var(--pbi-text-main);
      line-height: 1.6;
    }
    .atrium-partners-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }
    .partner-pill {
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      background: var(--pbi-surface-sunken);
      border: 1px solid var(--pbi-border-highlight);
      color: var(--pbi-text-main);
    }

    /* Sentiment 4-Pillar Grid */
    .sentiment-pillars-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-bottom: 24px;
    }
    @media (max-width: 1200px) {
      .sentiment-pillars-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
      .sentiment-pillars-grid { grid-template-columns: 1fr; }
    }
    .sentiment-pillar-card {
      background: var(--pbi-surface-card);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: var(--pbi-card-shadow);
      position: relative;
      overflow: hidden;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .sentiment-pillar-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }
    .pillar-card-emerald { border-inline-start: 4px solid var(--pbi-accent-emerald); }
    .pillar-card-amber { border-inline-start: 4px solid var(--pbi-accent-amber); }
    .pillar-card-purple { border-inline-start: 4px solid var(--pbi-accent-purple); }
    .pillar-card-rose { border-inline-start: 4px solid var(--pbi-accent-rose); }

    .pillar-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .pillar-title {
      font-size: 12px;
      font-weight: 800;
      color: var(--pbi-text-hero);
    }
    .pillar-badge {
      font-size: 10px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
    }
    .pillar-desc {
      font-size: 11.5px;
      color: var(--pbi-text-muted);
      line-height: 1.6;
    }
    .pillar-examples {
      font-size: 11px;
      font-weight: 700;
      color: var(--pbi-text-main);
      border-top: 1px dashed var(--pbi-border-subtle);
      padding-top: 8px;
    }

    /* 8-Point Checklist Styling */
    .checklist-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-top: 14px;
    }
    @media (max-width: 1200px) {
      .checklist-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .checklist-grid { grid-template-columns: 1fr; }
    }
    .checklist-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 12px 14px;
      background: var(--pbi-surface-elevated);
      border: 1px solid var(--pbi-border-subtle);
      border-radius: 10px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .checklist-item:hover {
      border-color: var(--pbi-accent-cyan);
      transform: translateX(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .checklist-icon {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(16, 185, 129, 0.15);
      color: var(--pbi-accent-emerald);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 900;
      flex-shrink: 0;
      margin-top: 2px;
    }
    .checklist-text {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .checklist-title {
      font-size: 11.5px;
      font-weight: 800;
      color: var(--pbi-text-hero);
    }
    .checklist-sub {
      font-size: 10.5px;
      color: var(--pbi-text-muted);
      line-height: 1.45;
    }

    /* Pulse Glow Animation */
    @keyframes pulse-glow {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.6; }
      100% { transform: scale(1); opacity: 1; }
    }
    .pulse-dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--pbi-accent-emerald);
      animation: pulse-glow 2s infinite ease-in-out;
      margin-inline-end: 6px;
    }
'''

if 'atrium-grid' not in code:
    code = code.replace("  </style>", css_addition + "\n  </style>")
    print("Added CSS extensions.")

# 2. Replace Tab 5: Contractors with full Atrium Network & Diligence Matrix
tab5_old = '''      <!-- ==========================================================================
           TAB 5: CONTRACTORS ROSTER
           ========================================================================== -->
      <div id="tab-contractors" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-cont-title">سجل المقاولين الرئيسيين ومقاولي الباطن وسلاسل الإمداد</div>
              <div class="pbi-card-subtitle" id="t-cont-sub">خريطة التعاقدات المنفذة عبر شركة الإسكندرية وأتريوم والمقاولين المستقلين</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="contractors-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="contractors-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>'''

tab5_new = '''      <!-- ==========================================================================
           TAB 5: CONTRACTORS ROSTER & ATRIUM EXPANDED NETWORK
           ========================================================================== -->
      <div id="tab-contractors" class="tab-pane">
        <!-- Section A: Atrium Quality Contractors (AQC) Multi-Tier JV Network Matrix -->
        <div class="pbi-card" style="margin-bottom:20px;">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="display:flex; align-items:center;">
                <span class="pulse-dot"></span>
                <span id="lbl-atrium-matrix-title">شبكة شركة أتريوم للمقاولات (Atrium AQC) والتحالفات المشتركة</span>
              </div>
              <div class="pbi-card-subtitle" id="lbl-atrium-matrix-sub">تحليل حزم المقاول العام المتكامل، تحالفات MEP، مقاولي الباطن المتخصصين، وكبرى مكاتب الإشراف الهندسي</div>
            </div>
            <span class="pbi-pill-badge badge-cyan" id="lbl-atrium-badge">6 مشروعات كبرى • تحالفات دولية</span>
          </div>

          <div class="atrium-grid">
            <!-- 1. Four Seasons Luxor -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">فندق فورسيزونز الأقصر (Four Seasons Luxor)</div>
                  <div class="atrium-entity-tag">آيكون (ICON) / إيجوث (EGOTH) / TMG</div>
                </div>
                <span class="badge badge-low">EPC Turnkey</span>
              </div>
              <div class="atrium-scope-box">
                المقاول العام المتكامل للمشروع الفندقي الفاخر؛ تشكيل تحالف استراتيجي مع CCC Electromechanical لتنفيذ الحزمة الكهروميكانيكية الرئيسية (CP02).
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-blue); font-weight:800;">JV: CCC Electromechanical</span>
                <span class="partner-pill">إدارة: Hill International</span>
                <span class="partner-pill">استشاري: مجموعة شاكر</span>
                <span class="partner-pill">مورد: كناوف مصر (Knauf)</span>
                <span class="partner-pill">تصميم: معمار إنتريرز</span>
              </div>
            </div>

            <!-- 2. Four Seasons Cairo Capital -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">فورسيزونز نيو كايرو كابيتال (مدينتي)</div>
                  <div class="atrium-entity-tag">مدينتي للمشروعات السياحية / آيكون</div>
                </div>
                <span class="badge badge-low">Package CP05</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ حزمة الفندق الرئيسية CP05 عبر تحالف أتريوم وCCC المشترك؛ اعتماد واستلام المواد (MIR-11) وتصميمات الإضاءة عبر شراكة ممتدة 25 عاماً.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-blue); font-weight:800;">JV: Atrium-CCC Consortium</span>
                <span class="partner-pill">باطن: Devzah SI</span>
                <span class="partner-pill">إشراف: Hill International</span>
                <span class="partner-pill">إضاءة: Andy Lang (LLD)</span>
              </div>
            </div>

            <!-- 3. Open Air Mall Madinaty -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">أوبن إير مول مدينتي (Open Air Mall)</div>
                  <div class="atrium-entity-tag">الشركة العربية للمشروعات (ACPUD)</div>
                </div>
                <span class="badge badge-low">Commercial EPC</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ المركز التجاري الأكبر؛ إسناد تصنيع وتوريد وتركيب الجمالونات والهياكل الإنشائية الحديدية لشركة إيفرلاست للمقاولات كباطن متخصص.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-cyan); font-weight:800;">باطن: Everlast Construction</span>
                <span class="partner-pill">استشاري: جماعة المهندسين (ECG)</span>
                <span class="partner-pill">المقاول العام: Atrium AQC</span>
              </div>
            </div>

            <!-- 4. East Hub Madinaty -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">إيست هب مول مدينتي (East Hub Mall)</div>
                  <div class="atrium-entity-tag">الشركة العربية للمشروعات (ACPUD)</div>
                </div>
                <span class="badge badge-low">Fit-out & MEP</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ أعمال التشطيبات المتكاملة، الواجهات المعمارية، شبكات MEP، وتوريد أنظمة الإضاءة المعمارية المتطورة من شركة سراج للإضاءة.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill">إدارة: دار الهندسة (EHAF)</span>
                <span class="partner-pill">إضاءة: Siraj Lighting</span>
                <span class="partner-pill">شراكة: سكوير (SQUARE)</span>
                <span class="partner-pill">تنفيذ: MCBS</span>
              </div>
            </div>

            <!-- 5. Celia New Capital -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">مشروع سيليا (العاصمة الإدارية الجديدة)</div>
                  <div class="atrium-entity-tag">الشركة العربية للمشروعات (ACPUD)</div>
                </div>
                <span class="badge badge-med">Villages & Services</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ حزم الفيلات وقرى سيليا السكنية ومراكز الخدمات والبنية التحتية واللاندسكيب بإشراف استشاري حمزة وشركاه، مع عزل تعاقدي يحمي القابضة.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill">استشاري: حمزة وشركاه (Hamza)</span>
                <span class="partner-pill">المقاول العام: Atrium AQC</span>
                <span class="partner-pill">المالك: العربية للمشروعات</span>
              </div>
            </div>

            <!-- 6. Noor Smart City -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">مدينة نور الذكية (حدائق العاصمة)</div>
                  <div class="atrium-entity-tag">الشركة العربية للاستثمار العمراني</div>
                </div>
                <span class="badge badge-low">Smart Superstructures</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ حزمة 72 عمارة سكنية وفيلات فاخرة؛ توريد خلايا الجهد المتوسط الذكية Simoprime 24 kV من إيماس السويدي بإشراف مجموعة شاكر.
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill">مورد: إيماس السويدي (EMAS)</span>
                <span class="partner-pill">استشاري: مجموعة شاكر (Shaker)</span>
                <span class="partner-pill">حزم الفيلات: كونكريت بلس</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Section B: Primary Contractors & Subcontractors Searchable Table -->
        <div class="pbi-card" style="margin-bottom:20px;">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-cont-title">سجل المقاولين الرئيسيين ومقاولي الباطن وسلاسل الإمداد</div>
              <div class="pbi-card-subtitle" id="t-cont-sub">خريطة التعاقدات المنفذة عبر شركة الإسكندرية وأتريوم والمقاولين المستقلين والموردين</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="contractors-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="contractors-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section C: 8-Point Documentary Diligence Checklist for CEO -->
        <div class="pbi-card" style="background:var(--pbi-surface-sunken); border:1px solid var(--pbi-border-highlight);">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" style="color:var(--pbi-accent-cyan);">قائمة التحقق المستندي الثمانية لعقود المقاولات (8-Point Forensic Checklist)</div>
              <div class="pbi-card-subtitle">المستندات الإلزامية المطلوب فحصها قبل توقيع أي صفقة أو تسوية مستحقات لفصل النزاعات التاريخية عن الالتزامات النافذة</div>
            </div>
            <span class="pbi-pill-badge badge-emerald">معايير فحص العناية الواجبة (Due Diligence)</span>
          </div>

          <div class="checklist-grid">
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">1. العقد الموقع وأمر الإسناد</div>
                <div class="checklist-sub">فحص الكيان القانوني الموقع وتحديد بنود الدفع وغرامات التأخير.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">2. تقويم ومدد الاعتماد</div>
                <div class="checklist-sub">تدقيق المدى الزمني لحصر الكميات بالموقع وتوقيع مهندسي الإشراف.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">3. سجل المستخلصات الجارية (IPC)</div>
                <div class="checklist-sub">تتبع تواريخ التقديم، الاعتماد الهندسي، تاريخ الاستحقاق الفعلي، وتاريخ التحصيل.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">4. سجل مبالغ الضمان (Retention)</div>
                <div class="checklist-sub">بيان نسبة الـ 5-10% المحتجزة وتاريخ استحقاق الإفراج الابتدائي والنهائي.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">5. سجل الأوامر التغييرية (VOs)</div>
                <div class="checklist-sub">فصل الأعمال الإضافية المعتمدة رسمياً عن المطالبات الشفهية غير المسندة.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">6. سجل الاستقطاعات والجزاءات</div>
                <div class="checklist-sub">حصر الخصومات المطبقة على مقاولي الباطن وأسبابها الهندسية المعتمدة.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">7. مخالصة الحساب الختامي</div>
                <div class="checklist-sub">تسوية الحسابات الختامية الموقعة بين المقاول العام والكيان التابع.</div>
              </div>
            </div>
            <div class="checklist-item">
              <div class="checklist-icon">✓</div>
              <div class="checklist-text">
                <div class="checklist-title">8. شهادة إبراء الذمة (Close-Out)</div>
                <div class="checklist-sub">استلام شهادة إخلاء الطرف النهائية وانقضاء مدة الضمان العشري أو الصيانة.</div>
              </div>
            </div>
          </div>
        </div>
      </div>'''

if 'lbl-atrium-matrix-title' not in code:
    code = code.replace(tab5_old, tab5_new)
    print("Replaced Tab 5 with Atrium Matrix & 8-point checklist.")

# 3. Replace Tab 8: Sentiment with 4-Pillar Matrix and Chart 15
tab8_old = '''      <!-- ==========================================================================
           TAB 8: CUSTOMER & LABOR SENTIMENT
           ========================================================================== -->
      <div id="tab-sentiment" class="tab-pane">
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-sent-table-title">سجل الشكاوى التفصيلي: المقاولون، عمال المقاولات، واتحادات السكان</div>
              <div class="pbi-card-subtitle" id="t-sent-table-sub">يتضمن واقعة مقاول مدينتي التاريخية، احتجاجات عمال الإسكندرية للإنشاءات، وبلاغات الملاك</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="complaints-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="complaints-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>'''

tab8_new = '''      <!-- ==========================================================================
           TAB 8: CUSTOMER & LABOR SENTIMENT & CONTRACTOR INTELLIGENCE
           ========================================================================== -->
      <div id="tab-sentiment" class="tab-pane">
        <!-- 4-Pillar Sentiment & Attribution Hierarchy Cards -->
        <div class="sentiment-pillars-grid">
          <!-- Pillar 1 -->
          <div class="sentiment-pillar-card pillar-card-emerald">
            <div class="pillar-header">
              <div class="pillar-title">1. شراكات مستمرة وتكرار أعمال</div>
              <span class="pillar-badge badge-emerald">Level A/B</span>
            </div>
            <div class="pillar-desc">
              عقود رسمية وشراكات ممتدة تعكس استمرارية تجارية ونجاح تسليم الحزم الكبرى؛ لا تتضمن بيانات علنية عن مدد سداد المستخلصات.
            </div>
            <div class="pillar-examples">
              ● كونكريت بلس (10B ساوث ميد بعد نور)<br>
              ● تحالف CCC وأتريوم (الأقصر والقاهرة)<br>
              ● أندي لانغ LLD (شراكة 25 عاماً)
            </div>
          </div>

          <!-- Pillar 2 -->
          <div class="sentiment-pillar-card pillar-card-amber">
            <div class="pillar-header">
              <div class="pillar-title">2. أجور وظروف العمالة الداخلية</div>
              <span class="pillar-badge badge-amber">Level A/B</span>
            </div>
            <div class="pillar-desc">
              احتجاجات ومذكرات للعاملين والمهندسين وحرس الأمن بشركة الإسكندرية للإنشاءات تخص الرواتب والتأمين؛ سياق عمالي منفصل عن فواتير المقاولين.
            </div>
            <div class="pillar-examples">
              ● 100+ عامل بالإسكندرية (مارس 2024)<br>
              ● 400 مهندس بشركة الإسكندرية (مارس 2024)<br>
              ● حرس أمن مدينتي (أكتوبر 2025)
            </div>
          </div>

          <!-- Pillar 3 -->
          <div class="sentiment-pillar-card pillar-card-purple">
            <div class="pillar-header">
              <div class="pillar-title">3. مخاطر سلاسل الدفع العليا</div>
              <span class="pillar-badge badge-purple">Level D</span>
            </div>
            <div class="pillar-desc">
              ادعاءات أهالي ومقاولي باطن محليين بعدم سداد مستحقات؛ نسبت التقارير التأخير لسداد جهات عليا للمقاولين، دون ثبوت مديونية مباشرة على طلعت مصطفى.
            </div>
            <div class="pillar-examples">
              ● مقاولو باطن ساوث ميد (مدى مصر 2024)<br>
              ● مصدر محلي غير محدد بالاسم<br>
              ● انقطاع الحجية المباشرة مع المطور
            </div>
          </div>

          <!-- Pillar 4 -->
          <div class="sentiment-pillar-card pillar-card-rose">
            <div class="pillar-header">
              <div class="pillar-title">4. مطالبات المستحقات المباشرة</div>
              <span class="pillar-badge badge-rose">Level A/B</span>
            </div>
            <div class="pillar-desc">
              نزاعات موثقة بمحاضر نيابة وقضايا محاكم تخص مستحقات مقاولي باطن مدنيين تجاه المقاول العام المدمج (شركة الإسكندرية للإنشاءات).
            </div>
            <div class="pillar-examples">
              ● شحاتة حسن وبلاغ النيابة (أكتوبر 2008)<br>
              ● اعتراف إبراهيم حسبو بتعمد التعطيل<br>
              ● دعوى 2923/2012 سقالات (609 ألف ج.م)
            </div>
          </div>
        </div>

        <!-- Evidence Classification Chart & Rules Grid -->
        <div class="grid-2" style="margin-bottom:20px;">
          <div class="pbi-card">
            <div class="pbi-card-header">
              <div>
                <div class="pbi-card-title">توزيع الأدلة الجنائية ومصادر التحقق (Evidence Hierarchy Breakdown)</div>
                <div class="pbi-card-subtitle">تصنيف نتائج الفحص الاستقصائي وفق معايير الإثبات القضائي والتوثيق التجاري</div>
              </div>
            </div>
            <div style="height:320px; position:relative;">
              <canvas id="chartEvidenceSentiment"></canvas>
            </div>
          </div>

          <div class="pbi-card">
            <div class="pbi-card-header">
              <div>
                <div class="pbi-card-title">مستويات الإثبات الجنائي وقواعد العزل التعاقدي (Attribution Rules)</div>
                <div class="pbi-card-subtitle">الضوابط القانونية للفصل بين ادعاءات النشر وحقيقة الالتزام المالي على المجموعة</div>
              </div>
            </div>
            <div style="display:flex; flex-direction:column; gap:12px; font-size:12px; line-height:1.7;">
              <div style="padding:10px 14px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-emerald);">
                <strong style="color:var(--pbi-text-hero);">Level A — علاقة تجارية موثقة بمستندات مستقلة:</strong><br>
                تحديد أطراف العقد بدقة (المشروع، النطاق، القيمة)، مثل إفصاحات البورصة، محاضر المحاكم، وعقود التمويل المشترك.
              </div>
              <div style="padding:10px 14px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-cyan);">
                <strong style="color:var(--pbi-text-hero);">Level B — بيانات رسمية صادرة عن الشركات:</strong><br>
                منشورات الشركاء والموردين والمصممين حول إنجاز الأعمال أو توريد المهمات، وهي أدلة استمرارية ولا تثبت تواريخ السداد.
              </div>
              <div style="padding:10px 14px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-amber);">
                <strong style="color:var(--pbi-text-hero);">Level C — تحليلات فنية عامة لصناعة المقاولات:</strong><br>
                دراسات استشارية تشرح أثر تأخر المستخلصات على مقاولي الباطن دون توجيه اتهام مباشر لمجموعة طلعت مصطفى.
              </div>
              <div style="padding:10px 14px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-rose);">
                <strong style="color:var(--pbi-text-hero);">Level D — ادعاءات مجهولة المصدر أو غير مؤيدة:</strong><br>
                أخبار صحفية تنقل عن مصادر مجهولة تأخر دفعات، مع انقطاع السند التعاقدي المباشر مع الشركة القابضة.
              </div>
            </div>
          </div>
        </div>

        <!-- Complaints and Sentiment Table -->
        <div class="pbi-card">
          <div class="pbi-card-header">
            <div>
              <div class="pbi-card-title" id="t-sent-table-title">سجل الشكاوى التفصيلي: المقاولون، عمال المقاولات، واتحادات السكان</div>
              <div class="pbi-card-subtitle" id="t-sent-table-sub">يتضمن واقعة مقاول مدينتي التاريخية، احتجاجات عمال الإسكندرية للإنشاءات، وبلاغات الملاك</div>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr id="complaints-th-row">
                  <!-- Populated via JS -->
                </tr>
              </thead>
              <tbody id="complaints-tbody">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>'''

if 'sentiment-pillars-grid' not in code:
    code = code.replace(tab8_old, tab8_new)
    print("Replaced Tab 8 with Sentiment Pillars & Chart 15.")

# 4. Add Chart 15 initialization inside initAll14Charts
chart15_code = '''
      // 15. Evidence Hierarchy & Contractor Sentiment Breakdown (Polar Area)
      const ctxEvSent = document.getElementById('chartEvidenceSentiment');
      if (ctxEvSent) {
        chartInstances.evSent = new Chart(ctxEvSent.getContext('2d'), {
          type: 'polarArea',
          data: {
            labels: currentLang === 'ar' ? [
              'علاقات تعاقدية وتكرار أعمال (Level A)',
              'إفصاحات توريد وشراكة معلنة (Level B)',
              'احتجاجات أجور وظروف عمل داخلية (Level A/B)',
              'ادعاءات سلاسل إمداد عليا جهات حكومية (Level D)',
              'شكاوى مستحقات تاريخية مباشرة (Level A/B)',
              'معايير ونزاعات قطاع المقاولات العام (Level C)'
            ] : [
              'Documented Commercial Repeat (Level A)',
              'Public Supplier Statement (Level B)',
              'Internal Labor Wage Actions (Level A/B)',
              'Upstream Payer Claims - Armed Forces (Level D)',
              'Direct Historic Contractor Dues (Level A/B)',
              'General Industry Claims Benchmark (Level C)'
            ],
            datasets: [{
              data: [8, 6, 4, 2, 2, 2],
              backgroundColor: [
                'rgba(16, 185, 129, 0.75)',
                'rgba(2, 132, 199, 0.75)',
                'rgba(245, 158, 11, 0.75)',
                'rgba(168, 85, 247, 0.75)',
                'rgba(225, 29, 72, 0.75)',
                'rgba(100, 116, 139, 0.75)'
              ],
              borderWidth: 1,
              borderColor: isLight ? '#FFFFFF' : '#111726'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'right',
                labels: { color: textColor, font: { family: fontFam, size: 9.5 }, boxWidth: 12 }
              },
              tooltip: {
                callbacks: {
                  label: ctx => ` ${ctx.label}: ${ctx.raw} حالات توثيق`
                }
              }
            },
            scales: {
              r: {
                grid: { color: gridColor },
                ticks: { display: false }
              }
            }
          }
        });
      }
'''

chart_hook = "// Re-render Tab 3 Line Chart if visible"
if 'chartEvidenceSentiment' not in code:
    code = code.replace(chart_hook, chart15_code + "\n      " + chart_hook)
    print("Added Chart 15 initialization.")

# 5. Add Slide 09 and Slide 10 in presenterSlides
# Let's inspect presenterSlides in build_perfect_dashboard.py or code
with open(r"F:\Mr Hesham\TMG\scripts\generate_powerbi_ceo_dashboard.py", "w", encoding="utf-8") as f:
    f.write(code)

print("generate_powerbi_ceo_dashboard.py updated with all new sections!")
