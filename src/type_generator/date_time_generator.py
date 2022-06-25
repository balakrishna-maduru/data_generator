import imp
from random import randrange
from datetime import datetime, timedelta


class DateTime:

    def __init__(self) -> None:
        pass

    def _random_timestamp(self, start, end):
        start = datetime.strptime(start, '%Y/%m/%d %H:%M:%S')
        end = datetime.strptime(end, '%Y/%m/%d %H:%M:%S')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

class DateType(DateTime):
    def __init__(self) -> None:
        super().__init__()
    
    def generate(self, *args):
        start, end = args[0].get("start"), args[0].get("end")
        return self._random_timestamp(f"{start} 00:00:00", f"{end} 00:00:00").date()

class TimestampType(DateTime):
    def __init__(self) -> None:
        super().__init__()
    
    def generate(self, *args):
        start, end = args[0].get("start"), args[0].get("end")
        return self._random_timestamp(start, end)