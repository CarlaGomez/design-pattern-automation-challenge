# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.enter_text import EnterText
from interactions.select_option import SelectOption


class FillAddress:
    def __init__(
        self,
        company,
        first_address,
        second_address,
        country_id,
        city,
        region_id,
        zip_code,
    ):
        self.company = company
        self.first_address = first_address
        self.second_address = second_address
        self.country_id = country_id
        self.city = city
        self.region_id = region_id
        self.zip_code = zip_code

    def perform_as(self, actor):
        actor.attempts_to(
            EnterText.into("#AccountFrm_company")(self.company),
            EnterText.into("#AccountFrm_address_1")(self.first_address),
            EnterText.into("#AccountFrm_address_2")(self.second_address),
            SelectOption.from_dropdown("#AccountFrm_country_id")(self.country_id),
            EnterText.into("#AccountFrm_city")(self.city),
            SelectOption.from_dropdown("#AccountFrm_zone_id")(self.region_id),
            EnterText.into("#AccountFrm_postcode")(self.zip_code),
        )
