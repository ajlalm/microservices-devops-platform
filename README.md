# 🚀 Microservices DevOps Platform

A production-style microservices platform built using **Flask, Docker, Kubernetes, Nginx, Prometheus, and Grafana**.

This project demonstrates modern DevOps practices including containerization, orchestration, monitoring, scaling, health checks, and CI/CD automation.

---

# 📌 Project Overview

The platform consists of two Flask microservices:

* **Auth Service** – Handles authentication-related APIs.
* **Task Service** – Handles task management APIs.

Traffic is routed through an **Nginx API Gateway**, deployed on **Kubernetes**, monitored using **Prometheus**, and visualized through **Grafana dashboards**.

---

# 🏗️ Architecture

```text
                    User
                      │
                      ▼
              Nginx Gateway
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
   Auth Service               Task Service
        │                           │
        └─────────────┬─────────────┘
                      │
                      ▼
                 Prometheus
                      │
                      ▼
                   Grafana
```

---

# 🛠️ Technology Stack

## Backend

* Python
* Flask

## Containerization

* Docker
* Docker Compose

## Orchestration

* Kubernetes

## API Gateway

* Nginx

## Monitoring & Observability

* Prometheus
* Grafana

## CI/CD

* GitHub Actions

## Version Control

* Git
* GitHub

---

# ✨ Features

## Auth Service

* Login endpoint
* Health endpoint
* Prometheus metrics endpoint

### Endpoints

```http
GET /health
POST /login
GET /metrics
```

---

## Task Service

* Fetch tasks
* Create tasks
* Health endpoint
* Prometheus metrics endpoint

### Endpoints

```http
GET /health
GET /tasks
POST /tasks
GET /metrics
```

---

# 🐳 Docker

Each microservice is containerized using Docker.

### Build Images

```bash
docker build -t auth-service:local ./services/auth-service
docker build -t task-service:local ./services/task-service
```

### Run with Docker Compose

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

# 🌐 Nginx API Gateway

The Nginx Gateway acts as a reverse proxy and routes requests to the correct service.

### Routing

```text
/auth/*  → Auth Service
/tasks/* → Task Service
```

Example:

```bash
curl http://localhost:8080/auth/health
curl http://localhost:8080/tasks/health
```

---

# ☸️ Kubernetes Deployment

The platform is deployed on Kubernetes using:

* Deployments
* Services
* ConfigMaps

## Deploy Services

```bash
kubectl apply -f k8s/auth-service/
kubectl apply -f k8s/task-service/
kubectl apply -f k8s/gateway/
```

Verify:

```bash
kubectl get pods
kubectl get svc
```

---

# 📈 Monitoring with Prometheus

Prometheus collects metrics from:

* Auth Service
* Task Service

Metrics are exposed through:

```text
/metrics
```

Example:

```bash
curl http://localhost:5001/metrics
curl http://localhost:5002/metrics
```

Prometheus configuration is managed using a Kubernetes ConfigMap.

---

# 📊 Grafana Dashboards

Grafana is connected to Prometheus and visualizes application metrics.

Example metrics:

```text
auth_service_requests_total
task_service_requests_total
```

Dashboard examples:

* Auth Service Requests
* Task Service Requests
* Service Health Monitoring

---

# 🔄 Kubernetes Scaling

The project demonstrates horizontal scaling.

Example:

```bash
kubectl scale deployment auth-service --replicas=3
```

Kubernetes automatically creates additional pods.

Verify:

```bash
kubectl get pods
```

---

# ❤️ Health Checks

The platform includes:

## Readiness Probe

Determines if the application is ready to receive traffic.

## Liveness Probe

Determines if the application is healthy and should continue running.

Example:

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 5001

livenessProbe:
  httpGet:
    path: /health
    port: 5001
```

---

# ⚙️ Resource Management

Resource requests and limits are configured.

Example:

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "250m"
    memory: "256Mi"
```

This prevents services from consuming excessive cluster resources.

---

# 🔧 CI/CD Pipeline

GitHub Actions is used to:

* Validate code
* Run automated tests
* Build containers
* Support deployment workflows

---

# 🚀 Running the Project

## Local Development

```bash
docker compose up -d
```

Test:

```bash
curl http://localhost:8080/auth/health
curl http://localhost:8080/tasks/health
```

---

## Kubernetes

```bash
kubectl apply -f k8s/auth-service/
kubectl apply -f k8s/task-service/
kubectl apply -f k8s/gateway/
kubectl apply -f k8s/monitoring/
```

Verify:

```bash
kubectl get pods
kubectl get svc
```

---

# 📚 DevOps Concepts Demonstrated

* Microservices Architecture
* Docker Containerization
* Docker Compose
* Reverse Proxy Routing
* Kubernetes Deployments
* Kubernetes Services
* ConfigMaps
* Health Checks
* Scaling
* Resource Management
* Monitoring
* Observability
* CI/CD Automation

---

# 🔮 Future Improvements

* Horizontal Pod Autoscaler (HPA)
* Centralized Logging
* Helm Charts
* Terraform Infrastructure
* AWS Deployment
* Kubernetes Ingress Controller
* Persistent Storage
* Distributed Tracing

---

# 👨‍💻 Author

**Ajlal Mubarik**


GitHub: https://github.com/ajlalm
