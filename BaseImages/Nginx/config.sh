touch /var/log/auth.log
touch /var/log/syslog
mkdir -p /var/log/nginx
chown www-data:syslog /var/log/nginx/
chown syslog:syslog /var/log/auth.log
chown syslog:syslog /var/log/syslog
rm -f config.sh 