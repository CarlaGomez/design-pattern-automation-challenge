# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class AssertTextVisible:
    def __init__(self, text, class_name=None):
        self.text = text
        self.class_name = class_name

    def perform_as(self, actor):
        if self.class_name:
            assert actor.page.locator(f"{self.class_name}:has-text('{self.text}')").is_visible()
        else:
            assert actor.page.locator(f"text={self.text}").is_visible()
            