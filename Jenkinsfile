pipeline {
    agent {
        docker {
            image 'python:3.9-slim-buster'
        }
    }
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my_image -f ./Flask_App_With_Jenkins/Dockerfile .'
            }
        }
        stage('Push Docker Image to ECR') {
            steps {
                sh '$(aws ecr get-login --no-include-email --region us-east-1)'
                sh 'docker tag my_image 420493635762.dkr.ecr.us-east-1.amazonaws.com/matan_app:$BUILD_NUMBER'
                sh 'docker push 420493635762.dkr.ecr.us-east-1.amazonaws.com/matan_app:$BUILD_NUMBER'
            }
        }
    }
}
