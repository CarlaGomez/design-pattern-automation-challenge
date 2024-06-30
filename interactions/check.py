"""
This module contains the Check interaction used in the Screenplay pattern for task execution.
"""

class Check:
    def __init__(self, selector):
        self.selector = selector

    def perform_as(self, actor):
        actor.page.locator(self.selector).check()
