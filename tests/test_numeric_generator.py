from unicodedata import decimal
import unittest

from numpy import integer
from src.type_generator.numeric_generator import IntegerType, FloatType
from src.data_generator.config import Config


class TestNumaricType(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_integer_type_with_range(self):
        test_data = [int]
        integer_type = IntegerType(self.config)
        data = list(map(int, integer_type.generate(low=10, high=20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_integer_type_with_size(self):
        test_data = [int]
        integer_type = IntegerType(self.config)
        data = list(map(int, integer_type.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_float_type_with_range(self):
        test_data = [float]
        float_type = FloatType(self.config)
        data = list(map(float, float_type.generate(low=10, high=20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_float_type_with_size(self):
        test_data = [float]
        float_type = FloatType(self.config)
        data = list(map(float, float_type.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_integer_type_with_range_multi_record(self):
        self.config.record_count = 2
        test_data = [int] * self.config.record_count
        integer_type = IntegerType(self.config)
        data = list(map(int, integer_type.generate(low=10, high=20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_integer_type_with_size_multi_record(self):
        self.config.record_count = 2
        test_data = [int] * self.config.record_count
        integer_type = IntegerType(self.config)
        data = list(map(int, integer_type.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_float_type_with_range_multi_record(self):
        self.config.record_count = 2
        test_data = [float] * self.config.record_count
        float_type = FloatType(self.config)
        data = list(map(float, float_type.generate(low=10, high=20)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data

    def test_float_type_with_size_multi_record(self):
        self.config.record_count = 2
        test_data = [float] * self.config.record_count
        float_type = FloatType(self.config)
        data = list(map(float, float_type.generate(size=5)))
        row_dt = [type(item) for item in data]
        assert row_dt == test_data


if __name__ == "__main__":
    unittest.main()
