import argparse
from utils import loadData

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def classify(path: str) -> None:
    """
    Loads the data of the given directory and trains a KNN classification algorithm, then tests the accuracy. 
 
    Args:
        path (str): Folder containing the directories with the CSV files.
 
    Returns:
        None
    """
    X, y = loadData(path)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

if __name__ == "__main__":   
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        dest='input',
                        type=str,
                        help='Input file or folder',
                        required=True)

    args = parser.parse_args()

    classify(args.input)