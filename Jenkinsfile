pipeline {
    agent any
    stages {
        stage('Install Docker') {
            steps {
                echo "hello"
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my_image .'
            }
        }
        stage('Push Docker Image to ECR') {
            steps {
                sh '$(aws ecr get-login --no-include-email --region us-east-1)'
                sh 'docker tag my_image 420493635762.dkr.ecr.us-east-1.amazonaws.com/matan_app:$BUILD_NUMBER'
                sh 'docker push 420493635762.dkr.ecr.us-east-1.amazonaws.com/matan_app:$BUILD_NUMBER'
            }
        }
        stage('Run Docker Image on Remote Server') {
            steps {
                sh 'ssh -o StrictHostKeyChecking=no -T -i ~/devopshome.pem ubuntu@3.86.97.209'
                sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 420493635762.dkr.ecr.us-east-1.amazonaws.com'
                sh 'sudo docker pull 420493635762.dkr.ecr.us-east-1.amazonaws.com/matan_app:$BUILD_NUMBER'
                sh 'sudo docker run -p 5000:5000 420493635762.dkr.ecr.us-east-1.amazonaws.com/matan_app:BUILD_NUMBER'
                
            }
        }
    }
}
