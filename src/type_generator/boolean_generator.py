import random

class BooleanType:

    def __init__(self) -> None:
        pass

    def generate(self, *args):
        return random.choice((True, False))