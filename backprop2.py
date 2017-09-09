import numpy as np
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
class NeuralNet(object):
	def __init__(self):
		self.inputlayers=5
		self.hiddenlayers=4
		self.outputlayers=1
		self.theta1=0.01*np.random.randn(5,4)
		self.theta2=0.01*np.random.randn(4,1)
	def activate(self,z,deriv=False):
		if deriv==True:
			return 1-z**2
		else:
			return np.tanh(z)
	def train(self,inputs,outputs):
		for i in range(1000):
			z2=np.dot(inputs,self.theta1)
			a2=self.activate(z2)
			z3=np.dot(a2,self.theta2)
			a3=self.activate(z3)
			l3_error=outputs-a3
			l3_delta=l3_error*self.activate(a3,True)
			l2_error=np.dot(l3_delta,self.theta2.T)
			l2_delta=l2_error*self.activate(a2,True)
			self.theta2+=np.dot(a2.T,l3_delta)
			self.theta1+=np.dot(inputs.T,l2_delta)
	def predict(self,inputs):
		z2=np.dot(inputs,self.theta1)
		a2=self.activate(z2)
		z3=np.dot(a2,self.theta2)
		a3=self.activate(z3)
		print(a3)
nn=NeuralNet()
d=load_iris()
X_train,X_test,Y_train,Y_test=train_test_split(d.data,d.target)
nn.train(X_train, Y_train)
