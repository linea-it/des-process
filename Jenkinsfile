pipeline {
	environment {
		registry = "des_process"
		registryCredential = 'Dockerhub'
		dockerImage = ''
	}

  agent any

  stages {
    stage('Deploy to Staging') {
      when {
        branch "master"
      }
      steps {
        echo "deploying"
      }
    }
  }
}