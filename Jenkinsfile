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
        sh 'ls -la'
        sh 'pip install requests --user'
        sh 'pip install pycodestyle --user'
        sh 'pip install snapshottest --user'
        //sh 'pip install coverage --user'
        sh 'pip install pytest --user'
        //sh 'pip install pytest-cov --user'
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
    //stage('Check coverage') {
      //steps {
        //sh 'coverage report'
        //sh 'coverage html'
      //}
    //}
  }
}
