 Self-Healing DevOps Monitoring System

A cloud-ready DevOps project that automates application deployment, monitoring, visualization, and alerting using Docker, Jenkins, Prometheus, and Grafana.

  Overview

The Self-Healing DevOps Monitoring System is designed to automate the deployment and monitoring of a containerized Flask application. It continuously collects application and system metrics, visualizes them through Grafana dashboards, and generates alerts when resource utilization exceeds predefined thresholds.

This project demonstrates practical DevOps concepts such as Continuous Integration (CI), containerization, infrastructure monitoring, and automated alerting.



 Objectives

- Automate application deployment using Docker.
- Implement Continuous Integration using Jenkins.
- Monitor application health and system performance.
- Visualize metrics using Grafana dashboards.
- Configure alerts for CPU, memory, and service failures.
- Build a scalable DevOps monitoring solution.



 Tech Stack

- Python
- Flask
- Docker
- Docker Compose
- Jenkins
- Prometheus
- Grafana
- Git & GitHub
- AWS EC2
- Prometheus Client
- psutil



 System Architecture

```
                GitHub Repository
                        │
                        ▼
                Jenkins Pipeline
                        │
                        ▼
                Docker Image Build
                        │
                        ▼
          Flask Application Container
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Health Check Endpoint           Metrics Endpoint
        │                               │
        └───────────────┬───────────────┘
                        ▼
                  Prometheus Server
                        │
                        ▼
                Grafana Dashboard
                        │
                        ▼
              Alert Notifications
```



 Project Structure

```
self-healing-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── monitoring/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── prometheus/
│   └── prometheus.yml
│
└── README.md
```



 Features

- Dockerized Flask application
- Jenkins CI/CD pipeline
- Prometheus metrics collection
- Grafana dashboards
- CPU monitoring
- Memory monitoring
- Application health monitoring
- Request count monitoring
- Service uptime tracking
- Alert configuration
- Scalable monitoring architecture



 Installation

1.Clone the Repository

```bash
git clone https://github.com/varshinichilukuri17/self-healing-project.git

cd self-healing-project
```
2.Build Docker Images

```bash
docker-compose build
```

3.Start All Services

```bash
docker-compose up -d
```

4.Verify Running Containers

```bash
docker ps
```



5.Access the Services

| Service | URL |
|----------|-----|
| Flask Application | http://localhost:5000 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |



 Grafana Login

Username

```
admin
```

Password

```
admin
```



 Monitoring Workflow

1. Flask application exposes metrics using Prometheus Client.
2. Prometheus scrapes application metrics.
3. Grafana queries Prometheus.
4. Dashboards display real-time metrics.
5. Alert rules evaluate thresholds.
6. Notifications are triggered when limits are exceeded.


 Grafana Dashboards

The monitoring dashboard includes:

- CPU Usage
- Memory Usage
- Application Request Count
- Service Uptime
- Application Health Status

Alert Rules

The following alerts are configured:

- High CPU Usage
- High Memory Usage
- Application Down
- Service Unhealthy
- Container Failure

CI/CD Workflow

```
Developer
     │
     ▼
 GitHub Repository
     │
     ▼
 Jenkins Pipeline
     │
     ▼
 Docker Image Build
     │
     ▼
 Container Deployment
     │
     ▼
 Prometheus Monitoring
     │
     ▼
 Grafana Dashboard
     │
     ▼
 Alert Notifications
```

 Learning Outcomes

Through this project, I gained hands-on experience in:

- Docker containerization
- Continuous Integration using Jenkins
- Monitoring with Prometheus
- Dashboard creation using Grafana
- Alert configuration
- Infrastructure monitoring
- DevOps automation
- Cloud deployment concepts


 Future Enhancements

- Kubernetes deployment
- Auto-healing using Kubernetes
- Slack notifications
- Microsoft Teams integration
- AWS CloudWatch integration
- Terraform (Infrastructure as Code)
- Ansible automation
- ELK Stack for centralized logging




Author

Varshini Chilukuri

B.Tech – Computer Science and Engineering (IoT)

Raghu Engineering College

GitHub: https://github.com/varshinichilukuri17



 License

This project is developed for academic learning and educational purposes.

