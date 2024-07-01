# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.fill_form import FillForm

class FillLoginDetails:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def perform_as(self, actor):
        actor.attempts_to(
            FillForm("#username", self.username),
            FillForm("#password", self.password),
            FillForm("#AccountFrm_confirm", self.password)
        )
