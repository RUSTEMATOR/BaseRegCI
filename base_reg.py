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


class Registration(BaseSetUp, PageElementsTabs, Generator):

    @property
    def generated_email(self):
        if self._generated_email is None:  # Generate and store the email if it hasn't been generated yet
            self._generated_email = self.generate_random_email()
        return self._generated_email
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
            self.check_18_years()



    def check_18_years(self):
        checkbox = self.page.locator("#is18-checkbox")
        try:
            checkbox.click()

        except Exception as e:

            raise AssertionError from e
        finally:
            self.fill_reg_info()


    def fill_reg_info(self):
        email_field = self.page.get_by_placeholder("E-mail")
        password_field = self.page.get_by_placeholder("Password")
        try:
            email_field.hover()
            time.sleep(1)
            email_field.click()
            time.sleep(1)
            email_field.fill(self.generated_email)
            time.sleep(1)
            password_field.hover()
            time.sleep(1)
            password_field.click()
            time.sleep(1)
            password_field.fill("193786Az()")
        except Exception as e:

            raise AssertionError from e
        finally:
            self.press_final_sign_up_button()

    def press_final_sign_up_button(self):
        sign_up_button = self.page.locator("form").get_by_role("button", name="Sign up")
        try:
            sign_up_button.hover()
            time.sleep(1)
            sign_up_button.click()

        except Exception as e:

            raise AssertionError from e
        finally:
            expect(self.page.locator('.deposit-card')).to_be_visible(timeout=90000)
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
        welcome_message = self.page.locator(".text-map_welcome")
        expect(welcome_message).to_contain_text(f'Welcome, {self.generated_email}')
