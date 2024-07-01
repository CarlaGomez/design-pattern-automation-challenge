# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import Page
from actors.actor import Actor
from tasks.register_user import RegisterUser
from tasks.login import Login
from tasks.logout import Logout
from tasks.navigate_to import NavigateTo
from tasks.validate_user_logged_in import ValidateUserLoggedIn
from tasks.validate_user_logged_out import ValidateUserLoggedOut

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")

address_data = [("223", "3630", "76876")]


@pytest.mark.parametrize("country_id, region_id, zip_code", address_data)
def test_register_user(page: Page, country_id, region_id, zip_code) -> None:
    actor = Actor("Test User", page)
    actor.attempts_to(
        NavigateTo(), RegisterUser(country_id, region_id, zip_code, login_password)
    )


def test_login(page: Page) -> None:
    actor = Actor("Test User", page)
    actor.attempts_to(
        NavigateTo(), Login(login_name, login_password), ValidateUserLoggedIn(True)
    )


def test_logout(page: Page) -> None:
    actor = Actor("Test User", page)
    actor.attempts_to(
        NavigateTo(),
        Login(login_name, login_password),
        ValidateUserLoggedIn(True),
        Logout(),
        ValidateUserLoggedIn(False),
        ValidateUserLoggedOut(True),
    )
