import matplotlib.pyplot as plt
import collections
import numpy as np
from pymatgen.core import Structure
from pymatgen.analysis.diffusion.analyzer import DiffusionAnalyzer, get_arrhenius_plot, get_extrapolated_conductivity
from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis

# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

path_U1_N0_OV1_1500K = ["S:/projects/25_LLTO_U2_MD/LLTO_U1_N0_OV1_1500K/run1/vasprun.xml"]
path_U1_N0_OV1_2000K = ["S:/projects/56_AIMD/LLTO_U1_N0_OV1_1/run1/vasprun.xml"]

analyzer_2000 = DiffusionAnalyzer.from_files(path_U1_N0_OV1_1500K, specie="Li", smoothed=False)

msd = analyzer_2000.msd[1:]
time = analyzer_2000.dt[1:]

msdlog = np.log(msd)
timelog = np.log(time)

# create plot with labels
plt.plot(time, msd)
plt.scatter(time, msd)
plt.xlabel('time')
plt.ylabel('MSD')
plt.show()

# create log-log plot with labels
plt.plot(timelog, msdlog)
plt.scatter(timelog, msdlog)
plt.xlabel('Log(time)')
plt.ylabel('Log(MSD)')
plt.show()

structure = analyzer_2000.structure
trajectories = [s.frac_coords for s in analyzer_2000.get_drift_corrected_structures()]
pda = ProbabilityDensityAnalysis(structure, trajectories, species=["Li"])
pda.to_chgcar("CHGCAR.vasp")  # Output to a CHGCAR-like file for visualization in VESTA.
