import socket


class IPNode:
    def __init__(self):
        self._alive = False
        self._ip = ""
        self._open_ports = {}

    def setAlive(self):
        self._alive = True

    def getAlive(self):
        return self._alive

    def setIP(self, ip):
        self._ip = ip

    def addOpenPort(self, open_port):
        self._open_ports[open_port] = PortNode(open_port)

    def __repr__(self) -> str:
        message = f"IP: {self._ip}"
        if self._alive:
            message += " alive\n"
        else:
            message += " dead\n"
        if self._open_ports:
            message += "Open Ports:\n"
            for port in self._open_ports:
                message += str(self._open_ports[port])
        return message


class PortNode:
    def __init__(self, port="", banner=""):
        self._port = port
        self._banner = banner

    def addPort(self, port):
        self._port = port

    def addBanner(self, banner):
        self._banner = banner

    def __repr__(self) -> str:
        message = f"\t{self._port}"
        if self._banner:
            message += f": {self._banner}"
        message += "\n"
        return message


ports = [20, 21, 22, 23, 25, 53, 80, 135, 139, 443, 445,  500, 5060, 8080]


def port_scan(address):
    socket.setdefaulttimeout(1)
    ip = IPNode()
    ip.setIP(address)

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((address, port))
            ip.setAlive()
            ip.addOpenPort(port)
            try:
                banner = s.recv(1024).decode()
                ip._open_ports[port].addBanner(banner)
            except:
                continue

        except:
            continue

    if ip.getAlive():
        print(ip)
