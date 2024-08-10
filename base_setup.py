from playwright.sync_api import Page, Playwright, expect
from page_elements import PageElementsGames
import time


class BaseSetUp(PageElementsGames):

    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=True,
                                                  proxy={
                                                      'server': 'http://138.197.150.103:8090',
                                                      'username': 'kbc',
                                                      'password': '347SP&Uwqt!2xZ7w',
                                                  })
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self._generated_email = None


    def handler(self):
        self.page.reload()
        time.sleep(5)


    def open_site(self):
        try:
            self.page.goto('https://tombriches.com/')

        except Exception as e:

            raise AssertionError from e

    def press_log_in_button(self):
        try:
            self.log_in_button.click()

        except Exception as e:

            raise AssertionError from e

    def enter_credentials(self):
        try:
            self.email_input.fill("samoilenkofluttershy@gmail.com")


            self.password_input.fill("193786Az()")


        except Exception as e:

            raise AssertionError from e

    def press_confirm_log_in_button(self):
        try:
            self.confirm_log_in_button.click()


            self.page.wait_for_selector("#depositPromocode")
            self.page.goto('https://tombriches.com/')
        except Exception as e:

            raise AssertionError from e

    def confirm_cookies(self):
        try:
            self.cookie_popup.click()

        except Exception as e:

            raise AssertionError from e

    def set_up(self):
        self.open_site()
        self.press_log_in_button()
        self.enter_credentials()
        self.press_confirm_log_in_button()
        self.confirm_cookies()

    def set_up_no_login(self):
        self.open_site()
