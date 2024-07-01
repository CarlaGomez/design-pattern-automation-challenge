# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class SelectOption:
    def __init__(self, selector, option):
        self.selector = selector
        self.option = option

    @staticmethod
    def from_dropdown(selector):
        return lambda option: SelectOption(selector, option)

    def perform_as(self, actor):
        actor.page.select_option(self.selector, self.option)
