FROM debian:stable
RUN apt update;apt full-upgrade -y
RUN apt install -y apache2 vim nano wget curl 
COPY entrypoint.sh .
COPY resolv .
WORKDIR /etc/apache2/sites-available
COPY projetoasa.conf . 
COPY wiki.conf .
WORKDIR /
COPY config.sh .
RUN chmod +x config.sh
RUN bash config.sh
RUN chmod +x /entrypoint.sh 
EXPOSE 80 443 
CMD [ "service", "apache2", "start" ]
ENTRYPOINT [ "bash", "/entrypoint.sh" ]