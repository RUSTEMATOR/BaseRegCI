import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tombriches.com/")
    time.sleep(7)
    page.locator("path").first.click()
    time.sleep(7)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)