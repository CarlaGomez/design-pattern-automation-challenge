# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidatePurchase:
    def __init__(self, order_confirmation_message):
        self.order_confirmation_message = order_confirmation_message

    def perform_as(self, actor):
        assert actor.page.locator(
            f"text={self.order_confirmation_message}"
        ).is_visible()
