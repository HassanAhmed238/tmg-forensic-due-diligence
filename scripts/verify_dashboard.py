# -*- coding: utf-8 -*-
with open(r"F:\Mr Hesham\TMG\TMG_Forensic_Due_Diligence_Dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

charts_list = [
    'chartWaterfallCashFlow',
    'chartRevenueBacklogCombo',
    'chartForensicRiskRadar',
    'chartDebtStructureTreemapDoughnut',
    'chartOwnershipUBODoughnut',
    'chartIPCMustakhlasatSCurve',
    'chartContractorDisputeBubble',
    'chartVulnerabilityGauge',
    'chartInflationTornado',
    'landbankBarChart',
    'chartEvidenceHierarchyPolar',
    'chartLagoonMEPCapexOpex',
    'chartComplaints',
    'chartProjectDeliveryTimeline',
    'chartEvidenceSentiment'
]

checks = [
    ("Total Size > 300KB", len(content) > 300000),
    ("White/Light Mode Default Active", 'data-theme="light"' in content),
    ("Dual Theme Toggle Supported", 'toggleTheme' in content and 'data-theme="dark"' in content),
    ("PowerBI Slicer Bar Present", 'pbi-slicer-bar' in content),
    ("Executive KPI Ribbon Present", 'pbi-kpi-ribbon' in content),
    ("All 15 Charts Present", all(cid in content for cid in charts_list)),
    ("D3.js Privity Tree Present", 'id="d3-privity-tree"' in content and 'd3.hierarchy' in content),
    ("No Hassan Soliman branding tags", 'Hassan Soliman Mode' not in content),
    ("No ui-a11y tags", '/ui-a11y' not in content),
    ("CEO Presenter Mode with 10 Slides Present", 'SLIDE 10 / 10' in content),
    ("Atrium Expanded Network Grid Present", 'lbl-atrium-matrix-title' in content and 'atrium-grid' in content),
    ("Sentiment 4-Pillar Matrix Present", 'sentiment-pillars-grid' in content and 'mada_southmed_2024' in content),
    ("8-Point Forensic Checklist Present", 'checklist-grid' in content and '8-Point Forensic Checklist' in content),
    ("New Contractor Network Present (Everlast, Siraj, EMAS, Devzah, Knauf)", all(n in content for n in ['Everlast', 'Siraj', 'EMAS', 'Devzah', 'Knauf'])),
    ("Core Projects Present", all(p in content for p in ['SouthMed', 'Noor City', 'Madinaty', 'Celia', 'Banan'])),
    ("Docx Case 2923/2012 Scaffolding Present", '2923' in content and '609,625' in content and 'خالد هنداوي' in content),
    ("Docx Case 2008 Intentional Delay Present", 'إبراهيم حسبو' in content and 'شحاتة' in content),
    ("Docx 5-Point Verification Protocol Present", 'verification-gap-grid' in content and 'Verification Gap' in content),
    ("Docx Legal & Investigative Sources Present", all(s in content for s in ['khatib_scaffolding_2012', 'haditha_contractor_2023', 'arij_land_allocation_2023', 'fra_assignment_guidance_2026'])),
    ("Tab 10 Investor & Homeowner Advisory Present", 'id="tab-advisory"' in content and 'nav-advisory' in content),
    ("Consumer Protection Law 181/2018 Article 15 Present", 'قانون حماية المستهلك رقم 181 لسنة 2018' in content and 'المادة 15' in content),
    ("CEO Presenter Mode with 11 Slides Present", 'SLIDE 11 / 11' in content),
    ("New Grounded Forensic Sources in sourcesDB", all(s in content for s in ['egx_leaseback_debt_2026', 'tmg_backlog_statutory_2025', 'fra_related_parties_2026', 'nuca_acud_land_decrees', 'tmg_standard_contract_terms', 'madinaty_maintenance_audit'])),
    ("Tab 10 Interactive Evidence Inspection Triggers", all(f"showSourceModal('{s}')" in content for s in ['egx_leaseback_debt_2026', 'tmg_backlog_statutory_2025', 'fra_related_parties_2026', 'nuca_acud_land_decrees', 'tmg_standard_contract_terms', 'madinaty_maintenance_audit', 'cpa_article15_resale', 'egx_filings_fy25_h126'])),
    ("Slide 11 Evidence Verification Buttons Active", 'SLIDE 11 / 11' in content and "showSourceModal('egx_filings_fy25_h126')" in content and "showSourceModal('cpa_article15_resale')" in content)
]

all_passed = True
for name, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        all_passed = False

print("\nCharts Check Detail:")
for cid in charts_list:
    found = cid in content
    print(f"  - {cid}: {'FOUND' if found else 'MISSING'}")

if all_passed:
    print(f"\n>>> ALL {len(checks)} VERIFICATION SUITES PASSED WITH 100% SUCCESS.")
else:
    print("\n>>> SOME CHECKS FAILED.")
