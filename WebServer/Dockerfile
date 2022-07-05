FROM nginx:debian-stable
RUN mkdir -p /var/www/html/wiki
RUN mkdir -p /var/www/html/asa
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 755 /var/www/html
WORKDIR /etc/nginx
COPY asa.conf ./sites-available
COPY wiki.conf ./sites-available
COPY asa.conf ./sites-enabled
COPY wiki.conf ./sites-enabled
RUN rm -f ./sites-enabled/default
WORKDIR /
CMD /etc/init.d/nginx restart
WORKDIR /var/www/html/asa
COPY asa/index.html .
WORKDIR /var/www/html/wiki
COPY wiki/index.html . 
WORKDIR /



