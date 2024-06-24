from base_reg import Registration
from playwright.sync_api import Page, Playwright, expect, sync_playwright


def test_registration(playwright):
    registration = Registration(playwright)
    registration.set_up()
    registration.press_sign_up_button()
    registration.browser.close()
