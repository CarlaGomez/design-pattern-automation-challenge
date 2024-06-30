"""
This module contains the Click interaction used in the Screenplay pattern for task execution.
"""

class Click:
    def __init__(self, selector):
        self.selector = selector

    def perform_as(self, actor):
        actor.page.locator(self.selector).click()
