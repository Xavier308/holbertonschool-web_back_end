# NoSQL

This project focuses on NoSQL databases, specifically MongoDB, and includes various tasks to practice working with NoSQL concepts.

## Installation

Follow these steps to set up the required environment:

```bash
# Update package list
sudo apt update

# Install Docker
sudo apt install docker.io

# Pull MongoDB 4.2 Docker image
sudo docker pull mongo:4.2

# Run MongoDB container
sudo docker run --name mongodb -d -p 27017:27017 mongo:4.2

# Verify container is running
sudo docker ps

# Access MongoDB shell
sudo docker exec -it mongodb mongo

# Install PyMongo
pip3 install pymongo
```

### Installing libssl1.1 on Ubuntu 22.04

If you encounter issues with libssl1.1, use these commands:

```bash
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
sudo dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb
```

### MongoDB Shell Installation

To install the MongoDB shell separately:

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org-shell
```


## Learning Objectives

- The meaning of NoSQL
- Differences between SQL and NoSQL
- What ACID is
- Document storage concepts
- Types of NoSQL databases
- Benefits of NoSQL databases
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File

- All files interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- Files should end with a new line
- First line of all files should be a comment: `// my comment`
- A `README.md` file at the root of the project folder is mandatory

## Resources

- NoSQL Databases Explained
- What is NoSQL?
- MongoDB with Python Crash Course - Tutorial for Beginners
- MongoDB Tutorial 2: Insert, Update, Remove, Query
- Aggregation
- Introduction to MongoDB and Python
- mongo Shell Methods
- The mongo Shell
