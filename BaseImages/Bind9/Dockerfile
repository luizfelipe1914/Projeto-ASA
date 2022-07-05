FROM debian:stable
RUN apt update -y;apt full-upgrade -y; apt autoremove -y; apt clean
RUN apt install  rsyslog -y
RUN apt install -y bind9 bind9utils wget curl dnsutils vim nano bash
COPY config.sh .
COPY entrypoint.sh .
RUN chmod 755 /config.sh /entrypoint.sh
RUN /config.sh
EXPOSE 53/udp 53/tcp
VOLUME [ "/etc/bind" ]
CMD [ "/etc/init.d/named", "restart", ]
ENTRYPOINT [ "/entrypoint.sh" ]