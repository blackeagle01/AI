import numpy as np
m=300
X=[np.random.random(5) for i in range(m)]
for i,_ in enumerate(X):
	X[i]=np.insert(X[i],0,1)
X=np.array(X)
rfeatures=np.array([2,90,6,89,10,19])
y=np.dot(rfeatures,X.T)
theta=np.random.random(6)
def hyp(X,):
	return np.dot(theta,X.T)
def loss(X,y):
	return (np.sum((hyp(X)-y)**2))/(2*m)
def train():
	global theta
	while loss(X, y)>np.exp(-44):
		theta1=theta.copy()
		theta1=theta1-0.09*(((hyp(X)-y).reshape(1,m)*X.T).sum(axis=1))/300
		theta=theta1
#print((((hyp(X)-y).reshape(1,3)*X.T)).sum(axis=1))
train()
print(loss(X, y))
print(theta)


