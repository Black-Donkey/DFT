import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter, \
    BSPlotter, BSPlotterProjected, DosPlotter


def main():
    path = "S:\\projects\\04_LLTO_2N_Ov_ISIF_3\\LLTO-2N-5-OV-ISIF0-1\\STEP2\\"

    dos_vasprun = Vasprun(path + "vasprun.xml")
    dos_data = dos_vasprun.complete_dos
    # bs_vasprun = Vasprun(path + "vasprun.xml", parse_projected_eigen=True)
    # bs_data = bs_vasprun.get_band_structure()

    # Total dos calculated at the end of run.
    tdos = dos_vasprun.tdos
    plot1 = DosPlotter(stack=False, sigma=0.5)
    plot1.add_dos("Total DOS", tdos)
    plot1.show()

    # run = BSVasprun(path + "vasprun.xml", parse_projected_eigen=True)
    # bs = run.get_band_structure("KPOINTS")
    # print("number of bands", bs.nb_bands)
    # print("number of kpoints", len(bs.kpoints))
    # print(bs.is_metal())
    # print(bs.is_spin_polarized)
    # bsplot = BSPlotter(bs)
    # # get the plot
    # bsplot.get_plot(ylim=(-20, 10), zero_to_efermi=True)
    # print(bs.efermi)
    #
    # # add some features
    # ax = plt.gca()
    # ax.set_title("N-LLTO Band Structure", fontsize=20)
    # xlim = ax.get_xlim()
    # ax.hlines(0, xlim[0], xlim[1], linestyles="dashed", color="black")
    #
    # # add legend
    # ax.plot((), (), "b-", label="spin up")
    # ax.plot((), (), "r--", label="spin down")
    # ax.legend(fontsize=16, loc="upper left")

    # ValueError: BSPlotter only works with BandStructureSymmLine objects. A BandStructure object (on a uniform grid
    # for instance and not along symmetry lines won't work)

    # v = BSVasprun(path + "vasprun.xml")
    # bs = v.get_band_structure(kpoints_filename="band/KPOINTS", line_mode=True)
    # plot2 = BSPlotter(bs)
    # plot2.get_plot(vbm_cbm_marker=True)
    # plot2.show()


if __name__ == '__main__':
    main()
