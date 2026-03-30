pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/tahirbalouch113/ci-cd-python-learning.git'
            }
        }

        stage('Setup') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                bat 'pytest -m unit'
            }
        }

        stage('Integration Tests') {
            steps {
                bat 'pytest -m integration'
            }
        }
    }
}