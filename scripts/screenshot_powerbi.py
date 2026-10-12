from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('file:///F:/Mr%20Hesham/TMG/TMG_Forensic_Due_Diligence_Dashboard.html')
    page.wait_for_timeout(1500)
    
    # 1. Capture Overview with native Power BI action bars and Waterfall connectors
    page.screenshot(path='pbi_overview_waterfall.png', full_page=False)

    # 2. Trigger Focus Mode on Cash Waterfall
    page.evaluate("openFocusMode('chartWaterfallCashFlow', '1. شلال تحويل السيولة النقدية (Cash Conversion Waterfall)')")
    page.wait_for_timeout(800)
    page.screenshot(path='pbi_focus_mode_waterfall.png', full_page=False)
    page.evaluate("closeFocusMode()")
    page.wait_for_timeout(400)

    # 3. Tab 2: Captive Procurement with 4-Pillar Hybrid Closed-Loop Model
    page.evaluate("switchTab('procurement')")
    page.wait_for_timeout(800)
    page.screenshot(path='pbi_tab2_procurement_hybrid.png', full_page=False)

    # 4. Tab 5: Contractors Grid with Concrete Plus 10B SouthMED Card
    page.evaluate("switchTab('contractors')")
    page.wait_for_timeout(800)
    page.screenshot(path='pbi_tab5_concrete_plus_card.png', full_page=False)

    browser.close()
    print('Power BI feature screenshots captured successfully.')
