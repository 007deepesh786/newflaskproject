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
sh "Docker build -t deepesh0786/newflaskapp"
}
else{
bat "Docker build -t deepesh0786/newflaskapp"
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
}
}