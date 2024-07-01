# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.select_option import SelectOption


class SortItems:
    def __init__(self, sort_criteria):
        self.sort_criteria = sort_criteria

    def perform_as(self, actor):
        actor.attempts_to(SelectOption.from_dropdown("#sort")(self.sort_criteria))
