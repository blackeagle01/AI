import numpy as np
np.random.seed(0)
inputs=np.random.randint(1,100,1000)
outputs=np.array([2*i+3 for i in inputs])
print(inputs[3],outputs[3])d
b,m=4,5
learning_rate=0.2
for i in range(1000):
	objective=m*inputs+b
	error=(1/2000)*np.sum((objective-outputs)**2)
	if i==999:
		print(error)
	b=b- learning_rate*(1/1000)*np.sum((objective - outputs))
	m=m- learning_rate*(1/1000)*np.sum((objective - outputs)*inputs)
print(b,m)
