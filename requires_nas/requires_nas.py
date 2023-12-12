import subprocess
import os
import time 
import sys

def log(*args):
    print(args)
    sys.stdout.flush()

mp = "/home/aerotract/NAS/main"

def requires_nas(mount_point=mp):
    mount_command = ["sudo", "mount", mount_point]
    try:
        contents = os.listdir(mount_point)
        if len(contents) == 0:
            subprocess.run(mount_command, check=True)
        return 1
    except:
        subprocess.run(mount_command, check=True)
        return 1
    
def requires_nas_loop(mount_point=mp, delay=0.2, n=100, info_logger=log, error_logger=log):
    x = 0
    while True:
        if requires_nas(mount_point=mount_point):
            info_logger("NAS mounted!")
            return 1
        x += 1
        if n is not None and x >= n:
            error_logger("Failed to mount NAS")
            return 0
        info_logger("Waiting for NAS...")
        time.sleep(delay)