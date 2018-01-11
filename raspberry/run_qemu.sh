#!/bin/sh

qemu-system-arm -kernel kernel-qemu-4.4.bin -cpu arm1176 -m 256 -M versatilepb -serial stdio -append "root=/dev/sda2 rootfstype=ext4 rw" -hda malvarma.img -no-reboot
