# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class AssertTextVisible:
    def __init__(self, text):
        self.text = text

    def perform_as(self, actor):
        assert actor.page.locator(f"text={self.text}").is_visible()
