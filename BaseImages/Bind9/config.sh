touch /var/log/auth.log
touch /var/log/syslog
mkdir -p /var/log/bind
touch /var/log/bind/bind.log
chown bind:syslog /var/log/bind/
chown syslog:syslog /var/log/auth.log
chown syslog:syslog /var/log/syslog
rm -f config.sh  