import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

path1 = "S:\\projects\\13_LLTO_U2_N2_OV0\\data_energy.csv"
csv_energy = pd.read_csv(path1, header=None)
list_energy = sum(csv_energy.values.tolist(), [])

La = [1, 2, 3, 4, 2, 0, 1, 2, 3, 2, 0, 1]
Li = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
N = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]

plot_symbol = ["o", "^", "s"]

fig = plt.figure()
ax = Axes3D(fig)
for index in range(0, len(set(Li))):
    plot_La = [La[i] for i, x in enumerate(Li) if x == index]
    plot_N = [N[i] for i, x in enumerate(Li) if x == index]
    plot_energy = [list_energy[i] for i, x in enumerate(Li) if x == index]
    ax.scatter(plot_La, plot_N, plot_energy, marker=plot_symbol[index], s=75)
ax.legend(['# Li=0', '# Li=1', '# Li=2'])
# ax.xlabel('# La')
# ax.ylabel('Energy (eV)')
# ax.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
