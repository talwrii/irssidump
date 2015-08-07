#!/usr/bin/python

import sys
import notify2 as notify

notify.init("Stream")
while True:
    line = sys.stdin.readline()
    if line == '':
        break
    notify.Notification("Stream", line).show()
