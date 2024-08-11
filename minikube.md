# Install Minikube en Ubuntu

## Update
sudo apt-get update -y
sudo apt-get upgrade -y

## Docker
sudo apt-get install -y curl apt-transport-https
sudo apt-get install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker

### snap
sudo snap install docker

### testing
docker run hello-world

## kubectl
curl -LO "https://dl.k8s.io/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

## minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Create k8s
minikube start --nodes=4 --cpus=2 --memory=2096 --driver=docker

# Install flannel
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

    