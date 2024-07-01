# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class NavigateTo:
    def __init__(self, url):
        self.url = url

    def perform_as(self, actor):
        actor.page.goto(self.url)
