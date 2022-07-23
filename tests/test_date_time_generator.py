import unittest
from datetime import date, datetime

from src.data_generator.config import Config
from src.type_generator.date_time_generator import DateType, TimestampType


class TestDateAndTimeType(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_date_type_with_range(self):
        row = [date]
        data_type = DateType(self.config)
        data = data_type.generate(start="2022/01/01", end="2022/01/31")
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_date_type_with_range_multi_record(self):
        self.config.record_count = 2
        row = [date] * self.config.record_count
        data_type = DateType(self.config)
        data = data_type.generate(start="2022/01/01", end="2022/01/31")
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_timestamp_type_with_range(self):
        row = [datetime]
        data_type = TimestampType(self.config)
        data = data_type.generate(start="2022/01/01 12:11:11", end="2022/01/31 22:23:24")
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_timestamp_type_with_range_multi_record(self):
        self.config.record_count = 2
        row = [datetime] * self.config.record_count
        data_type = TimestampType(self.config)
        data = data_type.generate(start="2022/01/01 12:11:11", end="2022/01/31 22:23:24")
        row_dt = [type(item) for item in data]
        assert row_dt == row

if __name__ == '__main__':
    unittest.main()
