# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.click import Click


class GoToCart:
    def perform_as(self, actor):
        actor.attempts_to(Click("link[name=' Cart']"))
