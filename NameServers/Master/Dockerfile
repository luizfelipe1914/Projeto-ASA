FROM bind9
WORKDIR /etc/bind
COPY dns/ .
WORKDIR /
CMD [ "service", "named", "restart" ]