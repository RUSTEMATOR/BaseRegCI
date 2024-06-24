import time
import re
from base_setup import BaseSetUp
from playwright.sync_api import Playwright, expect, sync_playwright
from page_elements import PageElementsGames, PageElementsTabs


class Generator():
    @staticmethod
    # Function to generate a random email
    def generate_random_email():
        import random
        import string
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        automaton = "automaton_"
        return f'{automaton}{random_word}{random_numbers}@kingbilly.xyz'

    @property
    def generated_email(self):
        return self.generate_random_email()


class Registration(BaseSetUp, PageElementsTabs, Generator):
    def set_up(self):
        try:
            super().set_up_no_login()


        except Exception as e:

            raise AssertionError from e

    def press_sign_up_button(self):
        sign_up_button = self.page.get_by_role("button", name="Sign up")
        try:
            sign_up_button.click()

        except Exception as e:

            raise AssertionError from e
        finally:
            self.check_transf_to_login()

    def check_transf_to_login(self):
        login_tab = self.page.locator("p").filter(has_text="Log in")

        try:
            login_tab.click()


        except Exception as e:

            raise AssertionError from e
        finally:
            self.back_to_registration()

    def back_to_registration(self):
        reg_tab = self.page.locator("p").filter(has_text=re.compile(r"^Sign up$"))

        try:
            reg_tab.click()


        except Exception as e:

            raise AssertionError from e

        finally:
            self.fill_reg_info()

    def fill_reg_info(self):
        email_field = self.page.get_by_placeholder("E-mail")
        password_field = self.page.get_by_placeholder("Password")
        try:
            email_field.click()

            self.fill_email_field(email_field)
            password_field.click()

            self.fill_password_field(password_field)
        except Exception as e:

            raise AssertionError from e
        finally:
            self.check_18_years()

    def fill_email_field(self, email_field):
        email_field.fill(self.generated_email)

    def fill_password_field(self, password_field):
        password_field.fill("193786Az()")

    def check_18_years(self):
        checkbox = self.page.locator("#is18-checkbox")
        try:
            checkbox.click()

        except Exception as e:

            raise AssertionError from e
        finally:
            self.press_final_sign_up_button()

    def press_final_sign_up_button(self):
        sign_up_button = self.page.locator("form").get_by_role("button", name="Sign up")
        try:
            sign_up_button.click()

        except Exception as e:

            raise AssertionError from e
        finally:
            time.sleep(10)
            self.refresh_page()

    def refresh_page(self):
        try:
            self.page.reload()
        finally:
            self.enter_account()

    def enter_account(self):
        account_button = self.page.get_by_role("button", name="Account")

        try:
            account_button.click()


        except Exception as e:

            raise AssertionError from e

        finally:
            self.check_if_registered()

    def check_if_registered(self):
        account_button = self.page.get_by_role("button", name="Account")
        welcome_message = self.page.locator(".text-map_welcome")
        account_button.click()
        expect(welcome_message).to_contain_text(f'Welcome, {self.generated_email}')
