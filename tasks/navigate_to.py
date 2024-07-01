# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class NavigateTo:
    def perform_as(self, actor):
        actor.page.goto("https://automationteststore.com/index.php?rt=account/login")
