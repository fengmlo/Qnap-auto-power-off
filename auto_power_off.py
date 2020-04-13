import platform  # For getting the operating system name
import subprocess  # For executing a shell command
import sys
import threading
import time
from time import sleep

failCount = 0
routerAddress = "192.168.1.1"


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


def shut_down():
    return subprocess.call(["poweroff"]) == 0


def check_power(host):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    result = ping(host)
    global failCount
    if not result:
        failCount += 1
        log("ping fail", "1")
        if failCount > 6:
            log("ping fail for 8 minutes, nas will shutdown", "2")
            if shut_down():
                log("shutdown execute successfully", "0")
                sys.exit()
            else:
                log("shutdown execute fail", "1")
    else:
        failCount = 0


def log(msg, level):
    print(msg)
    subprocess.call(["log_tool", "-a", msg, "-t", level, "-N", "Power Check", "-G", "Power"])


if __name__ == '__main__':

    log("Check power start!", "0")
    while True:
        threading.Thread(target=check_power(routerAddress), name='CheckPowerThread').start()
        sleep(60)
