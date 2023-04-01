from sklearn.base import BaseEstimator, TransformerMixin


class ColumnDropperTransformer(BaseEstimator, TransformerMixin):
    '''drop specified columns'''
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        df = X.copy()
        col = self.columns
        
        return df.drop(col, axis=1)