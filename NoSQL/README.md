# NoSQL


## Installation

```bash
sudo apt update
sudo apt install docker.io
sudo docker pull mongo:4.2
sudo docker run --name mongodb -d -p 27017:27017 mongo:4.2
sudo docker ps
sudo docker exec -it mongodb mongo
pip3 install pymongo

```

## How install libssl1.1 on ubuntu 22.04
```bash
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
sudo dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb
```
## MongoDB Shell Installation
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org-shell
```