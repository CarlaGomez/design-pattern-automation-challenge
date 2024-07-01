# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidateItemsOnShoppingCart:
    def __init__(self, page_title, product, quantity):
        self.page_title = page_title
        self.product = product
        self.quantity = quantity

    def perform_as(self, actor):
        assert actor.page.locator(f"text={self.page_title}").is_visible()
        assert actor.page.locator(f"role=cell[name='{self.product}']").is_visible()
        assert (
            actor.page.locator("#cart_quantity79")
            .locator(f"text={self.quantity}")
            .is_visible()
        )
