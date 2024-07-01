# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidateItemPrice:
    def __init__(self, price):
        self.price = price

    def perform_as(self, actor):
        item_price = actor.page.get_by_text(self.price).first
        assert item_price
