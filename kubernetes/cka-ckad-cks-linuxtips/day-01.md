# [CKA - CKAD] Day 1 - Workloads | Application Environment, configuration

## Intro

Requisitos:
- Máquina Linux
- Kind

### Instalação do Docker

```bash
curl -fsSL https://get.docker.com | bash
```

### Instalação do Kind

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.13/kind-linux-amd64
chmod +x ./kind
mv /usr/local/bin/
```

### Instalação do Kubectl

[Kubectl Documentação](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)


### Criando Cluster no Kind

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

### Testando o Kubectl

```bash
kubectl get pods
kubectl cluster-info
```

### Facilitando o nosso ambiente

#### Ativando o autocomplete:

De maneira provisória:

```bash
source <(kubectl completion bash)
```

De forma permanente:

```bash
echo 'source <(kubectl completion bash)' >>~/.bashrc
#Recarregando o bash
source .bashrc
```

#### Configurando o VIM

```bash
#Crie o arquivo
vim .vimrc
```

Adicione o conteúdo abaixo:

```bash
set expandtab #Usar o tab como espaço.
set tabstop=2 #Dois espaço para cada tab.
set shiftwidth=2 #Quantos espaços ele vai manter pra baixo.
```

#### Add Alias

Abra o arquivo **.bashrc** e add os alias:

```bash
alias k=kubectl
complete -F __start_kubectl k
alias kgd='kubectl get pod'
alias kd='kubectl describe'
```

Criando alias para o dry-run como variável de ambiente:

```
export d="--dry-run=client -o yaml"
```

## Pods

```
```