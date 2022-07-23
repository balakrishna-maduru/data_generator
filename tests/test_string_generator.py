import unittest

from src.data_generator.config import Config
from src.type_generator.string_generator import CharType, StringType


class TestStringGenerator(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_string_type(self):
        row = [str]
        string_type = StringType(self.config)
        data = string_type.generate(size=5)
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_string_type_multi_record(self):
        self.config.record_count = 2
        row = [str] * self.config.record_count
        string_type = StringType(self.config)
        data = string_type.generate(size=5)
        row_dt = [type(item) for item in data]
        assert row_dt == row

    def test_char_type(self):
        row = [str]
        char_type = CharType(self.config)
        data = char_type.generate()
        row_dt = [type(item) for item in data]
        assert row_dt == row and len(data) == 1

    def test_char_type_multi_record(self):
        self.config.record_count = 2
        row = [str] * self.config.record_count
        char_type = CharType(self.config)
        data = char_type.generate()
        row_dt = [type(item) for item in data]
        assert row_dt == row


if __name__ == "__main__":
    unittest.main()
