#!/usr/bin/env python3
import os
import sys
import subprocess

RPI_DIR = "raspberry"
CONFIG_DIR = "config"
MALVARMA_IMG_FILE = "malvarma.img"
MALVARMA_CHECKSUM_FILE = "malvarma.img.sha256"
MOUNTPT = "mountpt"
CHECKSUMS = "checksums"
RPI_IMG = "2017-11-29-raspbian-stretch-lite.img"
ROOT_MSG = ("Please run this script using sudo python3 {file} but manually"
            " vet the source code first.".format(file=__file__))
WALLETGEN_DIRNAME = "py2-monero-wallet-generator"
RNGTOOLS_FILE = "rng-tools_2-unofficial-mt.14-1_armhf.deb"
TEST_ENTROPY_FILE = "test_entropy.py"

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
    malvarma_imgfile = os.path.join(current_dir, RPI_DIR, MALVARMA_IMG_FILE)
    malvarma_checksum_file = os.path.join(current_dir, RPI_DIR, MALVARMA_CHECKSUM_FILE)
    config_file = os.path.join(RPI_DIR, CONFIG_DIR, "boot_config.txt")
    cmdline_file = os.path.join(RPI_DIR, CONFIG_DIR, "boot_cmdline.txt")
    rc_local_file = os.path.join(RPI_DIR, CONFIG_DIR, "etc_rc_local")
    walletgen_dir = os.path.join(current_dir, WALLETGEN_DIRNAME)
    rngtools_file = os.path.join(RPI_DIR, RNGTOOLS_FILE)
    test_entropy_file = os.path.join(current_dir, TEST_ENTROPY_FILE)
    
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

    remove_ssh_regen_srv = "rm -rf {mountpt}/lib/systemd/system/regenerate_ssh_host_keys.service".format(mountpt=mountpt)
    remove_ifup_srv = "rm -rf {mountpt}/lib/systemd/system/ifup@.service".format(mountpt=mountpt)
    remove_thd_srv = "rm -rf {mountpt}/lib/systemd/system/triggerhappy.service".format(mountpt=mountpt)
    remove_ssh_srv = "rm -rf {mountpt}/lib/systemd/system/ssh*".format(mountpt=mountpt)
    remove_net_srv = "rm -rf {mountpt}/lib/systemd/system/networking.service".format(mountpt=mountpt)
    remove_avahi_srv = "rm -rf {mountpt}/lib/systemd/system/avahi-daemon.service".format(mountpt=mountpt)
    remove_plymouth_srv = "rm -rf {mountpt}/lib/systemd/system/plymouth*".format(mountpt=mountpt)
    remove_utmp_srv = "rm -rf {mountpt}/lib/systemd/system/systemd-update-utmp*".format(mountpt=mountpt)
    remove_getty_srv = "rm -rf {mountpt}/lib/systemd/system/getty*".format(mountpt=mountpt)
    remove_us_srv = "rm -rf {mountpt}/lib/systemd/system/systemd-user-sessions.service".format(mountpt=mountpt)
    remove_apt_srv = "rm -rf {mountpt}/lib/systemd/system/apt*".format(mountpt=mountpt)
    remove_bt_srv = "rm -rf {mountpt}/lib/systemd/system/bluetooth.service".format(mountpt=mountpt)
    remove_sysd_net_srv = "rm -rf {mountpt}/lib/systemd/system/systemd-networkd.service".format(mountpt=mountpt)
    remove_dhcpd_srv = "rm -rf {mountpt}/lib/systemd/system/dhcpd.service".format(mountpt=mountpt)
    remove_nfs_srv = "rm -rf {mountpt}/lib/systemd/system/nfs*".format(mountpt=mountpt)
    remove_nts_srv = "rm -rf {mountpt}/lib/systemd/system/systemd-timesyncd.service".format(mountpt=mountpt)
    remove_journal_flush_srv = "rm -rf {mountpt}/lib/systemd/system/systemd-journal-flush.service".format(mountpt=mountpt)

    remove_bt_initd_srv = "rm -rf {mountpt}/etc/init.d/bluetooth".format(mountpt=mountpt)
    remove_net_initd_srv = "rm -rf {mountpt}/etc/init.d/networking".format(mountpt=mountpt)
    remove_plymouth_initd_srv = "rm -rf {mountpt}/etc/init.d/plymouth*".format(mountpt=mountpt)
    remove_nfs_initd_srv = "rm -rf {mountpt}/etc/init.d/nfs-common".format(mountpt=mountpt)
    remove_avahi_initd_srv = "rm -rf {mountpt}/etc/init.d/avahi-daemon".format(mountpt=mountpt)
    remove_swap_initd_srv = "rm -rf {mountpt}/etc/init.d/dphys-swapfile".format(mountpt=mountpt)
    remove_thd_initd_srv = "rm -rf {mountpt}/etc/init.d/triggerhappy".format(mountpt=mountpt)
    remove_alsa_initd_srv = "rm -rf {mountpt}/etc/init.d/alsa-utils".format(mountpt=mountpt)
    remove_rsync_initd_srv = "rm -rf {mountpt}/etc/init.d/rsync".format(mountpt=mountpt)
    remove_ssh_initd_srv = "rm -rf {mountpt}/etc/init.d/ssh".format(mountpt=mountpt)
    remove_rpcbind_initd_srv = "rm -rf {mountpt}/etc/init.d/rpcbind".format(mountpt=mountpt)
    remove_kbd_initd_srv = "rm -rf {mountpt}/etc/init.d/keyboard-setup.sh".format(mountpt=mountpt)

    copy_rngtools_cmd = "cp -r {rngtools_file} {mountpt}".format(rngtools_file=rngtools_file, mountpt=mountpt)
    copy_wallegen_cmd = "cp -r {walletgen_dir} {mountpt}".format(walletgen_dir=walletgen_dir, mountpt=mountpt)
    copy_rc_local_cmd = "cp {rc_local_file} {mountpt}/etc/rc.local".format(rc_local_file=rc_local_file, mountpt=mountpt)
    copy_test_ent_cmd = "cp {test_entropy_file} {mountpt}".format(test_entropy_file=test_entropy_file, mountpt=mountpt)

    mv_malvarma_cmd = "mv {imgfile} {malvarma_imgfile}" \
        .format(imgfile=imgfile, malvarma_imgfile=malvarma_imgfile)
    hash_malvarma_cmd = "sha256sum {malvarma_imgfile} > {malvarma_checksum_file}" \
        .format(malvarma_imgfile=malvarma_imgfile, malvarma_checksum_file=malvarma_checksum_file)

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
            remove_ssh_regen_srv,
            remove_dhcpd_cmd,
            remove_net_srv,
            remove_ssh_srv,
            remove_thd_srv,
            remove_ifup_srv,
            remove_avahi_srv,
            remove_plymouth_srv,
            remove_getty_srv,
            remove_utmp_srv,
            remove_us_srv,
            remove_apt_srv,
            remove_bt_srv,
            remove_sysd_net_srv,
            remove_dhcpd_srv,
            remove_nfs_srv,
            remove_nts_srv,
            remove_journal_flush_srv,

            remove_bt_initd_srv,
            remove_net_initd_srv,
            remove_plymouth_initd_srv,
            remove_nfs_initd_srv,
            remove_avahi_initd_srv,
            remove_swap_initd_srv,
            remove_thd_initd_srv,
            remove_alsa_initd_srv,
            remove_rsync_initd_srv,
            remove_ssh_initd_srv,
            remove_rpcbind_initd_srv,
            remove_kbd_initd_srv,

            copy_rngtools_cmd,
            copy_wallegen_cmd,
            copy_rc_local_cmd,
            copy_test_ent_cmd,

            unmount_cmd,

            mv_malvarma_cmd,
            hash_malvarma_cmd,
    ]

    for command in command_sequence:
        print(command)
        subprocess.check_call(command, shell=True)
