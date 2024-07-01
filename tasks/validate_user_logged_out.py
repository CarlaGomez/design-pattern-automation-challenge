# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.assert_text_visible import AssertTextVisible


class ValidateUserLoggedOut:
    def __init__(self, is_visible):
        self.is_visible = is_visible

    def perform_as(self, actor):
        if self.is_visible:
            actor.attempts_to(AssertTextVisible("Account Logout", ".maintext"))
        else:
            assert not actor.page.locator(
                "span.maintext:has-text('Account Logout')"
            ).is_visible()
