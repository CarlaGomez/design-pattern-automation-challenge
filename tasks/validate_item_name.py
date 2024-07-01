# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class ValidateItemName:
    def __init__(self, item):
        self.item = item

    def perform_as(self, actor):
        item_name = actor.page.get_by_role("heading", name="ck One Gift Set").get_by_text(self.item)
        assert item_name
