#!/usr/bin/python
# make code as python 3 compatible as possible
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import os
import re
import time

PARSER = argparse.ArgumentParser(description='Print out new irssi messages')
PARSER.add_argument('since_seconds', type=int,
                   help='How many seconds worth of messages to get')
PARSER.add_argument('--exclude-file', type=str, help='File containing regular expressions (python) of messages to not display')

def load_excludes(stream):
    result = []
    for line in stream:
        if line.startswith('#'):
            continue
        if not line.strip():
            continue
        result.append(re.compile(line.strip()))
    return result

args = PARSER.parse_args()

lines = []

if args.exclude_file:
    with open(args.exclude_file) as f:
        excludes = load_excludes(f)
else:
    excludes = []


message_start_time = time.time() - args.since_seconds
for direc, _, files in os.walk(os.path.join(os.environ['HOME'], 'irclogs')):
    for filename in files:
        path = os.path.join(direc, filename)
        with open(path) as stream:
            for line in stream:
                try:
                    timestamp, rest = line.split('k', 1)
                    timestruct = time.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
                    when = time.mktime(timestruct)

                    if any(e.search(line) for e in excludes):
                        continue
                    elif when < message_start_time:
                        continue
                    else:
                        lines.append(filename + " " + line)
                except ValueError:
                    continue

lines.sort()
for line in lines:
    print(line.strip())
