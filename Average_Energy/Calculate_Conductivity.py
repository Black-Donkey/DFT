import matplotlib.pyplot as plt

import collections
from pymatgen.core import Structure
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer, \
    get_arrhenius_plot, get_extrapolated_conductivity
# from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis
# from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

temperatures = [300, 300]


U2_N0_OV0_path = ["S:/projects/09_DFT_MD_test/LLTO_2U_1N_3/vasprun.xml"]
b = ["S:/projects/25_LLTO_U2_MD/LLTO_U2_N0_OV0/vasprun.xml"]

