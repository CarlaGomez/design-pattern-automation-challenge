# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class RegisterUser:
    def perform_as(self, actor):
        actor.page.locator("#AccountFrm div").filter(
            has_text="Continue").nth(2).click()
