# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        console_errors = []
        page.on('console', lambda msg: console_errors.append(f'[{msg.type}] {msg.text}') if msg.type == 'error' else None)
        page.on('pageerror', lambda err: console_errors.append(f'[UNCAUGHT] {err}'))
        
        await page.goto('file:///F:/Mr%20Hesham/TMG/TMG_Forensic_Due_Diligence_Dashboard.html')
        await page.wait_for_timeout(2000)
        
        # Click on Tab 5: Contractors
        await page.evaluate("switchTab('contractors')")
        await page.wait_for_timeout(1000)
        await page.screenshot(path=r'F:\Mr Hesham\TMG\dashboard_tab5_contractors.png', full_page=False)
        
        # Click on Tab 8: Sentiment
        await page.evaluate("switchTab('sentiment')")
        await page.wait_for_timeout(1000)
        await page.screenshot(path=r'F:\Mr Hesham\TMG\dashboard_tab8_sentiment.png', full_page=False)
        
        print('Screenshots captured for Tab 5 and Tab 8 successfully.')
        print('Console errors count:', len(console_errors))
        for err in console_errors:
            print('  ERROR:', err)
        await browser.close()

asyncio.run(main())
