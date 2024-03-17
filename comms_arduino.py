# Importing Libraries
import serial.tools.list_ports
import re


class Ports(serial.Serial):
    def __init__(self):
        super().__init__()
        # Taking serialInst adn scanningPorts as Objects that have the properties of Serial Functions
        self.serialInst = serial.Serial()
        self.scanningPorts = serial.tools.list_ports.comports()

        # Setting the values that will be gathered from the GUI
        self.serialInst.baudrate = 9600
        self.portName = None
        self.portList = None
        self.com = None

    # Making a function that Prints all the Ports
    def list_port(self):
        ports_listed = []
        for ports in self.scanningPorts:
            ports_listed.append(str(ports))
        self.portList = ports_listed[:]
        return self.portList

    # Way for the GUI device to select the baudrate
    def baudrate_selection(self, gui_baudrate):
        self.serialInst.baudrate = gui_baudrate

    # Way for the GUI device to select the COM Device
    def comm_selection(self, gui_com):
        self.com = gui_com
        match = re.search(r'COM(\d+)', self.com)
        if match:
            self.com = str(match.group())

    # Way for the GUI device to connect to COM Device
    def connect(self):
        self.serialInst.port = self.com
        self.serialInst.open()

    # Way for the GUI device to send to COM Device
    def send(self, command):
        self.serialInst.write(command.encode('utf-8'))
