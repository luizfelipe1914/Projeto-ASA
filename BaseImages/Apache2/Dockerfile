FROM debian:stable
RUN apt update;apt full-upgrade -y
RUN apt install -y apache2 vim nano wget curl 
COPY entrypoint.sh .
COPY resolv .
RUN chmod +x /entrypoint.sh 
EXPOSE 80 443 
CMD [ "service", "apache2", "start" ]
ENTRYPOINT [ "bash", "/entrypoint.sh" ]