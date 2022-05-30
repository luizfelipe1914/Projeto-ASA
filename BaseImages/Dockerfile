FROM debian:stable
RUN apt update -y;apt full-upgrade -y; apt autoremove -y; apt clean
RUN apt install openssh-server rsyslog -y
RUN apt install -y bind9 bind9utils
COPY ssh .
COPY config.sh .
COPY authorized_keys .
COPY entrypoint.sh .
RUN chmod 755 config.sh entrypoint.sh
RUN /config.sh
EXPOSE 53/udp 2222/tcp
VOLUME [ "/etc/bind" ]
ENTRYPOINT [ "/entrypoint.sh" ]