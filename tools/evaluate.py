__author__ = 'theodor'

from sklearn import metrics
from sklearn.cross_validation import train_test_split, cross_val_score

def evaluate(y_true, y_pred):

    """ Calculate prediction accuracy for a single model

        Parameters
        ----------
        y_true: Series, true values of response variable
        y_pred: Series, predicted values

        Returns
        -------
        scores: dict, mapping of score names and values
    """

    # accuracy, precision, recall, f1, AUC, P-R curve

    scores = dict()

    scores['accuracy'] = metrics.accuracy_score(y_true, y_pred)
    scores['precision'] = metrics.precision_score(y_true, y_pred)
    scores['recall'] = metrics.recall_score(y_true, y_pred)
    scores['f1'] = metrics.f1_score(y_true, y_pred)
    scores['auc'] = metrics.roc_auc_score(y_true, y_pred)

    return scores

def cross_validate(model, y, X, params=None, scores=['accuracy', 'precision', 'recall', 'f1', 'roc_auc'], k=3):

    """ Generate a set of cross-validated evaluation metrics

        Parameters
        ----------
        model: sklearn estimator object
        y: target (response) values
        X: features
        params: dict, set of parameters to pass to the estimator
        scores: list, collection of scores to return
        k: int, number of folds to use in cross validation

        Returns
        -------
        scores: dict, mapping of score names and values
    """

    # accuracy, precision, recall, f1, AUC, P-R curve


    results = dict()
    for score in scores:
        results[score] = cross_val_score(model, X, y, scoring=score, fit_params=params)

    return scores

def plot_precision_recall(y_true, probs, ax=None, label=''):

    """ Plot the precision-recall curve

        Parameters
        ----------
        y_true:
        probs:
        ax:
        label:

        Returns
        -------
        ax: matplotlib axes
    """

    # accuracy, precision, recall, f1, AUC, P-R curve

    pre, rec, thr = metrics.precision_recall_curve(y_true, probs)

    if ax is None:
        ax = plt.subplot(111)

    ax.plot(rec, pre, label=label, lw=2.)
    ax.plot([0,1],[1,0],'k--')
    ax.set_xlim(-0.05,1.05)
    ax.set_ylim(-0.05,1.05)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_ylabel('Precision')
    ax.set_xlabel('Recall')

    return ax