""" Testing data selector class """
import unittest

from src.data_generator.config import Config
from src.data_generator.data_selector import DataSelector


class TestDataSelector(unittest.TestCase):

    def setUp(self):
        pass

    def test_data_selector_int(self):
        row = [int, int]
        data = [1,2,3,4,5]
        data_selector = DataSelector()
        data = data_selector.select(data, 2)
        row_dt = [type(item) for item in data]
        return isinstance(data, list) and data.__len__() == 2 and row == row_dt

    def test_data_selector_double(self):
        row = [float] * 20
        data = [10.5,20.3,35.6,4.52345,5.67]
        data_selector = DataSelector()
        data = data_selector.select(data, 2)
        row_dt = [type(item) for item in data]
        return isinstance(data, list) and data.__len__() == 20 and row == row_dt

    def test_data_selector_char(self):
        row = [str] * 5
        data = ["M","F","O"]
        data_selector = DataSelector()
        data = data_selector.select(data, 5)
        row_dt = [type(item) for item in data]
        return isinstance(data, list) and data.__len__() == 5 and row == row_dt

    def test_data_selector_string(self):
        row = [str] * 10
        data = ["North", "East", "West", "South"]
        data_selector = DataSelector()
        data = data_selector.select(data, 10)
        row_dt = [type(item) for item in data]
        return isinstance(data, list) and data.__len__() == 10 and row == row_dt

if __name__ == '__main__':
    unittest.main()