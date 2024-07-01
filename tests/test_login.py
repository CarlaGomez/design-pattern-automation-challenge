# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from tasks.authenticate import Authenticate
from tasks.navigate_to import NavigateTo
from tasks.fill_login_details import FillLoginDetails
from tasks.verify_message import VerifyMessage

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")

def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        actor = Authenticate(context)
        actor.attempts_to(
            NavigateTo("https://automationteststore.com/index.php?rt=account/login"),
            FillLoginDetails(login_name, login_password),
            VerifyMessage("Welcome back John")
        )
        context.close()
        browser.close()
