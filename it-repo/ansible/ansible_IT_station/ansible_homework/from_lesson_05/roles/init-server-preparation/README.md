Role Name: init-server-preparation
=========
Role initialy setup remote hosts and does the next ops:
- Makes directory for ssh-keys
- Generates SSH key
- Add key to remote hosts
- Disable root login
- Enforce SSH key passphrases
- Disable password ssh connection
- Restart sshd

Requirements
------------
Ubuntu22.04 is required.

Role Variables
--------------
Into the playbook.yaml:
- local_user: dan  ---  defines local user (on the control node)
Into the defaults:
- ssh_key_filename: "{{inventory_hostname}}_ssh_key"  --- defines name of ssh keys
- ssh_keys_dir: ssh_keys  --- directory name on the control machine for gerated ssh keys
- sshd_config_file: /etc/ssh/sshd_config    ---  default ssh config file path on remote hosts


Dependencies
------------


Example Playbook
----------------


License
-------


Author Information
------------------


