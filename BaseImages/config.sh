#!/bin/bash

grep -v "^#" ssh | sed '/^$/d' > /etc/ssh/sshd_config
mkdir -p /root/.ssh
mv authorized_keys /root/.ssh/
touch /var/log/auth.log
touch /var/log/syslog.log
mkdir -p /var/log/bind
touch /var/log/bind/bind.log
chown bind:syslog -R /var/log/bind/
chmod -R 662 /var/log/bind/
chown bind:root -R /etc/bind
chmod -R 662 /etc/bind
chown syslog:syslog /var/log/auth.log
chattr +a /var/log/auth.log
chown syslog:syslog /var/log/syslog.log
chattr +a /var/log/syslog.log
rm -f config.sh ssh 