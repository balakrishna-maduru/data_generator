import threading
import pandas as pd

from src.data_generator.config import Config
from src.type_generator.boolean_generator import BooleanType
from src.type_generator.numeric_generator import FloatType, IntegerType
from src.type_generator.string_generator import StringType, CharType
from src.type_generator.date_time_generator import TimestampType, DateType
from src.data_generator.data_selector import DataSelector

class DataGenerator:

    def __init__(self, config: Config = Config()) -> None:
        self.config = config

    def generate(self, column: str , data_in: dict, params):
        if params.get('select'):
            data_selector = DataSelector()
            data_in[column] = data_selector.select(params.get('select'), self.config.record_count)
        else:
            type_class = params["type"]
            d_class = type_class(self.config)
            data_in[column] = d_class.generate(**params)



class Generator:
    def __init__(self, config: Config = Config()) -> None:
        self.config = config

    def collect(self, schema: dict):
        data = {}
        for column, value in schema.items():
            thread = threading.Thread(target=DataGenerator(self.config).generate,
                                      args=(column ,data, value))
            thread.start()
            thread.join()
        return data

    def get_df(self, schema: dict):
        data = self.collect(schema)
        return pd.DataFrame.from_dict(data)
