#!/usr/bin/env python3
import os
import sys
import subprocess

VERSION = "0.1.1-alpha"
RPI_DIR = "raspberry"
CONFIG_DIR = "config"
BUILD_DIR = "build"

MALVARMA_IMG_FILE = "malvarma-{version}.img".format(version=VERSION)
MALVARMA_CHECKSUM_FILE = "malvarma-{version}.img.sha256" \
    .format(version=VERSION)

MOUNTPT = "mountpt"
RPI_IMG = "raspbian_mod.img"
ROOT_MSG = ("Please run this script using sudo python3 {file} but manually"
            " vet the source code first.".format(file=__file__))
WALLETGEN_DIRNAME = "py2-monero-wallet-generator"
RNGTOOLS_FILE = "rng-tools_2-unofficial-mt.14-1_armhf.deb"
TEST_ENTROPY_FILE = "test_entropy.py"

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    mountpt = os.path.join(current_dir, RPI_DIR, MOUNTPT)
    imgfile = os.path.join(current_dir, RPI_DIR, RPI_IMG)

    malvarma_imgfile = os.path.join(current_dir, BUILD_DIR, MALVARMA_IMG_FILE)
    malvarma_checksum_file = \
        os.path.join(current_dir, BUILD_DIR, MALVARMA_CHECKSUM_FILE)

    config_file = os.path.join(RPI_DIR, CONFIG_DIR, "boot_config.txt")
    cmdline_file = os.path.join(RPI_DIR, CONFIG_DIR, "boot_cmdline.txt")
    rc_local_file = os.path.join(RPI_DIR, CONFIG_DIR, "etc_rc_local")
    walletgen_dir = os.path.join(current_dir, WALLETGEN_DIRNAME)
    rngtools_file = os.path.join(RPI_DIR, RNGTOOLS_FILE)
    test_entropy_file = os.path.join(current_dir, TEST_ENTROPY_FILE)
    

    create_mountpt_cmd = "mkdir -p {mountpt}".format(mountpt=mountpt)
    # command to mount the /boot partition of the RPi image
    mount_boot_cmd = ("guestmount -a {imgfile} -m /dev/sda1 --rw {mountpt}") \
        .format(mountpt=mountpt, imgfile=imgfile)

    # command to mount the / partition of the RPi image
    mount_cmd = ("guestmount -a {imgfile} -m /dev/sda2 --rw {mountpt}") \
        .format(mountpt=mountpt, imgfile=imgfile)

    # commands to copy config files
    copy_config_cmd = ("cp {config_file} {mountpt}/config.txt") \
        .format(config_file=config_file, mountpt=mountpt)

    copy_cmdline_cmd = ("cp {cmdline_file} {mountpt}/cmdline.txt") \
        .format(cmdline_file=cmdline_file, mountpt=mountpt)

    unmount_cmd = ("guestunmount {mountpt}".format(mountpt=mountpt))

    files_to_remove = [
        "/usr/sbin/sshd",
        "/usr/sbin/avahi-daemon"
        "/usr/bin/rsync",
        "/usr/sbin/thd",
        "/usr/sbin/bluetoothd",
        "/sbin/dhcpd*",
        "/sbin/dhclient*",
        "/lib/systemd/system/regenerate_ssh_host_keys.service",
        "/lib/systemd/system/ifup@.service",
        "/lib/systemd/system/triggerhappy.service",
        "/lib/systemd/system/ssh*",
        "/lib/systemd/system/networking.service",
        "/lib/systemd/system/avahi-daemon.service",
        "/lib/systemd/system/plymouth*",
        "/lib/systemd/system/systemd-update-utmp*",
        "/lib/systemd/system/getty*",
        "/lib/systemd/system/systemd-user-sessions.service",
        "/lib/systemd/system/apt*",
        "/lib/systemd/system/bluetooth.service",
        "/lib/systemd/system/systemd-networkd.service",
        "/lib/systemd/system/dhcpd.service",
        "/lib/systemd/system/nfs*",
        "/lib/systemd/system/systemd-timesyncd.service",
        "/lib/systemd/system/systemd-journal-flush.service",
        "/etc/init.d/bluetooth",
        "/etc/init.d/networking",
        "/etc/init.d/plymouth*",
        "/etc/init.d/nfs-common",
        "/etc/init.d/avahi-daemon",
        "/etc/init.d/dphys-swapfile",
        "/etc/init.d/triggerhappy",
        "/etc/init.d/alsa-utils",
        "/etc/init.d/rsync",
        "/etc/init.d/ssh",
        "/etc/init.d/rpcbind",
        "/etc/init.d/keyboard-setup.sh",
        "/etc/init.d/resize2fs_once",
        "/etc/init.d/dhcpcd",
        "/etc/init.d/raspi-config",
    ]

    # commands to disable unnecessary services
    file_removal_commands = []
    for f in files_to_remove:
        cmd = "rm -rf {mountpt}{f}".format(mountpt=mountpt, f=f)
        file_removal_commands.append(cmd)

    # commands to copy in files needed to create the cold wallet
    copy_rngtools_cmd = "cp -r {rngtools_file} {mountpt}".format(rngtools_file=rngtools_file, mountpt=mountpt)
    copy_wallegen_cmd = "cp -r {walletgen_dir} {mountpt}".format(walletgen_dir=walletgen_dir, mountpt=mountpt)
    copy_rc_local_cmd = "cp {rc_local_file} {mountpt}/etc/rc.local".format(rc_local_file=rc_local_file, mountpt=mountpt)
    copy_test_ent_cmd = "cp {test_entropy_file} {mountpt}".format(test_entropy_file=test_entropy_file, mountpt=mountpt)

    # rename the output img file 
    mv_malvarma_cmd = "mv {imgfile} {malvarma_imgfile}" \
        .format(imgfile=imgfile, malvarma_imgfile=malvarma_imgfile)

    # create a checksum file
    # hash_malvarma_cmd = "sha256sum {malvarma_imgfile} | sed 's/\.\/{build_dir}\///' > {malvarma_checksum_file}" \
        # .format(malvarma_imgfile=malvarma_imgfile, malvarma_checksum_file=malvarma_checksum_file, build_dir=BUILD_DIR)

    # execute each command sequentially
    command_sequence = [
        create_mountpt_cmd,
        mount_boot_cmd,
        copy_config_cmd,
        copy_cmdline_cmd,
        unmount_cmd,
        mount_cmd,
    ]

    command_sequence += file_removal_commands

    command_sequence += [
        copy_rngtools_cmd,
        copy_wallegen_cmd,
        copy_rc_local_cmd,
        copy_test_ent_cmd,
        unmount_cmd,
        mv_malvarma_cmd,
        # hash_malvarma_cmd,
    ]

    for command in command_sequence:
        try:
            print(command)
            subprocess.check_call(command, shell=True, stderr=subprocess.STDOUT)
        except:
            print("Could not build Malvarma. Exiting.")
            break
