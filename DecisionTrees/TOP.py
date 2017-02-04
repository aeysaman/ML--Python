import csv
from objects import Element, Node, Tree


def readIn(f):
    with open(f) as file:
        return [Element(row, fields) for row in csv.DictReader(file)]

def classifyAll(es, rf, amount):
    for e in es:
        if float(e.data[rf]) >=amount:
            e.classify("G")
        else:
            e.classify("B")

in_file = "test.csv"
rtn_field = "Return"
rtn_amt = .05
fields = ["P/E", "P/B", "ROIC"]
rtn_f = "Return"
k = 4


es = readIn("test.csv")

classifyAll(es, rtn_f, rtn_amt)

for e in es:
    print("{} {}".format(e.grp, e.data))


t = Tree(es, fields, k)
t.split()
t.printTree()
