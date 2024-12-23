import os
import pytz
from typing import Protocol
from datetime import datetime
from helpers import create_file

class Protocol_Saver(Protocol):
    def __init__(self, filepath):
        self.path = filepath
        pass

    def save_to_file(self, buffer) -> None:
        pass

class SaverTxt:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save_to_file(self, buffer):
         with open(self.filepath, "a") as file:
            for timestamp, name, value in buffer:
                file.write(f"{timestamp} {name} {value}\n")
            buffer.clear()

class SaverCsv:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save_to_file(self, buffer):
        with open(self.filepath, "a") as file:
            for timestamp, name, value in buffer:
                file.write(f"{timestamp};{name};{value}\n")
            buffer.clear()

class Statsd:
    def __init__(self, saver: Protocol_Saver, buffer_limit: int):
        self.saver = saver
        self.buffer_limit = buffer_limit
        self.buffer = []

    def incr(self, name: str):
        self._add_metric(name, 1)

    def decr(self, name: str):
        self._add_metric(name, -1)

    def _add_metric(self, name: str, value: int):
        utc_now = datetime.now(pytz.utc)
        timestamp = utc_now.strftime("%Y-%m-%dT%H:%M:%S%z")
        self.buffer.append((timestamp, name, value))

        if len(self.buffer) >= self.buffer_limit:
            self._evacuate()

    def _evacuate(self):
        self.saver.save_to_file(self.buffer)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._evacuate()
        self.buffer.clear()

def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    if not path.endswith('.txt'):
        raise ValueError("File must be a .txt or .csv file.")
    if not os.path.isfile(path):
        create_file(path)
    saved_element = SaverTxt(path)
    return Statsd(saved_element, buffer_limit)

def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    if not path.endswith('.csv'):
        raise ValueError("File must be a .txt or .csv file.")
    if not os.path.isfile(path):
        create_file(path)
    if os.path.getsize(path) == 0:
        with open(path, "a") as file:
            file.write("Timestamp;Name;Value\n")
    saved_element = SaverCsv(path)
    return Statsd(saved_element, buffer_limit)