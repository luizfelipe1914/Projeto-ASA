#### DOCUMENTAÇÃO DA INFRAESTRUTURA PROVISIONADA

1. Para um maior controle, é criada uma rede interna no docker chamada **ctnetwork**. Essa rede possui a faixa de endereçamento IPv4 172.25.0.0/24.

2. A zona DNS escolhida foi a mg.asa.br

2. Os Nameservers dessa zona são, respectivamente, ns1: 172.25.0.10 e ns2: 172.25.0.11.

3. O servidor de correio eletrônico da zona é o 172.16.0.25.

##### INSTRUÇÕES

1. Efetue a clonagem do repositório

2. No arquivo config.json dentro de NameServers/Master/dns, configure os parâmetros com os endereços IPv4 da rede externa(rede dos laboratórios do IFRN ou a rede da máquina que está executando o Docker)

3. Após configurados os parâmetros, dentro do repositório, há uma script chamado build&run-infra.sh. Execute esse script passando como parâmetro a palavra build:

```sh
    bash build&run-infra.sh build
```

4. Para que os containers entrem em execução, execute, novamente o script. Porém, dessa vez passe o parâmetro run:

```sh
    bash build&run-infra.sh run
```

