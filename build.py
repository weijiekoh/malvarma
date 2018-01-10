#!/usr/bin/env python3
import os
import sys
import subprocess

RPI_DIR = "raspberry"
MOUNTPT = "mountpt"
CHECKSUMS = "checksums"
RPI_IMG = "2017-11-29-raspbian-stretch-lite.img"
ROOT_MSG = ("Please run this script using sudo python3 {file} but manually"
            " vet the source code first.".format(file=__file__))
WALLETGEN_DIRNAME = "py2-monero-wallet-generator"
RNGTOOLS_FILE = "rng-tools_2-unofficial-mt.14-1_armhf.deb"

if __name__ == "__main__":
    # Exit if the user is not root
    # if False:
    if True:
        if os.getuid() != 0:
            print(ROOT_MSG)
            sys.exit(0)

    current_dir = os.path.dirname(__file__)
    mountpt = os.path.join(current_dir, RPI_DIR, MOUNTPT)
    imgfile = os.path.join(current_dir, RPI_DIR, RPI_IMG)
    config_file = os.path.join(RPI_DIR, "boot_config.txt")
    cmdline_file = os.path.join(RPI_DIR, "boot_cmdline.txt")
    rc_local_file = os.path.join(RPI_DIR, "etc_rc_local")
    walletgen_dir = os.path.join(current_dir, WALLETGEN_DIRNAME)
    rngtools_file = os.path.join(RPI_DIR, RNGTOOLS_FILE)
    
    mount_boot_cmd = ("guestmount -a {imgfile} -m /dev/sda1 --rw {mountpt}") \
        .format(mountpt=mountpt, imgfile=imgfile)

    mount_cmd = ("guestmount -a {imgfile} -m /dev/sda2 --rw {mountpt}") \
        .format(mountpt=mountpt, imgfile=imgfile)

    copy_config_cmd = ("cp {config_file} {mountpt}/config.txt") \
        .format(config_file=config_file, mountpt=mountpt)

    copy_cmdline_cmd = ("cp {cmdline_file} {mountpt}/cmdline.txt") \
        .format(cmdline_file=cmdline_file, mountpt=mountpt)

    unmount_cmd = ("guestunmount {mountpt}".format(mountpt=mountpt))

    remove_ssh_cmd = "rm -rf {mountpt}/usr/sbin/sshd".format(mountpt=mountpt)
    remove_avahi_cmd = "rm -rf {mountpt}/usr/sbin/avahi-daemon".format(mountpt=mountpt)
    remove_rsync_cmd = "rm -rf {mountpt}/usr/bin/rsync".format(mountpt=mountpt)
    remove_thd_cmd = "rm -rf {mountpt}/usr/sbin/thd".format(mountpt=mountpt)
    remove_bt_cmd = "rm -rf {mountpt}/usr/sbin/bluetoothd".format(mountpt=mountpt)
    remove_dhcpd_cmd = "rm -rf {mountpt}/sbin/dhcpd*".format(mountpt=mountpt)
    remove_dhclient_cmd = "rm -rf {mountpt}/sbin/dhclient*".format(mountpt=mountpt)

    copy_rngtools_cmd = "cp -r {rngtools_file} {mountpt}".format(rngtools_file=rngtools_file, mountpt=mountpt)
    copy_wallegen_cmd = "cp -r {walletgen_dir} {mountpt}".format(walletgen_dir=walletgen_dir, mountpt=mountpt)
    copy_rc_local_cmd = "cp {rc_local_file} {mountpt}/etc/rc.local".format(rc_local_file=rc_local_file, mountpt=mountpt)

    command_sequence = [
            mount_boot_cmd,
            copy_config_cmd,
            copy_cmdline_cmd,
            unmount_cmd,
            mount_cmd,
            remove_ssh_cmd,
            remove_avahi_cmd,
            remove_rsync_cmd,
            remove_thd_cmd,
            remove_bt_cmd,
            remove_dhcpd_cmd,
            copy_rngtools_cmd,
            copy_wallegen_cmd,
            copy_rc_local_cmd,
            unmount_cmd
    ]

    for command in command_sequence:
        print(command)
        subprocess.check_call(command, shell=True)
