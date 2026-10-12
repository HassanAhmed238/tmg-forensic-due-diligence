
    const document = {
      documentElement: { setAttribute: () => {}, getAttribute: () => 'ar' },
      getElementById: (id) => ({ innerHTML: '', textContent: '', value: '50000000', style: {}, classList: { toggle: () => {}, add: () => {}, remove: () => {} }, getContext: () => ({}) }),
      querySelectorAll: () => [],
      querySelector: () => null,
      addEventListener: () => {}
    };
    const window = { addEventListener: () => {} };
    const localStorage = { getItem: () => 'ar', setItem: () => {} };
    const Chart = function() { return { destroy: () => {} }; };
    const d3 = { select: () => ({ append: () => ({ attr: () => ({}) }) }) };
    
const TMG_COMPANIES = [{"id": 1, "name": "Concrete Plus for Engineering & Construction", "role": "مقاول خارجي\n179 مبنى سكنيًا كامل التشطيب وبنية تحتية؛ Zone C01", "project": "SouthMED", "relation": "عقد معلن مع TMG", "phone": "+20 2 2307 6581 / +20 2 2307 6582", "phone_notes": "الخط العام للشركة — منشور على الموقع الرسمي", "email": "info@concrete-plus.net", "website": "https://concrete-plus.net/", "rel_source": "https://www.egypttoday.com/Article/3/144267/Talaat-Moustafa-Group-TMG-signs-EGP-10B-200M-construction-contracts | https://www.dailynewsegypt.com/2025/12/30/tmg-signs-egp-10bn-contract-with-concrete-plus-for-south-med-phase/", "phone_source": "https://concrete-plus.net/contact-us/", "evidence_level": "A/B", "confidence": "مرتفعة", "notes": "أصل العقد غير منشور؛ لا دليل منشور هنا على مستخلصات غير مدفوعة"}, {"id": 2, "name": "Consolidated Contractors Company (CCC)", "role": "مقاول/شريك JV\nمقاول مشترك مع Atrium في Four Seasons Cairo Capital", "project": "مدينتي", "relation": "علاقة مؤكدة عبر JV؛ لا تفترض عقد منفرد لـCCC مع TMG", "phone": "+30 210 618 2000 (المقر المركزي؛ لم أتحقق من رقم مصري مباشر)", "phone_notes": "رقم الشركة المركزي؛ موقع مصر منشور دون رقم محلي في صفحة التواصل", "email": "cccmail@ccc.net", "website": "https://www.ccc.net/", "rel_source": "https://atriumeg.com/portfolio/four-seasons-hotel-and-private-residences-new-cairo-capital-at-madinaty/ | https://www.linkedin.com/posts/hill-international_on-january-21-hill-joined-talaat-moustafa-activity-6761996655584718848-Jt2v", "phone_source": "https://www.ccc.net/wp-content/uploads/2022/08/qr-ccc-building_the_future-corporate_capability.pdf", "evidence_level": "A/B", "confidence": "مرتفعة للعلاقة", "notes": "حصة كل شريك وشروط الدفع غير منشورة"}, {"id": 3, "name": "Atrium Quality Contractors (Atrium)", "role": "ذراع مقاولات بالمجموعة\nتنفيذ مشروعات سكنية ومولات ومدارس وفنادق وبنية أساسية", "project": "مدينتي، الرحاب، نور، Celia، شرم الشيخ", "relation": "شركة ضمن منظومة TMG وليست طرفًا خارجيًا مستقلًا تلقائيًا", "phone": "المقر: +20 2 3331 2000 | الرحاب: +20 2 2693 1643 / 1647 / 1648", "phone_notes": "الخط العام للمقر وفرع الرحاب", "email": "info@atriumeg.com", "website": "https://atriumeg.com/", "rel_source": "https://atriumeg.com/projects/ | https://atriumeg.com/", "phone_source": "https://atriumeg.com/contact/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "المحفظة المنشورة ليست كشفًا كاملاً بالموردين أو المقاولين الفرعيين"}, {"id": 4, "name": "Alexandria Construction Company (ACC)", "role": "مقاولات؛ مرتبطة بالمجموعة\nمقاول بمراحل الرحاب؛ يظهر اسم ACC/Atrium JV في محضر SouthMED", "project": "الرحاب؛ SouthMED", "relation": "علاقة موثقة تاريخيًا في الرحاب؛ ذكر SouthMED من محضر طرف ثالث", "phone": "+20 3 360 9269 / +20 3 360 0278", "phone_notes": "أرقام التواصل كما نشرها موقع الشركة؛ راجع الصيغة الدولية قبل الاتصال", "email": "info@alexconstruction.com.eg", "website": "https://www.acc.eg/", "rel_source": "https://pme-consultancy.com/2022/06/02/el-rehab-city-project/ | https://www.acc.eg/الرئيسية/ | https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://www.acc.eg/contact-us-en/", "evidence_level": "A/B للرحاب؛ C لـSouthMED", "confidence": "مرتفعة للرحاب؛ متوسطة للمحضر", "notes": "نسبة الملكية الحالية وحزمة SouthMED غير مثبتتين في المصادر المستخدمة"}, {"id": 5, "name": "SQUARE Engineering Firm", "role": "مقاول/تشطيبات وأعمال عامة\nمحفظة مشروعات مع APUD؛ ومذكور في اجتماع تنسيق SouthMED", "project": "مدينتي؛ SouthMED", "relation": "المحفظة تثبت مشروعات متصلة؛ تفاصيل حزمة SouthMED غير منشورة", "phone": "+20 105 010 6594", "phone_notes": "رقم التواصل العام الظاهر في موقع الشركة", "email": "", "website": "https://www.square.com.eg/", "rel_source": "https://www.square.com.eg/ | https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://www.square.com.eg/", "evidence_level": "B/C", "confidence": "متوسطة", "notes": "لا يوجد عقد محدد أو قيمة أو بيانات مستحقات في المصادر المستخدمة"}, {"id": 6, "name": "El Soadaa Group", "role": "مقاول محتمل/مشارك موقع\nمذكور ضمن شركات المقاولين في محضر SouthMED", "project": "SouthMED", "relation": "اسم وارد بمحضر مشروع منشور على منصة طرف ثالث", "phone": "+20 2 2704 1297", "phone_notes": "الخط العام للشركة", "email": "info@elsoadaa.com", "website": "https://elsoadaa.com/", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE | https://elsoadaa.com/company/", "phone_source": "https://elsoadaa.com/contact/", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "الحزمة والعقد والقيمة غير معروفة؛ يلزم أصل التعاقد"}, {"id": 7, "name": "Gharably Integrated Engineering Company (GIECO)", "role": "مقاول بنية تحتية محتمل\nمحضر SouthMED يسرد El Gharably ضمن أعمال/تنسيق البنية التحتية", "project": "SouthMED", "relation": "المحضر مصدر غير موثق رسميًا؛ موقع GIECO يثبت التخصص لا عقد TMG", "phone": "+20 3 429 7889", "phone_notes": "الخط العام للشركة — الإسكندرية", "email": "info@gharably.com", "website": "https://gharably.com/", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE | https://gharably.com/", "phone_source": "https://gharably.com/home/", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "لا عقد أو قيمة أو مستخلصات منشورة"}, {"id": 8, "name": "Al Shorouq Construction Co.", "role": "مقاول مشارك بالمشروع وفق محضر\nمذكور بين المقاولين في محضر SouthMED", "project": "SouthMED", "relation": "دليل محضر فني فقط", "phone": "مرشح فقط: +20 2 2247 2395", "phone_notes": "رقم من دليل أعمال لكيان باسم قريب؛ مطابقة الهوية مع اسم SouthMED غير مؤكدة", "email": "", "website": "https://www.alshorouk.com/", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://gludo.org/en/business-directory/1613-al-shorouk-construction", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "لا نطاق أو عقد أصلي أو قيمة معلنة\nلا تستخدم الرقم على أنه مؤكد للشركة المذكورة في محضر SouthMED قبل تأكيد الاسم القانوني."}, {"id": 9, "name": "Knauf Egypt", "role": "مورد أنظمة ومواد بناء\nتقول الشركة إن حلولها استخدمت في Four Seasons Luxor", "project": "Four Seasons Luxor", "relation": "صلة توريد/منتجات معلنة من حساب الشركة؛ مباشر/غير مباشر غير محسوم", "phone": "17300", "phone_notes": "مركز خدمة العملاء / الاستفسارات في مصر", "email": "", "website": "https://knauf.com/en-EG", "rel_source": "https://www.linkedin.com/company/knauf-egypt/", "phone_source": "https://knauf.com/en-EG", "evidence_level": "B", "confidence": "متوسطة-مرتفعة", "notes": "لا أمر شراء أو مبلغ أو رصيد مستحق منشور"}, {"id": 10, "name": "DEVZAH SI", "role": "مورد محتمل – الاسم كما ورد\nتظهر كبائع في بيان استلام مواد بمشروع Four Seasons Cairo Capital CP05", "project": "مدينتي", "relation": "مستند فحص مواد على Scribd؛ علاقة توريد غير مباشرة محتملة", "phone": "غير منشور/لم يُعثر على رقم موثوق", "phone_notes": "لا توجد مطابقة موثوقة لهوية الشركة في المصادر المفتوحة التي تمت مراجعتها", "email": "", "website": "", "rel_source": "https://www.scribd.com/document/928303864/MIR-11", "phone_source": "", "evidence_level": "C", "confidence": "متوسطة-منخفضة", "notes": "المستند غير مصادق عليه رسميًا؛ لا قيمة عقد أو دليل دين\nالاسم ورد في مستند مواد منشور على منصة طرف ثالث؛ يلزم مطابقة الاسم القانوني."}, {"id": 11, "name": "Cleopatra Company (الهوية القانونية غير مؤكدة)", "role": "مورد محتمل\nمحضر SouthMED يذكر توريد سيراميك وأدوات صحية لنموذج فيلات", "project": "SouthMED", "relation": "اسم مورد في محضر طرف ثالث؛ لا يثبت أنه Ceramica Cleopatra", "phone": "غير متاح — لا توجد مطابقة مؤكدة للكيان", "phone_notes": "لا ينبغي استخدام رقم سيراميكا كليوباترا دون إثبات أن المورد المذكور هو نفس الكيان", "email": "", "website": "", "rel_source": "https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE | https://www.cleopatraceramics.com/en/factories/", "phone_source": "", "evidence_level": "C", "confidence": "منخفضة-متوسطة", "notes": "يلزم مطابقة الاسم القانوني قبل ربطه بمجموعة سيراميكا كليوباترا\nمحضر المشروع يذكر Cleopatra Company فقط؛ لم يتم تأكيد تطابقها مع Ceramica Cleopatra."}, {"id": 12, "name": "Richmond Group Egypt", "role": "مقاول ظاهر في مستند موقع\nتجديد Aqua & Steak House في Four Seasons Nile Plaza", "project": "القاهرة", "relation": "مذكور كمقاول رئيسي في نموذج فحص/اعتماد مادة منشور", "phone": "+20 2 2519 2015", "phone_notes": "رقم في دليل أعمال خارجي؛ يجب تأكيد أنه ما زال يعمل", "email": "", "website": "https://www.rgegypt.com/", "rel_source": "https://www.scribd.com/document/343504517/INSPECTION-REQUEST-and-Mateiral-Approval-Aqua", "phone_source": "https://www.bizmideast.com/EG/richmond-group-egypt-company-02-25192015", "evidence_level": "C", "confidence": "منخفضة-متوسطة", "notes": "مستند منفرد غير رسمي؛ نطاق العقد وقيمته غير معلومين\nالموقع الرسمي لم يكن قابلاً للتحقق من صفحة الاتصال أثناء البحث؛ رقم الهاتف ليس مؤكدًا من مصدر الشركة."}, {"id": 13, "name": "Hill International", "role": "استشاري إدارة مشروع/إشراف\nFour Seasons Cairo Capital ومشاركات تنسيق/إشراف", "project": "مدينتي؛ SouthMED (ضمن محضر)", "relation": "موثق في صفحة Atrium وإعلان Hill؛ SouthMED مستند أضعف", "phone": "+20 2 2322 0000", "phone_notes": "مكتب القاهرة / الخط المحلي المنشور في ملف الشركة", "email": "", "website": "https://www.hillintl.com/", "rel_source": "https://atriumeg.com/portfolio/four-seasons-hotel-and-private-residences-new-cairo-capital-at-madinaty/ | https://www.linkedin.com/posts/hill-international_on-january-21-hill-joined-talaat-moustafa-activity-6761996655584718848-Jt2v", "phone_source": "https://www.hillintl.com/wp-content/uploads/2023/02/Hill-International-Cost-Consultancy-India-02-28-23.pdf", "evidence_level": "A/B؛ C في SouthMED", "confidence": "مرتفعة لـFour Seasons", "notes": "لا معلومات عامة هنا عن أتعاب أو مستحقات"}, {"id": 14, "name": "Dar Al-Handasah", "role": "استشاري هندسي\nEast Hub Mall وMadinaty Medical Center ومشروع شرم الشيخ", "project": "مدينتي؛ شرم الشيخ", "relation": "مسمى في صفحات Atrium الرسمية", "phone": "+20 2 3531 8000 (صفحة الاتصال الحالية) | +20 2 3531 0501 (صفحة مكتب أخرى)", "phone_notes": "مكتب القاهرة؛ تختلف الأرقام بين صفحات الاتصال الرسمية", "email": "info@dar.com / cairo@dar.com", "website": "https://www.dar.com/", "rel_source": "https://atriumeg.com/portfolio/east-hub-mall-at-madinaty/ | https://atriumeg.com/portfolio/madinaty-medical-center/ | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/", "phone_source": "https://www.dar.com/contact/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "أتعاب الاستشاري والمستحقات غير منشورة"}, {"id": 15, "name": "EHAF Consulting Engineers", "role": "استشاري هندسي\nمذكور باستشاريي East Hub Mall", "project": "مدينتي", "relation": "صفحة مشروع رسمية من Atrium", "phone": "+20 2 3760 1099 / +20 2 3760 8664", "phone_notes": "مكتب القاهرة", "email": "ehaf@ehaf.com", "website": "https://ehaf.com/", "rel_source": "https://atriumeg.com/portfolio/east-hub-mall-at-madinaty/", "phone_source": "https://ehaf.com/contact-ehaf/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "التوزيع الدقيق للنطاق بين EHAF وDar لم يفصل بالصفحة المختصرة"}, {"id": 16, "name": "ECG Engineering Consultants Group", "role": "استشاري هندسي\nOpen Air Mall وFour Seasons Sharm El Sheikh", "project": "مدينتي؛ شرم الشيخ", "relation": "صفحات Atrium الرسمية", "phone": "+20 2 2352 4740 / +20 2 2352 5748", "phone_notes": "مكاتب القاهرة — مدينة نصر / القرية الذكية", "email": "ecg@ecgsa.com", "website": "https://www.ecgsa.com/", "rel_source": "https://atriumeg.com/portfolio/open-air-mall-at-madinaty/ | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/", "phone_source": "https://www.ecgsa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "لا بيانات عن أتعاب أو مستحقات في المصادر التي روجعت"}, {"id": 17, "name": "Shaker Consultancy Group / SCG", "role": "استشاري تصميم/إشراف\nThe Strip Mall، Noor City، Four Seasons Sharm، ويظهر في محضر SouthMED", "project": "مدينتي؛ نور؛ شرم الشيخ؛ SouthMED", "relation": "A في صفحات Atrium؛ C في محضر SouthMED", "phone": "+20 2 2587 2500", "phone_notes": "مكتب القاهرة الجديدة", "email": "infocairo@shakergroup.com", "website": "https://shakergroup.com/", "rel_source": "https://atriumeg.com/portfolio/the-strip-mall-at-madinaty/ | https://atriumeg.com/portfolio/72-residential-buildings-at-noor-city/ | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/ | https://www.scribd.com/document/1051636804/PEG-1202-GN01-CN-HI-MOM-0032-TE", "phone_source": "https://shakergroup.com/contact/", "evidence_level": "A/C", "confidence": "مرتفعة للمشروعات الرسمية", "notes": "محضر SouthMED لا يثبت العقد وقيمته"}, {"id": 18, "name": "Raafat Miller Consulting / RMC", "role": "استشاري هندسي\nGateway Mall؛ All Seasons Park؛ RMC في تقرير HQ ومحضر SouthMED", "project": "الرحاب؛ مدينتي؛ SouthMED؛ مقر TMG الجديد", "relation": "صفحات Atrium تثبت بعض الأعمال؛ اختصار RMC في المستندات يحتاج مطابقة الاسم", "phone": "غير متحقق للكيان المحدد", "phone_notes": "لا تستخدم رقم شركة أخرى تحمل اسم Raafat دون مطابقة الاسم القانوني", "email": "", "website": "", "rel_source": "https://atriumeg.com/portfolio/gateway-mall-at-rehab-city/ | https://atriumeg.com/portfolio/all-seasons-park-at-madinaty/ | https://www.scribd.com/document/882859909/P0250-ATR-DPR-TMG-00010", "phone_source": "", "evidence_level": "A/C", "confidence": "مرتفعة للصفحات الرسمية؛ متوسطة للاختصار", "notes": "لا تدمج كل اسم RMC مع Raafat Miller دون مستند تعريف\nالاسم/الاختصار يحتاج تأكيدًا قانونيًا."}, {"id": 19, "name": "Hamza Associates", "role": "استشاري هندسي\nCelia New Capital وAll Seasons Park", "project": "العاصمة الإدارية؛ مدينتي", "relation": "صفحات مشروعات Atrium", "phone": "+20 2 3760 7238", "phone_notes": "المقر الرئيسي — الدقي", "email": "consult@hamza.org", "website": "https://www.hamza.org/", "rel_source": "https://atriumeg.com/portfolio/celia-new-capital/ | https://atriumeg.com/portfolio/all-seasons-park-at-madinaty/", "phone_source": "https://www.hamza.org/offices.html", "evidence_level": "A", "confidence": "مرتفعة", "notes": "أتعاب/مستحقات غير منشورة"}, {"id": 20, "name": "DMA Architects / DMA Design & Engineering Consultancy", "role": "استشاري تصميم\nPrivado وMadinaty V24 Villas", "project": "مدينتي", "relation": "صفحات مشروعات Atrium؛ الاسم مختلف بين الصفحتين", "phone": "لم يُعثر على رقم هاتف رسمي موثوق في صفحة الاتصال المفتوحة", "phone_notes": "الموقع الرسمي وصفحة LinkedIn متاحان؛ رقم مباشر غير مثبت", "email": "", "website": "https://www.dma-mea.com/", "rel_source": "https://atriumeg.com/portfolio/privado-compound-madinaty/ | https://atriumeg.com/portfolio/madinaty-v24-villas/", "phone_source": "https://www.dma-mea.com/", "evidence_level": "A", "confidence": "مرتفعة لذكر الاسم؛ متوسطة لتطابق الكيان", "notes": "لا توحّد الأسماء القانونية المختلفة قبل المطابقة"}, {"id": 21, "name": "PME Consultancy", "role": "استشاري إدارة مشروعات\nإدارة مشروع لمراحل 1–5 الرحاب لمصلحة ACC", "project": "الرحاب", "relation": "صفحة مشروع تاريخية من الاستشاري نفسه", "phone": "القاهرة: +20 122 440 8816 | الإسكندرية: +20 3 592 3291", "phone_notes": "مكتبا القاهرة والإسكندرية", "email": "info@pme-consultancy.com", "website": "https://pme-consultancy.com/", "rel_source": "https://pme-consultancy.com/2022/06/02/el-rehab-city-project/", "phone_source": "https://pme-consultancy.com/contact/", "evidence_level": "B", "confidence": "مرتفعة للعلاقة التاريخية", "notes": "لم تنشر الصفحة أي مديونية أو نزاع"}, {"id": 22, "name": "Mimar Interiors", "role": "مصمم داخلي/استشاري محتمل\nمذكور في منشور Knauf بشأن Four Seasons Luxor\nذكر في منشور Knauf عن Four Seasons Luxor", "project": "الأقصر", "relation": "ذكر في سياق منشور شركة مورد؛ تفاصيل دوره التعاقدي غير كاملة\nصلة من منشور مورد؛ لا تتوفر وثيقة نطاق أو عقد", "phone": "+20 2 2539 0163", "phone_notes": "خط مكتب Mimar Group بالقاهرة؛ لا يوجد رقم منفصل واضح لـMimar Interiors", "email": "projects@mimarinteriors.com", "website": "https://eg.erp-mimar-group.com/contactus", "rel_source": "https://www.linkedin.com/company/knauf-egypt/", "phone_source": "https://eg.erp-mimar-group.com/contactus", "evidence_level": "B", "confidence": "متوسطة", "notes": "لا وثيقة عقد أو نطاق عمل كامل منشور\nلم يتأكد هل هي استشاري أم مقاول تشطيبات أو طرف آخر بهذا المشروع\nرقم المجموعة لا يثبت وجود خط هاتفي مستقل لقسم التصميم الداخلي."}, {"id": 23, "name": "Interserve Consulting Group", "role": "خيط بحث استشاري – غير مؤكد\nاسم في ملف/مستند مشروع Four Seasons Cairo Capital CP03", "project": "مدينتي", "relation": "ظهور في مستند مشروع؛ لم يثبت تعاقده المباشر مع TMG", "phone": "غير منشور/لم يُعثر على رقم موثوق", "phone_notes": "هوية الكيان ودوره التعاقدي لم يتأكدا", "email": "", "website": "", "rel_source": "https://endelegypt.com/data/pdf/Endel_profile%2025_9_2023.pdf", "phone_source": "", "evidence_level": "C/D", "confidence": "منخفضة", "notes": "لا تصنفه كمقاول أو استشاري مؤكد دون خطاب تعيين/عقد\nاسم وارد في مستند مرتبط بحزمة مشروع؛ لا توجد مطابقة مؤكدة لهوية الشركة أو جهة اتصالها."}, {"id": 24, "name": "IEC Consultants", "role": "خيط بحث استشاري – غير مؤكد\nاسم في مستندات مرتبطة بـFour Seasons Cairo Capital CP03", "project": "مدينتي", "relation": "ذكر مستندي فقط", "phone": "مرشح فقط: +20 2 2639 4960 / +20 122 002 0213", "phone_notes": "رقم شركة International Engineering Company (IEC)؛ مطابقة الاسم القانوني مع الكيان الوارد في مستند المشروع غير محسومة", "email": "info@iec.com.eg", "website": "https://www.iec.com.eg/", "rel_source": "https://endelegypt.com/data/pdf/Endel_profile%2025_9_2023.pdf", "phone_source": "https://www.iec.com.eg/pages/contact.html", "evidence_level": "C/D", "confidence": "منخفضة", "notes": "الاختصار مبهم وقد يعود لكيانات متعددة\nتأكد من رقم السجل/الاسم القانوني قبل التعامل على أساس أن هذا هو IEC الوارد بمستند المشروع."}, {"id": 25, "name": "ENDEL Egypt", "role": "شركة – الدور غير مثبت\nملف/مستند يتعلق بحزمة Four Seasons Cairo Capital CP03", "project": "مدينتي", "relation": "ظهور في ملف الشركة/وثائق المشروع؛ نطاق التعاقد غير مثبت", "phone": "لم يُعثر على رقم حديث منشور في صفحة الاتصال الرسمية", "phone_notes": "صفحة الشركة تنشر البريد الإلكتروني دون رقم هاتف واضح", "email": "info@endelegypt.com", "website": "https://endelegypt.com/", "rel_source": "https://endelegypt.com/data/pdf/Endel_profile%2025_9_2023.pdf", "phone_source": "https://endelegypt.com/contactus.aspx", "evidence_level": "C/D", "confidence": "منخفضة", "notes": "لا تُصنف كمقاول باطن مؤكد من هذا المصدر فقط"}, {"id": 26, "name": "Jotun", "role": "علامة/مورد محتمل\nاسم Delivery Note في نموذج استلام مواد Four Seasons Cairo Capital", "project": "مدينتي", "relation": "المستند يذكر إشعار تسليم؛ لا يثبت العقد أو المشتري النهائي", "phone": "لا يظهر رقم مباشر عام لمكتب Jotun مصر في صفحة الاتصال الحالية", "phone_notes": "استخدم نموذج التواصل الرسمي أو دليل الموزعين/المطبقين المعتمدين", "email": "", "website": "https://www.jotun.com/eg-en/contact-us", "rel_source": "https://www.scribd.com/document/928303864/MIR-11", "phone_source": "https://www.jotun.com/eg-en/contact-us", "evidence_level": "C/D", "confidence": "منخفضة-متوسطة", "notes": "يلزم أمر شراء/اعتماد مادة يربطها بالحزمة بوضوح"}, {"id": 27, "name": "Bauer Egypt", "role": "مقاول أساسات محتمل – خيط منخفض الثقة\nملف مهني فردي يربطه بأعمال أساسات مقر TMG الجديد", "project": "المقر الجديد – القاهرة", "relation": "ملف مهني فقط؛ لم يظهر عقد أو إعلان رسمي يؤكد العلاقة", "phone": "لم يُعثر على رقم فرع مصر موثوق", "phone_notes": "علاقة المشروع نفسها منخفضة الثقة؛ لا توجد مطابقة مؤكدة لفرع محلي", "email": "", "website": "https://www.bauer.de/", "rel_source": "https://ae.linkedin.com/in/mohamed-gamal-594929168", "phone_source": "", "evidence_level": "D", "confidence": "منخفضة", "notes": "ليست علاقة مؤكدة ولا دليل على مستحقات\nالاسم وارد كخيط بحث مهني فقط وليس عقدًا أو إعلانًا رسميًا لمشروع TMG."}, {"id": 28, "name": "Power Axes Piling & Foundation LLC", "role": "مقاول أساسات محتمل – خيط منخفض الثقة\nذكر مهني ضمن سياق مشروع مقر TMG الجديد", "project": "المقر الجديد – القاهرة", "relation": "ملف مهني فقط؛ التسلسل التعاقدي غير مثبت", "phone": "+20 10 1691 0698 / +20 10 2210 5385", "phone_notes": "فرع مصر — الشروق / القاهرة الجديدة", "email": "info@poweraxes.com", "website": "https://poweraxes.com/", "rel_source": "https://ae.linkedin.com/in/mohamed-gamal-594929168", "phone_source": "https://poweraxes.com/contact.html", "evidence_level": "D", "confidence": "منخفضة", "notes": "يلزم أمر إسناد أو عقد أصلي قبل تصنيفها كمقاول\nرقم الشركة موثق، لكن اشتراكها في أعمال مقر TMG الجديد ما زال خيطًا منخفض الثقة غير مؤكد بعقد."}, {"id": 29, "name": "GEMS Egypt for Education Services", "role": "عميل/جهة مالكة للمشروع لا مورد\nصاحبة مشروع GEMS School بالرحاب حسب صفحة Atrium", "project": "الرحاب", "relation": "جهة مشروع؛ لا تعتبر موردًا لـTMG لمجرد وجودها بالمشروع", "phone": "الاستقبال: +20 2 2607 0291 / 0292 / 0294 / 0295 | القبول: +20 10 5038 5588 / +20 10 6003 9353", "phone_notes": "مدرسة GEMS British School Al Rehab — جهة تشغيل/تعليم بالمشروع وليست مقاولًا", "email": "registrar_tbs@gemsedu.com", "website": "https://www.tbs-cairo.com/", "rel_source": "https://atriumeg.com/portfolio/gems-school-at-rehab-city/", "phone_source": "https://www.tbs-cairo.com/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "يجب فصل العميل عن المقاول والمورد في قاعدة بيانات الأطراف"}, {"id": 30, "name": "First Design for Urban Investment and Development SAE", "role": "طرف تطوير/أرض محتمل وليس مقاولًا مثبتًا\nذكر في تقرير حضري بسياق بيع أرض/تطوير مشترك في Madinaty", "project": "مدينتي", "relation": "علاقة تطوير/أرض من مصدر ثانوي", "phone": "لم يُعثر على رقم رسمي موثوق", "phone_notes": "الكيان مذكور في مصدر ثانوي بسياق أرض/تطوير؛ لا يوجد خط اتصال موثق", "email": "", "website": "", "rel_source": "https://marsadomran.info/en/2022/09/2777/", "phone_source": "", "evidence_level": "C", "confidence": "منخفضة-متوسطة", "notes": "لا تدرج كمقاول أو مورد دون عقد إنشاء مستقل\nالعلاقة ليست عقد مقاولات مثبتًا؛ لا ينبغي إدراجه كمقاول أو مورد دون مستند إضافي."}, {"id": 31, "name": "Thabat", "role": "شريك إقليمي لـAtrium\nشراكة مع Atrium في السعودية بحسب موقع Atrium", "project": "السعودية", "relation": "شراكة مؤسسية؛ ليست موردًا مصريًا مؤكدًا", "phone": "لم يُعثر على رقم موثوق ضمن المصادر المستخدمة", "phone_notes": "شريك Atrium في السعودية وفق موقع Atrium؛ لم يثبت ارتباطه بمشروع مصري محدد", "email": "", "website": "https://atriumeg.com/", "rel_source": "https://atriumeg.com/", "phone_source": "", "evidence_level": "B", "confidence": "متوسطة", "notes": "إدراج للتعرّف على الشبكة لا لإثبات علاقة بمشروع مصري\nمدرج للشفافية فقط؛ خارج نطاق قائمة الموردين المحليين المصرية ما لم يظهر مشروع مصري مباشر."}, {"id": 32, "name": "Emileo Interiors", "role": "شركة مرتبطة بـAtrium/استحواذ معلن\nتصميم داخلي وتشطيبات حسب موقع Atrium", "project": "المشروعات غير المحددة", "relation": "صلة مؤسسية معلنة؛ لم يتحدد مشروع بعينه", "phone": "للتواصل الأولي عبر Atrium: +20 2 2693 1643 / 1647 / 1648", "phone_notes": "رقم مكتب Atrium العام؛ لم يُعثر على رقم مستقل موثوق لـEmileo Interiors", "email": "", "website": "https://atriumeg.com/", "rel_source": "https://atriumeg.com/", "phone_source": "https://atriumeg.com/contact/", "evidence_level": "B", "confidence": "متوسطة للصلة العامة", "notes": "لا ينسب إليها عقد محدد أو مطالبة دون مصدر خاص بالمشروع\nالموقع يعرض Emileo Interiors ضمن العلامات المرتبطة، لكن لم تُطابق علاقة مشروع محدد أو رقم مستقل."}, {"id": 33, "name": "MCBS – Modern Construction of Building Systems", "role": "كيان ضمن شبكة TMG؛ MEP/تيار خفيف/تشغيل\nأعمال خدمات فنية وصيانة للمنشآت والمراكز التجارية والفنادق", "project": "مرافق ومشروعات المجموعة", "relation": "يصف نفسه بأنه عضو بمجموعة TMG؛ ليست كل العقود منشورة", "phone": "غير منشور علنًا في المصادر التي تمت مراجعتها", "phone_notes": "شركة متخصصة بمجموعة TMG؛ يلزم طلب رقم إدارة الشركة من المجموعة", "email": "", "website": "https://eg.linkedin.com/company/mcbs-member-of-talaat-moustafa-group", "rel_source": "https://www.linkedin.com/company/mcbs-member-of-talaat-moustafa-group", "phone_source": "https://eg.linkedin.com/company/mcbs-member-of-talaat-moustafa-group", "evidence_level": "B", "confidence": "متوسطة-مرتفعة", "notes": "قائمة الملكية والقيمة والمشروعات تحتاج إفصاحًا أو سجلات داخلية\nلا أضع رقم TMG على أنه رقم مباشر لـMCBS؛ رقم المجموعة العام موجود بصف TMG مستقل."}, {"id": 34, "name": "Orion Facilities Management & Services", "role": "شركة مجموعة لإدارة المرافق\nإدارة مرافق وصيانة وخدمات عقارية", "project": "مدينتي ومشروعات المجموعة؛ The Spine", "relation": "شركة تابعة/مرتبطة بالمجموعة حسب المصادر الرسمية/ملف الشركة", "phone": "16286 | واتساب: +20 110 101 6286", "phone_notes": "خط حجز/استفسارات الخدمات — يشمل مدينتي والرحاب", "email": "", "website": "https://orion-eg.com/", "rel_source": "https://talaatmoustafa.com/upload/TMG%20Conso%20%20FS%2031%20December%202024-English.pdf | https://eg.linkedin.com/company/orionfms", "phone_source": "https://orion-eg.com/", "evidence_level": "A/B", "confidence": "مرتفعة للصلة العامة", "notes": "لا توجد قائمة موحدة للعقود أو أوامر العمل"}, {"id": 35, "name": "APUD – Arab Company for Projects and Urban Development", "role": "شركة مجموعة – مالك/مطور\nجهة مالكة لعدة مشروعات Atrium في مدينتي والرحاب", "project": "مدينتي؛ الرحاب", "relation": "كيان من مجموعة TMG؛ دوره غالبًا مالك/مطور وليس موردًا", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا لـAPUD", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/ar/investor-relations-ar/ | https://pme-consultancy.com/2022/06/02/el-rehab-city-project/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "يجب استخدام الكيان القانوني الدقيق في المطالبة والعقد\nالشركة جهة مالكة/مطور في مشاريع؛ الرقم المباشر للكيان لم يُتحقق منه."}, {"id": 36, "name": "Arab Company for Urban Investment", "role": "شركة مجموعة – جهة مالكة/استثمارية\nالجهة المالكة لمشروع 72 مبنى سكنيًا في Noor City على صفحة Atrium", "project": "نور", "relation": "اسم منفصل عن APUD بحسب مصدر المشروع", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://atriumeg.com/portfolio/72-residential-buildings-at-noor-city/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "لا تدمجها مع APUD دون مستند قانوني"}, {"id": 37, "name": "Nova Park Cairo", "role": "شركة تابعة/كيان مالك فندقي\nجهة مالكة/صاحب مشروع Four Seasons Nile Plaza على صفحة Atrium", "project": "القاهرة", "relation": "شركة ضمن سلسلة شركات TMG حسب القوائم 2025", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/upload/Consolidated%20financial%20statements%20for%20the%20year%20ended%2031-12-2025-English.pdf | https://atriumeg.com/portfolio/four-seasons-hotel-cairo-at-nile-plaza/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "ليست مقاولًا؛ تحدد كيان المشروع"}, {"id": 38, "name": "Egyptian Company for Development and Real Estate Projects", "role": "شركة تابعة/كيان مشروع\nجهة مالكة Four Seasons Sharm El Sheikh", "project": "شرم الشيخ", "relation": "شركة ضمن المجموعة بحسب القوائم 2025؛ جهة مشروع على صفحة Atrium", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/upload/Consolidated%20financial%20statements%20for%20the%20year%20ended%2031-12-2025-English.pdf | https://atriumeg.com/portfolio/four-seasons-resort-sharm-el-sheikh/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "قيمة الحزمة ليست مبلغ دين أو كامل قيمة الأصل"}, {"id": 39, "name": "San Stefano Company for Touristic Investment", "role": "شركة تابعة/كيان فندقي\nجهة مشروع Four Seasons San Stefano في صفحة Atrium", "project": "الإسكندرية", "relation": "صلة ملكية/مشروع ضمن سلسلة TMG الفندقية", "phone": "رقم المجموعة للتوجيه: +20 2 3331 2000 | الخط الساخن: 19691", "phone_notes": "أرقام TMG المركزية وليست رقمًا مباشرًا مستقلًا مثبتًا للكيان", "email": "TMGH@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/upload/Consolidated%20financial%20statements%20for%20the%20year%20ended%2031-12-2025-English.pdf | https://atriumeg.com/portfolio/four-seasons-hotel-san-stefano-grand-plaza/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "يجب فصلها عن San Stefano Real Estate Investment قانونيًا"}, {"id": 40, "name": "TMG Holding (Talaat Moustafa Group)", "role": "المطور/المالك الرئيسي\nالمطور الرئيسي ومجموعة الكيانات المالكة للمشروعات", "project": "مدينتي؛ الرحاب؛ SouthMED؛ نور؛ سيليا؛ الفنادق", "relation": "علاقة مباشرة كمالك/مطور؛ رقم التواصل هنا للخط العام للمجموعة", "phone": "الخط الساخن: 19691 | المقر: +20 2 3331 2000 / +20 2 3301 6701", "phone_notes": "الخط العام للمجموعة / المقر الرئيسي بالدقي", "email": "TMGH@tmg.com.eg | ir@tmg.com.eg", "website": "https://talaatmoustafa.com/", "rel_source": "https://talaatmoustafa.com/contact-us/ | https://talaatmoustafa.com/investor-relations/", "phone_source": "https://talaatmoustafa.com/contact-us/", "evidence_level": "A", "confidence": "مرتفعة", "notes": "استخدم رقم المجموعة للتوجيه فقط؛ لا يعني أن كل مقاول أو مورد لديه عقد مباشر مع TMG."}, {"id": 41, "name": "ACE Moharram Bakhoum", "role": "استشاري هندسي / تصميم وإشراف\nمذكور كاستشاري مشروع في بعض المشروعات الظاهرة بمحفظة SQUARE المرتبطة بجهات تطوير TMG؛ نطاق كل مشروع يحتاج مراجعة صفحة المشروع", "project": "مشروعات SQUARE المرتبطة بـAPUD/Arab Company for Urban Investment؛ مطابقة كل حزمة تحتاج تحققًا", "relation": "استشاري مرشح بعلاقة مشروعية غير مباشرة؛ لا يُفترض تعاقد مباشر مع TMG", "phone": "+20 2 3761 1576 (تحويلة 3930)", "phone_notes": "رقم الشركة العام المنشور على صفحة LinkedIn", "email": "admin.ace@ace-mb.com", "website": "https://ace-mb.com/", "rel_source": "https://www.square.com.eg/ | https://www.linkedin.com/company/ace-moharram-bakhoum", "phone_source": "https://www.linkedin.com/company/ace-moharram-bakhoum", "evidence_level": "B", "confidence": "متوسطة", "notes": "صفحة SQUARE تذكر ACE ضمن project consultant لبعض المشروعات؛ يلزم تحديد المشروع/الحزمة قبل اعتباره طرفًا مباشرًا."}, {"id": 42, "name": "Atrium Project Management (APM)", "role": "إدارة مشروعات / استشاري مرتبط بمجموعة Atrium\nذراع/شركة مرتبطة بـAtrium لإدارة المشروعات؛ لا يوجد في المصادر المستخدمة تعيين مؤكد على حزمة مصرية بعينها", "project": "صلة مؤسسية بمجموعة Atrium؛ المشروع المحدد غير مؤكد", "relation": "شركة مرتبطة مؤسسيًا؛ إدراج استكشافي وليس إثبات عقد مشروع محدد", "phone": "+20 2 2693 1643 / 1647 / 1648 (قناة Atrium العامة؛ ليست رقمًا منفصلًا مؤكدًا لـAPM)", "phone_notes": "رقم مجموعة Atrium بمباني الرحاب؛ قناة إحالة فقط", "email": "", "website": "https://www.apmeg.cloud/contact.html", "rel_source": "https://atriumeg.com/ | https://www.apmeg.cloud/contact.html", "phone_source": "https://www.apmeg.cloud/contact.html", "evidence_level": "B/C", "confidence": "متوسطة للصلة المؤسسية؛ منخفضة لتعيين مشروع بعينه", "notes": "رقم Atrium المنشور يصلح كقناة استفسار أولية فقط؛ لم يظهر رقم/عقد منفصل لكل مشروع."}];
    const TMG_TEAMS = [{"id": 1, "project": "SouthMED", "company": "Concrete Plus", "name": "Ahmed Ayman", "role": "Interior Project Manager", "linkedin": "https://eg.linkedin.com/in/ahmed-ayman-5056541a3", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/ahmed-ayman-5056541a3", "notes": "الملف مرتبط بـConcrete Plus؛ لا يثبت وحده تعيينه في SouthMED تحديدًا."}, {"id": 2, "project": "مشروعات Concrete Plus في مصر/السعودية", "company": "Concrete Plus", "name": "Ahmed Khashaba, PMP®, PMI-RMP®, PMI-SP®", "role": "المنصب الحالي الدقيق غير ظاهر في المقتطف العام؛ ملف مهني لدى Concrete Plus", "linkedin": "https://eg.linkedin.com/in/ahmedkhashaba", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/ahmedkhashaba", "notes": "الملف يعرض خبرة لدى Concrete Plus ومواقع متعددة، لكنه لا يربطه صراحةً بحزمة SouthMED."}, {"id": 3, "project": "مشروعات Concrete Plus", "company": "Concrete Plus", "name": "Ayman Tantawy", "role": "دور هندسي/تنفيذي؛ المسمى الحالي غير مؤكد بالمقتطف", "linkedin": "https://eg.linkedin.com/in/ayman-tantawy-853958103", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/ayman-tantawy-853958103", "notes": "الملف يذكر Concrete Plus وخبرة في تنفيذ أنشطة المشاريع؛ المشروع المحدد غير مؤكد."}, {"id": 4, "project": "مشروعات Concrete Plus", "company": "Concrete Plus", "name": "Kareem Eldsoky, PMP®, PE®", "role": "المسمى الحالي الدقيق غير ظاهر في المقتطف العام", "linkedin": "https://eg.linkedin.com/in/kareem-eldsoky", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/kareem-eldsoky", "notes": "خبرة منشورة لدى Concrete Plus، ومواقع مصرية متعددة؛ ليس تأكيدًا على SouthMED."}, {"id": 5, "project": "مشروعات Concrete Plus", "company": "Concrete Plus", "name": "Fady Mahfouz Youssef", "role": "Senior Electromechanical Commercial & Tendering Manager", "linkedin": "https://eg.linkedin.com/in/fady-mahfouz-youssef-642484a0", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/fady-mahfouz-youssef-642484a0", "notes": "ملف مهني يذكر Concrete Plus؛ لا يثبت تكليفه بمشروع TMG بعينه."}, {"id": 6, "project": "Four Seasons Cairo Capital / Madinaty", "company": "Atrium Quality Contractors", "name": "Ahmed Assaf", "role": "المسمى الوظيفي الحالي غير مؤكد بالمقتطف العام", "linkedin": "https://eg.linkedin.com/in/ahmed-assaf-ba10a9161", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/ahmed-assaf-ba10a9161", "notes": "الملف مرتبط بـAtrium وتوجد منشورات حول وظائف ومشروعات الشركة؛ المشروع المحدد غير محسوم."}, {"id": 7, "project": "مشروعات Atrium / وظائف مشروع بالقاهرة", "company": "Atrium Quality Contractors", "name": "Ahmed El Sobky", "role": "دور مهني لدى Atrium؛ المسمى الحالي غير ظاهر بالمقتطف", "linkedin": "https://eg.linkedin.com/in/ahmed-el-sobky-49841910b", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/ahmed-el-sobky-49841910b", "notes": "الملف مرتبط بـAtrium، لكن مقتطف الصفحة لا يقدم تعيينًا محددًا على مشروع TMG."}, {"id": 8, "project": "مشروعات Atrium", "company": "Atrium Quality Contractors", "name": "Mostafa Abdelatty", "role": "المسمى الوظيفي الحالي غير مؤكد؛ منشورات توظيف مرتبطة بالـQS", "linkedin": "https://eg.linkedin.com/in/mostafa-abdelatty-9a8726bb", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mostafa-abdelatty-9a8726bb", "notes": "يظهر بريد عمل منشور mostafa.abdelatty@atriumeg.com في منشور توظيف عام؛ لا يوجد رقم هاتف شخصي منشور."}, {"id": 9, "project": "Four Seasons Luxor", "company": "Atrium Quality Contractors", "name": "Amr A.", "role": "Civil Engineer؛ خبرة/مشروعات منشورة في Four Seasons Luxor", "linkedin": "https://eg.linkedin.com/in/amr-a-9525a4145", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/amr-a-9525a4145", "notes": "الملف يذكر خبرة Atrium ومشروعات Four Seasons Luxor؛ الاسم مختصر كما يعرضه LinkedIn."}, {"id": 10, "project": "FS Madinaty Villas وFS Luxor", "company": "Atrium Quality Contractors", "name": "Anas Reda, PMP®", "role": "المسمى الحالي التفصيلي غير ظاهر؛ ملف مرتبط بـAtrium", "linkedin": "https://eg.linkedin.com/in/anasreda1993", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/anasreda1993", "notes": "نشاطه العام يربط إعلانات QC بمشروعات FS Madinaty Villas وFS Luxor؛ لا يلزم أنه مدير المشروع."}, {"id": 11, "project": "The Strip Project / Madinaty", "company": "Atrium Quality Contractors", "name": "Abdelrahman Saeed", "role": "المسمى الحالي غير ظاهر بالمقتطف؛ ملف مرتبط بـAtrium", "linkedin": "https://eg.linkedin.com/in/عبدالرحمن-سعيد-8ba606237", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/عبدالرحمن-سعيد-8ba606237", "notes": "الملف/منشور Atrium يذكر اكتمال مرحلة من The Strip؛ يجب التحقق من رابط الملف المباشر على LinkedIn."}, {"id": 12, "project": "All Seasons Park Mall / Madinaty", "company": "Atrium Quality Contractors", "name": "Mahmoud El Najjar", "role": "Site Section Head Engineer", "linkedin": "https://eg.linkedin.com/in/mahmoud-el-najjar-3009b8a5", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mahmoud-el-najjar-3009b8a5", "notes": "الملف يذكر دور Site Section Head Engineer بمشاريع All Seasons Park Mall وGEMS American School Al-Rehab وGateway Mall."}, {"id": 13, "project": "Privado / Madinaty", "company": "Atrium Quality Contractors", "name": "Youssef Sameh", "role": "Planner Engineer", "linkedin": "https://eg.linkedin.com/in/youssef-sameh-a85716327", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/youssef-sameh-a85716327", "notes": "الملف يذكر Planner Engineer وخبرة Atrium في Privado, Madinaty؛ رابط ملف عام."}, {"id": 14, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Mahmoud Abd Elaal", "role": "الصفة الدقيقة غير واضحة بالمقتطف؛ ملف لدى CCC ويعرض حزمة MEP CP02", "linkedin": "https://eg.linkedin.com/in/mahmoud-abd-elaal-5a6a2380", "phone": "غير منشور", "evidence_level": "A/B", "source": "https://eg.linkedin.com/in/mahmoud-abd-elaal-5a6a2380", "notes": "يذكر صراحة العميل TMG، المقاول الرئيسي Atrium، مدير المشروع Hill International، والاستشاري Shaker Consultancy Group."}, {"id": 15, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Khaled Hesham", "role": "الصفة الحالية غير مؤكدة؛ ملف لدى CCC ومشاركات بشأن المشروع", "linkedin": "https://eg.linkedin.com/in/khaled-hesham-3555204", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/khaled-hesham-3555204", "notes": "شارك منشور JV عن حزمة MEP CP02. لا يُستنتج دور قيادي بالمشروع دون دليل إضافي."}, {"id": 16, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Sameh El Naggar", "role": "الصفة الحالية غير مؤكدة؛ ملف لدى CCC ومشاركات بشأن المشروع", "linkedin": "https://eg.linkedin.com/in/sameh-el-naggar-5b5a07161", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/sameh-el-naggar-5b5a07161", "notes": "شارك منشور JV عن الحزمة؛ المسمى والمهمة المحددان غير منشورين في المقتطف."}, {"id": 17, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium-CCCE JV", "name": "Mohyeeldin Kotb", "role": "Cost Control Engineer", "linkedin": "https://eg.linkedin.com/in/mohyeeldin-kotb", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mohyeeldin-kotb", "notes": "يذكر الانتقال إلى وظيفة Cost Control Engineer في JV Atrium–CCC بمشروع Four Seasons Luxor."}, {"id": 18, "project": "Four Seasons Luxor — MEP Package CP02", "company": "Atrium / CCCE JV", "name": "Mohamed Yasser", "role": "متدرب/مهندس في مرحلة مبكرة؛ المسمى التفصيلي غير واضح", "linkedin": "https://eg.linkedin.com/in/mohamed-yasser-aa7711381", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/mohamed-yasser-aa7711381", "notes": "منشور LinkedIn يقول إنه ساهم في مشروع Four Seasons Luxor ضمن فريق Atrium؛ المسمى الحالي غير متحقق."}, {"id": 19, "project": "Four Seasons Luxor", "company": "Atrium Quality Contractors", "name": "Samer Gobran", "role": "شركة حالية: ELEVATE Construction Company؛ ناشر تحديث مشروع، لا دليل على توظيفه لدى TMG", "linkedin": "https://eg.linkedin.com/in/samer-gobran-a063bb7", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/samer-gobran-a063bb7", "notes": "منشور يصف المالك TMG، الاستشاري Shaker، المقاول Atrium وJV للأعمال الكهروميكانيكية. لا نعدّه عضوًا في فريق TMG."}, {"id": 20, "project": "Four Seasons Luxor", "company": "استشاري المشروع / Hill International", "name": "Mohamed Karam", "role": "المسمى الحالي SODIC؛ ملفه يسرد خبرة مرتبطة بـFour Seasons Luxor", "linkedin": "https://eg.linkedin.com/in/mohamed-karam-eng", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/mohamed-karam-eng", "notes": "الملف يسرد المشروع والجهات Hill وShaker وIETC؛ لا يثبت أن الشخص موظف حاليًا لدى تلك الجهات."}, {"id": 21, "project": "Noor City / New Gardens Capital", "company": "Atrium Project Management (APM)", "name": "Mohammed Ali, MBA®, PMP®", "role": "دور في إدارة/تخطيط الإنشاءات؛ المسمى الدقيق غير ظاهر في مقتطف الصفحة", "linkedin": "https://eg.linkedin.com/in/mohammed-ali88", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/mohammed-ali88", "notes": "الملف يتضمن مشروعات Noor City، العميل TMG وحزم المباني والبنية التحتية."}, {"id": 22, "project": "Noor City / New Gardens Capital", "company": "Atrium Project Management (APM)", "name": "Sherif Nabil, PRMG", "role": "Project/Development Management؛ المسمى الحالي الدقيق يحتاج مراجعة الملف", "linkedin": "https://eg.linkedin.com/in/sherif-shaker-mba-prmg-aace-bsc-of-civil-eng-01a27641/ar", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/sherif-shaker-mba-prmg-aace-bsc-of-civil-eng-01a27641/ar", "notes": "صفحة LinkedIn تعرض Noor City ومشروعات تطوير أخرى بأدوار إدارة/تطوير."}, {"id": 23, "project": "Noor City", "company": "Atrium Project Management (APM)", "name": "Mahmoud Solyman", "role": "Civil Engineer؛ ملف مرتبط بـAPM وNoor City", "linkedin": "https://eg.linkedin.com/in/m-solyman", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/m-solyman", "notes": "الملف يذكر APM | TMG وخبرة في Noor City؛ المسمى المحدد الحالي ليس ظاهرًا بالمقتطف."}, {"id": 24, "project": "Noor City", "company": "Atrium Project Management (APM)", "name": "Alaa Badr", "role": "المسمى الوظيفي غير ظاهر بالمقتطف العام", "linkedin": "https://eg.linkedin.com/in/alaa-badr-b3a22819a", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/alaa-badr-b3a22819a", "notes": "الملف مرتبط بـAPM وNoor City; لا يوجد توصيف أكثر دقة في المقتطف العام."}, {"id": 25, "project": "Madinaty Central Park Extension / Madinaty Club Phase 2 / Madinaty Waterpark / Noor Smart City", "company": "TMG Developments", "name": "Haytham Ahmed Kadry", "role": "Project Manager؛ يذكر هذه المشاريع في خبرته", "linkedin": "https://eg.linkedin.com/in/haytham-kadry-project-manager", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/haytham-kadry-project-manager", "notes": "صفحة LinkedIn تذكر PM في التوسعات التجارية والإدارية والنوادي والـWaterpark وNour Smart City."}, {"id": 26, "project": "Water Park – Atrium / Madinaty", "company": "Atrium Quality Contractors", "name": "Fadel Mosaad", "role": "Mechanical Commercial Engineer؛ عمل في تقدير تكاليف MEP ومراجعة العطاءات والمستخلصات بالمشروع", "linkedin": "https://eg.linkedin.com/in/fadel-mosaad", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/fadel-mosaad", "notes": "الملف يحدد مشروع Water Park–Atrium (TMG) من يناير 2026، مع وصف لنطاق العمل."}, {"id": 27, "project": "Madinaty / Noor City", "company": "MCBS — Member of TMG", "name": "Farid Emile", "role": "MEP Operations Manager", "linkedin": "https://eg.linkedin.com/in/farid-emile", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/farid-emile", "notes": "الملف يذكر MCBS ومهام تشغيل مشروعات الشركة؛ المشروعات المحددة غير ظاهرة في المقتطف."}, {"id": 28, "project": "مشروعات MCBS / TMG", "company": "MCBS — Member of TMG", "name": "Adel Yassin, PMP®", "role": "Electromechanical Engineer؛ خبرة في المجال الكهربائي/الميكانيكي", "linkedin": "https://eg.linkedin.com/in/adel-yassin-pmp-%C2%AE-b0b13a208", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/adel-yassin-pmp-%C2%AE-b0b13a208", "notes": "ملف مرتبط بـMCBS، لكن المشروع المحدد غير مؤكد."}, {"id": 29, "project": "مدينتي ومرافق TMG", "company": "Orion Facilities Management — TMG", "name": "Tamer Ahmed", "role": "Senior Facilities Management Director", "linkedin": "https://eg.linkedin.com/in/tamerabdulaziz", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/tamerabdulaziz", "notes": "الملف يذكر Orion Facilities Management - TMG؛ لا يحدد مشروعًا منفردًا."}, {"id": 30, "project": "Atrium / TMG — قيادة الشركة", "company": "Atrium Quality Contractors / APM", "name": "Hagar Sabry, PRMG, MBA", "role": "المسمى الشخصي يحتاج تحققًا؛ المصدر يذكر قيادة APM/Atrium لشخص آخر في نص مقتطف مختلط", "linkedin": "https://eg.linkedin.com/in/hagar-sabry-prmg-mba-7bb7a9133", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/hagar-sabry-prmg-mba-7bb7a9133", "notes": "تم استبعاد أي استنتاج عن منصب CEO لأن المقتطف يخلط بوضوح أسماء/نبذات مختلفة. أُدرج كرابط للتحقق فقط."}, {"id": 31, "project": "Four Seasons Cairo Capital", "company": "Atrium Quality Contractors", "name": "Ali Elkady", "role": "مهندس؛ المسمى الدقيق غير ظاهر بالمقتطف", "linkedin": "https://eg.linkedin.com/in/ali-elkady-878784172", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/ali-elkady-878784172", "notes": "ملف مرتبط بـAtrium ومواقع متعددة؛ لا دليل كافٍ لربطه مباشرة بحزمة Four Seasons Cairo Capital."}, {"id": 32, "project": "Atrium / مشروعات متعددة", "company": "Atrium Quality Contractors", "name": "Mahmoud Elbakry", "role": "المسمى الوظيفي غير ظاهر بالمقتطف؛ يذكر مشروعات 2026", "linkedin": "https://eg.linkedin.com/in/mahmoudelbakry", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/mahmoudelbakry", "notes": "الملف يذكر Gate 3 Madinaty وRehab Hills Mall؛ ملكية Rehab Hills Mall بالصفحة تعود لجهة أخرى، لذا يلزم فصل المشروع عن حافظة TMG وعدم اعتباره تلقائيًا مشروع TMG."}, {"id": 33, "project": "مشروعات Atrium / Madinaty", "company": "Atrium Quality Contractors", "name": "Bassel Nabil, PMP®, CCP", "role": "Senior Cost Control Engineer", "linkedin": "https://eg.linkedin.com/in/bassel-nabil-ali", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/bassel-nabil-ali", "notes": "الملف يعرض خبرة في Atrium بمدينتي والقاهرة والعاصمة الإدارية؛ لا يحدد حزمة TMG واحدة في المقتطف."}, {"id": 34, "project": "مشروعات Atrium / أدوار QS والتجاري", "company": "Atrium Quality Contractors", "name": "Fadel Mosaad", "role": "Mechanical Commercial Engineer", "linkedin": "https://eg.linkedin.com/in/fadel-mosaad", "phone": "غير منشور", "evidence_level": "B", "source": "https://eg.linkedin.com/in/fadel-mosaad", "notes": "الملف يذكر مشروع Water Park – Atrium (TMG) خلال يناير 2026، مع مسؤوليات تقدير أعمال MEP والعطاءات والمستخلصات."}, {"id": 35, "project": "مشروعات Atrium / التوظيف الفني", "company": "Atrium Quality Contractors", "name": "Hoda Hussein", "role": "الدور الحالي غير محدد في المقتطف؛ حساب مرتبط بـAtrium", "linkedin": "https://eg.linkedin.com/in/hoda-hussein-7a98b012a", "phone": "غير منشور", "evidence_level": "C", "source": "https://eg.linkedin.com/in/hoda-hussein-7a98b012a", "notes": "منشورات عامة عن توظيف QS وProcurement وBIM وPlanning؛ ليست دليلًا على تعيينها في مشروع محدد."}, {"id": 36, "project": "مشروعات TMG / مدينتي والعاصمة", "company": "TMG Holding", "name": "Amir Elnabawy", "role": "Quantity Surveyor / Technical Office Manager وفق نبذة منشورة؛ وظيفته الدقيقة الحالية تحتاج تحققًا", "linkedin": "https://eg.linkedin.com/in/amir-el-nabawy", "phone": "غير منشور", "evidence_level": "B/C", "source": "https://eg.linkedin.com/in/amir-el-nabawy", "notes": "يذكر الخبرة لدى TMG في Madinaty وNew Capital؛ النبذة تشير إلى QS وTechnical Office Manager وخبرة يبحث لها عن فرصة، لذلك تحقق من الحالة الحالية قبل التواصل."}, {"id": 37, "project": "مشروعات TMG — القيادة المؤسسية", "company": "TMG Holding", "name": "Hesham Talaat Moustafa", "role": "CEO and Managing Director وفق الإفصاحات المؤسسية؛ ملف LinkedIn المطابق غير مؤكد في نتائج البحث", "linkedin": "غير متحقق", "phone": "غير منشور", "evidence_level": "A للمسمى المؤسسي؛ غير متحقق لملف LinkedIn", "source": "https://talaatmoustafa.com/investor-relations/", "notes": "لم يُدرج رابط ملف شخصي غير مؤكد."}, {"id": 38, "project": "مشروعات TMG — القيادة المؤسسية", "company": "TMG Holding", "name": "Tarek Talaat Moustafa", "role": "Chairman وفق الإفصاحات المؤسسية؛ ملف LinkedIn المطابق غير مؤكد", "linkedin": "غير متحقق", "phone": "غير منشور", "evidence_level": "A للمسمى المؤسسي؛ غير متحقق لملف LinkedIn", "source": "https://talaatmoustafa.com/investor-relations/", "notes": "نتائج البحث عن الاسم الأول والشركة لم تُنتج ملفًا يمكن تأكيد هويته."}];
    const TMG_SWOT = {"strengths": [{"id": "S1", "factor": "Dominant Landbank", "details": "Holds Egypt's largest private urban landbank across East Cairo, North Coast, Red Sea, and Gulf region.", "data": "26,722+ Feddans (>112mn sqm BUA); Madinaty (8,000 feddans), Noor (5,000 feddans), SouthMED (5,500 feddans)", "impact": "High Moat", "source": "TMG Investor Relations / Audit FY25"}, {"id": "S2", "factor": "Massive Sales Backlog", "details": "Unprecedented revenue visibility provided by contracted off-plan sales awaiting construction delivery.", "data": "EGP 441.2 Billion backlog (as of Dec 2025); excludes SouthMED gross sales", "impact": "High Visibility", "source": "FY2025 Earnings Release"}, {"id": "S3", "factor": "Strong Headline Financials", "details": "Record-setting revenue and net earnings growth driven by unit deliveries and hospitality consolidation.", "data": "FY25 Revenue EGP 62.5B (+46%), Net Profit EGP 18.2B (+43%); H1 26 Rev EGP 30.19B", "impact": "High Growth", "source": "Audited Financials FY2025 & H1 2026"}, {"id": "S4", "factor": "Hospitality Foreign Currency", "details": "Icon hotel portfolio generates strong USD/EUR cash flows, offering a natural hedge against EGP devaluation.", "data": "Hospitality Revenue EGP 14.9B in FY25 (+30%); 51% acquisition of Legacy Hotels (7 historic state hotels)", "impact": "FX Hedge Moat", "source": "Icon ADQ/ADNEC Filing & FS Notes"}, {"id": "S5", "factor": "Asset-Light Model Pivot", "details": "Shift toward master development partnership agreements that capture development fees without land balance-sheet liabilities.", "data": "SouthMED (~8% master development fee model) & The Spine (24.5% NBE JV plot sale EGP 67.12B)", "impact": "Capital Light", "source": "TMG Market Updates & Cabinet Decrees"}, {"id": "S6", "factor": "Integrated City Model", "details": "Combines residential units with recurring commercial retail leasing, sports clubs, utilities, and transportation.", "data": "Other Recurring Revenue EGP 10.9B (+64% YoY in FY25); Open Air Mall (260k sqm GLA)", "impact": "Resilient Cash", "source": "TMG Operating Segment Reports"}], "weaknesses": [{"id": "W1", "factor": "Cash Conversion Lag", "details": "Operating cash flow trails accounting profit due to heavy cash absorption into properties under development.", "data": "H1 2026 OCF EGP 3.11B vs Consolidated Profit EGP 9.95B (~31% conversion); EGP 18.26B WIP burn", "impact": "Liquidity Risk", "source": "H1 2026 Cash Flow Statement"}, {"id": "W2", "factor": "Off-Balance Sheet Lease Debt", "details": "Extensive use of sale-and-leaseback transactions creates fixed contractual debt-service obligations.", "data": "EGP 43.99 Billion in Financial Lease Notes Payable (June 2026), up from EGP 34.4B in Dec 2025", "impact": "High Leverage", "source": "Consolidated Balance Sheet Note 18"}, {"id": "W3", "factor": "High Interest Cost Environment", "details": "Elevated effective borrowing rates on local debt create substantial annual interest expense.", "data": "Direct Bank Loans EGP 16.5B at 28.6% average effective rate on EGP credit facilities", "impact": "Cost Drag", "source": "Financial Statement Notes H1 2026"}, {"id": "W4", "factor": "Resident & Customer Friction", "details": "Unilateral annual maintenance deficit surcharges and statutory resale transfer fee enforcement cause disputes.", "data": "Annual maintenance difference demands EGP 15k–45k/unit; CPA Art. 15 resale fee challenges", "impact": "Reputational Risk", "source": "CPA Registries & New Cairo Court Logs"}, {"id": "W5", "factor": "Captive EPC & Governance", "details": "Heavy reliance on related-party contractor Alexandria Construction Co. (ACC) and Atrium Quality Contractors.", "data": "ACC holds 8.05% TMGH stake; EGP 1.90B due from related parties in June 2026", "impact": "Governance Risk", "source": "TMG Corporate Governance Report FY25"}, {"id": "W6", "factor": "Long Delivery Horizons", "details": "Mega-projects require 15- to 20-year execution cycles, exposing developer to long-term macro volatility.", "data": "The Spine (2030 first delivery), SouthMED (2029 first delivery), Banan KSA (2029 first delivery)", "impact": "Execution Risk", "source": "IR Masterplan Timelines 2026"}], "opportunities": [{"id": "O1", "factor": "North Coast Tourism Boost", "details": "Transforming North Coast into a year-round international tourist destination via SouthMED.", "data": "$21 Billion projected lifetime project value; >25,000 units sold in initial launch phase", "impact": "High Topline", "source": "Financial Times & TMG Disclosures"}, {"id": "O2", "factor": "Saudi Arabia Expansion", "details": "Expanding master-community model into Riyadh under Saudi National Housing Company (NHC).", "data": "Banan City (10mn sqm landbank, 25k units, SAR 31.4B total projected investment)", "impact": "Regional Growth", "source": "TMG KSA / NHC Partnership Filing"}, {"id": "O3", "factor": "Omani Coastal Development", "details": "Entering Oman's real estate market via partnerships with the Omani Ministry of Housing.", "data": "Jood & Yamal projects (4.9mn sqm landbank, ~14k units, OMR 1.8B projected sales)", "impact": "Market Diversification", "source": "Oman Ministry Protocol May 2025"}, {"id": "O4", "factor": "Sovereign Wealth Partnerships", "details": "Direct equity co-investments with Gulf sovereign wealth funds and Egyptian state banks.", "data": "ADQ/ADNEC $800M investment for 40.5% in ICON; Rawasy EGP 11.9B commercial monetization", "impact": "Capital Inflow", "source": "EGX Disclosures & ADQ Press Releases"}, {"id": "O5", "factor": "Commercial Asset Monetization", "details": "Selling and leasing prime retail spaces in Open Air Mall, East Hub, and Craft Zone.", "data": "260k sqm GLA at Open Air Mall; expansion of retail leasing recurring cash flow", "impact": "High Margin", "source": "TMG Commercial Segment Reports"}, {"id": "O6", "factor": "Smart City & 5G Infrastructure", "details": "Monetizing smart-city utilities, solar microgrids, and fiber-optic networks across Noor City.", "data": "Integrated 5G smart-city grid, Siemens switchgear JV, solar microgrids", "impact": "Recurring Utility", "source": "EMAS Sewedy & TMG Tech Disclosures"}], "threats": [{"id": "T1", "factor": "Construction Cost Inflation", "details": "Cumulative domestic currency devaluation and imported material inflation push up cost-to-complete.", "data": "Egypt CPI inflation projected >16.7%; fixed-price off-plan sales sold in 2021-2023 at lower cost basis", "impact": "Margin Squeeze", "source": "Gleeds Construction Market Report 2026"}, {"id": "T2", "factor": "High Domestic Interest Rates", "details": "Elevated CBE policy rates increase borrowing costs and dampen mortgage affordability.", "data": "CBE overnight lending rate at 20%+; TMG interest-bearing debt & lease obligations >EGP 60.5B", "impact": "Financial Cost", "source": "Central Bank of Egypt MPC Statements"}, {"id": "T3", "factor": "Household Purchasing Strain", "details": "Erosion of domestic consumer real income reduces demand for primary residential property.", "data": "Contracted sales declined 24% YoY in 2025 (EGP 382.2B vs EGP 504.0B in 2024)", "impact": "Demand Risk", "source": "EFG Hermes Property Market Outlook 2026"}, {"id": "T4", "factor": "Consumer Protection Enforcement", "details": "CPA enforcement against 5%-10% resale transfer fees under Article 15 of Law 181/2018.", "data": "Widespread individual civil court rulings ordering refunds of administrative resale fees", "impact": "Legal Liability", "source": "Egyptian CPA Rulings & Law 181/2018"}, {"id": "T5", "factor": "Land Allocation Scrutiny", "details": "Public policy debates and media scrutiny regarding non-competitive direct state land allocations.", "data": "Historical 2010 SAC Madinaty annulment precedent; 2023 ARIJ investigative reporting", "impact": "Regulatory Risk", "source": "Egyptian State Council Rulings & ARIJ 2023"}, {"id": "T6", "factor": "Subcontractor Supply Chain Strain", "details": "Financial pressure on trade subcontractors leading to potential site walk-offs or delivery slippages.", "data": "2008 ACC Shehata Hassan complaint; 2024 Mada Masr SouthMED payment chain risk signal", "impact": "Operational Risk", "source": "Forensic Due Diligence & Press Reports"}]};
    const TMG_TOWS = {"SO": [{"id": "SO-1", "name": "Leverage Landbank for Asset-Light Growth", "roadmap": "Combine massive 26k+ feddan landbank with asset-light master development model (SouthMED) to maximize revenue while minimizing balance-sheet risk.", "priority": "High Priority"}, {"id": "SO-2", "name": "Monetize Icon Hotel FX Cash Flows", "roadmap": "Deploy USD/EUR hospitality revenues from Legacy/Four Seasons hotels to fund cross-border regional expansion in KSA (Banan) and Oman (Jood).", "priority": "High Priority"}, {"id": "SO-3", "name": "Scale Commercial Leasing Portfolio", "roadmap": "Utilize EGP 441B backlog visibility to pre-lease commercial retail centers (Open Air Mall, East Hub) and expand recurring revenue base.", "priority": "Medium Priority"}], "ST": [{"id": "ST-1", "name": "Centralized Bulk Material Hedging", "roadmap": "Use financial scale and liquidity reserves (EGP 66.4B) to bulk-purchase rebar and cement directly, hedging against construction cost inflation.", "priority": "High Priority"}, {"id": "ST-2", "name": "FX Debt & Revenue Matching", "roadmap": "Align foreign currency debt service with USD hospitality earnings, shielding group balance sheet from EGP devaluation shocks.", "priority": "High Priority"}, {"id": "ST-3", "name": "Flexible Customer Financing", "roadmap": "Utilize strong balance sheet to extend unit payment plans to 10-12 years, sustaining sales velocity amidst domestic affordability strain.", "priority": "Medium Priority"}], "WO": [{"id": "WO-1", "name": "Refinance High-Cost EGP Debt", "roadmap": "Use sovereign wealth partnerships (ADQ/ADNEC) and Gulf expansion cash flows to substitute 28.6% EGP debt with lower-cost regional credit.", "priority": "High Priority"}, {"id": "WO-2", "name": "Accelerate Cash Conversion via Asset Monetization", "roadmap": "Convert properties under development into liquid cash by monetizing commercial spaces via Rawasy and leasing vehicles to close OCF gap.", "priority": "High Priority"}, {"id": "WO-3", "name": "Enhance Maintenance Reserve Governance", "roadmap": "Establish independent audited trust accounts for Madinaty/Rehab maintenance deposits to eliminate resident litigation and improve brand trust.", "priority": "Medium Priority"}], "WT": [{"id": "WT-1", "name": "Shorten Subcontractor Payment Cycles", "roadmap": "Reduce post-dated check tenors from 270 days to 60-90 days to prevent trade subcontractor insolvency and avoid project completion slippages.", "priority": "Critical Priority"}, {"id": "WT-2", "name": "Reform Resale Fee Structures", "roadmap": "Replace percentage-based resale transfer fees with flat administrative costs to comply with CPA Article 15 and eliminate legal liability.", "priority": "High Priority"}, {"id": "WT-3", "name": "Cap Off-Balance Sheet Lease Leverage", "roadmap": "Freeze new sale-and-leaseback transactions (currently EGP 44B) to ensure debt service obligations do not consume operating cash flows.", "priority": "High Priority"}]};
    const TMG_PROJECTS_MAP = [{"id": "southmed", "name_ar": "مشروع ساوث ميد (SouthMED)", "name_en": "SouthMED Mediterranean Mega-Resort", "location_ar": "الضبعة، الساحل الشمالي (الكيلو 165 طريق الإسكندرية - مطروح)", "location_en": "El Dabaa, North Coast Mediterranean (Km 165)", "lat": 31.0167, "lng": 28.4, "area": "5,542 فدان (23.3 مليون م²)", "gdv": "21.0 مليار دولار GDV", "deliveries": "2029+", "contractors": "Concrete Plus (Zone C01 - 10B EGP), Atrium AQC, Metito, Crystal Lagoons", "color": "#06b6d4"}, {"id": "noor", "name_ar": "مدينة نور الذكية (Noor City)", "name_en": "Noor Smart City", "location_ar": "حدائق العاصمة، أمام العاصمة الإدارية (شرق القاهرة)", "location_en": "Capital Gardens, East Cairo (Opposite NAC)", "lat": 30.1667, "lng": 31.75, "area": "5,000 فدان (140,000 وحدة سكنية)", "gdv": "> 500 مليار جنيه مصري", "deliveries": "2026 – 2028+", "contractors": "Concrete Plus (V3.2 - 170 Villas), Atrium AQC, Siemens, Schneider Electric", "color": "#3b82f6"}, {"id": "madinaty", "name_ar": "مدينتي و East Hub و Open Air Mall", "name_en": "Madinaty Integrated City & East Hub", "location_ar": "القاهرة الجديدة، طريق السويس", "location_en": "New Cairo, Suez Road", "lat": 30.0833, "lng": 31.6333, "area": "8,000 فدان (33.6 مليون م²)", "gdv": "مجتمع متكامل يضم >700 ألف نسمة", "deliveries": "مكتمل جزئياً / توسعات مستمرة", "contractors": "Atrium AQC, Alexandria Construction (ACC), CCC (Four Seasons Capital JV), MCBS", "color": "#10b981"}, {"id": "celia", "name_ar": "مشروع سيليا (Celia New Capital)", "name_en": "Celia New Administrative Capital", "location_ar": "العاصمة الإدارية الجديدة، الحزام الأخضر", "location_en": "New Administrative Capital, Green River", "lat": 30.0167, "lng": 31.7, "area": "500 فدان (فيلات وعمارات فاخرة)", "gdv": "> 35 مليار جنيه مبيعات", "deliveries": "تسليمات مرحلية جارية", "contractors": "Atrium Quality Contractors, Alexandria Construction (ACC)", "color": "#8b5cf6"}, {"id": "fs_luxor", "name_ar": "فندق فورسيزونز الأقصر (Four Seasons Luxor)", "name_en": "Four Seasons Hotel Luxor", "location_ar": "الأقصر، كورنيش النيل مباشرة", "location_en": "Luxor, Direct Nile Corniche", "lat": 25.6872, "lng": 32.6396, "area": "فندق تاريخي فاخر 201 غرفة وجناح", "gdv": "رافعة تدفقات دولارية (Icon Hospitality)", "deliveries": "2026/2027", "contractors": "Atrium Quality Contractors (Main EPC Turnkey)", "color": "#f59e0b"}, {"id": "fs_sharm", "name_ar": "فورسيزونز شرم الشيخ (Four Seasons Sharm)", "name_en": "Four Seasons Resort Sharm El Sheikh", "location_ar": "شرم الشيخ، خليج القرش (البحر الأحمر)", "location_en": "Sharm El Sheikh, Sharks Bay (Red Sea)", "lat": 27.9158, "lng": 34.3299, "area": "توسعة منتجع فاخر بـ 1,400 غرفة وفيلا", "gdv": "أعلى عائد سياحي دولاري بالغرفة", "deliveries": "قيد التشغيل وتوسعات نشطة", "contractors": "Atrium Quality Contractors, ACC", "color": "#ec4899"}, {"id": "san_stefano", "name_ar": "سان ستيفانو جراند بلازا (San Stefano Alexandria)", "name_en": "San Stefano Grand Plaza Alexandria", "location_ar": "الإسكندرية، كورنيش سان ستيفانو", "location_en": "Alexandria, Corniche Landmark", "lat": 31.2439, "lng": 29.9678, "area": "برج متعدد الاستخدامات + فورسيزونز + مارينا", "gdv": "أحد أبرز أصول محفظة الضيافة والتجزئة", "deliveries": "مشروع قائم ومُدر للدخل الدوري", "contractors": "Alexandria Construction (ACC), Atrium AQC", "color": "#6366f1"}, {"id": "banan", "name_ar": "مدينة بنان الذكية - الرياض (Banan Riyadh)", "name_en": "Banan Smart City Riyadh (KSA)", "location_ar": "ضاحية الفرسان، شمال شرق الرياض، المملكة العربية السعودية", "location_en": "Al Fursan Suburb, North-East Riyadh, KSA", "lat": 24.85, "lng": 46.75, "area": "10.0 مليون م² (27,000 وحدة سكنية)", "gdv": "31.4 مليار ريال سعودي (> 8.3B USD)", "deliveries": "2029 المستهدف الأول", "contractors": "Atrium Saudi (100%), NHC (الشركة الوطنية للإسكان)", "color": "#10b981"}, {"id": "jood_yamal", "name_ar": "مدينتي جود ويامال - سلطنة عمان", "name_en": "Jood & Yamal Coastal Cities (Oman)", "location_ar": "مسقط / بركاء، ساحل سلطنة عمان", "location_en": "Muscat / Barka Coast, Sultanate of Oman", "lat": 23.7, "lng": 58.0, "area": "4.9 مليون م² (~14,000 وحدة سكنية)", "gdv": "1.8 مليار ريال عماني (~ 4.7B USD)", "deliveries": "مرحلة التخطيط والتمهيد", "contractors": "تحالف مجموعة طلعت مصطفى ووزارة الإسكان العمانية", "color": "#14b8a6"}];

    
    // XSS Sanitizer & Protocol Validator (Codex Audit Recommendation)
    function escapeHTML(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function safeUrl(url, allowedProtocols = ['http:', 'https:']) {
      if (!url) return '';
      try {
        const parsed = new URL(url);
        return allowedProtocols.includes(parsed.protocol) ? parsed.href : '';
      } catch (e) {
        return '';
      }
    }

    let activeProjectFilter = 'all';
    let tmgLeafletMapInstance = null;
    let tmgMapMarkers = {};

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
    function filterMapByProject(projId) {
      activeProjectFilter = projId;

      // Update Filter Chips UI
      document.querySelectorAll('#project-filter-chips .filter-chip').forEach(btn => {
        const onclickAttr = btn.getAttribute('onclick') || '';
        btn.classList.toggle('active', onclickAttr.includes(`'${projId}'`));
      });

      // Update Map View
      if (tmgLeafletMapInstance) {
        if (projId === 'all') {
          tmgLeafletMapInstance.setView([28.5, 36.0], 5);
          document.getElementById('map-selection-indicator').textContent = 'المشروع النشط: عرض جميع المشروعات';
        } else {
          const proj = TMG_PROJECTS_MAP.find(p => p.id === projId);
          if (proj) {
            tmgLeafletMapInstance.setView([proj.lat, proj.lng], 9);
            if (tmgMapMarkers[projId]) {
              tmgMapMarkers[projId].openPopup();
            }
            document.getElementById('map-selection-indicator').innerHTML = `المشروع النشط: <strong>${proj.name_ar}</strong> (${proj.area})`;
          }
        }
      }

      // Cross-filter Companies Table and Teams Grid
      renderCompaniesTable();
      renderTeamsCards();

      // Smooth scroll to table if a specific project was selected
      if (projId !== 'all') {
        const tableEl = document.getElementById('companies-table-dom');
        if (tableEl) {
          tableEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }
    }

    function resetProjectFilter() {
      filterMapByProject('all');
      document.getElementById('company-search-input').value = '';
      document.getElementById('company-role-filter').value = 'all';
      document.getElementById('team-search-input').value = '';
      applyCompanyFilters();
      applyTeamFilters();
    }

    // Render Companies Table
    function renderCompaniesTable() {
      const tbody = document.getElementById('companies-table-body');
      if (!tbody) return;

      const searchTerm = (document.getElementById('company-search-input')?.value || '').toLowerCase().trim();
      const roleFilter = document.getElementById('company-role-filter')?.value || 'all';

      let filtered = TMG_COMPANIES.filter(c => {
        // Project Match (Full Multi-Keyword & Oman Support)
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': ['southmed', 'ساوث'],
            'noor': ['نور', 'noor'],
            'madinaty': ['مدينتي', 'madinaty'],
            'celia': ['celia', 'سيليا'],
            'fs_luxor': ['أقصر', 'luxor'],
            'fs_sharm': ['شرم', 'sharm'],
            'san_stefano': ['سان ستيفانو', 'san stefano', 'إسكندرية'],
            'banan': ['سعودية', 'رياض', 'بنان', 'banan', 'ksa'],
            'jood_yamal': ['عمان', 'جود', 'يامال', 'oman']
          };
          const keywords = projMap[activeProjectFilter];
          if (keywords && !keywords.some(k => (c.project || '').toLowerCase().includes(k.toLowerCase()))) {
            return false;
          }
        }

        // Role Filter
        if (roleFilter !== 'all') {
          if (roleFilter === 'مقاول' && !c.role.includes('مقاول') && !c.relation.includes('مقاول')) return false;
          if (roleFilter === 'ذراع' && !c.role.includes('ذراع') && !c.relation.includes('منظومة')) return false;
          if (roleFilter === 'مورد' && !c.role.includes('مورد') && !c.role.includes('تجهيز') && !c.role.includes('أنظمة')) return false;
          if (roleFilter === 'استشاري' && !c.role.includes('استشار') && !c.role.includes('إشراف')) return false;
          if (roleFilter === 'بنك' && !c.role.includes('بنك') && !c.relation.includes('بنك')) return false;
        }

        // Search Term
        if (searchTerm) {
          const matchStr = `${c.name} ${c.role} ${c.project} ${c.phone} ${c.relation}`.toLowerCase();
          if (!matchStr.includes(searchTerm)) return false;
        }

        return true;
      });

      document.getElementById('companies-count-badge').textContent = `${filtered.length} / 42 شركة`;

      if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:30px; color:var(--text-muted);">لا توجد شركات مطابقة لمعايير البحث والتصفية المحددة.</td></tr>`;
        return;
      }

      tbody.innerHTML = filtered.map((c, idx) => {
        // Evidence badge color
        const evColor = c.evidence_level.startsWith('A') ? 'badge-low' : (c.evidence_level.includes('B') ? 'badge-med' : 'badge-high');
        
        // Format Phones with click-to-call
        const phoneLinks = c.phone && c.phone !== 'غير متاح'
          ? c.phone.split('/').map(p => {
              const cleanP = p.replace(/[^0-9+]/g, '');
              return `<a href="tel:${cleanP}" style="color:var(--accent-blue); text-decoration:none; font-family:var(--font-mono); font-size:12px; margin-inline-end:6px;">📞 ${p.trim()}</a>`;
            }).join('<br>')
          : `<span style="color:var(--text-muted); font-size:11.5px;">غير معلن</span>`;

        // Format Email
        const emailLink = c.email && c.email !== 'غير متاح'
          ? `<a href="mailto:${c.email}" style="color:var(--accent-cyan); text-decoration:none; font-size:11.5px; display:block; overflow:hidden; text-overflow:ellipsis;">✉️ ${c.email}</a>`
          : `<span style="color:var(--text-muted); font-size:11px;">—</span>`;

        // Website
        const webLink = c.website && c.website.startsWith('http')
          ? `<a href="${c.website}" target="_blank" style="color:var(--accent-emerald); text-decoration:none; font-size:11.5px; font-weight:700;">🌐 زيارة الموقع ↗</a>`
          : ``;

        return `
          <tr style="border-bottom: 1px solid var(--border-subtle); hover: background-color: var(--bg-surface-elevated);">
            <td style="padding: 10px 12px; font-weight:700; color:var(--text-muted);">${c.id}</td>
            <td style="padding: 10px 12px;">
              <div style="font-weight:800; color:var(--text-main); font-size:13.5px;">${c.name}</div>
              <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">${c.relation}</div>
            </td>
            <td style="padding: 10px 12px;">
              <span class="badge" style="background:rgba(59,130,246,0.1); color:var(--accent-blue); font-size:11px;">${c.project}</span>
            </td>
            <td style="padding: 10px 12px; font-size:12.5px; line-height:1.5;">
              <div style="white-space:pre-line;">${c.role}</div>
              ${c.notes ? `<div style="font-size:11px; color:var(--text-muted); margin-top:4px;">ℹ️ ${c.notes}</div>` : ''}
            </td>
            <td style="padding: 10px 12px; font-size:12px; color:var(--text-muted);">${c.relation}</td>
            <td style="padding: 10px 12px; line-height:1.6;">${phoneLinks}</td>
            <td style="padding: 10px 12px; line-height:1.5;">${emailLink}${webLink}</td>
            <td style="padding: 10px 12px; text-align:center;">
              <span class="badge ${evColor}" style="font-size:11px; font-weight:700;">${c.evidence_level}</span>
              <div style="font-size:10px; color:var(--text-muted); margin-top:2px;">${c.confidence}</div>
            </td>
          </tr>
        `;
      }).join('');
    }

    function applyCompanyFilters() {
      renderCompaniesTable();
    }

    // Render Teams Cards
    function renderTeamsCards() {
      const container = document.getElementById('teams-cards-grid');
      if (!container) return;

      const searchTerm = (document.getElementById('team-search-input')?.value || '').toLowerCase().trim();

      let filtered = TMG_TEAMS.filter(t => {
        // Project Match (Full Multi-Keyword & Oman Support)
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': ['southmed', 'ساوث'],
            'noor': ['نور', 'noor'],
            'madinaty': ['مدينتي', 'madinaty'],
            'celia': ['celia', 'سيليا'],
            'fs_luxor': ['أقصر', 'luxor'],
            'fs_sharm': ['شرم', 'sharm'],
            'san_stefano': ['سان ستيفانو', 'san stefano', 'إسكندرية'],
            'banan': ['سعودية', 'رياض', 'بنان', 'banan', 'ksa'],
            'jood_yamal': ['عمان', 'جود', 'يامال', 'oman']
          };
          const keywords = projMap[activeProjectFilter];
          if (keywords && !keywords.some(k => (t.project || '').toLowerCase().includes(k.toLowerCase()))) {
            return false;
          }
        }

        // Search Term
        if (searchTerm) {
          const matchStr = `${t.name} ${t.role} ${t.company} ${t.project}`.toLowerCase();
          if (!matchStr.includes(searchTerm)) return false;
        }

        return true;
      });

      document.getElementById('teams-count-badge').textContent = `${filtered.length} / 38 كادراً`;

      if (filtered.length === 0) {
        container.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:30px; color:var(--text-muted);">لا توجد ملفات مهنية مطابقة لخيارات التصفية.</div>`;
        return;
      }

      container.innerHTML = filtered.map(t => {
        const evBadge = t.evidence_level.startsWith('A') ? 'badge-low' : (t.evidence_level.includes('B') ? 'badge-med' : 'badge-high');
        
        return `
          <div style="background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); border-radius:10px; padding:14px; display:flex; flex-direction:column; justify-content:space-between; transition: transform 0.2s;" onmouseover="this.style.borderColor='var(--accent-blue)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:8px;">
                <div style="font-weight:800; font-size:14px; color:var(--text-main);">${t.name}</div>
                <span class="badge ${evBadge}" style="font-size:10.5px;">دليل ${t.evidence_level}</span>
              </div>
              
              <div style="font-size:12px; font-weight:700; color:var(--accent-blue); margin-top:4px; line-height:1.4;">
                ${t.role}
              </div>

              <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:8px;">
                <span style="font-size:11px; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:4px; color:var(--text-muted);">🏢 ${t.company}</span>
                <span style="font-size:11px; background:rgba(59,130,246,0.1); padding:2px 8px; border-radius:4px; color:var(--accent-blue);">📍 ${t.project}</span>
              </div>

              ${t.notes ? `<p style="font-size:11.5px; color:var(--text-muted); margin:8px 0 0; line-height:1.5;">${t.notes}</p>` : ''}
            </div>

            <div style="margin-top:12px; pt:8px; border-top:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:11px; color:var(--text-muted);">${t.phone !== 'غير منشور' ? t.phone : 'هاتف العمل متاح بالشركة'}</span>
              <a href="${t.linkedin}" target="_blank" style="background:#0a66c2; color:#fff; text-decoration:none; padding:4px 10px; border-radius:6px; font-size:11.5px; font-weight:700; display:inline-flex; align-items:center; gap:4px;">
                <svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                عرض الملف ↗
              </a>
            </div>
          </div>
        `;
      }).join('');
    }

    function applyTeamFilters() {
      renderTeamsCards();
    }

    // Render SWOT & TOWS
    function renderSwotAndTows() {
      // Strengths
      const strContainer = document.getElementById('swot-strengths-container');
      if (strContainer) {
        strContainer.innerHTML = TMG_SWOT.strengths.map(s => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-emerald);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${s.id}: ${s.factor}</span>
              <span class="badge badge-low" style="font-size:10px;">${s.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${s.details}</p>
            <div style="font-size:11px; color:var(--accent-emerald); margin-top:4px; font-weight:700;">📊 ${s.data}</div>
          </div>
        `).join('');
      }

      // Weaknesses
      const wContainer = document.getElementById('swot-weaknesses-container');
      if (wContainer) {
        wContainer.innerHTML = TMG_SWOT.weaknesses.map(w => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-rose);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${w.id}: ${w.factor}</span>
              <span class="badge badge-high" style="font-size:10px;">${w.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${w.details}</p>
            <div style="font-size:11px; color:var(--accent-rose); margin-top:4px; font-weight:700;">⚠️ ${w.data}</div>
          </div>
        `).join('');
      }

      // Opportunities
      const oContainer = document.getElementById('swot-opportunities-container');
      if (oContainer) {
        oContainer.innerHTML = TMG_SWOT.opportunities.map(o => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-blue);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${o.id}: ${o.factor}</span>
              <span class="badge badge-low" style="font-size:10px;">${o.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${o.details}</p>
            <div style="font-size:11px; color:var(--accent-blue); margin-top:4px; font-weight:700;">🚀 ${o.data}</div>
          </div>
        `).join('');
      }

      // Threats
      const tContainer = document.getElementById('swot-threats-container');
      if (tContainer) {
        tContainer.innerHTML = TMG_SWOT.threats.map(t => `
          <div style="background:var(--bg-surface-elevated); padding:10px 12px; border-radius:8px; border-inline-start:3px solid var(--accent-amber);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:800; font-size:13px; color:var(--text-main);">${t.id}: ${t.factor}</span>
              <span class="badge badge-med" style="font-size:10px;">${t.impact}</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); margin:4px 0 0; line-height:1.5;">${t.details}</p>
            <div style="font-size:11px; color:var(--accent-amber); margin-top:4px; font-weight:700;">⚡ ${t.data}</div>
          </div>
        `).join('');
      }

      // TOWS Containers
      ['SO', 'ST', 'WO', 'WT'].forEach(cat => {
        const el = document.getElementById(`tows-${cat.toLowerCase()}-container`);
        if (el && TMG_TOWS[cat]) {
          el.innerHTML = TMG_TOWS[cat].map(strat => `
            <div style="background:var(--bg-surface); padding:8px 10px; border-radius:6px; margin-bottom:6px;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:700; font-size:12.5px; color:var(--text-main);">${strat.id}: ${strat.name}</span>
                <span class="badge badge-med" style="font-size:10px;">${strat.priority}</span>
              </div>
              <p style="font-size:11.5px; color:var(--text-muted); margin:4px 0 0; line-height:1.4;">${strat.roadmap}</p>
            </div>
          `).join('');
        }
      });
    }

    function switchSwotView(view) {
      document.getElementById('swot-quadrants-view').style.display = view === 'swot' ? 'grid' : 'none';
      document.getElementById('tows-matrix-view').style.display = view === 'tows' ? 'flex' : 'none';
      document.getElementById('btn-show-swot').classList.toggle('active', view === 'swot');
      document.getElementById('btn-show-tows').classList.toggle('active', view === 'tows');
    }

    // Initial render on load
    document.addEventListener('DOMContentLoaded', function() {
      renderCompaniesTable();
      renderTeamsCards();
      renderSwotAndTows();
    });