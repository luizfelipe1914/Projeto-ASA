#!/bin/bash

mv /resolv /etc/resolv.conf
mkdir -p /var/www/html/wiki.projetoasa
mkdir -p /var/www/html/projetoasa
a2ensite /etc/apache2/sites-available/projetoasa.ifrn.local.conf
a2ensite wiki.projetoasa.ifrn.local