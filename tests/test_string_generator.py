import unittest
from xmlrpc.client import boolean
from src.type_generator.string_generator import StringType, CharType

class TestStringGenerator(unittest.TestCase):

    def setUp(self):
        pass

    def test_string_type(self):
        it = StringType()
        data = it.generate(10)
        print(data)
        assert isinstance(data, str)

    def test_char_type(self):
        it = CharType()
        data = it.generate()
        print(data)
        assert isinstance(data, str)

if __name__ == '__main__':
    unittest.main()