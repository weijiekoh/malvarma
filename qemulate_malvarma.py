#!/usr/bin/env python3

import sys
import subprocess

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 run_qemu.py build/malvarma-<version>.img")
        sys.exit(1)

    subprocess.call("qemu-system-arm -kernel raspberry/kernel-qemu-4.4.bin "
                    "-cpu arm1176 -m 256 -M versatilepb -serial stdio "
                    "-append \"root=/dev/sda2 rootfstype=ext4 rw loglevel=3 "
                    "logo.nologo quiet\" -drive "
                    "format=raw,file={malvarma_imgfile} -no-reboot"
                    .format(malvarma_imgfile=sys.argv[1]), shell=True)
