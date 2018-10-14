import socket

x = raw_input ("\n Press enter to resolve your hostname / IP or Please type the domain that you wish to do IP attribution on: ")  

data = socket.gethostbyname_ex(x)
print ("\n\nThe IP Address of the Domain Name is: "+repr(data))  

x = raw_input("\nPress enter to exit this progam\n")  
if x == '1':   
    execfile('C:\python\main_menu.py')  
