import pandas as pd
import numpy as np

kb = 8.62e-5
T = 773

U2_N0_OV0_path = "S:/projects/10_LLTO_U2_N0_OV0/data_energy.csv"
U2_N1_OV0_path = "S:/projects/11_LLTO_U2_N1_OV0/data_energy.csv"
U2_N2_OV0_path = "S:/projects/13_LLTO_U2_N2_OV0/data_energy.csv"
U2_N3_OV0_path = "S:/projects/15_LLTO_U2_N3_OV0/data_energy.csv"

# LLTO_U2_N1_OV0
U2_N0_OV0_count = [1]
U2_N0_OV0_energy = sum(pd.read_csv(U2_N0_OV0_path, header=None, nrows=len(U2_N0_OV0_count)).values.tolist(), [])
print(U2_N0_OV0_energy[0])

# LLTO_U2_N1_OV0
U2_N1_OV0_count = [2, 38, 12, 18, 4, 4, 20, 2, 6, 2]
U2_N1_OV0_energy = sum(pd.read_csv(U2_N1_OV0_path, header=None, nrows=len(U2_N1_OV0_count)).values.tolist(), [])

U2_N1_OV0_energy_min_idx = U2_N1_OV0_energy.index(min(U2_N1_OV0_energy))
U2_N1_OV0_energy_delta = [i - U2_N1_OV0_energy[U2_N1_OV0_energy_min_idx] for i in U2_N1_OV0_energy]

Z = 0
for idx in range(0, len(U2_N1_OV0_energy_delta)):
    Z += U2_N1_OV0_count[idx] * np.exp(-U2_N1_OV0_energy_delta[idx] / (kb * T))
sum_term = 0
for idx in range(0, len(U2_N1_OV0_energy_delta)):
    sum_term += U2_N1_OV0_energy[idx] * U2_N1_OV0_count[idx] * np.exp(-U2_N1_OV0_energy_delta[idx] / (kb * T))
U2_N1_OV0_average_energy = sum_term / Z
print(U2_N1_OV0_average_energy)

# LLTO_U2_N2_OV0
U2_N2_OV0_count = [2, 34, 12, 17, 4, 4, 4, 16, 2, 4, 6, 2]
U2_N2_OV0_energy = sum(pd.read_csv(U2_N2_OV0_path, header=None, nrows=len(U2_N2_OV0_count)).values.tolist(), [])
del U2_N2_OV0_count[4]
del U2_N2_OV0_energy[4]

U2_N2_OV0_energy_min_idx = U2_N2_OV0_energy.index(min(U2_N2_OV0_energy))
U2_N2_OV0_energy_delta = [i - U2_N2_OV0_energy[U2_N2_OV0_energy_min_idx] for i in U2_N2_OV0_energy]

Z = 0
for idx in range(0, len(U2_N2_OV0_energy_delta)):
    Z += U2_N2_OV0_count[idx] * np.exp(-U2_N2_OV0_energy_delta[idx] / (kb * T))
sum_term = 0
for idx in range(0, len(U2_N2_OV0_energy_delta)):
    sum_term += U2_N2_OV0_energy[idx] * U2_N2_OV0_count[idx] * np.exp(-U2_N2_OV0_energy_delta[idx] / (kb * T))
U2_N2_OV0_average_energy = sum_term / Z
print(U2_N2_OV0_average_energy)

# LLTO_U2_N3_OV0
U2_N3_OV0_count = [2, 32, 13, 16, 3, 1, 2, 4, 16, 5, 2, 3, 4, 1, 2]
U2_N3_OV0_energy = sum(pd.read_csv(U2_N3_OV0_path, header=None, nrows=len(U2_N3_OV0_count)).values.tolist(), [])

U2_N3_OV0_energy_min_idx = U2_N3_OV0_energy.index(min(U2_N3_OV0_energy))
U2_N3_OV0_energy_delta = [i - U2_N3_OV0_energy[U2_N3_OV0_energy_min_idx] for i in U2_N3_OV0_energy]

Z = 0
for idx in range(0, len(U2_N3_OV0_energy_delta)):
    Z += U2_N3_OV0_count[idx] * np.exp(-U2_N3_OV0_energy_delta[idx] / (kb * T))
sum_term = 0
for idx in range(0, len(U2_N3_OV0_energy_delta)):
    sum_term += U2_N3_OV0_energy[idx] * U2_N3_OV0_count[idx] * np.exp(-U2_N3_OV0_energy_delta[idx] / (kb * T))
U2_N3_OV0_average_energy = sum_term / Z
print(U2_N3_OV0_average_energy)
