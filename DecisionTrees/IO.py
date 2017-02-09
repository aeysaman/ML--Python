import csv
from objects import Element

def readIn(f, fields):
    with open(f) as file:
        reader = csv.DictReader(file)
        return ([Element(row, fields) for row in reader], reader.fieldnames)

def export(file_name, fields, es):
    with open(file_name, 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        for e in es:
            writer.writerow(e.data)
