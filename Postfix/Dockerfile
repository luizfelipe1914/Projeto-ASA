FROM debian:stable
RUN apt update -y \
    apt full-upgrade -y \ 
    apt autoremove -y \
    apt clean \ 
    apt install  rsyslog -y \
    apt install -y  bind9utils wget curl dnsutils vim nano bash \
    apt install postfix sendemail iproute2 iputils-ping -y
COPY config.sh .
COPY entrypoint.sh .
RUN chmod +x config.sh entrypoint.sh
EXPOSE 25/tcp 587/tcp
VOLUME [ "/var" ]
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "serice", "postfix", "restart" ]
