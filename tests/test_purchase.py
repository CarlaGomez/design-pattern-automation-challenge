# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from tasks.authenticate import Authenticate
from tasks.navigate_to import NavigateTo
from tasks.fill_personal_details import FillPersonalDetails
from tasks.fill_address import FillAddress
from tasks.fill_login_details import FillLoginDetails
from tasks.fill_newsletter import FillNewsletter
from tasks.check_privacy_policy import CheckPrivacyPolicy
from tasks.register_user import RegisterUser
from tasks.logout import Logout
from tasks.navigate_to import NavigateTo
from tasks.click_button import ClickButton
from tasks.verify_message import VerifyMessage

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")

def test_purchase():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        actor = Authenticate(context)
        actor.attempts_to(
            NavigateTo("https://automationteststore.com/index.php?rt=account/login"),
            FillPersonalDetails("John", "Doe", "john.doe@example.com", "1234567890", "9876543210"),
            FillAddress("Company Inc", "123 Street", "Apt 101", "US", "California", "90001"),
            FillLoginDetails(login_name, login_password),
            FillNewsletter(),
            CheckPrivacyPolicy(),
            RegisterUser(),
            NavigateTo("https://automationteststore.com/index.php?rt=checkout/cart"),
            ClickButton("Checkout"),
            FillAddress("Company Inc", "123 Street", "Apt 101", "US", "California", "90001"),
            ClickButton("Next Step"),
            ClickButton("Confirm Order"),
            VerifyMessage("Your Order Has Been Processed!"),
            Logout()
        )
        context.close()
        browser.close()

