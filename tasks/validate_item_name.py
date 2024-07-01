# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateItemName:
    def __init__(self, text):
        self.text = text

    def perform_as(self, actor):
        actor.attempts_to(AssertTextVisible(self.text, ".bgnone"))
