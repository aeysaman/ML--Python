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

def genTree(es, fs, k):
##    print (fs)
    tree = Tree(es, fs, k)
    tree.split()
##    tree.printTree()
##    print(tree.errorRate())
    return tree

def getRandSubset(fs, n):
    return [random.sample(fs, int(sqrt(len(fs)))) for _ in range(n)]
