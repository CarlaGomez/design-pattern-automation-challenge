"""
This module defines the Logout task for logging out a user.
"""

class Logout:
    def perform_as(self, actor):
        actor.page.get_by_role("link", name=" Account", exact=True).hover()
        actor.page.get_by_role("link", name=" Logout").click()
