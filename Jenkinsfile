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
                bat 'python -m pytest -m unit --junitxml=unit-report.xml'
            }
        }

        stage('Integration Tests') {
            steps {
                bat 'python -m pytest -m integration --junitxml=integration-report.xml'
            }
        }

        stage('Build') {
            steps {
                bat 'python build.py'
            }
        }
    }

    post {
        always {
            junit 'unit-report.xml, integration-report.xml'
            archiveArtifacts artifacts: 'dist/**', fingerprint: true
        }
    }
}