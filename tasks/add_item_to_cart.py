# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.fill_form import FillForm
from interactions.click import Click


class AddItemToCart:
    def __init__(self, quantity):
        self.quantity = quantity

    def perform_as(self, actor):
        actor.attempts_to(
            FillForm("#product_quantity", self.quantity),
            Click("link[name=' Add to Cart']"),
        )
