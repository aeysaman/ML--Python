import csv
from objects import Element, Node, Tree
from RandomForest import RF
from IO import readIn, export
from portfolios import genPortfolios, printInfo, classifyAll

in_file = "GE-test.csv"
out_file = "test-output.csv"
pred_field = "prediction"
rtn_amt = 1.1
fields = ["EV/EBITDA", "ROIC", "Operating Margins", "Revenue_stdev_8", "Earnings Per Share_stdev_8"]
rtn_f = "fwd_rtn_8"
k = 4
n_RF = 3

(es, all_fields) = readIn(in_file, fields)
future = readIn("GE-test predict.csv", fields)[0]

classes = classifyAll(es, rtn_f, rtn_amt)

rf = RF(es, fields, k, n_RF)
rf.genAll()

predictions = {e : rf.predict(e) for e in future}

for (e, c) in predictions.iteritems():
    e.data[pred_field] = c

all_fields.append(pred_field)

portfolios = genPortfolios(predictions, classes)

printInfo(portfolios, classes, rtn_f)

export(out_file, all_fields, predictions)
print("all done")
