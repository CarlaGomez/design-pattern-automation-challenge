# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.enter_text import EnterText
from interactions.click_element import ClickElement


class AddItemToCart:
    def __init__(self, product_quantity):
        self.product_quantity = product_quantity

    def perform_as(self, actor):
        actor.attempts_to(
            EnterText.into("#product_quantity")(self.product_quantity),
            ClickElement("role=link[name='\\uf217 Add to Cart']"),
        )
