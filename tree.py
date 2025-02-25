import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.tree import export_graphviz
for pydotplus import graph_from_dot_data
form joblib import load

model=load("model.joblib")
features=["Gates","Fan-In","Fan-Out"]

data=export_graphviz(model, filled=True, feature_names=features, out_file=none)

graph=graph_from_dot_data(dot_data)
graph.write_pnd("DecisionTreeRegressor.png")

image=mpimg.imread("DecisionTreeRegressor.png")
plt.figure(figsize=(12,8))
plt.show(image)
plt.axis("off")
plt.show()
