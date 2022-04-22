import matplotlib.pyplot as plt
import collections
import numpy as np
from pymatgen.core import Structure
from pymatgen.analysis.diffusion.analyzer import DiffusionAnalyzer, get_arrhenius_plot, get_extrapolated_conductivity
from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis

# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis


path_1300K = ["S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0_1500K/run1/vasprun.xml",
              "S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0_1500K/run2/vasprun.xml"]

analyzer_1500 = DiffusionAnalyzer.from_files(path_1300K, specie="Li", smoothed=False)

msd = analyzer_1500.msd[1:]
time = analyzer_1500.dt[1:]

msdlog = np.log(msd)
timelog = np.log(time)

# create log-log plot with labels
plt.plot(timelog, msdlog)
plt.scatter(timelog, msdlog)
plt.xlabel('Log(time)')
plt.ylabel('Log(MSD)')
plt.show()
