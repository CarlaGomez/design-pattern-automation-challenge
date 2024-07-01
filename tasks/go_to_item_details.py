# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.click import Click

class GoToItemDetails:
    def perform_as(self, actor):
        actor.attempts_to(
            Click("div:nth-child(3) > .thumbnail > a")
        )
