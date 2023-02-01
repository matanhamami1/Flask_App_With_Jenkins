Deploying a Flask App with Jenkins 

 

Objective: To gain hands-on experience with creating a repository, building a single file Flask app, and automating the deployment process using Jenkins. 

 

Steps: 

Create a new repository on Github and clone it locally. 

Create a single file Flask app that displays a "Hello World" message when querying it. 

Push the Flask app to the Github repository. 

Use the existing Jenkins server you have or create a new Jenkins server. 

Create an AWS EC2 instance and install Docker on it. 

Create an AWS ECR to which you will upload the Docker images. 

Create a new Jenkins pipeline that checks out the Github repository and builds the Flask app as a Docker image and pushes it to AWS ECR. 

Add a step to the pipeline that deploys the Docker image containing the Flask app. 

Push changes to the Github repository and verify that the Jenkins pipeline automatically builds and deploys the Flask app as a Docker container on the EC2 instance. 

Note: 

The pipeline should run each time changes are pushed to the master branch. 

Ensure the Jenkins instance has the necessary permissions to access the Github repository and deploy the Flask app. 
