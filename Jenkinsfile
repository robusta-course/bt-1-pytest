pipeline {
    agent { label 'ubuntu-2' }
    stages {
        stage('Install Dependencies') {
            steps {
                withPythonEnv('python3') {
                    sh 'pip install -r requirements.txt'
                    sh 'printenv'
                }
            }
        }
        stage('Run TDD') {
            steps {
                withPythonEnv('python3') {
                    sh 'python3 -m pytest tests/'
                }
            }
        }
        stage('Run BDD') {
            steps {
                withPythonEnv('python3') {
                    sh 'python3 -m behave'
                }
            }
        }
    }
}
