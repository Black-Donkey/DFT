import pandas as pd
import numpy as np
import math

kb = 8.62e-5
T = 773

U2_N0_OV0_path = "S:/projects/10_LLTO_U2_N0_OV0/data_energy.csv"
U2_N1_OV0_path = "S:/projects/11_LLTO_U2_N1_OV0/data_energy.csv"
U2_N2_OV0_path = "S:/projects/13_LLTO_U2_N2_OV0/data_energy.csv"

# LLTO_U2_N1_OV0
U2_N1_OV0_energy = sum(pd.read_csv(U2_N1_OV0_path, header=None).values.tolist(), [])
U2_N1_OV0_count = [2, 38, 12, 18, 4, 4, 20, 2, 6, 2]
Z = 0
for idx in range(0, len(U2_N1_OV0_energy)):
    Z += math.exp(-U2_N1_OV0_energy[idx] / (kb * T))

# np.multiply(U2_N1_OV0_energy, U2_N1_OV0_count)
