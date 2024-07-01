# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class CheckPrivacyPolicy:
    def perform_as(self, actor):
        actor.page.get_by_label(
            "I have read and agree to the Privacy Policy").check()
        