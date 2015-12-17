__author__ = 'theodor'

def impute(df, columns):

    """ Fill in missing data

        Parameters
        ----------
        df: pandas DataFrame object
        columns: list, names or integer locations of columns to fill on

        Returns
        -------
        df: filled DataFrame object
    """

    df.ix[:,columns] = df.ix[:,columns].fillna(df.mean())

    # Add possibility for imputation, clipping/windsorizing, drop missing, normalization, etc.

    return df