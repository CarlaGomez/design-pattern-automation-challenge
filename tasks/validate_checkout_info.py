# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateCheckoutInfo:
    def __init__(self, page_name, item_name, subtotal, total):
        self.page_name = page_name
        self.item_name = item_name
        self.subtotal = subtotal
        self.total = total

    def perform_as(self, actor):
        actor.attempts_to(AssertTextVisible(self.page_name, "span.maintext"))
        actor.attempts_to(AssertTextVisible(self.item_name, "a.checkout_heading"))
        actor.attempts_to(AssertTextVisible(self.subtotal, "span.bold"))
        actor.attempts_to(AssertTextVisible(self.total, "span.bold"))
