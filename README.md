## Overview

Ephemeral Messaging System is a simple web application where users can create temporary messages that expire after being viewed or after a limited time. The application is deployed on AWS and mainly built for hands-on infrastructure and deployment practice.
This project went through multiple deployment versions during the learning process.


### Version 1 — AWS Infrastructure Focus
Focused mainly on learning AWS architecture, automation, and service integrations.
[Version 1 Architecture README](https://github.com/pnakule/ephemeral-messaging-system-aws/blob/main/README.md)

### Version 2 — Cost Optimized Deployment
The infrastructure was later simplified to reduce AWS costs while keeping the project publicly accessible as a live demo.
[Version 2 Architecture README](https://github.com/pnakule/ephemeral-messaging-system-aws/edit/main/LIVE-ARCHITECTURE.md)


### Current Live Version — Dockerized Deployment
The current live deployment focuses mainly on:
- Docker & Docker Compose
- GitHub Actions CI/CD
- NGINX Reverse Proxy
- EC2 deployment workflows
- Flask + MySQL container integration

This version was mainly created for learning Docker, CI/CD automation, Linux operations, and basic DevOps workflows.

---

## Current Live Architecture

```text
User
→ Route 53
→ CloudFront
→ EC2
   ├── NGINX Reverse Proxy Container
   ├── Flask Application Container
   └── MySQL Container
```

## Tech Stack

- Python Flask
- Docker
- Docker Compose
- MySQL
- NGINX
- GitHub Actions
- AWS EC2
- Linux

## CI/CD Flow

```text
GitHub Commit
→ GitHub Actions Trigger
→ Connect to EC2
→ Pull Latest Code
→ Docker Compose Rebuild
→ Updated Version Live
```

## What I Learned

### Docker & Containerization

- Learned how to containerize a Flask application using Docker
- Understood the difference between application setup and containerized deployment
- Worked with Docker images, containers, rebuilds, and container lifecycle management
- Learned how Flask, MySQL, and NGINX containers communicate together using Docker Compose networking

### Docker Compose Workflow

- Learned how to manage multi-container applications using Docker Compose
- Worked with service dependencies between Flask and MySQL containers
- Understood container restart behavior and rebuild workflows during deployments
- Learned how environment variables are managed using `.env` files

### GitHub Actions CI/CD Workflow

- Built a basic GitHub Actions CI/CD pipeline for automatic deployment
- Understood the complete deployment flow:

```text
GitHub Commit
→ GitHub Actions Trigger
→ Connect to EC2
→ Pull Latest Project Changes
→ Docker Compose Rebuild
→ Updated Application Live
```

- Learned how GitHub Actions runners execute deployment jobs
- Understood how automated deployments work in practical environments
- Learned the difference between workflow execution failures and application deployment failures

### Deployment Workflow Understanding

- Learned how deployment synchronization issues can break automated deployments
- Understood why deployment servers should stay consistent with the latest repository version
- Learned safer deployment synchronization workflow using:

```bash
git fetch origin
git reset --hard origin/main
```

for deployment environments

### NGINX Reverse Proxy

- Learned the purpose of a reverse proxy in front of an application server
- Configured NGINX container to forward requests to the Flask application container
- Understood how reverse proxies separate public traffic from internal application services
- Learned basic reverse proxy routing configuration

### Linux & EC2 Operations

- Worked with Linux commands for troubleshooting containers and deployments
- Used Docker logs and Linux troubleshooting commands during debugging
- Learned basic operational workflow on an EC2 Linux server
- Understood practical deployment troubleshooting workflow

### Deployment Troubleshooting & Debugging

- Debugged GitHub Actions workflow trigger issues
- Solved deployment synchronization conflicts on EC2
- Debugged Docker deployment failures and container restart problems
- Solved MySQL table initialization issues during application startup
- Debugged NGINX reverse proxy configuration issues
- Learned how to isolate problems between:
  - GitHub Actions
  - EC2
  - Docker
  - NGINX
  - Application code

### Overall Understanding

This project helped me understand how multiple infrastructure, deployment, and automation components work together in a practical environment instead of learning each technology separately in isolation.
