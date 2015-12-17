__author__ = 'theodor'

import pandas as pd

def generate_dummies(df, columns):

    """ Create dummy variables from categories

        Parameters
        ----------
        df: pandas DataFrame object
        columns: list, names of categorical columns to be dummified

        Returns
        -------
        dummy_df: pandas DataFrame object with binary columns and names corresponding to categories
    """

    dummy_df = pd.DataFrame()
    for col in columns:
        dummy_df = pd.concat([dummy_df, pd.get_dummies(df[col])], axis=1)

    return dummy_df

def generate_categories(s, discrete=True, ordered=True, n=10, name='category'):

    """ Split continuous data into categories

        Parameters
        ----------
        s: pandas Series object of float type
        treat_continuous: boolean, indicates if passed series should be treated as continuous
        n: integer, number of categories
        name: string, prefix for category labels

        Returns
        -------
        s_cat: pandas Series object of categorical type
    """

    if discrete:
        s_cat = pd.Series(pd.Categorical(s, ordered=ordered))
    else:
        s_cat = pd.cut(s, n, include_lowest=True, labels=[name+str(x) for x in range(n)])

    return s_cat