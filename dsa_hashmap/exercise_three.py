#!/bin/usr/env python3
special_characters = [
    ",",
    ".",
    ";",
    ":",
    "!",
    "—",
    "\n",
]
word_bank = {}

with open("poems.txt") as peom_file:
    for row in peom_file:
        arr_row = []
        for s in special_characters:
            arr_row = row.replace(s, "").split(" ")
        for word in arr_row:
            if word in word_bank:
                word_bank[word] = word_bank[word] + 1
            else:
                word_bank[word] = 1

print(word_bank)
