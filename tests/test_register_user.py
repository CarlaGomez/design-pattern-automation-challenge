# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import os
import pytest
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
from tasks.verify_message import VerifyMessage

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")

address_data = [
    ("223", "3630", "76876"),
]

def test_register_user():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        actor = Authenticate(context)
        actor.attempts_to(
            NavigateTo("https://automationteststore.com/index.php?rt=account/login"),
            FillPersonalDetails("John", "Doe", "john.doe@example.com"),
            FillAddress("US", "California", "90001", "123 Street"),
            FillLoginDetails(login_name, login_password),
            FillNewsletter(),
            CheckPrivacyPolicy(),
            RegisterUser(),
            VerifyMessage("Your Account Has Been Created!")
        )
        context.close()
        browser.close()
