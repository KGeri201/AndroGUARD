#!/usr/bin/env python

"""Module providing a function printing python version."""

import os
import numpy as np
import pandas as pd

FREQUENCY = '250ms'

SENSORS = {
    "ACG.csv": ('x', 'y', 'z'),
    "GYRO.csv": ('x', 'y', 'z')
}

NR_FEATURES = 6
TIME_COL = 't_unix'


def read_csv_file(file: str, delimiter: str = ';') -> pd.DataFrame:
    """
    Reads predefined columns of CSV files, which we are interested in.

    Args:
        file (str): CSV file to be parsed.

    Returns:
        pd.DataFrame: Parsed columns.
    """
    if not file.endswith('.csv'):
        raise FileNotFoundError('Not a valid CSV file.')
    if os.path.split(file)[1] not in SENSORS:
        raise FileNotFoundError('CSV is not in list.')

    return pd.read_csv(
        file, delimiter=delimiter, usecols=(TIME_COL,) + SENSORS[os.path.split(file)[1]])


def combine_features(path: str, output: str = None) -> np.ndarray:
    """
    Combines CSV files contained in a folder.

    Args:
        path (str): Folder containing the CSV files.
        output (str): CSV files the data is written to. If it is none, 
                      no data will be saved. Defaults to None.

    Returns:
        np.ndarray: numpy array of the combined CSVs without the header.
    """

    if not os.path.exists(path):
        return None

    features = None
    files = [path] if path.endswith('.csv') else [file for file in os.listdir(
        path) if file.endswith('.csv') and file in SENSORS]
    if not files:
        raise FileNotFoundError(
            'No valid CSV file was found at the given location.')
    for filename in files:
        tmp = read_csv_file(path if path.endswith('.csv')
                            else os.path.join(path, filename))
        tmp[TIME_COL] = pd.to_datetime(tmp[TIME_COL], unit='ms')

        features = pd.merge_asof(
            features, tmp, on=TIME_COL, direction='forward') if features is not None else tmp

    # features = features.groupby(pd.Grouper(
    #     key=TIME_COL, freq=FREQUENCY)).mean()
    features = features.drop(TIME_COL, axis=1)
    features = features.dropna()
    if output is not None:
        features.to_csv(output)
    return features.to_numpy()


def load_data(path: str, target: str = None) -> tuple[np.ndarray, np.ndarray]:
    """
    Parses CSV files contained in any subfolder of the given directory.

    Args:
        path (str): Folder containing the directories with the CSV files.
        nr_measurements (int): Number of measuremnts to include int the dataset for each CSV.

    Returns:
        tuple[np.ndarray,np.ndarray]: tuple of features, 
                                       parsed and combined data from the CSVs and the targets.
    """
    features = None
    targets = np.zeros(shape=(1, 0))
    files = path if path.endswith('.csv') else [file for file in os.listdir(
        path) if os.path.isdir(os.path.join(path, file))]
    if not files:
        raise NotADirectoryError(
            'No valid folders were found at the given location.')
    for filename in files:
        tmp = combine_features(path if path.endswith('.csv') else os.path.join(
            path, filename, target))
        if tmp is None:
            continue
        if tmp.shape[1] != NR_FEATURES:
            tmp = np.resize(tmp, (tmp.shape[0], NR_FEATURES))
        features = np.vstack((features, tmp)) if features is not None else tmp
        targets = np.concatenate(
            (targets, np.full((tmp.shape[0], 1), filename)), axis=None)
        if path.endswith('.csv'):
            break

    return features, targets
