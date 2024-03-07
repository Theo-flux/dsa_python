import csv
from typing import Dict


jan_dict: Dict[str, int] = {}
with open("nyc_weather.csv", "r") as f:
    csv_file = csv.reader(f)
    for idx, row in enumerate(csv_file):
        if idx > 0:
            jan_dict[row[0]] = int(row[1])

print(jan_dict["Jan 9"])
print(jan_dict["Jan 4"])
