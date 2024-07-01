# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidatePurchase:
    def __init__(self, order_confirmation_message):
        self.order_confirmation_message = order_confirmation_message

    def perform_as(self, actor):
        actor.attempts_to(AssertTextVisible(self.order_confirmation_message))
