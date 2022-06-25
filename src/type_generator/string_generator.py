from ast import arg
import random
import string


class StringAndCharType:

    def __init__(self) -> None:
        pass

    def _only_string(self, only_string):
        if only_string:
            return string.ascii_lowercase + string.ascii_uppercase + string.digits
        return string.ascii_lowercase + string.ascii_uppercase

    def _string_generate(self, size, only_string=True):
        return ''.join(random.choices(self._only_string(only_string),k=size))


class StringType(StringAndCharType):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, *args):
        args = args[0]
        return self._string_generate(args.get("size"))

class CharType(StringAndCharType):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, *args):
        return self._string_generate(size=1)
