# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class FillForm:
    def __init__(self, fields):
        self.fields = fields

    def perform_as(self, actor):
        for selector, value in self.fields.items():
            actor.page.fill(selector, value)
