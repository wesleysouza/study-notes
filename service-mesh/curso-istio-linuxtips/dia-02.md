# Dia 02

Recriando as variáveis de ambiente temporárias:

```bash
export INGRESS_HOST=$(kubectl get po -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].status.hostIP}')

export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')

export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')

export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
```

## Entedendo melhor a relação entre a nossa App e o Istio

![istio-app](/service-mesh/curso-istio-linuxtips/img/app-istio.png)

## Entedendo o que é virtual service

Para que o Istio controle o tráfego precisamos passar para ele algumas informações. Essas informações são passadas por meio dos Custom Resources, eles são o **Virtual Service** e o **Destination Rule**.

```
kubectl get destionationrules
```

### Virtual Service

É um Custom Resource Definition (CRD), esses objetos são criados extendendo o Kubernetes.

Analisando o bookinfo gateway e virtualservice (samples/bookinfo/networking/bookinfo-gateway.yaml). O gateway configuyra as uls padrão para acesso.

Para adicionar uma nova versão é necessário adicionar um novo destination. A uri é epanas uma opção, podemos pegar os headers tmb.

Verifique as **labels* de um dos pods do reviews usando o comando kubectl describe pods.

Verifique o service de reviews com o kubctl, para mais detalhe use o comando abaixo:

```
kubectl get svc reviews -o yaml
```

O serviço por meio do **seletor** seleciona o pod para o qual ele vai enviar as requisições, como ele está procurando pelo label=reviews e todas as versões tem ele então o service faz um roud robin para cada uma das instâncias.

### Criando os virtual services

Verifique o arquivo **samples/bookinfo/networking/virtual-service-all-v1.yaml**. Com ele vamos criar virtual services para cada um dos nossos microserviços.

O subset é o campo que possibilita o envio das requisições para alguma versão da aplicação reviews.

Criando os virtual services:

```bash
kubectl apply -f samples/bookinfo/networking/virtual-service-all-v1.yaml
```

```bash
kubectl get virtualservices
```

Obs.: A aplicação vai quebrar, no tópico abaixo vamos resolver isso!

## Entendendo o que é Destination Rule - Traffic Shifting

Está dando problema porque ele não sabe chegar nos caras.

Analisando o arquivo do destination rule:

```bash
vim samples/bookinfo/networking/destination-rule-all.yaml
```

No destinaiton rule é definido como que chega nos serviços. O destination rule é onde vc define o que foi declarado no virtual service.

```bash
kubectl apply -f samples/bookinfo/networking/destination-rule-all.yaml
```

Altere o arquivo do virtual-service-all-v1.yaml adicionando novos destinations (as outras versões) no objeto destinationrule. Além disso, é necessário add o balanceamento:

![istio-app](/service-mesh/curso-istio-linuxtips/img/destinations.png)

O Destination Rule impacta diretamente no tráfego. O virtual service (VS) é como se fosse um nó.

## Explorando ainda mais o Virtual Service - Request Routing

Alterando o arquivo do virtual service: fazendo match com o headers:

![istio-app](/service-mesh/curso-istio-linuxtips/img/destination-match-with-headers.png)

Mudando versão pela identidade do usuário:

![istio-app](/service-mesh/curso-istio-linuxtips/img/destination-identidade-usuario.png)

## Mudando o comportamento da App utilizando o Virtual Service - Request Timeout

Aplicando o **fault injection** para ver como as aplicações se comportam:

![istio-app](/service-mesh/curso-istio-linuxtips/img/destination-fault-injection.png)

Por meio dessa injeção de falhas da pra saber o quanto a nossa aplicação pode suportar.

Resumo do que foi visto até o momento (Traffic Management):
- Fault Injection;
- Request route;
- Traffic Shifting;
- Request timeout.