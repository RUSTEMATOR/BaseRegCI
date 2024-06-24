import re
from playwright.sync_api import Page



class PageElementsGames():

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def log_in_button(self):
        return self.page.get_by_role("button", name="Log in")

    @property
    def email_input(self):
        return self.page.get_by_placeholder("E-mail")

    @property
    def password_input(self):
        return self.page.get_by_placeholder("Password")

    @property
    def confirm_log_in_button(self):
        return self.page.locator("xpath=//button[contains(@class, 'min-w-full') and contains(text(),'Log in')]")

    @property
    def cookie_popup(self):
        return self.page.get_by_role("button", name="ok")

    @property
    def casino_games_side(self):
        return self.page.get_by_text("Casino Games", exact=True)

    @property
    def top_online_casino_games(self):
        return self.page.get_by_label("Top", exact=True)

    @property
    def new_casino_games(self):
        return self.page.get_by_label("New", exact=True)

    @property
    def slot_casino_games(self):
        return self.page.get_by_label("Slots", exact=True)

    @property
    def megaways_casino_games(self):
        return self.page.get_by_label("Megaways", exact=True)

    @property
    def crash_casino_games(self):
        return self.page.get_by_label("Crash", exact=True)

    @property
    def fruit_casino_games(self):
        return self.page.get_by_label("Fruits", exact=True)

    @property
    def bonus_games(self):
        return self.page.get_by_label("Bonus games")

    @property
    def game_card_first(self):
        return self.page.locator(
            "//div[contains (@class, 'flex flex-col rounded-b-[10px] bg-gc_bg_card p-2 text-center') ]").first

    @property
    def game_card_second(self):
        return self.page.locator(
            "xpath=//div//img[contains(@class, 'relative z-[2] aspect-[29/40] h-full w-full rounded-t-lg')]").first

    @property
    def game_card_third(self):
        return self.page.locator("xpath=/html/body/div[2]/div/main/div/div/div[4]/div[1]/div[3]")

    @property
    def mini_jackpot_game(self):
        return self.page.locator(
            "xpath=//div[contains(@class, 'game-card relative z-0 flex h-auto flex-col justify-end')][1]")

    # ________________________________________________________________

    @property
    def live_games_dropdown(self):
        return self.page.get_by_text("Live Games", exact=True)

    @property
    def blackjack_games(self):
        return self.page.get_by_label("Blackjack")

    @property
    def bj_league_games(self):
        return self.page.get_by_label("Bj League")

    @property
    def baccarat_games(self):
        return self.page.get_by_label("Baccarat", exact=True)

    @property
    def poker_games(self):
        return self.page.get_by_label("Poker", exact=True)

    @property
    def roulette_games(self):
        return self.page.get_by_label("Roulette", exact=True)

    @property
    def live_dealer_games(self):
        return self.page.get_by_label("Live Dealer Shows")

    @property
    def jackpot_dropdown(self):
        return self.page.get_by_text("Jackpot Games")

    @property
    def max_games(self):
        return self.page.locator(
            "xpath=//div//a[contains(@class, 'flex w-full items-center rounded-lg bg-category_bg py-4 pl-3 transition-all hover:text-text_primary_sidebar [&_path]:hover:fill-text_primary_sidebar text-text_secondary_sidebar [&_path]:fill-text_secondary_sidebar') and @aria-label='Max']")

    @property
    def mid_games(self):
        return self.page.get_by_label("Mid", exact=True)

    @property
    def mini_games(self):
        return self.page.get_by_label("Mini", exact=True)


class PageElementsTabs(PageElementsGames):

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def all_games_btn(self):
        return self.page.get_by_label("All games")

    @property
    def jackpots_tab(self):
        return self.page.get_by_label("Jackpots", exact=True)

    @property
    def live_tab(self):
        return self.page.get_by_label("Live")

    @property
    def promotions_tab(self):
        return self.page.get_by_label("Promotions")

    @property
    def tournaments_tab(self):
        return self.page.get_by_label("Tournaments")

    @property
    def loyalty_tab(self):
        return self.page.get_by_label("Loyalty program")

    @property
    def support_iframe(self):
        return self.page.get_by_text("Support", exact=True)

    @property
    def game_card_first_jp(self):
        return self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[2]/div[1]/div/div[1]/div[1]/img')

    @property
    def game_card_second_jp(self):
        return self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[2]/div[2]/div/div[1]/div[1]/img')

    @property
    def game_card_third_jp(self):
        return self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[2]/div[3]/div/div[1]/div[1]/img')


class SearchFunctions(PageElementsTabs):

    def __init__(self, page: Page):
        super().__init__(page)

    def game_cards_visible_jp(self):
        return (self.game_card_first_jp.is_visible() and
                self.game_card_second_jp.is_visible() and
                self.game_card_third_jp.is_visible())

    def game_cards_visible(self):
        return (self.game_card_first.is_visible() or
                self.game_card_second.is_visible() or
                self.game_card_third.is_visible())

    def promo_banners_visible(self):
        return (self.page.get_by_text("Welcome Pack€/$2000 + 200").is_visible() and
                self.page.get_by_text("Cashback up to 15%Get from 10").is_visible() and
                self.page.get_by_text("1st Deposit Bonus100% up to").is_visible() and
                self.page.get_by_text("2nd Deposit Bonus50% up to").is_visible() and
                self.page.get_by_text("3rd Deposit Bonus25% up to").is_visible() and
                self.page.get_by_text("4th Deposit Bonus25% up to").is_visible() and
                self.page.get_by_text("Pharaoh’s Fortune Spins!Up to").is_visible() and
                self.page.get_by_text("Tomb Treasure!50% up to €/$").is_visible())

    def text_on_jackpot_pg_visible(self):
        return (self.page.get_by_text("How to win Jackpots?").is_visible() and
                self.page.get_by_text("Сhoose your game").is_visible() and
                self.page.get_by_text("all games qualify").is_visible() and
                self.page.get_by_text("Be online").is_visible() and
                self.page.get_by_text("just play your favorite games").is_visible() and
                self.page.get_by_text("Make a fortune").is_visible() and
                self.page.get_by_text("every bet can be the winning").is_visible() and
                self.page.get_by_text("How can I participate?").is_visible() and
                self.page.get_by_text("No extra effort required,").is_visible() and
                self.page.get_by_text("How do I get the jackpot?").is_visible() and
                self.page.get_by_text("Jackpots are drawn randomly").is_visible() and
                self.page.get_by_text("The winner is selected").is_visible() and
                self.page.get_by_text("mini: 500-1500 euro,").is_visible() and
                self.page.get_by_text("mid: 7000-10000 euro,").is_visible() and
                self.page.get_by_text("max: 35000-45000 euro.").is_visible() and
                self.page.get_by_text("You can keep track of Jackpot").is_visible() and
                self.page.get_by_text("How to increase the chances").is_visible() and
                self.page.get_by_text("The most important thing is").is_visible() and
                self.page.get_by_text("1) Confirm your email in").is_visible() and
                self.page.get_by_text("2) Install the TombRiches app").is_visible() and
                self.page.get_by_role("button", name="deposit & play").is_visible())

    def tournament_banners_visible(self):
        return (self.page.locator("div:nth-child(1) > .aspect-\\[40\\/29\\]").is_visible())
        # self.page.locator("div:nth-child(2) > .aspect-\\[40\\/29\\]").is_visible() and
        # self.page.locator("div:nth-child(3) > .aspect-\\[40\\/29\\]").is_visible())

    def loyalty_banners_visible(self):
        return (self.page.locator(".border-").first.is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(2)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(3)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(4)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(5)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(6)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(7)").is_visible() and
                self.page.locator(".max-w-\\[1100px\\] > div:nth-child(8)").is_visible() and
                self.page.locator('xpath=//*[@id="Tombriches"]/main/div/div/div[3]/div/div[9]').is_visible())


class BannersLocatorsZeroDep:
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def first_welcome_banner(self):
        return self.page.locator("xpath=//h3[contains(@class, 'text-mp_banner_vip_title') "
                                 "and contains(text(), 'Welcome Pack')]")

    @property
    def second_cashback_banner(self):
        return self.page.get_by_role("heading", name="CASHBACK UP TO 15%")

    @property
    def third_up_to_100_fs_banner(self):
        return self.page.get_by_role("heading", name="UP TO 100 FS")

    @property
    def fourth_tomb_treasure_banner(self):
        return self.page.get_by_role("heading", name="TOMB TREASURE!")

    @property
    def fifth_jackpot_banner(self):
        return self.page.get_by_role("button", name="get jackpot")

    @property
    def sixth_first_loyalty_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][6]")

    @property
    def seventh_winners_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][7]")

    @property
    def eighth_tournament_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][8]")

    @property
    def ninth_tournament_banner(self):
        return self.page.locator("xpath=//div[contains(@class, 'swiper-slide') and contains(@class, '!flex')][9]")


class GameSuitLocators:
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def search_field(self):
        return self.page.get_by_placeholder("Enter game name")

    @property
    def first_game_card(self):
        return self.page.locator("xpath=//div[contains(@class, 'game-card') and contains(@class, 'z-0')][1]").first

    @property
    def play_button(self):
        return self.page.locator(
            "xpath=//button[@title = 'play' and contains(@class, 'btn') and contains(@class, 'button-primary')][1]").first

    @property
    def ingame_close_button(self):
        return self.page.locator(
            "xpath=//button[@title='close' and contains(@class, 'btn button-secondary max-w-[150px]') and text()='close']")

    @property
    def sound_no_button(self):
        return self.page.locator("xpath=//div[contains(@class, 'button no')]")

    @property
    def spin_button(self):
        return self.page.frame_locator("#game-iframe").locator("#spinBtn")

    @property
    def warning(self):
        return self.page.frame_locator("#game-iframe").locator("xpath=//div[contains(@class, 'info-popup_message')]")

    @property
    def demo_button(self):
        return self.page.locator(".controls > button:nth-child(2)").first

    @property
    def balance_text(self):
        return self.page.locator("#depositPromocode").get_by_text("Balance")

    @property
    def seven_five_zero_button(self):
        return self.page.locator("xpath=//button[@title='40']")

    @property
    def providers_dropdown(self):
        return self.page.get_by_role("button", name="providers")


class MainSuiteLocators:

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def account_button(self):
        return self.page.get_by_role("button", name="Account")

    @property
    def verification_tab(self):
        return self.page.locator("div").filter(has_text=re.compile(r"^Verification$"))

    @property
    def title_uploading_documents(self):
        return self.page.get_by_text("Uploading of documents for")

    @property
    def title_proof_identity(self):
        return self.page.get_by_text("Proof of Identity:")

    @property
    def title_proof_address(self):
        return self.page.get_by_text("Proof of Address:")

    @property
    def title_proof_deposit(self):
        return self.page.get_by_text("Proof of Deposit:")

    @property
    def security_tab(self):
        return self.page.locator("div").filter(has_text=re.compile(r"^Security$"))

    @property
    def oldpass_input(self):
        return self.page.get_by_placeholder("Enter old password")

    @property
    def newpass_input(self):
        return self.page.locator("#password-input")

    @property
    def repeat_newpass(self):
        return self.page.locator("input[name=\"repeatPassword\"]")

    @property
    def main_tab(self):
        return self.page.get_by_text("Users_profile", exact=True)

    @property
    def first_name_input(self):
        return self.page.get_by_placeholder("First name")

    @property
    def last_name_input(self):
        return self.page.get_by_placeholder("Last name")

    @property
    def day_dropdown(self):
        return self.page.get_by_text("Day")

    @property
    def month_dropdown(self):
        return self.page.get_by_text("Month")

    @property
    def year_dropdown(self):
        return self.page.get_by_text("Year")

    @property
    def city_input(self):
        return self.page.get_by_placeholder("City")

    @property
    def postcode_input(self):
        return self.page.get_by_placeholder("Postcode")

    @property
    def full_address_house_number_input(self):
        return self.page.get_by_placeholder("Full address (house number,")

    @property
    def country_dropdown(self):
        return self.page.locator('input[name="country"]')

    @property
    def male_radio_button(self):
        return self.page.locator("div").filter(has_text=re.compile(r"^Male$")).get_by_role("radio")

    @property
    def female_radio_button(self):
        return self.page.locator("div").filter(has_text=re.compile(r"^Female$")).get_by_role("radio")

    @property
    def save_button(self):
        return self.page.get_by_role("button", name="Save")

    @property
    def confirmation_popup(self):
        return self.page.get_by_text("Profile data updated")

    @property
    def user_email(self):
        return self.page.get_by_text("samoilenkofluttershy@gmail.com")

    @property
    def coping_success_popup(self):
        return self.page.locator("div").filter(has_text="Mail has been copied").nth(3)

    @property
    def wrong_oldpassword_popup(self):
        return self.page.locator("div").filter(has_text="You have entered an incorrect").nth(3)

    @property
    def password_changed_success_popup(self):
        return self.page.locator("div").filter(has_text="Password changed successfully").nth(3)


class WalletLocators(MainSuiteLocators):

    @property
    def wallet_tab(self):
        return self.page.get_by_label("Wallet")

    @property
    def sixty_deposit_sum(self):
        return self.page.get_by_role("button", name="60")

    @property
    def deposit_tab(self):
        return self.page.locator(
            "xpath=//aside//div//button[@title='deposit' and contains(@class, 'btn') and contains(text(), 'deposit')][1]")

    @property
    def mastercard_button(self):
        return self.page.locator("//input[@type='radio' and @id='0' and @name='0' and @value='0']")

    @property
    def deposit_button(self):
        return self.page.locator(
            "xpath=//button[@title='deposit' and contains(@class, 'btn button-primary !min-w-full')]")

    @property
    def order_window(self):
        return self.page.locator("xpath=//div[contains(@class, 'order-info-compact')]")

    @property
    def withdrawal_tab(self):
        return self.page.get_by_text("Funds withdrawal")

    @property
    def withdrawal_mifinity_button(self):
        return self.page.locator(
            "//input[@type='radio' and contains(@class, 'absolute left-0 top-0 h-[100%] w-[100%] cursor-pointer opacity-0') and @id='3' and @name='3' and @value='3' ]")

    @property
    def account_input(self):
        return self.page.get_by_placeholder("Account")

    @property
    def amount_input(self):
        return self.page.get_by_placeholder("Amount")

    @property
    def send_button(self):
        return self.page.get_by_role("button", name="send")

    @property
    def transaction_history_tab(self):
        return self.page.get_by_text("Transaction history")

    @property
    def cancel_button(self):
        return self.page.get_by_role("button", name="Cancel")

    @property
    def date_from_input(self):
        return self.page.get_by_placeholder("Date From")

    @property
    def date_to_input(self):
        return self.page.get_by_placeholder("Date To")

    @property
    def error_message(self):
        return self.page.locator("div").filter(has_text="Your account has not been").nth(3)

    @property
    def withdrawal_skrill_button(self):
        return self.page.locator(
            "xpath=//input[@type='radio' and contains(@class, 'absolute left-0 top-0 h-[100%] w-[100%] cursor-pointer opacity-0') and @id='2' and @name='2' and @value='2' ]")
