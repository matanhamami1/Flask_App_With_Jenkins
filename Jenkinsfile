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
                sh 'container_id=$(sudo docker ps -a -q --filter ancestor=my_image --format="{{.ID}}")'
                sh 'if [ -n "$container_id" ]; then sudo docker stop $container_id; fi'
                sh 'sudo docker run --rm -p 5001:5000 my_image'
            }
        }
    }
}
