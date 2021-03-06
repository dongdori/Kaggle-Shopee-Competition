import numpy as np
import pandas as pd

def f1_score(y_true, y_pred):
    '''
    y_true : pd.Series
    y_pred : pd.Series
    '''
    y_true = y_true.apply(lambda x: set(x))
    y_pred = y_pred.apply(lambda x: set(x.split(' ')))
    intersection = np.array([len(x[0] & x[1]) for x in zip(y_true, y_pred)])
    len_y_pred = y_pred.apply(lambda x: len(x)).values
    len_y_true = y_true.apply(lambda x: len(x)).values
    f1 = 2 * intersection / (len_y_pred + len_y_true)
    return f1