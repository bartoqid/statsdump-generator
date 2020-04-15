import threading
import time
# Creating threads
def create_threads(list, firewall_admin, firewall_password, function):

    threads = []

    for ip in list:
        th = threading.Thread(target = function, args = (ip, firewall_admin, firewall_password, ))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
