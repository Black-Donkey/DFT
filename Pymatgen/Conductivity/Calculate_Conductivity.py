import matplotlib.pyplot as plt
# import json
import collections
from pymatgen.core import Structure
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer, \
    get_arrhenius_plot, get_extrapolated_conductivity
from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis
from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

temperatures = [500, 1000, 1500]


a = ["S:/projects/09_DFT_MD_test/LLTO_2U_1N_3/vasprun.xml"]
b = ["S:/projects/09_DFT_MD_test/LLTO_2U_1N_3/vasprun.xml"]
c = ["S:/projects/09_DFT_MD_test/LLTO_2U_1N_3/vasprun.xml"]

analyzer_500 = DiffusionAnalyzer.from_files(a, specie="Li", smoothed=False)
analyzer_1000 = DiffusionAnalyzer.from_files(b, specie="Li", smoothed=False)
analyzer_1500 = DiffusionAnalyzer.from_files(c, specie="Li", smoothed=False)

diffusivities = [analyzer_500.diffusivity, analyzer_1000.diffusivity, analyzer_1500.diffusivity]

plt = get_arrhenius_plot(temperatures, diffusivities)
plt.savefig("Li_Arrhenius_Plot.png")
rts = get_extrapolated_conductivity(temperatures, diffusivities,
                                    new_temp=300, structure=analyzer_500.structure,
                                    species="Li")
print("The Li ionic conductivity for anti-spinel Li3OBr at 300 K is %.4f mS/cm" % rts)
