pipeline {
    agent any
    parameters {
        string(defaultValue: 'watermark file name', 
            description: 'Please enter the watermark file name', 
            name: 'WaterMark', 
            trim: false)
    }
    stages {
        stage ('clean workspace') {
            steps {
                cleanWs()
            }
        }

        stage ('checkout the repo') {
            steps {
                checkout([$class: 'GitSCM', 
                branches: [[name: '*/uat_br']], 
                extensions: [], 
                userRemoteConfigs: [[credentialsId: 'OraHub_epact', 
                url: 'https://orahub.oci.oraclecorp.com/epact/epact-releaseautomation.git']]])
            }
        }

        /*stage ('Water mark Generation') {
            steps {
                sh 'ansible-playbook -i "${WORKSPACE}"/Ansible/inventory "${WORKSPACE}"/Ansible/watermark_creation.yaml'
            }
        }*/

        stage ('Migration to DEV Environement') {
            steps {
                sh 'ansible-playbook "${WORKSPACE}"/Ansible/migration.yaml --extra-vars "watermark_file="${WaterMark}"" -i "${WORKSPACE}"/Ansible/inventory'
            }
        }
    }
}
