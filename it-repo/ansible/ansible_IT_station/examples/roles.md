# roles
ansible-galaxy init nginx1                      # creates role tree
ansible-galaxy init nginx1 --init-path ./roles  # creates role tree in specified dir

# prioritet of vars without roles:
- vars in host_vars
- vars in group_vars

# prioritet of role vars:
- vars in main playbook
- vars in roles
- vars in host_vars
- vars in group_vars
- vars in defaults

# in