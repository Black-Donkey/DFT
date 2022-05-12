import os.path
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd


path1 = os.path.dirname(os.getcwd()) + '\\Machine_Learning\\energetics.csv'
csv_energy = pd.read_csv(path1)
list_energy = csv_energy['E'].values.tolist()
N = csv_energy['N'].values.tolist()
OV = csv_energy['OV'].values.tolist()
plot_symbol = ["o", "^"]

plt.style.use('seaborn-darkgrid')
for index in range(0, len(set(OV))):
    plot_N = [N[i] for i, x in enumerate(OV) if x == index]
    plot_energy = [list_energy[i] for i, x in enumerate(OV) if x == index]
    plt.plot(plot_N, plot_energy, plot_symbol[index], markersize=10, markerfacecolor='none')
plt.legend(['# OV = 0', '# OV = 1'])
plt.xlabel('# N dopant')
plt.ylabel('Energy (eV)')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig("energy_plot.svg", dpi=600, format="svg")
plt.show()
