from cdflib import CDF, cdfepoch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file_path = r"C:\Users\l\Desktop\New folder\swis_2025Jun30T155316036\AL1_ASW91_L2_TH1_20250628_UNP_9999_999999_V02.cdf"

cdf = CDF(file_path)

raw_time = cdf.varget('epoch_for_cdf_mod')  
time_dt = pd.to_datetime(cdfepoch.to_datetime(raw_time))

flux = cdf.varget('integrated_flux_mod')

flux_clean = np.nan_to_num(flux, nan=0.0)

total_flux = flux_clean.sum(axis=1)  

assert len(time_dt) == len(total_flux), "Time and flux length mismatch!"
print(cdf.cdf_info().rVariables)


plt.figure(figsize=(12, 5))
plt.plot(time_dt, total_flux, label="Total Integrated Ion Flux")
plt.xlabel("Time")
plt.ylabel("Flux (arbitrary units)")
plt.title("Aditya-L1 SWIS: Integrated Ion Flux vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
