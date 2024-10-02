#!/usr/bin/env python

"""Validates the obfuscation algorithm."""

import argparse

from utils import load_data

# from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, classification_report


def classify(path: str,
             classifier: str = 'knn',
             gridsearch: bool = True
             ) -> KNeighborsClassifier | RandomForestClassifier:
    """
    Loads the data of the given directory and trains a KNN classification algorithm, 
    then tests the accuracy. 

    Args:
        path (str): Folder containing the directories with the CSV files.
        classifier (str): Selected classifier method.
        gridsearch (bool): Should the parameters for the model be optimised via gridsearch 
                           or use default ones.

    Returns:
        Classifier: model trained on the dataset.
    """
    x, y = load_data(path)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42)

    # scaler = StandardScaler()
    # x_train = scaler.fit_transform(x_train)
    # x_test = scaler.transform(x_test)

    model = None
    param_grid = None

    if classifier == 'knn':
        param_grid = {
            'n_neighbors': [1, 2, 5],
            'weights': ['uniform', 'distance'],
            'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
        }
        model = KNeighborsClassifier(
            algorithm='auto', n_neighbors=1, weights='uniform')
    elif classifier == 'rf':
        param_grid = {
            'n_estimators': [200, 250, 300],
            'max_depth': [30, 40, 50]
        }
        model = RandomForestClassifier(n_estimators=250, max_depth=40)

    if gridsearch:
        if param_grid is None:
            raise ValueError("Parameters for GridSearch are not set.")

        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(x_train, y_train)
        best_model = grid_search.best_estimator_
    else:
        best_model = model

    if best_model is None:
        raise ValueError("Model is not set.")

    y_pred = best_model.predict(x_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Best Parameters:", best_model.get_params())
    print("")
    print(classification_report(y_test, y_pred))

    return best_model


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        dest='input',
                        type=str,
                        help='Input file or folder',
                        required=True)

    parser.add_argument('-c', '--classifier',
                        dest='classifier',
                        type=str,
                        default='knn',
                        choices=['knn', 'rf'],
                        help='Input file or folder')

    args = parser.parse_args()

    classify(args.input, args.classifier)
