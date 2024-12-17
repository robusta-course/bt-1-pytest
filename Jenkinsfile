pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                withPythonEnv('Python3') {
                    sh '''
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest tests/'
                }
            }
        }
    }
}
