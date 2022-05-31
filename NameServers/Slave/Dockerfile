FROM bind9:debian-stable
WORKDIR /etc/bind
COPY dns/ .
RUN mkdir -p /etc/bind/slave
RUN chown -R bind:bind /etc/bind
RUN chmod 772 -R /etc/bind
CMD [ "service", "named", "restart" ]