import objects


class BoostedDT:
    def __init__(self, es, fs, k, n):
        self.es = es
        self.fs = fs
        self.k = k
        self.n = n
    def generate(self):
        self.trees = train(


    def train(self, es, n):
        t = genTree(es, self.fs, self.k)
        errors = t.getErrors()
        if n>=1:
            return [t]
        return [t] + train(self, errors, n-1)
    
def genTree(es, fs, k):
    print (fs)
    tree = Tree(es, fs, k)
    tree.split()
    tree.printTree()
    print(tree.errorRate())
    return tree
