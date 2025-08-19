import pymc as pm
import numpy as np

def train_change_point_model(log_returns):
    T = len(log_returns)
    with pm.Model() as model:
        tau = pm.DiscreteUniform('tau', lower=0, upper=T-1)
        mu1 = pm.Normal('mu1', mu=0, sigma=0.02)
        mu2 = pm.Normal('mu2', mu=0, sigma=0.02)
        sigma = pm.Exponential('sigma', 1.0)
        mu = pm.math.switch(tau >= np.arange(T), mu1, mu2)
        y = pm.Normal('y', mu=mu, sigma=sigma, observed=log_returns)
        trace = pm.sample(2000, tune=1000, target_accept=0.95, cores=2)
    return trace
