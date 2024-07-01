# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.click_element import ClickElement
from interactions.hover_element import HoverElement


class SearchForProducts:
    def __init__(self, product, gender):
        self.product = product
        self.gender = gender

    def perform_as(self, actor):
        actor.attempts_to(
            HoverElement(f"role=link[name='{self.product}']"),
            ClickElement(f"role=link[name='{self.gender}']"),
        )
