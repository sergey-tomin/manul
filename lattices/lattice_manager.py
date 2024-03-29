import importlib
import logging
import numpy as np
from copy import deepcopy, copy
from ocelot import *
from ocelot.cpbd.magnetic_lattice import *
#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class LatSection:
    def __init__(self, name, str_cells, start=None, stop=None, z0=23.2, tw=None, load_all=True):
        self.name = name
        self.str_cells = str_cells
        self.start = start
        self.stop = stop
        self.z0 = z0
        self.tw = tw
        self.load_all = load_all


class Lattice:
    def __init__(self, path="lattices.phase_advance_5pi_sase2"):
        self.lat_zi = 23.2 # start position of the lattice in [m]
        self.default_section = "T4D"
        self.config = {"I1":       path + ".i1",
                       "L1":       path + ".l1",
                       "L2":       path + ".l2",
                       "L3":       path + ".l3",
                       "CL":       path + ".cl",
                       "TL34":     path + ".tl34",
                       "TL34_SA2": path + ".sase2_branch.tl34_sa2",
                       "SASE1":    path + ".sase1",
                       "SASE2":    path + ".sase2_branch.sase2",
                       "T1":       path + ".sase2_branch.t1",
                       "T3":       path + ".sase2_branch.t3",
                       "T5":       path + ".sase2_branch.t5",
                       "T5D":      path + ".sase2_branch.t5d",

                       "T4":    path + ".t4",
                       "SASE3": path + ".sase3",
                       "I1D":   path + ".i1d",
                       "B1D":   path + ".b1d",
                       "B2D":   path + ".b2d",
                       "TLD":   path + ".tld",
                       "T4D":   path + ".t4d"
                       }

        self.lats = {}
        self.load()
        self.sections = {}
        self.def_sections()

    def def_sections(self):
        tws_L3 = Twiss()
        tws_L3.beta_x = 20.6928140374
        tws_L3.beta_y = 6.8214735433
        tws_L3.alpha_x = 0.0332419824342
        tws_L3.alpha_y = -0.869862984066
        tws_L3.E = 2.39999998888

        tws_sase3 = Twiss()
        tws_sase3.beta_x = 13.6455956218
        tws_sase3.beta_y = 3.93176166974
        tws_sase3.alpha_x = 2.20226650304
        tws_sase3.alpha_y = -0.830611804908
        tws_sase3.E = 17.4999999889

        tws_cl = Twiss()
        tws_cl.beta_x = 20.8408455944
        tws_cl.beta_y = 45.1306436718
        tws_cl.alpha_x = -0.712872984902
        tws_cl.alpha_y = 1.41986586551
        tws_cl.E = 15.2349999889

        tws_400 = Twiss()
        tws_400.beta_x = 35.652369033650984
        tws_400.beta_y = 95.68178906106743
        tws_400.alpha_x = 1.3729804871141813
        tws_400.alpha_y = 4.304664424379663
        tws_400.E = 2.4
        tws_400.s = 392.03

        tws_794 = Twiss()
        tws_794.beta_x = 18.956766460347758
        tws_794.beta_y = 45.74254845271545
        tws_794.alpha_x = -0.8177409156797565
        tws_794.alpha_y = 1.3743713817184213
        tws_794.E = 6.588
        tws_794.s = 794.786

        tws_1460 = Twiss()
        tws_1460.beta_x = 26.316332066652432
        tws_1460.beta_y = 29.88398255328694
        tws_1460.alpha_x = -1.1095783987321168
        tws_1460.alpha_y = 0.975875866662716
        tws_1460.E = 14
        tws_1460.s = 1459.58

        self.sections = [
            LatSection("T4D+", str_cells=["I1", "L1", "L2", "L3", "CL", "TL34", "SASE1", "T4", "SASE3", "T4D"], load_all=False),
            LatSection("T5D+", str_cells=["I1", "L1", "L2", "L3", "CL", "TL34", "T1",
                                               "SASE2", "T3", "T5", "T5D"], load_all=False),
            LatSection("TLD+", str_cells=["I1", "L1", "L2", "L3", "CL", "TLD"], load_all=False),

            LatSection("60 - 450", str_cells=["L1", "L2"], stop=self.lats["L2"].otrb_450_b2, z0=62.089),
            LatSection("400 - 900", str_cells=["L2", "L3"], start=self.lats["L2"].otra_392_b2,
                       stop=self.lats["L3"].bpmc_902_l3, z0=392.03, tw=tws_400),
            LatSection("800 - 1600", str_cells=["L3", "CL"], start=self.lats["L3"].bpmc_794_l3,
                       stop=self.lats["L3"].otrbw_1597_l3, z0=794.786, tw=tws_794),
            LatSection("1460 - 1930", str_cells=["L3", "CL"], start=self.lats["L3"].tora_1459_l3,
                       stop=self.lats["CL"].otrbw_1929_tl, z0=1459.58, tw=tws_1460),
            LatSection("SASE1", str_cells=["SASE1", "T4"], stop=self.lats["T4"].stsub_2583_t4, z0=2025.38),

            LatSection("T4", str_cells=["T4"], z0=2438.517 + 23.2),
            #
            LatSection("SASE3", str_cells=["T4", "SASE3"], start=self.lats["T4"].stsub_2583_t4,
                       z0=2560.45 + 23.2, tw=tws_sase3),

            LatSection("SASE2", str_cells=["T1", "SASE2", "T3"], z0=2025.385823000017),
            LatSection("T3 + T5", str_cells=["T3", "T5"], z0=2424),

            LatSection("I1D", str_cells=["I1", "I1D"]),
            LatSection("B1D", str_cells=["I1", "L1", "B1D"]),
            LatSection("B2D", str_cells=["I1", "L1", "L2", "B2D"]),


            # LatSection("I1", str_cells = ["I1"]),
            # LatSection("L1", str_cells = ["L1"], z0=62.1),
            # LatSection("L2", str_cells=["L2"], z0=229.30),
            # LatSection("L3", str_cells=["L2", "L3", "CL"], start=self.lats["L2"].engrd_419_b2,
            #                    stop=self.lats["CL"].bpmi_1693_cl, z0=396.22+23.2, tw=tws_L3),



            # LatSection("CL", str_cells=["L3", "CL", "TL34", "SASE1"], start=self.lats["L3"].bpmr_1307_l3,
            #                    stop=self.lats["SASE1"].qa_2253_sa1, z0=1307, tw=tws_cl),
#
            # LatSection("SASE1", str_cells=[ "TL34", "SASE1", "T4"], stop=self.lats["T4"].stsub_2583_t4, z0=1957.18564 + 23.2),


            # LatSection("SASE2", str_cells=["TL34_SA2", "T1", "SASE2", "T3", "T5"], z0=1957.18564+23.2),

            #LatSection("up to B1", str_cells=["I1", "L1"]),
            #LatSection("up to B2", str_cells=["I1", "L1", "L2"]),
            #LatSection("up to CL", str_cells=["I1", "L1", "L2", "L3"]),
            #LatSection("up to TL", str_cells=["I1", "L1", "L2", "L3", "CL"]),
            #LatSection("up to SASE1", str_cells=["I1", "L1", "L2", "L3", "CL", "TL34", "SASE1"]),

            #LatSection("T4D", str_cells=["I1", "L1", "L2", "L3", "CL", "TL34", "SASE1", "T4", "SASE3", "T4D"]),


            #LatSection("up to SASE3", str_cells=["I1", "L1", "L2", "L3", "CL", "SASE1", "T4", "SASE3"])
        ]


    def load(self):
        self.lats = {}
        for sec in self.config.keys():
            self.lats[sec] = importlib.import_module(self.config[sec])
            logger.debug(self.lats[sec])

    def get_slice_sequence(self, seq, start=None, stop=None):
        seq = list(flatten(seq))
        names = [elem.id for elem in seq]
        try:
            if start != None:
                id1 = names.index(start.id)
            else:
                id1 = 0
            if stop != None:
                id2 = names.index(stop.id) + 1
                new_seq = seq[id1:id2]
            else:
                new_seq= seq[id1:]
        except:
            logger.error('cannot construct sequence, element not found')
            raise

        # switched off zero order coupler kick
        for elem in new_seq:
            if elem.__class__ == Cavity:
                elem.vx_up = 0.
                elem.vy_up = 0.
                elem.vx_down = 0.
                elem.vy_down = 0.

        return new_seq

    def return_twiss_des(self, section):
        self.tws0 = Twiss()
        self.tws0.E = 0.005000000
        self.tws0.beta_x = 55.7887190242
        self.tws0.beta_y = 55.7887190242
        self.tws0.alpha_x = 18.185436973
        self.tws0.alpha_y = 18.185436973
        if section.tw != None:
            logger.debug("return_twiss_des: config twiss")
            return section.tw
        else:
            try:
                tws = self.lats[section.str_cells[0]].tws
                logger.debug("return_twiss_des: twiss in the lattice")
            except:
                tws = self.tws0
                logger.debug("return_twiss_des: default twiss")
            return tws

    def get_section(self, name):
        names = [sec.name for sec in self.sections]
        indx = names.index(name)
        section = self.sections[indx]
        return section

    def get_sequence(self, section):
        #[print(sec_name) for sec_name in section.str_cells]
        cells = [self.lats[sec_name].cell for sec_name in section.str_cells]

        section.seq = self.get_slice_sequence(cells, start=section.start, stop=section.stop)
        return section.seq

    def get_correct_init_twiss(self, sequence, stop_element, tws_i):
        if stop_element == None:
            return tws_i
        seq = [copy(elem) for elem in self.get_slice_sequence(sequence, stop=stop_element)]
        tws = twiss(MagneticLattice(seq[:-1]), tws_i)
        return tws[-1]


    def return_lat_section(self, current_lat_section, start=None, stop=None): #qt_currentIndex=None, start=None, stop=None):
        """
        Method modifies an introduced LatSection object (arg: current_lat_section) taking into account
        "start" and "stop" elements and returns that object.

        :param current_lat_section: LatSection object
        :param start: start Element object (ocelot.cpbd.elements)
        :param stop: stop Element object (ocelot.cpbd.elements)
        :return: LatSection
        """
        logger.debug("return_lat: ... ")

        section = self.get_section(current_lat_section)
        section.seq = self.get_sequence(section)

        section.tws_des = self.return_twiss_des(section)
        section.tws_des = self.get_correct_init_twiss(section.seq, stop_element=start, tws_i=section.tws_des)

        logger.debug("len(section.seq) = " + str(len(section.seq)))

        method = MethodTM()
        method.global_method = TransferMap
        section.lat = MagneticLattice(self.get_slice_sequence(section.seq, start=start, stop=stop), method=method)
        return section




if __name__ == "__main__":
    xfel_lat = XFELLattice()
    for sec in xfel_lat.sections:
        print(sec.name)
    xfel_lat.return_lat_section("I1")
    #print(xfel_lat.sections.keys())