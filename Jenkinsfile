pipeline {
    agent any

    environment {
        IMAGE_NAME = 'feedback-app'
    }

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/HrishikeshWadile/feedback-form'
            }
        }

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
                sh "curl -f http://localhost:5000"
            }
        }
    }
}