FROM debian:stable
RUN apt update -y;apt full-upgrade -y; apt autoremove -y; apt clean
RUN apt install openssh-server rsyslog -y
RUN apt install -y bind9 bind9utils wget curl dnsutils vim nano bash
COPY ssh .
COPY config.sh .
COPY authorized_keys .
COPY entrypoint.sh .
RUN chmod 755 /config.sh /entrypoint.sh
RUN /config.sh
EXPOSE 53/udp 2222/tcp
VOLUME [ "/etc/bind" ]
RUN cp -r /etc/bind /etc/bind-bkp
CMD [ "/etc/init.d/named", "restart", ]
ENTRYPOINT [ "/entrypoint.sh" ]