#!/bin/sh 

rm -rf /etc/bind-bkp
/etc/init.d/ssh start
/etc/init.d/named start
bash