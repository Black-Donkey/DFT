import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter, \
    BSPlotter, BSPlotterProjected, DosPlotter


def main():
    path = "S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF3-2-DOS\\"

    dos_vasprun = Vasprun(path + "vasprun.xml")
    dos_data = dos_vasprun.complete_dos
    bs_vasprun = Vasprun(path + "vasprun.xml", parse_projected_eigen=True)
    bs_data = bs_vasprun.get_band_structure()

    # Total dos calculated at the end of run.
    tdos = dos_vasprun.tdos
    plotter = DosPlotter(stack=False, sigma=0.5)
    plotter.add_dos("Total DOS", tdos)
    plotter.show()

    v = BSVasprun(path + "vasprun.xml")
    bs = v.get_band_structure(kpoints_filename="band/KPOINTS", line_mode=True)
    plt = BSPlotter(bs)
    plt.get_plot(vbm_cbm_marker=True)
    plt.show()


if __name__ == '__main__':
    main()
