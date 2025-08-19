import pymc as pm
import numpy as np

def train_change_point_model(log_returns):
    n = len(log_returns)
    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=n-1)
        mu1 = pm.Normal("mu1", mu=0, sigma=0.02)
        mu2 = pm.Normal("mu2", mu=0, sigma=0.02)
        sigma = pm.Exponential("sigma", 50)
        mu = pm.math.switch(np.arange(n) < tau, mu1, mu2)
        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=log_returns)
        trace = pm.sample(2000, tune=1000, cores=2, target_accept=0.95)
    return trace