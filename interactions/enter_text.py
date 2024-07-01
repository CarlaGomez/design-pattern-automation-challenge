# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class EnterText:
    def __init__(self, selector, text):
        self.selector = selector
        self.text = text

    @staticmethod
    def into(selector):
        return lambda text: EnterText(selector, text)

    def perform_as(self, actor):
        actor.page.fill(self.selector, self.text)
