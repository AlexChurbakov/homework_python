import os
from importlib.resources import contents

import pytz
from datetime import datetime
from helpers import create_file

class Saver:
    def __init__(self, filepath: str, buffer):
        self.filepath = filepath
        self.buffer = buffer

    def save_to_file(self):
        format_dict = {
            '.csv': lambda ts, name, value: f"{ts};{name};{value}\n",
            '.txt': lambda ts, name, value: f"{ts} {name} {value}\n"
        }

        # Получаем формат записи из словаря с помощью get()
        write_format = format_dict.get(self.filepath[-4:], format_dict['.txt'])

        with open(self.filepath, "a") as file:
            for timestamp, name, value in self.buffer:
                file.write(write_format(timestamp, name, value))
                #print(f"{timestamp}    {name}    {value}\n")
            self.buffer.clear()
        with open(self.filepath, "r") as file:
            #for timestamp, name, value in self.buffer:
                content = file.read()
                print(content)

class Statsd:
    def __init__(self, filepath: str, buffer_limit: int):
        if not filepath.endswith(('.txt', '.csv')):

            raise ValueError("File must be a .txt or .csv file.")

        self.filepath = filepath
        self.buffer_limit = buffer_limit
        self.buffer = []

        if not os.path.isfile(self.filepath):
            create_file(self.filepath)
            # with open(self.filepath, "w") as file:
            #     file.write("Well come to file\n")

    def incr(self, name: str):
        self._add_metric(name, 1)

    def decr(self, name: str):
        self._add_metric(name, -1)

    def _add_metric(self, name: str, value: int):
        # Используем UTC-часовой пояс
        utc_now = datetime.now(pytz.utc)
        timestamp = utc_now.strftime("%Y-%m-%dT%H:%M:%S%z")
        self.buffer.append((timestamp, name, value))

        #print(f"Current buffer size: {len(self.buffer)}")  # Отладочный вывод

        if len(self.buffer) >= self.buffer_limit:
            self._evacuate()

    def _evacuate(self):

        #print(f"Evacuating buffer with size: {len(self.buffer)}")  # Отладочный вывод

        try_to_save = Saver(self.filepath, self.buffer)
        try_to_save.save_to_file()

        #print(f"Buffer after saving: {len(self.buffer)}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._evacuate()
        self.buffer.clear()


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    return Statsd(path, buffer_limit)


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    return Statsd(path, buffer_limit)