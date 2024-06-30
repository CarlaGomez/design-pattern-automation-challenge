"""
This module defines the ClickButton task for clicking a specific button.
"""

class ClickButton:
    def __init__(self, button_name):
        self.button_name = button_name

    def perform_as(self, actor):
        actor.page.get_by_role("button", name=self.button_name).click()
