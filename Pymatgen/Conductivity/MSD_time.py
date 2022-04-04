import matplotlib.pyplot as plt
import json
import collections
from pymatgen.core import Structure
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer, \
    get_arrhenius_plot, get_extrapolated_conductivity
from pymatgen.analysis.diffusion.aimd.pathway import ProbabilityDensityAnalysis
from pymatgen.analysis.diffusion.aimd.van_hove import VanHoveAnalysis

temperatures = [600, 800, 1000, 1200]
analyzers = collections.OrderedDict()
for temp in temperatures:
    with open("aimd_data/%d.json" % temp) as f:
        d = json.load(f)
        analyzers[temp] = DiffusionAnalyzer.from_dict(d)
