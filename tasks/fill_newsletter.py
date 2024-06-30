"""
This module defines the FillNewsletter task for filling the newsletter section in the register form.
"""

class FillNewsletter:
    def __init__(self, option):
        self.option = option

    def perform_as(self, actor):
        actor.page.get_by_label(self.option).check()
