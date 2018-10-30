features = [[140,1], [130,1], [150,0], [170, 0]]
labels = [0,0,1,1]
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[190,0],[160,0],[125,1]]))

# target_names = ['Apple', 'orange']
# features_name = ['weight', 'texture']
# from sklearn.externals.six import StringIO
# import pydot
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file=dot_data,
#  feature_names=features_name,
#  class_names=target_names,
#  filled=True, rounded=True,
#  impurity=False)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# graph[0].write_pdf("fruit.pdf")