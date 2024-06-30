"""
This module defines the CheckPrivacyPolicy task for checking a specific checkbox.
"""

class CheckPrivacyPolicy:
    
    def perform_as(self, actor):
        actor.page.get_by_label("I have read and agree to the Privacy Policy").check()