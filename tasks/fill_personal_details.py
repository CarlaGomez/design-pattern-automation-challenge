# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.fill_form import FillForm

class FillPersonalDetails:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def perform_as(self, actor):
        actor.attempts_to(
            FillForm("#first_name", self.first_name),
            FillForm("#last_name", self.last_name),
            FillForm("#email", self.email)
        )
