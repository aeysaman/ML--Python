import math
import copy

def formPorts(data, cs):
    return {c : buildPort(data, c) for c in cs}

def buildPort(preds, c):
    return [e for (e, v) in preds.iteritems() if v == c]

def printInfo(portfolios, classes, rtn_f):
    for c in classes:
        l = len(portfolios[c])
        if(l <1):
            continue
        s = sum([float(p.data[rtn_f]) for p in portfolios[c]])
        print("class:{} size:{} avg rtn:{}".format(c, l, s / l))

##def classifyAll(es, rf, amount):
##    for e in es:
##        if float(e.data[rf]) >=amount:
##            e.classify("G")
##        else:
##            e.classify("B")
##    return ["G", "B"]

def classifyAll(es, f, ls):
    for e in es:
        for name, funct in ls:
            if funct(float(e.data[f])):
                e.classify(name)
    return list(set([ name for name, funct in ls]))

def run(rf, test, pred_f, rtn_f, cs):
    preds = {e : rf.predictWeighted(e, cs) for e in test}

    for e, c in preds.iteritems():
        e.data[pred_f] = c

    ports =  formPorts(preds, cs)
##    printInfo(ports, cs, rtn_f)
    return preds, ports

class Qrtr:
    def __init__(self, y, q):
        self.y = int(y)
        self.q = int(q)
    def iterate(self, n):
        y = self.y + math.floor((self.q + n - 1) / 4)
        q = (self.q + n - 1) % 4 + 1
        return Qrtr(y, q)
    def toString(self):
        return str(self.y) + "-" + str(self.q)

def parseQ(foo):
    (y, q) = foo.split("-")
    return Qrtr(y, q)

def getNprev(qs, q, n):
    if(n==0):
        return []
    return [x for x in qs if q.iterate(-1).toString() == x.toString()] + getNprev(qs, q.iterate(-1), n-1)

def genPeriods(es, n):
    allDates = [parseQ(x) for x in set([x.data["qrtr"] for x in es])]
    unfiltered = {x : getNprev(allDates, x, n) for x in allDates}
    filtered = {x : y for x,y in unfiltered.iteritems() if len(y)==n}
    return filtered

def splitData(pers, es):
    data = list()
    for x, y in pers.iteritems():
        test = [copy.deepcopy(z) for z in es if x.toString() == z.data["qrtr"]]
        train = [copy.deepcopy(z) for z in es for w in y if w.toString() == z.data["qrtr"]]
        data.append((x, test, train))
    return data

def calcRtn(vals, rtn_f):
    if len(vals) ==0:
        return None
    else:
        return sum([float(x.data[rtn_f]) for x in vals])/ len(vals)

def printPorts(ports, cs, rtn_f):
    for c in cs:
        avg = [ (q.toString(), calcRtn(ls[c], rtn_f), len(ls[c])) for q, ls in ports.iteritems()]
        product = reduce(lambda x, y: x*y, [x for q,x,s in avg if x is not None])
        print ("Class:{} Rtn:{}".format(c,product))
        print(len(avg))
        for (q, x, s) in avg:
            print ( "Q:{} Rtn:{} Size:{}".format(q, x, s))

def genGroups(es, terms):
    return [(name, [copy.deepcopy(e) for e in es if funct(e.data)]) for name, funct in terms]
