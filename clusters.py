import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def read_points():
    coords_file = open("coordinates.txt", "r+")
    address_file = open("addresses.txt", "r+")

    points = []
    arr = []
    for idx in range(40):
        line = coords_file.readline()
        address = address_file.readline()
        lat = float(line[:line.index(",")])
        lng = float(line[line.index(",") + 1:])
        points.append([lat, lng])
        arr.append(address)
    return [arr, np.array(points)]


def distance(p1,p2):
    return np.sqrt(np.sum((p1-p2)**2))

def assign_clusters(X, clusters):
    for idx in range(X.shape[0]):
        dist = []
          
        curr_x = X[idx]
          
        for i in range(k):
            dis = distance(curr_x,clusters[i]['center'])
            dist.append(dis)
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(curr_x)
    return clusters

def update_clusters(X, clusters):
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0] > 0:
            new_center = points.mean(axis =0)
            clusters[i]['center'] = new_center
              
            clusters[i]['points'] = []
    return clusters

def pred_cluster(X, clusters):
    pred = []
    for i in range(X.shape[0]):
        dist = []
        for j in range(k):
            dist.append(distance(X[i],clusters[j]['center']))
        pred.append(np.argmin(dist))
    return pred

k = 2
  
clusters = {}
X = read_points()

for idx in range(k):
    center = 2*(2*np.random.random((X[1].shape[1],))-1)
    cluster = {
        'center' : center,
        'points' : []
    }
      
    clusters[idx] = cluster


clusters = assign_clusters(X[1], clusters)
clusters = update_clusters(X[1], clusters)
pred = pred_cluster(X[1], clusters)

for i in X[1]:
    plt.scatter(i[0], i[1])
plt.grid(True)
center = clusters[1]['center']
origin = [40.3988747, -79.7551241]
plt.scatter(center[0], center[1], marker = '*', c = 'red')
plt.scatter(origin[0], origin[1], marker = "*", c = 'yellow')
points = [[40.4297, -79.6444], [40.4362, -79.8662]]


plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'bo', linestyle="--")
outfile = open("clusters.txt", "r+")
outfile.write("Cluster 1:\n")
for i in range(len(X[1])):
    # Slope of the line splitting the clusters
    if X[1][i][1] < (-34.33422333033507 * X[1][i][0]) + 1308.479321430095:
        outfile.write(str(X[0][i]))

outfile.write("\nCluster 2:\n")
for i in range(len(X[1])):
    # Slope of the line splitting the clusters
    if X[1][i][1] > (-34.33422333033507 * X[1][i][0]) + 1308.479321430095:
        outfile.write(str(X[0][i]))
plt.show()