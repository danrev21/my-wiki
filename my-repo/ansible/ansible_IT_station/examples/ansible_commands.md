ansible-config init > ansible.cfg  # define default config file
ansible-config init --disabled > ansible.cfg


ssh-keygen -R 192.168.0.31
ansible-playbook --check playbook.yaml -l server1
ansible-playbook playbook1.yaml -l server1
ansible-playbook playbook1.yaml -l server1 --key-file ssh_admin_key   ---> after disable ssh connection 

# roles
ansible-galaxy init nginx1                      # creates role tree
ansible-galaxy init nginx1 --init-path ./roles  # creates role tree in specified dir
ansible-galaxy role list -p ./roles/            # list roles

# vault
ansible-vault encrypt vars.yaml
ansible-vault view vars.yaml --vault-pass-file my-pass
ansible-vault edit vars.yaml --vault-pass-file my-pass
ansible-vault decrypt vars.yaml --vault-pass-file my-pass

ansible-playbook playbook.yaml -l ubuntu1 --ask-vault-pass
ansible-playbook playbook.yaml -l ubuntu1 -J                 # the same

ansible-vault encrypt_string vagrant group_vars/all.yaml --vault-pass-file my-pass
ansible-vault encrypt_string
echo -n "secret" | ansible-vault encrypt_string

export ANSIBLE_VAULT_PASSWORD_FILE=$(pwd)/my-pass
ansible-playbook playbook.yaml -l ubuntu1
ansible-vault edit group_vars/all.yaml


