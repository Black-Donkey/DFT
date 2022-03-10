import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter, BSPlotterProjected, DosPlotter

path = "S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF3-2-DOS\\"

vaspout = BSVasprun(path + "vasprun.xml")
bandstr = vaspout.get_band_structure(line_mode=True)
plt = BSPlotter(bandstr).get_plot(ylim=[-12, 10])
plt.savefig("band.pdf")
