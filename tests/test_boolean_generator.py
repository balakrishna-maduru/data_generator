import unittest

import numpy as np

from src.data_generator.config import Config
from src.type_generator.boolean_generator import BooleanType


class TestBooleanType(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_date_type_with_range(self):
        row = [np.bool_]
        boolean_type = BooleanType(self.config)
        data = boolean_type.generate()
        row_dt = [type(item) for item in data]
        assert row == row_dt

    def test_date_type_with_range_multi_record(self):
        self.config.record_count = 2
        row = [np.bool_] * self.config.record_count
        boolean_type = BooleanType(self.config)
        data = boolean_type.generate()
        row_dt = [type(item) for item in data]
        assert row == row_dt


if __name__ == '__main__':
    unittest.main()
