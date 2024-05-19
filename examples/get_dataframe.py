from data_generator.config import Config
from data_generator.generator import Generator
from data_generator.type_generator.boolean_generator import BooleanType
from data_generator.type_generator.date_time_generator import DateType, TimestampType
from data_generator.type_generator.numeric_generator import FloatType, IntegerType
from data_generator.type_generator.string_generator import CharType, StringType

if __name__ == "__main__":
    config = Config()
    schema = {
            "id": {"type": IntegerType, "low":10, "high":100},
            "is_active": {"type": BooleanType},
            "name": {"type": StringType, "size": 10},
            "salary": {"type": FloatType, "size": 7},
            "sex": {"type": CharType},
            "date_of_birth": {"type": DateType, "start": '2010/01/01', "end": '2022/12/31'},
            "updated_date": {"type": TimestampType, "start": '2010/01/01 00:00:00', "end": '2022/12/31 00:00:00'},
            "region": {"type": StringType, "select": ["North", "East", "West","South"]}
        }
    config.record_count = 1
    rdg = Generator()
    df = rdg.get_df(schema)
    print(df)