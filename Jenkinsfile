pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                withPythonEnv('python3') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                withPythonEnv('python3') {
                    sh 'python3 -m pytest tests/'
                }
            }
        }
    }
}
