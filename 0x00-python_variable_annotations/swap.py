#!/usr/bin/env python3

list = [6, 5, 7, 9, 13, 3]
temp_list = []

for i in range(len(list)):
    if list[i] > list[i + 1]:
        list[i] = list[i + 1]
        list[i + 1] = list[i]
        print(list)
