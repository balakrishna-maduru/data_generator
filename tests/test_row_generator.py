import unittest
from datetime import date, datetime

import numpy as np
import pandas as pd

from src.data_generator.config import Config
from src.data_generator.generator import Generator
from src.type_generator.boolean_generator import BooleanType
from src.type_generator.date_time_generator import DateType, TimestampType
from src.type_generator.numeric_generator import FloatType, IntegerType
from src.type_generator.string_generator import CharType, StringType


class TestDateGenerator(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        self.schema = {
            "id": {"type": IntegerType, "low":10, "high":100},
            "is_active": {"type": BooleanType},
            "name": {"type": StringType, "size": 10},
            "salary": {"type": FloatType, "size": 7},
            "sex": {"type": CharType},
            "date_of_birth": {"type": DateType, "start": '2010/01/01', "end": '2022/12/31'},
            "updated_date": {"type": TimestampType, "start": '2010/01/01 00:00:00', "end": '2022/12/31 00:00:00'},
            "region": {"type": StringType, "select": ["North", "East", "West","South"]}
        }


    def test_generator(self):
        self.config.record_count = 1
        row = {"id": np.int64,
               "is_active": np.bool_,
               "name": str,
               "salary": np.float64,
               "sex": str,
               'updated_date': datetime,
               'date_of_birth': date,
               'region': np.str_}
               
        rdg = Generator()
        data = rdg.collect(self.schema)
        row_dt = {}
        for key, value in data.items():
            row_dt[key] = type(value[0])
        assert row == row_dt and data['region'][0] in self.schema["region"]["select"]

    def test_generator_multi_record(self):
        self.config.record_count = 2
        row = {"id": [np.int64] * 2,
               "is_active": [np.bool_] * 2,
               "name": [str] * 2,
               "salary": [np.float64]  * 2,
               "sex": [str]  * 2,
               'updated_date': [datetime] * 2,
               'date_of_birth': [date]  * 2,
               'region': [np.str_] * 2}
        rdg = Generator()
        data = rdg.collect(self.schema)
        row_dt = {}
        for key, value in data.items():
            row_dt[key] = [type(v) for v in value]
        assert row == row_dt

    def test_get_df(self):
        self.config.record_count = 2
        rdg = Generator()
        df = rdg.get_df(self.schema)
        assert isinstance(df,pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
    