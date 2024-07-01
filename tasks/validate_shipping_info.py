# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidateShippingInfo:
    def __init__(self, subtotal, total):
        self.subtotal = subtotal
        self.total = total

    def perform_as(self, actor):
        assert (
            actor.page.get_by_role("row", name=f"Sub-Total: ${self.subtotal}")
            .get_by_role("cell", name=self.subtotal)
            .nth(4)
        )
        assert actor.page.get_by_role("cell", name=self.total).nth(1)
