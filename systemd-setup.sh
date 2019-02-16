#!/bin/bash

##### check that systemd is on the system #####
systemd_expected=systemd
systemd_result=`ps -p 1 -o comm=`

if [ "$systemd_expected" != "$systemd_result"  ]; then
  echo System does not appear to be running "systemd" which is required by this script.
  exit 1
fi

##### check if running as root #####
# credit: https://askubuntu.com/questions/15853/how-can-a-script-check-if-its-being-run-as-root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

sc=/bin/systemctl
hd=hunter-douglas-remote-automation@pi

# install necessary python modules
apt install python3-gpiozero

cp systemd.service.template /etc/systemd/system/hunter-douglas-remote-automation@pi.service
systemctl --system daemon-reload

systemctl enable $hd

systemctl start $hd
