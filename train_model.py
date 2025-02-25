import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor  
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from joblib import dump

df = pd.read_csv("dataset.csv")

X = df.drop(columns=["Module Name", "Signal Name", "Depth"])
Y = df["Depth"]

print("Training Features:", X.columns.tolist())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

dump(model, "model.joblib")
print("Model saved as model.joblib")

mae   = mean_absolute_error(Y_test, Y_pred)
mse   = mean_squared_error(Y_test, Y_pred)
rmse  = np.sqrt(mse)
r2    = r2_score(Y_test, Y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R2) Score: {r2}")
