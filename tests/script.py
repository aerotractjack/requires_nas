import subprocess
from requires_nas import requires_nas

unmount_command = ["sudo", "umount", "/home/aerotract/NAS/main"]

print("NAS is mounted")
for i in range(3):
    print(requires_nas())

print("unmounting NAS")
subprocess.run(unmount_command, check=True)
for i in range(3):
    if requires_nas():
        print("Mounted NAS")
    else:
        print("NAS already mounted")
