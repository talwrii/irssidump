#!/bin/bash
here=$(dirname ${BASH_SOURCE[0]})
if [ -z "$1" ];  then
    echo "Needs period" 2>&1
    exit 1
fi;

exclude_file=~/.irssi-dumpd/excludes
mkdir -p ~/.irssi-dumpd
[ ! -f "$exclude_file" ] && touch $exclude_file

while true; do
    $here/irssi-dump.py $1 | grep -vEf $exclude_file  | python $here/notify-stream.py
    sleep $1
done;
