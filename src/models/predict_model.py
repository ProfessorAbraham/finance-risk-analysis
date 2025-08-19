# predict_model.py

import numpy as np

def get_change_point_date(trace, df):
    """Extract most probable change point index and convert to date"""
    tau_post = trace['tau']
    tau_index = int(np.median(tau_post))
    change_date = df.index[tau_index]
    return change_date

def quantify_shift(df, change_date):
    """Compute mean log return before and after change point"""
    before = df.loc[:change_date, 'log_return'].mean()
    after = df.loc[change_date:, 'log_return'].mean()
    shift = after - before
    return before, after, shift
