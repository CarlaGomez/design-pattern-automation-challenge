# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateItemName:
    def __init__(self, item):
        self.item = item

    def perform_as(self, actor):
        actor.attempts_to(AssertTextVisible(self.item))
