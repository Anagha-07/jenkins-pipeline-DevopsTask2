pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo 'Cloning the code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t jenkins-pipeline-demo .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run -d -p 5000:5000 --rm --name jenkins-demo jenkins-pipeline-demo'
            }
        }
    }
}
