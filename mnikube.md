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
