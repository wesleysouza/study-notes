# Monitoria, Governança e Comliance

## 08.01 Amazon CloudWatch

O **Amazon CloudWatch** é um serviço de monitoramento de desempenho dos recursos e dos aplicativos que você executa no seu ambiente.

Habilitado por padrão, registra os eventos dos últimos 90 dias.

### Funcionamento:

Coletar -> Monitoar -> Atuar -> analisar

#### Coletar

- Coleta de Métricas e Logs;
- Recursos e Serviços na Nuvem e on-premises;
- Métrica padrão 5 minutos;
- Métrica detalhada ($$$) por minuto;

Exemplos de métrics:
- Amazon EC2: Utilização de CPU, Status check, Rede (não RAM);
- EBS Volume: Leitura e gravação do disco;
- S3 Bucket: tamanho do bucket S3, número de objetos;
- Lambda: Tempo de execução e duração;

#### Monitorar

- Visualizar as aplicações e sua infraestrutura em um único local;
- Acessar um Dashboard automático;
- Criar o seu Dashboard (painel) personalizado, com os serviços e métricas que deseja acompanhar;
- Configurar alarmes viasuais do ambiente;

#### Atuar

- Criar alarmes para atuar como gatilho, baseado nas métricas de uso e desempenho;
- Opções do gatilho: amostra, %, valor máximo, mínimo, e etc.

- ALARM ACTION:
    - Auto Scaling Group: aumentar ou diminuir o número de instâncias no Amazon EC2;
    - Amazon EC2: Para terminar, reiniciar ou recuprar uma instância;
    - Amzon SNS: Enviar notificações para um SNS Topic, para que os assinantes recebam um e-mail.

#### Analisar

- Analisar em tempo real o seu ambiente, e segundos ou posterior com até 15 meses de armazenamento dos logs.
- Análise de alarmes possui três estados:
    - OK - tudo bem;
    - INSUFFICIENTE_DATA - coletando dados;
    - ALARM - algo ruim aconteceu ou para indicar que a sua métrica foi atingida.

## 08.02 AWS CloudTrail

O AWS CloudTrail é um serviço qu possibilita **governança**, **conformidade**, **auditoria** operacional e auditoria de riscos em sua conta AWS.

Quem acessou, quem mudou e etc.

### Diferença com o Amazon CloudWatch

Analogia da Corrida: No CludWatch coisas relaiconadas ao desempenho são medidas como calorias, tempo e distância percorrida. Por sua vez, no CloudTrail será registrado o caminho ou rota percorrida. 

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-08-cloudtrail.png)

Em suma, o CloudTrail Registra todas as modificações no ambientes possibilitando a auditoria.

## 08.03 AWS Config

O AWS Config é um serviço que permite acessar, auditar e avaliar as configurações dos recursos na AWS.

Funcionamento:
- Restrito a uma região;
- Configuração por meio de checklists:
    - Há acesso irrestrito via SSH nos meus grupos de segurança?
    - Meus Buckets S3 estão com acesso aberto ao público?
    - Como minha configuração do ALB mudou ao longo do tempo?

É possível monitorar e acompanhar uma linha do tempo das alterações realizadas. 

### Dicas do exame:
- AWS Config é **Regional**;
- Auxilia na **auditoria** das alterações dos recursos para compliance;
- Mantém histórico das alterações e armazena em um Bucket S3 para posterior análise;
- Notificaçõe de alterações são enviadas com o Amazon SNS e disponibilizadas no Dashboard (painel) do AWS Config.
- Não faz parte do free-tier.

## 08.04 AWS Organizations

Organizando o billing.

AWS Organizations permite que você **gerencia** e **controle** seu ambiente de maneira **centralizada**.

- Serviço global que gerencia múltiplas contas!
- Único faturamento e agregação de custos.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-08-aws-organizations.png "")

### Dicas do exame
- AWS Organizations é um serviço Global;
- Permite gerenciar múltiplas contas AWS;
- Uma conta principal (Master Account);
- API disponível para criação de contas;
- Restrição das contas usando SCP (Service Control Police).

## 08.05 AWS Well-Architected

Seguir as melhores práticas disponibilizadas pelos engenheiros da AWS.

### Princípios gerais:
- Pare de ficar adivinhando a sua capacidade;
- Teste o seu produto em escala de produção;
- Automatize a sua arquitetura para sua experimentação ser fácil;
- Permita a evolução da arquitetura;
- Construa sua arquitetura baseada em dados;
- Melhore através de gamedays;
    - Caos engeneering.
    - Simular eventos que podem acontecer no mundo real.

### Princípios do Design
- Escalabilidade: vertical & horizontal;
- Recursos descartáveis: nada é para sempre;
- Automação: serverless, IaaS, auto scaling;
- Loose couple: faslhas não podem cascatear & não ao monolito;
- Serviços não Servidores: será que não tem um serviço pra isso?

### Cinco Pilares Well-Architected
- **Operational Excellence**: executar e monitorar para entregar valor;
- **Security**: proteger informações e sistemas;
- **Reliability**: garantir que uma carga de trabalho execute sua função pretendida corretamente e de modo consistente;
- **Prformance Efficiency**: usos eficiente de recursos e computação;
- **Cost Optimization**: compreenção e controle de onde o dinheiro está sendo gasto, ajustando os recursos e serviços.

Obs.: É fundamental manter equilíbrio entre os cinco pilares.

## 08.06 AWS Artifact - Acordos e Relatórios de conformidade

### Artefatos de Compliance

- Os documntos são chamados de artefato;
- Os relatórios de segurança e compliance são ISO, PCI e SOC;
- Os acrodos de uso de serviços (agreements), são BAA e HIPAA;
- São utilizado em auditorias internas e conformidade;

## 08.07 AWS Artifact (LAB)

Armazenar e disponibilizaros  acordos de conformidade e relatórios de segurança e compliance.

Atividade:
- Acessar o AWS Artifact;
- Acessar os relatórios de segurança e conformidade;
- Baixar um relatório de segurança.

## 08.08 AWS Trusted Advisor

Ferramenta que fornece orientações em tempo real para a sua conta nas seguintes áreas:
- Otimização de custo;
- Desempenho;
- Segurança;
- Tolerância a falhas;
- Limites de serviço;

Cada categoria avalia o sem ambiente e sugere melhorias.

Os únicos planos que possuem todas as categorias são os businesse e enterprise.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-08-trusted-advisor.png "")

## 08.09 AWS Trusted Advisor (LAB)

- Serviço Global;
