#!/usr/bin/python
# make code as python 3 compatible as possible
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import os
import time

PARSER = argparse.ArgumentParser(description='Print out new irssi messages')
PARSER.add_argument('since_seconds', type=int,
                   help='How many seconds worth of messages to get')

args = PARSER.parse_args()

lines = []

for direc, _, files in os.walk(os.path.join(os.environ['HOME'], 'irclogs')):
    for filename in files:
        path = os.path.join(direc, filename)
        for line in open(path):
            try:
                timestamp, rest = line.split('k', 1)
                timestruct = time.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
                when = time.mktime(timestruct)
                if when > time.time() - args.since_seconds:
                    lines.append(filename + " " + line)
            except ValueError:
                continue

lines.sort()
for line in lines:
    print(line.strip())
