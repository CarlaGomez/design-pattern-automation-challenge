# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class CheckElement:
    def __init__(self, selector):
        self.selector = selector

    def perform_as(self, actor):
        actor.page.check(self.selector)
