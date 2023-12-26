pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo "building"
        sleep 10
        script {
          sh "su –"
          dockerImage = docker.build("weather" + ":$BUILD_NUMBER", "-f Dockerfile .")
        }
      }
    }
    stage('Test') {
      steps {
        echo "testing"
        sleep 30
      }
    }
    stage('Deploy') {
      steps {
        echo "deploying"
      }
    }
  }
}
