# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.enter_text import EnterText


class FillPersonalDetails:
    def __init__(self, first_name, last_name, email, phone, fax):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.fax = fax

    def perform_as(self, actor):
        actor.attempts_to(
            EnterText.into("#AccountFrm_firstname")(self.first_name),
            EnterText.into("#AccountFrm_lastname")(self.last_name),
            EnterText.into("#AccountFrm_email")(self.email),
            EnterText.into("#AccountFrm_telephone")(self.phone),
            EnterText.into("#AccountFrm_fax")(self.fax),
        )
