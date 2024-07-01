# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class Authenticate:
    def __init__(self, login_name, password):
        self.login_name = login_name
        self.password = password

    def perform_as(self, actor):
        actor.page.fill("#loginFrm_loginname", self.login_name)
        actor.page.fill("#loginFrm_password", self.password)
        actor.page.get_by_role("button", name=" Login").click()
