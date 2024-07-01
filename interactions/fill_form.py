# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class FillForm:
    def __init__(self, selector, value):
        self.selector = selector
        self.value = value

    def perform_as(self, actor):
        actor.page.locator(self.selector).fill(self.value)
