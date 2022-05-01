# Computação

## 05.01 Amazon (Elastic Compute Cloud) EC2

O **Amazon EC2** é um serviço web que disponibiliza uma **capacidade computacional** segura, representado por uma **instância redimensionável** na Nuvem.

Características:
- Modelo IaaS;
- Alugar máquinas virtuais (EC2);
- Armazenar dados em volumes virtuais - Amazon Elastic Block Storage (EBS);
- Distribuir a carga de trabalho - Elastic Load Balancing (ELB);
- Escalar serviço de acordo com a demanda - Amazon EC2 Auto Scaling (ASG);

### Conexão e acesso

Operador -> Autenticação e Autorização -> EC2;

### Tipos de instância

| Família     | Otimizado     | Ideal Para |
|-------------|---------------|------------|
|A, T, M, Mac | Uso Geral     | Servidores de web, homologação e repositórios de código.
| C           | Computação    | Modelagem científica, servidores de jogos, servidores de anúncios e ML.
| R, X, Z     | Memória       | Cargas de trabalho que processam grandes conjuntos de dados na memória.
| P, Inf, G, F | Processamento | Executar funções, como cálculos de números e ponto flutuante, processamento de gráficos.
| I, D, H      | Armazenamento | Cargas de trabalho que requerem uso intensivo de disco (IOPS).

### Entendendo a instância

Significado da nomeclatura da instância **T2.2xlarge**:
- Tipo: **T**2.2xlarge;
- Família: **T2**.2xlarge;
- Geração: T**2**.2xlarge;
- Tamanho: T2.**2xlarge**.

### Dicas do exame:
- O Amazon EC2 é um serviço web que disponibiliza uma **capacidade computacional** segura, representando por uma **instância redimensionável** na nuvem;
- Modelo computacional IaaS;
- Ambiente operacional Windows, macOS e Linux;
- Cobrança por hora ou segundo (mínimo de 60 segundos).

## 05.02 Criar uma instância EC2 LAB

É possível criar as proprías AMIs (Packer!).

No campo user data é possível rodar um comando na inicialização do sistema, por exemplo:

```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start http
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)<\h1>" > /var/www/html/index.html
```

Adicione as Tags, por exemplo, departamento:tecnologia.

### Configure o security group

Adicione regras para o ssh e HTTP.

### Crie a key pair para acesso

Faça o download e guarde em um local seguro.

Obs.: O endereço IP privado é o IP no ambiente AWS.

Obs.: Todas as vezes que voce parar uma instância e subir novamente o IP público da instância vai mudar.

### Atividade

- Escolha a **região** mais próxima de você;
- No **Amazon EC2** inicie uma instância **t2.micro**;
- Utilize o **script** de inicialização;
- Guarde o arquivo ".pem" (key pair).

## 05.03 Acessar uma instância EC2 via SSH

Acesso no windows:

```bash
ssh -i minha_cahe.pem ec2-user@ip
```

## 05.04 Amazon EC2 Lauch Types
 
Tipos de inicialização:
- Sob Demanda;
- Instâncias Spot;
- Instâncias reservada;
- Host e instância dedicada;

### Sob Demanda

- **Alto custo** se usado no longo **prazo**;
- **Cobrança** o que usar (por **hora** OU por **segundo**);
- **Sem compromisso de uso** (anos);
- Sem pagamento adiantado;
- Pode aumentar o diminuir a capacidade computacional.

**ÚTIL**: Cargas de trabalho de curto prazo, validar hipóteses, com pico de utilização previsível, testar e experimentar um ambiente.

### Instância Reservada

- **Até 75% de desconto** comparado as instâncias por demanda.
- Aplicações que exigem capacidade reservada;
- **Comprometimento de uso** da instância por um período de 01 ou 03 anos;
- Possuí pagamento adiantado.

**ÚTIL**: Ambinete de produção que foi testado e não será modificado, aplicações que precisar ser **estado contante: excelente para banco de dados**.

### Host Dedicado

- Hardware dedicado;
- Servidor físico EC2 exclusivo para você;
- Cumprir requisitos de conformidade;
- **Visibildiade de soquetes, núcleos, IDs de host;**
- **Comprometimento** por um período de 03 anos;
- Pode ser comprado sob demanda de horas;
- Se optar por reserva, até **70% de desconto** em comparação com instâncias por demanda.

**ÚTIL**: **Vincular licenças** de software, como Windows Server, SQL Server e SUSE Linux Enterprise Server.

Obs.: A visibildiade de soquetes, núcleos e IDs de host é necessária quando precisamos utililizar licenças de softwares proprietários na nuvem.

### Instância Dedicada

- Hardware dedicado;
- Pode compartilhar o hardware com outras instâncias, na mesma conta;
- Não tem controle sobre o posicionamento da instância (vocÊ só pode movimentar o hardware se interromper e reiniciar);
- **Comprometimento** por um período e **03 anos**.


### Instâncias SPOT

- Até 90% de desconto comparado a instância sob demanda;
- São terminadas quando o preço do spot, é maior do que o preço que você estabeleceu para pagar;
- **Memorize como leilão de instâncias**;
- Terminate = (preço da spot AWS > seu preço);
- Não utilize para **trabalhor críticos** e **banco de dados**;

**ÚTIL**: Quando você tem **urgência de grande capacidade computacional**, workloads que podem parar e serem iniciados novamente, trabalhos em lote, análise de dados, processamento de imagens.

### Resumindo

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-05-ec2-lauch-types.png "")

## 05.05 AWS Auto Scaling Group

Para que precisamos?
- **Escalabilidade** automatizada;
- **Scale out** (add instâncias);
- **Scale In** (remover instâncias);

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-05-auto-scaling-group.png "")

Obs.: Esse serviço tem um heath check que verifica se as instâncias estão rodando de maneira adequada, caso contrário essa instância é interrompida e uma nova é provisionada caso necessário.

É possível combinar esse serviço com o **Elastic Load Balancing** que vai distribuir as requisições entre as instâncias disponíveis.

### Dicas do exame

- Definir uma quantidade **mínima**, **desejável** e **máxima** de instâncias;
- Realiza **verificações** (health check), finaliza as instâncias **não saudáveis** (unhealthy) e inicia novas;
- Scale out (**aumentar** com as demandas) e **Scale in** (diminuir quando a demanda reduzir);
- O Auto Scaling Group é **gratuíto**, você paga apenas pelas instâncias que estão sendo executadas;

## 05.06 AWS Auto Scaling Group 

- EC2 Lauch Templates;
- Pare remover tudo é necessário primeiro deletar o Auto Scaling Group Criado.

## 05.07 AWS ELastic Beanstalk

Arquitetura de 3 camadas:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-05-arquitetura-3-camadas.png "")

Essa arquitetura entrega: Alta disponibilidade, segura, resiliente e que cresce de acordo com a demanda.

O **AWS Elastic Beanstalk** é um **serviço gerenciado** para os desenvolvedores realizarem uma fácil utilização de **implantação** e **escalabilidade** de aplicações e serviços web.

Passos:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-05-elastic-beanstalk.png "")

### Dicas do exame:

- Serviço **gerenciado** e gratuíto;
- Plataforma como Serviço (PaaS);
- Upload de código arquivo <512Mb ou Upload via URL Bucket S3;
- Balancemento de carga (load balancer);
- Alta disponibilidade (multi-az);
- Auto Scaling Group (ASG).
- Plataformas disponíveis:
    - Node, Python, Ruby, Golang, .NET, PHP, Docker, Java, Tomcat e Glassfish.

## 05.08 AWS ELastic Beanstalk (LAB)

Acessa o serviço pelo nome: AWS Elastic Beanstalk.

## 05.09 AWS Lambda

O **AWS Lambda** permite que você **execute códigos** **sem provisionar** ou gerenciar servidores, pagando apenas **pelo número de solicitações** e **pelo tempo de computação** que você utilizar.

Serverless: Possibilita a execução do código sem exigir o provisionamento de servidores, basta escrever o código e rodar no Lambda. Ele também é executável e roda em paralelo.

Possuí baixo custo e suporta múltiplas linguagens como:
- Java, Go, Node, C#, Python e etc.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-05-lambda.png "")

### Dicas do exame:
- Serviço serveless e gerenciado pela AWS;
- **AWS Lambda** **dimensiona** suas aplicações;
- Você pode **otimizar** o **tempo de execução** e o **tamanho da memória**;
- **Cobrança** por **número de solicitações** de suas funções e pela **duração por cada milisegundo** que leva para que seu código seja executado.


