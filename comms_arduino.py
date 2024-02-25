import serial.tools.list_ports

def list_ports():
    ports = serial.tools.list_ports.comports()
    ports_list = [str(one_port) for one_port in ports]
    return ports_list

def select_port():
    printPorts = print(list_ports())
    ports_list = list_ports()
    val = input('Select Port: COM')
    for port in ports_list:
        if port.startswith('COM' + str(val)):
            return 'COM' + str(val)
    raise ValueError("Port not found")

def open_serial(port):
    serial_inst = serial.Serial()
    serial_inst.baudrate = 9600
    serial_inst.port = port
    serial_inst.open()
    return serial_inst

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
