import importlib
import logging
import numpy as np
from copy import deepcopy, copy
from ocelot import *
from ocelot.cpbd.magnetic_lattice import *
#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class LatSection:
    def __init__(self, name, str_cells, start=None, stop=None, z0=23.2, tw=None):
        self.name = name
        self.str_cells = str_cells
        self.start = start
        self.stop = stop
        self.z0 = z0
        self.tw = tw


class Lattice:
    def __init__(self, path="lattices.phase_advance_5pi_sase2"):
        self.lat_zi = 23.2 # start position of the lattice in [m]
        self.default_section = "I1"
        self.config = {"FLASH1":       path + ".flash1",
                       "FLASH2":       path + ".flash2",
       
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

        self.sections = [
            LatSection("Arbitrary", str_cells=["FLASH2"]),
            LatSection("FLASH1", str_cells = ["FLASH1"]),
            LatSection("FLASH2", str_cells = ["FLASH2"]),
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
        return new_seq

    def return_twiss_des(self, section):
        self.tws0 = Twiss()
        self.tws0.E = 0.005000000
        self.tws0.alpha_x = 7.4896
        self.tws0.beta_x = 14.9286
        self.tws0.alpha_y = 7.6972
        self.tws0.beta_y = 15.3373
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