#!/bin/bash 

service start sshd
service start named
# tail -f /var/log/auth.log
bash