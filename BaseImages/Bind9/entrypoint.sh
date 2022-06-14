#!/bin/bash
/etc/init.d/ssh start
/etc/init.d/named start
/bin/bash
tail -f /dev/null