import unittest

from src.data_generator.config import Config
from src.type_generator.string_generator import CharType, StringType


class TestStringGenerator(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_string_type(self):
        row = [str]
        it = StringType(self.config)
        data = it.generate(size=5)
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_string_type_multi_record(self):
        row = [str,str]
        self.config.record_count = 2
        it = StringType(self.config)
        data = it.generate(size=5)
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_char_type(self):
        row = [str]
        it = CharType(self.config)
        data = it.generate()
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_char_type_multi_record(self):
        row = [str,str]
        self.config.record_count = 2
        it = CharType(self.config)
        data = it.generate()
        row_dt = [type(item) for item in data]
        assert row_dt == row

if __name__ == '__main__':
    unittest.main()
