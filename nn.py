import numpy as np
np.random.seed(1)
class NeuralNet(object):
	def __init__(self):
		self.inputlayer=6
		self.hiddenlayer=4
		self.outputlayer=1
	def nonlin(self,z,deriv=False):
		if deriv==True:
			return z*(1-z)
		else:
			return 1/(1+np.exp(-z))
	def train(self,inputs,outputs):
		self.syn0=2*np.random.rand(self.inputlayer,self.hiddenlayer)-1
		self.syn1=2*np.random.rand(self.hiddenlayer,self.outputlayer)-1 
		for i in range(6000):
			le=np.dot(inputs,self.syn0)
			l1=self.nonlin(le)
			lf=np.dot(l1,self.syn1)
			l2=self.nonlin(lf)
			l2_error=outputs-l2
			l2_delta=l2_error*self.nonlin(l2,True)
			l1_error=np.dot(l2_delta,self.syn1.T)
			l1_delta=l1_error*self.nonlin(l1,True)
			self.syn1+=np.dot(l1.T,l2_delta)
			self.syn0+=np.dot(inputs.T,l1_delta)
	def think(self,a):
		l1=self.nonlin(np.dot(a,self.syn0))
		l2=self.nonlin(np.dot(l1,self.syn1))
		return l2
nn=NeuralNet()
inputs=np.random.randint(0,2,180).reshape(30,6)
outputs=np.array([[(i[0] and i[1]) for i in inputs]]).T
nn.train(inputs,outputs)
print(nn.think([[1,1,1,1,1,1]]))