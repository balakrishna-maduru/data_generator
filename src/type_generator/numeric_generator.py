import numpy as np

from src.data_generator.config import Config

class BaseType:

    def __init__(self) -> None:
        pass

    def _get_low_high(self, size):
        self.config.low = int('1'+''.join(["0" for _ in range(size-1)]))
        self.config.high = int(''.join(['9' for _ in range(size)]))


class IntegerType(BaseType):

    def __init__(self, config: Config) -> None:
        self.config = config
        super().__init__()

    def generate(self, **kwargs):
        if "size" in kwargs:
            self._get_low_high(kwargs.get("size"))
        return np.random.randint(kwargs.get("low", self.config.low),
                                 kwargs.get("high", self.config.high),
                                 kwargs.get("record_count", self.config.record_count))

class FloatType(BaseType):

    def __init__(self, config: Config) -> None:
        self.config = config
        super().__init__()

    def generate(self, **kwargs):
        if "size" in kwargs:
            self._get_low_high(kwargs.get("size"))
        return np.random.uniform(kwargs.get("low", self.config.low),
                                 kwargs.get("high", self.config.high),
                                 kwargs.get("record_count", self.config.record_count))
