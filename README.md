# DevOps Project - From Local to CI/CD

![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-black)
![Python](https://img.shields.io/badge/Python-Flask-green)
![Status](https://img.shields.io/badge/Status-Working-success)

---

## Contexto

Este projeto foi criado para sair da teoria e executar um fluxo real de DevOps:

Da execução manual local  
Para um processo automatizado com CI/CD  

Durante o processo, enfrentei problemas reais (como erro de build e ficheiros não encontrados) e corrigi entendendo o funcionamento do Docker, não apenas seguindo passos.

---

## O QUE ESTE PROJECTO FAZ

- Cria uma aplicação simples em Python (Flask)
- Containeriza a aplicação com Docker
- Executa localmente via container
- Automatiza build e validação com CI/CD

---

##  ARQUITECTURA

```text
        +-------------------+
        |   Código (Git)    |
        +---------+---------+
                  |
                  v
        +-------------------+
        | GitHub Actions    |
        | (CI/CD Pipeline)  |
        +---------+---------+
                  |
                  v
        +-------------------+
        | Docker Build      |
        +---------+---------+
                  |
                  v
        +-------------------+
        | Container Running |
        +-------------------+

devops-project/
 ├── app.py
 ├── requirements.txt
 ├── Dockerfile
 ├── .github/
 │    └── workflows/
 │         └── deploy.yml


git clone <url-do-repo>
cd devops-project

docker build -t myapp .

docker run -p 5000:5000 myapp

http://localhost:5000

docker build -t myapp .
docker run -p 5000:5000 myapp


Pipeline criado com GitHub Actions:
Trigger: push na branch main
Etapas:
Checkout do código
Build da imagem Docker
Execução do container para validação
