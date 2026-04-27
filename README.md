🚀 Student Feedback Form - DevOps Setup

This project demonstrates a simple Flask-based Student Feedback Form integrated with Docker and Jenkins CI pipeline (Poll SCM + Webhook using ngrok).

📁 Project Structure
student-feedback-form/
│── app.py
│── requirements.txt
│── Dockerfile
│── templates/
│     ├── form.html
│     └── responses.html
│── Jenkinsfile
│── README.md
🔹 1. Run Flask App Locally
Install dependencies
pip install -r requirements.txt
Run application
python app.py
Open in browser
http://localhost:5000
🔹 2. Docker Setup
Build Docker Image
docker build -t feedback-app .
Run Container
docker run -d -p 5000:5000 feedback-app
Verify
http://localhost:5000
🔹 3. Run Jenkins using Docker
Pull Jenkins Image
docker pull jenkins/jenkins:lts
Run Jenkins Container (with Docker access)
Windows (PowerShell)
Use this 👇

docker run -d `
  --name jenkins-container `
  -u root `
  -p 8080:8080 `
  -p 50000:50000 `
  -v jenkins_home:/var/jenkins_home `
  -v //var/run/docker.sock:/var/run/docker.sock `
  jenkins/jenkins:lts

👉 This avoids all syntax issues

🔹 After running

Check:

docker ps

👉 You should see:

jenkins-container
🔹 Then install Docker inside Jenkins
docker exec -u 0 -it jenkins-container bash

Then:

apt update
apt install -y docker.io
exit
Linux / Mac
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins-container \
  jenkins/jenkins:lts
Open Jenkins
http://localhost:8080
Get Initial Admin Password
docker exec jenkins-container cat /var/jenkins_home/secrets/initialAdminPassword
Setup Jenkins
Install suggested plugins
Create admin user
🔹 4. Jenkins CI Pipeline Setup
Create Pipeline Job
Go to New Item → Pipeline
Choose Pipeline script from SCM
Add your GitHub repository URL
Enable Auto Trigger (Choose ONE or BOTH)
✔ Option 1: Poll SCM
Poll SCM
* * * * *
✔ Option 2: Webhook (using ngrok)
🔹 5. Setup ngrok (for Webhook)
Install ngrok

Download from:

https://ngrok.com/download
Add Auth Token (one-time)
ngrok config add-authtoken YOUR_TOKEN
Start ngrok
ngrok http 8080

👉 You will get:

https://your-url.ngrok-free.dev
🔹 6. Configure GitHub Webhook

Go to:

GitHub Repo → Settings → Webhooks → Add Webhook

Fill:

Payload URL:
https://your-url.ngrok-free.dev/github-webhook/

Content type:
application/json

Event:
Just the push event
🔹 7. Enable Webhook in Jenkins

✔ Enable:

GitHub hook trigger for GITScm polling
🔹 8. Jenkinsfile
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'feedback-app'
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Cleanup Old Container') {
            steps {
                sh "docker rm -f ${IMAGE_NAME} || true"
            }
        }

        stage('Run Container') {
            steps {
                sh "docker run -d -p 5000:5000 --name ${IMAGE_NAME} ${IMAGE_NAME}"
            }
        }

        stage('Test') {
            steps {
                sh "curl http://localhost:5000"
            }
        }
    }
}
🔹 9. CI Workflow
Using Poll SCM
GitHub → Jenkins (polls every minute) → Build → Run → Test
Using Webhook
GitHub Push → ngrok → Jenkins → Build → Run → Test
🔹 10. Test Trigger
For Poll SCM
Push code → wait 1 minute
For Webhook
Push code → build triggers instantly 🚀
🔹 11. Test Command
curl http://localhost:5000
✅ Features Demonstrated
Flask Web Application
Docker Containerization
Jenkins CI Pipeline
Poll SCM Automation
Webhook Integration using ngrok
Automated Build & Test
⚠️ Notes
Keep ngrok running during webhook usage
ngrok URL changes on restart → update webhook
Ensure Docker is running before Jenkins
Port 5000 should be free
🎯 Outcome
Code push triggers Jenkins automatically
Docker image is built
Container runs application
Test case executed
Build status shown in Jenkins
🧠 Viva Tip

Poll SCM vs Webhook:

Poll SCM → simple but delayed
Webhook → instant but needs public URL (ngrok)
✅ Final

👉 Works for both Poll SCM + Webhook
👉 Fully exam-ready setup