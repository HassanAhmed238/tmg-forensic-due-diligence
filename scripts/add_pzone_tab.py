# -*- coding: utf-8 -*-
"""
Helper script to inject P.ZONE case study & water MEP risk harness into build_perfect_dashboard.py
and regenerate TMG_Forensic_Due_Diligence_Dashboard.html and index.html.
"""
from pathlib import Path

builder_path = Path(r"f:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py")
content = builder_path.read_text(encoding="utf-8")

# 1. Add Nav Button
nav_btn_target = """      <button class="nav-btn" onclick="switchTab('risks')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
        <span id="nav-risks">مصفوفة المخاطر ودليل التحوط</span>
      </button>"""

nav_btn_replacement = nav_btn_target + """

      <button class="nav-btn" onclick="switchTab('pzone')">
        <svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
        <span id="nav-pzone">دراسة P.ZONE وحزم المياه</span>
      </button>"""

if nav_btn_target in content and 'switchTab(\'pzone\')' not in content:
    content = content.replace(nav_btn_target, nav_btn_replacement)
    print("Nav button injected successfully.")

# 2. Add Tab Pane
tab_pane_target = """        <!-- Stakeholder Playbooks -->
        <div class="grid-2" style="margin-top: 20px;" id="stakeholder-playbooks-container">
          <!-- Dynamically populated via JS -->
        </div>
      </div>"""

tab_pzone_html = """        <!-- Stakeholder Playbooks -->
        <div class="grid-2" style="margin-top: 20px;" id="stakeholder-playbooks-container">
          <!-- Dynamically populated via JS -->
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 10: P.ZONE & WATER MEP SPECIALIST AUDIT -->
      <!-- ========================================== -->
      <div id="tab-pzone" class="tab-pane">
        
        <!-- Header Banner -->
        <div class="bezel-wrap" style="margin-bottom: 20px;">
          <div class="card" style="background: linear-gradient(135deg, rgba(6, 182, 212, 0.12), rgba(59, 130, 246, 0.08)); border-inline-start: 5px solid var(--accent-cyan);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
              <div>
                <div style="display:flex; align-items:center; gap:10px;">
                  <span class="badge badge-high" style="background:rgba(6,182,212,0.2); color:var(--accent-cyan); border-color:var(--accent-cyan);">دراسة حالة تخصصية مقاول باطن</span>
                  <h3 style="margin:0; font-size:18px; font-weight:800; color:var(--text-main);">تقييم ائتماني وتشغيلي: دخول شركة P.ZONE INTERNATIONAL في حزم المياه ومسابح TMG</h3>
                </div>
                <p style="margin:8px 0 0; font-size:13.5px; color:var(--text-muted); line-height:1.6; max-width:1100px;">
                  تحليل جنائي واستراتيجي مُعمق مبني على بيانات القوائم المالية المعتمدة لمجموعة طلعت مصطفى (TMGH.CA). يدرس أثر التناقض الجذري بين استيراد معدات الـ MEP نقداً بالعملة الصعبة (60%-70%) وبين دورة سداد المجموعة المعتمدة على أوراق دفع مؤجلة تمتد لـ 360 يوماً.
                </p>
              </div>
              <div style="display:flex; gap:10px;">
                <a href="pzone_tmg_strategic_evaluation_deck.html" target="_blank" class="btn-action highlight" style="text-decoration:none;">
                  <span>🎴 فتح الـ Deck التفاعلي الكامل (Long Table) ↗</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- 4 CFO Key Financial Metrics -->
        <div class="kpi-grid" style="margin-bottom: 24px;">
          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title">معدل تحويل النقد التشغيلي (H1 26)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"/></svg>
            </div>
            <div class="kpi-value">31.25%</div>
            <div class="kpi-delta delta-down">3.11B تدفق نقدي / 9.95B أرباح دفترية</div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title">أوراق الدفع والشيكات الآجلة للمقاولين</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
            </div>
            <div class="kpi-value">> 15.79B ج.م</div>
            <div class="kpi-delta delta-down">متوسط فترة سداد (DPO) تتجاوز 180 يوماً</div>
          </div>

          <div class="kpi-card amber">
            <div class="kpi-header">
              <span class="kpi-title">المكون المستورد بأعمال المياه (MEP)</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064"/></svg>
            </div>
            <div class="kpi-value">60% – 70%</div>
            <div class="kpi-delta delta-up">طلمبات، فلترة، أغشية عزل، تحكم PLC</div>
          </div>

          <div class="kpi-card rose">
            <div class="kpi-header">
              <span class="kpi-title">تكلفة التمويل وخصم الشيكات بالبنوك</span>
              <svg class="kpi-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div class="kpi-value">28.6% سنوياً</div>
            <div class="kpi-delta delta-down">تآكل كامل لهامش ربح مقاول الباطن</div>
          </div>
        </div>

        <!-- The Strategic Dual Council: Buffett vs Altman -->
        <div class="grid-2" style="margin-bottom: 24px;">
          <!-- Warren Buffett Lens -->
          <div class="bezel-wrap">
            <div class="card" style="height:100%; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div class="card-header">
                  <div>
                    <div class="card-title" style="color:var(--accent-amber);">🏛️ منظور وارن بافيت: الأمان المالي وفخ التعويم السلبي</div>
                    <div class="card-subtitle">Margin of Safety & Involuntary Float Analysis</div>
                  </div>
                  <span class="badge badge-med">حفظ رأس المال</span>
                </div>
                <div style="font-style:italic; font-size:13px; color:var(--text-muted); border-inline-start:3px solid var(--accent-amber); padding-inline-start:12px; margin-bottom:14px;">
                  "القاعدة رقم 1: لا تخسر رأس المال. القاعدة رقم 2: إياك أن تنسى القاعدة رقم 1 مطلقاً."
                </div>
                <ul style="font-size:13px; color:var(--text-muted); line-height:1.75; padding-inline-start:18px; margin:0;">
                  <li><strong>فخ التعويم السلبي (Involuntary Float):</strong> كما تستخدم بيركشاير هاثاواي أقساط التأمين كتمويل مجاني، تستخدم TMG شيكات مقاولي الباطن كتمويل بفائدة 0% لتغطية عجز السيولة بينما يتحمل المقاول تكلفة 28.6%.</li>
                  <li><strong>انعدام هامش الأمان:</strong> قبول شيكات غير معززة بنكياً في ظل تضخم متسارع وقفزات عملة يعد مضاربة غير محسوبة.</li>
                  <li><strong>السيولة عند انحسار المد:</strong> صافي مركز السيولة لـ TMG بعد خصم التزامات التأجير التمويلي هو عجز نقدي (-13.38 مليار جنيه)، مما يجعل مقاولي الباطن الضحية الأولى لأي تباطؤ مبيعات.</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Sam Altman Lens -->
          <div class="bezel-wrap">
            <div class="card" style="height:100%; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div class="card-header">
                  <div>
                    <div class="card-title" style="color:var(--accent-cyan);">🚀 منظور سام ألتمان: الرافعة غير المتماثلة والمبادئ الأولية</div>
                    <div class="card-subtitle">First Principles, Moat & Asymmetric Leverage</div>
                  </div>
                  <span class="badge badge-low" style="background:rgba(6,182,212,0.15); color:var(--accent-cyan);">احتكار تقني</span>
                </div>
                <div style="font-style:italic; font-size:13px; color:var(--text-muted); border-inline-start:3px solid var(--accent-cyan); padding-inline-start:12px; margin-bottom:14px;">
                  "فكر من المبادئ الأولية (First Principles). لا تدخل كبائع سلعي مستبدل، بل كشريك يملك احتكاراً تقنياً."
                </div>
                <ul style="font-size:13px; color:var(--text-muted); line-height:1.75; padding-inline-start:18px; margin:0;">
                  <li><strong>رافعة التفاوض (Leverage Asymmetry):</strong> البحيرات الشاطئية وحمامات السباحة هي عصب البيع في ساوث ميد؛ P.ZONE تملك سجل إنجاز تقني نادر يحتاجه المطور بشدة.</li>
                  <li><strong>رفض حواجز المقاول العام:</strong> لا تتعاقد بشروط إذعان مع شركات مقاولات وسيطة؛ طالب بفتح اعتمادات استيراد مباشرة من المالك (Direct Owner L/C).</li>
                  <li><strong>قاعدة الشراكة أو الانسحاب:</strong> إذا لم تحصل P.ZONE على دفعة نقدية 25% مع تحييد سعر الصرف، فالانسحاب أجدى للحفاظ على صحة الشركة المالية.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- The 5 Structural Killers for P.ZONE -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title">⚠️ المخاطر الهيكلية الخمسة لمقاولي الأعمال المائية في مشروعات TMG</div>
                <div class="card-subtitle">تحليل المخاطر التشغيلية والتعاقدية الخاصة بحزم البحيرات وحمامات السباحة</div>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-rose); font-weight:800; font-size:14px; margin-bottom:6px;">1. تذبذب العملة ومشتريات الـ MEP المستوردة</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  معدات الفلترة وطلمبات الضخ وأغشية العزل (Geomembrane) مسعرة باليورو/الدولار وتتطلب دفعات نقدية فورية. العقود ذات السعر المقطوع بالجنيه تعني إفلاس المقاول فور أي تحرك لسعر الصرف.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-rose); font-weight:800; font-size:14px; margin-bottom:6px;">2. فخ أوراق الدفع والشيكات الآجلة (DPO > 180d)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  سداد TMG بشيكات آجلة تمتد من 6 إلى 12 شهراً يجبر P.ZONE على تمويل رأس المال العامل عبر البنوك المصرية بفائدة 28.6%، وهو ما يبتلع هامش الربح بالكامل.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-amber); font-weight:800; font-size:14px; margin-bottom:6px;">3. حاجز المقاول العام وشرط (Pay-When-Paid)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  التعاقد يتم غالباً مع الإسكندرية للإنشاءات (ACC) أو مقاول رئيسي وسيط (كونكريت بلس / أتريوم). وجود شرط التبعية يجمد مستحقات P.ZONE حال نشوب أي خلاف بين المقاول العام وTMG.
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-amber); font-weight:800; font-size:14px; margin-bottom:6px;">4. التبعية لجدول الأعمال المدنية وتكاليف التوقف</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  لا يمكن البدء في عزل وتبطين وتمديدات البحيرات وحمامات السباحة قبل اكتمال الحفر والخرسانات. أي تعطل لمقاول الخرسانة العام يعطل أطقم P.ZONE دون تعويض عن تكاليف مد الأجل (Prolongation).
                </p>
              </div>

              <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:16px;">
                <div style="color:var(--accent-cyan); font-weight:800; font-size:14px; margin-bottom:6px;">5. احتجاز ضمان الأعمال واختبارات التسريب (Retention)</div>
                <p style="font-size:12.5px; color:var(--text-muted); margin:0; line-height:1.6;">
                  حجز 5% إلى 10% كدفعة ضمان تخضع لاختبارات غمر هيدروليكية وملاحظات استشارية معقدة، وتُستغل لتعليق صرف المستخلص الختامي لسنوات بعد تسليم الموقع.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Project Ledger Matrix -->
        <div class="bezel-wrap" style="margin-bottom: 24px;">
          <div class="card">
            <div class="card-header">
              <div>
                <div class="card-title">📋 مصفوفة تقييم الحزم المائية بمشروعات TMG والشروط الإلزامية</div>
                <div class="card-subtitle">توصيف دقيق لطبيعة الأعمال، المخاطر المترتبة، والبنود الحمائية المطلوبة</div>
              </div>
            </div>
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>المشروع</th>
                    <th>الحزمة المائية والتخصص الهيدروليكي</th>
                    <th>مكمن الخطر المالي والتشغيلي</th>
                    <th>الشرط التعاقدي الإلزامي لـ P.ZONE</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">SouthMED</td>
                    <td>البحيرات الكريستالية الضخمة ومحطات الفلترة والضخ</td>
                    <td><span class="badge badge-high">حرج</span> قفزات العملة وحجم التوريدات المستوردة الهائل</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">اعتماد مستندي بنكي مباشر (Direct Owner L/C) للتوريدات من المالك</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">مدينة نور</td>
                    <td>مسابح المجمعات السكنية ونوافير الحدائق المركزية</td>
                    <td><span class="badge badge-high">عالي</span> تآكل الهامش بسبب العقود المقطوعة وثبات الأسعار</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">ربط الأسعار شهرياً بمؤشرات جهاز التعبئة والإحصاء (CAPMAS)</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">فورسيزونز الأقصر</td>
                    <td>مسابح الضيافة الفاخرة والنوافير التراثية المعقدة</td>
                    <td><span class="badge badge-med">متوسط</span> تعقيدات الاستلام الاستشاري وتجميد الختامي ومحتجز الضمان</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">تجزئة الاستلام لمحاضر هيدروليكية مستقلة تطلق الضمان فوراً</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">سيليا (العاصمة)</td>
                    <td>الممرات المائية ونوافير المنطقة المركزية</td>
                    <td><span class="badge badge-high">عالي</span> تأخر مستحقات المقاول العام وتجميد دفعات الباطن</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">الشطب الصريح لشرط (Pay-When-Paid) والالتزام بـ 30 يوماً كاش</td>
                  </tr>
                  <tr>
                    <td style="font-weight:800; color:var(--accent-cyan);">مدينتي</td>
                    <td>تجديد بحيرات الجولف وحمامات نوادي النادي القائمة</td>
                    <td><span class="badge badge-med">متوسط</span> نزاعات قضائية مستمرة حول حسابات ودائع الصيانة</td>
                    <td style="font-weight:700; color:var(--accent-emerald);">سداد المستخلصات خلال 30 يوماً كاش مع حق إيقاف الأعمال فوراً</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- The Non-Negotiable Contractual Armor -->
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

if tab_pane_target in content and 'id="tab-pzone"' not in content:
    content = content.replace(tab_pane_target, tab_pzone_html)
    print("Tab pane injected successfully.")

# 3. Add to Translations & setLanguage
i18n_ar_target = """          risks: "مصفوفة المخاطر ودليل التحوط","""
i18n_ar_replacement = """          risks: "مصفوفة المخاطر ودليل التحوط",
          pzone: "دراسة P.ZONE وحزم المياه","""

i18n_en_target = """          risks: "Risk Matrix & Playbooks","""
i18n_en_replacement = """          risks: "Risk Matrix & Playbooks",
          pzone: "P.ZONE Water MEP Case Study","""

if i18n_ar_target in content and 'pzone:' not in content:
    content = content.replace(i18n_ar_target, i18n_ar_replacement)
    content = content.replace(i18n_en_target, i18n_en_replacement)
    print("i18n strings injected successfully.")

set_lang_target = """      document.getElementById('nav-risks').textContent = t.risks;"""
set_lang_replacement = """      document.getElementById('nav-risks').textContent = t.risks;
      if (document.getElementById('nav-pzone')) document.getElementById('nav-pzone').textContent = t.pzone;"""

if set_lang_target in content and 'nav-pzone' not in content:
    content = content.replace(set_lang_target, set_lang_replacement)
    print("setLanguage handler injected successfully.")

# Save modified script
builder_path.write_text(content, encoding="utf-8")
print("build_perfect_dashboard.py updated successfully!")
