import unittest
from datetime import date, datetime

from src.data_generator.config import Config
from src.type_generator.date_time_generator import DateType, TimestampType


class TestDateAndTimeType(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_date_type_with_range(self):
        row = [date]
        it = DateType(self.config)
        data = it.generate(start="2022/01/01", end="2022/01/31")
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_date_type_with_range_multi_record(self):
        row = [date, date]
        self.config.record_count = 2
        it = DateType(self.config)
        data = it.generate(start="2022/01/01", end="2022/01/31")
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_timestamp_type_with_range(self):
        row = [datetime]
        it = TimestampType(self.config)
        data = it.generate(start="2022/01/01 12:11:11", end="2022/01/31 22:23:24")
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_timestamp_type_with_range_multi_record(self):
        row = [datetime, datetime]
        self.config.record_count = 2
        it = TimestampType(self.config)
        data = it.generate(start="2022/01/01 12:11:11", end="2022/01/31 22:23:24")
        row_dt = [type(item) for item in data]
        assert row_dt == row

if __name__ == '__main__':
    unittest.main()
