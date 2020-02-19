pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
    stage('Check Python') {
      steps {
        sh 'python --version'
      }
    }
    stage('Installing dependencies') {
      steps {
        sh 'sudo pip install --user requests pycodestyle snapshottest coverage pytest pytest-cov'
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
