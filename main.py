from network import port_scan
import ipaddress
import threading
from queue import Queue
import sys
import time
import curses
from curses import wrapper
'''
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
'''


def main(main_screen):
    curses.cbreak()
    curses.noecho()

    main_screen.addstr("This is a string for the screen")
    main_screen.refresh()

    curses.curs_set(1)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    while True:

        c = main_screen.getch()
        if chr(c) == "q":
            break

        main_screen.addch(chr(c), curses.color_pair(
            1) | curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)

        main_screen.refresh()


wrapper(main)


print("Window ended")
