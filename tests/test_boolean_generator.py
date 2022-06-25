import unittest
from xmlrpc.client import boolean
from src.type_generator.boolean_generator import BooleanType

class TestBooleanType(unittest.TestCase):

    def setUp(self):
        pass

    def test_date_type_with_range(self):
        it = BooleanType()
        data = it.generate()
        assert isinstance(data, boolean)

if __name__ == '__main__':
    unittest.main()