import shutil
import sys

def check_disk_usage(disk, min_absolute_gb, min_percent):
    """Returns True if there is enough free disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30

    if percent_free < min_percent or gigabytes_free < min_absolute_gb:
        return False
    return True

def main():
    # Check for at least 2 GB and 10% free on the root partition
    if not check_disk_usage("/", 2, 10):
        print("ERROR: Not enough disk space")
        return 1

    print("Everything ok")
    return 0

if __name__ == "__main__":
    sys.exit(main())