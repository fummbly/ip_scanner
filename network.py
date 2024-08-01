import socket

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
