# NOTE: mccli is avamar CLI. 

import pexpect
import paramiko
import xml.etree.ElementTree as ET 


#host = "204.67.16.10"
#username = "admin"
#password = "SuperSecretPassword"

#AVAMAR GRIDS
server101="204.25.16.10"
server201="204.25.16.36"
server301="204.25.16.62"
server401="204.25.16.88"
server501="204.25.16.114"

#hostname=["server101","server201","server301","server401","server501"]

gridarray=[server101,server201]

command = "sudo mccli client show --domain=/ --recursive=true --xml"   
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh.connect(hostname='204.67.16.10', username='admin', password='SuperSecretPassword', port=22)
# NOTE: block - for loop runs to connect to each grid, then runs command and captures output before making conncetion to next server
for grid in gridarray:
    print("---starting gridname:"+ grid)
    ssh.connect(hostname=grid, username='uipath', password='Texas123$')
    stdin, stdout, stderr = ssh.exec_command(command)
    tree=ET.parse(stdout)
    root=tree.getroot()
    print(root)
    #lines = stdout.readlines()
    #print(lines)
    lines = stderr.readlines()
    print(stdout) 
    # Assuming to capture output here. 
    #ATTEMPT 1
    #gridData = open('gridoutput.xml', "wb")
    #tree.write(f)
    #ATTEMPT2
    xml_data = "<root>...</root>"
    print(canonicalize(xml_data))
    with open("grid_output.xml", mode='w', encoding='utf-8') as out_file:
        canonicalize(xml_data, out=out_file)
    ssh.close()
    print("---stopping gridname:"+ grid)
