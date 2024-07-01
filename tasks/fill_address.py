# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


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
        actor.page.fill("#AccountFrm_company", self.company)
        actor.page.fill("#AccountFrm_address_1", self.first_address)
        actor.page.fill("#AccountFrm_address_2", self.second_address)
        actor.page.locator("#AccountFrm_country_id").select_option(
            self.country_id)
        actor.page.fill("#AccountFrm_city", self.city)
        actor.page.locator("#AccountFrm_zone_id").select_option(self.region_id)
        actor.page.fill("#AccountFrm_postcode", self.zip_code)
