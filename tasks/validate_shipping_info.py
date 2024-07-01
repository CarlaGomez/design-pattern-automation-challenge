# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidateShippingInfo:
    def __init__(self, subtotal, total):
        self.subtotal = subtotal
        self.total = total

    def perform_as(self, actor):
        assert actor.page.locator(
            f"role=row[name='Sub-Total: {self.subtotal}']"
        ).is_visible()
        assert actor.page.locator(f"role=cell[name='{self.total}']").is_visible()
