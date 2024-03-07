#!/bin/usr/env python3
import csv
from typing import List


jan_arr: List[int] = []
with open("nyc_weather.csv", "r") as f:
    csv_file = csv.reader(f)
    for idx, row in enumerate(csv_file):
        if idx > 0:
            jan_arr.append(int(row[1]))


def avg_temp(n: int):
    total = 0
    if n > len(jan_arr):
        print("Out of range")
    else:
        for i in range(n):
            total = total + jan_arr[i]

    return format(total/n, ".2f")

print(avg_temp(10))