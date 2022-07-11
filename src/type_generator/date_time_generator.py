from datetime import datetime, timedelta
from random import randrange

from src.data_generator.config import Config


class DateTime:

    def __init__(self) -> None:
        pass

    def _random_timestamp(self, start, end, date_only=False):
        start = datetime.strptime(start, '%Y/%m/%d %H:%M:%S')
        end = datetime.strptime(end, '%Y/%m/%d %H:%M:%S')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        date =  start + timedelta(seconds=random_second)
        return date.date() if date_only else date

class DateType(DateTime):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config
    
    def generate(self, **kwargs):
        return list(map(self._random_timestamp,
                        [f"{kwargs['start']} 00:00:00"]*self.config.record_count,
                        [f"{kwargs['end']} 00:00:00"]*self.config.record_count, 
                        [1]*self.config.record_count))

class TimestampType(DateTime):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config
    
    def generate(self, **kwargs):
        return list(map(self._random_timestamp,
                        [kwargs['start']]*self.config.record_count,
                        [kwargs['end']]*self.config.record_count))
        