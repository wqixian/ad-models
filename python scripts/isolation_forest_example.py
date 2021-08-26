from sklearn.ensemble import IsolationForest
import numpy as np
from sklearn2pmml import PMMLPipeline, sklearn2pmml, make_pmml_pipeline
from pypmml import Model

X = np.array([[-1, -2], [-3, -3], [-3, -4], [0, 0], [1, 1], [0, 2]])
model = IsolationForest(n_estimators=10)
model.fit(X)

pmml_pipeline = PMMLPipeline([
    ("iforest", model)
])

sklearn2pmml(pmml_pipeline, "isolation_forest_model.pmml")

# pulling the model and predicting on new datapoints
model = Model.fromFile('isolation_forest_model.pmml')
result = model.predict(
    [[0, -1], [20, 30]]
)

print('prediction: ', result)
