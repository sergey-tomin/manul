"""
XFEL machine interface
S.Tomin, 2017
"""
from __future__ import absolute_import, print_function

try:
    # in server "doocsdev12" set environment
    #  $ export PYTHONPATH=/home/ttflinac/user/python-2.7/Debian/
    import epics
except:
    pass  # Show message on Constructor if we try to use it.

import sys
import numpy as np
import subprocess
import base64
from threading import Lock
from mint.interface import MachineInterface, Device
import logging

logger = logging.getLogger(__name__)
from ocelot.cpbd.response_matrix import *


class AlarmDevice(Device):
    """
    Devices for getting information about Machine status
    """

    def __init__(self, eid=None):
        super(AlarmDevice, self).__init__(eid=eid)


class BESSYMachineInterface(MachineInterface):
    """
    Machine Interface for European XFEL
    """

    def __init__(self):
        super(BESSYMachineInterface, self).__init__()
        if 'pydoocs' not in sys.modules:
            print('error importing doocs library')
        self.logbook = "xfellog"
        self.allow_star_operation = False
        self.hide_section_selection = True
        self.hide_close_trajectory = True
        self.hide_xfel_specific = True
        self.hide_dispersion_tab = True
        self.twiss_periodic = True
        self.orm_method = RingRM
        self.drm_method = LinacDisperseSimRM

    def get_value(self, channel):
        """
        Getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        logger.debug(" get_value: channel" + channel)
        val = epics.PV(channel).get()
        # print(channel, "   TIMESTAMP:",  val["timestamp"])

        return val

    def set_value(self, channel, val):
        """
        Method to set value to a channel

        :param channel: (str) String of the devices name used in doocs
        :param val: value
        :return: None
        """
        # print("SETTING")
        epics.PV(channel).put(val)
        return

    def get_raw_value(self, channel):
        """
        Getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        logger.debug(" get_raw_value: channel" + channel)
        val = pydoocs.read(channel)
        return val

    def get_charge(self):
        return self.get_value("XFEL.DIAG/CHARGE.ML/TORA.25.I1/CHARGE.SA1")

    def send_to_logbook(self, *args, **kwargs):
        """
        Send information to the electronic logbook.

        :param args:
            Values sent to the method without keywork
        :param kwargs:
            Dictionary with key value pairs representing all the metadata
            that is available for the entry.
        :return: bool
            True when the entry was successfully generated, False otherwise.
        """
        author = kwargs.get('author', '')
        title = kwargs.get('title', '')
        severity = kwargs.get('severity', '')
        text = kwargs.get('text', '')
        image = kwargs.get('image', None)
        elog = self.logbook

        # The DOOCS elog expects an XML string in a particular format. This string
        # is beeing generated in the following as an initial list of strings.
        succeded = True  # indicator for a completely successful job
        # list beginning
        elogXMLStringList = ['<?xml version="1.0" encoding="ISO-8859-1"?>', '<entry>']

        # author information
        elogXMLStringList.append('<author>')
        elogXMLStringList.append(author)
        elogXMLStringList.append('</author>')
        # title information
        elogXMLStringList.append('<title>')
        elogXMLStringList.append(title)
        elogXMLStringList.append('</title>')
        # severity information
        elogXMLStringList.append('<severity>')
        elogXMLStringList.append(severity)
        elogXMLStringList.append('</severity>')
        # text information
        elogXMLStringList.append('<text>')
        elogXMLStringList.append(text)
        elogXMLStringList.append('</text>')
        # image information
        if image:
            try:
                encodedImage = base64.b64encode(image)
                elogXMLStringList.append('<image>')
                elogXMLStringList.append(encodedImage.decode())
                elogXMLStringList.append('</image>')
            except:  # make elog entry anyway, but return error (succeded = False)
                succeded = False
        # list end
        elogXMLStringList.append('</entry>')
        # join list to the final string
        elogXMLString = '\n'.join(elogXMLStringList)
        # open printer process
        try:
            lpr = subprocess.Popen(['/usr/bin/lp', '-o', 'raw', '-d', elog],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            # send printer job
            lpr.communicate(elogXMLString.encode('utf-8'))
        except:
            succeded = False
        return succeded


# test interface


class TestMachineInterface(MachineInterface):
    """
    Machine interface for testing
    """

    def __init__(self):
        super(TestMachineInterface, self).__init__()
        self.data = 1.
        self.allow_star_operation = False
        self.hide_section_selection = True
        self.hide_close_trajectory = True
        self.hide_xfel_specific = True
        self.hide_dispersion_tab = True
        self.twiss_periodic = True
        self.orm_method = RingRM
        self.drm_method = LinacDisperseSimRM

    def get_alarms(self):
        return np.random.rand(4)  # 0.0, 0.0, 0.0, 0.0]

    def get_value(self, device_name):
        """
        Testing getter function for XFEL.

        :param channel: (str) String of the devices name used in doocs
        :return: Data from pydoocs.read(), variable data type depending on channel
        """
        # if "QUAD" in device_name:
        #    return 0
        return np.random.rand(1)[0] - 0.5  # self.data

    def set_value(self, device_name, val):
        """
        Testing Method to set value to a channel

        :param channel: (str) String of the devices name used in doocs
        :param val: value
        :return: None
        """
        # print("set:", device_name,  "-->", val)
        self.data += np.sqrt(val ** 2)
        return 0.0

    def get_bpms_xy(self, bpms):
        """
        Testing method for getting bmps data

        :param bpms: list of string. BPMs names
        :return: X, Y - two arrays in [m]
        """
        X = np.zeros(len(bpms))
        Y = np.zeros(len(bpms))
        return X, Y

    def get_charge(self):
        return 0

    @staticmethod
    def send_to_logbook(*args, **kwargs):
        """
        Send information to the electronic logbook.

        :param args:
            Values sent to the method without keywork
        :param kwargs:
            Dictionary with key value pairs representing all the metadata
            that is available for the entry.
        :return: bool
            True when the entry was successfully generated, False otherwise.
        """
        author = kwargs.get('author', '')
        title = kwargs.get('title', '')
        severity = kwargs.get('severity', '')
        text = kwargs.get('text', '')
        elog = kwargs.get('elog', '')
        image = kwargs.get('image', None)

        # TODO: @sergey.tomin Figure out what to do for logbook at the TestMachineInterface
        print('Send to Logbook not implemented for TestMachineInterface.')
        return True
