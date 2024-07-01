# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class SelectOption:
    def __init__(self, selector, option):
        self.selector = selector
        self.option = option

    def perform_as(self, actor):
        actor.page.locator(self.selector).select_option(self.option)
