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
    python -u $here/irssi-dump.py --exclude-file $exclude_file $1 | python $here/notify-stream.py
    sleep $1
done;
