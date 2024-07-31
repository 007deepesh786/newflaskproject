pipeline {
agent any

stages {
stage('Docker Build') {
steps {
// Get some code from a GitHub repository
git url: 'https://github.com/007deepesh786/newflaskproject.git'

// Run Maven on a Unix agent.
script{
if(isUnix()){
sh "Docker build -t deepesh0786/newflaskapp ."
}
else{
bat "Docker build -t deepesh0786/newflaskapp ."
}
}
}
}



stage('Integration Test') {
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
    stage('Docker Push') {
            steps {
               withCredentials([usernamePassword(credentialsId:'dockerHub',passwordVariable: 'dockerHubPassword',usernameVariable:'dockerHubUser')]){
                bat "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                bat "docker push deepesh0786/newflaskapp:latest"
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
}
}