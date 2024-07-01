# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateUserLoggedIn:
    def __init__(self, is_logged_in):
        self.is_logged_in = is_logged_in

    def perform_as(self, actor):
        if self.is_logged_in:
            actor.attempts_to(AssertTextVisible("Welcome back John"))
        else:
            assert not actor.page.locator(
                "a[role='link'][name='Welcome back John']"
            ).is_visible()
