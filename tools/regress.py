__author__ = 'theodor'

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
import timeit

meth2mod = {'ols':LinearRegression(),
            'knn':KNeighborsRegressor(),
            'random_forest':RandomForestRegressor(),
            'gradient_boost':GradientBoostingRegressor(),
            'adaboost':AdaBoostRegressor()}

def fit_regressor(response, features, df, method='random_forest', params=None):

    """ Fit a regressor to a set of data

        Parameters
        ----------
        response: string, name of response (dependent) variable
        features: list, names of columns to be used as features
        df: pandas DataFrame object
        method: string, classification method (logit, knn, forest, boost)
        k: integer, number of nearest neighbors for knn method

        Returns
        -------
        result: (type???), fitted model
    """

    # Need to update this
    y = df[response]
    X = df.ix[:,features]

    assert(method in meth2mod.keys())

    model = meth2mod[method]

    if params is not None:
        assert(isinstance(params, dict))
        model.set_params(**params)

    if method == 'logit':
        model = LogisticRegression()
    elif method == 'knn':
        model = KNeighborsRegressor(n_neighbors=k)
    elif method == 'forest':
        model = RandomForestRegressor(n_estimators=50)
    elif method == 'boost':
        model = GradientBoostingRegressor()

    start = timeit.default_timer()

    result = model.fit(X, y)

    stop = timeit.default_timer()

    print 'Method: ', method
    print 'Solution time (s): ', stop-start

    return result

