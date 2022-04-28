# AWS IAM - Identidade e Segurança

## 04.01 Users, Groups & Roles

- Usuário (Operador de nome permanente):
	- Pessoa ou serviço, com credenciais **permanentes**;
	- **Não** compartilhe o susário **root** e use o **least privilege** (menor privilégio);
- Grupos:
	- Coletivo de usuários;
	- Grupos **não** podem conter outros grupos;
- Funções (Roles):
	- **Não** são suas permissões;
	- É um método de autenticação **temporária**

Obs.: A função é quando um usuário, máquina ou conjunto de serviços vai realizar uma comnunicação temporária. Toda a comunicação na AWS é via API, e eles usam essas funções.

### Regra básica:

Primeiro Autentica (usuários, grupos & funções)
Depois autoriza (Políticas & Permissões) -> Policy Documents

### Políticas e permissões

Documento JSON que define as permissões de acesso, exemplo:

```json
{
    "Version": "2012-10-17"
    "Statement": {
        "Effect": "Allow",
        "Action": "s3:ListBucket",
        "Resource": "arn:aws:s3:::example_bucket"
    }
}
```

A policy document escuta as requisições de uma API específica ou conjunto de APIs e passa por uma sequencia de condições como por exemplo, tipo de recurso, se está especificado em uma única subrede ou região...

Esse documento pode ser associado a um usuário, função ou grupo.

### API execution statement

A API engine verifica se a autenticação é válida e se o operador é permanente ou temporário (função). Com a autenticação válida o API engine vai para o passo 2 (validação do JSON) e verifica o que está autorizado para aquele operador, se o que ele que deseja fazer é permitido a operação é realizada.

### Dicas do Exame:

- **Usuários** possuem credenciais **permanentes** e **funções** possuem credenciais **temporárias**;
- Usuários root **NÃO** devem ser compartilhados;
- Use o **least privilege principle** nos usuários;
- Documentos JSON definem as permissões de acesso;
- Grupos contém outros usuários, mas **NÃO** podem conter outros grupos.

## 04.02 AWS IAM (LAB)

- O serviço do IAM é global.
- É recomendado a ativação do MFA no usuário root;

### Criando usuário admin para os labs

- Acesso programático: Acesso via CLI (Terraform);
- Acesso ao console de Gerenciamento;
- Tags são muito importantes, sempre utilize, elas trabalham com os campos chave e valor.
- A chave de acesso e chave secreta é para acesso programático, ela só será gerada uma única vez!
- Criando novo grupo com o nome Administradores e atribua a politica AdministratorAcess

### Melhorando a segurança

Vá em configurações da conta e em mudar política de senha.

### Atividade

- Trocar URL de login de acesso;
- Ativar MFA na conta root;
- Criar novo usuário;
- Criar grupo com permissão "administratoraccess"
- Adicionar o novo usuário nesse grupo;
- Melhorar a segurança das senhas no ambiente;
- Acessar o ambiente com o novo usuário e habilitar o MFA;

## 04.03 AWS Web Application Firewall (WAF)

O **AWS WAF** é um **firewall de aplicativos web** que permite especificar qual o tráfego tem o seu acesso permitido ou bloqueado, mediante a definição de regras personalizáveis.

Características:
- WEB ACL (URI) - Camada 7;
- Bloquear requisições maliciosas como SQL injection (SQLi) e cross-site scripting (XSS);
- Bloquear países (get-match), size constraints (limitar o tamanho das requisições) e rate based-rules (evitar DDOs).

### Dicas do Exame:
- WAF é um Firewall de Aplicações WEB;
- Atua na camada 7 -> **HTTP**;
- Bloqueia SQL injection (SQLi) e cross-site scripting (XSS);
- **Geo-match** (bloqueio países), **size constraints** (limitar o tamanho das requisições) e **rate based-rules** (limitar qtde. requisições por segundo).

## 04.04 AWS Shield Standard & Advanced

Por padrão está liberado esse serviço para proteção contra ataques DDOs:
- Gratuíto para todos os clientes AWS;
- Proteção SYN/UDP Floods, Reflection Attacks;
- Outros ataques na camada 3 e camada 4;

O serviço pago é o advanced:
- Serviço pago;
- Suporte 24x7;
- Proteção extra nos serviços:
    - Amazon EC2, Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator e o Route53.

Obs.: Qualquer prejuízo são cobertos pela AWS.

### Dicas do Exame:
- AWS Shield é para mitigar ataques DDoS;
- **Standard** é gratuíto para todos;
- **Advanced** é pago, suporte 24x7 e possuí proteção extra em determinados serviços.