import pandas as pd

from data_generator.config import Config
from data_generator.process_handler import ProcessHandler


class Generator:
    
    def __init__(self, config: Config = Config()) -> None:
        self.config = config

    def generate(self, schema: dict):
        process_handler = ProcessHandler(schema, self.config)
        return process_handler.handle()

    def get_df(self, schema: dict):
        data = self.generate(schema)
        return pd.DataFrame.from_dict(data)
