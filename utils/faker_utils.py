# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from faker import Faker


class FakeData:
    def __init__(self):
        self.fake = Faker()

    def first_name(self):
        return self.fake.first_name()

    def last_name(self):
        return self.fake.last_name()

    def email(self):
        return self.fake.email()

    def phone_number(self):
        return self.fake.phone_number()

    def company(self):
        return self.fake.company()

    def street_address(self):
        return self.fake.street_address()

    def address(self):
        return self.fake.address()

    def city(self):
        return self.fake.city()

    def user_name(self):
        return self.fake.user_name()

    def password(self):
        return self.fake.password()
