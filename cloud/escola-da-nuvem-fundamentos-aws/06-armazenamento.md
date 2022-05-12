# Armazenamento

## 06.01 Amazon S3 - Simple Storage Service

Definição: É um serviço **gerenciado** de armazenamento e recuperação de objetos, respondendo com escalabidade, disponibilidade, segurança e performance.

Benefícios:
- **Armazenamento** virtual ilimitado;
Compartilhar arquivos ou criar um website estático;
- Armazenar snapshots, backups, gerar um armazenamento híbrido do seu ambiente on-premises;
- Repositório de data lakes e análise de big data;
- Baixa latência e alta velocidade;
- Durabilidade 99,99999999999 (onze noves);

Nomeclaturas:
- Armazenamento: buckets;
- Arquivos: objetos;
- Sub-Pasta: pefixos;

Usando um Bucket S3:
- Criar Bucket (nome único global);
- Configurar permissões;
- Enviar dados;

Exemplo de URL:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-s3.png "")

Obs.: Essa pasta é apenas um prefixo, deixando o seu objeto com o nome grande.

Conhecendo objetos:
- Tamanho máximo do objeto: 5TB;
- Upload > 5GB use o multi-part upload;
- Metadata (chave e valor por sistema e usuário);
- Tags (chave e valor por **usuário**);
- Versionamento de objetos;

### Dicas do exame
- Amazon S3 é um serviço CORE da AWS;
- Entenda o que é e como ele funciona;
- Leia os benefícios e entenda o conceito de objetos;
- Faça os laboratórios disponíveis;
- Memorize a URL do S3;
- Lembre que não existe pasta no S3.

## 06.02 Classes de Armazenamento

Oferecer uma variedade de categorias de armazenamento, para atender diferentes casos de uso. Em conjunto com a **política de ciclo de vida**, os dados são migrados automaticamente entre essas categorias, refletindo em menor custo de armazenamento.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-classes-de-armazenamento.png "")

Cenário: O hospital onde você trabalha, está procurando formas de **armazenar** os prontuários médicos com menor custo. Qual a **melhor solução** que você pode apresentar, pensando na durabilidade e na disponibilidade dos dados?

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-cenario-s3.png "")

Obs.: Quanto mais profundo e menor acesso eu tiver ao arquivo menos eu vou pagar peloi amazenamento.

O S3 Intelligent Tiering (serviço pago) faz a movimentação automática do arquivo, mas eu posso fazer isso na mão.

S3 One Zone IA: armazena os dados em apenas uma zona de disponibilidade, com a vantagem de ter um menor custo.

Recuperação de dados: Enquanto ele não for movido para o S3 Glacier a recuperação dele é imediata, mas se for movido para o Glacier pode demorar minutos ou horas e se for para o Deep Archive, até 12 horas. Por esse motivo o armazenamento no Glacier é mais barato.

**IMPORTANTE: O S3 é exclusivo para objetos, para subir um SO usamos o Amazon EBS.**

## 06.03 Criar um bucket S3 (LAB)

- Acessar o Amazon S3
- Criar um Bucket S3
- Enviar um objeto no Bucket S3
- Acessar o objeto
- Criar pasta (prefixo);
- Deletar o objeto;

## 06.04 Criar um Website Estático (LAB)

- Acessar o Amazon S3;
- Upload dos arquivos **index.html** e **erros.html**;
- Alerar o Bucket S3 para um Website estático;
- Remover configuração do Bucket S3;
- Criar política via AWS Policy Generator;
    - Use o [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html) para criar a policy.
- Aplicar política no Bucket S3 e testar acesso público.

## 06.05 Amazon Elastic Block Storage (EBS)

**Armazenamento** de **blocos** de alta performace fácil de usar em qualquer escala.

Arquitetura lift and shift:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-lift-and-shift.png "")

Aplicação web com BD em um EC2:
- Toda a parte do BD, software e SO está armazenada dentro de um disco do amazon EBS.
- As imagens, códigos de páginas e vídeos (arquivos estáticos) estão dentro de um Bucket S3.

Definição EBS:

É um serviço de **armazenamento** de **blocos persistentes**, projetado como um **volume**, para ser **conectado** e utilizado como um **disco** em instâncias do Amazon EC2.

Obs.: Os dados das instâncias EC2 são efêmeros (se perdem quando a instância é desligada), para salvar os dados é necessário criar um disco com o EBS. Além disso, é possível atachar esse bloco em outra instância EC2.

**ZD: Conjunto de dadacenters conectados e fazendo a replicação de dados entre sí.**

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-caracteristicas-ebs.png "")

## 06.06 Criar um Snapshot (LAB)

Roteiro:
- Acessar o EBS;
    - Procurar por volumes;
    - Create Snapshot;
    - Vá em Snapshots e aguarde ele finalizar;
    - Create image (criando ami);
    - EC2 image builder.
- Gerar um Snapshot de um volume EBS;
- Criar uma AMI a partir do Snapshot, que foi gerado;
- Iniciar uma nova instância EC2, sendo o volume EBS, os dados do Snapshot.

## 06.07 Limpeza do ambiente

- Teminate instâncias EC2
- Remover as AMIs criadas;
    - AMIs desiregisters;
- Apagar Snapshots que foram gerados.

## 06.08 Família AWS Snow

Composto por três produtos:
- Snowcone;
- Snowball;
- Snowmobile.

Esse objetivos tem como o objetivo transferir dados de grandes quantidades de dados para dentro e para fora da AWS.

### AWS Snowcone

- 8TB;
- 2vCPU;
- 4GB de memória;
- Criptografia em 256 bits;
- Lugares inóspitos;
- Portátil;
- Pode computacional;

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-snowcone.png "")

### AWS Snowball Edge

**Transportar dados em escala petabyte!**

- Storage Optimized:
    - 100 TB (disponível 80 TB);
    - 24 vCPU;
    - 32 GB de memória.
    - **Migrar dados na escala petabites: solicitar conjunto de snowball edge**.

- Compute Optimized:
    - 42 TB (disponível 39.5 TB);
    - 52 vCPU;
    - 208 GB de memória;
    - SSD 7.68 TB NVMe.

Ambos possuem características:
- Criptografia em 256 bits
- Resistente a violações
- Menos de 32 Kgs

Cenário:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-snowball-edge.png "")

No caso de um cruzeiro podemos usar um Compute Optimized, após o uso dispachamos para a sincronização com a cloud.

### AWS SnowMobile

**Transporte de dados na escala exabytes.**

Pode transportar até **100 petabytes de dados** em **uma única viagem**, o equivalente a usar cerca de 1250 dispositivos AWS Snowball.

Esse serviço é limitado a algumas regiões e uma escolta armada vem junto.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-snowmobile.png "")

Resumo:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-resumo.png "")

Tabela com a comparação dos serviços:

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-snowtabela.png "")

Observações:
- Solução exabyte: snowmobile.
- Transferencia de dados petabyte: Snowball Storage Optimized.

## 06.09 Amazon S3 Glacier Deep Archive

Classes de armazenamento de objetos de longo prazo seguro, resiliêntes do Amazon S3 a partir de 1 USD oir terabyte por mês.

![Lista](/cloud/escola-da-nuvem-fundamentos-aws/imgs/cap-06-aws-gracier.png "")

Obs.: Cuidado com a criação da regra do ciclo de vida, ele pode gerar custos extras.

Características:
- Armazenamento a longo prazo;
- S3 Glacier: 0,004 USD por gigabyte por mês;
- Deep Archive: 0,000 USD GB-mês (acesso 1 ou 2x por ano);
- Durabilidade de 99,99%;
- Dados armazenados como um arquivo;
- Conteúdo é imutável após envio;
- Arquivamento de 1 byte até 40 terabytes;
- Recuperação Padrão de 3 até 5 horas;
- Recuperação Massa de 5 até 12 horas;
- Recuperação Expressa (<250mb) 1 a 5 minutos;
- Dados recuperados ficam no bucket S3 por 24 horas.

