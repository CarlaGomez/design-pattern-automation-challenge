# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.fill_form import FillForm
from interactions.select_option import SelectOption

class FillAddress:
    def __init__(self, country_id, region_id, zip_code, address):
        self.country_id = country_id
        self.region_id = region_id
        self.zip_code = zip_code
        self.address = address

    def perform_as(self, actor):
        actor.attempts_to(
            SelectOption("#country", self.country_id),
            SelectOption("#region", self.region_id),
            FillForm("#postcode", self.zip_code),
            FillForm("#address", self.address)
        )
