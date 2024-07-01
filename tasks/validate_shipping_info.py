# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateShippingInfo:
    def __init__(self, subtotal, total):
        self.subtotal = subtotal
        self.total = total

    def perform_as(self, actor):
        actor.attempts_to(
            AssertTextVisible(
                self.subtotal,
                "#totals_table > tbody > tr:nth-child(1) > td > span.bold",
            )
        )
        actor.attempts_to(AssertTextVisible(self.total))
