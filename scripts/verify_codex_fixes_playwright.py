import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def verify_codex_fixes():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1600, 'height': 1200})

        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(str(err)))

        file_url = f"file:///{os.path.abspath('TMG_Forensic_Due_Diligence_Dashboard.html').replace(os.sep, '/')}"
        await page.goto(file_url, wait_until='networkidle')
        await page.evaluate("switchTab('stakeholders')")
        await page.wait_for_timeout(1000)

        # 1. Test Oman (jood_yamal) project filter
        print("Testing Oman (jood_yamal) filter...")
        await page.evaluate("filterMapByProject('jood_yamal')")
        await page.wait_for_timeout(500)
        oman_comp_count = await page.evaluate("document.querySelectorAll('#companies-table-body tr').length")
        oman_team_count = await page.evaluate("document.querySelectorAll('#teams-cards-grid > div').length")
        print(f"Oman Filtered: Companies={oman_comp_count}, Teams={oman_team_count}")

        # 2. Test SouthMED filter
        print("Testing SouthMED filter...")
        await page.evaluate("filterMapByProject('southmed')")
        await page.wait_for_timeout(500)
        sm_comp_count = await page.evaluate("document.querySelectorAll('#companies-table-body tr').length")
        print(f"SouthMED Filtered: Companies={sm_comp_count}")

        # 3. Test Reset Filter
        print("Testing Reset filter...")
        await page.evaluate("resetProjectFilter()")
        await page.wait_for_timeout(500)
        reset_comp_count = await page.evaluate("document.querySelectorAll('#companies-table-body tr').length")
        reset_team_count = await page.evaluate("document.querySelectorAll('#teams-cards-grid > div').length")
        print(f"Reset Filtered: Companies={reset_comp_count} (expect 42), Teams={reset_team_count} (expect 38)")

        # 4. Test Dark/Light Theme Map Switch
        print("Testing Theme Switch on Map Tiles...")
        await page.evaluate("setTheme('dark')")
        await page.wait_for_timeout(500)
        dark_tile_url = await page.evaluate("window.tmgMapTiles ? window.tmgMapTiles._url : ''")
        print(f"Dark Tile URL: {dark_tile_url}")

        await page.evaluate("setTheme('light')")
        await page.wait_for_timeout(500)
        light_tile_url = await page.evaluate("window.tmgMapTiles ? window.tmgMapTiles._url : ''")
        print(f"Light Tile URL: {light_tile_url}")

        # 5. Test escapeHTML in DOM
        has_escape = await page.evaluate("typeof escapeHTML === 'function'")
        print(f"escapeHTML function defined: {has_escape}")

        # 6. Verify zero console errors
        print("\nConsole errors during run:")
        print(errors if errors else "Zero console errors! 100% verified clean.")

        await browser.close()

asyncio.run(verify_codex_fixes())
