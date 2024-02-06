import csv

def read_csv_file(filename):
    links = []
    with open(filename, mode='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            links.append(row[1])

        links.pop(0)
        return links
