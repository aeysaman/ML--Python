import csv
from IO import read_Data, org_Data, export, read_Fields
from fin_stats import getY
from access import getAllwLastNQ, query
from return_calc import getFwdRtns
from objects import element
from errors import closeErrorFile

in_file = "test_data GE.csv"
out_file = "output.csv"
fields_file = "fields.csv"

ns = {4, 8}
rs = {1, 2, 4, 8}

#read Data
db = org_Data(read_Data(in_file))
fields = read_Fields(fields_file)

#input ratios & fwd returns
for name in db:
    sec = db[name]
    for qStr in sec.elements:
        e = sec.elements[qStr]
        e.clean = {f: getY(e,f) for f in fields}
        e.clean.update({"fwd_rtn_{}".format(r) : getFwdRtns(sec, e.quarter, r) for r in rs})
        
#input calculations and move name/qrtr into clean for export
elements = getAllwLastNQ(db, max(ns))
for e in elements:
    e.clean.update({"{}_{}_{}".format(f, c, n) : query(db, e, n, f, c) for f in fields for c in fields[f] for n in ns})
    e.clean.update({"name" : e.name, "qrtr" : e.getQrtrStr(), "date" : e.getDateStr(), "industry" : e.raw["iname"]})

#build terms list
terms = ["name", "qrtr", "date", "industry"]
terms.extend([f for f in fields])
terms.extend(["{}_{}_{}".format(f, c, n) for f in fields for c in fields[f] for n in ns])
terms.extend(["fwd_rtn_{}".format(r) for r in rs])

print(terms)

#export
export(out_file, elements, terms)
                
closeErrorFile()
print("done")
