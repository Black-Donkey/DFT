from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.tree import export_graphviz
from six import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import pydotplus
import os

# Run this to add the path to the graphviz package
os.environ['PATH'] = os.environ['PATH'] + ';' + r"C:\Program Files\Graphviz\bin"


def main():
    data = pd.read_csv('energetics.csv')

    # Print the first 5 rows of the dataframe
    print(data.head())

    # Prepare the data for the model
    X = data.iloc[:, 1:-1].values
    y = data.iloc[:, -1].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Create the model
    regressor = RandomForestRegressor()

    pipe = Pipeline([('scaler', StandardScaler()), ('reduce_dim', PCA()), ('regressor', regressor)])
    pipe.fit(X_train, y_train)
    ypipe = pipe.predict(X_test)

    dot_data = StringIO()
    export_graphviz(pipe.named_steps['regressor'].estimators_[0],
                    out_file=dot_data)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('tree.png')

    importance = list(regressor.feature_importances_)
    # List of tuples with variable and importance
    print(importance)

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
    print(x_values)
    # Make a bar chart
    plt.bar(x_values, importance, orientation='vertical')
    # Tick labels for x axis
    plt.xticks(x_values, feature_list, rotation=6)
    # Axis labels and title
    plt.ylabel('Importance')
    plt.xlabel('Variable')
    plt.title('Variable Importance')
    plt.show()


if __name__ == '__main__':
    main()
