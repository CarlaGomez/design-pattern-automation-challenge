# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from utils.faker_utils import FakeData
from tasks.fill_personal_details import FillPersonalDetails
from tasks.fill_address import FillAddress
from tasks.fill_login_details import FillLoginDetails
from tasks.fill_newsletter import FillNewsletter
from tasks.check_privacy_policy import CheckPrivacyPolicy
from tasks.click_continue_button import ClickContinueButton


class RegisterUser:
    def __init__(self, country_id, region_id, zip_code, login_password):
        self.country_id = country_id
        self.region_id = region_id
        self.zip_code = zip_code
        self.login_password = login_password
        self.fake = FakeData()

    def perform_as(self, actor):
        actor.attempts_to(
            ClickContinueButton(),
            FillPersonalDetails(
                self.fake.first_name(),
                self.fake.last_name(),
                self.fake.email(),
                self.fake.phone_number(),
                self.fake.phone_number(),
            ),
            FillAddress(
                self.fake.company(),
                self.fake.street_address(),
                self.fake.address(),
                self.country_id,
                self.fake.city(),
                self.region_id,
                self.zip_code,
            ),
            FillLoginDetails(self.fake.user_name(), self.login_password),
            FillNewsletter(),
            CheckPrivacyPolicy(),
            ClickContinueButton(),
        )
