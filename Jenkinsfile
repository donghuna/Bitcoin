pipeline {
    agent any

    triggers {
        pollSCM('*/3 * * * *')
    }

    stages {
        stage('Prepare') {
            steps {
                echo "Prepare!"

                git url: 'https://github.com/donghuna/Bitcoin.git',
                    branch: 'master',
                    credentialsId: 'jenkinsgit'
            }
        }
        stage('Test') {
            agent any

            steps {
                echo "Prepare!"
            }
        }
        stage('Build') {
            agent any

            steps {
                echo "Prepare!"
            }
        }
    }
}