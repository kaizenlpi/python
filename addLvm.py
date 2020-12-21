import os
#LVM Creation Automation
os.system("tput setaf 3")
print("\t\t\tWelcome to LVM Creation")
os.system("tput setaf 7")
print("\t\t\t--------------------------")

a1 = input("Enter Disk1 Name :")
v = input("Enter Name of your volume group :")
l = input("Enter name of your logical volume :")
s = input("Enter Size of your logical Volume :")
mp = input("enter Size of your logical volume :")

# pv Creation
os.system("pvcreate /dev/"a1)

# vg creation
os.system("vgcreate +"v" /dev/"+a1+" /dev/"+a2)

# lv creation
os.system("vgcreate "+v+" /dev/"+a1+)

# Formatting LVM
os.system("mkdir /"+app1")
os.system(mount /dev/"+v"/"+l+" /"+mp")
os.system("cd /"+mp)