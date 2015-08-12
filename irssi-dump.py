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
def main():
    args = PARSER.parse_args()
    lines = []

    if args.exclude_file:
        with open(args.exclude_file) as f:
            excludes = load_excludes(f)
    else:
        excludes = []

    lines = sorted(get_new_lines(time.time() - args.since_seconds, excludes))
    for line in lines:
        print(line.strip())

def load_excludes(stream):
    result = []
    for line in stream:
        if line.startswith('#'):
            continue
        if not line.strip():
            continue
        result.append(re.compile(line.strip()))
    return result

def get_log_files(base_path):
    for direc, _, files in os.walk(base_path):
        for filename in files:
            path = os.path.join(direc, filename)
            yield filename, path

def get_log_time(line):
    try:
        timestamp, _ = line.split('k', 1)
        timestruct = time.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return None
    else:
        return time.mktime(timestruct)

def get_new_lines(message_start_time, excludes):
    for channel_name, path in get_log_files(os.path.join(os.environ['HOME'], 'irclogs')):
        with open(path) as stream:
            for line in stream:
                when = get_log_time(line)
                if when is None:
                    continue
                if any(e.search(line) for e in excludes):
                    continue
                elif when < message_start_time:
                    continue
                else:
                    yield channel_name + " " + line

if __name__ == '__main__':
	main()
