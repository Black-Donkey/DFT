import matplotlib.pyplot as plt
import collections
import numpy as np
from pymatgen.core import Structure
from pymatgen.analysis.diffusion.analyzer import DiffusionAnalyzer, get_arrhenius_plot, get_extrapolated_conductivity
from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis
from pymatgen.core.trajectory import Trajectory
from pymatgen.io.vasp.outputs import Xdatcar

# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

vasprun_U1_N0_OV1_2000K = ["S:/projects/56_AIMD/LLTO_U1_N0_OV1_1/run1/vasprun.xml"]
xdatcar_U1_N0_OV1_2000K = "S:/projects/56_AIMD/LLTO_U1_N0_OV1_1/run1/XDATCAR"

# analyzer_2000 = DiffusionAnalyzer.from_files(path_U1_N0_OV1_1500K, specie="Li", smoothed=False)
analyzer_2000 = DiffusionAnalyzer.from_files(vasprun_U1_N0_OV1_2000K, specie="Li", smoothed=False)

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

# structure = analyzer_2000.structure
# trajectories = [s.frac_coords for s in analyzer_2000.get_drift_corrected_structures()]
# pda = ProbabilityDensityAnalysis(structure, trajectories, species=["Li"])
# pda.to_chgcar("CHGCAR.vasp")  # Output to a CHGCAR-like file for visualization in VESTA.

traj = Trajectory.from_file(xdatcar_U1_N0_OV1_2000K)
diff = DiffusionAnalyzer.from_structures(traj, 'Li', 2000, time_step=500, step_skip=1)
pda = ProbabilityDensityAnalysis.from_diffusion_analyzer(diff, interval=0.5, species=(["Li"]))
pda.to_chgcar(filename="pda.vasp")
