#!/user/bin/python3

# Purpose: This script opens an ssh connection via paramiko module, runs ls, and prints the result to the screen. 
# This was a proof of concept to verify if we could use paramiko to connect to one of the 16 avamar (backup) grid servers.
# Note: The vars below could be used below if the script were to grow. 
# Example Proof of Concept was helpful: https://www.adamsmith.haus/python/answers/how-to-ssh-using-paramiko-in-python
# https://stackoverflow.com/questions/25409977/paramiko-module-object-has-no-attribute-error-sshclient


import pexpect
import paramiko

#host = "204.11.11.111"
#username = "admin"
#password = "adminPW"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='204.11.11.111', username='admin', password='adminPW', port=22)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
ssh.close()
