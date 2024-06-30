"""
This module contains the Actor class used in the Screenplay pattern for task execution.
"""

class Actor:
    def __init__(self, name, page):
        self.name = name
        self.page = page

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)
