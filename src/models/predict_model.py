import numpy as np

def get_change_point_date(trace, df):
    tau_posterior = trace.posterior['tau'].values.flatten()
    tau_index = int(np.median(tau_posterior))
    return df.index[tau_index]

def quantify_shift(df, change_date):
    before_mean = df['log_return'][df.index < change_date].mean()
    after_mean = df['log_return'][df.index >= change_date].mean()
    shift = after_mean - before_mean
    return before_mean, after_mean, shift