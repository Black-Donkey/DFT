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
import pandas as pd
import numpy as np
import pydotplus
import os

# Run this to add the path to the graphviz package
os.environ['PATH'] = os.environ['PATH'] + ';' + r"C:\Program Files\Graphviz\bin"

# Load the data
data = pd.read_csv('energetics.csv')

# Print the first 5 rows of the dataframe
print(data.head())

# Prepare the data for the model
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Create the model
regressor = RandomForestRegressor(n_estimators=800, min_samples_split=10, min_samples_leaf=2,
                                  max_features='auto', max_depth=None, bootstrap=False, random_state=0)

pipe = Pipeline([('scaler', StandardScaler()), ('reduce_dim', PCA()), ('regressor', regressor)])
pipe.fit(x_train, y_train)
y_pred_RF = pipe.predict(x_test)

dot_data = StringIO()
export_graphviz(pipe.named_steps['regressor'].estimators_[0], out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')

importance = list(regressor.feature_importances_)
# List of tuples with variable and importance

# Saving feature names for later use
feature_list = list(data.columns)[1:-1]

feature_importance = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importance)]
# Sort the feature importance by most important first
feature_importance = sorted(feature_importance, key=lambda x: x[1], reverse=True)
# Print out the feature and importance
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importance]

# Set the style
plt.style.use('bmh')
# list of x locations for plotting
x_values = list(range(len(importance)))
# Make a bar chart
plt.bar(x_values, importance, orientation='vertical')
# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation=6)
# Axis labels and title
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
# for train_index, test_index in kf.split(X):
# X_train, X_test = X[train_index], X[test_index]
# y_train, y_test = y[train_index], y[test_index]
# creating an object of LinearRegression class

LR = LinearRegression()
# fitting the training data
LR.fit(x_train, y_train)
y_pred_MLR = LR.predict(x_test)
# predicting the accuracy score
MLR_r2score = r2_score(y_test, y_pred_MLR)
MLR_mse = mean_squared_error(y_test, y_pred_MLR)
print("MLR r2 score is ", MLR_r2score)
print("MLR mse is ", MLR_mse)

# SVM model
clf = SVR(kernel='rbf')
clf.fit(x_train, y_train)
y_pred_SVM = clf.predict(x_test)

SVM_r2score = r2_score(y_test, y_pred_SVM)
SVM_mse = mean_squared_error(y_test, y_pred_SVM)
print("SVM r2 score is ", SVM_r2score)
print("SVM mse is ", SVM_mse)

x = pd.DataFrame(X)
vif = [variance_inflation_factor(x.values, x.columns.get_loc(i)) for i in x.columns]
rDf = x.corr()
print('pairwise correlation matrix：', rDf)
