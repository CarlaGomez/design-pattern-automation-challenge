# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.check_element import CheckElement


class FillNewsletter:
    def __init__(self, option):
        self.option = option

    def perform_as(self, actor):
        actor.attempts_to(CheckElement(f"label[text='{self.option}']"))
