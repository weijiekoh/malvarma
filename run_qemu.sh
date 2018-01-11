#!/bin/sh

qemu-system-arm -kernel raspberry/kernel-qemu-4.4.bin -cpu arm1176 -m 256 -M \
    versatilepb -serial stdio \
    -append "root=/dev/sda2 rootfstype=ext4 rw loglevel=3 logo.nologo quiet" \
    -drive format=raw,file=build/malvarma-0.1-alpha.img -no-reboot 
