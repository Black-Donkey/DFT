from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.tree import export_graphviz
from six import StringIO
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
import pydotplus
import shap
import os

'''
    This file is the python script to train regression models.
'''

# Run this to add the path to the graphviz package
os.environ['PATH'] = os.environ['PATH'] + ';' + r"C:\Program Files\Graphviz\bin"

# Load the data
data = pd.read_csv('energetics.csv')

# Print the first 5 rows of the dataframe
print(data.head())

# Prepare the data for the model
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

x = pd.DataFrame(X)
vif = [variance_inflation_factor(x.values, x.columns.get_loc(i)) for i in x.columns]
rDf = x.corr()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=587)

'''
    Random Forest model
'''

# Create the model
regressor = RandomForestRegressor(n_estimators=200, min_samples_split=2, min_samples_leaf=1,
                                  max_features='auto', max_depth=100, bootstrap=True, random_state=587)

pipe = Pipeline([('scaler', StandardScaler()), ('reduce_dim', PCA()), ('regressor', regressor)])
pipe.fit(X_train, y_train)
y_pred_RF = pipe.predict(X_test)

dot_data = StringIO()
export_graphviz(pipe.named_steps['regressor'].estimators_[0], out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')

importance = list(regressor.feature_importances_)
# List of tuples with variable and importance

# Saving feature names for later use
feature_list = list(data.columns)[1:-1]

# Set the style
plt.style.use('bmh')
# list of X locations for plotting
X_values = list(range(len(importance)))
# Make a bar chart
plt.bar(X_values, importance, orientation='vertical')
# Tick labels for X aXis
plt.xticks(X_values, feature_list, rotation=6)
# AXis labels and title
plt.ylabel('Importance')
plt.xlabel('Variable')
plt.title('Variable Importance')
plt.show()

RF_r2score = r2_score(y_test, y_pred_RF)
RF_mse = mean_squared_error(y_test, y_pred_RF)
print("RF r2 score is ", RF_r2score)
print("RF mse is ", RF_mse)

# kf = KFold(n_splits=10)
# kf.get_n_splits(X)
# KFold(n_splits=10, random_state=None, shuffle=True)
# for train_indeX, test_indeX in kf.split(X):
# X_train, X_test = X[train_indeX], X[test_indeX]
# y_train, y_test = y[train_indeX], y[test_indeX]
# creating an object of LinearRegression class

'''
    Multi-Linear Regression model
'''

LR = LinearRegression()
# fitting the training data
LR.fit(X_train, y_train)
y_pred_MLR = LR.predict(X_test)
# predicting the accuracy score
MLR_r2score = r2_score(y_test, y_pred_MLR)
MLR_mse = mean_squared_error(y_test, y_pred_MLR)
print("MLR r2 score is ", MLR_r2score)
print("MLR mse is ", MLR_mse)

'''
    Support Vector Machine (SVM) model
'''

clf = SVR(kernel='rbf')
clf.fit(X_train, y_train)
y_pred_SVM = clf.predict(X_test)

SVM_r2score = r2_score(y_test, y_pred_SVM)
SVM_mse = mean_squared_error(y_test, y_pred_SVM)
print("SVM r2 score is ", SVM_r2score)
print("SVM mse is ", SVM_mse)

'''
    XGBoost model
'''
xgb_model = xgb.XGBRegressor(objective="reg:squarederror", max_depth=100, learning_rate=0.05, n_estimators=200,
                             random_state=587)
xgb_model.fit(X_train, y_train)
y_pred_XGB = xgb_model.predict(X_test)
XGB_r2score = r2_score(y_test, y_pred_XGB)
XGB_mse = mean_squared_error(y_test, y_pred_XGB)
print("XGB r2 score is ", XGB_r2score)
print("XGB mse is ", XGB_mse)

'''
    Shapley values
'''
cols = list(data.columns)[1:-1]
explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(data[cols])
shap.summary_plot(shap_values, data[cols])
shap.summary_plot(shap_values, data[cols], plot_type="bar")