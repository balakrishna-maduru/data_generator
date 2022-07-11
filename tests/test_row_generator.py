import imp
import unittest
from datetime import date, datetime

import numpy as np

from src.data_generator.data_generator import RowDataGenerator
from src.data_generator.generator import Generator
from src.type_generator.boolean_generator import BooleanType
from src.type_generator.numeric_generator import FloatType, IntegerType
from src.type_generator.string_generator import StringType, CharType
from src.type_generator.date_time_generator import TimestampType, DateType
from src.data_generator.config import Config


class TestDateGenerator(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        self.schema = {
            "id": {"type": "IntegerType", "range": (100, 200)},
            "name": {"type": "StringType", "size": 10},
            "sex": {"type": "CharType"},
            "date_of_birth": {"type": "DateType", "start": '2010/01/01', "end": '2022/12/31'},
            "salary": {"type": "DecimalType", "size": (7,2)},
            "is_active": {"type": "BooleanType"},
            "updated_date": {"type": "TimestampType", "start": '2010/01/01 00:00:00', "end": '2022/12/31 00:00:00'},
        }
        self.schema = {
            "id": {"type": IntegerType, "low":10, "high":100},
            "is_active": {"type": BooleanType},
            "name": {"type": StringType, "size": 10},
            "salary": {"type": FloatType, "size": 7},
            "sex": {"type": CharType},
            "date_of_birth": {"type": DateType, "start": '2010/01/01', "end": '2022/12/31'},
            "updated_date": {"type": TimestampType, "start": '2010/01/01 00:00:00', "end": '2022/12/31 00:00:00'},
        }


    def test_row_generator(self):
        self.config.record_count = 1
        row = {"id": np.int64,
               "is_active": np.bool_,
               "name": str,
               "salary": np.float64,
               "sex": str,
               'updated_date': datetime,
               'date_of_birth': date}
        rdg = Generator()
        data = rdg.collect(self.schema)
        print(data)
        row_dt = {}
        for key, value in data.items():
            row_dt[key] = type(value[0])
        print(row)
        print(row_dt)
        assert row == row_dt

    # def test_row_generator_multi_record(self):
    #     self.config.record_count = 2
    #     row = {"id": [np.int64, np.int64], 
    #            "is_active": [np.bool_, np.bool_]}
    #     rdg = Generator()
    #     data = rdg.collect(self.schema)
    #     row_dt = {}
    #     for key, value in data.items():
    #         row_dt[key] = [type(v) for v in value]
    #     assert row == row_dt




if __name__ == '__main__':
    unittest.main()