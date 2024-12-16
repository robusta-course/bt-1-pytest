pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                    #sudo apt-get install python3-pip python3.12-venv -y
                    mkdir venv || true
                    sudo python3 -m venv venv
                    ls -al venv/bin/activate
                    . venv/bin/activate
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
