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

        stage('Clean old container') {
            steps {
                script {
                    def containerExists = sh (
                        script: "docker ps -a -q -f name=jenkins-demo",
                        returnStdout: true
                    ).trim()

                    if (containerExists) {
                        echo "Removing existing container with ID: ${containerExists}"
                        sh "docker rm -f jenkins-demo"
                    } else {
                        echo "No existing container named jenkins-demo found."
                    }
                }
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
