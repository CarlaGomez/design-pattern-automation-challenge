# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.click_element import ClickElement


class Logout:
    def perform_as(self, actor):
        actor.attempts_to(ClickElement("a[role='link'][name='Logout']"))
