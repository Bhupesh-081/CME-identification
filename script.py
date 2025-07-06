from cdflib import CDF, cdfepoch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# === Load the CDF file ===
file_path = r"C:\Users\l\Desktop\CME-idetification\swis_2025Jun30T155316036\AL1_ASW91_L2_TH2_20250628_UNP_9999_999999_V02.cdf"
cdf = CDF(file_path)

# === Load and clean time ===
raw_time = cdf.varget('epoch_for_cdf_mod')
time_dt = pd.to_datetime(cdfepoch.to_datetime(raw_time), errors='coerce')
valid_time_mask = ~time_dt.isna()
time_dt = time_dt[valid_time_mask]

# === Load and clean energy ===
energy_raw = np.array(cdf.varget('energy_center_mod'))
energy_raw = np.nan_to_num(energy_raw, nan=0.0, posinf=0.0, neginf=0.0)
energy = np.nanmean(energy_raw[valid_time_mask], axis=0)  # average over time

# === Load and clean flux ===
flux = np.array(cdf.varget('integrated_flux_mod'))
flux = flux[valid_time_mask]
flux = np.nan_to_num(flux, nan=0.0, posinf=0.0, neginf=0.0)

# === Convert to log scale and transpose ===
log_flux = np.log10(flux + 1e-2)
log_flux_T = log_flux.T  # shape: (50, 17275)

# === Final shape check ===
print("✅ time_dt.shape:", time_dt.shape)
print("✅ energy.shape:", energy.shape)
print("✅ log_flux_T.shape:", log_flux_T.shape)

# === Plot ===
plt.figure(figsize=(14, 6))
pc = plt.pcolormesh(time_dt, energy, log_flux_T, shading='auto', cmap='plasma')
plt.colorbar(pc, label='log₁₀(Flux)')

plt.title("Aditya-L1 SWIS: Energy vs Time Spectrogram")
plt.xlabel("Time (UTC)")
plt.ylabel("Energy (keV)")
plt.gca().xaxis.set_major_formatter(DateFormatter("%m-%d %H:%M"))
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
