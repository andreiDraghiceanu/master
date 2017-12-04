import os
import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    print(csv_data)
    '''We don't want headers or first line of bad data'''
    next(csv_data)
    next(csv_data)

    # print(list(csv_data))

    for line in csv_data:
        name = line[0], line[1]
        names.append(name)

    for n in names:
        print(n)

