# -*- coding: utf-8 -*-
"""
Enrich build_perfect_dashboard.py with the verified data from:
1. TMG_Contractor_Sentiment_Step6 (2).md
2. TMG_Atrium_Expanded_Contractor_Network_Review.md
"""

with open(r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Enrich sourcesDB
sources_anchor = '      ccc_atrium_mep_luxor: {'
new_sources = '''      mada_southmed_2024: {
        titleAr: "مدى مصر: ادعاءات عمال ومقاولي باطن محليين بساوث ميد وتأخر مستحقات جهات عليا",
        titleEn: "Mada Masr: Local Subcontractor Dues Report on SouthMED & Upstream Payer Claims",
        publisherAr: "موقع مدى مصر الاستقصائي المستقل (5 نوفمبر 2024)",
        publisherEn: "Mada Masr Investigative Platform (5 Nov 2024)",
        badgeAr: "ادعاء مصدر محلي غير مؤيد بمستند",
        badgeEn: "Uncorroborated Local Source Claim",
        date: "5 نوفمبر 2024",
        url: "https://www.madamasr.com/ar/2024/11/05/news/سياسة/إصابة-شاب-والقبض-على-اثنين-في-اشتباكات/",
        archiveUrl: "https://www.madamasr.com/en/2024/11/05/news/politics/residents-clash-with-military-in-matrouh-to-protest-displacement-for-talaat-moustafa-group-tourism-project-1-person-shot-2-arrested/",
        descAr: `تقرير صحفي أورد ادعاءً لمصدر محلي حول عدم سداد مستحقات أعمال مقاولات باطن لأهالي المنطقة بساوث ميد، وعزا المصدر التأخير لتباطؤ سداد جهات بالقوات المسلحة للمقاولين الرئيسيين. يؤكد تقرير الفحص أن الخبر لا يثبت مديونية مباشرة على طلعت مصطفى أو كونكريت بلس.`,
        descEn: `Report alleging local subcontracting work non-payment on SouthMED, with an anonymous source attributing delay to upstream payments by Armed Forces to prime contractors. Does not establish direct TMG or Concrete Plus liability.`
      },
      mada_engineers_2024: {
        titleAr: "مدى مصر: احتجاج 400 مهندس بشركة الإسكندرية للإنشاءات (مدينتي وسيليا ونور)",
        titleEn: "Mada Masr: 400 ACC Engineers Protest Over Salaries & Healthcare Benefits",
        publisherAr: "موقع مدى مصر (27 مارس 2024)",
        publisherEn: "Mada Masr (27 March 2024)",
        badgeAr: "احتجاج مهني داخلي موثق",
        badgeEn: "Documented Internal Labor Action",
        date: "27 مارس 2024",
        url: "https://www.madamasr.com/ar/2024/03/27/news/سياسة/مهندسو-طلعت-مصطفى-يحتجون-للمطالبة-ب/",
        archiveUrl: "https://www.madamasr.com/ar/2024/03/27/news/سياسة/مهندسو-طلعت-مصطفى-يحتجون-للمطالبة-ب/",
        descAr: `وقفة احتجاجية شارك فيها نحو 400 مهندس من العاملين بشركة الإسكندرية للإنشاءات بمواقع مدينتي وسيليا ونور للمطالبة بزيادة الرواتب لمواكبة التضخم وتحسين التأمين الطبي، وتعد سياقاً عمالياً داخلياً وليس نزاعاً على فواتير مقاولي باطن.`,
        descEn: `Labor action by ~400 ACC engineers across Madinaty, Celia, and Noor demanding cost-of-living adjustments and improved medical benefits. Represents internal workforce remuneration, not subcontractor trade dispute.`
      },
      everlast_openair: {
        titleAr: "إيفرلاست للمقاولات: تصنيع وتركيب جمالونات الحديد لأوبن إير مول مدينتي",
        titleEn: "Everlast Construction: Steel Trusses Fabrication & Erection for Open Air Mall Madinaty",
        publisherAr: "سجل مشاريع شركة إيفرلاست للمقاولات واستشارات ECG",
        publisherEn: "Everlast Construction Works Profile & ECG Engineering",
        badgeAr: "إنجاز أعمال مقاولة باطن متخصصة",
        badgeEn: "Specialist Subcontract Delivery",
        date: "2021 – 2023",
        url: "https://eg.linkedin.com/in/mohamed-zein-86051680",
        archiveUrl: "https://atriumeg.com/portfolio/open-air-mall-madinaty/",
        descAr: `سجل مهني يوثق قيام شركة إيفرلاست للمقاولات بتصنيع وتركيب جمالونات وهياكل الحديد الإنشائية لمشروع أوبن إير مول بمدينتي كأحد مقاولي الباطن المتخصصين تحت إشراف شركة أتريوم والاستشاري العام جماعة المهندسين الاستشاريين (ECG).`,
        descEn: `Engineering record verifying Everlast Construction fabricating and erecting structural steel trusses at Open Air Mall Madinaty as specialist subcontractor under Atrium AQC and supervising consultant ECG.`
      },
      siraj_easthub: {
        titleAr: "سراج للإضاءة: تصميم وتوريد إضاءة الواجهات واللاندسكيب لمول إيست هب مدينتي",
        titleEn: "Siraj Lighting: Facade & Landscape Architectural Lighting for East Hub Madinaty",
        publisherAr: "سجل أعمال شركة سراج العالمية للإضاءة ومول إيست هب",
        publisherEn: "Siraj Lighting Official Project Index",
        badgeAr: "سجل توريد وشراكة معتمد",
        badgeEn: "Verified Architectural Lighting Partner",
        date: "2023 – 2024",
        url: "https://www.linkedin.com/posts/siraj-lighting-company_lightingfromtheheartofegypt-sirajlighting-activity-7084456074832920578-IMdH",
        archiveUrl: "https://atriumeg.com/portfolio/east-hub-mall-at-madinaty/",
        descAr: `توثيق رسمي لتوريد أنظمة الإضاءة المعمارية لواجهات وشوارع إيست هب مول بمدينتي، ضمن شبكة تعاقدية ضمت العربية للمشروعات (المالك)، دار الهندسة (مدير المشروع)، وأتريوم (المقاول العام).`,
        descEn: `Corporate supplier statement detailing architectural lighting design and supply for East Hub Madinaty under developer ACPUD, Dar Al-Handasah (PM), and Atrium (EPC).`
      },
      emas_elsewedy_noor: {
        titleAr: "إيماس السويدي: توريد موزعات الجهد المتوسط Simoprime لمدينة نور",
        titleEn: "EMAS El Sewedy: Siemens Simoprime 24kV Medium-Voltage Switchgear for Noor City",
        publisherAr: "شركة السويدي إندستريز (EMAS El Sewedy) ومجموعة شاكر",
        publisherEn: "EMAS El Sewedy Industries & Shaker Consultancy Group",
        badgeAr: "توريد مهمات بنية تحتية ذكية",
        badgeEn: "Smart Infrastructure Equipment Supply",
        date: "2024 – 2025",
        url: "https://www.linkedin.com/posts/sayed-mahmoud-pmp%C2%AE-pmi-acp%C2%AE-mba-rolling-66030511a_simoprime-development-electrificationandautomation-activity-7376736839182823424",
        archiveUrl: "https://elsewedy.com",
        descAr: `إفصاح رسمي عن تصنيع وتوريد خلايا الجهد المتوسط طراز Simoprime 24 kV لشبكات التوزيع الذكية بمدينة نور، بإشراف استشاري المشروع مجموعة شاكر للاستشارات الهندسية والشركة العربية للاستثمار العمراني.`,
        descEn: `Official supplier milestone confirming delivery of Siemens Simoprime 24 kV switchgear for Noor City electrical grid under Arab Co. for Urban Investment and Shaker Consultancy.`
      },
      andy_lang_lld: {
        titleAr: "تصميمات LLD العالمية: شراكة ممتدة 25 عاماً في مشروعات فورسيزونز طلعت مصطفى",
        titleEn: "LLD Lighting Design: 25-Year Partnership Across TMG Four Seasons Developments",
        publisherAr: "أندي لانغ (LLD International) وسجلات فورسيزونز كابيتال مدينتي",
        publisherEn: "Andy Lang / LLD International & Four Seasons Records",
        badgeAr: "شراكة استشارية ممتدة (25 عاماً)",
        badgeEn: "Long-Term Professional Partnership (25 Years)",
        date: "2024 – 2026",
        url: "https://www.linkedin.com/posts/andy-lang-8094b05_construction-continues-on-thefour-seasons-activity-7417638710898397185-kjA7",
        archiveUrl: "https://www.fourseasons.com",
        descAr: `بيان مهني موثق من المصمم العالمي أندي لانغ يؤكد أن فندق فورسيزونز نيو كايرو كابيتال بمدينتي يمثل المشروع السادس لفورسيزونز بمصر والتعاون الممتد لأكثر من ربع قرن مع مجموعة طلعت مصطفى، كدليل استمرارية وتكرار أعمال رفيع المستوى.`,
        descEn: `First-person professional statement from lighting designer Andy Lang highlighting Four Seasons New Cairo Capital as the 6th Egypt FS project and a ~25-year working relationship with TMG.`
      },
      devzah_cairo_capital: {
        titleAr: "سجل استلام المواد (MIR-11): توريد شركة ديفزاه لمشروع فورسيزونز كابيتال CP05",
        titleEn: "Material Inspection Record (MIR-11): Devzah SI Subcontractor at Four Seasons CP05",
        publisherAr: "سجلات الفحص الهندسي واستلام المواد تحت إشراف هيل إنترناشيونال",
        publisherEn: "Engineering Material Inspection Record & Hill International",
        badgeAr: "مستند فحص واستلام مواد هندسي",
        badgeEn: "Engineering Inspection Docket",
        date: "2023 – 2024",
        url: "https://www.scribd.com/document/928303864/MIR-11",
        archiveUrl: "https://atriumeg.com",
        descAr: `مستند فحص واستلام مواد (Material Inspection Report) يوثق عمل شركة Devzah SI كمقاول باطن / مورد لحزمة الفندق CP05 المنفذة عبر تحالف أتريوم وCCC تحت إشراف مدير المشروع هيل إنترناشيونال.`,
        descEn: `Material Inspection Request (MIR-11) record identifying Devzah SI as trade vendor/subcontractor under Atrium-CCC JV for Package CP05 overseen by Hill International.`
      },
      knauf_luxor: {
        titleAr: "كناوف مصر: توريد أنظمة الجبس بورد المتطورة لفندق فورسيزونز الأقصر",
        titleEn: "Knauf Egypt: Advanced Drywall & Gypsum Systems for Four Seasons Luxor",
        publisherAr: "شركة كناوف مصر واستشارات معمارية معمار إنتريرز",
        publisherEn: "Knauf Egypt Corporate & Mimar Interiors",
        badgeAr: "سجل شراكة وتوريد تخصصي",
        badgeEn: "Specialist Drywall Systems Partner",
        date: "2024 – 2025",
        url: "https://www.linkedin.com/company/knauf-egypt/",
        archiveUrl: "https://knauf.eg",
        descAr: `بيان رسمي يوثق اعتماد وتوريد قواطع وأنظمة الجبس المقاوم للرطوبة والحريق من كناوف مصر لفندق فورسيزونز الأقصر بالتعاون مع المقاول العام والتحالف المنفذ، واستشاري التصميم الداخلي معمار إنتريرز.`,
        descEn: `Corporate supplier statement detailing Knauf Egypt gypsum partitions for Four Seasons Luxor under Atrium-CCC execution and Mimar Interiors design consultancy.`
      },
      elhadad_claims_2022: {
        titleAr: "دراسة استشارية لمطالبات المقاولات: أثر تأخر صرف المستخلصات الجارية على سلاسل الإمداد",
        titleEn: "Construction Claims Analysis: Systemic Impacts of Interim Payment Certification Delays",
        publisherAr: "الاستشاري محمد الحداد (خبير إدارة العقود والمطالبات الهندسية)",
        publisherEn: "Mohamed Elhadad (Contracts & Claims Advisory)",
        badgeAr: "تحليل فني لصناعة المقاولات",
        badgeEn: "Industry Claims & Contracts Benchmark",
        date: "2022",
        url: "https://ae.linkedin.com/posts/mohamed-elhadad-%D9%85%D8%AD%D9%85%D8%AF-%D8%A7%D9%84%D8%AD%D8%AF%D8%A7%D8%AF-81883569_%D8%A7%D9%84%D9%86%D8%B2%D8%A7%D8%B9-%D8%A7%D9%84%D9%85%D9%86%D8%B4%D8%A3-%D9%84%D9%84%D9%85%D8%B7%D8%A7%D9%84%D8%A8%D8%A7%D8%AA-9-%D8%AA%D8%A3%D8%AE%D9%8A%D8%B1-%D8%B5%D8%B1%D9%81-activity-6882910353459401444-UHoa",
        archiveUrl: "https://linkedin.com",
        descAr: `تحليل فني وتعاقدي متخصص يشرح الآليات التي يؤدي بها تأخير اعتماد المستخلصات وصرفها إلى اختناق السيولة لدى مقاولي الباطن، مما يولد نزاعات تمديد وقت (EOT) وغرامات تأخير ومطالبات تعويضية.`,
        descEn: `Technical analysis detailing how interim payment certification bottlenecks create severe working capital strain for subcontractors, triggering extension of time (EOT) and prolongation claims.`
      },
'''

if 'mada_southmed_2024' not in code:
    code = code.replace(sources_anchor, new_sources + sources_anchor)
    print("Added new sources to sourcesDB.")

# 2. Enrich contractorsData
contractors_anchor = '    const complaintsData = ['
new_contractors = '''      {
        projectAr: "أوبن إير مول مدينتي (Open Air Mall)",
        projectEn: "Open Air Mall Madinaty",
        clientAr: "الشركة العربية للمشروعات (ACPUD)",
        clientEn: "Arab Co. for Projects & Urban Dev.",
        mainContractorAr: "شركة أتريوم للمقاولات (Atrium AQC)",
        mainContractorEn: "Atrium Quality Contractors",
        subcontractorAr: "شركة إيفرلاست للمقاولات (Everlast Construction)",
        subcontractorEn: "Everlast Construction",
        scopeAr: "تصنيع وتوريد وتركيب الجمالونات والهياكل الإنشائية الحديدية للصالات التجارية بإشراف استشارات ECG",
        scopeEn: "Fabrication & erection of structural steel trusses for commercial halls under ECG supervision",
        docAr: "سجل مشاريع إيفرلاست واستشارات ECG",
        docEn: "Everlast Track Record & ECG Project Filings",
        noteAr: "تنسيق هندسي دقيق للبحور الإنشائية الكبيرة؛ إنجاز تجاري وتسليم ناجح دون نزاعات معلنة",
        noteEn: "Complex structural spans; no payment disputes on record; successful delivery",
        flagAr: "تسليم ناجح (Level A)",
        flagEn: "Delivered (Level A)",
        badge: "badge-low",
        sourceKey: "everlast_openair"
      },
      {
        projectAr: "إيست هب مول مدينتي (East Hub)",
        projectEn: "East Hub Commercial Mall (Madinaty)",
        clientAr: "الشركة العربية للمشروعات (ACPUD)",
        clientEn: "Arab Co. for Projects & Urban Dev.",
        mainContractorAr: "شركة أتريوم للمقاولات (Atrium AQC)",
        mainContractorEn: "Atrium Quality Contractors",
        subcontractorAr: "سراج للإضاءة (Siraj Lighting) / سكوير / MCBS",
        subcontractorEn: "Siraj Lighting / SQUARE / MCBS",
        scopeAr: "تصنيع وتوريد شبكات الإضاءة المعمارية للواجهات والشوارع، وتشطيبات MEP، بإشراف دار الهندسة (EHAF)",
        scopeEn: "Architectural facade & street lighting design & supply, MEP packages under Dar Al-Handasah (EHAF)",
        docAr: "إفصاحات رسمية لشركة سراج وأتريوم",
        docEn: "Siraj Lighting & Atrium Quality Disclosures",
        noteAr: "حزم متعددة الأطراف تتطلب تنسيق اعتمادات استشاري المشروع؛ توريد منتظم",
        noteEn: "Multi-party package requiring consultant sign-offs; regular supply",
        flagAr: "توريد معتمد (Level B)",
        flagEn: "Verified Supply (Level B)",
        badge: "badge-low",
        sourceKey: "siraj_easthub"
      },
      {
        projectAr: "مدينة نور (حدائق العاصمة - البنية الذكية)",
        projectEn: "Noor Smart City (MV Grid Infrastructure)",
        clientAr: "الشركة العربية للاستثمار العمراني",
        clientEn: "Arab Co. for Urban Investment SAE",
        mainContractorAr: "شركة أتريوم للمقاولات / الإسكندرية للإنشاءات",
        mainContractorEn: "Atrium Quality Contractors / ACC",
        subcontractorAr: "إيماس السويدي (EMAS El Sewedy / السويدي إندستريز)",
        subcontractorEn: "EMAS El Sewedy Industries",
        scopeAr: "تصنيع وتوريد خلايا الجهد المتوسط 24 ك.ف (Simoprime) لشبكات التوزيع الذكية بإشراف مجموعة شاكر",
        scopeEn: "Manufacturing & supply of Siemens Simoprime 24 kV MV switchgear under Shaker Group supervision",
        docAr: "إعلان رسمي صادر عن إيماس السويدي (2025)",
        docEn: "Official EMAS El Sewedy Milestone (2025)",
        noteAr: "توريد تقني رفيع المستوى؛ شروط دفع تجارية للمطور؛ لا توجد شكاوى مستحقات",
        noteEn: "High-spec technology supply; negotiated vendor credit terms; zero complaints recorded",
        flagAr: "بنية ذكية (Level B)",
        flagEn: "Smart Infra (Level B)",
        badge: "badge-low",
        sourceKey: "emas_elsewedy_noor"
      },
      {
        projectAr: "فورسيزونز نيو كايرو كابيتال (مدينتي)",
        projectEn: "Four Seasons New Cairo Capital at Madinaty",
        clientAr: "مدينتي للمشروعات السياحية / آيكون",
        clientEn: "Madinaty Co. for Tourism / ICON",
        mainContractorAr: "تحالف أتريوم وCCC (Package CP05)",
        mainContractorEn: "Atrium - CCC Joint Venture (CP05)",
        subcontractorAr: "شركة ديفزاه (Devzah SI) / LLD Lighting Design",
        subcontractorEn: "Devzah SI / LLD Lighting (Andy Lang)",
        scopeAr: "حزمة المقاول العام CP05، فحص المواد MIR-11 وتصميمات الإضاءة الفندقية (شراكة ممتدة 25 عاماً)",
        scopeEn: "Package CP05 main works, MIR-11 material inspection & lighting design (25-yr partnership)",
        docAr: "محاضر فحص المواد (MIR-11) وإفصاح المصمم أندي لانغ",
        docEn: "Engineering MIR-11 & Andy Lang Statement",
        noteAr: "تطبيق معايير فورسيزونز الدولية الصارمة بإشراف هيل إنترناشيونال؛ نموذج شراكة إيجابي ممتد",
        noteEn: "Strict Four Seasons specifications under Hill International; positive repeat partnership",
        flagAr: "شراكة ممتدة (Level A)",
        flagEn: "Repeat Partner (Level A)",
        badge: "badge-low",
        sourceKey: "andy_lang_lld"
      },
      {
        projectAr: "سيليا (العاصمة الإدارية - الفيلات والمرافق)",
        projectEn: "Celia (New Capital Villas & Village Packages)",
        clientAr: "الشركة العربية للمشروعات (ACPUD)",
        clientEn: "Arab Co. for Projects & Urban Dev.",
        mainContractorAr: "شركة أتريوم للمقاولات (Atrium AQC)",
        mainContractorEn: "Atrium Quality Contractors",
        subcontractorAr: "تحالفات مقاولي تشطيب وبنية تحتية محلية",
        subcontractorEn: "Local Finishing & Infrastructure Trade Subcontractors",
        scopeAr: "تنفيذ عمارات وفيلات قرية سيليا ومركز الخدمات والشبكات بإشراف استشاري حمزة وشركاه",
        scopeEn: "Execution of Celia village clusters, service centres & utilities under Hamza Associates",
        docAr: "دليل مشاريع شركة أتريوم الرسمي وتقارير الإنجاز",
        docEn: "Official Atrium Projects Directory & Progress",
        noteAr: "ضغوط التنسيق الموقعي مع شبكات العاصمة ACUD؛ التزام تعاقدي معزز بالقوة القاهرة",
        noteEn: "Site coordination challenges with ACUD municipal grids; force majeure defense on master utilities",
        flagAr: "تسليم مرحلي (Level A)",
        flagEn: "Phased Handover (Level A)",
        badge: "badge-med",
        sourceKey: "alborsanews_atrium"
      },
'''

if 'everlast_openair' not in code:
    code = code.replace(contractors_anchor, new_contractors + contractors_anchor)
    print("Added new contractors to contractorsData.")

# 3. Enrich complaintsData
complaints_anchor = '    const risksData = ['
new_complaints = '''      {
        projectAr: "ساوث ميد (ادعاء مقاولي الباطن المحليين)",
        projectEn: "SouthMED (Local Subcontractors Payment Allegation)",
        categoryAr: "ادعاء عدم سداد باطن ونزاع جهات عليا",
        categoryEn: "Subcontractor Dues & Upstream Payer Pass-Through",
        claimAr: "أورد موقع مدى مصر ادعاءً لمصدر محلي بأن عمالاً وسائقين ومقاولي باطن محليين لم يتسلموا مستحقاتهم عن أعمال بساوث ميد؛ ونسب المصدر السبب إلى تأخر سداد جهات بالقوات المسلحة لمستحقات المقاولين الرئيسيين. يؤكد التدقيق الجنائي أن هذا الادعاء صادر عن مصدر مجهول ولا يثبت أن طلعت مصطفى أو كونكريت بلس مدينة مباشرة لهؤلاء المقاولين.",
        claimEn: "Mada Masr reported an allegation by an anonymous local source that local subcontracting workers on SouthMED had not received dues, attributing the issue to delayed payments by Armed Forces to primary contractors. Forensic review confirms this is an indirect upstream pass-through allegation and does not establish that TMG or Concrete Plus owed or withheld the money.",
        date: "5 نوفمبر 2024",
        sourceName: "مدى مصر (تقرير استقصائي)",
        sourceKey: "mada_southmed_2024",
        classAr: "ادعاء مصدر محلي غير مؤيد بمستند (خطر سلاسل إمداد عليا)",
        classEn: "Uncorroborated Local Source Claim (Upstream Pass-Through Risk)",
        badge: "badge-med"
      },
      {
        projectAr: "شركة الإسكندرية للإنشاءات (وقفة 400 مهندس)",
        projectEn: "Alexandria Construction (400 Engineers Protest)",
        categoryAr: "أجور وبدلات ورعاية صحية داخلية",
        categoryEn: "Internal Professional Salaries & Benefits",
        claimAr: "نظم نحو 400 مهندس بشركة الإسكندرية للإنشاءات التابعة لمجموعة طلعت مصطفى وقفة احتجاجية في مشروعات مدينتي وسيليا ونور للمطالبة بزيادة الرواتب ورفع بدلات الانتقال وتحسين التأمين الطبي في مواجهة التضخم. يجب تصنيف هذه الواقعة بدقة كنزاع أجور عمالة مهنية داخلية، وليس دليلاً على امتناع الشركة عن سداد فواتير مقاولي الباطن التجاريين.",
        claimEn: "Around 400 engineers at Alexandria Construction (ACC) across Madinaty, Celia, and Noor protested demanding salary inflation indexation and enhanced medical benefits. Due diligence classifies this strictly as internal professional employee remuneration, not evidence of unpaid commercial subcontractor certificates.",
        date: "27 مارس 2024",
        sourceName: "مدى مصر (تغطية عمالية)",
        sourceKey: "mada_engineers_2024",
        classAr: "نزاع عمالي مهني داخلي (منفصل عن مستخلصات المقاولين)",
        classEn: "Internal Labor Remuneration (Separated from Trade Subcontracts)",
        badge: "badge-med"
      },
      {
        projectAr: "قطاع الإنشاءات وإدارة المطالبات (تحليل فني)",
        projectEn: "Construction Sector Claims Advisory (Technical Commentary)",
        categoryAr: "مخاطر تأخير اعتماد المستخلصات (IPCs)",
        categoryEn: "Interim Payment Certificate (IPC) Delay Mechanics",
        claimAr: "يوضح الاستشاري محمد الحداد (خبير إدارة العقود والمطالبات) في دراسته المهنية أن تأخير اعتماد المستخلصات الجارية يمثل الجذر الرئيسي للنزاعات الإنشائية، حيث يجبر مقاول الباطن على تمويل المشروع ذاتياً، وحين تنفد سيولته يتوقف العمل وتوقع عليه غرامات تأخير جزافية، ما يحتم وجود حسابات وسيطة (Escrow) وجداول فحص محددة المدد.",
        claimEn: "Claims expert Mohamed Elhadad analyzes how delayed interim payment certifications trigger subcontractor liquidity crises, leading to project paralysis and asymmetric delay penalty exposure, highlighting the necessity of escrow payment mechanisms.",
        date: "2022",
        sourceName: "تحليل تعاقدي منشور",
        sourceKey: "elhadad_claims_2022",
        classAr: "تحليل فني عام لقطاع المقاولات (معيار قياسي للصناعة)",
        classEn: "General Construction Industry Commentary (Benchmark)",
        badge: "badge-low"
      },
'''

if 'mada_southmed_2024' not in code:
    code = code.replace(complaints_anchor, new_complaints + complaints_anchor)
    print("Added new complaints to complaintsData.")

with open(r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py", "w", encoding="utf-8") as f:
    f.write(code)

print("build_perfect_dashboard.py updated successfully.")
