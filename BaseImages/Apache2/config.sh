#!/bin/sh

mv /resolv /etc/resolv.conf
mkdir -p /var/www/html/wiki.projetoasa
mkdir -p /var/www/html/projetoasa
ln -sv /etc/apache2/sites-available/projetoasa.conf /etc/apache2/sites-enabled/projetoasa
ln -sv /etc/apache2/sites-available/wiki.conf /etc/apache2/sites-enabled/wiki
#service apache2 reload