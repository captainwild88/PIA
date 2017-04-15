import os 
import subprocess
import glob
import fileinput
import sys

path = "/etc/openvpn"
ovpn = "sed -i -- 's/auth-user-pass/auth-user-pass password.txt/g' *.ovpn"
cmd = "sudo openvpn " 
new = "sudo apt-get install openvpn"
install = input("Is this a new install? >")



if install == "yes" or install == "y":
    username = input("What is your username >  ")
    password = input("What is you password >  ")
    os.system(new)
    os.chdir(path)
    os.system('sudo unzip openvpn.zip')
    f = open("password.txt", 'w')
    f.write(username + "\n")
    f.write(password + "\n")
    f.close()
    os.system(ovpn)
    

	
else:
	
	os.chdir(path)
	for file in glob.glob("*.ovpn"):
		print(file)
	location = input("copy and paste your location >  ")
	os.system(cmd + location)
