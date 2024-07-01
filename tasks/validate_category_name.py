# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateCategoryName:
    def __init__(self, category_name):
        self.category_name = category_name

    def perform_as(self, actor):
        actor.attempts_to(AssertTextVisible(self.category_name))
