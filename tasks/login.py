# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.enter_text import EnterText
from interactions.click_element import ClickElement


class Login:
    def __init__(self, login_name, login_password):
        self.login_name = login_name
        self.login_password = login_password

    def perform_as(self, actor):
        actor.attempts_to(
            EnterText.into("#loginFrm_loginname")(self.login_name),
            EnterText.into("#loginFrm_password")(self.login_password),
            ClickElement("button.btn.btn-orange.pull-right:has-text('Login')"),
        )
