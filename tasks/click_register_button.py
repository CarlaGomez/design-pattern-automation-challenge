# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.click_element import ClickElement


class ClickRegisterButton:
    def perform_as(self, actor):
        actor.attempts_to(ClickElement("button[name='register']"))
