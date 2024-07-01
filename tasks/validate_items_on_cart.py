# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidateItemsOnCart:
    def __init__(self, page_title, product, quantity):
        self.page_title = page_title
        self.product = product
        self.quantity = quantity

    def perform_as(self, actor):
        assert actor.page.get_by_text(self.page_title).is_visible()
        assert actor.page.get_by_role("cell", name=self.product).is_visible()
        assert actor.page.locator("#cart_quantity79").get_by_text(self.quantity)
