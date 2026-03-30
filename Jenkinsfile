pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
    }

    stages {
        stage('Setup') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                bat 'python -m pytest -m unit'
            }
        }

        stage('Integration Tests') {
            steps {
                bat 'python -m pytest -m integration'
            }
        }
    }
}