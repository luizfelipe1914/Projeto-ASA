FROM bind9:debian-stable
WORKDIR /etc/bind
COPY dns/ .
CMD [ "service", "named", "restart" ]