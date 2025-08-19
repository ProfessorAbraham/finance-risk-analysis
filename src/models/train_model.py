# train_model.py

import pymc as pm
import numpy as np

def train_change_point_model(log_returns):
    """Train Bayesian Change Point Model"""
    n = len(log_returns)
    with pm.Model() as model:
        tau = pm.DiscreteUniform('tau', lower=0, upper=n-1)
        mu1 = pm.Normal('mu1', mu=0, sigma=0.05)
        mu2 = pm.Normal('mu2', mu=0, sigma=0.05)
        sigma = pm.HalfNormal('sigma', sigma=0.05)
        mu = pm.math.switch(tau >= np.arange(n), mu1, mu2)
        obs = pm.Normal('obs', mu=mu, sigma=sigma, observed=log_returns)
        trace = pm.sample(1000, tune=1000, cores=2, return_inferencedata=False)
    return trace
