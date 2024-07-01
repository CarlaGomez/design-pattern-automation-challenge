# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from playwright.sync_api import expect


class AssertTextVisible:
    def __init__(self, text, selector=None):
        self.text = text
        self.selector = selector

    def perform_as(self, actor):
        if self.selector:
            locator = actor.page.locator(f"{self.selector}:has-text('{self.text}')")
        else:
            locator = actor.page.locator(f"text={self.text}")

        expect(locator).to_be_visible()
