# Redes e CDN

## Amazon VPC

O Amazon VPC é uma **sessão isolada logicamente** na nuvem AWS, que permite customizar uma rede virtual e executar recursos, em um ambiente com controle total.

Benefícios;
- Mesmo conceito on-premises;
- Total controle na configuração;
- Oferece camadas de segurança (SG & NACLs);
- Conectividade com outros serviços.

Serviço de fundação que se integra com os demais serviços.

Características:
- Região e Zonas de Disponibilidade: Foi construído para rodar em uma região e pode ser dividido em mais de uma zona de disponibilidade;
- Sub-redes [Pública e Privada];
- Tabela de roteamento;
- Internet Gateway [sub-rede pública]: portão para que as instâncias que estão na sub-rede pública consigam chegar na internet;
- Nat Gateway [sub-rede privada]: permite que sua subrede privada acesse a internet de forma segura;
- Security Group [SG] e Network Access List [NACLs] são firewals virtuais.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-vpc.png "")

Dica: Leia o FAQ da VPC!

## Amazon Route 53

O **Amazon Route 53** é um serviço que atua como DNS (Domain Name System), que **encaminha** as **solicitações** dos usuários, para aplicativos de Internet.

O nome Route53 é uma referência a **porta 53**.

Características:
- Gerenciamento de DNS: Um conjunto de regras e registros que ajudam o clisnte a chegar ao destino através de uma URL amigável.
- Gerenciamento de tráfégo com políticas de roteamento.
- Monitoramento e Disponibilidade (health check);
- Registro de Domínios.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-route-53-caracteristicas.png "")

### Gerenciamento de tráfégo com políticas de roteamento

Simples:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-route-53-simples.png "")

Ponderado:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-route-53-ponderado.png "")

Latência:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-route-53-latencia.png "")

Failover:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-route-53-failover.png "")

Geolocalização:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-route-53-geolocalizacao.png "")

Valores Múltiplos:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-route-53-valores-multiplos.png "")

## Amazon Route 53 LAB

- Acessar o Amazon Route 53;
- Conhecer as Políticas de Tráfego;
- Saber como registrar um domínio;

Geoproximity: recursos;

## Amazon CloudFront

O amazon Cloudfront é um serviço de **entrega de conteúdo (CDN)** que entrega dados, vídeos, aplicativos e APIs a clientes de forma mundial, com segurança, **baixa latência** e **alta velocidade**.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-cloud-front-1.png "")

### Funcionamento

Ponto de presença funciona como uma espécie de cache.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-cloud-front-2.png "")


## 07.05 Elastic Load Balancer

Distribuir automaticamente o tráfego de entrada de aplicativos entre diversos destinos, como instâncias do **Amazon EC2**, **contêineres**, **endereços IP** e funções **Lambda**.

Tipos de Load Balancer:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-07-tipos-load-balancer.png "")

## 07.05 Elastic Load Balancer (LAB)

Roteiro:
- Criar duas instâncias no Amazon EC2 em diferentes zonas e disponibiliade;
- Utilizar o campo user data nas instâncias para instalar um servidor Apache HTTP;
- Criar um Application Load Balancer;
- Associar as duas instâncias no ALB;
- Testar o funcionamento do ALB;


