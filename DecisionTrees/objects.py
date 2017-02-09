from collections import Counter
from math import log


class Element:
    def __init__(self, data, fs):
        self.data = data
        self.data.update({f : float(data[f]) for f in fs})
    def classify(self, grp):
        self.grp = grp

class Node:
    def __init__(self, es, tree):
        self.es = es
        self.tree = tree
    #returns best split based on highest info gain. return is tuple of (Node, Field, Amount, Score)
    def bestSplit(self):
        n = 5
        scores = {(f,x): infoGain(self.es, f, x) for f in self.tree.fs for x in genSplits(self.es, f, n)}
        best = max(scores, key = scores.get)
        return (self, best[0], best[1], scores[best])
    def split(self, info):
        (node, f, amt, score) = info
        (node.f, node.amt) = (f,amt)
        
        (node.left, lowOption) = newNode([e for e in node.es if e.data[f]<amt], node.tree)
        (node.right, highOption) = newNode([e  for e in node.es if e.data[f]>=amt], node.tree)
        return [lowOption, highOption]
    def printTree(self, n):
        if hasattr(self, "f"):
            print("{}F: {} A: {}".format(n * " ", self.f, self.amt))
            self.left.printTree(n+1)
            self.right.printTree(n+1)
        else:
            print("{} S:{} G:{}".format(n * " ", len(self.es), len([e for e in self.es if e.grp =="G"])))
    def predict(self, x):
        if hasattr(self, "f"):
            if x.data[self.f] >= self.amt:
                return self.right.predict(x)
            else:
                return self.left.predict(x)
        else:
            return majorityCount(self.es)

def newNode(es, tree):
    node = Node(es, tree)
    return (node, node.bestSplit())
                      
class Tree:
    def __init__(self, es, fs, k):
        self.es = es
        self.fs = fs
        self.k = k
    def split(self):
        self.top = Node(self.es, self)
        self.splitOptions = [self.top.bestSplit()]
        self.keepSplitting()
    def keepSplitting(self):
        for i in range(1,self.k):
            best = max(self.splitOptions, key = lambda x : x[3])
            self.splitOptions.remove(best)
            self.splitOptions.extend(best[0].split(best))
    def printTree(self):
        self.top.printTree(0)
    def predict(self, x):
        return self.top.predict(x)

def majorityCount(es):
    count = Counter([e.grp for e in es])
    return count.most_common(1)[0][0]
            
def genSplits(es, f, n):
    ls = sorted([e.data[f] for e in es])
    ran = ls[len(ls) -1] - ls[0]
    return [ls[0] + i * ran/ n for i in range (1, n)]

def infoGain(es, f, amt):
    (oScr, oCnt) = entropy(es)
    (lScr, lCnt) = entropy([e for e in es if e.data[f]<amt])
    (hScr, hCnt) = entropy([e  for e in es if e.data[f]>=amt])
    IG = oScr - (lScr * lCnt + hScr * hCnt) / oCnt
    return IG

def entropy(es):
    total = float(len(es))
    c = Counter([e.grp for e in es])
    score = -sum([count/total * log(count/total) for count in dict(c).values()])
    return (score, float(total))
