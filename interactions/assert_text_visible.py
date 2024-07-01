# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class AssertTextVisible:
    def __init__(self, text, class_name=None, timeout=5000):
        self.text = text
        self.class_name = class_name
        self.timeout = timeout

    def perform_as(self, actor):
        if self.class_name:
            locator = actor.page.locator(f"{self.class_name}:has-text('{self.text}')")
        else:
            locator = actor.page.locator(f"text={self.text}")

            locator.wait_for(state="visible", timeout=self.timeout)
        assert locator.is_visible()
