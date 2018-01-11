#!/bin/sh

wget -nv https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/2017-11-29-raspbian-stretch-lite.zip -O \
    raspberry/2017-11-29-raspbian-stretch-lite.zip

wget -nv https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/2017-11-29-raspbian-stretch-lite.zip.sha256 \
    -O raspberry/raspbian_checksum

sha256sum -c raspberry/raspbian_checksum

cd raspberry
unzip 2017-11-29-raspbian-stretch-lite.zip 
mv 2017-11-29-raspbian-stretch-lite.img raspbian_mod.img
