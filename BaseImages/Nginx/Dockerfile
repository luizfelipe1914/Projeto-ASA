FROM debian:stable
RUN apt update -y;apt full-upgrade -y; apt autoremove -y; apt clean
RUN apt install rsyslog -y
RUN apt install -y nginx wget curl dnsutils vim nano bash
COPY entrypoint.sh . 
COPY config.sh .
RUN chmod +x config.sh entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "service", "nginx", "restart"]