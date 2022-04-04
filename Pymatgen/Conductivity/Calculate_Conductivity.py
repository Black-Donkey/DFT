import matplotlib.pyplot as plt
# import json
import collections
from pymatgen.core import Structure
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer, \
    get_arrhenius_plot, get_extrapolated_conductivity
# from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis
# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

temperatures = [300, 300]


path_300K = ["S:/projects/09_DFT_MD_test/LLTO_2U_1N_3/vasprun.xml"]


analyzer_300 = DiffusionAnalyzer.from_files(path_300K, specie="Li", smoothed=False)
diffusivities = [analyzer_300.diffusivity, analyzer_300.diffusivity]

plt = analyzer_300.get_msd_plot()
plt.show()
# analyzer_900 = DiffusionAnalyzer.from_files(b, specie="Li", smoothed=False)

# diffusivities = [analyzer_300.diffusivity, analyzer_900.diffusivity]

fig = get_arrhenius_plot(temperatures, diffusivities)
fig.savefig("Li_Arrhenius_Plot.png")
fig.show()
rts = get_extrapolated_conductivity(temperatures, diffusivities,
                                    new_temp=500, structure=analyzer_300.structure,
                                    species="Li")
print("The Li ionic conductivity for LLTO at 500 K is %.4f mS/cm" % rts)
