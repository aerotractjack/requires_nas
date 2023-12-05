import subprocess
import os

def requires_nas(mount_point="/home/aerotract/NAS/main"):
    mount_command = ["sudo", "mount", mount_point]
    try:
        contents = os.listdir(mount_point)
        if len(contents) == 0:
            subprocess.run(mount_command, check=True)
            return 1
        return 0
    except:
        subprocess.run(mount_command, check=True)
        return 1