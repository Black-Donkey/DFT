import matplotlib.pyplot as plt
# import json
import collections
from pymatgen.core import Structure
from pymatgen.analysis.diffusion.analyzer import DiffusionAnalyzer, get_arrhenius_plot, get_extrapolated_conductivity
from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis

# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

temperatures = [300, 1300]

path_300K = ["S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0_300K/vasprun.xml"]
path_1300K = ["S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0_1300K/vasprun.xml"]

analyzer_300 = DiffusionAnalyzer.from_files(path_300K, specie="Li", smoothed=False)
analyzer_1300 = DiffusionAnalyzer.from_files(path_1300K, specie="Li", smoothed=False)

msd_300 = analyzer_300.get_msd_plot()
msd_300.show()
msd_1300 = analyzer_1300.get_msd_plot()
msd_1300.show()

diffusivities = [analyzer_300.diffusivity, analyzer_1300.diffusivity]
fig = get_arrhenius_plot(temperatures, diffusivities)
fig.savefig("Li_Arrhenius_Plot.png")
fig.show()
rts = get_extrapolated_conductivity(temperatures, diffusivities,
                                    new_temp=300, structure=analyzer_300.structure, species="Li")
print("The Li ionic conductivity for LLTO at 500 K is %.4f mS/cm" % rts)

structure = analyzer_1300.structure
trajectories = [s.frac_coords for s in analyzer_1300.get_drift_corrected_structures()]
pda = ProbabilityDensityAnalysis(structure, trajectories, species="Li")
pda.to_chgcar("CHGCAR.vasp")
