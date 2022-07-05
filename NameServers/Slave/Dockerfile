FROM bind9:debian-stable
COPY dns/named.conf.default-zones /etc/bind
COPY dns/named.conf.options /etc/bind
RUN mkdir -p /etc/bind/slave
RUN chown -R bind:bind /etc/bind
RUN chmod 772 -R /etc/bind
CMD [ "service", "named", "restart" ]