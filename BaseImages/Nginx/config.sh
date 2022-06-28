cat /ssh > /etc/ssh/sshd_config 
mkdir -p /root/.ssh
mv authorized_keys /root/.ssh/
touch /var/log/auth.log
touch /var/log/syslog
mkdir -p /var/log/nginx
chown www-data:syslog /var/log/named/
chown syslog:syslog /var/log/auth.log
chown syslog:syslog /var/log/syslog
rm -f config.sh ssh 