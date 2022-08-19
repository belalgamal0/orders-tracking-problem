import csv
from typing import Iterable
from pandas import *


class FileMethod:
    header_row = ["id", "location", "product", "quantity", "brand"]

    @classmethod
    def add_header(cls, file_path: str):
        with open(file_path, newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]
        with open(file_path, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(cls.header_row)
            w.writerows(data)

    @classmethod
    def read_input_file(cls, file_path: str):
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            file_header = next(reader)
        if file_header != cls.header_row: cls.add_header(file_path)
        return read_csv(file_path, on_bad_lines='skip')

    @classmethod
    def write_output_file(cls, file_path: str, output_data: [Iterable]):
        with open(file_path, 'w', encoding='UTF8') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(output_data)
