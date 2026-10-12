import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def verify_tab11():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1600, 'height': 1200})
        page = await context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: console_errors.append(str(err)))

        file_url = f"file:///{os.path.abspath('TMG_Forensic_Due_Diligence_Dashboard.html').replace(os.sep, '/')}"
        print(f"Loading {file_url}...")
        await page.goto(file_url, wait_until="networkidle")

        # Switch to tab-stakeholders
        print("Switching to tab-stakeholders...")
        await page.evaluate("switchTab('stakeholders')")
        await page.wait_for_timeout(2000)

        # Check DOM elements
        map_rendered = await page.evaluate("document.querySelector('#tmg-leaflet-map .leaflet-pane') !== null")
        companies_count = await page.evaluate("document.querySelectorAll('#companies-table-body tr').length")
        teams_count = await page.evaluate("document.querySelectorAll('#teams-cards-grid > div').length")
        swot_strengths = await page.evaluate("document.querySelectorAll('#swot-strengths-container > div').length")
        
        print(f"Leaflet Map Rendered: {map_rendered}")
        print(f"Companies Rendered in Table: {companies_count}")
        print(f"Teams Rendered in Grid: {teams_count}")
        print(f"SWOT Strengths Count: {swot_strengths}")

        # Capture screenshots
        os.makedirs("test_screenshots", exist_ok=True)
        await page.screenshot(path="test_screenshots/tab11_stakeholders_overview.png", full_page=False)
        print("Captured test_screenshots/tab11_stakeholders_overview.png")

        # Scroll to companies table and screenshot
        companies_el = page.locator("#companies-table-dom")
        if await companies_el.count() > 0:
            await page.evaluate("document.querySelector('#tab-stakeholders').scrollIntoView()")
            await page.screenshot(path="test_screenshots/tab11_companies_section.png", full_page=False)

        # Click TOWS view button and check
        print("Testing TOWS toggle...")
        await page.evaluate("switchSwotView('tows')")
        await page.wait_for_timeout(500)
        tows_so_count = await page.evaluate("document.querySelectorAll('#tows-so-container > div').length")
        print(f"TOWS SO Strategies count: {tows_so_count}")

        # Test project filter click (SouthMED)
        print("Testing Project Filter (SouthMED)...")
        await page.evaluate("filterMapByProject('southmed')")
        await page.wait_for_timeout(500)
        filtered_companies = await page.evaluate("document.querySelectorAll('#companies-table-body tr').length")
        print(f"Companies after filtering to SouthMED: {filtered_companies}")

        # Reset filter
        await page.evaluate("resetProjectFilter()")
        await page.wait_for_timeout(500)
        reset_companies = await page.evaluate("document.querySelectorAll('#companies-table-body tr').length")
        print(f"Companies after reset: {reset_companies}")

        print("\nConsole Errors encountered during execution:")
        print(console_errors if console_errors else "None! Zero errors.")

        await browser.close()

asyncio.run(verify_tab11())
