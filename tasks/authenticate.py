# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.fill_form import FillForm
from interactions.click import Click


class Authenticate:
    def __init__(self, login_name, login_password):
        self.login_name = login_name
        self.login_password = login_password

    def perform_as(self, actor):
        actor.attempts_to(
            FillForm("#loginFrm_loginname", self.login_name),
            FillForm("#loginFrm_password", self.login_password),
            Click("button[name=' Login']"),
        )
