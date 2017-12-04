import csv

with open('names.csv', 'r+') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # '''next() will jump over the first row'''
    # next(csv_reader)

    # with open('new_names.csv', 'w', newline='') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')

    for line in csv_reader:
        csv_reader.writerow(line['email'])
