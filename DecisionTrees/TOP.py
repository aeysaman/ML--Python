import csv
import copy
from objects import Element, Node, Tree
from RandomForest import RF
from IO import readIn, export
from portfolios import run, printInfo, classifyAll, Qrtr, parseQ, getNprev, genPeriods, splitData

in_file = "Data multi.csv"
out_file = "test multi-output.csv"
pred_field = "prediction"
fields = ["EV/EBITDA", "ROIC", "Operating Margins", "Revenue_stdev_8", "Earnings Per Share_stdev_8"]
rtn_f = "fwd_rtn_8"
rtn_amt = .9    #split for classification
k = 5           #number of nodes allowed in decision treem
n_RF = 5        #number of Random Forests to generate
back = 8        #number of backward periods to train on

(es, all_fields) = readIn(in_file, fields)
future = readIn("GE-test predict.csv", fields)[0]

classes = classifyAll(es, rtn_f, rtn_amt)

all_fields.append(pred_field)

periods = genPeriods(es, back)

data = splitData(periods, es)

portfolios = dict()

for q, test, train in data:
    print("---")
    rf = RF(train, fields, k, n_RF)
    (preds, ports) = run(rf, test, pred_field, rtn_f, classes)
    portfolios[q] = ports

##export(out_file, all_fields, predictions)
print("all done")


