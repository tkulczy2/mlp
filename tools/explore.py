__author__ = 'theodor'

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def summary(df):

    """ Display summary exploratory information

        Parameters
        ----------
        df: pandas DataFrame object

        Returns
        -------
        various numbers/figures???
    """
    print 'SHAPE'
    print '# of Variables: ', df.shape[1], ',\t# of Observations: ', df.shape[0]
    print

    print 'VARIABLE NAMES AND DATA TYPES'
    display(df.dtypes)
    print

    print 'INITIAL OBSERVATIONS'
    display(df.head())
    print

    print 'SUMMARY STATISTICS'
    display(df.describe())
    print

    print 'MISSING VALUES'
    display(df.isnull().sum())
    print

    # print 'POTENTIAL OUTLIERS'


    return

def marginal(s, kind='', name=''):

    """ Explore distributional charactersitics of single variable

        Parameters
        ----------
        s: pandas Series object
        kind: string, kind of variable (continuous, binary, category-unordered, category-ordered)
        name: string, variable name

        Returns
        -------
        various numbers/figures???
    """

    kinds = ['continuous', 'binary', 'category-unordered', 'category-ordered']
    if kind not in kinds:
        dt = s.dtype

    print '===== ' + name + ' ====='
    print
    print 'UNIQUE VALUES'
    print '# of unique values: ', len(s.unique())
    print 'Top 10 values:'
    display(s.value_counts().iloc[:10])
    print

    if kind == 'continuous':
        bins = max(100, len(s.unique()))
        s.hist(bins=bins, color='#cccccc')
        plt.title(name)
        plt.show()
    elif kind == 'binary':
        s.value_counts().plot(kind='bar', rot=0, title=name)
        print 'p = ', sum(s==s.unique()[0])/len(s)
    elif kind == 'category-unordered':
        s.value_counts().plot(kind='bar', rot=0, title=name)
    elif kind == 'category-ordered':
        s.value_counts().sort_index().plot(kind='bar', rot=0, title=name)

    print 'POTENTIAL OUTLIERS'

    print

    return

def joint(s1, s2):

    """ Explore joint distribution of 2 variables

        Parameters
        ----------
        s1: pandas Series object
        s2: pandas Series object

        Returns
        -------
        various numbers/figures???
    """

    return df

def conditional(s1, s2):

    """ Explore conditional distribution of 2 variables

        Parameters
        ----------
        s1: pandas Series object, variable of interest
        s2: pandas Series object, conditioning variable

        Returns
        -------
        various numbers/figures???
    """

    return df

def pca():
    """

    :return:
    """
