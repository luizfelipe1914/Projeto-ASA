FROM debian:stable
RUN apt update;apt full-upgrade -y
RUN apt install -y apache2 vim nano wget curl 
COPY entrypoint.sh .
COPY resolv .
WORKDIR /etc/apache2/sites-available
COPY projetoasa.ifrn.local.conf . 
COPY wiki.projetoasa.ifrn.local .
WORKDIR /
COPY config.sh .
RUN CHMOD +x config.sh
RUN /config.sh
RUN chmod +x /entrypoint.sh 
EXPOSE 80 443 
CMD [ "service", "apache2", "start" ]
ENTRYPOINT [ "bash", "/entrypoint.sh" ]