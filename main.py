from network import port_scan
import ipaddress
import threading
from queue import Queue
import sys
import time

print_lock = threading.Lock()


def threader():
    while True:

        worker = q.get()

        port_scan(f"{worker}")

        q.task_done()


q = Queue()


for x in range(25):
    t = threading.Thread(target=threader)

    t.daemon = True

    t.start()


start = time.time()

if len(sys.argv) != 2:
    print("Invalid use of program")
    exit()

net = ipaddress.ip_network(sys.argv[1])

for worker in net:
    q.put(worker)


q.join()
