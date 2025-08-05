# 🚀 Jenkins CI/CD Pipeline for Flask App

---

## 📌 Overview

This project demonstrates a fully automated Jenkins pipeline that builds, deploys, and runs a simple Flask web application inside Docker. The pipeline is triggered automatically on every code push to the GitHub repository, showcasing core DevOps automation concepts using Jenkins and Docker.

The pipeline stages include:

- Cloning the GitHub repo  
- Building a Docker image of the Flask app  
- Running the app container on port 5000  

This task helped solidify foundational skills in Jenkins pipeline creation, Docker containerization, and automated deployment.

---

## 🛠️ Tech Stack

| Tool/Platform | Purpose                      |
|---------------|------------------------------|
| Jenkins       | CI/CD automation server       |
| Docker        | Containerization and deployment|
| Flask (Python)| Simple web app framework      |
| GitHub        | Source code repository        |
| ngrok         | Local tunneling for webhook   |

---

## ⚙️ How It Works

1. **Edit code** in your local repo (`app.py`, `Jenkinsfile`, `Dockerfile`).  
2. **Push changes** to GitHub `master` branch.  
3. Jenkins **detects the push via webhook** and triggers the pipeline.  
4. Pipeline stages run sequentially:  
    - Clone code  
    - Build Docker image  
    - Run Docker container  
5. The Flask app becomes accessible at `http://<jenkins-host>:5000`  

---

 

## 🧪 Local Setup & Testing

### Run Flask app locally (optional)

```bash
python app.py
````

Visit: `http://localhost:5000` to verify the app works before containerizing.

### Run Docker container manually

```bash
docker build -t jenkins-pipeline-demo .
docker run -d -p 5000:5000 --rm --name jenkins-demo jenkins-pipeline-demo
```

 

---

## 🔄 GitHub Webhook Setup for Auto Build Trigger

To enable Jenkins to trigger builds automatically on code pushes:

1. Expose your Jenkins server URL publicly or use **ngrok** to create a tunnel:

```bash
ngrok http 8080
```

2. Copy the **ngrok public URL**, e.g., `https://1234abcd.ngrok.io`.

3. Go to your GitHub repository → **Settings** → **Webhooks** → **Add webhook**.

4. Enter the payload URL:

```
https://1234abcd.ngrok.io/github-webhook/
```

5. Select **application/json** as the content type.

6. Choose **Just the push event**.

7. Save the webhook.

Now, whenever you push code, GitHub sends a notification to Jenkins, which triggers the pipeline build automatically.

---

## 📁 Project Structure

```
jenkins-pipeline-DevopsTask2/
├── app.py          # Flask app serving a simple "Hello from Jenkins Pipeline!" message
├── Dockerfile      # Containerizes Flask app with Python 3.8-slim
├── Jenkinsfile     # Declarative Jenkins pipeline script for CI/CD automation
└── README.md       # Project documentation and instructions
```

---

## 📷 Visual Walkthrough

<details>
<summary>Click to expand screenshots</summary>

1. **Jenkins Pipeline Setup**
   ![jenkins-setup](./screenshots/jenkins-setup.png)

2. **Pipeline Running and Console Output**
   ![jenkins-console](./screenshots/jenkins-console.png)

3. **Docker Image Built Successfully**
   ![docker-image](./screenshots/docker-image.png)

4. **Flask App Running in Container**
   ![flask-app](./screenshots/flask-app.png)

5. **GitHub Webhook Setup**
   ![github-webhook](./screenshots/github-webhook.png)

6. **ngrok Tunnel Running**
   ![ngrok-tunnel](./screenshots/ngrok-tunnel.png)

</details>

---

## 🔒 Security & Credentials

* SSH keys are used to authenticate Jenkins with GitHub securely.
* Jenkins server needs access to Docker daemon (mounted socket).
* ngrok used to expose Jenkins webhook URL during development.

---

## 🧠 What I Learned

* Creating declarative Jenkins pipelines to automate builds and deployments
* Integrating Docker container workflows within Jenkins pipelines
* Configuring GitHub webhooks for automatic CI/CD triggering
* Managing Jenkins credentials and Docker socket permissions
* Troubleshooting Docker container lifecycle and pipeline failures

---

## 📚 Task Checklist

* [x] Jenkins installed and running with Docker support
* [x] Created Flask app and Dockerfile
* [x] Wrote Jenkinsfile with pipeline stages (clone, build, run)
* [x] Configured GitHub webhook for automated builds
* [x] Pipeline runs successfully and deploys app
* [x] Documented project with clear README and screenshots

---
