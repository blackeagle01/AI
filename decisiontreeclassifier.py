from sklearn import tree
import numpy as np
x=np.array(np.random.randint(0,2,120).reshape(20,6))
y=[i[0]^i[1]^i[2] for i in x]
clf=tree.DecisionTreeClassifier()
clf.fit(x,y)
print(clf.predict([[1,1,0,0,1,1]]))