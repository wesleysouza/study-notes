# Métricas com o Prometheus

[Documentação do Prometheus](https://prometheus.io/docs/introduction/overview/)

## Anatomia de uma métrica

Digite isso na busca do Prometheus:

```
logback_events_total{application="app-forum-api", instance="app-forum-api:8080", job="app-forum-api", level="debug"}
```

Toda métrica possuí 3 componentes básicos:
- **Matric name**: nome da métrica
- **Labels (Rótulos)**: Identificam a série temporal que você quer consultar.
- **Sample**: Resultado da consulta de uma determinada métrica.

Tipos de dados que uma métrica pode possuir no Prometheus:
- Instant vector: vetor instatâneo;
- Range vector: vetor de uma série temporável;
- Dado tipo escalar: um ponto flutuante;
- String: cadeia de caracteres (não utilizado).

Quando você digita logback_events_total na busca é retornado um vetor, onde cada indice retorna uma série temporal. A distinção entre os vetores é possível graças as **labels**.

### Trabalhando com Range vector:

Para obter o range vector digite a string abaixo na busca do Prometheus:

```
logback_events_total[1m]
```

Saída (No formato Unix Timestamp):

```bash
0 @1655055316.987
0 @1655055321.988
```

Para transformar esse dado em um formáto legível digite o comando abaixo no seu terminal:

```bash
date -d @1655055321.988
```

Tratando mais de um valor:

```
array=(@1655055321.988 @1655055336.988 @1655055351.984 @1655055366.988)
for i in "$array[@]"; do date -d $i; done
```

No caso, temos um range de tempo dentro de uma série temporal.

Outro exemplo, vendo as métricas dos últimos 30s dos últimos 30 segundos:

```bash
logback_events_total[5m:30s]
```

Obs.: Gráficos são possíveis com instante vector e dados escalares.


## Tipos de Métricas

[Documentação tipos de métricas](https://prometheus.io/docs/concepts/metric_types/#metric-types)

O Prometheus trabalha com 4 tipos de métricas:
- Counter;
- Gauge;
- Histogram;
- Summary.

### 1 Counter 

Métrica crescente e sempre incrementada, comulativa. 

- Desvantagem: se a aplicação for reiniciada ela zera, mas é posśivel obter os valores antigos observando outra série temporal.
- Não adequada para valores que vão variar.

### 2 Gauge

Boa para avaliar consume de CPU e memória, é ótima para valores variáveis.

Métrica tipo Gauge que avalia o uso de CPU:

```bash
process_cpu_usage
```

### 3 Histogram

Ele traz observações relacionadas a duração e tamanho de resposta. Ele tem uma configuração de alocação de séries temporais em buckets, esse buckets eles vão responder a umas regras que a gente vai definir.

Existe uma métrica de SLA definida em application properties da aplicação.

Aplicações: Tempo de resposta da API.

### 4 Summary

É mais utilizado para verificar o tamanho de uma requisição e o tamanho da resposta. Além disso, é posśivel ter o somatório e contagem total de venetos captados na métrica.

## Seletores, Modificadores e Funções

Vamos iniciar a discussão com a métrica abaixo:

```bash
http_server_requests_seconds_count{application="app-forum-api", method=~"GET|POST", status=~"2..|3..", uri!="/actuator/prometheus"}
```

Observações:
- 2.. (O "." é um coringa);
- =~ (permite adicionar o ou "|" prapegar o GET e POST)

Melhorando:

```bash
http_server_requests_seconds_count{application="app-forum-api", method=~"GET|POST", status!~"2..|3..", uri!="/actuator/prometheus"}
```

Observações:
- !~ Negação;

### Aglutinação de resultados

Para aglutinar utilizando o operador offset:

```bash
http_server_requests_seconds_count{application="app-forum-api", method=~"GET|POST", status!~"2..|3..", uri!="/actuator/prometheus"} offset 1m
```

### Funções

Vamos descobrir a taxa de crescimento de uma métrica:

```bash
http_server_requests_seconds_count{application="app-forum-api", uri!="/actuator/prometheus"}[1m]
```

Saída, um rage vector, daí eu não tenho uma taxa de crescimento. Para obter essa taxa utilizamos a função increase:

```bash
increase(http_server_requests_seconds_count{application="app-forum-api", uri!="/actuator/prometheus"}[1m])
```

Saber o número de requisições com a função **sum**:

```bash
sum(increase(http_server_requests_seconds_count{application="app-forum-api", uri!="/actuator/prometheus"}[1m]))
```

Vamos agora saber quantas requisições por segundo chegaram nos últimos 5 segundos:

```bash
irate(http_server_requests_seconds_count{application="app-forum-api", uri!="/actuator/prometheus"}[5m])
```