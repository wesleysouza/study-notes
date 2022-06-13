# Primeiros passos com Prometheus

## Subindo a stack com API e Prometheus

Baixe os arquivos necesários e suba com o comando abaixo:

```
docker-compose up -d
```

Agora podemos acessar tudo sem a porta graças ao proxy:

```
localhost/topicos
localhost/metrics
```

As configurações do proxy estão disponíveis no diretório do nginx no arquivo nginx.conf.

Obs.: O Proxy só serve para acessar a aplicação e os endpoints da aplicação de forma externa.

Para acessar o Prometheus use o link **localhost:9090**.

Obs.: 

## Conhecendo as configurações do Prometheus

Acesse o link **http://localhost:9090**.

Obs.: O diretório prometheus_data ta com permissão 777, porque ele está no path do linux.

Configurações importantes:
- **scrape _interval**: pra qualquer configuração de scrape ele tem um tempo para realizar uma nova consulta.
- **scrape**: tempo entre uma consulta e outra em um endpoint de métricas.

## Subindo o cliente para consumo da API

Precisamos criar um consumidor da API. Vamos rodar um container que vai consumir a nossa aplicação e assim alimentando as métricas.

Entre no diretório **client** do projeto e de uma olhada no arquivo Dockerfile e no script com o nome **client.sh**.

