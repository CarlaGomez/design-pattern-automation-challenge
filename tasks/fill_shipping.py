# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.fill_form import FillForm
from interactions.select_option import SelectOption
from interactions.click import Click


class FillShipping:
    def __init__(self, country_id, region_id, zip_code):
        self.country_id = country_id
        self.region_id = region_id
        self.zip_code = zip_code

    def perform_as(self, actor):
        actor.attempts_to(
            SelectOption("#estimate_country", self.country_id),
            SelectOption("#estimate_country_zones", self.region_id),
            FillForm("#estimate_postcode", self.zip_code),
            Click("button[name=' Estimate']"),
        )
