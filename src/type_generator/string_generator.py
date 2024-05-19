import random
import string

from src.data_generator.config import Config


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
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config
        
    def generate(self, **kwargs):
        return list(map(self._string_generate,[kwargs.get("size",1)]*self.config.record_count))

class CharType(StringAndCharType):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config

    def generate(self, **kwargs):
        return list(map(self._string_generate,[1]*self.config.record_count))
