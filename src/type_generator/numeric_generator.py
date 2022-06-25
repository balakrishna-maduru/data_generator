import random
import string

class IntegerType:
    
    def __init__(self, *args, **kwargs) -> None:
        pass

    def _integer_range_generator(self, range):
        return random.randint(range[0],range[1])

    def _integer_size_generator(self, size):
        return int(''.join(random.choices(string.digits, k=size)))

    def generate(self, *args, **kwargs):
        args = args[0]
        key = "size" if 'size' in args else "range"
        return getattr(self, f"_integer_{key}_generator")(args[key])

class DecimalType:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def _decimal_range_generator(self, range):
        return round(random.uniform(range[0], range[1]),range[2])

    def _decimal_size_generator(self, size):
        pre = int('1'+''.join(['0' for i in range(size[1])]))
        return int(''.join(random.choices(string.digits, k=size[0])))/pre

    def generate(self, *args, **kwargs):
        args = args[0]
        key = "size" if 'size' in args else "range"
        return getattr(self, f"_decimal_{key}_generator")(args[key])
