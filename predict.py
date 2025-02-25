import pandas as pd
from joblib import load

loaded_model = load("model.joblib")

new_signal = pd.DataFrame([[3, 2, 1]], columns=["Gates", "Fan-In", "Fan-Out"])

predicted_depth = loaded_model.predict(new_signal)
print("Predicted Depth:", predicted_depth[0])
