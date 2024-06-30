"""
This module contains the FillForm interaction used in the Screenplay pattern for task execution.
"""

class FillForm:
    def __init__(self, fields):
        self.fields = fields

    def perform_as(self, actor):
        for selector, value in self.fields.items():
            actor.page.fill(selector, value)
