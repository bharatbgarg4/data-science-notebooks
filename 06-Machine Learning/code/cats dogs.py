features = [[1000,30], [1200,40], [2000,60], [1800, 80]]
labels = [0,0,1,1]
from sklearn import tree,svm
# clf = svm.LinearSVC()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[1700,70],[1100,50]]))



[1,2,3,4]
[5,6,7,8]
.
.
.
[97,98,99,100]


25*4