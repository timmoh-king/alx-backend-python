#!/usr/bin/env python3

list = [6, 5, 5, 7, 9, 13, 3]
max = list[0]

for i in list:
    if i > max:
        max = i
print(max)

numbers = []

for i in list:
    if i not in numbers:
        numbers.append(i)

print(numbers)
