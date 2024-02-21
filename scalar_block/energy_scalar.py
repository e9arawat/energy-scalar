"""
rtm
"""

import csv
import os
from answer import answer


def create_csv_file(block_scalar):
    """
    creates a csv file
    """
    with open("energy_scalar.csv", "w", encoding="utf-8", newline="") as f:
        fieldnames = ["date", "energy_scalar"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in block_scalar:
            writer.writerow(row)


def solver():
    """
    Creates a csv file with TBn revenue
    """
    file_path = os.path.abspath("hourly_prices.csv")
    with open(file_path, "r", encoding="utf-8-sig") as f:
        csv_reader = csv.DictReader(f)
        data = list(csv_reader)
        _data = []
        for x in data:
            _data.append({"date": x["date"], "price": float(x["price"])})
        block_scalar = []
        index = 0
        months = [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ]
        month = 0
        while index < len(_data):
            year = _data[index]["date"][:4]
            month_data = [
                d for d in _data if d["date"].startswith(f"{year}-{months[month]}")
            ]
            energy_scalar = answer(month_data)
            for row in energy_scalar:
                block_scalar.append(row)
            index += len(month_data)
            month += 1

        create_csv_file(block_scalar)


if __name__ == "__main__":
    solver()
