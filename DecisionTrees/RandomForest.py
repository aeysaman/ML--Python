import objects
from math import sqrt
from objects import Tree
from collections import Counter
import random
import string

class RF:
    def __init__(self, es, all_fs, k, n):
        self.es = es
        self.all_fs = all_fs
        self.k = k
        self.n = n
        self.genAll()
    def genAll(self):
        self.trees = [genTree(self.es, fields, self.k) for fields in getRandSubset(self.all_fs, self.n)]
    def predict(self, x):
        preds = [t.predict(x) for t in self.trees]
        return Counter(preds).most_common(1)[0][0]
    def predictWeighted(self, x, cs):
        preds = [(t.errorRate(), t.predict(x)) for t in self.trees]
        weightedCounts = filter(lambda x: x[0] is not None, [(getAvg(preds, c), c) for c in cs])
        return min(weightedCounts, key  = (lambda z: z[0]))[1]

def getAvg(ls, c):
    foos = [i[0] for i in ls if i[1] ==c]
    if len(foos) == 0:
        return None
    return sum(foos) / len(foos)
        
def genTree(es, fs, k):
##    print (fs)
    tree = Tree(es, fs, k)
    tree.split()
##    tree.printTree()
##    print(tree.errorRate())
    return tree

def getRandSubset(fs, n):
    return [random.sample(fs, int(sqrt(len(fs)))) for _ in range(n)]
