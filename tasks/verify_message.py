"""
This module defines the VerifyMessage task for checking the visibility of a message.
"""

class VerifyMessage:
    def __init__(self, message, is_visible=True):
        self.message = message
        self.is_visible = is_visible

    def perform_as(self, actor):
        if self.is_visible:
            assert actor.page.get_by_text(self.message).is_visible()
        else:
            assert actor.page.get_by_text(self.message).is_hidden()
