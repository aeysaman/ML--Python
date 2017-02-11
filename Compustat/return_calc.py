from objects import quarterDate
from datetime import timedelta
from errors import throwError

price = "data14"
div = "data16"
adjustment = "data17"

def getFwdRtns(sec, q, n, index):
    if ( n <=0):
        return 1
    x = sec.elements
    curr_q = q.toString()
    curr_date = x[curr_q].date
    futr_q = q.iterate(1).toString()
    
    if ( not testRtns(x, curr_q, futr_q)):
        return 1
    
    curr_price = float(x[curr_q].raw[price])
    futr_price = float(x[futr_q].raw[price])
    dividend = float(x[curr_q].raw[div])
    curr_adj = float(x[curr_q].raw[adjustment])
    futr_adj = float(x[curr_q].raw[adjustment])

    curr_index = getIndex(index, x[curr_q].date)
    futr_index = getIndex(index, x[futr_q].date)

    rtn = (futr_price *(curr_adj / futr_adj) - curr_price + dividend) / curr_price
    index_rtn = (futr_index - curr_index) / curr_index
    alpha = rtn - index_rtn
    
    #print (curr_q + ' c-p: {0}  f-p: {1}  d: {2} => rtn: {3}'.format(curr_price, futr_price, dividend, rtn))
    return (1 + alpha) * getFwdRtns(sec, q.iterate(1), n-1, index)

def getIndex(index, date):
    if date in index:
        return float(index[date])
    for i in range(10):
        if date + timedelta(1) in index:
            return float(index[date + timedelta(1)])
        if date - timedelta(1) in index:
            return float(index[date - timedelta(1)])

#simplify the below
def testRtns(x, c_qtr, f_qtr):
    name = x[c_qtr].name
    for (q, foo) in [(c_qtr, "current"), (f_qtr, "future")]:
        if (not q in x):
            throwError(foo + " data not found", name, q, "rtns", "")
            return False
        if (not price in x[q].raw):
            throwError(foo + " price not found", name, q, "rtns", "")
            return False
    return True

##db = org_Data(read_Data('test_data EXPRS.csv'))
##
##sec = db.get("EXPRESS SCRIPTS INC")
##
##print( getFwdRtns(sec, quarterDate(2003, 3), 3) - 1)
