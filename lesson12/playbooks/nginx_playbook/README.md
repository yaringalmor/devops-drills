# Setting up nginx app using Ansible
In lesson 12 we're got to know Ansible as a configuration management tool.\
Based on this tool, we'll be able to set nginx custom up on remote host.

## Requirements
- Ansible - [Installation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#pip-install)
- Remote host with ssh port (22) available.


## Setup
1. Apply your remote hosts settings in hosts inventory file - ansible host (ip address) and ssh key path.

## Usage
- For installing nginx prerequisites, simply run the playbook - <br />
`ansible-playbook -i ../../hosts playbook.yaml` <br />
- If you'd like to skip nginx prerequisites installations, apply the tag 'skip_installation'. <br />
`ansible-playbook -i ../../hosts playbook.yaml --tags skip_installation` <br />
- If you'd like to just ensure your app is running, apply the tag 'start_app'. <br />
`ansible-playbook -i ../../hosts playbook.yaml --tags start_app` <br />