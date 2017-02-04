from objects import Centroid, Point, assignPoints, calcD, evaluate, readPoints, assignLetters, export
import random


in_file = "test.csv"
out_file = "Clustered.csv"
info_fields = ["Name", "BirthDate"]
fields = ["IQ", "Height", "Grades"]
k = 3
n = 10
m = 5

def run():
    points = readPoints(in_file, info_fields, fields)
    centroids = [Centroid(x, fields) for x in random.sample(points, k)]
    assignLetters(centroids)
    for i in range(n):
        assignPoints(points, centroids, fields)

        for c in centroids:
            c.update(fields)

        score = evaluate(points, fields)
        print (score)
    return (score, points)

bestPoints = min([run() for range(m)], key = lambda x: x[0])

print (bestPoints)

all_fields = info_fields + fields
all_fields.append("Cluster")

export(out_file, all_fields, bestPoints[1])
