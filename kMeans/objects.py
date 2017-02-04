from statistics import mean
import csv
#ps/p are points, cs/c are centroids, fs are fields, d is distance

class Centroid:
    def __init__(self, p, fs):
        self.points = list()
        self.features = {f:p.features.get(f) for f in fs}
    def update(self, fs):
        self.features = {f : mean([p.features.get(f) for p in self.points]) for f in fs}
    def get(self, f):
        return self.features[f]

class Point:
    def __init__(self, data, info_fields, fields): 
        self.features = {f : float(data.get(f)) for f in fields}
        self.features.update({f : data.get(f) for f in info_fields})
        self.cluster = None
    def assign(self, c):
        self.cluster = c
        self.features["Cluster"] = c.name
    def get(self, f):
        return self.features[f]

def assignPoints(ps, cs, fs):
    for p in ps:
        bestC = min([(calcD(p,c,fs),c) for c in cs], key = lambda x: x[0]) [1]
        p.assign(bestC)
        bestC.points.append(p)

def calcD(p, c, fs):
    return pow(sum([pow(p.get(f)-c.get(f), 2) for f in fs]), .5)

def evaluate(ps, fs):
    return mean([calcD(p,p.cluster, fs) for p in ps])

def readPoints(file, info_fields, fields):
    with open(file) as csvfile:
        return [Point(row, info_fields, fields) for row in csv.DictReader(csvfile)]

def assignLetters(cs):
    chars = [chr(i) for i in range(ord('a'), ord('a')+len(cs))]
    for i in range(len(cs)):
        cs[i].name = chars[i]

def export(file_name, fs, ps):
    with open(file_name, 'w', newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fs)
        writer.writeheader()
        for p in ps:
            writer.writerow(p.features)
