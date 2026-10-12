from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('file:///F:/Mr%20Hesham/TMG/TMG_Forensic_Due_Diligence_Dashboard.html')
    page.wait_for_timeout(1000)
    
    # Click advisory nav button
    page.evaluate("switchTab('advisory')")
    page.wait_for_timeout(1000)
    page.screenshot(path='dashboard_tab10_advisory.png', full_page=False)

    # Click a source link to open modal
    page.evaluate("showSourceModal('cpa_article15_resale')")
    page.wait_for_timeout(500)
    page.screenshot(path='dashboard_source_modal_cpa.png')
    page.evaluate("closeSourceModal()")
    page.wait_for_timeout(300)
    
    # Open Presenter mode and jump to slide 11
    page.evaluate("openPresenterMode()")
    page.wait_for_timeout(500)
    page.evaluate("renderSlide(10)") # 0-indexed slide 11
    page.wait_for_timeout(500)
    page.screenshot(path='dashboard_slide11_advisory.png')
    
    browser.close()
    print('All screenshots captured successfully.')

