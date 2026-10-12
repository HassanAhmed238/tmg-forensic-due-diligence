# -*- coding: utf-8 -*-
with open(r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace SLIDE XX / 08 with SLIDE XX / 10
for i in range(1, 9):
    code = code.replace(f'SLIDE 0{i} / 08', f'SLIDE 0{i} / 10')

slide_08_end = '''              </ul>
            </div>
          </div>
        `
      }
    ];'''

slide_09_10 = '''              </ul>
            </div>
          </div>
        `
      },
      {
        num: "SLIDE 09 / 10",
        titleAr: "شبكة مقاولي أتريوم (Atrium) والتحالفات الاستراتيجية الكبرى",
        titleEn: "Atrium Expanded Contractor Network & Strategic JVs",
        noteAr: "تتولى شركة أتريوم دور المقاول العام المتكامل للأعمال الفندقية والتجارية، وتشكل تحالفات دولية مع CCC Electromechanical، ومقاولين متخصصين مثل إيفرلاست وسراج وإيماس السويدي.",
        noteEn: "Atrium AQC acts as the turnkey EPC vehicle for hospitality & commercial assets, partnering with CCC Electromechanical, Everlast, Siraj, and EMAS.",
        contentAr: `
          <div class="grid-3">
            <div class="flag-card" style="border-inline-start-color: var(--accent-cyan);">
              <div class="flag-title">فورسيزونز الأقصر & كابيتال</div>
              <div class="flag-desc">تحالف استراتيجي مع CCC Electromechanical لحزم MEP الكبرى (CP02 / CP05) بإشراف Hill International واستشارات شاكر وكناوف مصر.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-emerald);">
              <div class="flag-title">أوبن إير مول وإيست هب</div>
              <div class="flag-desc">إسناد جمالونات الحديد لشركة إيفرلاست (استشاري ECG)، وتوريد أنظمة الإضاءة المعمارية المتطورة من سراج للإضاءة بإشراف دار الهندسة.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">مدينة نور وسيليـا</div>
              <div class="flag-desc">تنفيذ 72 عمارة وفيلات بنور، وتوريد خلايا الجهد المتوسط 24kV من إيماس السويدي، وحزم العاصمة الإدارية بإشراف حمزة وشركاه.</div>
            </div>
          </div>
          <div style="font-size:12.5px; color:var(--text-muted); line-height:1.7; margin-top:16px;">
            ● يضمن نموذج المقاول المدمج (Atrium / ACC) حماية كاملة لأرصدة ومبيعات المجموعة القابضة من أي دعاوى مباشرة لمقاولي الباطن.
          </div>
        `,
        contentEn: `
          <div class="grid-3">
            <div class="flag-card" style="border-inline-start-color: var(--accent-cyan);">
              <div class="flag-title">FS Luxor & Cairo Capital</div>
              <div class="flag-desc">Strategic JV with CCC Electromechanical for MEP packages (CP02 / CP05) under Hill International, Shaker Group & Knauf.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-emerald);">
              <div class="flag-title">Open Air & East Hub Malls</div>
              <div class="flag-desc">Specialist steel trusses by Everlast Construction (ECG Consultant), architectural lighting by Siraj under Dar Al-Handasah.</div>
            </div>
            <div class="flag-card" style="border-inline-start-color: var(--accent-amber);">
              <div class="flag-title">Noor City & Celia Capital</div>
              <div class="flag-desc">72 residential buildings at Noor, Siemens 24kV switchgear by EMAS El Sewedy, and New Capital packages under Hamza Associates.</div>
            </div>
          </div>
          <div style="font-size:12.5px; color:var(--text-muted); line-height:1.7; margin-top:16px;">
            ● Captive general contracting ring-fences TMG Holding balances and escrow receivables from downstream trade subcontractor liens.
          </div>
        `
      },
      {
        num: "SLIDE 10 / 10",
        titleAr: "استقصاء مشاعر المقاولين وحقيقة الدفع: نتائج التدقيق الجنائي",
        titleEn: "Contractor Sentiment & Payment Truth: Forensic Audit Conclusions",
        noteAr: "أظهر التدقيق الجنائي تفاوتاً حاداً بين الشكاوى التاريخية ومزاعم النشر الصحفي والواقع التعاقدي؛ لا يوجد دليل على سياسة عامة لحبس المستحقات حالياً، وتكرار التعاقدات (10B لكونكريت بلس) يؤكد استقرار الشراكات الكبرى.",
        noteEn: "Forensic audit strictly separates direct historic dues complaints (2008) from upstream military payment lags (SouthMED 2024) and internal workforce wages.",
        contentAr: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-emerald);">
              <div class="card-title" style="color:var(--accent-emerald);">الأدلة التجارية المؤكدة والإيجابية</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>تكرار إسناد المشروعات الضخمة: كونكريت بلس بـ 10 مليار جنيه بساوث ميد.</li>
                <li>شراكات ممتدة لربع قرن (أندي لانغ LLD في 6 فنادق فورسيزونز).</li>
                <li>توريدات تخصصية منتظمة دون أي قضايا أو بلاغات (إيماس، سراج، كناوف).</li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-rose);">
              <div class="card-title" style="color:var(--accent-rose);">النزاعات المحصورة وقواعد العزل الجنائي</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>واقعة 2008 (شحاتة حسن) تاريخية مرتبطة بظروف حبس هشام طلعت واعتراف ACC.</li>
                <li>ادعاء باطن ساوث ميد (2024) عُزي لتأخر سداد جهات عليا للمقاولين (انقطاع الحجية).</li>
                <li>احتجاجات عمال ومهندسي ACC (2024–2025) نزاع أجور داخلي وليس فواتير مقاولين.</li>
              </ul>
            </div>
          </div>
        `,
        contentEn: `
          <div class="grid-2">
            <div class="card" style="border-top:3px solid var(--accent-emerald);">
              <div class="card-title" style="color:var(--accent-emerald);">Confirmed Commercial Partnerships</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>Major repeat contract awards: Concrete Plus ~EGP 10B at SouthMED following Noor.</li>
                <li>Quarter-century continuous collaboration: Andy Lang (LLD) on 6 Four Seasons hotels.</li>
                <li>Regular high-spec technology supply with zero litigation: EMAS, Siraj, Knauf Egypt.</li>
              </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--accent-rose);">
              <div class="card-title" style="color:var(--accent-rose);">Forensic Isolation & Privity Realities</div>
              <ul style="font-size:12px; color:var(--text-muted); line-height:1.8; margin-top:8px; padding-inline-start:16px;">
                <li>2008 case (Shehata) was isolated historical event during crisis, acknowledged by ACC.</li>
                <li>2024 SouthMED claim was attributed to upstream Armed Forces lags, not TMG liability.</li>
                <li>ACC worker/engineer actions (2024-25) represent internal wage disputes, not trade debt.</li>
              </ul>
            </div>
          </div>
        `
      }
    ];'''

if 'SLIDE 10 / 10' not in code:
    code = code.replace(slide_08_end, slide_09_10)
    print("Added Slides 09 and 10 to build_perfect_dashboard.py.")

with open(r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py", "w", encoding="utf-8") as f:
    f.write(code)

print("build_perfect_dashboard.py slide update complete.")
