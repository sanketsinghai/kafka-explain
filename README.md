# 🚀 Docker Beginner Guide for Python Developers

## 📌 What is Docker?
Docker is a **containerization platform** that allows developers to package applications along with their dependencies into **lightweight, portable containers**.

### 🔥 Why Use Docker?
✅ **Portability** – Runs consistently across different environments.  
✅ **Efficiency** – Consumes fewer resources than Virtual Machines.  
✅ **Scalability** – Easily scales applications across multiple servers.  
✅ **Isolation** – Each container runs independently.  

---

## 🎯 1️⃣ Installing Docker

### 📍 On Ubuntu / Debian
```sh
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker


docker --version


🎯 2️⃣ Basic Docker Commands
✅ Checking Docker Version
```sh
docker --version

✅ Running a Test Container
```sh
docker run hello-world
✅ Listing All Containers
```sh
docker ps -a
✅ Stopping & Removing Containers
```sh
docker stop <container_id>
docker rm <container_id>
✅ Pulling & Running an Image
```sh
docker pull python:3.9
docker run -it python:3.9 /bin/bash
🎯 3️⃣ Running a Python App in Docker
Step 1: Create a Simple Python App
Create app.py:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
Step 2: Create requirements.txt
```sh
flask
Step 3: Create Dockerfile
```sh
Edit
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
Step 4: Build & Run the Docker Container
```sh
docker build -t my-python-app .
docker run -p 5000:5000 my-python-app
Visit http://localhost:5000.

🎯 4️⃣ Using Docker Compose
Step 1: Create docker-compose.yml
```yaml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: "redis:alpine"
Step 2: Run & Stop Containers
```sh
docker-compose up
docker-compose down
🎯 5️⃣ Docker Best Practices
✅ Use a .dockerignore file:
