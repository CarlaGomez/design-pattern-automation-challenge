# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.check_element import CheckElement


class CheckPrivacyPolicy:
    def perform_as(self, actor):
        actor.attempts_to(CheckElement("#AccountFrm_agree"))
