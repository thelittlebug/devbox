# devbox

## install virtualbox
download: https://download.virtualbox.org/virtualbox/6.1.6/

## create virtual machine
    name: xubuntu2004
    memory size: 8192mb
    main partition:
        name: xubuntu2004.vdi
        size: 128gb
    shared clipboard: enabled
    drag'n'drop: enabled
    cpu cores 4
    enable 3d acceleration
    network 1:
        bridged
    network 2:
        host only, without dhcp
        host addr: 192.168.251.1/24
        mac addr: 08:00:27:a1:a3:fc

## install xubuntu
download: http://ftp.uni-kl.de/pub/linux/ubuntu-dvd/xubuntu/releases/20.04/release/xubuntu-20.04-desktop-amd64.iso

    language: english
    keyboard: german, no dead keys
    install third-party software...
    erase disk and install
    name: tlb
    computer name: tlbvm
    username: tlb

restart

## path a: use old data partition (if possible)
add data.vdi to virtualbox

    sudo mkdir /devbox
    sudo chown tlb:tlb /devbox
    sudo mount /dev/sdb1 /devbox
    cd /devbox

before the 1st install the symlinks are not set. so you have to run
    /devbox/bin/devbox-install

after the 1st install you are able to devbox-install from everywhere

## path b: create new data partition
create a new 256gb data partition in virtualbox

## path b: restore devbox
    sudo apt install git
    cd /
    git clone https://github.com/thelittlebug/devbox
    chown tlb:tlb /devbox
    cd devbox
    bin/restore-devbox
    ./install

## path b: recover files
    borg-list [snapshotname]
    cd /devbox
    borg-extract snapshotname [paths to restore]

