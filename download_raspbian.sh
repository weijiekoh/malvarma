#!/bin/sh

echo "Downloading Raspbian Lite..."
axel -a https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/2017-11-29-raspbian-stretch-lite.zip -o \
    raspberry/2017-11-29-raspbian-stretch-lite.zip

wget -nv https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/2017-11-29-raspbian-stretch-lite.zip.sha256 \
    -O raspberry/raspbian_checksum

echo "Verifying checksums..."
sha256sum -c raspberry/raspbian_checksum

echo "Unzipping Raspbian..."
cd raspberry
unzip 2017-11-29-raspbian-stretch-lite.zip 
mv 2017-11-29-raspbian-stretch-lite.img raspbian_mod.img
