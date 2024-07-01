from interactions.hover_element import HoverElement
from interactions.click import Click

class SearchForProducts:
    def __init__(self, product, gender):
        self.product = product
        self.gender = gender

    def perform_as(self, actor):
        actor.attempts_to(
            HoverElement(f"link[name='{self.product}']"),
            Click(f"link[name='{self.gender}']")
        )
