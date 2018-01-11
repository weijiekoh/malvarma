# Verifying the rngtest binary

The `rng-tools` package for Raspbian can be downloaded from:

http://mirror.rise.ph/raspbian/raspbian/pool/main/r/rng-tools/rng-tools_2-unofficial-mt.14-1_armhf.deb

The SHA256 hash of `rng-tools_2-unofficial-mt.14-1_armhf.deb` is:

`115e359d38d24208eb95844b891838c539a92626ccfcfe238b0be43d374c80d8`

This should match the SHA256 hash for `rng-tools` as provided by any Raspbian
Stretch mirror, such as any of the following. Note that each `Packages` file is
about 59M in size.

http://mirror.rise.ph/raspbian/raspbian/dists/stretch/main/binary-armhf/Packages
https://mirrors.ocf.berkeley.edu/raspbian/raspbian/dists/stretch/main/binary-armhf/Packages
http://mirror.ox.ac.uk/sites/archive.raspbian.org/archive/raspbian/dists/stretch/main/binary-armhf/Packages

A full list of Raspbian mirrors can be found here: https://www.raspbian.org/RaspbianMirrors