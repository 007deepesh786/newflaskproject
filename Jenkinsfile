pipeline {
    agent any


stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git url: 'https://github.com/krishnamurthypradeep/newflaskproject.git'

                // Run Maven on a Unix agent.
                script{
                if(isUnix()){
                sh "pip3 install -r requirements.txt"
				}
                else{
                 bat "pip3 install -r requirements.txt"
                 }
                 }
            }
            }



         stage('Unit Test') {
            steps {

                // Run Maven on a Unix agent.
                script{
                if(isUnix()){
                sh "pytest"
				}
                else{
                 bat "pytest"
                 }
                 }
            }

    	}

    	stage('Docker Build') {
            steps {
                script{
                if(isUnix()){
                sh "docker build -t deepesh0786/newflaskapp:latest ."
                }
                else{
                 bat "docker build -t deepesh0786/newflaskapp:latest ."
                 }
                 }

            }
        }

        stage('Docker Push') {
            steps {
               withCredentials([usernamePassword(credentialsId:'dockerHub',passwordVariable: 'dockerHubPassword',usernameVariable:'dockerHubUser')]){
                bat "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                bat "docker push deepesh0786/newflaskapp:latest"
                }


            }
    }

    stage('Kubernetes Pod') {

    steps {
                script{
 if (isUnix()){

 sh "kubectl apply -f deployment.yaml"
 } else {
 bat("kubectl apply -f deployment.yaml")
 }
                }
    }

 }

 stage('Kubernetes Service') {

    steps {
                script{
 if (isUnix()){

 sh "kubectl apply -f service.yaml"
 } else {
 bat("kubectl apply -f service.yaml")
 }
                }
    }

 }

    
    }
   }