# to run playbook.yaml:
ansible-playbook playbook1.yaml -i admin/hosts

# при выполнении playbook:
TASK [Gathering Facts] - собирает данные о системе, лучше отключать "gather_facts: no", т.к. занимает время и 
                         включать, когда необходимо получить эти данные
  tasks:
  - name: debug
    debug:
      var: ansible_facts  <--- позволяет увидеть инфу, которую собирает TASK [Gathering Facts]

# отключить gather_facts:
---
- name: First server preparation
  hosts: all
  gather_facts: no          <--------------
  become: no
  vars:
    ssh_key_filename: ssh_admin_key
    ssh_key_location_path: /home/dan/.ssh/

  tasks:
  - name: debug
    debug:
      msg: "no_ansible_facts"     <----вывести сообщение 


