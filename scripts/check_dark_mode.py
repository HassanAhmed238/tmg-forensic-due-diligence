import asyncio
import os
from playwright.async_api import async_playwright

async def check_dark():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1600, 'height': 1200})
        file_url = f"file:///{os.path.abspath('TMG_Forensic_Due_Diligence_Dashboard.html').replace(os.sep, '/')}"
        await page.goto(file_url, wait_until='networkidle')
        await page.evaluate("switchTab('stakeholders')")
        await page.evaluate("setTheme('dark')")
        await page.wait_for_timeout(1000)
        await page.screenshot(path='test_screenshots/tab11_dark_mode.png')
        await browser.close()
        print('Captured test_screenshots/tab11_dark_mode.png')

asyncio.run(check_dark())
