========================================================
# Installing Ansible
https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html#installing-ansible-on-ubuntu
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible

--------------------------------------------------------
# Ad-hoc commands in Ansible are quick, one-line commands that you run from the terminal to perform simple tasks without creating full playbooks.
They're handy for tasks you want to do on-the-fly without writing a playbook.

ansible [targets] -m [module] -a "[module_arguments]" -i [inventory_file]

targets: Specifies the host or group of hosts you want to target.
module: Defines the action you want to perform (e.g., ping, command, shell).
module_arguments: Additional options or parameters for the module.

ansible server1 -i inventory -m ping
ansible all -i inventory -m ping

# если user, passwd не указаны в inventory:
ansible all -i hosts -m ping -u den --ask-pass 

ansible all -m command -a "ls /etc"
ansible all -m copy -a "src=/path/to/local/file.txt dest=/path/on/remote/"

# Use the -l option to target specific hosts or groups:
ansible -l web_servers -m command -a "uptime"

ansible -l db_server1 -m command -a "mkdir /{{db_data_directory}}"

# If a task requires elevated privileges, use -b for become (similar to sudo):
ansible all -b -m yum -a "name=httpd state=latest"

--------------------------------------------------------
# inventory:
apache ansible_host=192.168.0.19 ansible_user=den ansible_password=4563

# to reboot remote host:
ansible apache -m command -a "/sbin/reboot" -i hosts --become --ask-become-pass
ansible apache -i hosts -m ping

# update host:
ansible nginx-servers -i hosts -m apt -a "update_cache=true" -b --as
k-become-pass

# install apache2 (present is default value):
ansible apache -i hosts -m apt -a "name=apache2 state=present" -b --
ask-become-pass

# check latesr varsion apache2 installed:
ansible apache -i hosts -m apt -a "name=apache2 state=latest" -b --
ask-become-pass

# remove apache2 from host:
ansible apache -i hosts -m apt -a "name=apache2 state=absent" -b --ask-become-pass

-------------------------------------------------------
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html#parameter-state
# inventory:
[apache-servers]
apache ansible_host=192.168.0.19 ansible_user=den ansible_password=4563

[nginx-servers]
node1 ansible_host=192.168.0.21
node2 ansible_host=192.168.0.22

ansible nginx-servers -i hosts -m apt -a "name=nginx state=latest" -b --ask-become-pass
ansible all -i hosts -m apt -a "name=nginx state=latest" -b --ask-become-pass
--------------------------------------------------------

# variables in host_vars have most priority than group_vars


















