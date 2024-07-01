# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateItemPrice:
    def __init__(self, price):
        self.price = price

    def perform_as(self, actor):
        actor.attempts_to(AssertTextVisible(self.price))
