

def genPortfolios(predictions, classes):
    return { c : buildPort(predictions, c) for c in classes}

def buildPort(preds, c):
    return [e for (e, v) in preds.iteritems() if v == c]

def printInfo(portfolios, classes, rtn_f):
    for c in classes:
        l = len(portfolios[c])
        if(l <1):
            continue
        s = sum([float(p.data[rtn_f]) for p in portfolios[c]])
        print("{} {} {}".format(c, l, s / l))

def classifyAll(es, rf, amount):
    for e in es:
        if float(e.data[rf]) >=amount:
            e.classify("G")
        else:
            e.classify("B")
    return ["G", "B"]
