# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class VerifyMessage:
    def __init__(self, message):
        self.message = message

    def perform_as(self, actor):
        assert actor.page.get_by_text(self.message).is_visible()
