# Proxy Reverso

Um proxy é um servidor por onde passa todas as resuisições de rede. Já o proxy reverso é feito o mesmo procedimento no lado do servidor. Ele pode verificar cache, fazer redirecionamento, balanceamento de carga e etc.

## Configurando

Acesse o arquivo nginx.conf e verifique onde ta os servers, adicione no **location** o seguinte comando:

proxy_pass http://localhost:80;

Agora, quando alguém mandar uma requisição para esse servidor ela será encaminhada para **http://localhost:80**.

## Trabalhando com outro servidor de aplicação

Objetivo: sempre que for buscado algo com php a requisição será redirecionada para um servidor que roda php.
