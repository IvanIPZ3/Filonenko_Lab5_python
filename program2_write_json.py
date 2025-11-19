# program2_write_json.py
# -*- coding: utf-8 -*-

"""
Program 2: Write Ukrainian names to JSON file with UTF-8 encoding.

Dictionary structure:
    {
        "Surname": ["First name", "Patronymic", year_of_birth],
        ...
    }

All records are in Ukrainian. JSON is saved with ensure_ascii=False so that
characters stay readable in a text editor.
"""

import json
import os

DATA_DIR = "data"
OUTPUT_PATH = os.path.join(DATA_DIR, "people.json")


def build_people_dict():
    """Return example dictionary with at least 10 Ukrainian records."""
    return {
        "Філоненко": ["Іван", "Олександрович", 2004],
        "Шевченко": ["Марія", "Ігорівна", 2005],
        "Петренко": ["Олег", "Сергійович", 2003],
        "Бондар": ["Ірина", "Петрівна", 2004],
        "Сидоренко": ["Артем", "Борисович", 2005],
        "Ковальчук": ["Юлія", "Андріївна", 2004],
        "Гриценко": ["Тарас", "Миколайович", 2003],
        "Яременко": ["Єлизавета", "Романівна", 2005],
        "Євченко": ["Ілля", "Олегович", 2004],
        "Їжак": ["Ївга", "Артемівна", 2003],
    }


def main():
    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    people = build_people_dict()

    # Write JSON with UTF-8 and readable Cyrillic characters
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(people, f, ensure_ascii=False, indent=4)

    print(f"Файл {OUTPUT_PATH} успішно створено.")


if __name__ == "__main__":
    main()
