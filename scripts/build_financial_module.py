# -*- coding: utf-8 -*-
"""
Full injector for TMG Interactive Financial Command Center & Slicer Suite.
"""

import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

print("Original length:", len(text))

# Define tab-financials replacement HTML
tab_financials_html = '''      <div id="tab-financials" class="tab-pane">
        
        <!-- Header Banner -->
        <div class="bezel-wrap" style="margin-bottom: 20px;">
          <div class="card" style="background: linear-gradient(135deg, rgba(6, 182, 212, 0.12), rgba(59, 130, 246, 0.08)); border-inline-start: 5px solid var(--accent-cyan);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
              <div>
                <div style="display:flex; align-items:center; gap:10px;">
                  <span class="badge badge-high" style="background:rgba(6,182,212,0.2); color:var(--accent-cyan); border-color:var(--accent-cyan);" id="badge-fin-hero">مدقق جنائياً — البورصة المصرية</span>
                  <h3 style="margin:0; font-size:18px; font-weight:800; color:var(--text-main);" id="t-fin-hero-title">مركز التحليل المالي والتدقيق الجنائي المتقدم (2021 – 2025 + H1 2026)</h3>
                </div>
                <p style="margin:8px 0 0; font-size:13.5px; color:var(--text-muted); line-height:1.6; max-width:1100px;" id="t-fin-hero-sub">
                  تحليل تفاعلي ديناميكي كامل لقوائم الدخل والمركز المالي لمجموعة طلعت مصطفى القابضة (TMGH.CA). يتضمن تحليل مصادر واستخدامات الأموال، التحليل الرأسي النسبي، مؤشرات Construction CFO، وتقييم أثر السيولة والائتمان على مقاولي الباطن (P.ZONE).
                </p>
              </div>
              <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <a href="RISK/TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx" download class="btn-action highlight" style="text-decoration:none;">
                  <span>📥 تحميل نموذج Excel المعتمد بالمعادلات (.xlsx)</span>
                </a>
                <button class="btn-action" onclick="setFinView('guide')">
                  <span>💡 دليل غير الماليين والحاسبة</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- ====================================================================
             DYNAMIC SLICER CONTROL DECK
             ==================================================================== -->
        <div class="fin-slicer-deck">
          <!-- Row 1: Sub-View Slicer -->
          <div class="fin-slicer-row">
            <div class="fin-slicer-group">
              <span class="fin-slicer-label" id="lbl-slicer-view">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg>
                نافذة التحليل:
              </span>
              <div class="fin-pills-wrap">
                <button class="fin-pill active" data-view="is-bs" onclick="setFinView('is-bs')" id="btn-v-isbs">📑 القوائم المالية الكاملة</button>
                <button class="fin-pill" data-view="sources-uses" onclick="setFinView('sources-uses')" id="btn-v-sources">🔄 مصادر واستخدامات النقدية</button>
                <button class="fin-pill" data-view="common-size" onclick="setFinView('common-size')" id="btn-v-common">⚖️ التحليل الرأسي %</button>
                <button class="fin-pill" data-view="cfo-ratios" onclick="setFinView('cfo-ratios')" id="btn-v-ratios">📈 نسب Construction CFO</button>
                <button class="fin-pill" data-view="pzone-deep" onclick="setFinView('pzone-deep')" id="btn-v-pzone">🛡️ تقييم P.ZONE وحزم المياه</button>
                <button class="fin-pill" data-view="guide" onclick="setFinView('guide')" id="btn-v-guide">💡 دليل المبتدئين والحاسبة</button>
              </div>
            </div>
          </div>

          <!-- Row 2: Year Slicer + Unit/Currency Slicer + Instant Search -->
          <div class="fin-slicer-row">
            <!-- Year Slicer -->
            <div class="fin-slicer-group">
              <span class="fin-slicer-label" id="lbl-slicer-year">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                النطاق الزمني:
              </span>
              <div class="fin-pills-wrap">
                <button class="fin-pill active" data-year="all" onclick="setFinYear('all')" id="btn-y-all">المسار (2021-2025)</button>
                <button class="fin-pill" data-year="2025" onclick="setFinYear('2025')">2025 المعتمد</button>
                <button class="fin-pill" data-year="2024" onclick="setFinYear('2024')">2024</button>
                <button class="fin-pill" data-year="2023" onclick="setFinYear('2023')">2023</button>
                <button class="fin-pill" data-year="2022" onclick="setFinYear('2022')">2022</button>
                <button class="fin-pill" data-year="2021" onclick="setFinYear('2021')">2021</button>
                <button class="fin-pill" data-year="h126" onclick="setFinYear('h126')">H1 2026</button>
              </div>
            </div>

            <!-- Currency/Unit Slicer -->
            <div class="fin-slicer-group">
              <span class="fin-slicer-label" id="lbl-slicer-unit">
                <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                وحدة العرض:
              </span>
              <div class="fin-pills-wrap">
                <button class="fin-pill active" data-unit="billions" onclick="setFinUnit('billions')" id="btn-u-b">مليار جنيه (Bn)</button>
                <button class="fin-pill" data-unit="thousands" onclick="setFinUnit('thousands')" id="btn-u-k">ألف جنيه (k - البورصة)</button>
                <button class="fin-pill" data-unit="usd" onclick="setFinUnit('usd')" id="btn-u-usd">مليون دولار ($ Mn @ 49.5)</button>
              </div>
            </div>

            <!-- Instant Search -->
            <div class="fin-search-box">
              <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
              <input type="text" id="finSearchInput" placeholder="بحث فوري في البنود..." oninput="handleFinSearch(this.value)">
            </div>
          </div>
        </div>

        <!-- ====================================================================
             DYNAMIC KPI SUMMARY STRIP (6 CARDS)
             ==================================================================== -->
        <div class="kpi-grid" style="margin-bottom: 24px;">
          <div class="kpi-card cyan">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-fin-rev-t">إجمالي الإيرادات المجمعة</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
            </div>
            <div class="kpi-value" id="kpi-fin-rev-v">62.50 B</div>
            <div class="kpi-delta delta-up" id="kpi-fin-rev-d">+33.3% سنوي | 4 أضعاف 2021</div>
          </div>

          <div class="kpi-card emerald">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-fin-ni-t">صافي الأرباح المجمعة</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div class="kpi-value" id="kpi-fin-ni-v">18.20 B</div>
            <div class="kpi-delta delta-up" id="kpi-fin-ni-d">هامش صافي 29.1% | نصيب الأم 14.5B</div>
          </div>

          <div class="kpi-card amber">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-fin-adv-t">مقدمات وحجوزات العملاء (Float)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
            </div>
            <div class="kpi-value" id="kpi-fin-adv-v">117.68 B</div>
            <div class="kpi-delta delta-down" id="kpi-fin-adv-d">31.6% من إجمالي الميزانية (التزام تسليم)</div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-fin-notes-t">أوراق دفع الموردين والمقاولين</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
            </div>
            <div class="kpi-value" id="kpi-fin-notes-v">15.79 B</div>
            <div class="kpi-delta delta-down" id="kpi-fin-notes-d">+208% نمو | تمويل عبر مدفوعات المقاولين</div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-fin-lease-t">التزامات التأجير التمويلي (Off-Balance)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
            </div>
            <div class="kpi-value" id="kpi-fin-lease-v">34.40 B</div>
            <div class="kpi-delta delta-down" id="kpi-fin-lease-d">فنادق ICON | خدمة دين سنوية 4.56B</div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title" id="kpi-fin-dpo-t">فترة سداد الموردين (DPO)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div class="kpi-value" id="kpi-fin-dpo-v">160 يوماً</div>
            <div class="kpi-delta delta-down" id="kpi-fin-dpo-d">صعود من 134 يوماً (سحب ائتمان مقاولي الباطن)</div>
          </div>
        </div>

        <!-- ====================================================================
             DYNAMIC CHARTS ROW
             ==================================================================== -->
        <div class="grid-2" style="margin-bottom: 24px;">
          <!-- Chart 1: Revenue vs Net Profit vs Backlog -->
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-fin-c1-title">مسار نمو الإيرادات وصافي الأرباح وهوامش التشغيل (2021 – 2026)</div>
                  <div class="card-subtitle" id="t-fin-c1-sub">مقارنة نمو النشاط العقاري والفنادق ومبيعات الباكلوج المتعاقد عليها</div>
                </div>
                <span class="badge badge-high" id="badge-fin-c1">نمو تاريخي</span>
              </div>
              <div class="chart-box" style="height: 300px;">
                <canvas id="chartFinancialTrendsDynamic"></canvas>
              </div>
            </div>
          </div>

          <!-- Chart 2: Balance Sheet Composition -->
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-fin-c2-title">هيكل المركز المالي: الأصول مقابل الالتزامات والملكية</div>
                  <div class="card-subtitle" id="t-fin-c2-sub">أعمال قيد التنفيذ والمقدمات والتأجير التمويلي (مليار جنيه)</div>
                </div>
                <span class="badge badge-high" id="badge-fin-c2">توزيع الميزانية</span>
              </div>
              <div class="chart-box" style="height: 300px;">
                <canvas id="chartBalanceSheetDynamic"></canvas>
              </div>
            </div>
          </div>
        </div>

        <div class="grid-2" style="margin-bottom: 24px;">
          <!-- Chart 3: DPO vs CCC Contractor Stretch -->
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-fin-c3-title">منحنى استنزاف مقاولي الباطن: فترات سداد الموردين (DPO) والسيولة</div>
                  <div class="card-subtitle" id="t-fin-c3-sub">تتبع اتساع فجوة السداد من 134 يوماً إلى 160 يوماً بالتزامن مع تضخم أوراق الدفع</div>
                </div>
                <span class="badge badge-high" id="badge-fin-c3">مؤشر الخطر التشغيلي</span>
              </div>
              <div class="chart-box" style="height: 280px;">
                <canvas id="chartDpoDynamic"></canvas>
              </div>
            </div>
          </div>

          <!-- Chart 4: Capital Sources & Uses Flow -->
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-fin-c4-title">تدفق مصادر واستخدامات الأموال لعام 2025 (109.8 مليار جنيه)</div>
                  <div class="card-subtitle" id="t-fin-c4-sub">من أين جاءت السيولة (Sources) وأين تم ضخها وتجميدها (Uses)</div>
                </div>
                <span class="badge badge-high" id="badge-fin-c4">توازن التدفق</span>
              </div>
              <div class="chart-box" style="height: 280px;">
                <canvas id="chartSourcesUsesDynamic"></canvas>
              </div>
            </div>
          </div>
        </div>

        <!-- ====================================================================
             SUB-VIEW 1: FINANCIAL STATEMENTS (IS & BS)
             ==================================================================== -->
        <div id="subview-is-bs" class="fin-subview active">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-tbl-fs-title">القوائم المالية المجمعة والمدققة (FY2021 – FY2025 + H1 2026)</div>
                  <div class="card-subtitle" id="t-tbl-fs-sub">كافة الأرقام مطابقة بنسبة 100% لإفصاحات البورصة المصرية ومصنفة محاسبياً مع فحص الميزان (Check = 0.00)</div>
                </div>
                <div style="display:flex; gap:8px;">
                  <button class="btn-action active" onclick="toggleStatementType('all')" id="btn-st-all">عرض القوائم معاً</button>
                  <button class="btn-action" onclick="toggleStatementType('is')" id="btn-st-is">قائمة الدخل فقط</button>
                  <button class="btn-action" onclick="toggleStatementType('bs')" id="btn-st-bs">المركز المالي فقط</button>
                </div>
              </div>

              <div class="table-container" style="max-height: 700px; overflow-y: auto;">
                <table class="fin-data-table" id="tableFinancialStatements">
                  <thead>
                    <tr id="fin-fs-th-row">
                      <!-- Populated via JS -->
                    </tr>
                  </thead>
                  <tbody id="fin-fs-tbody">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- ====================================================================
             SUB-VIEW 2: SOURCES & USES ANALYSIS
             ==================================================================== -->
        <div id="subview-sources-uses" class="fin-subview">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-tbl-su-title">تحليل مصادر واستخدامات الأموال والسيولة (2024 مقابل 2025)</div>
                  <div class="card-subtitle" id="t-tbl-su-sub">تتبع حركة النقد ورأس المال بين سنتي الأساس والنمو — توازن إجمالي المصادر والاستخدامات (109.84 مليار جنيه)</div>
                </div>
                <span class="badge badge-high" style="background:rgba(16,185,129,0.2); color:var(--accent-emerald); border-color:var(--accent-emerald);">توازن تام: Delta = 0.00</span>
              </div>

              <div class="table-container">
                <table class="fin-data-table" id="tableSourcesUses">
                  <thead>
                    <tr id="fin-su-th-row">
                      <!-- Populated via JS -->
                    </tr>
                  </thead>
                  <tbody id="fin-su-tbody">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>

              <!-- Forensic Notes on Sources & Uses -->
              <div style="margin-top: 20px; padding: 16px; background: var(--bg-surface-elevated); border-radius: 10px; border-inline-start: 4px solid var(--accent-cyan);">
                <div style="font-weight: 800; margin-bottom: 8px; font-size: 13px; color: var(--text-main);" id="t-su-note-title">🔍 الخلاصة الجنائية لحركة رأس المال والسيولة لعام 2025:</div>
                <ul style="margin: 0; padding-inline-start: 20px; font-size: 12.5px; color: var(--text-muted); line-height: 1.8;" id="t-su-note-list">
                  <li><strong>المصدر الأكبر للسيولة:</strong> تمثل في <strong>الحصص غير المسيطرة (ADQ) بقيمة 26.0 مليار جنيه</strong> و<strong>مقدمات حجز العملاء الجديدة بقيمة 22.68 مليار جنيه</strong> و<strong>الأرباح المحتجزة بقيمة 15.33 مليار جنيه</strong>.</li>
                  <li><strong>الاستخدام الأكبر للأموال:</strong> تم ضخ <strong>36.0 مليار جنيه في الإنشاءات ومخزون الأراضي غير المسلمة (Real Estate WIP)</strong> و<strong>26.1 مليار جنيه في الأصول الثابتة وتطوير فنادق صفقة ICON</strong>.</li>
                  <li><strong>عبء مقاولي الباطن:</strong> ساهم مقاولو الباطن والموردون بتمويل إضافي قدره <strong>2.29 مليار جنيه</strong> في شكل شيكات وأوراق دفع مؤجلة إضافية فوق أرصدة 2024.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- ====================================================================
             SUB-VIEW 3: COMMON SIZE ANALYSIS %
             ==================================================================== -->
        <div id="subview-common-size" class="fin-subview">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-tbl-cs-title">التحليل الرأسي والنسبي لقوائم الدخل والمركز المالي (2023 – 2025)</div>
                  <div class="card-subtitle" id="t-tbl-cs-sub">النسبة المئوية لكل بند من إجمالي المبيعات وقائمة المركز المالي مع تتبع الانحرافات الهيكلية</div>
                </div>
              </div>

              <div class="table-container">
                <table class="fin-data-table" id="tableCommonSize">
                  <thead>
                    <tr id="fin-cs-th-row">
                      <!-- Populated via JS -->
                    </tr>
                  </thead>
                  <tbody id="fin-cs-tbody">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>

              <!-- Common size insights -->
              <div class="grid-2" style="margin-top: 20px; gap: 16px;">
                <div style="padding: 16px; background: var(--bg-surface-elevated); border-radius: 10px; border-inline-start: 4px solid var(--accent-rose);">
                  <div style="font-weight: 800; font-size: 13px; color: var(--accent-rose); margin-bottom: 6px;">⚠️ قفزة الأعباء التمويلية (Finance Costs)</div>
                  <p style="margin: 0; font-size: 12.5px; color: var(--text-muted); line-height: 1.6;">
                    ارتفعت الفوائد المدينة من 6.0% من إجمالي الإيرادات في 2023 إلى <strong>7.3% في 2025 (4.56 مليار جنيه)</strong> نتيجة أسعار الفائدة المرتفعة بالبنك المركزي وأقساط التأجير التمويلي، مما يضغط بشدة على هوامش الأمان للسيولة النقدية.
                  </p>
                </div>
                <div style="padding: 16px; background: var(--bg-surface-elevated); border-radius: 10px; border-inline-start: 4px solid var(--accent-amber);">
                  <div style="font-weight: 800; font-size: 13px; color: var(--accent-amber); margin-bottom: 6px;">⚠️ هيمنة مقدمات العملاء (Customer Float)</div>
                  <p style="margin: 0; font-size: 12.5px; color: var(--text-muted); line-height: 1.6;">
                    تمثل مقدمات العملاء <strong>31.6% من إجمالي أصول المجموعة (117.7 مليار جنيه)</strong>. هذا يعني أن ثلث الميزانية عبارة عن التزامات تسليم حتمية، وأي تعطل في سلاسل الإمداد أو إنجاز المقاولين يعرض المجموعة لغرامات تأخير ضخمة.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ====================================================================
             SUB-VIEW 4: CONSTRUCTION CFO RATIOS
             ==================================================================== -->
        <div id="subview-cfo-ratios" class="fin-subview">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-tbl-ratios-title">مصفوفة نسب ومؤشرات Construction CFO وإدارة السيولة</div>
                  <div class="card-subtitle" id="t-tbl-ratios-sub">مؤشرات السيولة، النشاط ورأس المال العامل، الرافعة المالية، والربحية (2021 – 2025) مع تقييم أثرها على مقاولي الباطن</div>
                </div>
              </div>

              <div class="table-container">
                <table class="fin-data-table" id="tableCfoRatios">
                  <thead>
                    <tr id="fin-rt-th-row">
                      <!-- Populated via JS -->
                    </tr>
                  </thead>
                  <tbody id="fin-rt-tbody">
                    <!-- Populated dynamically via JS -->
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- ====================================================================
             SUB-VIEW 5: P.ZONE WATER WORKS RISK ASSESSMENT
             ==================================================================== -->
        <div id="subview-pzone-deep" class="fin-subview">
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-pz-eval-title">الفحص الائتماني والتعاقدي الشامل: دخول P.ZONE INTERNATIONAL في حزم المياه ومسابح TMG</div>
                  <div class="card-subtitle" id="t-pz-eval-sub">تشريح المخاطر المالية لمقاولي الأعمال الكهروميكانيكية، حمامات السباحة، البحيرات الصناعية، ومحطات المعالجة</div>
                </div>
                <span class="badge badge-high" style="background:rgba(244,63,94,0.2); color:var(--accent-rose); border-color:var(--accent-rose);">مستوى المخاطرة: حرج / مرتفع جداً</span>
              </div>

              <!-- 3 Pillar Analysis Grid -->
              <div class="grid-3" style="margin-top: 16px; gap: 16px;">
                <div class="sim-stat-box" style="border-inline-start: 4px solid var(--accent-rose);">
                  <div style="font-weight: 800; font-size: 13.5px; color: var(--accent-rose);">1. فخ استيراد المعدات نقداً مقابل الدفع المؤجل</div>
                  <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6; margin: 8px 0 0;">
                    أعمال حمامات السباحة والبحيرات تتطلب <strong>60% إلى 70% مكونات كهروميكانيكية مستوردة (مضخات، فلاتر، صمامات، عوازل EPDM)</strong> يتم سدادها نقداً بالدولار مقدماً للموردين الدوليين. في المقابل، تسدد TMG مستحقات مقاوليها عبر دورة سداد تمتد إلى <strong>160 يوماً (DPO) وشيكات آجلة تمتد لـ 180-360 يوماً</strong> بالجنيه المصري غير المعوض للتضخم!
                  </p>
                </div>

                <div class="sim-stat-box" style="border-inline-start: 4px solid var(--accent-amber);">
                  <div style="font-weight: 800; font-size: 13.5px; color: var(--accent-amber);">2. تآكل هوامش الربح تحت سعر الفائدة (28%+)</div>
                  <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6; margin: 8px 0 0;">
                    إذا اضطرت شركة P.ZONE إلى تمويل أعمال الموقع من خطوط الائتمان البنكية الخاصة بها لتغطية تأخير مستخلصات TMG، فإن <strong>فائدة الإقراض بالبنك المركزي المصري (28% - 31%) تلتهم كامل هامش ربح المقاولة (المقدر بـ 18%-22%)</strong> وتتحول العملية إلى خسارة محققة بعد الشهر الرابع من التأخير!
                  </p>
                </div>

                <div class="sim-stat-box" style="border-inline-start: 4px solid var(--accent-cyan);">
                  <div style="font-weight: 800; font-size: 13.5px; color: var(--accent-cyan);">3. حقيقة سيولة TMG (الشركة تمتلك كاش لكن تؤجل السداد!)</div>
                  <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6; margin: 8px 0 0;">
                    رصيد النقدية لدى TMG يبلغ <strong>41.2 مليار جنيه في 2025 و66.4 مليار في H1 2026</strong>، ومقدمات العملاء بلغت 117.7 مليار. هذا يعني أن تأخير سداد المقاولين <strong>ليس عجزاً في السيولة الإجمالية</strong>، بل سياسة مالية ممنهجة (Working Capital Aggression) لاستخدام أموال المقاولين كتمويل مجاني لتوسعات الفنادق والمشاريع الخارجية!
                  </p>
                </div>
              </div>

              <!-- P.ZONE Contractual Armor Blueprint -->
              <div style="margin-top: 24px; padding: 20px; background: var(--bg-surface-elevated); border-radius: 12px; border: 1px solid var(--border-subtle);">
                <div style="font-size: 15px; font-weight: 800; color: var(--text-main); margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                  <span>🛡️ الشروط الإلزامية غير القابلة للتفاوض لشركة P.ZONE قبل توقيع أي عقد مع TMG:</span>
                </div>
                <div class="guide-grid-3">
                  <div class="guide-step-card">
                    <div class="guide-step-num">1</div>
                    <div style="font-weight: 800; font-size: 13px; color: var(--text-main);">شطب شرط Back-to-Back نهائياً</div>
                    <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6; margin: 0;">
                      رفض أي صياغة تفيد "السداد عند تحصيل طلعت مصطفى من عملائه" (Pay-When-Paid). مستحقات P.ZONE ترتبط حصراً بتمام الإنجاز الفني للمسبح أو محطة المياه.
                    </p>
                  </div>
                  <div class="guide-step-card">
                    <div class="guide-step-num">2</div>
                    <div style="font-weight: 800; font-size: 13px; color: var(--text-main);">دفعة مقدمة 35% - 45% بالعملة الصعبة</div>
                    <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6; margin: 0;">
                      اشتراط دفعة مقدمة نقدية تغطي 100% من قيمة المعدات الكهروميكانيكية والمضخات المستوردة لفتح اعتمادات مستندية معززة (LCs) تجنباً لأي مخاطر عملة.
                    </p>
                  </div>
                  <div class="guide-step-card">
                    <div class="guide-step-num">3</div>
                    <div style="font-weight: 800; font-size: 13px; color: var(--text-main);">اعتماد وصرف المستخلص خلال 21 يوماً</div>
                    <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6; margin: 0;">
                      وضع مدة قصوى لاعتماد المستخلص (14 يوماً) وصرفه (7 أيام). في حال التأخير، يحق لـ P.ZONE التوقف التام عن الموقع مع احتساب غرامة تأخير تجارية بنكية.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ====================================================================
             SUB-VIEW 6: BEGINNER GUIDE & INTERACTIVE CONTRACT SIMULATOR
             ==================================================================== -->
        <div id="subview-guide" class="fin-subview">
          <!-- 1. The 2-Minute Decoder -->
          <div class="bezel-wrap" style="margin-bottom: 24px;">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-gd-dec-title">💡 دليل المبتدئين وغير الماليين: كيف تفهم ميزانية طلعت مصطفى في دقيقتين؟</div>
                  <div class="card-subtitle" id="t-gd-dec-sub">شرح مباشر ومبسط للمصطلحات المالية المعقدة بلغة هندسية وتنفيذية واضحة</div>
                </div>
                <span class="badge badge-high" style="background:rgba(59,130,246,0.2); color:var(--accent-blue); border-color:var(--accent-blue);">لغير الماليين</span>
              </div>

              <div class="guide-grid-3">
                <div class="guide-step-card">
                  <div class="guide-step-num" style="background:var(--accent-blue);">1</div>
                  <div style="font-weight: 800; font-size: 14px; color: var(--text-main);">ما هو الـ DPO (فترة سداد الموردين)؟</div>
                  <p style="font-size: 12.5px; color: var(--text-muted); line-height: 1.6; margin: 0;">
                    <strong>بالبلدي:</strong> لما تقدم مستخلصك، طلعت مصطفى بياخد في المتوسط <strong>160 يوماً (أكثر من 5 أشهر)</strong> عشان يصرفلك فلوسك! وفي الواقع العملي بتوصل لـ 8 أشهر بشيكات مؤجلة. ده معناه إنك لازم تكون عامل حسابك في سيولة تكفيك تشتغل 6 شهور من غير ما تاخد مليم.
                  </p>
                </div>

                <div class="guide-step-card">
                  <div class="guide-step-num" style="background:var(--accent-amber);">2</div>
                  <div style="font-weight: 800; font-size: 14px; color: var(--text-main);">ما هي "مقدمات العملاء" (117.7 مليار)؟</div>
                  <p style="font-size: 12.5px; color: var(--text-muted); line-height: 1.6; margin: 0;">
                    <strong>بالبلدي:</strong> دي مش فلوس طلعت مصطفى الخاصة ولا أرباح! دي فلوس الناس اللي اشترت شقق وفلل في مدينتي ونور وساوث ميد.. الفلوس دي عبارة عن "دين تسليم" ملزم؛ طلعت مصطفى مبيقدرش يسجلها كأرباح إلا لما يبني ويسلمك المفتاح.
                  </p>
                </div>

                <div class="guide-step-card">
                  <div class="guide-step-num" style="background:var(--accent-rose);">3</div>
                  <div style="font-weight: 800; font-size: 14px; color: var(--text-main);">ما هي ديون التأجير التمويلي (34.4 مليار)؟</div>
                  <p style="font-size: 12.5px; color: var(--text-muted); line-height: 1.6; margin: 0;">
                    <strong>بالبلدي:</strong> طلعت مصطفى اشترى 7 فنادق تاريخية (شركة ICON) بقروض تأجير تمويلي ضخمة مش باينة في خانة الديون المباشرة. ديون الفنادق دي بتسحب أقساط شهرية ضخمة (أكثر من 4.5 مليار سنوياً) للبنوك، وأقساط البنوك ليها الأولوية الأولى في الصرف قبل أي مستخلص مقاول!
                  </p>
                </div>
              </div>

              <!-- Traffic Light Radar -->
              <div style="margin-top: 24px;">
                <div style="font-weight: 800; font-size: 14px; color: var(--text-main); margin-bottom: 12px;">🚦 رادار الإشارات الثلاثية لمقاول الباطن:</div>
                <div class="tl-radar-grid">
                  <div class="tl-card green">
                    <div style="font-weight: 900; font-size: 13.5px; color: var(--accent-emerald); margin-bottom: 6px;">🟢 الإشارة الخضراء (أين الأمان؟)</div>
                    <ul style="margin: 0; padding-inline-start: 18px; font-size: 12px; color: var(--text-muted); line-height: 1.7;">
                      <li>حجم أصول عملاق (372 مليار جنيه) يدعمه مخزون أراضي استراتيجي.</li>
                      <li>مبيعات قياسية تتجاوز 460 مليار جنيه (Backlog).</li>
                      <li>استحالة إفلاس أو تعثر سيادي للمجموعة.</li>
                    </ul>
                  </div>

                  <div class="tl-card amber">
                    <div style="font-weight: 900; font-size: 13.5px; color: var(--accent-amber); margin-bottom: 6px;">🟡 الإشارة الصفراء (أين الحذر؟)</div>
                    <ul style="margin: 0; padding-inline-start: 18px; font-size: 12px; color: var(--text-muted); line-height: 1.7;">
                      <li>التزامات تسليم إنشائية ضخمة تتطلب سيولة مستمرة بلا توقف.</li>
                      <li>أعباء تمويلية تأكل 7.3% من الإيرادات بسبب أسعار الفائدة.</li>
                      <li>بيروقراطية معقدة وتعدد لجان فحص المستخلصات قبل الاعتماد.</li>
                    </ul>
                  </div>

                  <div class="tl-card red">
                    <div style="font-weight: 900; font-size: 13.5px; color: var(--accent-rose); margin-bottom: 6px;">🔴 الإشارة الحمراء (الخطر القاتل!)</div>
                    <ul style="margin: 0; padding-inline-start: 18px; font-size: 12px; color: var(--text-muted); line-height: 1.7;">
                      <li>دفعات المقاولين مؤجلة بمتوسط 160 يوماً بشيكات بنكية.</li>
                      <li>شروط تعاقدية مجحفة تنقل مخاطر العميل وتضخم الأسعار على ظهر المقاول.</li>
                      <li>المقاول الذي يدخل بدون دفعة مقدمة بالدولار محكوم عليه بالإفلاس النقدي!</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 2. Interactive Subcontractor Risk Simulator -->
          <div class="bezel-wrap">
            <div class="card">
              <div class="card-header">
                <div>
                  <div class="card-title" id="t-sim-title">🧮 حاسبة محاكاة مخاطر عقد مقاول الباطن التفاعلية (P.ZONE Risk Simulator)</div>
                  <div class="card-subtitle" id="t-sim-sub">أدخل تفاصيل مشروعك المتوقع مع طلعت مصطفى وشاهد الحسابات التلقائية لرأس المال المجمد وتكلفة التمويل والحد الأدنى للدفعة المقدمة</div>
                </div>
                <span class="badge badge-high" style="background:rgba(6,182,212,0.2); color:var(--accent-cyan); border-color:var(--accent-cyan);">محاكاة لحظية</span>
              </div>

              <div class="sim-grid">
                <!-- Inputs Side -->
                <div style="background: var(--bg-surface-elevated); padding: 20px; border-radius: 12px; border: 1px solid var(--border-subtle);">
                  <div style="font-weight: 800; font-size: 14px; margin-bottom: 16px; color: var(--text-main);">بيانات العقد المقترح:</div>

                  <div class="sim-slider-row">
                    <div class="sim-slider-header">
                      <span>قيمة العقد الإجمالية (جنيه مصري):</span>
                      <span id="disp-sim-val" style="color:var(--accent-cyan); font-family:var(--font-mono); font-weight:800;">50,000,000 ج.م</span>
                    </div>
                    <input type="range" class="sim-slider" id="sim-input-val" min="5000000" max="200000000" step="5000000" value="50000000" oninput="updateSimCalculations()">
                  </div>

                  <div class="sim-slider-row">
                    <div class="sim-slider-header">
                      <span>نسبة المعدات المستوردة بالدولار (مضخات/فلاتر):</span>
                      <span id="disp-sim-mep" style="color:var(--accent-cyan); font-family:var(--font-mono); font-weight:800;">65%</span>
                    </div>
                    <input type="range" class="sim-slider" id="sim-input-mep" min="20" max="90" step="5" value="65" oninput="updateSimCalculations()">
                  </div>

                  <div class="sim-slider-row">
                    <div class="sim-slider-header">
                      <span>فترة تأخير سداد المستخلص المتوقعة (يوماً):</span>
                      <span id="disp-sim-days" style="color:var(--accent-rose); font-family:var(--font-mono); font-weight:800;">160 يوماً</span>
                    </div>
                    <input type="range" class="sim-slider" id="sim-input-days" min="60" max="270" step="15" value="160" oninput="updateSimCalculations()">
                  </div>

                  <div class="sim-slider-row">
                    <div class="sim-slider-header">
                      <span>نسبة الارتفاع المحتمل لسعر الصرف / التضخم (%):</span>
                      <span id="disp-sim-fx" style="color:var(--accent-amber); font-family:var(--font-mono); font-weight:800;">15%</span>
                    </div>
                    <input type="range" class="sim-slider" id="sim-input-fx" min="0" max="40" step="5" value="15" oninput="updateSimCalculations()">
                  </div>
                </div>

                <!-- Outputs Side -->
                <div style="display: flex; flex-direction: column; gap: 12px;">
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    <div class="sim-stat-box">
                      <span style="font-size: 11.5px; color: var(--text-muted); font-weight: 700;">رأس المال العامل المطلوب تجميده</span>
                      <span class="sim-stat-num val-neg" id="res-sim-frozen">21.92 M</span>
                      <span style="font-size: 11px; color: var(--text-dim);">لتغطية مصاريف الموقع خلال التأخير</span>
                    </div>

                    <div class="sim-stat-box">
                      <span style="font-size: 11.5px; color: var(--text-muted); font-weight: 700;">تكلفة التمويل البنكي الضائعة (@28%)</span>
                      <span class="sim-stat-num val-neg" id="res-sim-interest">2.69 M</span>
                      <span style="font-size: 11px; color: var(--text-dim);">فوائد مدينة تأكل من ربح المقاولة</span>
                    </div>

                    <div class="sim-stat-box">
                      <span style="font-size: 11.5px; color: var(--text-muted); font-weight: 700;">مخاطر تآكل العملة على الاستيراد</span>
                      <span class="sim-stat-num val-warn" id="res-sim-fxloss">4.88 M</span>
                      <span style="font-size: 11px; color: var(--text-dim);">خسارة في حال تحرك سعر الدولار</span>
                    </div>

                    <div class="sim-stat-box" style="border: 1.5px solid var(--accent-cyan);">
                      <span style="font-size: 11.5px; color: var(--accent-cyan); font-weight: 800;">الحد الأدنى للدفعة المقدمة الإلزامية</span>
                      <span class="sim-stat-num val-cyan" id="res-sim-advpay">20.00 M (40%)</span>
                      <span style="font-size: 11px; color: var(--text-dim);">لتأمين استيراد المعدات فوراً</span>
                    </div>
                  </div>

                  <!-- Dynamic Verdict Box -->
                  <div class="sim-verdict-box" id="res-sim-verdict" style="background: rgba(244,63,94,0.08); border-color: var(--accent-rose);">
                    <div style="font-weight: 900; font-size: 14px; color: var(--accent-rose); margin-bottom: 4px;" id="res-sim-verdict-title">⚠️ تقييم العقد: عالي المخاطرة النقدية (High Liquidity Exposure)</div>
                    <div style="font-size: 12px; color: var(--text-muted); line-height: 1.5;" id="res-sim-verdict-desc">
                      تكلفة التمويل وفروق العملة تبتلع ما يفوق 15% من قيمة العقد. لا يجوز توقيع هذا العقد إلا بعد اشتراط دفعة مقدمة نقدية بنسبة 40% وإلغاء شرط الباك تو باك.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>'''

# Find boundaries to replace in HTML
start_marker = '<div id="tab-financials" class="tab-pane">'
end_marker = '<!-- ========================================== -->\n      <!-- TAB 8: CUSTOMER & LABOR SENTIMENT -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("ERROR: Could not find start or end markers for tab-financials!")
    sys.exit(1)

print(f"Replacing tab-financials slice from char {start_idx} to {end_idx}...")
new_text = text[:start_idx] + tab_financials_html + "\n\n      " + text[end_idx:]
print("New text length after tab replacement:", len(new_text))

# Save interim
with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Successfully replaced tab-financials markup.")
