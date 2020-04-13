import subprocess  # For executing a shell command


def log(msg, level):
    print(msg)
    subprocess.call(["log_tool", "-a", msg, "-t", level, "-N", "Power Check", "-G", "Power"])


if __name__ == '__main__':
    output = subprocess.check_output(["ps"])
    # print(output)
    if "auto_power_off.py" not in output:
        log("Check power thread dead! Starting again!", "1")
        subprocess.call(["/bin/sh", "/share/CACHEDEV1_DATA/software/start_check_power.sh"])
    # else:
        # print("Check power OK")
