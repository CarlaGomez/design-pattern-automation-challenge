# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class Actor:
    def __init__(self, name, page):
        self.name = name
        self.page = page

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)
