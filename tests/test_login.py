"""
This module contains the test case for logging in a user.
"""

import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from actors.actor import Actor
from tasks.navigate_to import NavigateTo
from tasks.authenticate import Authenticate
from tasks.verify_message import VerifyMessage

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")

def test_login(page: Page) -> None:
    actor = Actor("User", page)
    
    actor.attempts_to(
        NavigateTo(f"{os.getenv('BASE_URL')}/index.php?rt=account/login"),
        Authenticate(login_name, login_password),
        VerifyMessage("Welcome back John", is_visible=True)
    )
