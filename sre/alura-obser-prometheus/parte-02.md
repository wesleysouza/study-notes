# Métricas default e personalizadas

## Métricas da JVM

hicaricp: métricas relacionadas com o Banco de Dados.

## Métricas Personalizadas

Chegou a hora de criar métricas que possam medir regras de negócio. Aqui vamos criar duas métricas personalizadas para:
- Métrica para autenticação com sucesso;
- Métrica para erro de autenticação.

Entre no diretório do projeto **src/main/java** e depois no pacote **br.com.alura.forum.controller** e abra a classe **AutenticacaoController.java**. Essa classe retorna um token caso a autenticação for um sucesso.

Crie os atributos abaixo na classe:

```java
Counter authUserSuccess;
Counter authUserErrors;
```

Obs.: Será necessário importar o **Counter** do micrometer.

Agora crie o método abaixo:

```java
public AutenticacaoController(MeterRegistry registry) {
    authUserSucess = Counter.builder("auth_user_sucess").description("usuarios autenticados").register(registry);

    authUserErrors = Counter.builder("auth_user_error").description("erros de login").register(registry);
}
```

Agora vamos configurar a contagem para que ela seja "ativada" no local adequado:

```java
@PostMapping
public ResponseEntity<TokenDto> autenticar(@RequestBody @Valid LoginForm form) {
	UsernamePasswordAuthenticationToken dadosLogin = form.converter();
	try {
		Authentication authentication = authManager.authenticate(dadosLogin);
		String token = tokenService.gerarToken(authentication); 
        //AQUI
		authUserSuccess.increment();
		return ResponseEntity.ok(new TokenDto(token, "Bearer"));
			
	} catch (AuthenticationException e) {
        // E AQUI
		authUserErrors.increment();
		return ResponseEntity.badRequest().build();
	}
}
```

Agora já estamos com uma métrica do tipo Counter configurada.

Execute novamente o comando abaixo para reconstruir a aplicação:

```bash
mvn clean package
```

Para rodar user novamente o script **start.sh**.

### Testando com o Postman

Abra o Postman e faça uma requisição do tipo Post para o endpoint **localhost:8080/auth** utilizando as configuações abaixo:
- Authorization: Bearer Token
- Headers: Adicione a key **Content-Type** e o valor **application/json**.
- Body:

```json
{
    "email":"moderador@email.com",
    "senha":"123456"
}
```

Envie a requisição e agora veja as métricas no link **http://localhost:8080/actuator/prometheus**.

Para mais detalhes consule [Spring Metrics](https://docs.spring.io/spring-metrics/docs/current/public/prometheus).

## Preparando a API para a conteinerização

Vá no diretório **src/main/properties** e edite o arquivo **aaplication-prod.properties** nas linhas 5 e 10 deixando dessa forma:

```bash
# Redis cache config 
spring.cache.type=redis
spring.redis.host=redis-forum-api
spring.redis.port=6379

# datasource
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://mysql-forum-api:3306/forum
spring.datasource.username=forum
spring.datasource.password=Bk55yc1u0eiqga6e
```

Execute novamente o comando abaixo para reconstruir a aplicação:

```bash
mvn clean package
```

Para rodar user novamente o script **start.sh**.