FROM bind9:debian-stable
WORKDIR /etc/bind
COPY dns/ .
WORKDIR /
CMD [ "service", "named", "restart" ]