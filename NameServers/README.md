1. Criar a rede no docker
   
   ```shell
   docker network create --subnet=172.25.0.0/24 CT-NETWORK
   ```

2. Criar as pastas para o mapeamento do volume
   
   ```sh
   mkdir -p ~/dns/etc
   mkdir -p ~/dns/logs
   ```

3. Buildar os arquivos Dockerfile contidos na pasta Nameservers
   
   ```shell
   # Para o master (Master/):
   docker build -t bind9:debian-stable-master .
   
   # Para o slave(Slave/):
   docker build -t bind9:debian-stable-slave .
   ```
   
   4. Executar os containers com o docker run:
      
      4.1. Para o master:
      
      ```shell
      docker run --net ctnetwork --ip 172.25.0.10 -itd -p 2222:2222 -p 53:53 dns-master:bind9
      ```
      
       4.2. Para o Slave:
      
      ```shell
      docker run --net ctnetwork --ip 172.25.0.11 -itd -p 2223:2222 -p 53:53 dns-slave:bind9
      ```

                
