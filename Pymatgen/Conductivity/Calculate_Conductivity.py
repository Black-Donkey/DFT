import matplotlib.pyplot as plt
import collections
import numpy as np
from pymatgen.core import Structure
from pymatgen.analysis.diffusion.analyzer import DiffusionAnalyzer, get_arrhenius_plot, get_extrapolated_conductivity
from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis

# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

temperatures = [300, 1500]

path_300K = ["S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0_300K/vasprun.xml"]
path_1300K = ["S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0_1500K/run1/vasprun.xml",
              "S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0_1500K/run2/vasprun.xml"]

analyzer_300 = DiffusionAnalyzer.from_files(path_300K, specie="Li", smoothed=False)
analyzer_1500 = DiffusionAnalyzer.from_files(path_1300K, specie="Li", smoothed=False)

msd_300 = analyzer_300.get_msd_plot()
msd_300.show()
msd_1500 = analyzer_1500.get_msd_plot()
msd_1500.show()

diffusivities = [analyzer_300.diffusivity, analyzer_1500.diffusivity]
fig = get_arrhenius_plot(temperatures, diffusivities)
fig.savefig("Li_Arrhenius_Plot.png")
fig.show()
rts = get_extrapolated_conductivity(temperatures, diffusivities,
                                    new_temp=300, structure=analyzer_300.structure, species="Li")
print("The Li ionic conductivity for LLTO at 500 K is %.4f mS/cm" % rts)

structure = analyzer_1500.structure
trajectories = [s.frac_coords for s in analyzer_1500.get_drift_corrected_structures()]
pda = ProbabilityDensityAnalysis(structure, trajectories, species=["Li"])
pda.to_chgcar("CHGCAR.vasp")
