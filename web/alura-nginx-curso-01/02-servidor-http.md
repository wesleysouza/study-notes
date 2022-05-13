# NGINX 

docker run --name=web-server2 -p 80:80 -d nginx

nginx -h //ajuda

## Servidor HTTP

nginx -h //ajuda

Nessa ajoda são exibidas várias informações importantes, como por exemplo o arquivo de configuração padrão.

### Arquivos de configuração

Vendo o arquivo de configuração principal sem os comentários:

```bash
cat /etc/nginx/nginx.conf | grep -ve '^\s*#' | grep -ve '^$'
```

Explicando as linhas do arquivo de configuração:

```
user  nginx;
worker_processes  auto; # Definição do número de workers
error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;
events {
    worker_connections  1024; # Quantas conexões um worker pode ter, número máximo de file descriptors.
}
#Configuração do HTTP
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    keepalive_timeout  65;
    include /etc/nginx/conf.d/*.conf;
}

```

A configuração do server está no arquivo etc/nginx/conf.d/*.conf. Nesse arquiv, no momento da configuração de um site troque o server_name para o seu domínio.

O location no servidor o / significa a definição da URL.

## Criando um servidor

Procure o arquivo **default.conf** ele está em /etc/nginx/conf.d/
Crie um novo arquivo.

```
server {
    listen 8080;
    server_name localhost;

    location / {

        root path;
        index index.html
    }
}
```

Testando a sintaxe do arquivo:

```
nginx -t
```

Recarregando a configuração do nginx

digite nginx -h para ver a opção

nginx -s reload

Os arquivos de configuração estão em /etc/nginx/nginx.conf

## Configurando páginas de erro

Códigos de erro:
- Feixa 400: erro do cliente, ele digitou a URL errada
- Faixa 500: erro no servidor

```bash
server {
    listen 8080;
    server_name localhost;

    location / {

        root path;
        index index.html
    }
    # E esperado que dentro do root o arquivo erro.html exista!
    error_page 404 400 401 /erro.html
}
```

Container com um volume:
```
docker run --name=web-server -p 80:80 -p 8080:8080 -v /web-server-lab/nginx-files/nginx-conf-files/:/etc/nginx/conf.d/ -d nginx
```