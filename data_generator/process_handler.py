import json
import threading
from multiprocessing import Manager, Pool

from data_generator.config import Config
from data_generator.type_generator.type_generator import TypeGenerator


class ProcessHandler:

    def __init__(self, schema: dict, config: Config) -> None:
        self.schema = schema
        self.config = config

    def handle(self):
        if self.config.process_handler == "multiprocess":
            return self._multi_process_handler()
        elif self.config.process_handler == "thread":
            return self._thread_handler()
        else:
            raise TypeError("Processes handler was not implemented")

    def _thread_handler(self):
        data = {}
        for column, value in self.schema.items():
            thread = threading.Thread(
                target=TypeGenerator(self.config).generate, args=(column, data, value)
            )
            thread.start()
            thread.join()
        return data

    def _multi_process_handler(self):
        with Pool(self.config.process_count) as pool, Manager() as manager:
            data = manager.dict()
            for column, value in self.schema.items():
                pool.apply_async(TypeGenerator(self.config).generate,
                                (column, data, value))
            pool.close()
            pool.join()
            return self._copy_multi_thread_dict(data)

    def _copy_multi_thread_dict(self, data):
        data_out = {}
        for key, value in data.items():
            data_out[key] = value
        return data_out