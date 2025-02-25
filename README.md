# 2025-GIH

##**Overview**
**QuickDepth** is an AI algorithm designed to predict the **combinational logic depth** of signals in RTL designs. Timing analysis is complex IP/SoCs can be very **time-consuming process** because it requires a **full synthesis run**. The following model speeds up this process by predicting the **logic depth using a Decision Tree Regressor**, enabling early detection of potential timing violations and reducing overall design delays.

---

**Problem Statement**
Timing analysis is a crucial step in **IP/SoC design** and is often **slow**.
If a design has **time violations**, it may require **architectural changes** which may cause further **delays**. 
The following project addresses this by predicting the **combinational logic depth** directly from behavioral RTL. This prediction allows designers for early **detection of potential timing issues** and **streamlining the design process**.

---

**Project Blueprint**

**A. `dataset.csv`**
It contains the dataset with the following columns :
-**Module Name**
-**Signal Name**
-**Gates**
-**Fan-In**
-**Fan-Out**
-**Depth**


**B. `train_model.py`**
-Script loads and preprocesses the dataset
-Splits the data training and testing sets, 
-Trains the Decision Tree Regressor, 
-Evaluates the model performance using mutiple metrics, and 
-Saves the trained model as model.joblib.

**C. `predict.py`**
-Loads the saved model and makes predictions on new input data. 
-The input must be the feature of the order used during training.

**D. `model.joblib`**
-The automatically generated serialzed trained model by train_model.py.

**E. `README.md`** 
-It provides the overview of the project.

**Environment Setup**

The following project requires the latest version of the Python and requires the following libraries :

A. pandas

B. numpy

C. scikit-learn

D. joblib

**How to Run the Project**

A. Train the Model

a. Ensure that the dataset.csv file is in the same directory as train_model.py.

b. On running the train_model.py 

~The dataset will get loaded and preprocessed and will use the numberic columns (Gates,Fan-In and Fan-Out) as the prdictors.

~The data will be split in training (80%) and testing (20%) sets.

~The Decision tree Regressor will be trained and performance metrics (Mean Absolute Error,Mean Square Error, Root Mean Square Error and R2 Score) will be calculated.

~And finally the model will be saved in model.joblib.

B. Making Predictions using the predict.py script and make changes in the input as needed by you.
  
  
