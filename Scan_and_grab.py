import socket

#Create a socket connection
scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Take input from the user to adjust to their needs
#Input for ports are converted from str to int
meta = input("Please input the IP address of your target: ")
p1 = int(input("Please input what port you would like the scan to start at: "))
p2 = int(input("Please input what port you would like the scan to end at: "))

#create scanandgrab & define what this function will do when called
#Insert and try and except to differentiate the status of ports (open or closed)
#Lines 10-14 will scan each port specified below and return a value for each port
def scanandgrab(port):
    try:
        scan.connect((meta, port))
        return True
    except:
        return False

print("Scanning is in progress, please wait...")

#For statement to identify what ports will be scanned
#If will report that a port is open and print the statement
#Else will ensure the program does not print anything if the port is closed
for x in range (19,26):
    if scanandgrab(x):
        print("Port", x, "is open!")
    else:
        pass