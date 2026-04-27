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
                    url: 'https://github.com/HrishikeshWadile/feedback-app'
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
                sh '''
                echo "Waiting for app to start..."
                sleep 5

                for i in {1..10}; do
                curl -f http://localhost:5000 && exit 0
                echo "Retrying in 3s..."
                sleep 3
                done

                echo "App failed to respond"
                exit 1
                '''
            }
        }
    }
}