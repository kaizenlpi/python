#!/usr/bin/env python3

import os

filename = input("Enter filename containing list of usernames to delete: ")

# Check if file exists
if not os.path.isfile(filename):
    print(f"Error: File {filename} not found")
    exit(1)

# Loop through file and delete users
with open(filename) as f:
    for username in f:
        username = username.strip()  # Remove newline characters
        try:
            os.system(f"sudo userdel -fr {username}")
            print(f"User {username} deleted")
        except:
            print(f"Error deleting user {username}")
        # To Do: use this code if you didn't include the -fr options for userdel
        try:
            os.system(f"sudo rm -fr {username}")
            print(f"User {username} deleted")
        except:
            print(f"Error deleting user's home directory {username}")
