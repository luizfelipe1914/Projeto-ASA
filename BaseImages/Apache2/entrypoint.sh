#!/bin/bash
cat /resolv.conf > /etc/resolv.conf
service apache2 start
/bin/bash