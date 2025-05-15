import numpy as np

def chi_z(z, alpha=0.001, gamma=1.0):
    """Compute the entropic correction χ(z) for z ≤ 5"""
    z = np.asarray(z)
    chi = np.where(z <= 5, alpha * (1 + z)**(-gamma), 0.0)
    return chi
