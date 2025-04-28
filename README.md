# **Cloud-Automated Web Application Deployment with Monitoring**

## **Overview**

This project demonstrates the deployment of a containerized web application using AWS infrastructure, leveraging DevOps practices, Infrastructure as Code (IaC), CI/CD automation, and monitoring tools. The application is built using Python Flask, containerized with Docker, deployed on AWS EKS with Kubernetes, and includes Prometheus and Grafana for monitoring and visualization.

## **Key Components:**
- **Terraform:** Infrastructure provisioning on AWS.

- **Docker:** Containerization of the Python Flask application.

- **GitHub Actions:** CI/CD pipeline automation.

- **Helm:** Simplified installation and management of Prometheus and Grafana.

- **Kubernetes (EKS)**: Deployment and scaling of the application.

- **Prometheus:** Monitoring and alerting.

- **Grafana:** Visualizing application metrics.

## **Project Flow**

## **1. Infrastructure Provisioning with Terraform**
Terraform is used to automate the provisioning of AWS resources, including:

-EC2 instances for the app deployment.

-VPC, subnets, and security groups for network configuration.

-IAM roles and policies for AWS service access.

Steps to provision infrastructure:

Navigate to the terraform/ directory.

Run the following commands to initialize and apply Terraform configurations:

- terraform init
- terraform plan
- terraform apply
- This will set up your infrastructure on AWS.

### **2. Docker Setup**
The Flask application is containerized using **Docker**. Below is the example `Dockerfile` used to containerize the application.
Steps to build and push the Docker image:

**Build the Docker image:**

Navigate to the app/ directory where the Dockerfile is located.

Run the following command to build the Docker image:
docker build -t YOUR_USERNAME/devops-flask-app .
Push the Docker image to DockerHub:

Login to your DockerHub account (make sure your DOCKER_USERNAME and DOCKER_PASSWORD are stored in GitHub secrets):

docker login --username YOUR_USERNAME
Push the image to DockerHub using the following command:

docker push YOUR_USERNAME/devops-flask-app


## **3. CI/CD Pipeline with GitHub Actions**
The **GitHub Actions pipeline** automates the entire process:
- **Linting**: Ensures code quality by running linters.
- **Build and test**: Builds the Docker image and runs any tests.
- **Push**: Pushes the image to DockerHub/GitHub Container Registry.
- **Deploy**: Deploys the application to the Kubernetes cluster on **AWS EKS**.

This is automated in the `.github/workflows/deploy.yml` file. The pipeline is triggered on `push` events to the `main` branch

## **4. Kubernetes Manifests for Deployment**
The **Kubernetes manifests** (`k8s/deployment.yaml` and `k8s/service.yaml`) describe the resources for deploying the Flask application to the Kubernetes cluster. These include the configuration for **pods**, **services**, and **replicas**.

**deployment.yaml** and **service.yaml**

Applying the Kubernetes Manifests:
Once the manifests are prepared, apply them to your Kubernetes cluster using kubectl:

Deploy the application:

kubectl apply -f k8s/deployment.yaml
Expose the service:

kubectl apply -f k8s/service.yaml

## **5. Monitoring Setup with Prometheus and Grafana**

Prometheus and Grafana are deployed via Helm to monitor the application:

Prometheus collects application metrics.

Grafana visualizes these metrics in real-time on a dashboard.

The GitHub Actions pipeline installs Prometheus and Grafana on the Kubernetes cluster using the following Helm commands:

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace

helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana grafana/grafana --namespace monitoring

## **6. Accessing Grafana Dashboard**
After deploying Grafana, access the dashboard to monitor the application metrics

**Retrieve the admin password for Grafana:**

kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

**Access Grafana via port-forwarding:**

kubectl port-forward --namespace monitoring service/grafana 3000:80
Open http://localhost:3000 in your browser and log in with the admin password.

helm install grafana grafana/grafana --namespace monitoring
Configure Prometheus to Monitor the Application
Once Prometheus and Grafana are installed, Prometheus automatically starts scraping metrics from all services in the Kubernetes cluster.


## **Conclusion**
This project demonstrates a full DevOps workflow, from infrastructure provisioning with Terraform to application deployment with Kubernetes, and continuous monitoring using Prometheus and Grafana. It highlights the importance of automation and monitoring in the modern software development lifecycle.
