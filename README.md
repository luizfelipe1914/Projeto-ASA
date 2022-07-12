# Projeto ASA

Repositório destinado ao Projeto da disciplina de Administração de Sistemas Abertos (ASA). Toda infraestrutura desnvolvida na disciplina será provisionada como código. Tecnologias utilizadas:
  * Docker
  * Docker Compose (num futuro bem próximo...)
  * Shell Script(Bash)
  * Python
  * Ansible(num futuro bem próximo...)
  * Kubernetes ou Swarm (em análise...)
  
 Componentes da equipe:
  * Luiz Felipe e Silva Machado - 20201014050008
  * Larissa Batista do Nascimento - 20182014050036
  * Mizael Arthur da Silva Coelho - 20201014050002

O projeto consiste em provisionar uma infraestrutura containerizada composta por:

  * DNS Servers - Bind 9(Master e Slave)
  * Servidores HTTP - Nginx e/ou Apache2 (Atuando como Proxy Reverso e Hospedando alguma aplicação como por exemplo DokuWiki, GLPI, WordPress ou Joomla)
  * Stack de monitoramento - Prometheus + Grafana 
  * Serviço de gerência de Logs (Rsyslog + Graylog)
  * Serviço de Banco de Dados(PostgreSQL e/ou MySQL)
  * Ferramentas de observabilidade (Elasticsearch + Kibana)
  * Serviço de Web Chat (Rocket Chat)
  
  Os procedimentos operacionais encontram-se no arquivo [DOCS](DOCS.md).
  
  #### Serviços já provisionados:
  
  * [DNS](NameServers)
  * [HTTP(S) - Nginx](WebServer)
  
