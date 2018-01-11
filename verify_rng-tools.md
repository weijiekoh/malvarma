# Verifying the rng-tools package

The `rng-tools` package for Raspbian can be downloaded from any of the following mirrors:

- http://mirror.rise.ph/raspbian/raspbian/pool/main/r/rng-tools/rng-tools_2-unofficial-mt.14-1_armhf.deb
- http://mirror.ox.ac.uk/sites/archive.raspbian.org/archive/raspbian/pool/main/r/rng-tools/rng-tools_2-unofficial-mt.14-1_armhf.deb
- https://mirrors.ocf.berkeley.edu/raspbian/raspbian/pool/main/r/rng-tools/rng-tools_2-unofficial-mt.14-1_armhf.deb


The SHA256 hash of `rng-tools_2-unofficial-mt.14-1_armhf.deb` is:

`115e359d38d24208eb95844b891838c539a92626ccfcfe238b0be43d374c80d8`

This should match the SHA256 hash for `rng-tools` as provided by any Raspbian
Stretch mirror, such as any of the following. Note that each `Packages` file is
about 59M in size.

- http://mirror.rise.ph/raspbian/raspbian/dists/stretch/main/binary-armhf/Packages
- https://mirrors.ocf.berkeley.edu/raspbian/raspbian/dists/stretch/main/binary-armhf/Packages
- http://mirror.ox.ac.uk/sites/archive.raspbian.org/archive/raspbian/dists/stretch/main/binary-armhf/Packages

```
Package: rng-tools
Version: 2-unofficial-mt.14-1
Architecture: armhf
Maintainer: Henrique de Moraes Holschuh <hmh@debian.org>
Installed-Size: 156
Depends: libc6 (>= 2.4), udev (>= 0.053) | makedev (>= 2.3.1-77)
Conflicts: intel-rng-tools
Replaces: intel-rng-tools
Provides: intel-rng-tools
Priority: optional
Section: utils
Filename: pool/main/r/rng-tools/rng-tools_2-unofficial-mt.14-1_armhf.deb
Size: 48706
SHA256: 115e359d38d24208eb95844b891838c539a92626ccfcfe238b0be43d374c80d8
SHA1: ded722313428e79793076028663d6ac4ea4335eb
MD5sum: e5780182cc42eff294802f94930b7090
```

A full list of Raspbian mirrors can be found here: https://www.raspbian.org/RaspbianMirrors
