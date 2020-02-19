pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
    stage('Check Python') {
      steps {
        sh 'python --version'
      }
    }
    stage('Install dependencies') {
      steps {
        sh 'python setup.py develop'
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
        sh 'cd des_process'
        sh 'pytest'
      }
    }
    stage('Check coverage') {
      steps {
        sh 'cd des_process'
        sh 'coverage report'
        sh 'coverage html'
      }
    }
  }
}
