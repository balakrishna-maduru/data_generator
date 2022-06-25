from datetime import datetime
from unicodedata import decimal
import unittest
from src.type_generator.date_time_generator import DateType, TimestampType
from datetime import date

class TestDateAndTimeType(unittest.TestCase):

    def setUp(self):
        pass

    def test_date_type_with_range(self):
        it = DateType()
        data = it.generate("2022/01/01", "2022/01/31")
        assert isinstance(data, date)
        
    def test_timestamp_type_with_range(self):
        it = TimestampType()
        data = it.generate("2022/01/01 12:11:11", "2022/01/31 22:23:24")
        assert isinstance(data, datetime)


if __name__ == '__main__':
    unittest.main()