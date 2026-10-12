import asyncio
import os
from playwright.async_api import async_playwright

async def capture_sections():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1600, 'height': 1200})
        page = await context.new_page()

        file_url = f"file:///{os.path.abspath('TMG_Forensic_Due_Diligence_Dashboard.html').replace(os.sep, '/')}"
        await page.goto(file_url, wait_until="networkidle")
        await page.evaluate("switchTab('stakeholders')")
        await page.wait_for_timeout(1000)

        # Screenshot Companies Table
        await page.locator("#companies-table-dom").scroll_into_view_if_needed()
        await page.screenshot(path="test_screenshots/tab11_companies_table.png")

        # Screenshot Teams Grid
        await page.locator("#teams-cards-grid").scroll_into_view_if_needed()
        await page.screenshot(path="test_screenshots/tab11_teams_grid.png")

        # Screenshot SWOT / TOWS
        await page.locator("#swot-quadrants-view").scroll_into_view_if_needed()
        await page.screenshot(path="test_screenshots/tab11_swot_matrix.png")

        # Click TOWS
        await page.evaluate("switchSwotView('tows')")
        await page.wait_for_timeout(300)
        await page.locator("#tows-matrix-view").scroll_into_view_if_needed()
        await page.screenshot(path="test_screenshots/tab11_tows_matrix.png")

        await browser.close()
        print("Captured all section screenshots!")

asyncio.run(capture_sections())
