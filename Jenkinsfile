pipeline {
agent any

stages {
stage('Build') {
steps {
// Get some code from a GitHub repository
git url: 'https://github.com/007deepesh786/newflaskproject.git'

// Run Maven on a Unix agent.
script{
if(isUnix()){
sh "pip3 install -r requirements.txt"
}
else{
bat "pip install -r requirements.txt"
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