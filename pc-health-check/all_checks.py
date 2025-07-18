import shutil
import sys
import os

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def main():
    if check_reboot():
        print("Pending reboot detected.")
        return 1
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk space is too low.")
        return 1

    print("System is healthy.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
