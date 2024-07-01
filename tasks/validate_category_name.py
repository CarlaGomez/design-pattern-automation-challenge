# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidateCategoryName:
    def __init__(self, category_name):
        self.category_name = category_name

    def perform_as(self, actor):
        assert actor.page.get_by_text(self.category_name, exact=True).is_visible()
