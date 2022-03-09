import numpy as n
import matplotlib.pyplot as p
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler


centers = [[1, 1], [-1, -1], [1, -1]]
X, ol = make_blobs(n_samples=750, centers=centers, cluster_std=0.4, random_state=0)
X = StandardScaler().fit_transform(X)

#The DBSCAN main function
def d(D, E, Mn):
    l = [0]*len(D)
    C = 0
    for P in range(0, len(D)):
        if not (l[P] == 0):
            continue
        np = rq(D, P, E)
        if len(np) < Mn:
            l[P] = -1
        else:
            C += 1
            gc(D, l, P, np, C, E, Mn)
    return l

#Calculation of the Core points
def gc(D, l, P, np, C, E, Mn):
    l[P] = C
    i = 0
    while i < len(np):
        Pn = np[i]
        if l[Pn] == -1:
            l[Pn] = C
        elif l[Pn] == 0:
            l[Pn] = C
            Pnnp = rq(D, Pn, E)
            if len(Pnnp) >= Mn:
                np = np + Pnnp
        i += 1

#Finding the points which lie less than the epsiolon
def rq(D, P, E):
    nei = []
    for Pn in range(0, len(D)):
        if n.linalg.norm(D[P] - D[Pn]) < E:
            nei.append(Pn)
    return nei

#The output color selction function
def pc(lst):
    cols = []
    for l in lst:
        if l == 1:
            cols.append('red')
        elif l == 2:
            cols.append('blue')
        elif l == 0:
            cols.append('#5ac18e')
        elif l == -1:
            cols.append('green')
        else:
            cols.append('yellow')
    return cols


col = pc(ol)
fig, ax = p.subplots()
ax.scatter(X[:, 0], X[:, 1], s=4, c=col[:])
nl = d(X, E=0.3, Mn=10)
colors = pc(nl)
fig1, yx = p.subplots()
yx.scatter(X[:, 0], X[:, 1], c=colors[:], s=10)
p.show()
