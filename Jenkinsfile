pipeline {
  
  environment {
    registry = "567935704451.dkr.ecr.us-east-1.amazonaws.com/inadev"
  }
  
  agent any
  
  stages {

    stage('Checkout Source') {
      steps {
        git branch: "main",
        url: 'https://github.com/ps895r/inadev-weather.git'
      }
    }
    
    stage('Security and Code Quality Checks') {
      steps {
        echo "Add in SonarQube scanning later"
      }
    }
    
    stage('Build') {
      steps {
        echo "building"
        script {
          dockerImage = docker.build(registry + ":$BUILD_NUMBER", "-f Dockerfile .")
        }
      }
    }
    stage('Push Image') {
      steps {
        docker.withRegistry( '567935704451.dkr.ecr.us-east-1.amazonaws.com/inadev', 'ecr:us-east-2:bot-jenkins-vid-inadev' )
        dockerImage.push("${env.Build_NUMBER}")
        dockerImage.push("latest")
      }
    }
    stage('Deploy') {
      steps {
        echo "deploying"
      }
    }
  }
}
