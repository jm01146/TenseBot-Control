import serial.tools.list_ports

def list_ports():
    # Grabs all ports in use or registered in device
    ports = serial.tools.list_ports.comports()
    # Stores it in easy string format
    ports_list = [str(one_port) for one_port in ports]
    return ports_list

def select_port():
    # Prints for user to select. WARNING: Grab smallest port with bluetooth address.
    # Ex. COM25 (Bluetooth) and COM26 (Bluetooth) select COM25
    printPorts = print(list_ports())
    ports_list = list_ports()
    val = input('Select Port: COM')
    # User selection for port to be used
    for port in ports_list:
        if port.startswith('COM' + str(val)):
            return 'COM' + str(val)
    raise ValueError("Port not found")

# Port way to open at the apporiate addresses and baudrate
def open_serial(port):
    serial_inst = serial.Serial()
    serial_inst.baudrate = 9600
    serial_inst.port = port
    serial_inst.open()
    return serial_inst

# Send commands to serial arduino
def send_command(serial_inst):
    while True:
        command = input('Arduino Command: (ON/OFF); ')
        serial_inst.write(command.encode('utf-8'))
        if command == 'exit':
            break

# Example to run the entire code
#     port = select_port()
#     serial_connection = open_serial(port)
#     send_command(serial_connection)
