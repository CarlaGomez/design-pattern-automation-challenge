# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class FillNewsletter:
    def __init__(self, option):
        self.option = option

    def perform_as(self, actor):
        actor.page.get_by_label(self.option).check()
