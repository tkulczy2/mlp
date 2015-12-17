__author__ = 'theodor'

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
import timeit

meth2mod = {'logit':LogisticRegression(),
            'knn':KNeighborsClassifier(),
            'tree':DecisionTreeClassifier(),
            'random_forest':RandomForestClassifier(),
            'gradient_boost':GradientBoostingClassifier(),
            'adaboost':AdaBoostClassifier(),
            'svm':LinearSVC(),
            'naive_bayes':GaussianNB()}

def get_classifier(method='random_forest', params=None):

    """ Return an estimator object without fitting it do data

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
    assert(method in meth2mod.keys())

    model = meth2mod[method]

    if params is not None:
        assert(isinstance(params, dict))
        model.set_params(**params)

    return model

def fit_classifier(y, X, method='random_forest', params=None):

    """ Fit a classifier to a set of data

        Parameters
        ----------
        y: Series, values of response (dependent) variable
        X: DataFrame, feature data
        method: string, classification method (logit, knn, svm, random_forest, gradient_boost, adaboost)
        k: integer, number of nearest neighbors for knn method

        Returns
        -------
        result: (type???), fitted model
    """
    assert(method in meth2mod.keys())
    assert(all([yi in [0,1] for yi in y]))

    model = meth2mod[method]

    if params is not None:
        assert(isinstance(params, dict))
        model.set_params(**params)

    start = timeit.default_timer()
    result = model.fit(X, y)
    stop = timeit.default_timer()

    #print 'Method: ', method
    #print 'Solution time (s): ', stop-start

    return result, stop-start

def classify(response, features, df, method='random_forest', params=None):

    """ Fit a classifier to training data

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
    assert(method in meth2mod.keys())

    y = df[response]
    X = df.ix[:,features]

    assert(all([yi in [0,1] for yi in y]))

    model = meth2mod[method]

    if params is not None:
        assert(isinstance(params, dict))
        model.set_params(**params)

    start = timeit.default_timer()
    result = model.fit(X, y)
    stop = timeit.default_timer()

    print 'Method: ', method
    print 'Solution time (s): ', stop-start

    return result

