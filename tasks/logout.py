# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.hover_element import HoverElement
from interactions.click_element import ClickElement


class Logout:
    def perform_as(self, actor):
        actor.attempts_to(
            HoverElement("li[data-id='menu_account']"),
            ClickElement("li[data-id='menu_logout']"),
        )
