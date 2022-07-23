from src.data_generator.config import Config
from src.type_generator.boolean_generator import BooleanType
from src.type_generator.numeric_generator import FloatType, IntegerType
from src.type_generator.string_generator import StringType, CharType
from src.type_generator.date_time_generator import TimestampType, DateType
from src.data_generator.data_selector import DataSelector


class TypeGenerator:

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