pipeline {
    agent {
        docker {
            image 'python:3.9-slim-buster'
        }
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def app = docker.build("my_image")
                }
            }
        }
        stage('Push Docker Image to ECR') {
            steps {
                script {
                    withAWS(credentials: 'aws-credentials') {
                        def registry = "your_ecr_registry_url"
                        def command = "docker push ${registry}:${env.BUILD_NUMBER}"
                        sh command
                    }
                }
            }
        }
    }
}
