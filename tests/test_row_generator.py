from datetime import date, datetime
import unittest
from src.data_generator.data_generator import RowDataGenerator

class TestDateGenerator(unittest.TestCase):

    def setUp(self):
        self.schema = {
            "id": {"type": "IntegerType", "range": (100, 200)},
            "name": {"type": "StringType", "size": 10},
            "sex": {"type": "CharType"},
            "date_of_birth": {"type": "DateType", "start": '2010/01/01', "end": '2022/12/31'},
            "Salary": {"type": "DecimalType", "size": (7,2)},
            "is_active": {"type": "BooleanType"},
            "updated_date": {"type": "TimestampType", "start": '2010/01/01 00:00:00', "end": '2022/12/31 00:00:00'},
        }

    def test_row_generator(self):
        row = [int, str, str, date, float, bool, datetime]
        rdg = RowDataGenerator()
        data = rdg.generate(self.schema)
        row_dt = [type(item) for item in data]
        assert row == row_dt




if __name__ == '__main__':
    unittest.main()