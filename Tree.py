from sklearn import tree
from random import randint

Tests = [[1,0,1,0,1,1,0],
[1,0,0,0,1,0,1],
[0,0,1,1,0,1,1],
[0,1,0,0,1,1,0],
[0,1,1,0,1,0,1],
[0,1,0,1,0,1,1],
[0,1,0,0,1,0,0],
[0,0,1,1,1,1,1],
[0,0,1,0,0,0,1],
[1,1,1,1,1,1,1],
[0,1,0,1,1,0,1],
[0,0,0,1,1,0,1],
[1,0,1,0,1,1,1],
[0,0,0,0,1,1,0],
[0,0,1,0,0,1,0],
[1,1,1,0,0,0,0],
[0,0,0,0,1,1,0],
[0,0,1,0,1,0,0],
[1,1,0,0,1,1,0],
[1,0,1,1,1,0,0],
[0,1,0,0,0,0,0],
[0,0,1,1,0,1,0],
[0,1,1,0,1,0,0],
[1,1,0,1,1,1,0],
[1,1,1,1,1,0,0],
[0,1,0,0,0,1,1],
[0,1,0,1,0,0,0],
[0,1,1,1,1,0,1],
[1,1,1,1,1,1,0],
[1,1,1,1,1,0,1],
[1,0,1,0,0,0,1],
[1,0,1,1,1,1,0],
[1,0,0,0,0,0,1],
[1,1,1,1,0,0,1],
[0,0,0,0,0,0,1],
[0,1,1,0,1,0,1],
[1,1,0,1,1,1,1],
[0,1,1,1,0,0,0],
[1,0,1,0,1,1,0],
[1,1,0,1,1,1,0],
[0,1,1,1,1,1,0],
[1,0,1,1,1,1,1],
[1,0,0,0,1,1,0],
[1,1,1,0,1,1,1],
[0,0,0,0,1,0,1],
[1,0,1,1,0,0,1],
[1,1,1,0,1,1,1],
[0,1,1,0,0,1,1],
[0,1,0,0,0,0,1],
[0,1,0,0,1,1,1],
[1,1,1,1,1,0,0],
[1,1,0,0,1,1,1],
[0,1,1,1,0,1,1],
[0,1,0,1,1,0,1],
[1,1,1,0,0,0,0],
[0,0,0,0,0,0,1],
[0,1,0,0,0,1,0],
[0,0,1,0,1,0,1],
[0,1,1,1,1,0,1],
[0,1,0,0,1,1,1],
[1,1,1,0,0,0,0],
[1,0,1,0,1,1,1],
[1,1,0,1,1,0,0],
[1,1,1,0,0,0,0],
[1,1,0,0,1,0,0],
[0,1,0,0,0,1,1],
[1,0,0,0,0,1,0],
[1,1,0,0,0,1,0],
[0,0,1,1,0,0,1],
[1,0,0,1,0,0,0],
[0,0,0,0,1,1,0],
[0,0,0,0,1,0,0],
[0,0,0,0,1,0,1],]

TestScore=[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(Tests,TestScore)
# wywołanie : clf.predict([[0,0,0,0,0,0,0]])
# output: 0-wróć później, 1-rozbrajaj