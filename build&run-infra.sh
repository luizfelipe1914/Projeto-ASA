#!/bin/bash

## Buildando as imagens personalizadas...
function buildImages(){
    echo -e "---------------------------------------------------"
    echo -e "Construindo a imagem base do DNS Server..."
    docker build -t bind9:debian-stable ./BaseImages/Bind9

    echo -e "---------------------------------------------------"
    echo -e "Construindo a imagem do DNS Master..."
    python3 ./NameServers/Master/dns/configuration_tool.py
    docker build -t dns-master:bind9 ./NameServers/Master/

    echo -e "---------------------------------------------------"
    echo -e "Construindo a imagem do DNS Slave..."
    docker build -t dns-slave:bind9 ./NameServers/Slave/
    
    echo -e "---------------------------------------------------"
    echo -e "Construindo a imagem base do Web Server Nginx"
    docker build -t nginx:debian-stable ./BaseImages/Nginx/

    echo -e "---------------------------------------------------"
    echo -e "Construindo a imagem base do WebServer"
    docker build -t webserver:nginx ./WebServer/

    echo -e "---------------------------------------------------"
    echo -e "Obra finalizada!"
}
function runContainers(){
    if [ $(docker network ls | awk '{ print $2 }' | grep ctnetwork) -ne "ctnetwork" ]; then
        docker network create --subnet=172.25.0.0/24 ctnetwork # Criando a rede interna 172.25.0.0/24
    fi
    docker run --name named-master --net ctnetwork --ip 172.25.0.10 --dns 172.25.0.10 --dns 172.25.0.11 -itd -p 0.0.0.0:31053:53/tcp -p 0.0.0.0:31053:53/udp dns-master:bind9
    docker run --name named-slave --net ctnetwork --ip 172.25.0.11 --dns 172.25.0.10 --dns 172.25.0.11 -itd  -p 0.0.0.0:31153:53/udp -p 0.0.0.0:31153:53/tcp dns-slave:bind9
    docker run --name web-01 --net ctnetwork --ip 172.25.0.20 --dns 172.25.0.10 --dns 172.25.0.11 -itd  -p 0.0.0.0:8080:80/tcp webserver:nginx
}

case $1 in 
    "build")
        buildImages
        ;;
    "run")
        runContainers
        ;;
esac