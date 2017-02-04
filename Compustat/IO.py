import csv
from objects import element,security

#reads data dictionary from file_name into a list of qrtr objects
def read_Data(file):
    print(file +":", end = '\n')
    with open(file) as f:
        return [element(row) for row in csv.DictReader(f) if len(row['rdqe']) >3]

#goes through list of qrtrs and stores into a list of secs
def org_Data(ls):
    result = {i : security(i) for i in [i.name for i in ls]}
    for i in ls:
        result[i.name].elements[i.getQrtrStr()] = i

    return result

def export(file, elements, terms):
    with open(file, 'w', newline = "") as csvfile:
        writer = csv.DictWriter(csvfile,delimiter = ",", fieldnames = terms)
        writer.writeheader()
        for e in elements:
            writer.writerow(e.clean)

def read_Fields(file):
    print (file + ":\n")
    with open(file) as f:
        return {row["Field"] : row["Calculations"].split(";") for row in csv.DictReader(f)}


