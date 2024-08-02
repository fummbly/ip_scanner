import socket

class IPNode:
    def __init__(self):
        self._alive = False
        self._ip = ""
        self._open_ports = []

    def setAlive(self):
        self._alive = True

    def setIP(self, ip):
        self._ip = ip

    def addOpenPort(self, open_port):
        self._open_ports.append(PortNode(open_port))


class PortNode:
    def __init__(self, port = "", banner = ""):
        self._port = port
        self._banner = banner

    def addPort(self, port):
        self._port = port

    def addBanner(self, banner):
        self._banner = banner

ports = [20, 21, 22, 23, 25, 53, 80, 135, 139, 443, 445,  500, 5060, 8080]

def port_scan(address):
    alive = False
    socket.setdefaulttimeout(1)

    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((address, port))
            alive = True
            open_ports.append(port)
            try:
                banner = s.recv(1024).decode()
                print(f"IP: {address} port information")
                print(f"\tport {port} is open with banner {banner}")
            except:
                pass
            continue

        except:
            continue



    if alive:
        print(f"{address}: alive on port(s) {open_ports}")
