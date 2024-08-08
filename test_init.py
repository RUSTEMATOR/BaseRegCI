from base_reg import Registration
from playwright.sync_api import Page, Playwright, expect, sync_playwright


def test_registration(playwright):
    registration = Registration(playwright)

    registration.page.add_locator_handler(registration.page.locator('xpath=//*[@id="Tombriches"]/div[2]/div/div/div/div/button'),
                                   registration.handler)

    registration.set_up_no_login()
    registration.press_sign_up_button()
    registration.check_18_years()
    registration.fill_reg_info()
    registration.press_final_sign_up_button()

    # registration.refresh_page()
    registration.enter_account()
    registration.check_if_registered()
    registration.browser.close()
