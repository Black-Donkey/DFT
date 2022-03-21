import matplotlib.pyplot as plt
# import json
import collections
from pymatgen.core import Structure
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer, \
    get_arrhenius_plot, get_extrapolated_conductivity
# from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis
# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

temperatures = [300, 900]


a = ["S:/projects/09_DFT_MD_test/LLTO_2U_1N_3/vasprun.xml"]
b = ["S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0/vasprun.xml"]

analyzer_300 = DiffusionAnalyzer.from_files(a, specie="Li", smoothed=False)
diffusivities = [analyzer_300.diffusivity, analyzer_300.diffusivity]

# analyzer_900 = DiffusionAnalyzer.from_files(b, specie="Li", smoothed=False)

# diffusivities = [analyzer_300.diffusivity, analyzer_900.diffusivity]

fig = get_arrhenius_plot(temperatures, diffusivities)
fig.savefig("Li_Arrhenius_Plot.png")
fig.show()
rts = get_extrapolated_conductivity(temperatures, diffusivities,
                                    new_temp=1200, structure=analyzer_300.structure,
                                    species="Li")
print("The Li ionic conductivity for anti-spinel LLTO at 300 K is %.4f mS/cm" % rts)
