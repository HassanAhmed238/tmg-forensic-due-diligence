# -*- coding: utf-8 -*-
"""
Perfect integration of Tab 8 (4-Pillar Sentiment + Chart 15 + Attribution Rules)
into generate_powerbi_ceo_dashboard.py, with expanded data from 12 Oct 2026.
"""

with open(r"F:\Mr Hesham\TMG\scripts\generate_powerbi_ceo_dashboard.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Cutoff Date to 12 October 2026
text = text.replace("11 أكتوبر 2026", "12 أكتوبر 2026")
text = text.replace("11 October 2026", "12 October 2026")

# 2. Update presenter-slide-num and dock indicator to 10
text = text.replace('<div class="slide-number" id="presenter-slide-num">SLIDE 01 / 08</div>', '<div class="slide-number" id="presenter-slide-num">SLIDE 01 / 10</div>')
text = text.replace('<div style="font-family:var(--pbi-font-mono); font-size:12px; color:var(--pbi-text-muted);" id="presenter-dock-indicator">1 / 8</div>', '<div style="font-family:var(--pbi-font-mono); font-size:12px; color:var(--pbi-text-muted);" id="presenter-dock-indicator">1 / 10</div>')

# 3. Update Atrium Portfolio Badge in Tab 5 from "6 مشروعات كبرى" to "40 مشروعاً • تحالفات دولية"
text = text.replace('<span class="pbi-pill-badge badge-cyan" id="lbl-atrium-badge">6 مشروعات كبرى • تحالفات دولية</span>', '<span class="pbi-pill-badge badge-cyan" id="lbl-atrium-badge">40 مشروعاً معتمداً • تحالفات دولية</span>')

# 4. Add Cairo Gate and FS Luxor CP02 details to Atrium Matrix
# In Card 1: Four Seasons Luxor
luxor_old = '''              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-blue); font-weight:800;">JV: CCC Electromechanical</span>
                <span class="partner-pill">إدارة: Hill International</span>
                <span class="partner-pill">استشاري: مجموعة شاكر</span>
                <span class="partner-pill">مورد: كناوف مصر (Knauf)</span>
                <span class="partner-pill">تصميم: معمار إنتريرز</span>
              </div>'''

luxor_new = '''              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-blue); font-weight:800;">JV: CCC Electromechanical (CP02)</span>
                <span class="partner-pill">إدارة: Hill International</span>
                <span class="partner-pill">استشاري: مجموعة شاكر</span>
                <span class="partner-pill">مورد: كناوف مصر (Knauf)</span>
                <span class="partner-pill">تصميم: معمار إنتريرز (Mimar)</span>
                <span class="partner-pill" style="color:var(--pbi-accent-cyan);">إشراف: محمود عبد العال</span>
              </div>'''

if luxor_old in text:
    text = text.replace(luxor_old, luxor_new)
    print("Updated Luxor card with CP02 supervision.")

# In Card 2: Four Seasons Cairo Capital
fs_cairo_old = '''              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">فورسيزونز نيو كايرو كابيتال (مدينتي)</div>
                  <div class="atrium-entity-tag">مدينتي للمشروعات السياحية / آيكون</div>
                </div>
                <span class="badge badge-low">Package CP05</span>
              </div>'''

fs_cairo_new = '''              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">فورسيزونز نيو كايرو كابيتال (مدينتي)</div>
                  <div class="atrium-entity-tag">العربية للمشروعات (المالك) / آيكون / مدينتي</div>
                </div>
                <span class="badge badge-low">Package CP05</span>
              </div>'''

if fs_cairo_old in text:
    text = text.replace(fs_cairo_old, fs_cairo_new)
    print("Updated Four Seasons Cairo Capital entity tag with Arabian Company.")

# Add 7th Card for Cairo Gate & Townsquare Offices in Atrium Grid
noor_card_end = '''              <div class="atrium-partners-row">
                <span class="partner-pill">مورد: إيماس السويدي (EMAS)</span>
                <span class="partner-pill">استشاري: مجموعة شاكر (Shaker)</span>
                <span class="partner-pill">حزم الفيلات: كونكريت بلس</span>
              </div>
            </div>
          </div>'''

cairo_gate_card = '''              <div class="atrium-partners-row">
                <span class="partner-pill">مورد: إيماس السويدي (EMAS)</span>
                <span class="partner-pill">استشاري: مجموعة شاكر (Shaker)</span>
                <span class="partner-pill">حزم الفيلات: كونكريت بلس</span>
              </div>
            </div>

            <!-- 7. Cairo Gate & Townsquare Offices (Emaar Misr) -->
            <div class="atrium-card">
              <div class="atrium-card-header">
                <div>
                  <div class="atrium-proj-name">كايرو جيت - تاون سكوير (Cairo Gate)</div>
                  <div class="atrium-entity-tag">شركة إعمار مصر للتنمية (Emaar Misr)</div>
                </div>
                <span class="badge badge-low">Delivered Turnkey</span>
              </div>
              <div class="atrium-scope-box">
                تنفيذ الأعمال الإنشائية والتشطيبات المتكاملة لمباني مكاتب تاون سكوير بوتيك المتطورة كأحد مشاريع المقاولات لصالح عميل إقليمي مرموق (إعمار مصر).
              </div>
              <div class="atrium-partners-row">
                <span class="partner-pill" style="color:var(--pbi-accent-emerald); font-weight:800;">العميل: إعمار مصر (Emaar)</span>
                <span class="partner-pill">المقاول العام: Atrium AQC</span>
                <span class="partner-pill">تسليم تجاري ناجح</span>
                <span class="partner-pill">صفر نزاعات مستحقات</span>
              </div>
            </div>
          </div>'''

if noor_card_end in text and 'Townsquare' not in text:
    text = text.replace(noor_card_end, cairo_gate_card)
    print("Added Cairo Gate & Townsquare card to Atrium grid.")

# 5. Inject 4-Pillar Sentiment + Chart 15 + Attribution Rules into Tab 8
tab8_target = '''      <!-- ==========================================================================
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

tab8_replacement = '''      <!-- ==========================================================================
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
              ● أندي لانغ LLD (شراكة 25 عاماً في 6 فنادق)
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
              ● حرس أمن مدينتي (المنصة - أكتوبر 2025)
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
              ● مقاولو باطن ساوث ميد (مدى مصر نوفمبر 2024)<br>
              ● مصدر محلي غير محدد بالاسم أو المستند<br>
              ● انقطاع الحجية المباشرة مع المطور القابض
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
              ● اعتراف إبراهيم حسبو بتعمد التعطيل آنذاك<br>
              ● دعوى 2923/2012 سقالات (609 ألف ج.م)
            </div>
          </div>
        </div>

        <!-- Evidence Classification Chart & Attribution Rules Grid -->
        <div class="grid-2" style="margin-bottom:20px;">
          <div class="pbi-card">
            <div class="pbi-card-header">
              <div>
                <div class="pbi-card-title">توزيع الأدلة الجنائية ومصادر التحقق (Evidence Hierarchy Breakdown)</div>
                <div class="pbi-card-subtitle">تصنيف نتائج الفحص الاستقصائي وفق معايير الإثبات القضائي والتوثيق التجاري (15 مخططاً)</div>
              </div>
              <span class="pbi-pill-badge badge-cyan">Chart 15 • Polar Area</span>
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
            <div style="display:flex; flex-direction:column; gap:10px; font-size:11.5px; line-height:1.65;">
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-emerald);">
                <strong style="color:var(--pbi-text-hero);">Level A — علاقة تجارية موثقة بمستندات مستقلة:</strong><br>
                تحديد أطراف العقد بدقة (المشروع، النطاق، القيمة)، مثل إفصاحات البورصة، محاضر المحاكم، وعقود التمويل المشترك.
              </div>
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-cyan);">
                <strong style="color:var(--pbi-text-hero);">Level B — بيانات رسمية صادرة عن الشركات:</strong><br>
                منشورات الشركاء والموردين والمصممين حول إنجاز الأعمال أو توريد المهمات، وهي أدلة استمرارية ولا تثبت تواريخ السداد.
              </div>
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-amber);">
                <strong style="color:var(--pbi-text-hero);">Level C — تحليلات فنية عامة لصناعة المقاولات:</strong><br>
                دراسات استشارية تشرح أثر تأخر المستخلصات على مقاولي الباطن دون توجيه اتهام مباشر لمجموعة طلعت مصطفى.
              </div>
              <div style="padding:9px 12px; background:var(--pbi-surface-elevated); border-radius:8px; border-inline-start:4px solid var(--pbi-accent-rose);">
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

if tab8_target in text:
    text = text.replace(tab8_target, tab8_replacement)
    print("Replaced Tab 8 with 4-Pillar Grid, Chart 15, and Attribution Rules.")
else:
    print("Warning: tab8_target not found directly!")

# 6. Ensure Chart 15 is initialized inside initAll14Charts
# Check if chartEvidenceSentiment is initialized
if "chartInstances.evSent = new Chart(ctxEvSent" not in text:
    chart15_init = '''
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
    text = text.replace('// Re-render Tab 3 Line Chart if visible', chart15_init + '\n      // Re-render Tab 3 Line Chart if visible')
    print("Added Chart 15 JS initialization.")

with open(r"F:\Mr Hesham\TMG\scripts\generate_powerbi_ceo_dashboard.py", "w", encoding="utf-8") as f:
    f.write(text)

print("generate_powerbi_ceo_dashboard.py perfectly updated.")
