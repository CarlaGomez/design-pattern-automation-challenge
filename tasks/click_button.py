# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ClickButton:
    def __init__(self, button_name):
        self.button_name = button_name

    def perform_as(self, actor):
        actor.page.get_by_role("button", name=self.button_name).click()
