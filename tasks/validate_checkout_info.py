# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

class ValidateCheckoutInfo:
    def __init__(self, page_name, item_name, subtotal, total):
        self.page_name = page_name
        self.item_name = item_name
        self.subtotal = subtotal
        self.total = total

    def perform_as(self, actor):
        assert actor.page.get_by_text(self.page_name).is_visible()
        assert actor.page.get_by_role("cell", name=self.item_name, exact=True).is_visible()
        assert actor.page.get_by_role("cell", name=self.subtotal).nth(2)
        assert actor.page.get_by_role("cell", name=self.total).first
