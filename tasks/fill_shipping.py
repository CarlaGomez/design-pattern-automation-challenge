# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.enter_text import EnterText
from interactions.select_option import SelectOption
from interactions.click_element import ClickElement


class FillShipping:
    def __init__(self, country_id, region_id, zip_code):
        self.country_id = country_id
        self.region_id = region_id
        self.zip_code = zip_code

    def perform_as(self, actor):
        actor.attempts_to(
            SelectOption.from_dropdown("#estimate_country")(self.country_id),
            SelectOption.from_dropdown("#estimate_country_zones")(self.region_id),
            EnterText.into("#estimate_postcode")(self.zip_code),
            ClickElement("role=button[name='Estimate']"),
        )
