import numpy as np
from src.data_generator.config import Config

class BooleanType:

    def __init__(self, config: Config) -> None:
        self.config = config

    def generate(self,*args, **kwargs):
        return np.random.randint(2, size=self.config.record_count) == 0