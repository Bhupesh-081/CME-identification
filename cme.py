from cdflib import CDF
import cdflib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Load your CDF file
file_path = r"C:\Users\l\Desktop\New folder\swis_2025Jun30T155316036\AL1_ASW91_L2_TH1_20250628_UNP_9999_999999_V02.cdf"
cdf = CDF(file_path)

# Load time
epoch = cdf.varget("epoch_for_cdf_mod")
time_dt = cdflib.cdfepoch.to_datetime(epoch)

# Load flux values
flux_total = np.nanmean(cdf.varget("integrated_flux_mod"), axis=1)
flux_s9    = np.nanmean(cdf.varget("integrated_flux_s9_mod"), axis=1)
flux_s10   = np.nanmean(cdf.varget("integrated_flux_s10_mod"), axis=1)
flux_s11   = np.nanmean(cdf.varget("integrated_flux_s11_mod"), axis=1)

# Plot
plt.figure(figsize=(15, 6))
plt.plot(time_dt, flux_total, label='Total Flux', color='black', linewidth=2)
plt.plot(time_dt, flux_s9, label='Flux S9', alpha=0.7)
plt.plot(time_dt, flux_s10, label='Flux S10', alpha=0.7)
plt.plot(time_dt, flux_s11, label='Flux S11', alpha=0.7)

plt.title("Aditya-L1 SWIS Ion Flux (Total and Sectors)")
plt.xlabel("Time (UTC)")
plt.ylabel("Ion Flux (Arbitrary Units)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
