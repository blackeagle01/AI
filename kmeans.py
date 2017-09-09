from sklearn.datasets import make_blobs
import numpy as np
import random
from sklearn.cluster import KMeans
X,Y=make_blobs(n_features=5)
m=len(X)
k=3
km=KMeans(n_clusters=3).fit(X)
print(km.predict(X))
minloss=float('inf')
def mindistindex(x):
	d=np.sqrt(np.sum((cluster_centroids-x)**2,axis=1))
	d=d.tolist()
	return d.index(min(d))
def kmeans(X,k):
	c={}
	global cluster_centroids
	u={i:[] for i in range(k)}
	for _ in range(300):
		for i,x in enumerate(X):
			c[i]=mindistindex(x)
			u[c[i]].append(x)
		cluster_centroids=np.array([np.mean(v,axis=0) for v in u.values() ])
	return c.values()
def loss(c,cluster_centroids):
	new=np.array([cluster_centroids[i] for i in c])
	return np.sum(np.sum((X-new)**2,axis=1))/m
for _ in range(10):
	indicies=random.sample(range(m),3)
	cluster_centroids=np.array([X[i] for i in indicies])
	c=kmeans(X, k)
	los=loss(c, cluster_centroids)
	if los<minloss:
		minloss=los
		di=c
di=np.array(list(di))
print(di)




