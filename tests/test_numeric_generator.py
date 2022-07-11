from unicodedata import decimal
import unittest
from src.type_generator.numeric_generator import IntegerType, FloatType
from src.data_generator.config import Config

class TestNumaricType(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_integer_type_with_range(self):
        test_data = [int]
        it = IntegerType(self.config)
        data = list(map(int,it.generate(low = 10,high = 20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data
        
    def test_integer_type_with_size(self):
        test_data = [int]
        it = IntegerType(self.config)
        data = list(map(int,it.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_float_type_with_range(self):
        test_data = [float]
        it = FloatType(self.config)
        data = list(map(float,it.generate(low = 10,high = 20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data
        
    def test_float_type_with_size(self):
        test_data = [float]
        it = FloatType(self.config)
        data = list(map(float,it.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data


    def test_integer_type_with_range_multi_record(self):
        test_data = [int,int]
        self.config.record_count = 2
        it = IntegerType(self.config)
        data = list(map(int,it.generate(low = 10,high = 20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data
        
    def test_integer_type_with_size_multi_record(self):
        test_data = [int,int]
        self.config.record_count = 2
        it = IntegerType(self.config)
        data = list(map(int,it.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_float_type_with_range_multi_record(self):
        test_data = [float,float]
        self.config.record_count = 2
        it = FloatType(self.config)
        data = list(map(float,it.generate(low = 10,high = 20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data
        
    def test_float_type_with_size_multi_record(self):
        test_data = [float,float]
        self.config.record_count = 2
        it = FloatType(self.config)
        data = list(map(float,it.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data


if __name__ == '__main__':
    unittest.main()