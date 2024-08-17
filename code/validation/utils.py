import os
import numpy as np
import pandas as pd

SENSORS = {
    "ACG.csv": ('x', 'y', 'z'),
    "GYRO.csv": ('x', 'y', 'z')
}

NR_FEATURES = len([i for sub in SENSORS.values() for i in sub])
NR_MEASUREMENTS = 12000

def readCSVFile(file: str, nrows: int = NR_MEASUREMENTS) -> np.ndarray:  
    """
    Reads predefined columns of CSV files, which we are interested in.
 
    Args:
        file (str): CSV file to be parsed.
        nrows (int): Number of rows to be read from the CSV.
 
    Returns:
        np.ndarray: numpy array of the parsed columns.
    """
    if not file.endswith('.csv'): raise Exception('Not a valid CSV file.')
    if os.path.split(file)[1] not in SENSORS: raise Exception('CSV is not in list.')
    return pd.read_csv(file, delimiter=';', usecols=SENSORS[os.path.split(file)[1]], nrows=nrows).to_numpy()

def combineCSVs(path: str, output: str = None, nrows: int = NR_MEASUREMENTS) -> np.ndarray:
    """
    Combines CSV files contained in a folder.
 
    Args:
        path (str): Folder containing the CSV files.
        output (str): CSV files the data is written to. If it is none, no data will be saved. Defaults to None.
        nrows (int): Number of rows to be read from the CSV.
 
    Returns:
        np.ndarray: numpy array of the combined CSVs without the header.
    """
    features = None
    files = path if path.endswith('.csv') else [file for file in os.listdir(path) if file.endswith('.csv') and file in SENSORS.keys()]
    if not files: raise Exception('No valid CSV file was found at the given location.')
    for filename in files:
        tmp = readCSVFile(path if path.endswith('.csv') else os.path.join(path, filename), nrows=nrows)
        features = np.hstack((features, tmp)) if features is not None else tmp
        if path.endswith('.csv'): break
    if output is not None:
        np.savetxt(output, features, delimiter=',', fmt='%s')
    return features

def loadData(path: str, nr_measurements: int = NR_MEASUREMENTS) -> tuple[np.ndarray, np.ndarray]:
    """
    Parses CSV files contained in any subfolder of the given directory.
 
    Args:
        path (str): Folder containing the directories with the CSV files.
        nr_measurements (int): Number of measuremnts to include int the dataset for each CSV.
 
    Returns:
        tuple[np.ndarray, np.ndarray]: tuple of features, parsed and combined data from the CSVs and the targets.
    """
    features = None
    targets = np.zeros(shape=(1, 0))
    files = path if path.endswith('.csv') else [file for file in os.listdir(path) if os.path.isdir(os.path.join(path, file))]
    if not files: raise Exception('No valid folders were found at the given location.')
    for target, filename in enumerate(files):
        tmp = combineCSVs(path if path.endswith('.csv') else os.path.join(path, filename), nrows=nr_measurements)
        if tmp.shape[1] != NR_FEATURES : tmp = np.resize(tmp, (tmp.shape[0], NR_FEATURES))
        features = np.vstack((features, tmp)) if features is not None else tmp
        targets = np.concatenate((targets, np.full((tmp.shape[0], 1), filename)), axis=None)
        if path.endswith('.csv'): break

    return features, targets