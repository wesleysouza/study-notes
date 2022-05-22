# Dia 01

## Service Mesh

## O que é o Istio

Conjunto de ferramentas para simplificar a observabilidade, gerenciamento do tráfego, segurança e políticas por meio de um service mesh.

Vantagens do Istio:
- Observabilidade;
- Gerenciamento de tráfego;
    - Mudar o tráfego entre versões das aplicações;
- Security:
    - Server to server security (MTLS).
    - Autenticação e autorização.
- Teste: Forçar erros na aplicação.

Obs.: Use com cuidado, o Istio pode prejudicar o desemenho das aplicações.

## Criando um cluster Kubernetes com o Kind

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.14.0/kind-linux-amd64
chmod +x ./kind
mv ./kind /usr/local/bin/kind
```

Vendo os clusters:

```bash
kind get clusters
```

Crie o arquivo kind-example-config.yaml com o conteúdo abaixo:

```yaml
# four nodes (two workers) cluster config
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
```

Esse arquivo que define a estrutura do cluster.

Salve o arquivo e rode o comando abaixo:

```bash
kind create cluster --name nome-do-cluster --config kind-example-config.yaml
```

Observações: 
- É possível pra instalar o Istio com o Helm ou o Terraform.
- O kubectl deve estar apontando para o cluster!

## Instalando o Istio

[Documentação](https://istio.io/latest/docs/setup/getting-started/)

```bash
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.13.4
export PATH=$PWD/bin:$PATH
```

```bash
sudo cp instio-1.13.0/bin/instioctl /usr/local/bin
```

Veja os samples, tem muita coisa boa lá.

### Configuration Profiles

[Perfis de configuração do Istio](https://istio.io/latest/docs/setup/additional-setup/config-profiles/).

```
istioctl install --set profile=demo -y
```

Após a instalação vc vai ver a mensagem abaixo:

Making this installation the default for injection and validation.

Depois disso, deve-se adicionar a flag com o comando abaixo para que o istio consig observar os namespaces:

```bash
kubectl label namespace default istio-injection=enabled
```

Qualquer aplicação que eu subir no namespace default agora o Istio vai adicionar o sidecar para trabalhar como proxy em cada uma das instâncias da aplicação.

### Deploy BookInfo

Entre no diretório **istio-1.13.4/samples/bookinfo/platform/kube** e veja o arquivo bookinfo.yaml.

Rode o arquivo com o kubectl:

```
kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml 
```

Rode o comando kubectl get pods: 

```
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-586577784f-rf2zz       2/2     Running   0          3m48s
productpage-v1-589b848cc9-k2msf   2/2     Running   0          3m48s
...
```

Observe o pod details, nele roda dois containers, o da aplicação e o sidecar (o proxy).

Testando a aplicação:

```bash
kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

### Criando um Istio Ingress Gateway

Forma de conseguir acessar de fora do cluster, crie com o comando abaixo:

```bash
kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml 
```

```
kubectl get virtualservice
```

Checando o namespace:

```
istioctl analyze
```

Não temos loadbalancer, então vamos usar um nodePort. Na AWS será necessário um external IP.

```bash
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
```

Verificando a porta os node ports que ele vai pegar:

```bash
kubectl describe service -n istio-system
```

Ele vai pegar o http2 e https.

Para ver as portas é só dar um echo nas variáveis:

```bash
echo $INGRESS_PORT
echo $SECURE_INGRESS_PORT
```

Definindo ingress host:

```bash
export INGRESS_HOST=$(kubectl get po -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].status.hostIP}')
```

Vendo o IP com a porta para acessar o serviço:

```bash
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
echo $GATEWAY_URL
```

Testando a aplicação:
http://172.18.0.2:31407/productpage

## Deploy dos AddOns: Jaeger, Kiali, Grafana e Prometheus

Criando os serviços:

```bash
kubectl apply -f samples/addons
```

Vendo os 

```bash
kubectl get pods -n istio-system
```

Vendo os dashboards:

- kiali:
```bash
istioctl dashboard kiali
```

### Gerando um tráfego só pra teste

```bash
for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL/productpage"; done
```
