pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Abdullah-Maneka/Project03.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python -m venv venv'
                    withEnv(['PATH+VENV=venv/bin', 'PYTHON=venv/bin/python']) {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'python -m unittest discover -s tests'
                }
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                echo 'Deploying to production...'
                // Your deployment steps go here
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
