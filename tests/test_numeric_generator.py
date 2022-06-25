from unicodedata import decimal
import unittest
from src.type_generator.numeric_generator import IntegerType, DecimalType

class TestNumaricType(unittest.TestCase):

    def setUp(self):
        pass

    def test_integer_type_with_range(self):
        it = IntegerType()
        data = it.generate(range=[10,20])
        assert isinstance(data, int)
        
    def test_integer_type_with_size(self):
        it = IntegerType()
        data = it.generate(size=4)
        assert isinstance(data, int)

    def test_decimal_type_with_range(self):
        it = DecimalType()
        data = it.generate(range=(10,20,2))
        assert isinstance(data, float)

    def test_decimal_type_with_size(self):
        it = DecimalType()
        data = it.generate(size=(10,2))
        assert isinstance(data, float)


if __name__ == '__main__':
    unittest.main()