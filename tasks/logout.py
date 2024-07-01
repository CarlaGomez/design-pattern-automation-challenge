# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class Logout:
    def perform_as(self, actor):
        actor.page.get_by_role("link", name=" Account", exact=True).hover()
        actor.page.get_by_role("link", name=" Logout").click()
