import os.path
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd


path1 = os.path.dirname(os.getcwd()) + "\\Machine_Learning\\LLTO_Fingerprint\\energetics.csv"
csv_energy = pd.read_csv(path1, header=None)
# list_energy = sum(csv_energy.values.tolist(), [])
#
# La = [1, 2, 3, 4, 0, 1, 2, 3, 0, 1]
# Li = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2]
# plot_symbol = ["o", "^", "s"]
#
# for index in range(0, len(set(Li))):
#     plot_La = [La[i] for i, x in enumerate(Li) if x == index]
#     plot_energy = [list_energy[i] for i, x in enumerate(Li) if x == index]
#     plt.scatter(plot_La, plot_energy, marker=plot_symbol[index], s=75)
# plt.legend(['# Li=0', '# Li=1', '# Li=2'])
# plt.xlabel('# La')
# plt.ylabel('Energy (eV)')
# plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.show()
