# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.check import Check

class FillNewsletter:
    def perform_as(self, actor):
        actor.attempts_to(
            Check("#newsletter")
        )
