#!/bin/bash
here=$(dirname ${BASH_SOURCE[0]})
if [ -z "$1" ];  then
    echo "Needs period" 2>&1
    exit 1
fi;

while true; do
    $here/irssi-dump.py $1 | python $here/notify-stream.py
    sleep $1
done;
