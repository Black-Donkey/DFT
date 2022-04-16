from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
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
regressor = RandomForestRegressor(random_state=0)

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2,
                               random_state=42, n_jobs=-1)
# Fit the random search model
rf_random.fit(x_train, y_train)

# pipe = Pipeline([('scaler', StandardScaler()), ('reduce_dim', PCA()), ('regressor', regressor)])
# pipe.fit(x_train, y_train)
# y_pred_RF = pipe.predict(x_test)
#
# dot_data = StringIO()
# export_graphviz(pipe.named_steps['regressor'].estimators_[0], out_file=dot_data)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_png('tree.png')
#
# importance = list(regressor.feature_importances_)
# # List of tuples with variable and importance
#
# # Saving feature names for later use
# feature_list = list(data.columns)[1:-1]
#
# feature_importance = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importance)]
# # Sort the feature importance by most important first
# feature_importance = sorted(feature_importance, key=lambda x: x[1], reverse=True)
# # Print out the feature and importance
# [print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importance]
#
# # Set the style
# plt.style.use('bmh')
# # list of x locations for plotting
# x_values = list(range(len(importance)))
# # Make a bar chart
# plt.bar(x_values, importance, orientation='vertical')
# # Tick labels for x axis
# plt.xticks(x_values, feature_list, rotation=6)
# # Axis labels and title
# plt.ylabel('Importance')
# plt.xlabel('Variable')
# plt.title('Variable Importance')
# plt.show()
