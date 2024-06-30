"""
This module contains the test case for registering a user.
"""

import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from faker import Faker
from actors.actor import Actor
from tasks.navigate_to import NavigateTo
from tasks.fill_personal_details import FillPersonalDetails
from tasks.fill_address import FillAddress
from tasks.fill_login_details import FillLoginDetails
from tasks.fill_newsletter import FillNewsletter
from tasks.check_privacy_policy import CheckPrivacyPolicy
from tasks.register_user import RegisterUser
from tasks.click_button import ClickButton
from tasks.verify_message import VerifyMessage

load_dotenv()

login_password = os.getenv("LOGIN_PASSWORD")

address_data = [
    ("223", "3630", "76876"),
]

@pytest.mark.parametrize("country_id, region_id, zip_code", address_data)
def test_register_user(page: Page, country_id, region_id, zip_code) -> None:
    actor = Actor("User", page)
    fake = Faker()
    
    actor.attempts_to(
        NavigateTo(f"{os.getenv('BASE_URL')}/index.php?rt=account/login"),
        ClickButton(" Continue"),
        FillPersonalDetails(
            fake.first_name(),
            fake.last_name(),
            fake.email(),
            fake.phone_number(),
            fake.phone_number()
        ),
        FillAddress(
            fake.company(),
            fake.street_address(),
            fake.address(),
            country_id,
            fake.city(),
            region_id,
            zip_code
        ),
        FillLoginDetails(fake.user_name(), login_password),
        FillNewsletter("Yes"),
        CheckPrivacyPolicy(),
        RegisterUser(),
        VerifyMessage("Your Account Has Been Created!"),
        ClickButton(" Continue")
    )
