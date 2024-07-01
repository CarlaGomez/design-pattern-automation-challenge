# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class FillLoginDetails:
    def __init__(self, login_name, password):
        self.login_name = login_name
        self.password = password

    def perform_as(self, actor):
        actor.page.fill("#AccountFrm_loginname", self.login_name)
        actor.page.fill("#AccountFrm_password", self.password)
        actor.page.fill("#AccountFrm_confirm", self.password)
