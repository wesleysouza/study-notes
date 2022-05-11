# Gerenciamento de Custos

## 03.01 - Nível Gratuíto da AWS

[Free Tier AWS](https://aws.amazon.com/pt/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)

## 03.02 - Plano de Suporte AWS

[Planos do AWS Support](https://aws.amazon.com/pt/premiumsupport/plans/)

### Cenário exemplo

Um grupo de desenvolvedores de uma startup está decidindo o melhor plano para a empresa. Eles atuam em horário comercial e uma única pessoa será responsável pela abertura do case de suporte.

Resposta: Developer.

### Dicas de exame:
- Case de suporte técnico NÃO são oferecidos no plano **Básico**;
- Trusted Advisor **completo** somente nos planos **Business e Enterprise**;
- Suporte em até 15 minutos, apenas no plano **Enterprise**.
- **TAM**, **Concierge** e **revisão** de arquitetura, apenas no plano **Enterprise**.

## 03.03 - Interface de Acesso da AWS

As interfaces de acesso são:
- AWS Management Console;
- Linha de comando (CLI);
- Software Development Kit (SDK).
    - Acesso a funcionalidades do ambiente por meio de linguagens de programação.

Essas interfaces foram construídas em cima da API principal da AWS.

### Dicas do Exame:
- Console Gerenciamento AWS:
    - via https & app.
- AWS Command Line Interface:
    - via terminal.
- Software Development Kit:
    - via API, programação.

## 03.04 Criando Conta na AWS

A criação é simples e o cartão de crédito será necessário.

## 03.05 AWS Budgets (Criando Orçamento)

Criando buget:
- Acesso como root;
- Painel;
- Meu painel de faturamento;
- Preferências de Faturamento:
    - Ativar receber alerta de uso da camanda gratuíta
    - Crie um orçamento:
        - Defina período e nome;
        - Defina limites de alerta;
        - Defina os destinatários de e-mail.

## 03.06 AWS Cost Explorer

Abra o AWS Cost Manager.

Abra no console o Cost Explorer.

Obs.: É possível gerar e salvar relatórios.

### Pergunta de exame:

O gerente de tecnologia, da multinacional que você atua, solicitou um relatório de qual região na AWS está gerando o maior custo.

Qual a ferramenta você deve utilizar para atender este pedido e gerar um relatório no formato .CSV?

Resp: AWS Cost Explorer.

### Dicas de exame:
- **AWS Cost Explorer** é uma interface para visualizar, entender e gerenciar os custos e usa da AWS ao **longo do tempo**.
- **AWS Budgets** é para definir **orçamentos** personalizados e **enviar alertas** quando o uso ou os cursos excede o valor orçado.

## 03.07 AWS Pricing Calculator

Essa calculadora foi desenvolvida para ajudar na mensuração de custos de projetos.

Estimar custos e serviços:
- Modifique o idioma.
- Adicione o serviço:
    - Realize a busca pelo nome ou característica;
- Configure e ajuste:
    - Altere os detalhes de uso e o custo do serviço.
- Obtenha uma estimativa:
    - Custos separados por serviço, grupo ou total.

Obs.: Os preços da calculadora são em dólares e não levam em consideração impostos e etc.
