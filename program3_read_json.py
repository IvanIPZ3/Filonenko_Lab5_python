# program3_read_json.py
# -*- coding: utf-8 -*-

"""
Program 3: Read Ukrainian names from JSON file (UTF-8) and print them.

Reads the file created by program2_write_json.py and prints all records
in a human-readable format.
"""

import json
import os

DATA_DIR = "data"
INPUT_PATH = os.path.join(DATA_DIR, "people.json")


def main():
    # Check that JSON file exists
    if not os.path.exists(INPUT_PATH):
        print(f"Файл {INPUT_PATH} не знайдено. Спочатку запустіть program2_write_json.py.")
        return

    # Read JSON with proper UTF-8 encoding
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        people = json.load(f)

    print("Дані з JSON файлу:\n")

    # Python 3.7+ keeps insertion order for dict
    for surname, (first_name, patronymic, year) in people.items():
        print(f"{surname}: {first_name} {patronymic}, {year} р.н.")


if __name__ == "__main__":
    main()
