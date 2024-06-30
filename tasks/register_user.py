"""
This module defines the RegisterUser task for clicking on the register button.
"""

class RegisterUser:
    def perform_as(self, actor):
        actor.page.locator("#AccountFrm div").filter(has_text="Continue").nth(2).click()
