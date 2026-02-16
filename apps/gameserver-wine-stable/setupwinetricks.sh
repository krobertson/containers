#!/bin/bash

exec 6>display.log
/usr/bin/Xvfb -displayfd 6 -nolisten tcp -nolisten unix &
XVFB_PID=$!
while [[ ! -s display.log ]]; do
  sleep 1
done
read -r DPY_NUM < display.log
rm display.log

export DISPLAY=:$DPY_NUM

PACKAGES="$@"
for PACKAGE in $PACKAGES; do
  winetricks -q $PACKAGE
done
rm -rf ~/.cache/winetricks ~/.cache/fontconfig

exec 6>&-
kill $XVFB_PID

exit 0

