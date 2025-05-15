# chi-z-cosmology

This repository presents a simplified cosmological model introducing a **late-time entropic correction term χ(z)** to the Friedmann equation. This correction is smoothly confined to redshifts **z ≤ 5**, enabling the model to address both the **Hubble tension** and **sound horizon tension** while preserving early-universe physics (e.g., BBN, recombination).

---

## 📝 White Paper

📄 **Suppressed Entropic Corrections Resolve the Hubble and Sound Horizon Tensions in Late-Time Cosmology**  
[Download PDF](./Suppressed%20Entropic%20Corrections%20Resolve%20the%20Hubble%20and%20Sound%20Horizon%20Tensions%20in%20Late-Time%20Cosmology.pdf)

This paper includes:
- Modified Friedmann framework with χ(z)
- MCMC fitting to Pantheon+ SNe data
- Fisher matrix and PCA analysis
- Plans for theoretical derivation and multi-probe testing

---

## 📂 Contents

- `src/chi_z_model.py`: Computes the χ(z) correction function for given α and γ
- `src/plot_chi_z.py`: Plots χ(z) and comparison baselines
- `requirements.txt`: Dependencies for running the model and plot
- `Suppressed Entropic Corrections...pdf`: Final peer-reviewed white paper

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/plot_chi_z.py
