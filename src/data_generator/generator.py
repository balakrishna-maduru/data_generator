import threading
import pandas as pd

from src.data_generator.config import Config
from src.type_generator.type_generator import TypeGenerator


class Generator:
    def __init__(self, config: Config = Config()) -> None:
        self.config = config

    def generate(self, schema: dict):
        data = {}
        for column, value in schema.items():
            thread = threading.Thread(target=TypeGenerator(self.config).generate,
                                      args=(column ,data, value))
            thread.start()
            thread.join()
        return data

    def get_df(self, schema: dict):
        data = self.generate(schema)
        return pd.DataFrame.from_dict(data)
