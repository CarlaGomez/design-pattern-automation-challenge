# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from actors.actor import Actor
from tasks.navigate_to import NavigateTo
from tasks.authenticate import Authenticate
from tasks.logout import Logout
from tasks.verify_message import VerifyMessage

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")


def test_logout(page: Page) -> None:
    actor = Actor("User", page)

    actor.attempts_to(
        NavigateTo("https://automationteststore.com/index.php?rt=account/login"),
        Authenticate(login_name, login_password),
        VerifyMessage("Welcome back John"),
        Logout(),
        VerifyMessage("Welcome back John"),
        VerifyMessage("Account Logout"),
    )
