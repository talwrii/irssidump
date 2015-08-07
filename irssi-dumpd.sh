if [ -z "$1" ];  then
    echo "Needs period" 2>&1
    exit 1
fi;

while true; do
    irssi-dump.py $1 | notify-stream
    sleep $1
done;
