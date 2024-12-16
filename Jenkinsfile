pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    apt-get install python3-pip
                    python3 -m venv .env
                    source .env/bin/active
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
