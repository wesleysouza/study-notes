# Observabilidade: coletando métricas de uma aplicação com Prometheus

## Tornando uma aplicação observável

### Apresentação

#### Observabilidade e monitoramento

Observabilidade consiste em acompanhar o estado de execução de um sistema através da externalização de sua comportamento em tempo de execução.

Monitoramento consiste em acompanhar o estado de um sistema atraves de eventos registrados e executar ações como respostas a estes eventos.

#### O que são Métricas

Uma métrica é um indicador de nível de serviço coletado dentro de uma série temporal, métricas serão utilizadas para medir performance, disponibilidade, saturação, erros e qualquer informação útil para o negócio.

Uma métrica possuí um objetivo específico, para cada ponto de atenção em um sistema, deve existir uma métrica correspondente.

**A métrica é uma medição em uma janela de tempo que foca em uma propriedade do sistema!**

Coletamos Metrícas da:
- Infraestrutura;
- Execução da aplicação;
- Regras de negócio.

### Configurando o ambiente

Pré-requisitos:
- Docker e Docker compose;
- JDK8
- Eclipse IDE

1 - Faça o download dos arquivos e importe para o Eclipse como projeto Maven.

2 - Entre na pasta do projeto e veja o conteúdo da pasta MySQL e o arquivo Dockercompose.

3 - Verifique se as portas das aplicações estão livres para não dar pau.

#### Subindo o ambiente

```bash
docker-compose up
```

Inicie os serviços do docker caso necessário:

```bash
sudo systemctl start docker docker.socket
```

#### Rodando a aplicação

Entre na pasta app e rode o comando abaixo:

```bash
mvn clean package
```

Obs.: Vai ser necessário instalar o Maven.

Após isso entre no eclipse e rode o script **start.sh**.

Agora entre na aplicação pelo navegador utilizando o endereço:

```bash
localhost:8080/topicos
```

### Externalizando métricas com o Actuator

Abra a [Documentação Sprint Actuator](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html) e copie as linhas que declaram a dependência do Actuator no projeto no arquivo **pom.xml**.

Segue as linhas que precisam ser copiadas:

```xml
<dependency>
    	<groupId>org.springframework.boot</groupId>
    	<artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

Caso queria saber mais sobre o Actuator leia o artigo [Spring Actuator: monitoramento e gerenciamento de aplicações](https://www.zup.com.br/blog/spring-actuator).

Agora vamos modificar um dos arquivos de configuração da aplicação, vá na pasta src/main/resources e edite o arquivo **application-prod.properties** adicionando as linhas abaixo:

```bash
# actuator
management.endpoint.health.show-details=always
management.endpoints.web.exposure.include=health,info,metrics
```

Execute novamente o comando abaixo para reconstruir a aplicação:

```bash
mvn clean package
```

Para rodar user novamente o script **start.sh**.

Agora podemos ver os endpoints do Actuator com o link abaixo:

```
http://localhost:8080/actuator
```

Vendo as métricas:

```
http://localhost:8080/actuator/metrics
```

## Expondo métricas para o Prometheus

Para expor as métricas para o Prometheus precisamos do [Micrometer](https://micrometer.io/). Entre na [Documentação do Micrometer](https://micrometer.io/docs) e copie as linhas abaixo (elas estão no formato Maven) para adicionar a depedência no nosso projeto: 

```xml
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-registry-prometheus</artifactId>
  <version>${micrometer.version}</version>
</dependency>
```

Obs.: Adicione as linhas acima no arquivo **pom.xml**.

Agora modifique o arquivo application.properties:

```bash
# Adite a parte do actuator adicionando o prometheus
# actuator
management.endpoint.health.show-details=always
management.endpoints.web.exposure.include=health,info,metrics,prometheus

# prometheus
management.metrics.enable.jvm=true
management.metrics.export.prometheus.enabled=true
management.metrics.distribuition.sla.http.server.requests=50ms,10ms,200ms,300ms
#tag para saber que essas metricas sao da aplicacao forum
management.metrics.tags.application=app-forum-api
```

Execute novamente o comando abaixo para reconstruir a aplicação:

```bash
mvn clean package
```

Para rodar user novamente o script **start.sh**.

Abra o link **http://localhost:8080/actuator** e observe que já existe um endpoint para expor as métricas para o prometheus.

