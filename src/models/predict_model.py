import numpy as np

def get_change_point_date(trace, df):
    tau_samples = trace.posterior['tau'].values.flatten()
    change_point_idx = int(np.median(tau_samples))
    return df.index[change_point_idx]

def quantify_shift(df, change_point_date):
    idx = df.index.get_loc(change_point_date)
    before = df['log_return'].iloc[:idx].mean()
    after = df['log_return'].iloc[idx:].mean()
    shift = after - before
    return before, after, shift
