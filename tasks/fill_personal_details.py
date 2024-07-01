# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class FillPersonalDetails:
    def __init__(self, first_name, last_name, email, phone, fax):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.fax = fax

    def perform_as(self, actor):
        actor.page.fill("#AccountFrm_firstname", self.first_name)
        actor.page.fill("#AccountFrm_lastname", self.last_name)
        actor.page.fill("#AccountFrm_email", self.email)
        actor.page.fill("#AccountFrm_telephone", self.phone)
        actor.page.fill("#AccountFrm_fax", self.fax)
