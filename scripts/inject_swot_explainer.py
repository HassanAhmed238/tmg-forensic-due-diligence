# -*- coding: utf-8 -*-
"""
Inject interactive explanatory guide into SWOT / TOWS section in TMG_Forensic_Due_Diligence_Dashboard.html
"""

import sys

sys.stdout.reconfigure(encoding='utf-8')

DASHBOARD_PATH = r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html"

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

target_marker = '<!-- View 1: 4 SWOT Quadrants -->'
idx = text.find(target_marker)

if idx == -1:
    print("Could not find target marker for SWOT quadrants!")
    sys.exit(1)

swot_explainer_html = '''<!-- EXPLANATORY GUIDE FOR VIEWERS (SWOT vs TOWS Decoder) -->
            <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 18px; margin-bottom: 20px; border-inline-start: 5px solid var(--accent-cyan);">
              <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="font-size:18px;">💡</span>
                  <span style="font-weight:900; font-size:14.5px; color:var(--text-main);" id="t-swot-guide-title">دليل المشاهد: كيف تقرأ وتفهم مصفوفة SWOT ومصفوفة TOWS التنفيذية؟</span>
                </div>
                <span class="badge badge-low" style="background:rgba(6,182,212,0.15); color:var(--accent-cyan); border-color:var(--accent-cyan);" id="badge-swot-guide">فلسفة التحليل الاستراتيجي</span>
              </div>
              
              <p style="margin:0 0 14px; font-size:12.5px; color:var(--text-muted); line-height:1.6;" id="t-swot-guide-intro">
                <strong>الفرق الجوهري:</strong> تحليل <strong>SWOT</strong> هو <em>مرآة تشخيصية ساكنة</em> ترصد الوضع الحالي (الداخل: القوة والضعف / الخارج: الفرص والتهديدات). أما مصفوفة <strong>TOWS</strong> فهي <em>خريطة قتال تفاعلية</em> تقاطع المحاور الأربعة لتوليد استراتيجيات عملية تجيب على سؤال: <strong>"ماذا سنفعل الآن؟"</strong>
              </p>

              <!-- 4 Matrix Explainer Cards -->
              <div class="grid-4" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 14px;">
                <div style="background:var(--bg-card); border:1px solid rgba(16,185,129,0.3); border-radius:8px; padding:12px; border-inline-start:3px solid var(--accent-emerald);">
                  <div style="font-weight:800; font-size:12.5px; color:var(--accent-emerald); margin-bottom:4px;" id="t-swot-card-so-t">🎯 استراتيجيات SO (الهجوم)</div>
                  <div style="font-size:11.5px; color:var(--text-muted); line-height:1.5;" id="t-swot-card-so-d"><strong>القوة + الفرص (Maxi-Maxi):</strong> استغلال الأصول الضخمة والفنادق لاقتناص مشاريع ساوث ميد والتوسع الخليجي.</div>
                </div>

                <div style="background:var(--bg-card); border:1px solid rgba(245,158,11,0.3); border-radius:8px; padding:12px; border-inline-start:3px solid var(--accent-amber);">
                  <div style="font-weight:800; font-size:12.5px; color:var(--accent-amber); margin-bottom:4px;" id="t-swot-card-st-t">🛡️ استراتيجيات ST (التحصين)</div>
                  <div style="font-size:11.5px; color:var(--text-muted); line-height:1.5;" id="t-swot-card-st-d"><strong>القوة + التهديدات (Maxi-Mini):</strong> استخدام الكاش الملياري والشراء المركزي لمواد البناء لتحييد التضخم والفائدة.</div>
                </div>

                <div style="background:var(--bg-card); border:1px solid rgba(59,130,246,0.3); border-radius:8px; padding:12px; border-inline-start:3px solid var(--accent-blue);">
                  <div style="font-weight:800; font-size:12.5px; color:var(--accent-blue); margin-bottom:4px;" id="t-swot-card-wo-t">🔄 استراتيجيات WO (العلاج)</div>
                  <div style="font-size:11.5px; color:var(--text-muted); line-height:1.5;" id="t-swot-card-wo-d"><strong>الضعف + الفرص (Mini-Maxi):</strong> معالجة فجوة السيولة وديون التأجير التمويلي عبر شراكات التطوير السيادية (ADQ).</div>
                </div>

                <div style="background:var(--bg-card); border:1px solid rgba(244,63,94,0.3); border-radius:8px; padding:12px; border-inline-start:3px solid var(--accent-rose);">
                  <div style="font-weight:800; font-size:12.5px; color:var(--accent-rose); margin-bottom:4px;" id="t-swot-card-wt-t">🚨 استراتيجيات WT (الإنقاذ)</div>
                  <div style="font-size:11.5px; color:var(--text-muted); line-height:1.5;" id="t-swot-card-wt-d"><strong>الضعف + التهديدات (Mini-Mini):</strong> تفادي أزمات تعثر مقاولي الباطن والشيكات الآجلة وتجميد قروض التأجير التمويلي.</div>
                </div>
              </div>

              <!-- P.ZONE Lens Callout -->
              <div style="background:rgba(6,182,212,0.06); border:1px dashed var(--accent-cyan); border-radius:8px; padding:10px 14px; display:flex; align-items:center; gap:10px;">
                <span style="font-size:16px;">⚠️</span>
                <div style="font-size:12px; color:var(--text-main); line-height:1.5;" id="t-swot-pz-lens">
                  <strong>دلالة التحليل لمقاول الباطن (P.ZONE):</strong> طلعت مصطفى يستخدم المقاولين كخط دفاع في <strong>ST1 و WT1</strong> (عبر تأخير الصرف DPO لـ 160 يوماً لامتصاص التضخم). وفي نفس الوقت، تفتح استراتيجية <strong>SO1 و SO2</strong> فرصاً غير مسبوقة لحزم البحيرات والمسابح بمليارات الجنيهات في ساوث ميد وبنان. <em>الشرط الوحيد للنجاح: حماية شروط الدفع والعملة!</em>
                </div>
              </div>
            </div>

            '''

if "<!-- EXPLANATORY GUIDE FOR VIEWERS (SWOT vs TOWS Decoder) -->" not in text:
    text = text[:idx] + swot_explainer_html + text[idx:]
    print("Injected SWOT explainer HTML successfully!")
else:
    print("SWOT explainer HTML already present.")

# Also add bilingual update logic inside updateFinancialLanguage or setLanguage
translation_swot = """
      // SWOT / TOWS Explainer Translations
      const swotTrans = {
        guideTitle: { ar: "دليل المشاهد: كيف تقرأ وتفهم مصفوفة SWOT ومصفوفة TOWS التنفيذية؟", en: "Viewer Guide: How to Read & Interpret TMG SWOT & Executive TOWS Matrix" },
        guideBadge: { ar: "فلسفة التحليل الاستراتيجي", en: "Strategic Methodology" },
        guideIntro: {
          ar: "<strong>الفرق الجوهري:</strong> تحليل <strong>SWOT</strong> هو <em>مرآة تشخيصية ساكنة</em> ترصد الوضع الحالي (الداخل: القوة والضعف / الخارج: الفرص والتهديدات). أما مصفوفة <strong>TOWS</strong> فهي <em>خريطة قتال تفاعلية</em> تقاطع المحاور الأربعة لتوليد استراتيجيات عملية تجيب على سؤال: <strong>\\\"ماذا سنفعل الآن؟\\\"</strong>",
          en: "<strong>Core Difference:</strong> <strong>SWOT</strong> is a <em>diagnostic snapshot</em> of current state (Internal: S & W / External: O & T). The <strong>TOWS</strong> matrix is an <em>actionable battle plan</em> that cross-matches the 4 pillars to answer: <strong>\\\"What specific actions do we execute right now?\\\"</strong>"
        },
        soT: { ar: "🎯 استراتيجيات SO (الهجوم)", en: "🎯 SO Strategies (Offensive Maxi-Maxi)" },
        soD: { ar: "<strong>القوة + الفرص:</strong> استغلال الأصول الضخمة والفنادق لاقتناص مشاريع ساوث ميد والتوسع الخليجي.", en: "<strong>Strengths + Opportunities:</strong> Deploy massive landbank & hotel cash flows to capture SouthMED and Gulf expansion." },
        stT: { ar: "🛡️ استراتيجيات ST (التحصين)", en: "🛡️ ST Strategies (Defensive Maxi-Mini)" },
        stD: { ar: "<strong>القوة + التهديدات:</strong> استخدام الكاش الملياري والشراء المركزي لمواد البناء لتحييد التضخم والفائدة.", en: "<strong>Strengths + Threats:</strong> Use liquidity scale & centralized bulk buying to neutralize building inflation & 28% interest rates." },
        woT: { ar: "🔄 استراتيجيات WO (العلاج)", en: "🔄 WO Strategies (Remedial Mini-Maxi)" },
        woD: { ar: "<strong>الضعف + الفرص:</strong> معالجة فجوة السيولة وديون التأجير التمويلي عبر شراكات التطوير السيادية (ADQ).", en: "<strong>Weaknesses + Opportunities:</strong> Overcome cash conversion lag & lease liabilities via sovereign joint ventures (ADQ)." },
        wtT: { ar: "🚨 استراتيجيات WT (الإنقاذ)", en: "🚨 WT Strategies (Survival Mini-Mini)" },
        wtD: { ar: "<strong>الضعف + التهديدات:</strong> تفادي أزمات تعثر مقاولي الباطن والشيكات الآجلة وتجميد قروض التأجير التمويلي.", en: "<strong>Weaknesses + Threats:</strong> Mitigate trade contractor insolvencies, shorten checks, and freeze new leaseback leverage." },
        pzLens: {
          ar: "<strong>دلالة التحليل لمقاول الباطن (P.ZONE):</strong> طلعت مصطفى يستخدم المقاولين كخط دفاع في <strong>ST1 و WT1</strong> (عبر تأخير الصرف DPO لـ 160 يوماً لامتصاص التضخم). وفي نفس الوقت، تفتح استراتيجية <strong>SO1 و SO2</strong> فرصاً غير مسبوقة لحزم البحيرات والمسابح بمليارات الجنيهات في ساوث ميد وبنان. <em>الشرط الوحيد للنجاح: حماية شروط الدفع والعملة!</em>",
          en: "<strong>Implication for Subcontractors (P.ZONE):</strong> TMG deploys contractors as a buffer in <strong>ST1 & WT1</strong> (stretching DPO to 160 days to absorb macro inflation). Simultaneously, strategies <strong>SO1 & SO2</strong> unlock multi-billion EGP water packages in SouthMED and Banan. <em>Crucial rule for success: Protect FX pricing & demand advance letters of credit!</em>"
        }
      };

      const setSwotT = (id, obj) => {
        const el = document.getElementById(id);
        if (el) el.innerHTML = isAr ? obj.ar : obj.en;
      };

      setSwotT('t-swot-guide-title', swotTrans.guideTitle);
      setSwotT('badge-swot-guide', swotTrans.guideBadge);
      setSwotT('t-swot-guide-intro', swotTrans.guideIntro);
      setSwotT('t-swot-card-so-t', swotTrans.soT);
      setSwotT('t-swot-card-so-d', swotTrans.soD);
      setSwotT('t-swot-card-st-t', swotTrans.stT);
      setSwotT('t-swot-card-st-d', swotTrans.stD);
      setSwotT('t-swot-card-wo-t', swotTrans.woT);
      setSwotT('t-swot-card-wo-d', swotTrans.woD);
      setSwotT('t-swot-card-wt-t', swotTrans.wtT);
      setSwotT('t-swot-card-wt-d', swotTrans.wtD);
      setSwotT('t-swot-pz-lens', swotTrans.pzLens);
"""

# Inject into updateFinancialLanguage
if "const swotTrans = {" not in text:
    marker_lang = "function updateFinancialLanguage() {"
    text = text.replace(marker_lang, marker_lang + "\n" + translation_swot, 1)
    print("Injected SWOT bilingual translation into updateFinancialLanguage!")

with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("Finished updating dashboard with SWOT explainer!")
