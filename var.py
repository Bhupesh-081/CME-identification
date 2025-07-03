from cdflib import CDF

file_path = r"C:\Users\l\Desktop\New folder\swis_2025Jun30T155316036\AL1_ASW91_L2_TH1_20250628_UNP_9999_999999_V02.cdf"
cdf = CDF(file_path)

# 🔧 Correct way: get zVariable names using .cdf_info()
info = cdf.cdf_info()

# Print all available zVariables
print("📦 Available zVariables in this file:\n")
for var in info.zVariables:
    print(f"🔹 {var}")
