"""
This module defines the NavigateTo task for navigating to a specific URL.
"""

class NavigateTo:
    def __init__(self, url):
        self.url = url

    def perform_as(self, actor):
        actor.page.goto(self.url)
