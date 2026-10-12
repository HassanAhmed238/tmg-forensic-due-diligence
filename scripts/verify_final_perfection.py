import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def verify_everything():
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

        # Test EN language switch
        print("Testing English language switch...")
        await page.evaluate("setLanguage('en')")
        await page.wait_for_timeout(1000)

        en_title = await page.evaluate("document.getElementById('stakeholders-header-title').textContent")
        print(f"EN Header Title: {en_title}")

        await page.screenshot(path="test_screenshots/tab11_en_mode.png")

        # Test Arabic language switch back
        print("Testing Arabic language switch back...")
        await page.evaluate("setLanguage('ar')")
        await page.wait_for_timeout(1000)

        ar_title = await page.evaluate("document.getElementById('stakeholders-header-title').textContent")
        print(f"AR Header Title: {ar_title}")

        # Check export buttons presence
        btn_exp_c = await page.evaluate("document.getElementById('btn-export-companies') !== null")
        btn_exp_t = await page.evaluate("document.getElementById('btn-export-teams') !== null")
        print(f"Export Buttons Present: Companies={btn_exp_c}, Teams={btn_exp_t}")

        # Verify console errors
        print("\nConsole errors:")
        print(errors if errors else "Zero console errors! 100% clean execution.")

        await browser.close()

asyncio.run(verify_everything())
