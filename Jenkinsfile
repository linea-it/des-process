pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
    stage('Check Python') {
      steps {
        sh 'python --version'
      }
    }
    stage('Virtual ENV') {
      steps {
        sh 'python -m venv env'
        sh '. ./env/bin/activate'
        sh 'ls -lah'
      }
    }
    stage('Installing dependencies') {
      steps {
        withDockerContainer(image: 'python:3.6.9', args:'-u root:root'){
          sh 'pip install --user requests pycodestyle snapshottest coverage pytest pytest-cov'
        }
      }
    }
    stage('Check lint') {
      steps {
        sh 'cd des_process'
        sh 'python -m pycodestyle .'
      }
    }
    stage('Check testing') {
      steps {
        sh 'python -m pytest'
      }
    }
    stage('Check coverage') {
      steps {
        sh 'python -m coverage report'
        sh 'python -m coverage html'
      }
    }
  }
}
