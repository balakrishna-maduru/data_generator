# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

from src.data_generator.config import Config
from src.type_generator.boolean_generator import BooleanType
from src.type_generator.numeric_generator import FloatType, IntegerType
from src.type_generator.string_generator import StringType, CharType
from src.type_generator.date_time_generator import TimestampType, DateType

class DataGenerator:

    def __init__(self, config: Config = Config()) -> None:
        self.config = config

    def generate(self, column: str , data_in: dict, params):
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