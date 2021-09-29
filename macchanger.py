import subprocess

#first you must know name of Wireless adapter, just type ifconfig ...


print("Create by Cunoo\n if yo \nShutdown Wireless adapter... \n")
subprocess.call(["sudo", "ifconfig", "enter name of wireless adapter", "down"])

macadress = input("please write macadress thanks: \n")
subprocess.call(["sudo", "ifconfig", "enter name of wireless adapter", "hw", "ether", macadress])

subprocess.call(["sudo", "ifconfig", "enter name of wireless adapter", "up"])

