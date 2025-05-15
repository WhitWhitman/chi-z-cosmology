import numpy as np
import matplotlib.pyplot as plt
from chi_z_model import chi_z

z_vals = np.linspace(0, 10, 500)
chi_vals = chi_z(z_vals)

plt.figure(figsize=(8, 5))
plt.plot(z_vals, chi_vals, label=r"$\chi(z) = \alpha (1+z)^{-\gamma}$")
plt.axvline(5, color='red', linestyle='--', label="Suppression at z = 5")
plt.xlabel("Redshift z")
plt.ylabel(r"$\chi(z)$")
plt.title("Entropic Correction Term χ(z)")
plt.legend()
plt.grid(True)
plt.savefig("figures/chi_z_plot.png")
