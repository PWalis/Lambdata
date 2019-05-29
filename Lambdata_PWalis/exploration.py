#!/user/bin/env python
from sklearn.model_selection import train_test_split
import pandas as pd


def values(x):
    # Given a dataframe this function will print out all of the columns values counts
    for column in x.columns:
        print(x[column].value_counts())

def cardinality_finder(df, threshold, dtype):
    # Given a DataFrame and an int this function will print the features below the threshold and display 
    # the cardinality along with the dtype, give a list of dtypes to check if more than one is desired.
    # dtype should be a string
    cf = df.select_dtypes(include=dtype)
    for column in cf.columns:
        data_type = cf[column].dtype
        unique = cf[column].unique()
        length = len(unique)
        if (length < threshold):
            print(column, length, data_type)
