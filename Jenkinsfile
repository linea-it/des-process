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
        sh 'pip install --user requests pycodestyle snapshottest coverage pytest pytest-cov'
        sh 'ls -la'
      }
    }
    stage('Check lint') {
      steps {
        sh 'cd des_process'
        sh 'pycodestyle .'
      }
    }
    stage('Check testing') {
      steps {
        sh 'pytest'
      }
    }
    stage('Check coverage') {
      steps {
        sh 'coverage report'
        sh 'coverage html'
      }
    }
  }
}
