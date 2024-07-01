# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from interactions.click import Click

class RegisterUser:
    def perform_as(self, actor):
        actor.attempts_to(
            Click("button[name=' Register']")
        )
