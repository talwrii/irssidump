#irssi-dump

## Description

Tool to periodically dump irc messages from irssi via libnotify.

## Purpose

Electronic communication is a complicated beast, one has to balance the value of 
of quick contactability with the overhead of interruption.

IRC is a particularly interesting case in that the point of using 
irc *and* e-mail is to allow two forms of communication, one 
slow and reliable, the other fast and unreliable.

"I'll just check this every 15 minutes or so", is a surprising difficult 
aspiration to acheive, and general tends to become: "I will check this 
once a day" or "I will continually check this". This tool tries to 
help you reach a happy medium.

## Usage

- Check this out.
- Install python-notify2.
- Enable irssi logs:

        /set autolog on
        /set log_timestamp %Y-%m%-%dT%H:%M:%Sk
        /save

- Run `irssi-dumpd.sh 900` to dump out irssi messages every 15 minutes.
