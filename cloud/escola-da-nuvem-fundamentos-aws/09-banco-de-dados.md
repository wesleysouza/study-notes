# Banco de Dados

## 09.01 Amazon Relational Database Service (RDS)

O **Amazon Relational Database Service** (ou amazon RDS) é um **banco de dados relacional** qe destaca-se por sua escalabidade, automatização na aplicação de patches, provisionamento de hasrware e becape na Nuvem AWS.

Linguagem: SQL (Linguagem de Consulta Estruturada)

Mecanismos Disponíveis:
- Amazon Aurora;
- MySQL;
- MariaDB;
- PostgreSQL;
- Oracle;
- SQLServer.

### Multi-az:
- Todas as modificações no BD estão associadas a uma região e zona de disponibilidade. 
- É possível criar réplicas em outras zonas.

### Vantagens
- simples, segura e funcional;
- réplica em outra zona;
- redundância de dados;
- eliminar congelamento;
- minimizar picos;
- alta disponibilidade;

## 09.02 Amazon RDS (LAB)

## 09.03 Amazon DynamoDB

O Amazon DynamoDB é um **banco de dados não relacional (NoSQL)** de valor-chave e documento que oferece desempenho de milissegundos.

Características:
- Serveless: A AWS gerencia os recursos;
- Escalável: virtualmente ilimitado;
- Confiável: criptografia em repouso por padrão;
- Rápido: latência em microsegundos;

Estrutura:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-09-dynamo-db.png "")

### Dicas do exame:
- Tabela é uma coleção de itens;
- Cada item possuí um atributo;
- Chave primária é obrigatória e é utilizada para identificar um item na tabela;
- Chave secundária é opicional e fornece flexibilidade na consulta.
