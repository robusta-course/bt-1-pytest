pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                    #sudo apt-get install python3-pip python3.12-venv -y
                    sudo python3 -m venv .env
                    ls -al .env/bin/active
                    . .env/bin/active
                    sudo pip install -r requirements.txt
                    """
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
