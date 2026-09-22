import asyncio
from playwright.async_api import async_playwright
import csv
from datetime import datetime

def log_result(test_name, result):
    with open("qa_results.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([test_name, result, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()

    await page.goto("http://localhost:8501")

    # Test 1: Page Title
    title = await page.title()
    if "Streamlit" in title:
        print("✅ Page title loaded")
        log_result("Page Title", "Pass")
    else:
        print("❌ Page title failed")
        log_result("Page Title", "Fail")

    # Test 2: Applications Table
    try:
        await page.wait_for_selector("div[data-testid='stDataFrame']", timeout=10000)
        print("✅ Applications table loaded")
        log_result("Applications Table", "Pass")
    except:
        print("❌ Applications table failed")
        log_result("Applications Table", "Fail")

    # Test 3: Chart
    try:
        await page.wait_for_selector("div[data-testid*='Chart']", timeout=15000)
        print("✅ Chart loaded")
        log_result("Applications Chart", "Pass")
    except:
        print("❌ Chart failed")
        log_result("Applications Chart", "Fail")

    await page.screenshot(path="dashboard_test.png")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
