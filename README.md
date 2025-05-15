# chi-z-cosmology

This repository contains a simplified, observationally tested cosmological model that introduces a **late-time entropic correction term χ(z)** to the Friedmann equation. The correction is smoothly suppressed beyond redshift z > 5 using a tanh function, preserving early-universe physics while addressing both the **Hubble** and **sound horizon tensions**.

## 📄 Paper

- [`Suppressed Entropic Corrections Resolve the Hubble and Sound Horizon Tensions in Late-Time Cosmology`](./Suppressed%20Entropic%20Corrections%20Resolve%20the%20Hubble%20and%20Sound%20Horizon%20Tensions%20in%20Late-Time%20Cosmology.pdf)  
  Final white paper PDF (May 2025). Includes methodology, MCMC results, Fisher/PCA analysis, and future theoretical roadmap.

## 📂 Contents

- `src/chi_z_model.py` – Computes χ(z) for given α, γ, with tanh-suppression at z > 5.
- `src/plot_chi_z.py` – Plots χ(z) and optionally overlays standard ΛCDM.
- `requirements.txt` – Python dependencies (numpy, matplotlib, scipy, etc.)
- `LICENSE` – MIT License

## ▶️ How to Run

Install dependencies and generate the χ(z) plot:

```bash
pip install -r requirements.txt
python src/plot_chi_z.py

