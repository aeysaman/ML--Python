from objects import quarterDate
from statistics import stdev, mean
from errors import throwError

#returns the elements which are n quarters previous to current, including current
def getLastNQs (sec, q, n):
    if(n<=0):
        return None
    if (n==1):
        result = list()
    else:
        result = getLastNQs(sec, q.iterate(-1), n-1)
    result.append(sec.elements.get(q.toString()))
    return result

#returns True if the data contains elements that have n previous quarters
def hasLastNQs(sec, q, n):
    return not any([y is None for y in getLastNQs(sec, q, n)])

#returns list of all elements that have n prev quarters
def getAllwLastNQ(db, n):
    return [db[name].elements[d] for name in db for d in db[name].elements if hasLastNQs(db[name], db[name].elements[d].quarter, n)]

def growth_rate(ls):
    time = len(ls) -1                                       
    return (1 + (ls[time] - ls[0]) / abs(ls[0])) ** (4 / time) -1

#calculates the avg/stdev of a specific security at some point in time
def query (db, e, n, field, calc):
    try:
        result = [x.clean[field] for x in getLastNQs(db[e.name], e.quarter, n)]
        if calc == "avg":
            return mean(result)
        if calc == "stdev":
            return stdev(result)
        if calc == "grth":
            return growth_rate(result)
    except (ZeroDivisionError, TypeError) as err:
        throwError(err, e.name, e.getQrtrStr(), field, calc)
        print ("couldn't get calc '{}' of '{}' at {}".format(calc, field, e.toString()))
        return None
