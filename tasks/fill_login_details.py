# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.enter_text import EnterText


class FillLoginDetails:
    def __init__(self, login_name, password):
        self.login_name = login_name
        self.password = password

    def perform_as(self, actor):
        actor.attempts_to(
            EnterText.into("#AccountFrm_loginname")(self.login_name),
            EnterText.into("#AccountFrm_password")(self.password),
            EnterText.into("#AccountFrm_confirm")(self.password),
        )
