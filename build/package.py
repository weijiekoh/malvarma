#!/usr/bin/env python3

"""
This script checksums, signs, and compresses malvarma-<version>.img, and
creates malvarma-<version>.tar.bz2.

The author's GPG signature is hardcoded below.
"""

import os
import shutil
import sys
import subprocess

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 package.py malvarma-<version>.img")
        sys.exit(1)

    imgfile = sys.argv[1]
    folder_name = imgfile.split(".img")[0]

    if not os.path.exists(imgfile):
        print("Error: {imgfile} does not exist.".format(imgfile=imgfile))
        sys.exit(1)

    print("Checksumming...")
    subprocess.check_call("sha256sum {imgfile} > {imgfile}.sha256".format(imgfile=imgfile),
                          shell=True, stderr=subprocess.STDOUT)

    print("Signing...")
    subprocess.check_call("gpg --detach-sign --default-key 0x90DB43617CCC1632 --sign {imgfile}".format(imgfile=imgfile),
                          shell=True, stderr=subprocess.STDOUT)

    print("Compressing")
    shutil.rmtree(folder_name, ignore_errors=True)
    os.makedirs(folder_name)
    shutil.move(imgfile, folder_name)
    shutil.move(imgfile + ".sig", folder_name)
    shutil.move(imgfile + ".sha256", folder_name)

    subprocess.check_call("tar -cvjSf {folder_name}.tar.bz2 {folder_name}".format(folder_name=folder_name),
                          shell=True, stderr=subprocess.STDOUT)
