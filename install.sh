#!/bin/bash

sudo apt install ansible
ansible-playbook stage1.yml
ansible-playbook stage2.yml
