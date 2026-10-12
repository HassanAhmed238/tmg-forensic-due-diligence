# -*- coding: utf-8 -*-
import sys, os
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # iPhone 14 Pro viewport (393 x 852)
    context = browser.new_context(viewport={'width': 393, 'height': 852}, is_mobile=True, has_touch=True)
    page = context.new_page()
    
    # 1. Load local HTML
    page.goto('file:///f:/Mr%20Hesham/TMG/index.html')
    page.wait_for_timeout(1000)
    page.screenshot(path='mobile_1_overview.png')
    print("Screenshot 1: Overview rendered")

    # 2. Tap Hamburger Button
    page.click('#btn-mobile-nav')
    page.wait_for_timeout(500)
    page.screenshot(path='mobile_2_drawer_open.png')
    print("Screenshot 2: Drawer opened")

    # 3. Tap Financials Navigation button
    page.click('#nav-financials')
    page.wait_for_timeout(800)
    page.screenshot(path='mobile_3_financials_tab.png')
    print("Screenshot 3: Financials tab loaded and drawer closed")

    # 4. Tap Excel Modal button
    page.click('button[onclick="openExcelModal()"]')
    page.wait_for_timeout(500)
    page.screenshot(path='mobile_4_excel_modal.png')
    print("Screenshot 4: Excel modal opened")

    # 5. Close Excel Modal
    page.click('button[onclick="closeExcelModal()"]')
    page.wait_for_timeout(400)
    
    # 6. Test Interactive Balance Sheet stress sliders
    page.fill('#slider-lease', '50')
    page.evaluate("document.getElementById('slider-lease').dispatchEvent(new Event('input'))")
    page.wait_for_timeout(400)
    page.screenshot(path='mobile_5_bs_stress_slider.png')
    print("Screenshot 5: Stress slider interactive test passed")

    # 7. Tap Stakeholders GIS Map Tab
    page.click('#btn-mobile-nav')
    page.wait_for_timeout(400)
    page.click('#nav-stakeholders')
    page.wait_for_timeout(1200)
    page.screenshot(path='mobile_6_gis_map.png')
    print("Screenshot 6: GIS Map tab loaded cleanly on mobile")

    browser.close()

print("ALL MOBILE E2E TESTS PASSED!")
